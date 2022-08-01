"""
Uses Python's interface from https://github.com/banteg/multicall.py.git for MakerDAO's multicall contract.
Multicall contract helps reduce node calls by combining contract function calls
and returning the values all together. This is helpful especially if API nodes like Infura are being used.
"""
import asyncio
import math
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from clamfig.base import Registry
from eth_abi import decode_single
from multicall import Call
from multicall import Multicall
from multicall import multicall
from multicall.constants import MULTICALL2_ADDRESSES
from multicall.constants import MULTICALL_ADDRESSES
from multicall.constants import Network
from telliot_core.tellor.tellorflex.autopay import TellorFlexAutopayContract
from telliot_core.utils.response import error_status
from telliot_core.utils.timestamp import TimeStamp
from web3.main import Web3

from telliot_feeds.feeds import CATALOG_FEEDS
from telliot_feeds.queries.query_catalog import query_catalog
from telliot_feeds.utils.log import get_logger

logger = get_logger(__name__)

# add testnet support for multicall that aren't avaialable in the package
Network.Mumbai = 80001
MULTICALL_ADDRESSES[Network.Mumbai] = MULTICALL2_ADDRESSES[
    Network.Mumbai
] = "0x35583BDef43126cdE71FD273F5ebeffd3a92742A"
Network.ArbitrumRinkeby = 421611
MULTICALL_ADDRESSES[Network.ArbitrumRinkeby] = MULTICALL2_ADDRESSES[
    Network.ArbitrumRinkeby
] = "0xf609687230a65E8bd14caceDEfCF2dea9c15b242"
Network.OptimismKovan = 69
MULTICALL_ADDRESSES[Network.OptimismKovan] = MULTICALL2_ADDRESSES[
    Network.OptimismKovan
] = "0xf609687230a65E8bd14caceDEfCF2dea9c15b242"


async def run_in_subprocess(coro: Any, *args: Any, **kwargs: Any) -> Any:
    """Use ThreadPoolExecutor to execute tasks"""
    return await asyncio.get_event_loop().run_in_executor(ThreadPoolExecutor(16), coro, *args, **kwargs)


# Multicall interface uses ProcessPoolExecutor which leaks memory and breaks when used for the tip listener
# switching to use ThreadPoolExecutor instead seems to fix that
multicall.run_in_subprocess = run_in_subprocess

# Mapping of queryId to query tag for supported queries
CATALOG_QUERY_IDS = {query_catalog._entries[tag].query.query_id: tag for tag in query_catalog._entries}


@dataclass
class Tag:
    query_tag: str
    feed_id: str


@dataclass
class FeedDetails:
    """Data types for feed details contract response"""

    reward: int
    balance: int
    startTime: int
    interval: int
    window: int
    priceThreshold: int
    feedsWithFundingIndex: int


