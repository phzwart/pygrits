"""
Viewpoint schema loading and materials-science example validation.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pygrits.resources import viewpoint_json_schema_path, viewpoint_schema_path
from pygrits.viewpoints import blank_slate_v0, document_extraction_v0, materials_science_v0
from pygrits.viewpoints.materials_science_v0 import (
    Activity,
    EvidenceRecord,
    MaterialsScienceScope,
    Object,
    ThermodynamicScope,
    ViewpointDirective,
)

MATERIALS_EXAMPLES_DIR = (
    Path(__file__).parent.parent
    / "viewpoints"
    / "materials_science_v0"
    / "examples"
)

MATERIALS_EXAMPLE_CLASSES = {
    "01_viewpoint_alkali_halide.yaml": ViewpointDirective,
    "02_paper_licl.yaml": Object,
    "03_evidence_licl_span.yaml": EvidenceRecord,
    "04_synthesis_activity.yaml": Activity,
    "05_claim_licl_mp.yaml": Object,
}


def test_materials_science_viewpoint_imports_cleanly() -> None:
    assert materials_science_v0.ThermodynamicScope is not None
    assert materials_science_v0.MaterialsScienceScope is not None


def test_blank_slate_viewpoint_imports_cleanly() -> None:
    assert blank_slate_v0.BlankSlateScope is not None


def test_document_extraction_viewpoint_imports_cleanly() -> None:
    assert document_extraction_v0.DocumentExtractionEvidenceType is not None


def test_thermodynamic_scope_subclass_validates() -> None:
    scope = ThermodynamicScope(
        scope_type="ThermodynamicScope",
        temperature_kelvin=300.0,
        pressure_pascal=101325.0,
    )
    assert scope.temperature_kelvin == 300.0


def test_materials_science_scope_composite_validates() -> None:
    scope = MaterialsScienceScope(
        scope_type="MaterialsScienceScope",
        thermodynamic=ThermodynamicScope(
            scope_type="ThermodynamicScope",
            pressure_pascal=101325.0,
        ),
    )
    assert scope.thermodynamic is not None
    assert scope.thermodynamic.pressure_pascal == 101325.0


def test_viewpoint_schema_paths_resolve() -> None:
    assert viewpoint_schema_path("materials_science_v0").exists()
    assert viewpoint_json_schema_path("materials_science_v0").exists()


@pytest.mark.parametrize("filename,cls", MATERIALS_EXAMPLE_CLASSES.items())
def test_materials_science_example_validates(filename: str, cls: type) -> None:
    path = MATERIALS_EXAMPLES_DIR / filename
    assert path.exists(), f"Example file not found: {path}"

    with open(path) as f:
        data = yaml.safe_load(f)

    instance = cls(**data)
    assert instance.id is not None
    assert instance.viewpoint_directive_id is not None
    assert instance.should_not_claim
    assert instance.provenance


def test_materials_synthesis_activity_links_inputs_and_outputs() -> None:
    with open(MATERIALS_EXAMPLES_DIR / "04_synthesis_activity.yaml") as f:
        data = yaml.safe_load(f)
    activity = Activity(**data)
    assert "obj:paper-licl-demo-v0" in activity.inputs
    assert "evi:span-licl-mp-v0" in activity.inputs
    assert "obj:claim-licl-mp-v0" in activity.outputs
