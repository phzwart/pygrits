# Composable epistemic layers

pygrits models interpretive contracts as four composable, content-addressed
grits. A deterministic resolver folds them into one frozen interpretive
contract.

## The four layers

| Layer | Responsibility | Answers |
|-------|----------------|---------|
| [ViewpointDirective](viewpoint_directive.md) | epistemic admissibility | what may be claimed / refused, under what scope |
| [ExtractionProfile](extraction_profile.md) | extraction / grounding density | how finely content is decomposed and grounded |
| [VocabularyPack](vocabulary_pack.md) | ontology / namespace surface | which vocabularies and CURIE namespaces are active |
| [ReasoningPolicy](reasoning_policy.md) | inferential permission | what synthesis / inference / adjudication is allowed |

All four are `Object` subclasses (via `OperationalLayer is_a Object`, except
`ViewpointDirective` which is directly `is_a Object`). They share the same
identity, provenance, lifecycle, and canonical-hashing discipline. Reusable
foundational layers reference the bootstrap meta-viewpoint
(`viewpoint_directive_id: vpt:meta-v0`).

Identity uses one pathway: `canonical_hash_instance` (RFC 8785 JCS).

## Composition is explicit and field-local

- Each layer declares an explicit, semantically named parent slot
  (`parent_viewpoint_ids`, `parent_extraction_profile_ids`,
  `parent_vocabulary_pack_ids`, `parent_reasoning_policy_ids`) — never a generic
  `parent_ids`.
- The caller passes an explicit `registry` mapping id to layer instance. There is
  no global state and no implicit runtime parent lookup.
- Resolution walks each layer's own chain parents-first, with cycle detection,
  and folds field by field. This is structural composition, not OO inheritance
  and not a policy engine.

## `CompositionMode`

A LinkML enum. Not every layer supports every mode (no artificial symmetry):

| Mode | Meaning | Supported by |
|------|---------|--------------|
| `additive` | add without removing inherited content | all layers |
| `restrictive` | narrow the admissible space | `ViewpointDirective`, `ReasoningPolicy` |
| `overriding` | child replaces overlapping fields | `ViewpointDirective`, `ExtractionProfile` |
| `isolated` | inherit no parent content; parents kept only as source refs | `VocabularyPack` |

Declaring an unsupported mode raises `CompositionError`.

## Merge rules (deterministic, field-local)

| Field kind | Rule |
|------------|------|
| `prompts`, `exemplars` | append parent then child, dedup by `(uri, sha256, hash_mode)` |
| `imposed_should_not_claim`, `should_not_claim` | union + dedup, first-seen order |
| `vocabulary_refs`, `ontology_refs`, `active_namespaces` | union + dedup (`additive`); child-only (`isolated`) |
| `preserve_content_kinds`, `require_grounding_for_content_kinds`, `high_fidelity_content_kinds` | union + dedup (`additive`); child-only (`overriding`) |
| `target_schema`, scalar/enum fields | most-derived non-null wins; child override under `overriding` |
| `allow_*` booleans | logical AND under `restrictive`; logical OR under `additive` |
| `preserve_*` / `require_*` / `enable_*` booleans | logical OR (tightening) |

Content kinds are opaque `CurieOrUri` values in core. Their meaning is supplied
by viewpoint vocabularies (e.g. `paper_parsing_v0` defines `pp:equation`,
`pp:measurement`, ...). Core contains no document or domain semantics.

The optional semantic-web slots (`instance_of`, `payload_schema`,
`abstraction_level`) are **not folded by the resolver in v1**. They are carried
as metadata on the grits/viewpoints; auto-derivation of `should_not_claim` from
`abstraction_level` is a documented but deferred extension. See
[ViewpointDirective](viewpoint_directive.md#abstraction-level-optional).

## The composed result

`compose_viewpoint(viewpoint_id, registry, *, extraction_profile_id=...,
vocabulary_pack_id=..., reasoning_policy_id=...)` returns a
`ComposedViewpointDirective` (`is_a ViewpointDirective`). It:

- inlines `resolved_extraction_profile`, `resolved_vocabulary_pack`,
  `resolved_reasoning_policy`;
- records flattened, parents-first `source_*_ids` for inspectability;
- gets a deterministic id `vpt:composed:<sha8>` derived from the ordered source
  chains, so identical inputs yield an identically hashed artifact.

It remains conceptually a viewpoint-level interpretive contract, not a runtime
configuration object. The inherited `provenance` string plus `source_*_ids` plus
deterministic ordering are sufficient.

## Example

`viewpoints/paper_parsing_v0/examples/` ships one layer of each kind:
`GenericScientificPaperView` + `DetailedExtraction` + `MaterialsScienceVocabulary`
+ `ConservativeReasoning`, which compose into a single
`ComposedViewpointDirective` without duplicating prompts, extraction contracts,
or admissibility rules.

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
