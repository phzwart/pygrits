# Entity

An **Entity** is a subject node: a claim, document, measurement, or plan element. It subclasses **Grit** and maps to `prov:Entity`.

Required on every grit: `id`, `viewpoint_id`. Optional integrity field `content_hash` is excluded from canonical hashing; use `stamp()` after construction.

## Typed domain content

Core `Entity` only carries structural slots:

- `summary` — short description (`dcterms:description`)
- `sources` — primary artifacts (`prov:hadPrimarySource`)
- `derived_from` — prior entity ids (`prov:wasDerivedFrom`)
- `evidence` — labelled links to `EvidenceRecord` ids
- `plan_variable` — optional P-Plan variable CURIE

Subclass `Entity` in a domain LinkML schema for scientific fields (temperature, k_cat, formula, …). Do not put JSON blobs in string slots.

## Evidence links

Each `EvidenceLink` has `evidence_id` and `label` (`direct`, `derived`, `inferred`, `unknown`). The label lives on the entity because one record may support multiple claims differently. `validate_bundle()` requires `rationale` when the label is `derived` or `inferred`.

## Provenance on the node

- `generated_by` — Activity id that produced this entity (`prov:wasGeneratedBy`)
- `agent` — software or person (`prov:wasAttributedTo`)
- `created_at` — timestamp (`prov:generatedAtTime`)
