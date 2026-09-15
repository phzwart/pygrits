"""
Verify the shipped example bundle loads and passes bundle validation.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from pygrits import (
    Activity,
    Entity,
    EvidenceRecord,
    NegativeEvidenceRecord,
    ViewpointDirective,
    validate_bundle,
)

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"

EXAMPLE_SPECS: tuple[tuple[str, type], ...] = (
    ("01_viewpoint.yaml", ViewpointDirective),
    ("02_evidence_line_range.yaml", EvidenceRecord),
    ("03_negative_evidence.yaml", NegativeEvidenceRecord),
    ("04_derivation_activity.yaml", Activity),
    ("05_entity_kcat_landscape.yaml", Entity),
)


def _load(name: str, cls: type):
    with open(EXAMPLES_DIR / name) as f:
        return cls(**yaml.safe_load(f))


def test_all_examples_present() -> None:
    on_disk = {p.name for p in EXAMPLES_DIR.glob("*.yaml")}
    declared = {name for name, _ in EXAMPLE_SPECS}
    assert on_disk == declared


def test_example_bundle_validates() -> None:
    grits = [_load(name, cls) for name, cls in EXAMPLE_SPECS]
    validate_bundle(grits)


def test_derivation_activity_links_bundle() -> None:
    activity = _load("04_derivation_activity.yaml", Activity)
    assert activity.outputs == ["ent:kcat-landscape-v0"]
    assert "evi:source-line-range-v0" in activity.inputs
