from typing import Any
from typing import Dict

from telliot_feeds.datafeed import DataFeed
from telliot_feeds.feeds.aave_usd_feed import aave_usd_median_feed
from telliot_feeds.feeds.albt_usd_feed import albt_usd_median_feed
from telliot_feeds.feeds.ampl_usd_vwap_feed import ampl_usd_vwap_feed
from telliot_feeds.feeds.avax_usd_feed import avax_usd_median_feed
from telliot_feeds.feeds.badger_usd_feed import badger_usd_median_feed
from telliot_feeds.feeds.bch_usd_feed import bch_usd_median_feed
from telliot_feeds.feeds.bct_usd_feed import bct_usd_median_feed
from telliot_feeds.feeds.btc_usd_feed import btc_usd_median_feed
from telliot_feeds.feeds.comp_usd_feed import comp_usd_median_feed
from telliot_feeds.feeds.crv_usd_feed import crv_usd_median_feed
from telliot_feeds.feeds.dai_usd_feed import dai_usd_median_feed
from telliot_feeds.feeds.daily_volatility_manual_feed import daily_volatility_manual_feed
from telliot_feeds.feeds.diva_manual_feed import diva_manual_feed
from telliot_feeds.feeds.doge_usd_feed import doge_usd_median_feed
from telliot_feeds.feeds.dot_usd_feed import dot_usd_median_feed
from telliot_feeds.feeds.eth_btc_feed import eth_btc_median_feed
from telliot_feeds.feeds.eth_jpy_feed import eth_jpy_median_feed
from telliot_feeds.feeds.eth_usd_30day_volatility import eth_usd_30day_volatility
from telliot_feeds.feeds.eth_usd_feed import eth_usd_median_feed
from telliot_feeds.feeds.eul_usd_feed import eul_usd_median_feed
from telliot_feeds.feeds.eur_usd_feed import eur_usd_median_feed
from telliot_feeds.feeds.evm_call_feed import evm_call_feed
from telliot_feeds.feeds.evm_call_feed import evm_call_feed_example
from telliot_feeds.feeds.fil_usd_feed import fil_usd_median_feed
from telliot_feeds.feeds.gas_price_oracle_feed import gas_price_oracle_feed
from telliot_feeds.feeds.gas_price_oracle_feed import gas_price_oracle_feed_example
from telliot_feeds.feeds.gno_usd_feed import gno_usd_median_feed
from telliot_feeds.feeds.idle_usd_feed import idle_usd_median_feed
from telliot_feeds.feeds.link_usd_feed import link_usd_median_feed
from telliot_feeds.feeds.ltc_usd_feed import ltc_usd_median_feed
from telliot_feeds.feeds.matic_usd_feed import matic_usd_median_feed
from telliot_feeds.feeds.mimicry.collection_stat_feed import mimicry_collection_stat_feed
from telliot_feeds.feeds.mimicry.collection_stat_feed import mimicry_example_feed
from telliot_feeds.feeds.mimicry.macro_market_mashup_feed import mimicry_mashup_example_feed
from telliot_feeds.feeds.mimicry.macro_market_mashup_feed import mimicry_mashup_feed
from telliot_feeds.feeds.mimicry.nft_index_feed import mimicry_nft_market_index_eth_feed
from telliot_feeds.feeds.mimicry.nft_index_feed import mimicry_nft_market_index_feed
from telliot_feeds.feeds.mimicry.nft_index_feed import mimicry_nft_market_index_usd_feed
from telliot_feeds.feeds.mkr_usd_feed import mkr_usd_median_feed
from telliot_feeds.feeds.numeric_api_response_feed import numeric_api_response_feed
from telliot_feeds.feeds.numeric_api_response_manual_feed import numeric_api_response_manual_feed
from telliot_feeds.feeds.olympus import ohm_eth_median_feed
from telliot_feeds.feeds.op_usd_feed import op_usd_median_feed
from telliot_feeds.feeds.pls_usd_feed import pls_usd_feed
from telliot_feeds.feeds.rai_usd_feed import rai_usd_median_feed
from telliot_feeds.feeds.reth_btc_feed import reth_btc_median_feed
from telliot_feeds.feeds.reth_usd_feed import reth_usd_median_feed
from telliot_feeds.feeds.ric_usd_feed import ric_usd_median_feed
from telliot_feeds.feeds.shib_usd_feed import shib_usd_median_feed
from telliot_feeds.feeds.snapshot_feed import snapshot_feed_example
from telliot_feeds.feeds.snapshot_feed import snapshot_manual_feed
from telliot_feeds.feeds.spot_price_manual_feed import spot_price_manual_feed
from telliot_feeds.feeds.steth_btc_feed import steth_btc_median_feed
from telliot_feeds.feeds.steth_usd_feed import steth_usd_median_feed
from telliot_feeds.feeds.string_query_feed import string_query_feed
from telliot_feeds.feeds.sushi_usd_feed import sushi_usd_median_feed
from telliot_feeds.feeds.tellor_rng_feed import tellor_rng_feed
from telliot_feeds.feeds.tellor_rng_manual_feed import tellor_rng_manual_feed
from telliot_feeds.feeds.trb_usd_feed import trb_usd_median_feed
from telliot_feeds.feeds.twap_manual_feed import twap_30d_example_manual_feed
from telliot_feeds.feeds.twap_manual_feed import twap_manual_feed
from telliot_feeds.feeds.uni_usd_feed import uni_usd_median_feed
from telliot_feeds.feeds.usdc_usd_feed import usdc_usd_median_feed
from telliot_feeds.feeds.usdt_usd_feed import usdt_usd_median_feed
from telliot_feeds.feeds.uspce_feed import uspce_feed
from telliot_feeds.feeds.vesq import vsq_usd_median_feed
from telliot_feeds.feeds.wsteth_feed import wsteth_eth_median_feed
from telliot_feeds.feeds.wsteth_feed import wsteth_usd_median_feed
from telliot_feeds.feeds.xdai_usd_feed import xdai_usd_median_feed
from telliot_feeds.feeds.yfi_usd_feed import yfi_usd_median_feed


