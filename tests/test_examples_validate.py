"""
Verify every shipped example YAML loads as a valid Pydantic instance of
its declared class.

This catches: schema-example drift, gen-pydantic regressions, and
required-field violations on the example side.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pygrits import (
    Activity,
    EvidenceRecord,
    Object,
    ViewpointDirective,
)


EXAMPLES_DIR = Path(__file__).parent.parent / "examples"

# Map example filename → expected Pydantic class
EXAMPLE_CLASSES = {
    "01_viewpoint_meta.yaml": ViewpointDirective,
    "02_viewpoint_alkali_halide.yaml": ViewpointDirective,
    "03_paper_licl.yaml": Object,
    "04_evidence_licl_span.yaml": EvidenceRecord,
    "05_synthesis_activity.yaml": Activity,
    "06_claim_licl_mp.yaml": Object,
}


@pytest.mark.parametrize("filename,cls", EXAMPLE_CLASSES.items())
def test_example_validates(filename: str, cls: type) -> None:
    path = EXAMPLES_DIR / filename
    assert path.exists(), f"Example file not found: {path}"

    with open(path) as f:
        data = yaml.safe_load(f)

    instance = cls(**data)
    assert instance.id is not None
    assert instance.viewpoint_directive_id is not None
    assert instance.should_not_claim, "should_not_claim must be non-empty"
    assert instance.provenance


def test_all_examples_present() -> None:
    """Guard against silent example deletion."""
    on_disk = {p.name for p in EXAMPLES_DIR.glob("*.yaml")}
    declared = set(EXAMPLE_CLASSES.keys())
    assert on_disk == declared, (
        f"Example set drift: on disk {on_disk}, declared {declared}"
    )


def test_synthesis_activity_consumes_paper_and_evidence() -> None:
    """The synthesis Activity must reference the paper and the evidence."""
    with open(EXAMPLES_DIR / "05_synthesis_activity.yaml") as f:
        data = yaml.safe_load(f)
    activity = Activity(**data)
    assert "obj:paper-licl-demo-v0" in activity.inputs
    assert "evi:span-licl-mp-v0" in activity.inputs
    assert "obj:claim-licl-mp-v0" in activity.outputs


def test_claim_object_links_back_to_activity() -> None:
    """The output claim Object must back-link to the synthesis Activity."""
    with open(EXAMPLES_DIR / "06_claim_licl_mp.yaml") as f:
        data = yaml.safe_load(f)
    claim = Object(**data)
    assert "act:synth-licl-mp-v0" in claim.synthesis_link_ids
