# EvidenceRecord

An **EvidenceRecord** anchors a statement in a source artifact. It subclasses **Grit** and is also typed as `prov:Entity` (evidence-as-entity).

## Required fields

- `source` — `ContentReference` (`uri`, `sha256`, `hash_mode`)
- `locator` — typed pointer into the artifact (char range, line range, bbox, table cell, …)

Optional: `extracted_content`, `evidence_type` (viewpoint CURIE, e.g. `de:text_span`), `extraction_confidence`.

## Locators

Use **LineRangeLocator** for text files and notebooks (`path`, `line_start`, `line_end`). Use **FileRegionLocator** for binary byte ranges. Compose with **CompositeLocator** when needed.

## NegativeEvidenceRecord

When a search under declared scope finds nothing, use **NegativeEvidenceRecord**: `search_method`, `search_scope`, `result` (`absent`, `weak_signal`, `excluded`, `inconclusive`). Locator is optional.

Absence is first-class data, not an empty list.
