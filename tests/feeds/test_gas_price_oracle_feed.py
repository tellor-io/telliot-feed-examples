from datetime import datetime

import pytest

from telliot_feed_examples.feeds.gas_price_oracle_feed import chain_id
from telliot_feed_examples.feeds.gas_price_oracle_feed import gas_price_oracle_feed
from telliot_feed_examples.feeds.gas_price_oracle_feed import timestamp


@pytest.mark.asyncio
async def test_fetch_new_datapoint():
    """Retrieve historical gas price data from source."""

    v, t = await gas_price_oracle_feed.source.fetch_new_datapoint(timestamp, chain_id)

    assert v is not None and t is not None
    assert isinstance(v, float)
    assert isinstance(t, datetime)