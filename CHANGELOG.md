# Changelog

All notable changes to pygrits will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/) once v1.0 is reached;
until then, the schema may evolve without strict SemVer guarantees.

## [0.2.0] — 2026-05-27

**BREAKING** from v0.1.0.

### Changed

- **`Scope` is now an opaque marker in core.** The core defines no domain scope
  dimensions. Viewpoints subclass `Scope` in their own LinkML schemas to declare
  the scope commitments they populate. Core ships `NotesOnlyScope` for
  free-form notes only.
- **`EvidenceRecord.evidence_type` is now an open `CurieOrUri`.** No core-supplied
  permissible values; viewpoints supply evidence-type vocabulary.
- **Top-level `pygrits` re-exports shrink.** Domain-specific scope classes and
  `EvidenceTypeBase` are no longer exported from `pygrits`. Import them from
  viewpoint modules (e.g. `pygrits.viewpoints.materials_science_v0`).
- **Examples reorganized.** Core-level examples in `examples/` are now
  viewpoint-neutral and validate against the bare core schema. Alkali-halide
  thermodynamics examples moved to
  `viewpoints/materials_science_v0/examples/`.

### Removed from core

- `ThermodynamicScope`, `TemporalScope`, `BiologicalScope`, `CompositionalScope`,
  `StatisticalScope`, `MethodologicalScope`, `SpatialScope` — moved to
  `pygrits.viewpoints.materials_science_v0`.
- `EvidenceTypeBase` enum — removed entirely.

### Added

- **`viewpoints/` directory** with three example viewpoint schemas:
  - `blank_slate_v0` — no domain vocabulary; bootstrap-honest.
  - `document_extraction_v0` — document-extraction evidence-type CURIEs
    (`de:text_span`, `de:figure`, etc.).
  - `materials_science_v0` — materials-science scope dimensions and composite
    `MaterialsScienceScope`.
- **Generated viewpoint Pydantic modules** under `pygrits.viewpoints.*`,
  importable as e.g. `from pygrits.viewpoints.materials_science_v0 import ThermodynamicScope`.
- **`viewpoint_schema_path()` / `viewpoint_json_schema_path()`** resource helpers.
- **Regression tests** confirming core alone defines no domain vocabulary and
  that `evidence_type` accepts arbitrary CURIEs.

## [0.1.0] — 2026-05-27

Initial public draft. **Alpha — schema may break between commits.**

### Added

- **LinkML core schema** (`src/pygrits/core.yaml`) defining the ISOM v0.1
  vertical slice:
  - Abstract `Entity` base carrying the discipline contract.
  - Three concrete entity classes: `Object`, `Activity`, `EvidenceRecord`.
  - Specializations: `ViewpointDirective` (Object), `NegativeEvidenceRecord`
    (EvidenceRecord).
  - `ContentReference` primitive with mandatory `sha256` and `hash_mode`.
  - `Scope` as a composite of seven optional scope-dimension classes.
  - Seven `Locator` subtypes (CharRange, Bbox, SequencePosition,
    ProcessingLogLine, TableCell, FileRegion, Composite).
  - `Confidence` with calibration metadata.
  - `CompatibilityJudgment`.
  - Enums: `HashMode`, `ActivityType` (the seven hyperedge types),
    `LifecycleState`, `ReviewState`, `EpistemicStatus`, `LineageType`,
    `RefusalState` (five-state taxonomy), `CompatibilityStatus`,
    `ConfidenceBasis`, `EvidenceTypeBase`.
  - Subsets: `MVE`, `ParticipationReady`, `Full`.
- **Generated Pydantic models** (`src/pygrits/core.py`) with `extra="forbid"`,
  field validators on patterns, and proper inheritance.
- **Generated JSON Schema** (`src/pygrits/core.schema.json`) for
  non-Python validators.
- **Canonical-form helpers** (`src/pygrits/canonical.py`):
  - `canonical_hash_instance(entity)` — RFC 8785 JCS over Pydantic JSON dump,
    SHA-256.
  - `canonical_hash_bytes(data)` — SHA-256 of raw bytes.
  - `verify_content_reference(ref, content)` — dispatches on `hash_mode`.
  - `canonical_bytes_for_instance(entity)` — exposes the canonical bytes
    directly.
- **Six example instances** (`examples/`) exercising the vertical slice:
  the bootstrap meta-viewpoint, an alkali-halide thermodynamics viewpoint,
  a paper Object, an EvidenceRecord with CharRangeLocator, a SYNTHESIS_EDGE
  Activity, and the claim Object the Activity produces.
- **Test suite** (40 tests):
  - All examples validate against their declared classes.
  - Negative tests confirm MVE field requirements, sha256 pattern,
    `extra="forbid"`.
  - Canonical-form round-trip tests prove hash stability and change
    detection under both hash modes.
- **GitHub Actions CI** with three jobs: test (Python 3.11, 3.12),
  schema-consistency (regenerate and diff), lint (ruff).
- **Regeneration script** (`scripts/regenerate.sh`) for rebuilding Pydantic,
  JSON Schema, and docs from the LinkML source.
- **Auto-generated Markdown docs** (`docs/`).

### Known limitations

- `features` and `normalized_payload` are typed as `string` with the
  convention that the content is serialized JSON whose shape is determined
  by the viewpoint. Future versions may use viewpoint-declared LinkML
  profiles to type these payloads explicitly.
- Provenance is a free-form string for v0.1. Structured provenance
  (PROV-O-aligned) is deferred.
- The bootstrap meta-viewpoint is self-referential; this is intentional
  but not enforced as a DAG-validity constraint by the schema.
- Speech acts, reactions, threads, communities, wiki statements, and the
  harmonization process are not yet modeled — deferred to v0.2.

[0.2.0]: https://example.com/pygrits/releases/tag/v0.2.0
[0.1.0]: https://example.com/pygrits/releases/tag/v0.1.0
