from __future__ import annotations

import json
from pathlib import Path

import pytest

from pygrits import (
    ContentRef,
    canonical_hash_bytes,
    canonical_hash_instance,
    compute_content_hash,
    load,
    stamp,
    verify_content_reference,
)
from pygrits.models import Entity

EXAMPLES = Path(__file__).parent.parent / "examples"


def _entity() -> Entity:
    bundle = load(EXAMPLES / "kcat.jsonld")
    node = bundle.graph[-1]
    assert isinstance(node, Entity)
    return node


def test_hash_format() -> None:
    h = canonical_hash_instance(_entity())
    assert h.startswith("sha256:")
    digest = h.removeprefix("sha256:")
    assert len(digest) == 64


def test_hash_is_deterministic() -> None:
    node = _entity()
    assert canonical_hash_instance(node) == canonical_hash_instance(node)


def test_hash_independent_of_key_order() -> None:
    node = _entity()
    via_json = Entity.model_validate(json.loads(node.model_dump_json(exclude_none=True, by_alias=True)))
    assert canonical_hash_instance(node) == canonical_hash_instance(via_json)


def test_field_change_changes_hash() -> None:
    node = _entity()
    changed = node.model_copy(update={"summary": "different"})
    assert canonical_hash_instance(node) != canonical_hash_instance(changed)


def test_content_hash_excluded_from_canonical_bytes() -> None:
    node = _entity()
    stamped = stamp(node)
    assert canonical_hash_instance(node) == canonical_hash_instance(stamped)
    assert compute_content_hash(node) == stamped.content_hash


def test_stamping_is_idempotent() -> None:
    node = _entity()
    assert stamp(node).content_hash == stamp(stamp(node)).content_hash


def test_canonical_hash_bytes_empty() -> None:
    assert (
        canonical_hash_bytes(b"")
        == "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )


def test_verify_content_reference() -> None:
    content = b"some prompt text"
    digest = canonical_hash_bytes(content).removeprefix("sha256:")
    ref = ContentRef(uri="file://prompt.txt", sha256=digest)
    assert verify_content_reference(ref, content) is True
    assert verify_content_reference(ref, b"other") is False


def test_verify_requires_bytes() -> None:
    ref = ContentRef(uri="file://x", sha256="a" * 64)
    with pytest.raises(TypeError):
        verify_content_reference(ref, "not-bytes")  # type: ignore[arg-type]
