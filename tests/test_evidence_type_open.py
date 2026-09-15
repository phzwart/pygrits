"""
Confirm EvidenceRecord.evidence_type is an open CURIE under bare core.
"""

from __future__ import annotations

from pygrits import (
    CharRangeLocator,
    ContentReference,
    EvidenceRecord,
    HashMode,
)


def _minimal_evidence(**overrides: object) -> EvidenceRecord:
    base = dict(
        id="evi:open-curie-test",
        viewpoint_id="vpt:meta-v0",
        source=ContentReference(
            uri="file://test.pdf",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        ),
        locator=CharRangeLocator(
            locator_type="CharRangeLocator",
            char_start=0,
            char_end=10,
        ),
    )
    base.update(overrides)
    return EvidenceRecord(**base)


def test_arbitrary_curie_evidence_type_validates() -> None:
    er = _minimal_evidence(evidence_type="any-arbitrary-curie:value")
    assert er.evidence_type == "any-arbitrary-curie:value"


def test_viewpoint_curie_evidence_type_validates_under_core() -> None:
    er = _minimal_evidence(evidence_type="de:text_span")
    assert er.evidence_type == "de:text_span"
