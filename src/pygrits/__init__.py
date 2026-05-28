"""
pygrits — raisins in the pudding.

Evidence-grounded scientific grits with viewpoint-aware refusal.

Python implementation of the pygrits core schema for structured epistemic
containment in agentic scientific reasoning.
"""

__version__ = "0.3.0"

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
    ContentReference,
    EpistemicStatus,
    EvidenceRecord,
    FileRegionLocator,
    Grit,
    HashMode,
    LifecycleState,
    LineageType,
    Locator,
    NegativeEvidenceRecord,
    NotesOnlyScope,
    Object,
    ProcessingLogLineLocator,
    RefusalState,
    ReviewState,
    Scope,
    SequencePositionLocator,
    TableCellLocator,
    ViewpointDirective,
)
from pygrits.resources import (
    json_schema_path,
    schema_path,
    viewpoint_json_schema_path,
    viewpoint_schema_path,
)

__all__ = [
    "__version__",
    "Grit",
    "Object",
    "Activity",
    "EvidenceRecord",
    "ViewpointDirective",
    "NegativeEvidenceRecord",
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
    "HashMode",
    "ActivityType",
    "LifecycleState",
    "ReviewState",
    "EpistemicStatus",
    "LineageType",
    "RefusalState",
    "CompatibilityStatus",
    "ConfidenceBasis",
    "canonical_hash_instance",
    "canonical_hash_bytes",
    "verify_content_reference",
    "canonical_bytes_for_instance",
    "schema_path",
    "json_schema_path",
    "viewpoint_schema_path",
    "viewpoint_json_schema_path",
]
