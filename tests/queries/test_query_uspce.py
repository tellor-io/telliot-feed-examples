"""Test USPCE query type."""
from telliot_feeds.queries.ampleforth.uspce import USPCE


def test_uspce_query():
    """Validate USPCE query id and data"""
    q = USPCE()

    print(q.query_data.hex())
    print(q.query_id.hex())

    assert q.query_data.hex() == "000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000005555350434500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert q.query_id.hex() == "d930e22716071ff74cae6e25dd94a715846bfa4237db10c667521f7749caecdf"