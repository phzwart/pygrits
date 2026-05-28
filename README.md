# pygrits

**Raisins in the pudding** — evidence-grounded scientific entities with viewpoint-aware refusal.

Python implementation of the **ISOM** schema (Interactive Scientific Object Model) for **structured epistemic containment** in agentic scientific reasoning. The job of pygrits is to make it harder for agentic systems to silently collapse evidence, inference, synthesis, confidence, lineage, and viewpoint into unqualified truth claims.

The motivating failure case is concrete. An agent asked *"What is the melting point of NaCl?"* against a corpus containing only LiCl, KCl, LiF, NaF, and KF observations will typically fabricate a plausible number. A pygrits-built system instead returns: direct evidence absent, negative-evidence record produced, related-family evidence available, interpolation proposed under stated assumptions and viewpoint, review state machine_generated, recommended action: direct retrieval. The fabricated number is structurally impossible.

## Status

**Alpha.** Core schema is at v0.2; expect breaking changes between commits until the first real ingestion adapter has bent the schema against actual data. Stability is not a goal yet.

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
    ActivityType, HashMode, NotesOnlyScope,
    CharRangeLocator,
    canonical_hash_instance, verify_content_reference,
)

# Build a minimal Object under a declared viewpoint (core schema only)
paper = Object(
    id="obj:minimal-demo",
    type="isom:object",
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

# Canonical, deterministic content hash
h = canonical_hash_instance(paper)
print(h)  # sha256:<64 hex>
```

For domain-specific scope dimensions, load a viewpoint schema:

```python
from pygrits.viewpoints.materials_science_v0 import ThermodynamicScope

scope = ThermodynamicScope(
    scope_type="ThermodynamicScope",
    pressure_pascal=101325.0,
)
```

See `examples/` for core-level instances that validate against the bare core schema alone. See `viewpoints/materials_science_v0/examples/` for alkali-halide thermodynamics instances that require the materials-science viewpoint.

## What this package gives you

**Core schema (`pygrits.core`)** — structural primitives only:

- **`Entity` hierarchy** — `Object`, `Activity`, `EvidenceRecord` (three siblings sharing an abstract discipline contract), plus `ViewpointDirective` and `NegativeEvidenceRecord` specializations.
- **`Scope` marker** — opaque container for viewpoint-supplied scope dimensions. Core ships `NotesOnlyScope` (free-form notes only). No domain dimensions (temperature, organism, formula, etc.) are defined in core.
- **`Locator` hierarchy** — seven concrete subtypes describing *how* an anchor into a source artifact is shaped (character range, bounding box, sequence position, etc.), not *what* content the source contains.
- **`ContentReference`** — content-addressed with mandatory sha256 + hash_mode.
- **`Confidence`**, **`CompatibilityJudgment`** — universal structured metadata.
- **Enums** — `ActivityType` (the seven hyperedge types), `LifecycleState`, `ReviewState`, `EpistemicStatus`, `LineageType`, `RefusalState`, `CompatibilityStatus`, `ConfidenceBasis`, `HashMode`.
- **`EvidenceRecord.evidence_type`** — open CURIE; no core-supplied vocabulary.
- **Canonical hashing** — `canonical_hash_instance(entity)` returns a stable SHA-256 over any entity, via LinkML normalization + RFC 8785 JCS.
- **Bundled schemas** — `pygrits.schema_path()`, `pygrits.json_schema_path()`, and viewpoint helpers `viewpoint_schema_path(name)`.

**Viewpoint schemas (`pygrits.viewpoints.*`)** — domain vocabulary layered on core:

- `blank_slate_v0` — bootstrap-honest; no domain vocabulary.
- `document_extraction_v0` — evidence-type CURIEs for document extraction (`de:text_span`, `de:figure`, etc.).
- `materials_science_v0` — scope-dimension subclasses (`ThermodynamicScope`, etc.) and composite `MaterialsScienceScope`.

Type and vocabulary are viewpoint-defined, not schema-defined. Domain labels (`mse:paper`, `de:text_span`, thermodynamic scope dimensions) live in viewpoint schemas that import or extend the core.

## What this package does *not* (yet) give you

Deferred to future versions:

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

1. **Everything is an entity.** Three classes — `Object`, `Activity`, `EvidenceRecord` — share an abstract discipline contract (identity, type, viewpoint, provenance, scope, should_not_claim, review state, lifecycle, generation mode). Domain-specific labels (`mse:paper`, `mse:claim`, etc.) are CURIE values of the `type` field, drawn from viewpoint vocabulary — not Python classes in core.

2. **Activities are not Objects.** Activities transform inputs to outputs; they don't participate in conversations. They record how a step of reasoning happened. Outputs are *new* entities — Activities never mutate their inputs. This makes the append-only graph mechanical, not aspirational.

3. **Extraction is viewpoint-defined.** Every entity declares which `ViewpointDirective` shaped it. There is no neutral extraction. Different viewpoints applied to the same source produce different entities, not the same entity with different annotations.

4. **Identity by declaration, integrity by content hash.** Viewpoint directives have human-readable names plus content hashes on every referenced piece of content. Names are the human reference; hashes are the integrity check. The canonical form is RFC 8785 JCS on LinkML JSON for instances, raw bytes for opaque content.

5. **Hard refusal modes.** Every entity carries `should_not_claim`. The refusal taxonomy is five-state: `unknown`, `not_searched`, `searched_absent`, `out_of_viewpoint`, `contradicted`. The system surfaces these distinctly; it does not collapse them into a single "I don't know" or — worse — into a fabricated answer.

The full specification document lives separately; pygrits is the Python implementation of its schema-level commitments.

## Schema regeneration

```bash
bash scripts/regenerate.sh
```

This runs `gen-pydantic`, `gen-json-schema`, and `gen-doc` against `src/pygrits/core.yaml`, then regenerates viewpoint artifacts from `viewpoints/*.yaml`. CI guards that the checked-in artifacts match the sources.

## Tests

```bash
pytest
```

Test suite covers:

- Core-level example YAML files load as valid Pydantic instances against bare core.
- Materials-science viewpoint examples validate when loaded with `pygrits.viewpoints.materials_science_v0`.
- Core alone defines no domain vocabulary (`ThermodynamicScope`, `EvidenceTypeBase`, etc.).
- `evidence_type` accepts arbitrary CURIEs under core.
- Missing MVE fields fail with `ValidationError`.
- Canonical hashes are deterministic across construction order and YAML/JSON round-trip.
- `verify_content_reference` accepts matches and rejects mismatches under both hash modes.

## License

BSD-3-Clause.

## Acknowledgments

Built on [LinkML](https://linkml.io), with [Pydantic](https://docs.pydantic.dev) for runtime typing and the [jcs](https://pypi.org/project/jcs/) package for RFC 8785 canonicalization.