CATALOG_FEEDS: Dict[str, DataFeed[Any]] = {
    "ampleforth-custom": ampl_usd_vwap_feed,
    "ampleforth-uspce": uspce_feed,
    "eth-jpy-spot": eth_jpy_median_feed,
    "ohm-eth-spot": ohm_eth_median_feed,
    "vsq-usd-spot": vsq_usd_median_feed,
    "bct-usd-spot": bct_usd_median_feed,
    "dai-usd-spot": dai_usd_median_feed,
    "ric-usd-spot": ric_usd_median_feed,
    "idle-usd-spot": idle_usd_median_feed,
    "mkr-usd-spot": mkr_usd_median_feed,
    "sushi-usd-spot": sushi_usd_median_feed,
    "matic-usd-spot": matic_usd_median_feed,
    "usdc-usd-spot": usdc_usd_median_feed,
    "gas-price-oracle-example": gas_price_oracle_feed_example,
    "eth-usd-30day_volatility": eth_usd_30day_volatility,
    "eur-usd-spot": eur_usd_median_feed,
    "snapshot-proposal-example": snapshot_feed_example,
    "numeric-api-response-example": numeric_api_response_feed,
    "diva-protocol-example": diva_manual_feed,
    "string-query-example": string_query_feed,
    "tellor-rng-example": tellor_rng_feed,
    "twap-eth-usd-example": twap_30d_example_manual_feed,
    "pls-usd-spot": pls_usd_feed,
    "eth-usd-spot": eth_usd_median_feed,
    "btc-usd-spot": btc_usd_median_feed,
    "trb-usd-spot": trb_usd_median_feed,
    "albt-usd-spot": albt_usd_median_feed,
    "rai-usd-spot": rai_usd_median_feed,
    "xdai-usd-spot": xdai_usd_median_feed,
    "eth-btc-spot": eth_btc_median_feed,
    "evm-call-example": evm_call_feed_example,
    "aave-usd-spot": aave_usd_median_feed,
    "avax-usd-spot": avax_usd_median_feed,
    "badger-usd-spot": badger_usd_median_feed,
    "bch-usd-spot": bch_usd_median_feed,
    "comp-usd-spot": comp_usd_median_feed,
    "crv-usd-spot": crv_usd_median_feed,
    "doge-usd-spot": doge_usd_median_feed,
    "dot-usd-spot": dot_usd_median_feed,
    "eul-usd-spot": eul_usd_median_feed,
    "fil-usd-spot": fil_usd_median_feed,
    "gno-usd-spot": gno_usd_median_feed,
    "link-usd-spot": link_usd_median_feed,
    "ltc-usd-spot": ltc_usd_median_feed,
    "shib-usd-spot": shib_usd_median_feed,
    "uni-usd-spot": uni_usd_median_feed,
    "usdt-usd-spot": usdt_usd_median_feed,
    "yfi-usd-spot": yfi_usd_median_feed,
    "mimicry-crypto-coven-tami": mimicry_example_feed,
    "mimicry-nft-index-usd": mimicry_nft_market_index_usd_feed,
    "mimicry-nft-index-eth": mimicry_nft_market_index_eth_feed,
    "mimicry-mashup-example": mimicry_mashup_example_feed,
    "steth-btc-spot": steth_btc_median_feed,
    "steth-usd-spot": steth_usd_median_feed,
    "reth-btc-spot": reth_btc_median_feed,
    "reth-usd-spot": reth_usd_median_feed,
    "wsteth-usd-spot": wsteth_usd_median_feed,
    "wsteth-eth-spot": wsteth_eth_median_feed,
    "op-usd-spot": op_usd_median_feed,
}

DATAFEED_BUILDER_MAPPING: Dict[str, DataFeed[Any]] = {
    "SpotPrice": spot_price_manual_feed,
    "DivaProtocol": diva_manual_feed,
    "SnapshotOracle": snapshot_manual_feed,
    "GasPriceOracle": gas_price_oracle_feed,
    "StringQuery": string_query_feed,
    "NumericApiManualResponse": numeric_api_response_manual_feed,
    "NumericApiResponse": numeric_api_response_feed,  # this build will parse and submit response value automatically
    "TWAP": twap_manual_feed,
    "DailyVolatility": daily_volatility_manual_feed,
    "TellorRNG": tellor_rng_feed,
    "TellorRNGManualResponse": tellor_rng_manual_feed,
    "AmpleforthCustomSpotPrice": ampl_usd_vwap_feed,
    "AmpleforthUSPCE": uspce_feed,
    "MimicryCollectionStat": mimicry_collection_stat_feed,
    "MimicryNFTMarketIndex": mimicry_nft_market_index_feed,
    "MimicryMacroMarketMashup": mimicry_mashup_feed,
    "EVMCall": evm_call_feed,
}
