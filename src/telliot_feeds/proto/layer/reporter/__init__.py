# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: layer/reporter/genesis.proto, layer/reporter/oracle_reporter.proto, layer/reporter/params.proto, layer/reporter/query.proto, layer/reporter/selection.proto, layer/reporter/token_origin.proto, layer/reporter/tx.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...cosmos.base.query import v1beta1 as __cosmos_base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the module."""

    min_commission_rate: str = betterproto.string_field(1)
    """
    min_commission_rate, adopted from staking module, is the minimum commission rate a reporter can their delegators
    """

    min_trb: str = betterproto.string_field(2)
    """min_trb to be a reporter"""

    max_selectors: int = betterproto.uint64_field(3)
    """max number of selectors for a reporter"""


@dataclass(eq=False, repr=False)
class StakeTracker(betterproto.Message):
    expiration: datetime = betterproto.message_field(1)
    amount: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless overwritten).
    """

    params: "Params" = betterproto.message_field(2)
    """NOTE: All parameters must be supplied."""


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
     MsgUpdateParams message.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgCreateReporter(betterproto.Message):
    """MsgCreateReporter defines the Msg/CreateReporter request type."""

    reporter_address: str = betterproto.string_field(1)
    """reporter_address is the address of the reporter."""

    commission_rate: str = betterproto.string_field(2)
    min_tokens_required: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgCreateReporterResponse(betterproto.Message):
    """
    MsgCreateReporterResponse defines the Msg/CreateReporter response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgSelectReporter(betterproto.Message):
    """MsgSelectReporter defines the Msg/SelectReporter request type."""

    selector_address: str = betterproto.string_field(1)
    """selector_address is the address of the selector."""

    reporter_address: str = betterproto.string_field(2)
    """reporter_address is the address of the reporter to select."""


@dataclass(eq=False, repr=False)
class MsgSelectReporterResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MsgSwitchReporter(betterproto.Message):
    """MsgSwitchReporter defines the Msg/SwitchReporter request type."""

    selector_address: str = betterproto.string_field(1)
    """selector_address is the address of the selector."""

    reporter_address: str = betterproto.string_field(2)
    """reporter_address is the address of the reporter to switch."""