class AutopayCalls:
    def __init__(self, autopay: TellorFlexAutopayContract, catalog: Dict[bytes, str] = CATALOG_QUERY_IDS):
        self.autopay = autopay
        self.w3: Web3 = autopay.node._web3
        self.catalog = catalog

    async def get_current_feeds(self, require_success: bool = True) -> Any:
        """
        Getter for:
        - feed ids list for each query id in catalog
        - a report's timestamp index from oracle for current timestamp and three months ago
        (used for getting all timestamps for the past three months)

        Reason of why three months: reporters can't claim tips from funded feeds past three months
        getting three months of timestamp is useful to determine if there will be a balance after every eligible
        timestamp claims a tip thus draining the feeds balance as a result

        Return:
        - {'tag': (feed_id_bytes,), ('tag', 'current_time'): index_at_timestamp,
        ('tag', 'three_mos_ago'): index_at_timestamp}
        """
        calls = []
        current_time = TimeStamp.now().ts
        three_mos_ago = current_time - 7889238  # 3 months in seconds
        for query_id, tag in self.catalog.items():
            if "legacy" in tag or "spot" in tag:
                calls.append(
                    Call(
                        self.autopay.address,
                        ["getCurrentFeeds(bytes32)(bytes32[])", query_id],
                        [[tag, None]],
                    )
                )
                calls.append(
                    Call(
                        self.autopay.address,
                        ["getIndexForDataBefore(bytes32,uint256)(bool,uint256)", query_id, current_time],
                        [["disregard_boolean", None], [(tag, "current_time"), None]],
                    )
                )
                calls.append(
                    Call(
                        self.autopay.address,
                        ["getIndexForDataBefore(bytes32,uint256)(bool,uint256)", query_id, three_mos_ago],
                        [["disregard_boolean", None], [(tag, "three_mos_ago"), None]],
                    )
                )
        multi_call = Multicall(calls=calls, _w3=self.w3, require_success=require_success)
        data = await multi_call.coroutine()
        # remove status boolean thats useless here
        try:
            data.pop("disregard_boolean")
        except KeyError as e:
            msg = f"No feeds returned by multicall, KeyError: {e}"
            logger.warning(msg)
        return data

    async def get_feed_details(self, require_success: bool = True) -> Any:
        """
        Getter for:
        - timestamps for three months of reports to oracle using queryId and index
        - feed details of all feedIds for every queryId
        - current values from oracle for every queryId in catalog (used to determine
        can submit now in eligible window)

        Return:
        - {('current_feeds', 'tag', 'feed_id'): [feed_details], ('current_values', 'tag'): True,
        ('current_values', 'tag', 'current_price'): float(price),
        ('current_values', 'tag', 'timestamp'): 1655137179}
        """

        current_feeds = await self.get_current_feeds()

        if not current_feeds:
            logger.info("No available feeds")
            return None

        # separate items from current feeds
        # create dict of tag and feed_id in current_feeds
        tags_with_feed_ids = {
            tag: feed_id for tag, feed_id in current_feeds.items() if type(tag) != tuple if len(current_feeds[tag]) > 0
        }
        idx_current = []  # indices for every query id reports' current timestamps
        idx_three_mos_ago = []  # indices for every query id reports' three months ago timestamps
        tags = []  # query tags from catalog
        for key in current_feeds:
            if type(key) == tuple and key[0] in tags_with_feed_ids:
                if key[1] == "current_time":
                    idx_current.append(current_feeds[key])
                    tags.append((key[0], tags_with_feed_ids[key[0]]))
                else:
                    idx_three_mos_ago.append(current_feeds[key])

        merged_indices = list(zip(idx_current, idx_three_mos_ago))
        merged_query_idx = dict(zip(tags, merged_indices))

        get_timestampby_query_id_n_idx_call = [
            Call(
                self.autopay.address,
                [
                    "getTimestampbyQueryIdandIndex(bytes32,uint256)(uint256)",
                    query_catalog._entries[tag].query.query_id,
                    idx,
                ],
                [[(tag, idx), None]],
            )
            for (tag, _), (end, start) in merged_query_idx.items()
            for idx in range(start, end)
        ]

        def _to_list(val: Any) -> List[Any]:
            """Helper function, converts feed_details from tuple to list"""
            return list(val)

        get_data_feed_call = [
            Call(
                self.autopay.address,
                ["getDataFeed(bytes32)((uint256,uint256,uint256,uint256,uint256,uint256,uint256))", feed_id],
                [[("current_feeds", tag, feed_id.hex()), _to_list]],
            )
            for tag, feed_ids in merged_query_idx
            for feed_id in feed_ids
        ]
        get_current_values_call = [
            Call(
                self.autopay.address,
                ["getCurrentValue(bytes32)(bool,bytes,uint256)", query_catalog._entries[tag].query.query_id],
                [
                    [("current_values", tag), None],
                    [("current_values", tag, "current_price"), self._current_price],
                    [("current_values", tag, "timestamp"), None],
                ],
            )
            for tag, _ in merged_query_idx
        ]
        calls = get_data_feed_call + get_current_values_call + get_timestampby_query_id_n_idx_call
        multi_call = Multicall(calls=calls, _w3=self.w3, require_success=require_success)
        feed_details = await multi_call.coroutine()

        return feed_details

    async def reward_claim_status(self, require_success: bool = True) -> Any:
        """
        Getter that checks if a timestamp's tip has been claimed
        """
        feed_details_before_check = await self.get_feed_details()
        if not feed_details_before_check:
            logger.info("No feeds balance to check")
            return None
        # create a key to use for the first timestamp since it doesn't have a before value that needs to be checked
        feed_details_before_check[(0, 0)] = 0
        timestamp_before_key = (0, 0)

        feeds = {}
        current_values = {}
        for i, j in feed_details_before_check.items():
            if "current_feeds" in i:
                feeds[i] = j
            elif "current_values" in i:
                current_values[i] = j

        reward_claimed_status_call = []
        for _, tag, feed_id in feeds:
            details = FeedDetails(*feeds[(_, tag, feed_id)])
            for keys in list(feed_details_before_check):
                if "current_feeds" not in keys and "current_values" not in keys:
                    if tag in keys:
                        is_first = _is_timestamp_first_in_window(
                            feed_details_before_check[timestamp_before_key],
                            feed_details_before_check[keys],
                            details.startTime,
                            details.window,
                            details.interval,
                        )
                        timestamp_before_key = keys
                        if is_first:
                            reward_claimed_status_call.append(
                                Call(
                                    self.autopay.address,
                                    [
                                        "getRewardClaimedStatus(bytes32,bytes32,uint256)(bool)",
                                        bytes.fromhex(feed_id),
                                        query_catalog._entries[tag].query.query_id,
                                        feed_details_before_check[keys],
                                    ],
                                    [[(tag, feed_id, feed_details_before_check[keys]), None]],
                                )
                            )

        multi_call = Multicall(calls=reward_claimed_status_call, _w3=self.w3, require_success=require_success)
        data = await multi_call.coroutine()

        return feeds, current_values, data

    async def get_current_tip(self, require_success: bool = False) -> Any:
        """
        Return response from autopay getCurrenTip call.
        Default value for require_success is False because AutoPay returns an
        error if tip amount is zero.
        """
        calls = [
            Call(self.autopay.address, ["getCurrentTip(bytes32)(uint256)", query_id], [[self.catalog[query_id], None]])
            for query_id in self.catalog
        ]
        multi_call = Multicall(calls=calls, _w3=self.w3, require_success=require_success)
        data = await multi_call.coroutine()

        return data

    def _current_price(self, *val: Any) -> Any:
        """
        Helper function to decode price value from oracle
        """
        if len(val) > 1:
            if val[1] == b"":
                return val[1]
            return Web3.toInt(hexstr=val[1].hex()) / 1e18
        return Web3.toInt(hexstr=val[0].hex()) / 1e18 if val[0] != b"" else val[0]


