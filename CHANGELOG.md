# Changelog

## 0.6.0 — 2026-09-15

Breaking. The package is a PROV-O + Web Annotation emit profile and validator. Invented core classes are gone.

### Removed

- LinkML `core.yaml` and generated `core.py` / JSON Schema / JSON-LD context
- `Grit`, `ViewpointDirective`, `EvidenceRecord`, `NegativeEvidenceRecord`, `EvidenceLink`, locator classes
- Viewpoint package and `document_extraction_v0`
- RDF dumper, `scripts/regenerate.sh`, composition / ISOM / domain-vocab guards
- YAML example bundle

### Replaced by

- `PROFILE.md` — agent directive
- `context.jsonld` — existing terms only (`prov`, `oa`, `dcterms`)
- `schema.json` — closed emit shape
- `Plan` / `Entity` / `Activity` Pydantic models (`prov:Plan`, `prov:Entity`, `prov:Activity`)
- `load`, `dump`, `validate`, `stamp`, `profile_text`

### Rules `validate()` still enforces

- Referenced ids exist; `plan` must be a `prov:Plan`
- `how` of `derived` / `inferred` requires `rationale`
- `how` of `quote` requires `source` and `target`
- `support` / `contradiction` must not `generated`

## 0.5.0 — 2026-09-15

Breaking release. No compatibility with 0.4.

### Removed classes

`Object`, `Composable`, `OperationalLayer`, `ExtractionProfile`, `VocabularyPack`, `ReasoningPolicy`, `ComposedViewpointDirective`, `CompatibilityJudgment`, `ProcessingLogLineLocator`.

### Removed enums

`CompositionMode`, `ExtractionGranularity`, `EvidenceDensity`, `LocatorFidelity`, `EpistemicStatus`, `RefusalState`, `LifecycleState`, `LineageType`, `CompatibilityStatus`.

### Removed slots

**Former `Object` / now `Entity`:** `features`, `payload_schema`, `observations`, `unspecified_items`, `reported_claims`, `methods`, `assumptions`, `uncertainties`, `synthesis_link_ids`, `operation_link_ids`, `instance_of`, `type`, `source_artifact_refs`, `evidence_record_ids`.

**`EvidenceRecord`:** `normalized_payload`, `payload_schema`, `lineage`, `cited_from`, `instance_of`, `source_artifact_ref`.

**`Activity`:** `compatibility_judgments`, `assumptions`, `admissibility_rationale`, `type`.

**`Grit` (all nodes):** `provenance`, `generation_mode`, `lifecycle_state`, required `should_not_claim`, `viewpoint_directive_id`, `type`.

**`ViewpointDirective`:** `parent_viewpoint_ids`, `composition_mode`, `abstraction_level`, `directive_name`, and composition-related source/parent slots.

### Renames and replacements

- `Object` → `Entity` (`prov:Entity`)
- `viewpoint_directive_id` → `viewpoint_id`
- `should_not_claim` → optional `caveats`
- `provenance` string → `generated_by`, `agent`, `created_at`
- `source_artifact_ref(s)` → `source` / `sources`
- `evidence_record_ids` → `Entity.evidence` (`EvidenceLink` with `EvidenceLabel`)
- `ActivityType` values: `derivation`, `support`, `contradiction`, `adjudication` (replacing `SYNTHESIS_EDGE`, `SUPPORT_EDGE`, etc.)

### Added

- `LineRangeLocator`, `EvidenceLink`, `EvidenceLabel`, `NegativeResult` (enum values unchanged)
- `content_hash`, `compute_content_hash`, `stamp`, `validate_bundle`, `pygrits.rdf.to_graph`
- `core.context.jsonld`; JSON-LD context generation in `scripts/regenerate.sh`
- Single shipped viewpoint: `document_extraction_v0`

### Removed packages / docs

- `viewpoint_resolution.py`, all viewpoints except `document_extraction_v0`, committed `docs/`, composition guides, materials/coordination/paper/blank_slate viewpoints and examples.
