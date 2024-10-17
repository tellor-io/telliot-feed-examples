from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.solvbtcbbn_source import pancakePoolPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

solvbtcbbn_usd_median_feed = DataFeed(
    query=SpotPrice(asset="SOLVBTCBBN", currency="USD"),
    source=PriceAggregator(
        asset="solvbtcbbn",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="solvbtcbbn", currency="usd"),
            pancakePoolPriceSource(asset="solvbtcbbn", currency="usd"),
        ],
    ),
)
