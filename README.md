# pygrits

**Structured epistemic containment for agentic scientific reasoning.**

pygrits is a Python package built on [LinkML](https://linkml.io) that defines a small, strict object model for scientific knowledge work. Every claim, measurement, synthesis step, and refusal is a **grit** — a typed node with identity, provenance, viewpoint, scope, and explicit epistemic boundaries. The goal is to make it structurally difficult for agentic systems to collapse evidence, inference, synthesis, confidence, and viewpoint into unqualified truth.

## The problem pygrits solves

An agent is asked: *"What is the reported catalytic turnover number (k_cat) for enzyme E on substrate S?"*

The paper corpus contains k_cat values for E on three related substrates (S1, S2, S3), each anchored to a specific passage. There is no measurement for S.

A naive agent returns a plausible number. A pygrits-built system returns something different:

| What happened | Grit produced |
|---------------|---------------|
| k_cat found for S1, S2, S3 | `EvidenceRecord` per measurement, each with a `Locator` into the source |
| S searched, not found | `NegativeEvidenceRecord` (`result: absent`) |
| Optional extrapolation offered | `Activity` (`SYNTHESIS_EDGE`) → new `Object` with `should_not_claim` forbidding presentation as a measured value, `review_state: machine_generated` |

The fabricated "measured value for S" is not representable. Direct evidence, absence, and inference occupy distinct slots with distinct epistemic labels.

## Install

```bash
pip install -e .

pip install -e '.[test]'    # tests
pip install -e '.[schema]'  # LinkML toolchain (regenerate artifacts only)
```

Python 3.11+.

## Quickstart

```python
from pygrits import (
    Object, Activity, EvidenceRecord, ContentReference,
    ActivityType, HashMode, NotesOnlyScope,
    CharRangeLocator,
    canonical_hash_instance, verify_content_reference,
)

paper = Object(
    id="obj:minimal-demo",
    type="grits:object",
    viewpoint_directive_id="vpt:blank-slate-v0",
    provenance="ingested via demo pipeline v0",
    should_not_claim=[
        "Source claims are reported, not independently validated.",
    ],
    scope=NotesOnlyScope(
        scope_type="NotesOnlyScope",
        notes="No domain scope dimensions bound.",
    ),
    source_artifact_refs=[
        ContentReference(
            uri="file://./sources/demo/artifact.txt",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        )
    ],
    evidence_record_ids=["evi:minimal-span-v0"],
)

h = canonical_hash_instance(paper)
print(h)  # sha256:<64 hex>
```

Domain-specific scope dimensions come from viewpoint schemas:

```python
from pygrits.viewpoints.materials_science_v0 import ThermodynamicScope

scope = ThermodynamicScope(
    scope_type="ThermodynamicScope",
    pressure_pascal=101325.0,
)
```

Compose a viewpoint with optional operational layers:

```python
from pygrits import compose_viewpoint

composed = compose_viewpoint(
    "vpt:generic-paper-parse-v0",
    registry,
    extraction_profile_id="ep:detailed-extraction-v0",
    vocabulary_pack_id="voc:materials-science-v0",
    reasoning_policy_id="rpol:conservative-v0",
)
```

See `examples/` for core-level instances. See `viewpoints/*/examples/` for viewpoint-specific instances.

## The object model

Everything in pygrits is a **grit**. Three role classes share an abstract discipline contract; four composable layers define how extraction and reasoning are permitted.

```
Grit (abstract)
├── Object          — subject nodes (claims, papers, measurements)
├── Activity        — hyperedges (transforms, support, contradiction)
└── EvidenceRecord  — anchors into source artifacts

Object specializations
├── ViewpointDirective      — interpretive frame (what may be claimed)
├── ExtractionProfile       — grounding density (how finely to extract)
├── VocabularyPack          — namespace surface (which CURIEs are active)
└── ReasoningPolicy         — inferential permission (what synthesis is allowed)
```

| Class | Role | Guide |
|-------|------|-------|
| [Object](guide/object.md) | Subject node holding claims and references to evidence | What you assert |
| [Activity](guide/activity.md) | Hyperedge recording a transform step | How you got there |
| [EvidenceRecord](guide/evidence_record.md) | Anchor into a source artifact via a typed locator | What the source actually says |
| [ViewpointDirective](guide/viewpoint_directive.md) | Epistemic admissibility contract | What you may claim or refuse |
| [ExtractionProfile](guide/extraction_profile.md) | Extraction and grounding semantics | How finely to decompose and ground |
| [VocabularyPack](guide/vocabulary_pack.md) | Ontology and namespace bindings | Which terms are in play |
| [ReasoningPolicy](guide/reasoning_policy.md) | Inferential permission surface | What synthesis is permitted |

Full overview: [guide/README.md](guide/README.md).

## Composable epistemic layers

pygrits models *what may be claimed*, *how content is extracted*, *which vocabulary applies*, and *what inference is allowed* as four independent, content-addressed grits that compose deterministically into a frozen `ComposedViewpointDirective`.

```python
composed = compose_viewpoint(viewpoint_id, registry, ...)
```

Composition is explicit (caller-supplied registry, no global state), field-local (documented merge rules per field kind), and deterministic (identical inputs → identical hash). See [guide/composition.md](guide/composition.md).

## What the package provides

**Core schema (`pygrits.core`)** — structural primitives only:

- `Grit` hierarchy: `Object`, `Activity`, `EvidenceRecord`
- `Scope` marker and `Locator` hierarchy (seven concrete locator types)
- `ContentReference` with mandatory `sha256` + `hash_mode`
- `Confidence`, `CompatibilityJudgment`
- Enums: `ActivityType`, `LifecycleState`, `ReviewState`, `EpistemicStatus`, `RefusalState`, `LineageType`, `HashMode`, `CompositionMode`, ...
- Canonical hashing: `canonical_hash_instance(grit)` via LinkML normalization + RFC 8785 JCS
- Bundled schemas: `schema_path()`, `json_schema_path()`, `viewpoint_schema_path(name)`

**Viewpoint schemas (`pygrits.viewpoints.*`)** — domain vocabulary layered on core:

| Viewpoint | Purpose |
|-----------|---------|
| `blank_slate_v0` | No domain vocabulary |
| `document_extraction_v0` | Evidence-type CURIEs for document extraction |
| `materials_science_v0` | Thermodynamic scope dimensions, materials vocabulary |
| `coordination_v0` | Multi-node workflow slots |
| `paper_parsing_v0` | Generic scientific-paper content kinds (`pp:section`, `pp:measurement`, ...) |

Type labels (`mse:paper`, `pp:measurement`, `de:text_span`) are CURIE values of the `type` field, drawn from viewpoint vocabulary — not Python classes in core.

## Schema regeneration

```bash
bash scripts/regenerate.sh
```

Regenerates `core.py`, `core.schema.json`, `docs/` (LinkML auto-doc), and viewpoint artifacts from `src/pygrits/core.yaml` and `viewpoints/*.yaml`.

## Tests

```bash
pytest
```

## License

BSD-3-Clause.

## Acknowledgments

Built on [LinkML](https://linkml.io), [Pydantic](https://docs.pydantic.dev), and [jcs](https://pypi.org/project/jcs/) (RFC 8785 canonicalization).
