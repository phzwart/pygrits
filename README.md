# pygrits

**Raisins in the pudding** — evidence-grounded scientific entities with viewpoint-aware refusal.

Python implementation of the **ISOM** schema (Interactive Scientific Object Model) for **structured epistemic containment** in agentic scientific reasoning. The job of pygrits is to make it harder for agentic systems to silently collapse evidence, inference, synthesis, confidence, lineage, and viewpoint into unqualified truth claims.

The motivating failure case is concrete. An agent asked *"What is the melting point of NaCl?"* against a corpus containing only LiCl, KCl, LiF, NaF, and KF observations will typically fabricate a plausible number. A pygrits-built system instead returns: direct evidence absent, negative-evidence record produced, related-family evidence available, interpolation proposed under stated assumptions and viewpoint, review state machine_generated, recommended action: direct retrieval. The fabricated number is structurally impossible.

## Status

**Alpha.** Schema is at v0.1; expect breaking changes between commits until the first real ingestion adapter has bent the schema against actual data. Stability is not a goal yet.

## Install

```bash
# from a git checkout
pip install -e .

# with test deps
pip install -e '.[test]'

# with the LinkML toolchain (only needed to regenerate the schema artifacts)
pip install -e '.[schema]'
```

Python 3.11+.

## Quickstart

```python
from pygrits import (
    Object, Activity, EvidenceRecord, ContentReference,
    ActivityType, HashMode, LineageType,
    CharRangeLocator,
    canonical_hash_instance, verify_content_reference,
)

# Build a paper Object under a declared viewpoint
paper = Object(
    id="obj:paper-licl-demo",
    type="isom:paper",
    viewpoint_directive_id="vpt:alkali-halide-thermo-v0",
    provenance="ingested via paperqa-A v0",
    should_not_claim=[
        "Source claims are reported, not independently validated.",
        "Citation lineage of values is unresolved at ingestion.",
    ],
    source_artifact_refs=[
        ContentReference(
            uri="file://./sources/papers/licl_demo.pdf",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        )
    ],
    evidence_record_ids=["evi:span-licl-mp-v0"],
)

# Canonical, deterministic content hash
h = canonical_hash_instance(paper)
print(h)  # sha256:<64 hex>

# Verify a ContentReference matches the actual content
ok = verify_content_reference(paper.source_artifact_refs[0], b"<pdf bytes>")
```

See `examples/` for six complete end-to-end instances: a bootstrap meta-viewpoint, a domain viewpoint, a paper Object, an EvidenceRecord with a CharRangeLocator, a SYNTHESIS_EDGE Activity, and the claim Object the Activity produces.

## What this package gives you

- **`Entity` hierarchy** — `Object`, `Activity`, `EvidenceRecord` (three siblings sharing an abstract discipline contract), plus `ViewpointDirective` and `NegativeEvidenceRecord` specializations.
- **Primitives** — `ContentReference` (content-addressed with mandatory sha256 + hash_mode), `Scope` (composite of seven optional dimension classes), the `Locator` hierarchy (seven concrete subtypes for different anchor styles), `Confidence` (structured with calibration metadata), `CompatibilityJudgment`.
- **Enums** — `ActivityType` (the seven hyperedge types), `LifecycleState`, `ReviewState`, `EpistemicStatus`, `LineageType`, `RefusalState` (five-state taxonomy), `CompatibilityStatus`, `ConfidenceBasis`, `HashMode`.
- **Canonical hashing** — `canonical_hash_instance(entity)` returns a stable SHA-256 over any entity, via LinkML normalization + RFC 8785 JCS. The hash is invariant to Python-runtime field ordering, OS, library version, and unicode rendering choices.
- **ContentReference verification** — `verify_content_reference(ref, content)` checks the declared hash matches actual content, dispatching on `hash_mode`.
- **The LinkML source schema** is shipped with the package (`pygrits.schema_path()`), so downstream tools can use the LinkML validator against it.
- **The generated JSON Schema** is shipped (`pygrits.json_schema_path()`), so non-Python consumers can validate against it.

## What this package does *not* (yet) give you

Deferred to v0.2+:

- Speech acts, reactions, threads, communities (spec §16–§18).
- Wiki statement Objects with append-only graph + mutable rendering.
- Harmonization process and viewpoint supersession Activities.
- Composition of viewpoint directives (strict/permissive variants).
- Structured provenance (currently a free-form string).
- A `linkml_canonical_rdfc` hash mode for schema-level logical equivalence.
- Hyperedge admissibility and synthesis admissibility rules (open §27 of the spec).
- Ingestion adapters from real paper-extraction tool output.

## Design

The conceptual underpinning is the **Interactive Scientific Object Model** specification. The key ideas:

1. **Everything is an entity.** Three classes — `Object`, `Activity`, `EvidenceRecord` — share an abstract discipline contract (identity, type, viewpoint, provenance, scope, should_not_claim, review state, lifecycle, generation mode). Domain-specific labels (`paper`, `diffraction_dataset`, `material_entry`, etc.) are CURIE values of the `type` field, drawn from viewpoint vocabulary — not Python classes.

2. **Activities are not Objects.** Activities transform inputs to outputs; they don't participate in conversations. They record how a step of reasoning happened. Outputs are *new* entities — Activities never mutate their inputs. This makes the append-only graph mechanical, not aspirational.

3. **Extraction is viewpoint-defined.** Every entity declares which `ViewpointDirective` shaped it. There is no neutral extraction. Different viewpoints applied to the same source produce different entities, not the same entity with different annotations.

4. **Identity by declaration, integrity by content hash.** Viewpoint directives have human-readable names plus content hashes on every referenced piece of content. Names are the human reference; hashes are the integrity check. The canonical form is RFC 8785 JCS on LinkML JSON for instances, raw bytes for opaque content.

5. **Hard refusal modes.** Every entity carries `should_not_claim`. The refusal taxonomy is five-state: `unknown`, `not_searched`, `searched_absent`, `out_of_viewpoint`, `contradicted`. The system surfaces these distinctly; it does not collapse them into a single "I don't know" or — worse — into a fabricated answer.

The full specification document lives separately; pygrits is the Python implementation of its schema-level commitments.

## Schema regeneration

```bash
bash scripts/regenerate.sh
```

This runs `gen-pydantic`, `gen-json-schema`, and `gen-doc` against `src/pygrits/core.yaml` and writes the outputs back into the package and into `docs/`. CI guards that the checked-in artifacts match the source.

## Tests

```bash
pytest
```

Test suite covers:

- All example YAML files load as valid Pydantic instances.
- Missing MVE fields fail with `ValidationError`.
- Malformed sha256 patterns fail.
- Pydantic `extra="forbid"` catches undeclared fields.
- Canonical hashes are deterministic across construction order and YAML/JSON round-trip.
- Any field change changes the hash.
- `verify_content_reference` accepts matches and rejects mismatches under both hash modes.
- Activities with identical discriminating content hash identically (the property that enables idempotent synthesis detection).

## License

BSD-3-Clause.

## Acknowledgments

Built on [LinkML](https://linkml.io), with [Pydantic](https://docs.pydantic.dev) for runtime typing and the [jcs](https://pypi.org/project/jcs/) package for RFC 8785 canonicalization.
