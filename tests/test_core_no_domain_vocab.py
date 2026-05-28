"""
Regression guard: the core schema must not define domain vocabulary.

If ThermodynamicScope, temperature_kelvin, or EvidenceTypeBase reappear in
pygrits.core, the core-vs-viewpoint boundary has been violated.
"""

from __future__ import annotations

import pytest

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


def test_core_module_has_no_domain_scope_classes() -> None:
    for name in DOMAIN_SYMBOLS:
        assert not hasattr(pygrits.core, name), (
            f"pygrits.core must not define domain symbol {name!r}"
        )


def test_top_level_package_does_not_reexport_domain_symbols() -> None:
    for name in DOMAIN_SYMBOLS:
        assert not hasattr(pygrits, name), (
            f"pygrits top-level must not re-export domain symbol {name!r}"
        )
        assert name not in pygrits.__all__, (
            f"pygrits.__all__ must not include domain symbol {name!r}"
        )


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
        assert token not in core_yaml_text, (
            f"core.yaml must not contain domain token {token!r}"
        )


def test_shipped_core_yaml_contains_no_paper_semantics(core_yaml_text: str) -> None:
    """Document-level paper semantics belong to viewpoint vocabularies, not core.

    ExtractionProfile references content kinds only as opaque CURIEs, so these
    document terms must never appear as literals in the core schema. (`section`
    is excluded: it is a generic LocatorFidelity value; `citation` is excluded:
    it appears in the cited_from description; `table` is excluded: it is the
    structural TableCellLocator.)
    """
    forbidden = (
        "figure",
        "equation",
        "measurement",
    )
    lowered = core_yaml_text.lower()
    for token in forbidden:
        assert token not in lowered, (
            f"core.yaml must not contain paper-semantic token {token!r}"
        )


def test_core_still_exports_structural_primitives() -> None:
    for name in (
        "Grit",
        "Object",
        "Activity",
        "EvidenceRecord",
        "Scope",
        "NotesOnlyScope",
        "CharRangeLocator",
        "HashMode",
        "ActivityType",
    ):
        assert hasattr(pygrits, name)
        assert name in pygrits.__all__
