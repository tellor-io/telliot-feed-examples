# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/orm/module/v1alpha1/module.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class Module(betterproto.Message):
    """
    Module defines the ORM module which adds providers to the app container for
     module-scoped DB's. In the future it may provide gRPC services for interacting
     with ORM data.
    """

    pass