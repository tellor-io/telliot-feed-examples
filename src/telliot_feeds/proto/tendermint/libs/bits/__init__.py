# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/libs/bits/types.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class BitArray(betterproto.Message):
    bits: int = betterproto.int64_field(1)
    elems: List[int] = betterproto.uint64_field(2)