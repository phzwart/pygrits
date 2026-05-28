# VocabularyPack

## Purpose

A `VocabularyPack` is the **namespace and ontology binding surface**. It declares which vocabulary definitions, ontology files, and CURIE-prefix namespaces are active for a layer. Core is ontology-neutral — the actual terms live in externally referenced content.

It answers: *which terms are in play* — not *how* to extract (ExtractionProfile) or *what* may be claimed (ViewpointDirective).

## What it is

`VocabularyPack` is a subclass of `OperationalLayer`, which is a subclass of `Object`.

```
Object
└── OperationalLayer
    └── VocabularyPack
```

Supported composition modes: `additive`, `isolated`.

`isolated` mode inherits no parent vocabulary content — parent ids are retained only as source references for provenance.

## Key fields

### Inherited from OperationalLayer / Object / Grit

`layer_name`, `composition_mode`, `parent_vocabulary_pack_ids`, full discipline contract.

### VocabularyPack-specific

| Field | Description |
|-------|-------------|
| `vocabulary_refs` | Content-addressed references to vocabulary definitions |
| `ontology_refs` | Content-addressed references to ontology definitions |
| `active_namespaces` | CURIE-prefix namespaces this pack activates (e.g. `pp`, `mse`, `de`) |

## Relationships

```
ViewpointDirective → may also carry vocabulary_refs (viewpoint-level bindings)
VocabularyPack     → parent_vocabulary_pack_ids (composition chain)
Object.type        → CURIE values drawn from active namespaces
EvidenceRecord.evidence_type → CURIE values drawn from active namespaces
```

A `ViewpointDirective` and a `VocabularyPack` can both reference vocabularies. The viewpoint carries prompts and admissibility rules; the pack supplies the namespace surface for composition. When composed, resolved vocabulary refs union with deduplication.

## Why it exists

Scientific domains use different ontologies. A paper-parsing pipeline may need document-level terms (`pp:section`) for one task and materials-science terms (`mse:compound`) for another — without forking the entire viewpoint directive.

`VocabularyPack` lets you attach domain vocabulary to a generic viewpoint at composition time:

```
GenericScientificPaperView  +  MaterialsScienceVocabulary  →  composed directive
```

Core never defines domain terms. Viewpoints (`paper_parsing_v0`, `materials_science_v0`, …) supply them; packs select which namespaces are active.

## Minimal example

```python
from pygrits import VocabularyPack, ContentReference, HashMode

pack = VocabularyPack(
    id="voc:materials-science-v0",
    type="grits:vocabulary_pack",
    viewpoint_directive_id="vpt:meta-v0",
    provenance="hand-authored materials science vocabulary pack v0",
    should_not_claim=[],
    layer_name="vocabulary_pack:materials_science:v0",
    composition_mode="additive",
    vocabulary_refs=[
        ContentReference(
            uri="file://./viewpoints/materials_science_v0.yaml",
            sha256="1" * 64,
            hash_mode=HashMode.raw_bytes,
        )
    ],
    active_namespaces=["mse", "pp"],
)
```

YAML equivalent: [`viewpoints/paper_parsing_v0/examples/03_materials_vocabulary_pack.yaml`](../viewpoints/paper_parsing_v0/examples/03_materials_vocabulary_pack.yaml).
