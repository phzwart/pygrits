"""
pygrits — raisins in the pudding.

Evidence-grounded scientific entities with viewpoint-aware refusal.

Python implementation of the ISOM schema (Interactive Scientific Object Model)
for structured epistemic containment in agentic scientific reasoning.
"""

__version__ = "0.1.0"

# Re-export the entity classes
from pygrits.core import (
    # Abstract base
    Entity,
    # Concrete entity classes
    Object,
    Activity,
    EvidenceRecord,
    ViewpointDirective,
    NegativeEvidenceRecord,
    # Primitives
    ContentReference,
    Scope,
    ThermodynamicScope,
    TemporalScope,
    BiologicalScope,
    CompositionalScope,
    StatisticalScope,
    MethodologicalScope,
    SpatialScope,
    Locator,
    CharRangeLocator,
    BboxLocator,
    SequencePositionLocator,
    ProcessingLogLineLocator,
    TableCellLocator,
    FileRegionLocator,
    CompositeLocator,
    Confidence,
    CompatibilityJudgment,
    # Enums
    HashMode,
    ActivityType,
    LifecycleState,
    ReviewState,
    EpistemicStatus,
    LineageType,
    RefusalState,
    CompatibilityStatus,
    ConfidenceBasis,
    EvidenceTypeBase,
)

# Canonicalization helpers
from pygrits.canonical import (
    canonical_hash_instance,
    canonical_hash_bytes,
    verify_content_reference,
    canonical_bytes_for_instance,
)

# Schema file path for runtime validators that want it
from pygrits.resources import schema_path, json_schema_path

__all__ = [
    "__version__",
    # Entity classes
    "Entity",
    "Object",
    "Activity",
    "EvidenceRecord",
    "ViewpointDirective",
    "NegativeEvidenceRecord",
    # Primitives
    "ContentReference",
    "Scope",
    "ThermodynamicScope",
    "TemporalScope",
    "BiologicalScope",
    "CompositionalScope",
    "StatisticalScope",
    "MethodologicalScope",
    "SpatialScope",
    "Locator",
    "CharRangeLocator",
    "BboxLocator",
    "SequencePositionLocator",
    "ProcessingLogLineLocator",
    "TableCellLocator",
    "FileRegionLocator",
    "CompositeLocator",
    "Confidence",
    "CompatibilityJudgment",
    # Enums
    "HashMode",
    "ActivityType",
    "LifecycleState",
    "ReviewState",
    "EpistemicStatus",
    "LineageType",
    "RefusalState",
    "CompatibilityStatus",
    "ConfidenceBasis",
    "EvidenceTypeBase",
    # Canonicalization
    "canonical_hash_instance",
    "canonical_hash_bytes",
    "verify_content_reference",
    "canonical_bytes_for_instance",
    # Resources
    "schema_path",
    "json_schema_path",
]
