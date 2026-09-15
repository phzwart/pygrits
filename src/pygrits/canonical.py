"""Canonical bytes and content-reference integrity (RFC 8785 JCS)."""

from __future__ import annotations

import hashlib
import json
from typing import Any

import jcs

from pygrits.core import ContentReference, Grit, HashMode


def canonical_bytes_for_instance(grit: Grit) -> bytes:
    if not isinstance(grit, Grit):
        raise TypeError(f"expected Grit, got {type(grit).__name__}")
    json_str = grit.model_dump_json(
        exclude_none=True, by_alias=True, exclude={"content_hash"}
    )
    return jcs.canonicalize(json.loads(json_str))


def canonical_hash_instance(grit: Grit) -> str:
    digest = hashlib.sha256(canonical_bytes_for_instance(grit)).hexdigest()
    return f"sha256:{digest}"


def canonical_hash_bytes(data: bytes) -> str:
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError(f"expected bytes, got {type(data).__name__}")
    return f"sha256:{hashlib.sha256(data).hexdigest()}"


def _strip_scheme(hash_value: str) -> str:
    return hash_value.removeprefix("sha256:")


def verify_content_reference(
    ref: ContentReference,
    content: bytes | Grit | dict[str, Any],
) -> bool:
    expected = _strip_scheme(ref.sha256)
    if ref.hash_mode == HashMode.raw_bytes:
        if not isinstance(content, (bytes, bytearray)):
            raise TypeError("raw_bytes mode requires bytes content")
        actual = hashlib.sha256(content).hexdigest()
    elif ref.hash_mode == HashMode.linkml_canonical_jcs:
        if isinstance(content, Grit):
            canonical = canonical_bytes_for_instance(content)
        elif isinstance(content, dict):
            canonical = jcs.canonicalize(content)
        else:
            raise TypeError("linkml_canonical_jcs mode requires Grit or dict")
        actual = hashlib.sha256(canonical).hexdigest()
    else:
        raise ValueError(f"Unknown hash_mode: {ref.hash_mode!r}")
    return actual == expected


def compute_content_hash(grit: Grit) -> str:
    return hashlib.sha256(canonical_bytes_for_instance(grit)).hexdigest()


def stamp(grit: Grit) -> Grit:
    return grit.model_copy(update={"content_hash": compute_content_hash(grit)})
