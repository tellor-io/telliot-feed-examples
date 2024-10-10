# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crypto/secp256k1/keys.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class PubKey(betterproto.Message):
    """
    PubKey defines a secp256k1 public key
     Key is the compressed form of the pubkey. The first byte depends is a 0x02 byte
     if the y-coordinate is the lexicographically largest of the two associated with
     the x-coordinate. Otherwise the first byte is a 0x03.
     This prefix is followed with the x-coordinate.
    """

    key: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class PrivKey(betterproto.Message):
    """PrivKey defines a secp256k1 private key."""

    key: bytes = betterproto.bytes_field(1)