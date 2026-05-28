# Object

## Purpose

An `Object` is a **subject node** in the pygrits graph. It holds what the system asserts about a scientific entity — a paper, a measurement, a claim, a material — together with references to the source artifacts and evidence records that ground those assertions.

## What it is

`Object` is a concrete subclass of `Grit`. It is the default role for anything that *is* something rather than *does* something (Activities) or *anchors into* something (EvidenceRecords).

```
Grit
└── Object
    ├── ViewpointDirective
    ├── ExtractionProfile      (via OperationalLayer)
    ├── VocabularyPack         (via OperationalLayer)
    ├── ReasoningPolicy        (via OperationalLayer)
    └── … domain Objects (papers, claims, measurements — typed by CURIE)
```

Domain-specific objects are not separate Python classes in core. A materials-science paper is an `Object` whose `type` is `mse:paper`; a parsed measurement is an `Object` whose `type` is `pp:measurement`. The viewpoint vocabulary supplies the label; core supplies the shape.

## Key fields

### Discipline contract (inherited from `Grit`, MVE-tagged)

| Field | Required (MVE) | Description |
|-------|------------------|-------------|
| `id` | yes | Canonical grit id (`obj:…`) |
| `type` | yes | CURIE into viewpoint vocabulary |
| `viewpoint_directive_id` | yes | Interpretive frame that shaped this object |
| `provenance` | yes | How this object was produced |
| `should_not_claim` | yes | Epistemic boundaries (multivalued) |

### Object-specific

| Field | Subset | Description |
|-------|--------|-------------|
| `source_artifact_refs` | MVE | Content-addressed references to source files |
| `evidence_record_ids` | MVE | EvidenceRecord grits anchoring this object's claims |
| `summary` | ExtendedProfile | Short descriptive text |
| `features` | ExtendedProfile | Viewpoint-defined structured payload (JSON string in v1) |
| `observations` | ExtendedProfile | Free-text observations |
| `unspecified_items` | ExtendedProfile | Dimensions not bound under current viewpoint |
| `reported_claims` | Full | Claims attributed to the source |
| `methods` | Full | Methods referenced |
| `assumptions` | Full | Stated assumptions |
| `uncertainties` | Full | Known uncertainties |
| `synthesis_link_ids` | Full | Backward pointers to Activities that used this object |
| `operation_link_ids` | Full | Backward pointers to ACTION_EDGE Activities |

## Relationships

```
ContentReference ← source_artifact_refs
EvidenceRecord   ← evidence_record_ids (by id)
Activity         → outputs (Activities produce new Objects)
ViewpointDirective → viewpoint_directive_id
```

An Object does not embed evidence inline. Claims are supported by separate `EvidenceRecord` grits referenced by id. This keeps anchors inspectable and reusable across multiple Objects.

## Why it exists

`Object` is the typed subject node. Every assertion declares:

- **where it came from** (`source_artifact_refs`, `evidence_record_ids`)
- **under which interpretive frame** (`viewpoint_directive_id`)
- **what it must not be taken to mean** (`should_not_claim`)
- **under what conditions it applies** (`scope`)

The k_cat example: a synthesized estimate for substrate S is a *different* Object from the measured values for S1–S3, with different `should_not_claim` and `review_state`. They cannot be merged into one undifferentiated "the k_cat."

## Minimal example

```python
from pygrits import Object, ContentReference, HashMode, NotesOnlyScope

paper = Object(
    id="obj:paper-2024-enzyme-kinetics",
    type="pp:paper",
    viewpoint_directive_id="vpt:generic-paper-parse-v0",
    provenance="extracted by paper_parsing pipeline v0",
    should_not_claim=[
        "Document structure is extracted; domain semantics are not asserted.",
    ],
    scope=NotesOnlyScope(
        scope_type="NotesOnlyScope",
        notes="Full-text PDF, methods and results sections.",
    ),
    source_artifact_refs=[
        ContentReference(
            uri="file://./corpus/smith2024.pdf",
            sha256="abc123…",  # 64 hex chars
            hash_mode=HashMode.raw_bytes,
        )
    ],
    evidence_record_ids=[
        "evi:kcat-s1-span",
        "evi:kcat-s2-span",
        "evi:kcat-s3-span",
        "evi:negative-kcat-s",
    ],
    summary="Smith et al. 2024 — kinetic characterization of enzyme E.",
)
```

YAML equivalent: [`examples/03_object_minimal.yaml`](../examples/03_object_minimal.yaml).
