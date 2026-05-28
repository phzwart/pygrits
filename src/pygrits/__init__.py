"""
pygrits — raisins in the pudding.

Evidence-grounded scientific entities with viewpoint-aware refusal.

Python implementation of the ISOM schema (Interactive Scientific Object Model)
for structured epistemic containment in agentic scientific reasoning.
"""

__version__ = "0.2.0"

# Re-export the entity classes
# Canonicalization helpers
from pygrits.canonical import (
    canonical_bytes_for_instance,
    canonical_hash_bytes,
    canonical_hash_instance,
    verify_content_reference,
)
from pygrits.core import (
    Activity,
    ActivityType,
    BboxLocator,
    CharRangeLocator,
    CompatibilityJudgment,
    CompatibilityStatus,
    CompositeLocator,
    Confidence,
    ConfidenceBasis,
    # Primitives
    ContentReference,
    # Abstract base
    Entity,
    EpistemicStatus,
    EvidenceRecord,
    FileRegionLocator,
    # Enums
    HashMode,
    LifecycleState,
    LineageType,
    Locator,
    NegativeEvidenceRecord,
    NotesOnlyScope,
    # Concrete entity classes
    Object,
    ProcessingLogLineLocator,
    RefusalState,
    ReviewState,
    Scope,
    SequencePositionLocator,
    TableCellLocator,
    ViewpointDirective,
)

# Schema file path for runtime validators that want it
from pygrits.resources import (
    json_schema_path,
    schema_path,
    viewpoint_json_schema_path,
    viewpoint_schema_path,
)

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
    "NotesOnlyScope",
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
    # Canonicalization
    "canonical_hash_instance",
    "canonical_hash_bytes",
    "verify_content_reference",
    "canonical_bytes_for_instance",
    # Resources
    "schema_path",
    "json_schema_path",
    "viewpoint_schema_path",
    "viewpoint_json_schema_path",
]
