import statistics

import pytest

from telliot_feeds.feeds import op_usd_median_feed


@pytest.mark.asyncio
async def test_op_asset_price_feed(caplog):
    """Retrieve median OP/USD price."""
    v, _ = await op_usd_median_feed.source.fetch_new_datapoint()

    assert v is not None
    assert v > 0
    assert "sources used in aggregate: 4" in caplog.text.lower()
    print(f"OP/USD Price: {v}")

    # Get list of data sources from sources dict
    source_prices = [source.latest[0] for source in op_usd_median_feed.source.sources if source.latest[0]]

    # Make sure error is less than decimal tolerance
    assert (v - statistics.median(source_prices)) < 10**-6
