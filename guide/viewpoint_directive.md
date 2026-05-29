# ViewpointDirective

## Purpose

A `ViewpointDirective` is the **interpretive frame** under which grits are extracted and asserted. It answers: what may be claimed, what must be refused, which prompts and exemplars shape extraction, and which vocabulary applies. There is no neutral extraction — every grit names the directive that shaped it.

## What it is

`ViewpointDirective` is a subclass of `Object`. It carries prompts, exemplars, vocabulary references, a target schema, and `imposed_should_not_claim` rules that propagate to every grit extracted under it.

```
Object
└── ViewpointDirective
    └── ComposedViewpointDirective
```

`ViewpointDirective` itself has a `viewpoint_directive_id` — typically the bootstrap meta-viewpoint (`vpt:meta-v0`) for hand-authored directives, or self-reference for the meta-viewpoint.

## Key fields

### Inherited from Object / Grit

Full discipline contract plus `source_artifact_refs`, `evidence_record_ids`, etc.

### ViewpointDirective-specific

| Field | Description |
|-------|-------------|
| `directive_name` | Human-readable name (e.g. `viewpoint:generic_paper_parse:v0`) |
| `parent_viewpoint_ids` | ViewpointDirective ids this composes from (parents-first) |
| `composition_mode` | How this layer folds against parents (`additive`, `restrictive`, `overriding`) |
| `prompts` | Content-addressed extraction prompts |
| `exemplars` | Content-addressed few-shot examples |
| `vocabulary_refs` | Content-addressed vocabulary definitions |
| `target_schema` | LinkML schema (or profile) this directive commits to |
| `imposed_should_not_claim` | Rules imposed on every grit extracted under this directive |
| `abstraction_level` | Optional ontology class CURIE at which this viewpoint makes claims |

Identity is **by declaration plus content hash**: `directive_name` is the human reference; `canonical_hash_instance()` is the integrity check.

### Abstraction level (optional)

`abstraction_level` is the optional semantic-web slot on a viewpoint. It declares the ontology class at which the viewpoint makes claims: instance-level viewpoints reference leaf classes (a specific assay type), while merged/general viewpoints reference parent classes (e.g. the class for any Raman spectroscopy). This makes the abstraction explicit so that two structurally identical viewpoints — one extracting a specific instance, one extracting a general class — are distinguishable.

In v1 the slot is carried as metadata only: the intended `should_not_claim` rule ("claims are valid only at the declared class level; do not assert instance-specific details suppressed by the abstraction") is documented but **not yet auto-derived** by composition. The CURIE is drawn from the ontologies a [VocabularyPack](vocabulary_pack.md) references via `ontology_refs`.

## ComposedViewpointDirective

`compose_viewpoint()` produces a `ComposedViewpointDirective` — a frozen, hashable result of composing a ViewpointDirective with optional `ExtractionProfile`, `VocabularyPack`, and `ReasoningPolicy` layers.

| Field | Description |
|-------|-------------|
| `resolved_extraction_profile` | Inlined resolved extraction profile |
| `resolved_vocabulary_pack` | Inlined resolved vocabulary pack |
| `resolved_reasoning_policy` | Inlined resolved reasoning policy |
| `source_viewpoint_ids` | Flattened parents-first chain of viewpoint ids |
| `source_extraction_profile_ids` | Flattened extraction profile chain |
| `source_vocabulary_pack_ids` | Flattened vocabulary pack chain |
| `source_reasoning_policy_ids` | Flattened reasoning policy chain |

`ComposedViewpointDirective` is not hand-authored. It is produced by `compose_viewpoint()` with a deterministic id `vpt:composed:<sha8>`.

## Relationships

```
Every Grit  → viewpoint_directive_id
ViewpointDirective → parent_viewpoint_ids (composition chain)
ExtractionProfile / VocabularyPack / ReasoningPolicy → composed into ComposedViewpointDirective
```

## Why it exists

Every grit names the interpretive frame that shaped it. `ViewpointDirective` makes that contract:

- **Inspectable** — prompts, exemplars, and rules are content-addressed grits
- **Composable** — strict and permissive variants layer without duplication
- **Mandatory** — every grit must declare `viewpoint_directive_id`; absence is invalid

The generic paper-parsing viewpoint (`vpt:generic-paper-parse-v0`) commits to document structure (`pp:section`, `pp:figure`, `pp:measurement`) without asserting domain semantics. A materials vocabulary pack layers on separately.

## Minimal example

```python
from pygrits import ViewpointDirective, ContentReference, HashMode

directive = ViewpointDirective(
    id="vpt:generic-paper-parse-v0",
    type="grits:viewpoint_directive",
    viewpoint_directive_id="vpt:meta-v0",
    provenance="hand-authored generic paper parsing viewpoint v0",
    should_not_claim=[
        "Document structure is extracted; domain semantics are not asserted.",
    ],
    directive_name="viewpoint:generic_paper_parse:v0",
    parent_viewpoint_ids=["vpt:meta-v0"],
    composition_mode="additive",
    prompts=[
        ContentReference(
            uri="file://./prompts/generic_paper_parse/extraction.v0.txt",
            sha256="0" * 64,
            hash_mode=HashMode.raw_bytes,
        )
    ],
    imposed_should_not_claim=[
        "Every grit must declare its viewpoint_directive_id.",
        "Extracted content is reported structure, not validated scientific claims.",
    ],
)
```

YAML equivalent: [`viewpoints/paper_parsing_v0/examples/01_generic_paper_parse_view.yaml`](../viewpoints/paper_parsing_v0/examples/01_generic_paper_parse_view.yaml).

See [composition.md](composition.md) for how this layers with ExtractionProfile, VocabularyPack, and ReasoningPolicy.
