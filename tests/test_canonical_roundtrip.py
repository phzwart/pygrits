"""
Canonical-form round-trip tests.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from pygrits import (
    ContentReference,
    Entity,
    HashMode,
    canonical_bytes_for_instance,
    canonical_hash_bytes,
    canonical_hash_instance,
    compute_content_hash,
    stamp,
    verify_content_reference,
)

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def _load_entity() -> Entity:
    with open(EXAMPLES_DIR / "05_entity_kcat_landscape.yaml") as f:
        return Entity(**yaml.safe_load(f))


def test_hash_format() -> None:
    obj = _load_entity()
    h = canonical_hash_instance(obj)
    assert h.startswith("sha256:")
    digest = h[len("sha256:"):]
    assert len(digest) == 64
    assert all(c in "0123456789abcdef" for c in digest)


def test_canonical_bytes_is_valid_json() -> None:
    obj = _load_entity()
    raw = canonical_bytes_for_instance(obj)
    parsed = json.loads(raw)
    assert isinstance(parsed, dict)
    assert parsed["id"] == "ent:kcat-landscape-v0"


def test_hash_is_deterministic() -> None:
    obj = _load_entity()
    assert canonical_hash_instance(obj) == canonical_hash_instance(obj)


def test_hash_independent_of_yaml_key_order() -> None:
    obj = _load_entity()
    h_yaml = canonical_hash_instance(obj)
    json_str = obj.model_dump_json(exclude_none=True, by_alias=True)
    obj_via_json = Entity(**json.loads(json_str))
    assert h_yaml == canonical_hash_instance(obj_via_json)


def test_changing_a_field_changes_the_hash() -> None:
    obj = _load_entity()
    h_before = canonical_hash_instance(obj)
    modified = obj.model_copy(update={"summary": "different summary"})
    assert h_before != canonical_hash_instance(modified)


def test_content_hash_excluded_from_canonical_bytes() -> None:
    obj = _load_entity()
    stamped = stamp(obj)
    assert canonical_hash_instance(obj) == canonical_hash_instance(stamped)


def test_canonical_hash_bytes_known_value() -> None:
    assert (
        canonical_hash_bytes(b"")
        == "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )


def test_verify_content_reference_raw_bytes_match() -> None:
    content = b"some prompt text"
    expected_hex = canonical_hash_bytes(content)[len("sha256:"):]
    ref = ContentReference(
        uri="file://prompt.txt",
        sha256=expected_hex,
        hash_mode=HashMode.raw_bytes,
    )
    assert verify_content_reference(ref, content) is True


def test_verify_content_reference_jcs_match() -> None:
    obj = _load_entity()
    expected = canonical_hash_instance(obj)[len("sha256:"):]
    ref = ContentReference(
        uri="file://obj.json",
        sha256=expected,
        hash_mode=HashMode.linkml_canonical_jcs,
    )
    assert verify_content_reference(ref, obj) is True


def test_verify_content_reference_wrong_content_type() -> None:
    ref = ContentReference(
        uri="file://obj.json",
        sha256="a" * 64,
        hash_mode=HashMode.linkml_canonical_jcs,
    )
    with pytest.raises(TypeError):
        verify_content_reference(ref, b"raw bytes not allowed for jcs mode")


def test_compute_content_hash_matches_stamp() -> None:
    obj = _load_entity()
    assert compute_content_hash(obj) == stamp(obj).content_hash
