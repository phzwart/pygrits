# Activity

## Purpose

An `Activity` is a **hyperedge** in the pygrits graph. It records a transform step: what grits were consumed as inputs, what grits were produced as outputs, under what assumptions, and with what activity type. Activities make reasoning steps inspectable and append-only.

## What it is

`Activity` is a concrete subclass of `Grit` with `class_uri: prov:Activity`. It does not hold domain payload; it records *how* other grits were combined or related.

```
Grit
└── Activity
```

Activities are never Objects. The distinction is structural: Objects assert; Activities transform.

## Key fields

### Discipline contract (inherited from `Grit`, MVE-tagged)

Same as all grits: `id`, `type`, `viewpoint_directive_id`, `provenance`, `should_not_claim`.

For Activities, `type` is a CURIE corresponding to the `ActivityType` value (e.g. `grits:activity_type/synthesis_edge`).

### Activity-specific

| Field | Required (MVE) | Description |
|-------|------------------|-------------|
| `activity_type` | yes | One of seven hyperedge kinds (see below) |
| `inputs` | yes | Grit ids consumed by this activity |
| `outputs` | no | Grit ids produced (may be empty for declarative edges) |
| `assumptions` | no | Stated assumptions for this step |
| `admissibility_rationale` | no | Why this activity is valid given inputs and viewpoint |
| `compatibility_judgments` | no | Recorded compatibility over input grits |
| `confidence` | no | Structured confidence for this step |

## Activity types

| `ActivityType` | Role |
|----------------|------|
| `SYNTHESIS_EDGE` | Inputs + assumptions → new synthesis grit |
| `SUPPORT_EDGE` | Evidence → claim/synthesis it supports |
| `CONTRADICTION_EDGE` | Evidence → claim/synthesis it contradicts |
| `COMPATIBILITY_EDGE` | Records a compatibility judgment over grits |
| `VALIDATION_EDGE` | Validating grit → grit it validates |
| `ACTION_EDGE` | Operation with inputs and output grits |
| `ADJUDICATION_EDGE` | Resolves a set of CONTRADICTION_EDGEs |

Declarative edges (`SUPPORT`, `CONTRADICTION`) may have empty `outputs` — the Activity itself is the record.

> **Note.** The semantic-web `instance_of` slot is intentionally *not* on `Activity` in v1 (it lives on [Object](object.md) and [EvidenceRecord](evidence_record.md) only). Declaring ontology class membership for transform edges is deferred to when provenance-graph reasoning needs it.

## Relationships

```
Object / EvidenceRecord  → inputs
Object / EvidenceRecord  ← outputs (new grits only)
```

**Activities never mutate their inputs.** A synthesis step that extrapolates k_cat for substrate S produces a *new* Object in `outputs`. The original EvidenceRecords for S1–S3 are unchanged. The graph is append-only by construction.

## Why it exists

`Activity` makes each reasoning step a first-class, hashable, viewpoint-tagged node. A downstream consumer can walk the graph and see:

- which evidence supported which claim (`SUPPORT_EDGE`)
- which evidence contradicted which claim (`CONTRADICTION_EDGE`)
- how a new claim was derived (`SYNTHESIS_EDGE`)
- whether contradictions were adjudicated (`ADJUDICATION_EDGE`)

In the k_cat example, an optional extrapolation for substrate S is an `Activity` with `activity_type: SYNTHESIS_EDGE`, not an edit to existing evidence.

## Minimal example

```python
from pygrits import Activity, ActivityType

synthesis = Activity(
    id="act:kcat-s-extrapolation-v0",
    type="grits:activity_type/synthesis_edge",
    viewpoint_directive_id="vpt:generic-paper-parse-v0",
    provenance="synthesis engine v0 — extrapolation under stated assumptions",
    should_not_claim=[
        "Output is an extrapolation, not a reported measurement.",
    ],
    activity_type=ActivityType.SYNTHESIS_EDGE,
    inputs=[
        "evi:kcat-s1-span",
        "evi:kcat-s2-span",
        "evi:kcat-s3-span",
        "evi:negative-kcat-s",
    ],
    outputs=["obj:kcat-s-estimate-v0"],
    assumptions=[
        "Substrate S is kinetically similar to S1–S3.",
        "Same assay conditions apply.",
    ],
    review_state="machine_generated",
)
```

YAML equivalent: [`examples/05_synthesis_activity_minimal.yaml`](../examples/05_synthesis_activity_minimal.yaml).
