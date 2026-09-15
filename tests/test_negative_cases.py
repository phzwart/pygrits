"""
Negative tests: confirm that violations of the discipline contract fail.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from pygrits import (
    Activity,
    ActivityType,
    BundleValidationError,
    CharRangeLocator,
    ContentReference,
    Entity,
    EvidenceRecord,
    HashMode,
    LineRangeLocator,
    ViewpointDirective,
    validate_bundle,
)


def test_entity_missing_viewpoint_fails() -> None:
    with pytest.raises(ValidationError):
        Entity(id="ent:test", summary="x")


def test_entity_missing_id_fails() -> None:
    with pytest.raises(ValidationError):
        Entity(viewpoint_id="vpt:meta-v0")


def test_activity_missing_inputs_fails() -> None:
    with pytest.raises(ValidationError):
        Activity(
            id="act:test",
            viewpoint_id="vpt:meta-v0",
            activity_type=ActivityType.derivation,
        )


def test_evidence_record_missing_locator_fails() -> None:
    with pytest.raises(ValidationError):
        EvidenceRecord(
            id="evi:test",
            viewpoint_id="vpt:meta-v0",
            source=ContentReference(
                uri="file://test.pdf",
                sha256="a" * 64,
                hash_mode=HashMode.raw_bytes,
            ),
        )


def test_malformed_sha256_fails() -> None:
    vpt = ViewpointDirective(id="vpt:t", viewpoint_id="vpt:t", name="t")
    er = EvidenceRecord(
        id="evi:t",
        viewpoint_id="vpt:t",
        source=ContentReference(
            uri="file://test.pdf",
            sha256="not_a_sha256",
            hash_mode=HashMode.raw_bytes,
        ),
        locator=CharRangeLocator(
            locator_type="CharRangeLocator",
            char_start=0,
            char_end=1,
        ),
    )
    with pytest.raises(BundleValidationError, match="sha256"):
        validate_bundle([vpt, er])


def test_extra_field_fails() -> None:
    with pytest.raises(ValidationError):
        Entity(
            id="ent:test",
            viewpoint_id="vpt:meta-v0",
            nonsense_field="not allowed",
        )


def test_minimal_entity_validates() -> None:
    ent = Entity(id="ent:minimal-test", viewpoint_id="vpt:meta-v0")
    assert ent.id == "ent:minimal-test"


def test_minimal_activity_validates() -> None:
    act = Activity(
        id="act:minimal-test",
        viewpoint_id="vpt:meta-v0",
        activity_type=ActivityType.derivation,
        inputs=["ent:some-input"],
    )
    assert act.activity_type == ActivityType.derivation


def test_line_range_locator_validates() -> None:
    loc = LineRangeLocator(
        locator_type="LineRangeLocator",
        path="src/foo.py",
        line_start=1,
        line_end=10,
    )
    assert loc.path == "src/foo.py"


def test_minimal_evidence_record_validates() -> None:
    er = EvidenceRecord(
        id="evi:minimal-test",
        viewpoint_id="vpt:meta-v0",
        source=ContentReference(
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
