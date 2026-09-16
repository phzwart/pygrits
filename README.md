# pygrits

Closed **PROV-O + Web Annotation** emit profile and validator. Agents dump a JSON-LD graph; this package checks it. It is not a new ontology.

The contract is [`PROFILE.md`](PROFILE.md). Attach `profile_text()` or `schema.json` to the run.

## What you emit

A `@graph` of `prov:Plan`, `prov:Entity`, and `prov:Activity`. Quotes use `oa:TextQuoteSelector`. Failed searches are entities with `result: absent`. Domain values live in a `payload` schema, not here.

## Install

```bash
pip install -e .
pip install -e '.[test]'
```

Python 3.11+.

## Quickstart

```python
from pygrits import load, stamp, validate, profile_text

bundle = load("examples/kcat.jsonld")
validate(bundle)
stamped = stamp(bundle)
print(profile_text()[:80])
```

`validate()` fails on dangling ids, inferred/derived without rationale, quotes without a selector, and support/contradiction activities that generate nodes.

## Layout

- `PROFILE.md` — agent directive
- `src/pygrits/context.jsonld` — `prov` / `oa` / `dcterms` aliases
- `src/pygrits/schema.json` — closed JSON Schema for structured output
- `examples/kcat.jsonld` — enzyme story (quote, absence, derivation)
