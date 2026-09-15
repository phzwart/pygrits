"""
Regression guard: the core schema must not define domain vocabulary.
"""

from __future__ import annotations

import re

import pytest
import yaml

import pygrits
import pygrits.core
from pygrits.resources import schema_path

DOMAIN_SYMBOLS = (
    "ThermodynamicScope",
    "TemporalScope",
    "BiologicalScope",
    "CompositionalScope",
    "StatisticalScope",
    "MethodologicalScope",
    "SpatialScope",
    "EvidenceTypeBase",
    "Pressure",
    "temperature_kelvin",
    "pressure_pascal",
)


@pytest.fixture
def core_yaml_text() -> str:
    return schema_path().read_text()


@pytest.fixture
def core_schema() -> dict:
    return yaml.safe_load(schema_path().read_text())


def test_core_module_has_no_domain_scope_classes() -> None:
    for name in DOMAIN_SYMBOLS:
        assert not hasattr(pygrits.core, name)


def test_top_level_package_does_not_reexport_domain_symbols() -> None:
    for name in DOMAIN_SYMBOLS:
        assert not hasattr(pygrits, name)
        assert name not in pygrits.__all__


def test_shipped_core_yaml_contains_no_domain_tokens(core_yaml_text: str) -> None:
    forbidden = (
        "ThermodynamicScope",
        "temperature_kelvin",
        "pressure_pascal",
        "EvidenceTypeBase",
        "organism:",
        "formula:",
    )
    for token in forbidden:
        assert token not in core_yaml_text


def test_no_json_string_payload_slots(core_schema: dict) -> None:
    """Slots must not smuggle JSON blobs via string + JSON in the description."""
    classes = core_schema.get("classes") or {}
    for cls_name, cls_def in classes.items():
        for slot_name, slot_def in (cls_def.get("attributes") or {}).items():
            if not isinstance(slot_def, dict):
                continue
            if slot_def.get("range") != "string":
                continue
            desc = (slot_def.get("description") or "").lower()
            assert "json" not in desc, (
                f"{cls_name}.{slot_name} looks like a JSON-in-string payload slot"
            )


def test_core_still_exports_structural_primitives() -> None:
    for name in (
        "Grit",
        "Entity",
        "Activity",
        "EvidenceRecord",
        "Scope",
        "NotesOnlyScope",
        "CharRangeLocator",
        "LineRangeLocator",
        "HashMode",
        "ActivityType",
    ):
        assert hasattr(pygrits, name)
        assert name in pygrits.__all__
