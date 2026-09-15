# pygrits

Structured epistemic containment for agentic scientific reasoning. pygrits is a LinkML core schema plus a small Python library: every claim, measurement, and pipeline step is a **grit** with declared identity, viewpoint, optional integrity hash, and typed links to evidence. Domain vocabulary lives in viewpoint schemas that subclass `Entity` and `Scope`, not in core.

## Motivating example

An agent is asked for the catalytic turnover number (k_cat) of enzyme E on substrate S. The corpus reports k_cat for related substrates S1–S3 but not S.

| Outcome | Representation |
|--------|----------------|
| Anchored measurements | `EvidenceRecord` with a `Locator` |
| Search for S finds nothing | `NegativeEvidenceRecord` (`result: absent`) |
| Optional synthesis | `Activity` (`derivation`) → `Entity` with `EvidenceLink` labels and optional `caveats` |

Direct evidence, absence, and inference stay in separate slots with explicit labels.

## Install

```bash
pip install -e .
pip install -e '.[test]'    # pytest
pip install -e '.[schema]'  # regenerate LinkML artifacts
pip install -e '.[rdf]'     # PROV RDF export
```

Python 3.11+.

## Three roles

- **Entity** — subject node (claim, document, measurement). Domain schemas subclass this with typed slots.
- **Activity** — hyperedge: `inputs`, optional `outputs`, `activity_type`.
- **EvidenceRecord** — anchor into a source via `ContentReference` + `Locator`.

**Activity types:** `derivation` (inputs → new entity), `support`, `contradiction` (no outputs), `adjudication`.

**Evidence labels** (on `Entity.evidence` → `EvidenceLink`): `direct`, `derived`, `inferred`, `unknown`. Use `validate_bundle()` to require rationale for `derived` / `inferred`.

## Quickstart

```python
from pygrits import (
    Entity, EvidenceRecord, ContentReference, HashMode, LineRangeLocator,
    EvidenceLink, EvidenceLabel, canonical_hash_instance, validate_bundle,
)

evi = EvidenceRecord(
    id="evi:demo",
    viewpoint_id="vpt:demo",
    source=ContentReference(
        uri="file://paper.txt",
        sha256="a" * 64,
        hash_mode=HashMode.raw_bytes,
    ),
    locator=LineRangeLocator(
        locator_type="LineRangeLocator",
        path="paper.txt",
        line_start=10,
        line_end=12,
    ),
)
ent = Entity(
    id="ent:demo",
    viewpoint_id="vpt:demo",
    evidence=[EvidenceLink(evidence_id="evi:demo", label=EvidenceLabel.direct)],
)
validate_bundle([evi, ent])
print(canonical_hash_instance(ent))
```

## PROV export

With `[rdf]` installed:

```python
from pygrits.rdf import to_graph
g = to_graph([evi, ent])
```

Activities emit `prov:used` / `prov:generated`; entities emit `prov:Entity` and `prov:hadPrimarySource` where applicable.

## Extending with a domain schema

```yaml
id: https://example.org/my_domain
name: my_domain
imports:
  - linkml:types
  - pygrits/core   # or path to shipped core.yaml

classes:
  CatalyticClaim:
    is_a: Entity
    attributes:
      k_cat_per_s: { range: float, required: true }
      enzyme_id: { range: string, required: true }
  AssayScope:
    is_a: Scope
    attributes:
      scope_type: { designates_type: true, required: true }
      temperature_kelvin: { range: float }
```

Ship one viewpoint YAML (see `viewpoints/document_extraction_v0.yaml`) for evidence-type CURIEs; bind scientific slots in your domain import.

## Layout

- `src/pygrits/core.yaml` — LinkML source (generated: `core.py`, `core.schema.json`, `core.context.jsonld`)
- `examples/` — one valid demo bundle
- `guide/` — role-oriented notes

Autodoc under `docs/` is generated in CI only, not committed.
