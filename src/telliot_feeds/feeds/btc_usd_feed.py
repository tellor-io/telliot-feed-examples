from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price.spot.gemini import GeminiSpotPriceSource
from telliot_feeds.sources.price.spot.kraken import KrakenSpotPriceSource
from telliot_feeds.sources.price.spot.okx import OKXSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

# from telliot_feeds.sources.price.spot.binance import BinanceSpotPriceSource

btc_usd_median_feed = DataFeed(
    query=SpotPrice(asset="BTC", currency="USD"),
    source=PriceAggregator(
        asset="btc",
        currency="usd",
        algorithm="median",
        sources=[
            # BinanceSpotPriceSource(asset="btc", currency="usdt"),
            CoinGeckoSpotPriceSource(asset="btc", currency="usd"),
            GeminiSpotPriceSource(asset="btc", currency="usd"),
            KrakenSpotPriceSource(asset="xbt", currency="usd"),
            OKXSpotPriceSource(asset="btc", currency="usdt"),
        ],
    ),
)
