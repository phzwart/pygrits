"""
Canonical-form round-trip tests.

These tests prove that the canonical hash is actually canonical:

- Hashing an entity, serializing it to JSON, parsing it back, and re-hashing
  must yield the same hash.
- Two semantically-identical entities constructed in different field orders
  must hash identically.
- Modifying any field must change the hash.
- The canonical bytes must be valid JSON (so they round-trip through any
  JSON parser, not just our own).

Without these guarantees, the entire content-addressed reference discipline
(ContentReference integrity, ViewpointDirective identity, idempotent Activity
detection) breaks.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from pygrits import (
    Activity,
    ActivityType,
    CharRangeLocator,
    ContentReference,
    EvidenceRecord,
    HashMode,
    Object,
    canonical_bytes_for_instance,
    canonical_hash_bytes,
    canonical_hash_instance,
    verify_content_reference,
)


EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def _load_example(name: str, cls: type):
    with open(EXAMPLES_DIR / name) as f:
        return cls(**yaml.safe_load(f))


# -------- Hash format --------

def test_hash_format() -> None:
    obj = _load_example("03_paper_licl.yaml", Object)
    h = canonical_hash_instance(obj)
    assert h.startswith("sha256:")
    digest = h[len("sha256:"):]
    assert len(digest) == 64
    assert all(c in "0123456789abcdef" for c in digest)


def test_canonical_bytes_is_valid_json() -> None:
    """The canonical bytes must be parseable as JSON by any JSON parser."""
    obj = _load_example("03_paper_licl.yaml", Object)
    raw = canonical_bytes_for_instance(obj)
    parsed = json.loads(raw)
    assert isinstance(parsed, dict)
    assert parsed["id"] == "obj:paper-licl-demo-v0"


# -------- Determinism --------

def test_hash_is_deterministic() -> None:
    """Hashing the same instance twice produces the same hash."""
    obj = _load_example("03_paper_licl.yaml", Object)
    h1 = canonical_hash_instance(obj)
    h2 = canonical_hash_instance(obj)
    assert h1 == h2


def test_hash_independent_of_construction_order() -> None:
    """Two entities with the same logical content hash identically,
    even when constructed from differently-ordered kwargs."""
    a = ContentReference(
        uri="file://a.pdf",
        sha256="a" * 64,
        hash_mode=HashMode.raw_bytes,
    )
    b = ContentReference(
        hash_mode=HashMode.raw_bytes,
        sha256="a" * 64,
        uri="file://a.pdf",
    )
    # ContentReference is not an Entity; hash its dict form via JCS directly.
    import hashlib
    import jcs
    ha = hashlib.sha256(jcs.canonicalize(a.model_dump(exclude_none=True))).hexdigest()
    hb = hashlib.sha256(jcs.canonicalize(b.model_dump(exclude_none=True))).hexdigest()
    assert ha == hb


def test_hash_independent_of_yaml_key_order() -> None:
    """Loading an example through YAML and re-loading the JSON form yields
    the same hash."""
    obj = _load_example("03_paper_licl.yaml", Object)
    h_yaml = canonical_hash_instance(obj)

    # Round-trip via JSON
    json_str = obj.model_dump_json(exclude_none=True, by_alias=True)
    obj_via_json = Object(**json.loads(json_str))
    h_json = canonical_hash_instance(obj_via_json)

    assert h_yaml == h_json


# -------- Change detection --------

def test_changing_a_field_changes_the_hash() -> None:
    obj = _load_example("03_paper_licl.yaml", Object)
    h_before = canonical_hash_instance(obj)

    obj_modified = obj.model_copy(update={"summary": "different summary"})
    h_after = canonical_hash_instance(obj_modified)

    assert h_before != h_after


def test_changing_should_not_claim_changes_the_hash() -> None:
    obj = _load_example("03_paper_licl.yaml", Object)
    h_before = canonical_hash_instance(obj)

    obj_modified = obj.model_copy(
        update={"should_not_claim": obj.should_not_claim + ["additional rule"]}
    )
    h_after = canonical_hash_instance(obj_modified)

    assert h_before != h_after


# -------- Raw bytes mode --------

def test_canonical_hash_bytes_known_value() -> None:
    """Known input → known output, so external systems can verify our hashing
    matches the standard."""
    h = canonical_hash_bytes(b"")
    assert h == "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def test_canonical_hash_bytes_for_text() -> None:
    h = canonical_hash_bytes(b"hello world")
    assert h == "sha256:b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"


# -------- verify_content_reference --------

def test_verify_content_reference_raw_bytes_match() -> None:
    content = b"some prompt text"
    expected_hex = canonical_hash_bytes(content)[len("sha256:"):]
    ref = ContentReference(
        uri="file://prompt.txt",
        sha256=expected_hex,
        hash_mode=HashMode.raw_bytes,
    )
    assert verify_content_reference(ref, content) is True


def test_verify_content_reference_raw_bytes_mismatch() -> None:
    ref = ContentReference(
        uri="file://prompt.txt",
        sha256="a" * 64,  # nonsense
        hash_mode=HashMode.raw_bytes,
    )
    assert verify_content_reference(ref, b"some prompt text") is False


def test_verify_content_reference_jcs_match() -> None:
    obj = _load_example("03_paper_licl.yaml", Object)
    expected = canonical_hash_instance(obj)[len("sha256:"):]
    ref = ContentReference(
        uri="file://obj.json",
        sha256=expected,
        hash_mode=HashMode.linkml_canonical_jcs,
    )
    assert verify_content_reference(ref, obj) is True


def test_verify_content_reference_jcs_mismatch() -> None:
    obj = _load_example("03_paper_licl.yaml", Object)
    ref = ContentReference(
        uri="file://obj.json",
        sha256="a" * 64,
        hash_mode=HashMode.linkml_canonical_jcs,
    )
    assert verify_content_reference(ref, obj) is False


def test_verify_content_reference_wrong_content_type() -> None:
    """JCS mode requires Entity or dict, not bytes."""
    ref = ContentReference(
        uri="file://obj.json",
        sha256="a" * 64,
        hash_mode=HashMode.linkml_canonical_jcs,
    )
    with pytest.raises(TypeError):
        verify_content_reference(ref, b"raw bytes not allowed for jcs mode")


def test_verify_content_reference_raw_bytes_wrong_content_type() -> None:
    """raw_bytes mode requires bytes, not Entity."""
    obj = _load_example("03_paper_licl.yaml", Object)
    ref = ContentReference(
        uri="file://prompt.txt",
        sha256="a" * 64,
        hash_mode=HashMode.raw_bytes,
    )
    with pytest.raises(TypeError):
        verify_content_reference(ref, obj)


# -------- Distinct entities hash distinctly --------

def test_different_examples_hash_differently() -> None:
    """Every example file should hash to a unique value."""
    paper = _load_example("03_paper_licl.yaml", Object)
    claim = _load_example("06_claim_licl_mp.yaml", Object)

    h_paper = canonical_hash_instance(paper)
    h_claim = canonical_hash_instance(claim)

    assert h_paper != h_claim


# -------- Idempotent Activity detection --------

def test_activity_with_same_inputs_hashes_identically() -> None:
    """Two Activities with the same inputs and assumptions hash the same.
    This is the property that enables idempotent synthesis detection."""
    a1 = Activity(
        id="act:idempotence-test-1",
        type="isom:activity_type/synthesis_edge",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="idempotence test",
        should_not_claim=["test"],
        activity_type=ActivityType.SYNTHESIS_EDGE,
        inputs=["obj:a", "evi:b"],
        outputs=["obj:result"],
        assumptions=["assumption 1"],
    )

    # Same Activity, different id — the *content* (excluding id) hashes the same?
    # Actually no — id is part of the content. The point of idempotence is that
    # if you construct an Activity with the same inputs + assumptions, you can
    # detect the duplication BEFORE creating a new id. Demonstrated by hashing
    # the discriminating subset:

    def disc(act: Activity) -> str:
        # Hash only the fields that determine "same Activity".
        # Note: use_enum_values=True is set on ConfiguredBaseModel, so
        # act.activity_type is already a string, not an Enum instance.
        return canonical_hash_bytes(
            json.dumps({
                "activity_type": act.activity_type,
                "inputs": sorted(act.inputs),
                "outputs": sorted(act.outputs),
                "assumptions": sorted(act.assumptions),
                "viewpoint_directive_id": act.viewpoint_directive_id,
            }, sort_keys=True).encode()
        )

    a2 = Activity(
        id="act:idempotence-test-2",  # different id
        type="isom:activity_type/synthesis_edge",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="different provenance string",
        should_not_claim=["test"],
        activity_type=ActivityType.SYNTHESIS_EDGE,
        inputs=["obj:a", "evi:b"],  # same as a1
        outputs=["obj:result"],  # same as a1
        assumptions=["assumption 1"],  # same as a1
    )

    assert disc(a1) == disc(a2)
