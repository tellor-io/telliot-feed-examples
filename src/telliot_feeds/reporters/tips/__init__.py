import logging
from typing import Optional

from multicall.constants import MULTICALL2_ADDRESSES
from multicall.constants import MULTICALL3_ADDRESSES
from multicall.constants import Network
from multicall.constants import NO_STATE_OVERRIDE

from telliot_feeds.queries.query_catalog import query_catalog

logger = logging.getLogger(__name__)


# add testnet support for multicall that aren't avaialable in the package
def add_multicall_support(
    network: str,
    network_id: int,
    state_override: bool = True,
    multicall2_address: Optional[str] = None,
    multicall3_address: Optional[str] = None,
) -> None:
    """Add support for a network that doesn't have multicall support in the package"""
    if not hasattr(Network, network):
        setattr(Network, network, network_id)
        attr = getattr(Network, network)
        if not state_override:
            # Gnosis chain doesn't have state override so we need to add it
            # to the list of chains that don't have state override in the package
            # to avoid errors
            NO_STATE_OVERRIDE.append(attr)
        if multicall2_address:
            MULTICALL2_ADDRESSES[attr] = multicall2_address
        else:
            MULTICALL3_ADDRESSES[attr] = multicall3_address
    else:
        logger.info(f"Network {network} already exists in multicall package")


add_multicall_support(
    network="PulsechainTestnet", network_id=941, multicall2_address="0x959a437F1444DaDaC8aF997E71EAF0479c810267"
)

add_multicall_support(
    network="Chiado",
    network_id=10200,
    state_override=False,
    multicall3_address="0x08e08170712c7751b45b38865B97A50855c8ab13",
)

add_multicall_support(
    network="Filecoin Hyperspace Testnet",
    network_id=3141,
    state_override=False,
    multicall3_address="0x08e08170712c7751b45b38865B97A50855c8ab13",
)

add_multicall_support(
    network="Filecoin calibration Testnet",
    network_id=314159,
    state_override=False,
    multicall3_address="0x08e08170712c7751b45b38865B97A50855c8ab13",
)

add_multicall_support(
    network="Filecoin",
    network_id=314,
    state_override=False,
    multicall3_address="0x5c691b93A8A77D9a36C1Cc8e4e08a4283d1665e1",
)

CATALOG_QUERY_IDS = {query_catalog._entries[tag].query.query_id: tag for tag in query_catalog._entries}
CATALOG_QUERY_DATA = {query_catalog._entries[tag].query.query_data: tag for tag in query_catalog._entries}
# A list of query types that have a generic source that can take any properly formatted inputs and return a price
# unlike manual input sources that prompt user input. This allows tip listener to fetch prices when needing to check
# threshold conditions
TYPES_WITH_GENERIC_SOURCE = ["MimicryMacroMarketMashup", "MimicryCollectionStat"]
