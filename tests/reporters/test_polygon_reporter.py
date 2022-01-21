import pytest
from telliot_core.apps.core import TelliotCore
from telliot_core.utils.response import ResponseStatus

from telliot_feed_examples.feeds.eth_usd_feed import eth_usd_median_feed
from telliot_feed_examples.reporters.tellorflex import PolygonReporter


@pytest.fixture
async def polygon_reporter(mumbai_cfg):
    async with TelliotCore(config=mumbai_cfg) as core:
        flex = core.get_tellorflex_contracts()
        r = PolygonReporter(
            oracle=flex.oracle,
            token=flex.token,
            endpoint=core.endpoint,
            private_key=core.get_staker().private_key,
            chain_id=80001,
        )
        return r


@pytest.mark.asyncio
async def test_ensure_profitable(polygon_reporter):
    status = await polygon_reporter.ensure_profitable(eth_usd_median_feed)

    assert isinstance(status, ResponseStatus)
    assert status.ok


@pytest.mark.asyncio
async def test_fetch_gas_price(polygon_reporter):
    price = await polygon_reporter.fetch_gas_price()

    assert isinstance(price, int)
    assert price > 0


@pytest.mark.asyncio
async def test_ensure_staked(polygon_reporter):
    staked, status = await polygon_reporter.ensure_staked()

    assert isinstance(status, ResponseStatus)
    assert isinstance(staked, bool)
    assert status.ok
    assert staked


@pytest.mark.asyncio
async def test_check_reporter_lock(polygon_reporter):
    status = await polygon_reporter.check_reporter_lock()

    assert isinstance(status, ResponseStatus)
    if not status.ok:
        assert "reporter lock" in status.error


@pytest.mark.asyncio
async def test_get_num_reports_by_id(polygon_reporter):
    qid = eth_usd_median_feed.query.query_id
    count, status = await polygon_reporter.get_num_reports_by_id(qid)

    assert isinstance(status, ResponseStatus)
    if status.ok:
        assert isinstance(count, int)
    else:
        assert count is None
