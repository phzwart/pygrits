# Changelog

All notable changes to pygrits will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/) once v1.0 is reached;
until then, the schema may evolve without strict SemVer guarantees.

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

[0.1.0]: https://example.com/pygrits/releases/tag/v0.1.0
