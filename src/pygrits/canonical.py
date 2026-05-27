"""
Canonicalization and integrity helpers for ISOM entities.

The contract is simple but strict:

- ``canonical_bytes_for_instance(entity)`` returns the bytes that uniquely
  identify the entity's logical content, under the ``linkml_canonical_jcs``
  hash mode. Pipeline: Pydantic JSON dump → parse to dict → RFC 8785 JCS
  canonicalize → bytes.

- ``canonical_hash_instance(entity)`` returns ``"sha256:<hex>"`` over those
  bytes.

- ``canonical_hash_bytes(data)`` returns ``"sha256:<hex>"`` over raw bytes,
  for use with the ``raw_bytes`` hash mode.

- ``verify_content_reference(ref, content)`` checks a ContentReference's
  declared hash against actual content, choosing the right pipeline based on
  the reference's ``hash_mode``.

Why this matters: the entire content-addressed-reference discipline in the
ISOM spec (ViewpointDirective integrity, idempotent Activity detection,
auditable provenance) depends on the canonical form being stable across
machines, library versions, and operating systems. JSON serialization alone
is not stable — key ordering, number formatting, whitespace, and unicode
normalization all vary. RFC 8785 JCS pins those choices.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

import jcs

from pygrits.core import ContentReference, Entity, HashMode


def canonical_bytes_for_instance(entity: Entity) -> bytes:
    """
    Produce the canonical byte representation of a Pydantic entity instance.

    Pipeline:
        1. Dump the entity to JSON via Pydantic's `model_dump_json` with
           ``exclude_none=True`` (None-valued optional fields are omitted, so
           absent and explicitly-None are treated identically for hashing).
        2. Parse the JSON string back to a Python dict.
        3. Apply RFC 8785 JCS canonicalization to that dict.

    The intermediate JSON-string-then-parse step is deliberate. It strips
    Pydantic's serialization quirks (e.g. trailing whitespace differences,
    int-vs-float distinctions in number rendering) and gives JCS a clean
    Python dict to canonicalize.
    """
    if not isinstance(entity, Entity):
        raise TypeError(
            f"canonical_bytes_for_instance expects an Entity subclass instance, "
            f"got {type(entity).__name__}"
        )
    json_str = entity.model_dump_json(exclude_none=True, by_alias=True)
    obj = json.loads(json_str)
    return jcs.canonicalize(obj)


def canonical_hash_instance(entity: Entity) -> str:
    """
    Compute the canonical SHA-256 of an entity instance.

    Returns a string of the form ``"sha256:<64 lowercase hex chars>"``.

    Two entities with the same logical content (same field values, modulo
    None-vs-absent which are treated as equivalent) produce the same hash,
    regardless of field ordering or Python runtime.
    """
    canonical_bytes = canonical_bytes_for_instance(entity)
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    return f"sha256:{digest}"


def canonical_hash_bytes(data: bytes) -> str:
    """
    Compute SHA-256 of raw bytes. For use with the ``raw_bytes`` hash mode.

    Returns ``"sha256:<64 lowercase hex chars>"``.
    """
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError(
            f"canonical_hash_bytes expects bytes, got {type(data).__name__}"
        )
    digest = hashlib.sha256(data).hexdigest()
    return f"sha256:{digest}"


def _strip_scheme(hash_value: str) -> str:
    """
    Accept either a bare hex digest or a ``sha256:<hex>`` prefixed form;
    return the bare hex.
    """
    if hash_value.startswith("sha256:"):
        return hash_value[len("sha256:"):]
    return hash_value


def verify_content_reference(
    ref: ContentReference,
    content: bytes | Entity | dict[str, Any],
) -> bool:
    """
    Verify that a ContentReference's declared hash matches the actual content.

    Dispatches on ``ref.hash_mode``:

    - ``HashMode.raw_bytes`` — ``content`` must be bytes; compares
      SHA-256 of those bytes to ``ref.sha256``.
    - ``HashMode.linkml_canonical_jcs`` — ``content`` may be an Entity
      instance or a dict; applies the canonical pipeline and compares the
      resulting SHA-256 to ``ref.sha256``.

    Returns True if the hash matches, False otherwise. Raises TypeError on
    type/mode mismatches (e.g. passing bytes for the JCS mode).
    """
    expected = _strip_scheme(ref.sha256)

    if ref.hash_mode == HashMode.raw_bytes:
        if not isinstance(content, (bytes, bytearray)):
            raise TypeError(
                f"hash_mode=raw_bytes requires bytes content, "
                f"got {type(content).__name__}"
            )
        actual = hashlib.sha256(content).hexdigest()
        return actual == expected

    if ref.hash_mode == HashMode.linkml_canonical_jcs:
        if isinstance(content, Entity):
            canonical = canonical_bytes_for_instance(content)
        elif isinstance(content, dict):
            canonical = jcs.canonicalize(content)
        else:
            raise TypeError(
                f"hash_mode=linkml_canonical_jcs requires Entity or dict content, "
                f"got {type(content).__name__}"
            )
        actual = hashlib.sha256(canonical).hexdigest()
        return actual == expected

    raise ValueError(f"Unknown hash_mode: {ref.hash_mode!r}")
