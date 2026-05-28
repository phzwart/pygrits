"""
Negative tests: confirm that violations of the discipline contract fail.

If any of these tests pass without raising ValidationError, the schema
or the generated Pydantic has regressed and the system is no longer
enforcing the discipline it claims to enforce.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from pygrits import (
    Activity,
    ActivityType,
    BboxLocator,
    CharRangeLocator,
    ContentReference,
    EvidenceRecord,
    HashMode,
    Object,
)

# -------- Missing MVE fields --------

def test_object_missing_viewpoint_fails() -> None:
    with pytest.raises(ValidationError):
        Object(
            id="obj:test",
            type="isom:paper",
            # viewpoint_directive_id missing
            provenance="test",
            should_not_claim=["test"],
            source_artifact_refs=[],
            evidence_record_ids=[],
        )


def test_object_missing_should_not_claim_fails() -> None:
    with pytest.raises(ValidationError):
        Object(
            id="obj:test",
            type="isom:paper",
            viewpoint_directive_id="vpt:meta-v0",
            provenance="test",
            # should_not_claim missing
            source_artifact_refs=[],
            evidence_record_ids=[],
        )


def test_object_missing_id_fails() -> None:
    with pytest.raises(ValidationError):
        Object(
            # id missing
            type="isom:paper",
            viewpoint_directive_id="vpt:meta-v0",
            provenance="test",
            should_not_claim=["test"],
            source_artifact_refs=[],
            evidence_record_ids=[],
        )


def test_activity_missing_inputs_fails() -> None:
    with pytest.raises(ValidationError):
        Activity(
            id="act:test",
            type="isom:activity_type/synthesis_edge",
            viewpoint_directive_id="vpt:meta-v0",
            provenance="test",
            should_not_claim=["test"],
            activity_type=ActivityType.SYNTHESIS_EDGE,
            # inputs missing
        )


def test_evidence_record_missing_locator_fails() -> None:
    with pytest.raises(ValidationError):
        EvidenceRecord(
            id="evi:test",
            type="isom:text_span",
            viewpoint_directive_id="vpt:meta-v0",
            provenance="test",
            should_not_claim=["test"],
            source_artifact_ref=ContentReference(
                uri="file://test.pdf",
                sha256="a" * 64,
                hash_mode=HashMode.raw_bytes,
            ),
            # locator missing
        )


# -------- Malformed values --------

def test_malformed_sha256_fails() -> None:
    with pytest.raises(ValidationError):
        ContentReference(
            uri="file://test.pdf",
            sha256="not_a_sha256",
            hash_mode=HashMode.raw_bytes,
        )


def test_short_sha256_fails() -> None:
    with pytest.raises(ValidationError):
        ContentReference(
            uri="file://test.pdf",
            sha256="abc123",  # too short
            hash_mode=HashMode.raw_bytes,
        )


def test_uppercase_sha256_fails() -> None:
    with pytest.raises(ValidationError):
        ContentReference(
            uri="file://test.pdf",
            sha256="A" * 64,  # uppercase rejected by pattern
            hash_mode=HashMode.raw_bytes,
        )


def test_content_reference_missing_hash_mode_fails() -> None:
    with pytest.raises(ValidationError):
        ContentReference(
            uri="file://test.pdf",
            sha256="a" * 64,
            # hash_mode missing
        )


# -------- Strict extra="forbid" check --------

def test_extra_field_fails() -> None:
    """Pydantic models are configured with extra='forbid' — sneaking in
    undeclared fields should fail."""
    with pytest.raises(ValidationError):
        Object(
            id="obj:test",
            type="isom:paper",
            viewpoint_directive_id="vpt:meta-v0",
            provenance="test",
            should_not_claim=["test"],
            source_artifact_refs=[],
            evidence_record_ids=[],
            nonsense_field="this should not be accepted",
        )


# -------- Valid minimal construction --------

def test_minimal_object_validates() -> None:
    """An Object meeting the MVE contract must validate."""
    obj = Object(
        id="obj:minimal-test",
        type="isom:paper",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="minimal test",
        should_not_claim=["test should_not_claim"],
        source_artifact_refs=[],
        evidence_record_ids=[],
    )
    assert obj.id == "obj:minimal-test"


def test_minimal_activity_validates() -> None:
    """An Activity meeting the MVE contract must validate."""
    act = Activity(
        id="act:minimal-test",
        type="isom:activity_type/synthesis_edge",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="minimal test",
        should_not_claim=["test"],
        activity_type=ActivityType.SYNTHESIS_EDGE,
        inputs=["obj:some-input"],
    )
    assert act.activity_type == ActivityType.SYNTHESIS_EDGE


def test_minimal_evidence_record_validates() -> None:
    """An EvidenceRecord meeting the MVE contract must validate."""
    er = EvidenceRecord(
        id="evi:minimal-test",
        type="isom:text_span",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="minimal test",
        should_not_claim=["test"],
        source_artifact_ref=ContentReference(
            uri="file://test.pdf",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        ),
        locator=CharRangeLocator(
            locator_type="CharRangeLocator",
            char_start=0,
            char_end=100,
        ),
    )
    assert er.locator.char_start == 0


def test_bbox_locator_validates() -> None:
    """Alternative Locator subclass works through the polymorphic slot."""
    bbox = BboxLocator(
        locator_type="BboxLocator",
        page=1,
        bbox_x0=0.0,
        bbox_y0=0.0,
        bbox_x1=100.0,
        bbox_y1=200.0,
    )
    assert bbox.page == 1
