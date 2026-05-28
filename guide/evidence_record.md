# EvidenceRecord

## Purpose

An `EvidenceRecord` is an **anchor unit**. It grounds a piece of data to exactly one source artifact at a specific location (character range, bounding box, table cell, sequence position, …). EvidenceRecords are the foundation of epistemic discipline: claims in Objects point here, not to free-floating text.

## What it is

`EvidenceRecord` is a concrete subclass of `Grit`. Each record ties one extraction to one `ContentReference` via a typed `Locator`.

```
Grit
└── EvidenceRecord
    └── NegativeEvidenceRecord
```

## Key fields

### Discipline contract (inherited from `Grit`, MVE-tagged)

`id`, `type`, `viewpoint_directive_id`, `provenance`, `should_not_claim`.

### EvidenceRecord-specific

| Field | Required (MVE) | Description |
|-------|------------------|-------------|
| `source_artifact_ref` | yes | Single ContentReference to the source file |
| `locator` | yes | Typed anchor into that source (see Locator hierarchy) |
| `extracted_content` | no | Raw extracted text or value |
| `normalized_payload` | no | Viewpoint-defined structured payload (JSON string in v1) |
| `evidence_type` | no | CURIE identifying content kind (viewpoint-supplied vocabulary) |
| `extraction_method` | no | How extraction was performed |
| `extraction_confidence` | no | Structured confidence for the extraction |
| `lineage` | no | Independence classification (`independent`, `derived`, `cited`, …) |
| `cited_from` | no | Prior evidence this record derives from |

`evidence_type` has no core-supplied permissible values. Viewpoints define them (e.g. `de:text_span`, `pp:measurement`).

## Locator hierarchy

Locators describe **how** an anchor is shaped, not **what** content the source contains:

| Locator | Anchors to |
|---------|------------|
| `CharRangeLocator` | Character range in extracted text |
| `BboxLocator` | Axis-aligned box on a rasterized page |
| `SequencePositionLocator` | Range in a reference sequence |
| `ProcessingLogLineLocator` | Line range in a processing log |
| `TableCellLocator` | Specific table cell |
| `FileRegionLocator` | Byte range in opaque binary |
| `CompositeLocator` | Combination of sub-locators |

## NegativeEvidenceRecord

A search that returned no result under stated scope is not the same as "we didn't look."

| Field | Description |
|-------|-------------|
| `search_method` | How the search was performed (required) |
| `search_scope` | What was searched |
| `search_timestamp` | When |
| `search_confidence` | Confidence in the negative result |
| `result` | `absent`, `weak_signal`, `excluded`, or `inconclusive` |

This pairs with `RefusalState.searched_absent` — distinct from `unknown` (not considered) and `not_searched` (in scope but not attempted).

In the k_cat example, the search for enzyme E on substrate S produces a `NegativeEvidenceRecord` with `result: absent`, while the S1–S3 measurements each get a positive `EvidenceRecord`.

## Relationships

```
ContentReference  ← source_artifact_ref
Object          → evidence_record_ids (Objects reference EvidenceRecords by id)
Activity        → inputs (Activities consume EvidenceRecords)
```

Evidence is never embedded inside Objects. Separation keeps anchors reusable and inspectable.

## Why it exists

`EvidenceRecord` makes every grounded datum traceable:

1. **Which file** (`source_artifact_ref` with integrity hash)
2. **Where in the file** (`locator`)
3. **What was extracted** (`extracted_content`)
4. **Under which viewpoint** (`viewpoint_directive_id`)

A consumer can verify the anchor independently of the Object that uses it.

## Minimal example

```python
from pygrits import (
    EvidenceRecord, NegativeEvidenceRecord,
    ContentReference, CharRangeLocator, HashMode,
)

evidence = EvidenceRecord(
    id="evi:kcat-s1-span",
    type="grits:evidence_record",
    viewpoint_directive_id="vpt:generic-paper-parse-v0",
    provenance="extracted by paper_parsing pipeline v0",
    should_not_claim=[
        "Extracted value is reported by the source, not independently validated.",
    ],
    source_artifact_ref=ContentReference(
        uri="file://./corpus/smith2024.pdf",
        sha256="abc123…",
        hash_mode=HashMode.raw_bytes,
    ),
    locator=CharRangeLocator(
        locator_type="CharRangeLocator",
        char_start=8420,
        char_end=8512,
        page=4,
    ),
    extracted_content="k_cat = 12.4 s⁻¹ (substrate S1, 25 °C)",
    evidence_type="pp:measurement",
)

negative = NegativeEvidenceRecord(
    id="evi:negative-kcat-s",
    type="grits:negative_evidence_record",
    viewpoint_directive_id="vpt:generic-paper-parse-v0",
    provenance="full-text search, results section",
    should_not_claim=[],
    source_artifact_ref=ContentReference(
        uri="file://./corpus/smith2024.pdf",
        sha256="abc123…",
        hash_mode=HashMode.raw_bytes,
    ),
    locator=CharRangeLocator(
        locator_type="CharRangeLocator",
        char_start=0,
        char_end=0,
        page=0,
    ),
    search_method="full_text_regex",
    search_scope="results section, substrate S",
    result="absent",
)
```

YAML equivalent: [`examples/04_evidence_minimal.yaml`](../examples/04_evidence_minimal.yaml).