async def get_feed_tip(query: bytes, autopay: TellorFlexAutopayContract) -> Optional[int]:
    """
    Get total tips for a query id with funded feeds

    - query: if the query exists in the telliot queries catalog then input should be the query id,
    otherwise input should be the query data for newly generated ids in order to determine if submission
    for the query is supported by telliot
    """
    if not autopay.connect().ok:
        msg = "can't suggest feed, autopay contract not connected"
        error_status(note=msg, log=logger.critical)
        return None
    try:
        single_query = {query: CATALOG_QUERY_IDS[query]}
    except KeyError:
        qtype_name, _ = decode_single("(string,bytes)", query)
        if qtype_name not in Registry.registry:
            logger.warning(f"Unsupported query type: {qtype_name}")
            return None
        else:
            query = Web3.keccak(query)
            CATALOG_QUERY_IDS[query] = query.hex()
            single_query = {query: CATALOG_QUERY_IDS[query]}
    except Exception as e:
        msg = f"Error fetching feed tips for query id: {query.hex()}"
        error_status(note=msg, log=logger.warning, e=e)
        return None

    autopay_calls = AutopayCalls(autopay, catalog=single_query)
    feed_tips = await get_continuous_tips(autopay, autopay_calls)
    if feed_tips is None:
        tips = 0
        msg = "No feeds available for query id"
        logger.warning(msg)
        return tips
    tips = feed_tips[CATALOG_QUERY_IDS[query]]
    return tips


async def get_one_time_tips(
    autopay: TellorFlexAutopayContract,
) -> Any:
    """
    Check query ids in catalog for one-time-tips and return query id with the most tips
    """
    one_time_tips = AutopayCalls(autopay=autopay, catalog=CATALOG_QUERY_IDS)
    return await one_time_tips.get_current_tip()


async def get_continuous_tips(autopay: TellorFlexAutopayContract, tipping_feeds: Any = None) -> Any:
    """
    Check query ids in catalog for funded feeds, combine tips, and return query id with most tips
    """
    if tipping_feeds is None:
        tipping_feeds = AutopayCalls(autopay=autopay, catalog=CATALOG_QUERY_IDS)
    response = await tipping_feeds.reward_claim_status()
    if not response:
        logger.info("No feeds to check")
        return None
    current_feeds, current_values, claim_status = response
    # filter out feeds that don't have a remaining balance after accounting for claimed tips
    current_feeds = _remaining_feed_balance(current_feeds, claim_status)
    # remove "current_feeds" word from tuple key in current_feeds dict to help when checking
    # current_values dict for corresponding current values
    current_feeds = {(key[1], key[2]): value for key, value in current_feeds.items()}
    values_filtered = {}
    for key, value in current_values.items():
        if len(key) > 2:
            values_filtered[(key[1], key[2])] = value
        else:
            values_filtered[key[1]] = value
    return await _get_feed_suggestion(current_feeds, values_filtered)


