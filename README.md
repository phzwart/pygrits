# pygrits

Closed **PROV-O + Web Annotation** emit profile and validator. Agents dump a JSON-LD graph; this package checks it. Types are `prov:` / `oa:`. Remaining keys have IRIs under `https://phzwart.github.io/pygrits/ns#` so they survive expansion.

The contract is [`PROFILE.md`](PROFILE.md). Attach `profile_text()` or `schema.json` to the run.

## What you emit

A `@graph` of `prov:Plan`, `prov:Entity`, and `prov:Activity`. Quotes use `oa:TextQuoteSelector`. Failed searches are entities with `result: absent` and a `summary`. Domain values live in another document: `payload` is that schema’s URL, `payload_ref` is the document’s `{uri, sha256}`.

`plan` on a node is `grits:plan` (sub-property of `prov:wasInfluencedBy`). Optional `plan_step` / `plan_variable` bind to a P-Plan graph. Entities use `agent`; activities use `performed_by`.

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

`validate()` fails on dangling ids, inferred/derived without rationale, quotes without a selector, support/contradiction activities that generate nodes, adjudication without rationale, and absence without a summary.

## Layout

- `PROFILE.md` — agent directive
- `src/pygrits/context.jsonld` — `prov` / `oa` / `pplan` / `grits` term map
- `src/pygrits/schema.json` — closed JSON Schema for structured output
- `examples/kcat.jsonld` — enzyme story (quote, absence, derivation)
