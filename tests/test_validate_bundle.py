"""Tests for validate_bundle semantic checks."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pygrits import (
    Activity,
    ActivityType,
    BundleValidationError,
    Entity,
    EvidenceLabel,
    EvidenceLink,
    ViewpointDirective,
    validate_bundle,
)

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def _load_example_bundle():
    from pygrits import EvidenceRecord, NegativeEvidenceRecord

    mapping = (
        ("01_viewpoint.yaml", ViewpointDirective),
        ("02_evidence_line_range.yaml", EvidenceRecord),
        ("03_negative_evidence.yaml", NegativeEvidenceRecord),
        ("04_derivation_activity.yaml", Activity),
        ("05_entity_kcat_landscape.yaml", Entity),
    )
    grits = []
    for name, cls in mapping:
        with open(EXAMPLES_DIR / name) as f:
            grits.append(cls(**yaml.safe_load(f)))
    return grits


def test_valid_example_bundle_passes() -> None:
    validate_bundle(_load_example_bundle())


def test_dangling_id_fails() -> None:
    grits = _load_example_bundle()
    ent = grits[-1]
    bad = ent.model_copy(
        update={
            "evidence": [
                EvidenceLink(
                    evidence_id="evi:missing",
                    label=EvidenceLabel.direct,
                )
            ]
        }
    )
    grits[-1] = bad
    with pytest.raises(BundleValidationError, match="missing id"):
        validate_bundle(grits)


def test_derived_without_rationale_fails() -> None:
    vpt = ViewpointDirective(id="vpt:x", viewpoint_id="vpt:x", name="n")
    evi_id = "evi:only"
    from pygrits import ContentReference, EvidenceRecord, HashMode, LineRangeLocator

    evi = EvidenceRecord(
        id=evi_id,
        viewpoint_id="vpt:x",
        source=ContentReference(
            uri="file://t",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        ),
        locator=LineRangeLocator(
            locator_type="LineRangeLocator",
            path="p",
            line_start=1,
            line_end=2,
        ),
    )
    ent = Entity(
        id="ent:y",
        viewpoint_id="vpt:x",
        evidence=[
            EvidenceLink(
                evidence_id=evi_id,
                label=EvidenceLabel.derived,
            )
        ],
    )
    with pytest.raises(BundleValidationError, match="requires rationale"):
        validate_bundle([vpt, evi, ent])


def test_support_with_outputs_fails() -> None:
    vpt = ViewpointDirective(id="vpt:x", viewpoint_id="vpt:x", name="n")
    act = Activity(
        id="act:s",
        viewpoint_id="vpt:x",
        activity_type=ActivityType.support,
        inputs=["ent:a"],
        outputs=["ent:b"],
    )
    ent_a = Entity(id="ent:a", viewpoint_id="vpt:x")
    ent_b = Entity(id="ent:b", viewpoint_id="vpt:x")
    with pytest.raises(BundleValidationError, match="must not have outputs"):
        validate_bundle([vpt, ent_a, ent_b, act])
