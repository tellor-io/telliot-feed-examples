from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List
from typing import Optional

from telliot_core.apps.telliot_config import TelliotConfig

from telliot_feeds.dtypes.datapoint import datetime_now_utc
from telliot_feeds.dtypes.datapoint import OptionalDataPoint
from telliot_feeds.feeds.eth_usd_feed import eth_usd_median_feed
from telliot_feeds.pricing.price_service import WebPriceService
from telliot_feeds.pricing.price_source import PriceSource
from telliot_feeds.utils.log import get_logger

logger = get_logger(__name__)

AERODROME_CONTRACT = "0xee717411f6E44F9feE011835C8E6FAaC5dEfF166"
CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "uint8", "name": "src_len", "type": "uint8"},
            {"internalType": "contract IERC20Metadata[]", "name": "connectors", "type": "address[]"},
        ],
        "name": "getManyRatesWithConnectors",
        "outputs": [{"internalType": "uint256[]", "name": "rates", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function",
    }
]
SRC_LEN = 1
CONNECTORS = [
    "0xDBFeFD2e8460a6Ee4955A68582F85708BAEA60A3",
    "0x4200000000000000000000000000000000000006",
    "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
]


class superOETHbSpotPriceService(WebPriceService):
    """Custom superOETHb Price Service"""

    def __init__(self, **kwargs: Any) -> None:
        kwargs["name"] = "Custom superOETHb Price Service"
        kwargs["url"] = ""
        super().__init__(**kwargs)
        self.cfg = TelliotConfig()
        self.contract_address: Optional[str] = None
        self.contract_abi: Optional[Any] = None
        self.src_len: Optional[int] = None
        self.connectors: Optional[List[Any]] = None

    def get_aerodrome_usd_price(self) -> Optional[float]:
        # get endpoint
        endpoint = self.cfg.endpoints.find(chain_id=8453)
        if not endpoint:
            logger.error("Endpoint not found for mainnet to get superoethb_eth_ratio")
            return None
        ep = endpoint[0]
        if not ep.connect():
            logger.error("Unable to connect endpoint for mainnet to get superoethb_eth_ratio")
            return None
        w3 = ep._web3
        if w3 is None:
            logger.error("Unable to get web3 for mainnet to get superoethb_eth_ratio")
            return None
        # get usd price of superOETHb
        try:
            src_len = SRC_LEN
            connectors = CONNECTORS
            contract = w3.eth.contract(address=AERODROME_CONTRACT, abi=CONTRACT_ABI)

            contract_function = contract.functions.getManyRatesWithConnectors(src_len, connectors)
            aerodrome_response = contract_function.call()
            response_int = aerodrome_response[0]
            response_usd_price = w3.fromWei(response_int, "ether")
            response_price_float = float(response_usd_price)
        except Exception as e:
            print(f"Error querying Aerodrome: {e}")

        return response_price_float

    async def get_price(self, asset: str, currency: str) -> OptionalDataPoint[float]:
        """This implementation gets the superOETHb/ETH ratio by checking the oracle
        price from Aerodrome's price oracle contract
        """
        asset = asset.lower()
        currency = currency.lower()

        source = eth_usd_median_feed.source
        eth_price, timestamp = await source.fetch_new_datapoint()
        if eth_price is None:
            logger.error("Unable to get eth/usd price for superOETHb conversion")
            return None, None

        usd_price = self.get_aerodrome_usd_price()
        logger.info(f"superoethb usd_price: {usd_price}")
        if usd_price is None:
            logger.error("usd_price is None for superOETHb (check source)")
            return None, None

        superoethb_eth_ratio = float(usd_price / eth_price)
        if superoethb_eth_ratio is None:
            logger.error("Unable to get superoethb_eth_ratio")
            return None, None

        return superoethb_eth_ratio, datetime_now_utc()


@dataclass
class superoethbSpotPriceSource(PriceSource):
    """Gets data from Aerodrome contract"""

    asset: str = ""
    currency: str = ""
    service: superOETHbSpotPriceService = field(default_factory=superOETHbSpotPriceService, init=False)


if __name__ == "__main__":
    import asyncio

    async def main() -> None:
        source = superoethbSpotPriceSource(asset="superoethb", currency="eth")
        v, _ = await source.fetch_new_datapoint()
        print(v)

    asyncio.run(main())