async def autopay_suggested_report(
    autopay: TellorFlexAutopayContract,
) -> Tuple[Optional[str], Any]:
    """
    Gets one-time tips and continuous tips then extracts query id with the most tips for a report suggestion

    Return: query id, tip amount
    """
    chain = autopay.node.chain_id
    if chain in (137, 80001, 69, 1666600000, 1666700000, 421611):
        assert isinstance(autopay, TellorFlexAutopayContract)
        # get query_ids with one time tips
        singletip_dict = await get_one_time_tips(autopay)
        # get query_ids with active feeds
        datafeed_dict = await get_continuous_tips(autopay)

        # remove none type from dict
        single_tip_suggestion = {}
        if singletip_dict is not None:
            single_tip_suggestion = {i: j for i, j in singletip_dict.items() if j}

        datafeed_suggestion = {}
        if datafeed_dict is not None:
            datafeed_suggestion = {i: j for i, j in datafeed_dict.items() if j}

        # combine feed dicts and add tips for duplicate query ids
        combined_dict = {
            key: _add_values(single_tip_suggestion.get(key), datafeed_suggestion.get(key))
            for key in single_tip_suggestion | datafeed_suggestion
        }
        # get feed with most tips
        tips_sorted = sorted(combined_dict.items(), key=lambda item: item[1], reverse=True)  # type: ignore
        if tips_sorted:
            suggested_feed = tips_sorted[0]
            return suggested_feed[0], suggested_feed[1]
        else:
            return None, None
    else:
        return None, None


async def _get_feed_suggestion(feeds: Any, current_values: Any) -> Any:
    """
    Calculates tips and checks if a submission is in an eligible window for a feed submission
    for a given query_id and feed_ids

    Return: a dict tag:tip amount
    """
    current_time = TimeStamp.now().ts
    query_id_with_tips = {}

    for query_tag, feed_id in feeds:  # i is (query_id,feed_id)
        if feeds[(query_tag, feed_id)] is not None:  # feed_detail[i] is (details)
            try:
                feed_details = FeedDetails(*feeds[(query_tag, feed_id)])
            except TypeError:
                msg = "couldn't decode feed details from contract"
                continue
            except Exception as e:
                msg = f"unknown error decoding feed details from contract: {e}"
                continue

        if feed_details.balance <= 0:
            continue
        num_intervals = math.floor((current_time - feed_details.startTime) / feed_details.interval)
        # Start time of latest submission window
        current_window_start = feed_details.startTime + (feed_details.interval * num_intervals)

        if not current_values[query_tag]:
            value_before_now = 0
            timestamp_before_now = 0
        else:
            value_before_now = current_values[(query_tag, "current_price")]
            timestamp_before_now = current_values[(query_tag, "timestamp")]

        rules = [
            (current_time - current_window_start) < feed_details.window,
            timestamp_before_now < current_window_start,
        ]
        if not all(rules):
            msg = f"{query_tag}, isn't eligible for a tip"
            error_status(note=msg, log=logger.info)
            continue

        if feed_details.priceThreshold == 0:
            if query_tag not in query_id_with_tips:
                query_id_with_tips[query_tag] = feed_details.reward
            else:
                query_id_with_tips[query_tag] += feed_details.reward
        else:
            datafeed = CATALOG_FEEDS[query_tag]
            value_now = await datafeed.source.fetch_new_datapoint()  # type: ignore
            if not value_now:
                note = f"Unable to fetch {datafeed} price for tip calculation"
                error_status(note=note, log=logger.warning)
                continue
            value_now = value_now[0]

            if value_before_now == 0:
                price_change = 10000

            elif value_now >= value_before_now:
                price_change = (10000 * (value_now - value_before_now)) / value_before_now

            else:
                price_change = (10000 * (value_before_now - value_now)) / value_before_now

            if price_change > feed_details.priceThreshold:
                if query_tag not in query_id_with_tips:
                    query_id_with_tips[query_tag] = feed_details.reward
                else:
                    query_id_with_tips[query_tag] += feed_details.reward

    return query_id_with_tips


def _add_values(x: Optional[int], y: Optional[int]) -> Optional[int]:
    """Helper function to add values when combining dicts with same key"""
    return sum((num for num in (x, y) if num is not None))


def _is_timestamp_first_in_window(
    timestamp_before: int, timestamp_to_check: int, feed_start_timestamp: int, feed_window: int, feed_interval: int
) -> bool:
    """
    Calculates to check if timestamp(timestamp_to_check) is first in window

    Return: bool
    """
    # Number of intervals since start time
    num_intervals = math.floor((timestamp_to_check - feed_start_timestamp) / feed_interval)
    # Start time of latest submission window
    current_window_start = feed_start_timestamp + (feed_interval * num_intervals)
    eligible = [(timestamp_to_check - current_window_start) < feed_window, timestamp_before < current_window_start]
    return all(eligible)


def _remaining_feed_balance(current_feeds: Any, reward_claimed_status: Any) -> Any:
    """
    Checks if a feed has a remaining balance

    """
    for _, tag, feed_id in current_feeds:
        details = FeedDetails(*current_feeds[_, tag, feed_id])
        balance = details.balance
        if balance > 0:
            for _tag, _feed_id, timestamp in reward_claimed_status:
                if balance > 0 and tag == _tag and feed_id == _feed_id:
                    if not reward_claimed_status[tag, feed_id, timestamp]:
                        balance -= details.reward
                        current_feeds[_, tag, feed_id][1] = max(balance, 0)
    return current_feeds