@dataclass(eq=False, repr=False)
class MsgSwitchReporterResponse(betterproto.Message):
    """
    MsgSwitchReporterResponse defines the Msg/SwitchReporter response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgRemoveSelector(betterproto.Message):
    """MsgRemoveSelector defines the Msg/RemoveSelector request type."""

    any_address: str = betterproto.string_field(1)
    """any_address is the caller which can be any address."""

    selector_address: str = betterproto.string_field(2)
    """selector_address is the address of the selector."""


@dataclass(eq=False, repr=False)
class MsgRemoveSelectorResponse(betterproto.Message):
    """
    MsgRemoveSelectorResponse defines the Msg/RemoveSelector response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgUnjailReporter(betterproto.Message):
    """MsgUnjailReporter defines the Msg/UnjailReporter request type."""

    reporter_address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgUnjailReporterResponse(betterproto.Message):
    """
    MsgUnjailReporterResponse defines the Msg/UnjailReporter response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgWithdrawTip(betterproto.Message):
    """MsgWithdrawTip defines the Msg/WithdrawTip request type."""

    selector_address: str = betterproto.string_field(1)
    validator_address: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgWithdrawTipResponse(betterproto.Message):
    """MsgWithdrawTipResponse defines the Msg/WithdrawTip response type."""

    pass


@dataclass(eq=False, repr=False)
class OracleReporter(betterproto.Message):
    """OracleReporter is the struct that holds the data for a reporter"""

    min_tokens_required: str = betterproto.string_field(1)
    """min_tokens_required to select this reporter"""

    commission_rate: str = betterproto.string_field(2)
    """commission for the reporter"""

    jailed: bool = betterproto.bool_field(3)
    """jailed is a bool whether the reporter is jailed or not"""

    jailed_until: datetime = betterproto.message_field(4)
    """jailed_until is the time the reporter is jailed until"""


@dataclass(eq=False, repr=False)
class Selection(betterproto.Message):
    """Selection is a type that represents a  delegator's selection"""

    reporter: bytes = betterproto.bytes_field(1)
    """reporter is the address of the reporter being delegated to"""

    locked_until_time: datetime = betterproto.message_field(2)
    """
    locked_until_time is the time until which the tokens are locked before they
     can be used for reporting again
    """

    delegations_count: int = betterproto.int64_field(3)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is response type for the Query/Params RPC method.
    """

    params: "Params" = betterproto.message_field(1)
    """params holds all the parameters of this module."""


@dataclass(eq=False, repr=False)
class QueryReportersRequest(betterproto.Message):
    """
    QueryReportersRequest is the request type for the Query/Reporters RPC method.
    """

    pagination: "__cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class Reporter(betterproto.Message):
    address: str = betterproto.string_field(1)
    metadata: "OracleReporter" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryReportersResponse(betterproto.Message):
    """
    QueryReportersResponse is the response type for the Query/Reporters RPC method.
    """

    reporters: List["Reporter"] = betterproto.message_field(1)
    """all the reporters."""

    pagination: "__cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QuerySelectorReporterRequest(betterproto.Message):
    """
    QuerySelectorReporterRequest is the request type for the
     Query/SelectorReporter RPC method.
    """

    selector_address: str = betterproto.string_field(1)
    """selector_address defines the selector address to query for."""


@dataclass(eq=False, repr=False)
class QuerySelectorReporterResponse(betterproto.Message):
    """
    QuerySelectorReporterResponse is the response type for the
     Query/SelectorReporter RPC method.
    """

    reporter: str = betterproto.string_field(1)
    """reporter defines the reporter of a selector."""


@dataclass(eq=False, repr=False)
class QueryAllowedAmountRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryAllowedAmountResponse(betterproto.Message):
    staking_amount: str = betterproto.string_field(1)
    """
    allowed_amount defines the currently allowed amount to stake or unstake.
    """

    unstaking_amount: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class QueryAllowedAmountExpirationRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryAllowedAmountExpirationResponse(betterproto.Message):
    expiration: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class QueryNumOfSelectorsByReporterRequest(betterproto.Message):
    """
    QueryNumOfSelectorsByReporterRequest is the request type for the
     Query/NumOfSelectorsByReporter RPC method.
    """

    reporter_address: str = betterproto.string_field(1)
    """reporter_address defines the reporter address to query for."""


@dataclass(eq=False, repr=False)
class QueryNumOfSelectorsByReporterResponse(betterproto.Message):
    """
    QueryNumOfSelectorsByReporterResponse is the response type for the
     Query/NumOfSelectorsByReporter RPC method.
    """

    num_of_selectors: int = betterproto.int32_field(1)
    """num_of_selectors defines the number of selectors by a reporter."""


@dataclass(eq=False, repr=False)
class QuerySpaceAvailableByReporterRequest(betterproto.Message):
    """
    QuerySpaceAvailableByReporterRequest is the request type for the
     Query/SpaceAvailableByReporter RPC method.
    """

    reporter_address: str = betterproto.string_field(1)
    """reporter_address defines the reporter address to query for."""


@dataclass(eq=False, repr=False)
class QuerySpaceAvailableByReporterResponse(betterproto.Message):
    """
    QuerySpaceAvailableByReporterResponse is the response type for the
     Query/SpaceAvailableByReporter RPC method.
    """

    space_available: int = betterproto.int32_field(1)
    """space_available defines the space available in a reporter."""


@dataclass(eq=False, repr=False)
class QueryAvailableTipsRequest(betterproto.Message):
    selector_address: str = betterproto.string_field(1)
    """selector address defines the address of the selector to query for."""


@dataclass(eq=False, repr=False)
class QueryAvailableTipsResponse(betterproto.Message):
    available_tips: str = betterproto.string_field(1)
    """
    available_tips defines the tips available for withdrawal for a given selector.
    """


@dataclass(eq=False, repr=False)
class TokenOriginInfo(betterproto.Message):
    """
    TokenOriginInfo is the struct that holds the data of where tokens are staked
    """

    delegator_address: bytes = betterproto.bytes_field(1)
    """delegator_address is the address of the delegator"""

    validator_address: bytes = betterproto.bytes_field(2)
    """validator_address is the address of the validator"""

    amount: str = betterproto.string_field(3)
    """amount is the amount of tokens staked"""


@dataclass(eq=False, repr=False)
class DelegationsAmounts(betterproto.Message):
    """
    DelegationsAmounts is the struct that holds the data of delegations and amounts and the total
    """

    token_origins: List["TokenOriginInfo"] = betterproto.message_field(1)
    """
    token_origins is the list of token origins for and where the amounts are staked
    """

    total: str = betterproto.string_field(2)
    """total amount of tokens in the list"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the reporter module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the parameters of the module."""


