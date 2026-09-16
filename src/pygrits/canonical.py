"""Canonical bytes and content-reference integrity (RFC 8785 JCS)."""

from __future__ import annotations

import hashlib
import json

import jcs

from pygrits.models import Bundle, ContentRef, Node, NodeBase


def canonical_bytes_for_instance(node: Node) -> bytes:
    if not isinstance(node, NodeBase):
        raise TypeError(f"expected a node, got {type(node).__name__}")
    payload = json.loads(
        node.model_dump_json(exclude_none=True, by_alias=True, exclude={"content_hash"})
    )
    return jcs.canonicalize(payload)


def canonical_hash_instance(node: Node) -> str:
    digest = hashlib.sha256(canonical_bytes_for_instance(node)).hexdigest()
    return f"sha256:{digest}"


def canonical_hash_bytes(data: bytes) -> str:
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError(f"expected bytes, got {type(data).__name__}")
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def verify_content_reference(ref: ContentRef, content: bytes) -> bool:
    if not isinstance(content, (bytes, bytearray)):
        raise TypeError("content must be bytes")
    return hashlib.sha256(content).hexdigest() == ref.sha256


def compute_content_hash(node: Node) -> str:
    return hashlib.sha256(canonical_bytes_for_instance(node)).hexdigest()


def stamp(obj: Node | Bundle) -> Node | Bundle:
    if isinstance(obj, Bundle):
        return Bundle.model_validate(
            {
                "@context": obj.context,
                "@graph": [stamp(node) for node in obj.graph],
            }
        )
    if not isinstance(obj, NodeBase):
        raise TypeError(f"expected a node or Bundle, got {type(obj).__name__}")
    return obj.model_copy(update={"content_hash": compute_content_hash(obj)})
