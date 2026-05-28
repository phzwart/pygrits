# ReasoningPolicy

## Purpose

A `ReasoningPolicy` is the **inferential permission surface**. It governs what synthesis, inference, normalization, and contradiction adjudication a layer permits. It does not control extraction behavior — that belongs to `ExtractionProfile`.

It answers: *what reasoning is allowed* — not *how* to extract or *which terms* apply.

## What it is

`ReasoningPolicy` is a subclass of `OperationalLayer`, which is a subclass of `Object`.

```
Object
└── OperationalLayer
    └── ReasoningPolicy
```

Supported composition modes: `additive`, `restrictive`.

Under `restrictive`, permission booleans combine by logical AND (narrowing). Under `additive`, they combine by logical OR (widening).

## Key fields

### Inherited from OperationalLayer / Object / Grit

`layer_name`, `composition_mode`, `parent_reasoning_policy_ids`, full discipline contract.

### ReasoningPolicy-specific

| Field | Description |
|-------|-------------|
| `allow_speculative_inference` | Whether speculative inference is permitted |
| `allow_cross_document_synthesis` | Whether synthesis across multiple documents is permitted |
| `allow_ontology_normalization` | Whether ontology normalization is permitted |
| `enable_contradiction_adjudication` | Whether contradiction adjudication is enabled |
| `notes` | Free-text clarification of the reasoning posture |

## Relationships

```
ViewpointDirective → composed with ReasoningPolicy via compose_viewpoint()
Activity (SYNTHESIS_EDGE) → permitted or forbidden by policy flags
Activity (ADJUDICATION_EDGE) → requires enable_contradiction_adjudication
```

## Why it exists

Different workflows need different inferential freedom. A regulatory audit pipeline forbids speculative inference and cross-document synthesis. An exploratory literature review permits both — under explicit, inspectable flags.

`ReasoningPolicy` makes inferential permissions:

- **Explicit** — boolean flags, not prompt hints
- **Composable** — a conservative policy layers over a permissive base via `restrictive` mode
- **Inspectable** — content-addressed grit with canonical hash

In the k_cat example, a conservative policy with `allow_speculative_inference: false` blocks the synthesis Activity from running unless the caller explicitly composes a more permissive policy. The measured values for S1–S3 remain; extrapolation for S requires a deliberate policy choice.

## Minimal example

```python
from pygrits import ReasoningPolicy

policy = ReasoningPolicy(
    id="rpol:conservative-v0",
    type="grits:reasoning_policy",
    viewpoint_directive_id="vpt:meta-v0",
    provenance="hand-authored conservative reasoning policy v0",
    should_not_claim=[],
    layer_name="reasoning_policy:conservative:v0",
    composition_mode="restrictive",
    allow_speculative_inference=False,
    allow_cross_document_synthesis=False,
    allow_ontology_normalization=False,
    enable_contradiction_adjudication=True,
    notes="Direct evidence and explicit synthesis only; no speculative extrapolation.",
)
```

YAML equivalent: [`viewpoints/paper_parsing_v0/examples/04_conservative_reasoning_policy.yaml`](../viewpoints/paper_parsing_v0/examples/04_conservative_reasoning_policy.yaml).