class MsgStub(betterproto.ServiceStub):
    async def update_params(
        self,
        msg_update_params: "MsgUpdateParams",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgUpdateParamsResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def create_reporter(
        self,
        msg_create_reporter: "MsgCreateReporter",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgCreateReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/CreateReporter",
            msg_create_reporter,
            MsgCreateReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def select_reporter(
        self,
        msg_select_reporter: "MsgSelectReporter",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgSelectReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/SelectReporter",
            msg_select_reporter,
            MsgSelectReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def switch_reporter(
        self,
        msg_switch_reporter: "MsgSwitchReporter",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgSwitchReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/SwitchReporter",
            msg_switch_reporter,
            MsgSwitchReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def remove_selector(
        self,
        msg_remove_selector: "MsgRemoveSelector",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgRemoveSelectorResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/RemoveSelector",
            msg_remove_selector,
            MsgRemoveSelectorResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def unjail_reporter(
        self,
        msg_unjail_reporter: "MsgUnjailReporter",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgUnjailReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/UnjailReporter",
            msg_unjail_reporter,
            MsgUnjailReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def withdraw_tip(
        self,
        msg_withdraw_tip: "MsgWithdrawTip",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgWithdrawTipResponse":
        return await self._unary_unary(
            "/layer.reporter.Msg/WithdrawTip",
            msg_withdraw_tip,
            MsgWithdrawTipResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def reporters(
        self,
        query_reporters_request: "QueryReportersRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryReportersResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/Reporters",
            query_reporters_request,
            QueryReportersResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def selector_reporter(
        self,
        query_selector_reporter_request: "QuerySelectorReporterRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySelectorReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/SelectorReporter",
            query_selector_reporter_request,
            QuerySelectorReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def allowed_amount(
        self,
        query_allowed_amount_request: "QueryAllowedAmountRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAllowedAmountResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/AllowedAmount",
            query_allowed_amount_request,
            QueryAllowedAmountResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def allowed_amount_expiration(
        self,
        query_allowed_amount_expiration_request: "QueryAllowedAmountExpirationRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAllowedAmountExpirationResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/AllowedAmountExpiration",
            query_allowed_amount_expiration_request,
            QueryAllowedAmountExpirationResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def num_of_selectors_by_reporter(
        self,
        query_num_of_selectors_by_reporter_request: "QueryNumOfSelectorsByReporterRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryNumOfSelectorsByReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/NumOfSelectorsByReporter",
            query_num_of_selectors_by_reporter_request,
            QueryNumOfSelectorsByReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def space_available_by_reporter(
        self,
        query_space_available_by_reporter_request: "QuerySpaceAvailableByReporterRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySpaceAvailableByReporterResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/SpaceAvailableByReporter",
            query_space_available_by_reporter_request,
            QuerySpaceAvailableByReporterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def available_tips(
        self,
        query_available_tips_request: "QueryAvailableTipsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAvailableTipsResponse":
        return await self._unary_unary(
            "/layer.reporter.Query/AvailableTips",
            query_available_tips_request,
            QueryAvailableTipsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgBase(ServiceBase):

    async def update_params(
        self, msg_update_params: "MsgUpdateParams"
    ) -> "MsgUpdateParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def create_reporter(
        self, msg_create_reporter: "MsgCreateReporter"
    ) -> "MsgCreateReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def select_reporter(
        self, msg_select_reporter: "MsgSelectReporter"
    ) -> "MsgSelectReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def switch_reporter(
        self, msg_switch_reporter: "MsgSwitchReporter"
    ) -> "MsgSwitchReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def remove_selector(
        self, msg_remove_selector: "MsgRemoveSelector"
    ) -> "MsgRemoveSelectorResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def unjail_reporter(
        self, msg_unjail_reporter: "MsgUnjailReporter"
    ) -> "MsgUnjailReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def withdraw_tip(
        self, msg_withdraw_tip: "MsgWithdrawTip"
    ) -> "MsgWithdrawTipResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_update_params(
        self, stream: "grpclib.server.Stream[MsgUpdateParams, MsgUpdateParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_params(request)
        await stream.send_message(response)

    async def __rpc_create_reporter(
        self,
        stream: "grpclib.server.Stream[MsgCreateReporter, MsgCreateReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_reporter(request)
        await stream.send_message(response)

    async def __rpc_select_reporter(
        self,
        stream: "grpclib.server.Stream[MsgSelectReporter, MsgSelectReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.select_reporter(request)
        await stream.send_message(response)

    async def __rpc_switch_reporter(
        self,
        stream: "grpclib.server.Stream[MsgSwitchReporter, MsgSwitchReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.switch_reporter(request)
        await stream.send_message(response)

    async def __rpc_remove_selector(
        self,
        stream: "grpclib.server.Stream[MsgRemoveSelector, MsgRemoveSelectorResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.remove_selector(request)
        await stream.send_message(response)

    async def __rpc_unjail_reporter(
        self,
        stream: "grpclib.server.Stream[MsgUnjailReporter, MsgUnjailReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.unjail_reporter(request)
        await stream.send_message(response)

    async def __rpc_withdraw_tip(
        self, stream: "grpclib.server.Stream[MsgWithdrawTip, MsgWithdrawTipResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.withdraw_tip(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/layer.reporter.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
            "/layer.reporter.Msg/CreateReporter": grpclib.const.Handler(
                self.__rpc_create_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateReporter,
                MsgCreateReporterResponse,
            ),
            "/layer.reporter.Msg/SelectReporter": grpclib.const.Handler(
                self.__rpc_select_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSelectReporter,
                MsgSelectReporterResponse,
            ),
            "/layer.reporter.Msg/SwitchReporter": grpclib.const.Handler(
                self.__rpc_switch_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSwitchReporter,
                MsgSwitchReporterResponse,
            ),
            "/layer.reporter.Msg/RemoveSelector": grpclib.const.Handler(
                self.__rpc_remove_selector,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgRemoveSelector,
                MsgRemoveSelectorResponse,
            ),
            "/layer.reporter.Msg/UnjailReporter": grpclib.const.Handler(
                self.__rpc_unjail_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUnjailReporter,
                MsgUnjailReporterResponse,
            ),
            "/layer.reporter.Msg/WithdrawTip": grpclib.const.Handler(
                self.__rpc_withdraw_tip,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgWithdrawTip,
                MsgWithdrawTipResponse,
            ),
        }


class QueryBase(ServiceBase):

    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def reporters(
        self, query_reporters_request: "QueryReportersRequest"
    ) -> "QueryReportersResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def selector_reporter(
        self, query_selector_reporter_request: "QuerySelectorReporterRequest"
    ) -> "QuerySelectorReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def allowed_amount(
        self, query_allowed_amount_request: "QueryAllowedAmountRequest"
    ) -> "QueryAllowedAmountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def allowed_amount_expiration(
        self,
        query_allowed_amount_expiration_request: "QueryAllowedAmountExpirationRequest",
    ) -> "QueryAllowedAmountExpirationResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def num_of_selectors_by_reporter(
        self,
        query_num_of_selectors_by_reporter_request: "QueryNumOfSelectorsByReporterRequest",
    ) -> "QueryNumOfSelectorsByReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def space_available_by_reporter(
        self,
        query_space_available_by_reporter_request: "QuerySpaceAvailableByReporterRequest",
    ) -> "QuerySpaceAvailableByReporterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def available_tips(
        self, query_available_tips_request: "QueryAvailableTipsRequest"
    ) -> "QueryAvailableTipsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_reporters(
        self,
        stream: "grpclib.server.Stream[QueryReportersRequest, QueryReportersResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.reporters(request)
        await stream.send_message(response)

    async def __rpc_selector_reporter(
        self,
        stream: "grpclib.server.Stream[QuerySelectorReporterRequest, QuerySelectorReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.selector_reporter(request)
        await stream.send_message(response)

    async def __rpc_allowed_amount(
        self,
        stream: "grpclib.server.Stream[QueryAllowedAmountRequest, QueryAllowedAmountResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.allowed_amount(request)
        await stream.send_message(response)

    async def __rpc_allowed_amount_expiration(
        self,
        stream: "grpclib.server.Stream[QueryAllowedAmountExpirationRequest, QueryAllowedAmountExpirationResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.allowed_amount_expiration(request)
        await stream.send_message(response)

    async def __rpc_num_of_selectors_by_reporter(
        self,
        stream: "grpclib.server.Stream[QueryNumOfSelectorsByReporterRequest, QueryNumOfSelectorsByReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.num_of_selectors_by_reporter(request)
        await stream.send_message(response)

    async def __rpc_space_available_by_reporter(
        self,
        stream: "grpclib.server.Stream[QuerySpaceAvailableByReporterRequest, QuerySpaceAvailableByReporterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.space_available_by_reporter(request)
        await stream.send_message(response)

    async def __rpc_available_tips(
        self,
        stream: "grpclib.server.Stream[QueryAvailableTipsRequest, QueryAvailableTipsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.available_tips(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/layer.reporter.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/layer.reporter.Query/Reporters": grpclib.const.Handler(
                self.__rpc_reporters,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryReportersRequest,
                QueryReportersResponse,
            ),
            "/layer.reporter.Query/SelectorReporter": grpclib.const.Handler(
                self.__rpc_selector_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySelectorReporterRequest,
                QuerySelectorReporterResponse,
            ),
            "/layer.reporter.Query/AllowedAmount": grpclib.const.Handler(
                self.__rpc_allowed_amount,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllowedAmountRequest,
                QueryAllowedAmountResponse,
            ),
            "/layer.reporter.Query/AllowedAmountExpiration": grpclib.const.Handler(
                self.__rpc_allowed_amount_expiration,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllowedAmountExpirationRequest,
                QueryAllowedAmountExpirationResponse,
            ),
            "/layer.reporter.Query/NumOfSelectorsByReporter": grpclib.const.Handler(
                self.__rpc_num_of_selectors_by_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryNumOfSelectorsByReporterRequest,
                QueryNumOfSelectorsByReporterResponse,
            ),
            "/layer.reporter.Query/SpaceAvailableByReporter": grpclib.const.Handler(
                self.__rpc_space_available_by_reporter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySpaceAvailableByReporterRequest,
                QuerySpaceAvailableByReporterResponse,
            ),
            "/layer.reporter.Query/AvailableTips": grpclib.const.Handler(
                self.__rpc_available_tips,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAvailableTipsRequest,
                QueryAvailableTipsResponse,
            ),
        }