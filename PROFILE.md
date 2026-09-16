# pygrits profile

Emit a JSON-LD graph. This file is the contract. Do not invent types or keys.

Profile keys have IRIs in `context.jsonld` (`grits:` = `https://phzwart.github.io/pygrits/ns#`) so they survive JSON-LD expansion. Types stay `prov:` / `oa:`. `plan` is `grits:plan`, a documented sub-property of `prov:wasInfluencedBy`.

## Shape

- The document has `@context` and `@graph`.
- Every node is `prov:Entity`, `prov:Activity`, or `prov:Plan`.
- `@id` is a compact id (`plan:…`, `evi:…`, `act:…`, `ent:…`).
- The plan you followed is a `prov:Plan` in the same graph. Every other node sets `plan` to that `@id`.
- The plan carries `prompt_digest` and `schema_digest`: SHA-256 hex of the prompt bytes and of the payload schema bytes.
- Optional `plan_variable` on an entity (`pplan:correspondsToVariable`) and `plan_step` on an activity (`pplan:correspondsToStep`) bind the node to a type-level transformation graph.

## Sources

- Point at bytes with `source`: `{ "uri", "sha256" }`. `sha256` is lowercase hex of the raw file. `uri` is the node’s `@id` in RDF.
- Point into the file with `target.selector`. Use a Web Annotation type:
  - `oa:TextQuoteSelector` (`exact`, optional `prefix` / `suffix`) — prefer this
  - `oa:TextPositionSelector` (`start`, `end`)
  - `oa:DataPositionSelector` (`start`, `end` bytes)
  - `oa:FragmentSelector` (`value`, optional `conformsTo`)
- Optional `target.hasSource` repeats the artifact URI.

## How a claim relates to a source

On a `prov:Entity`, set `how` to one of: `quote`, `derived`, `inferred`, `unknown`.

- `quote` — the selector is the statement. Requires `source` and `target`. No `result`.
- `derived` / `inferred` — require a non-empty `rationale`.
- `unknown` — the slot is needed and nothing fills it.

Domain values (k_cat, temperature, …) do not go on these nodes. Put them in another document. Set `payload` to that schema’s URL and `payload_ref` to a `{ "uri", "sha256" }` of the document itself.

## Attribution

- `agent` on a `prov:Entity` or `prov:Plan` (`prov:wasAttributedTo`)
- `performed_by` on a `prov:Activity` (`prov:wasAssociatedWith`)

## Absence

If you searched and found nothing, emit a `prov:Entity` with `result` (`absent`, `weak`, `excluded`, `inconclusive`) and a required `summary` of the search. No selector required. Do not stay silent.

## Activities

A `prov:Activity` has `kind`, `used` (ids), and optional `generated` (ids).

- `derivation` — inputs produce a new entity
- `support` / `contradiction` — no `generated`
- `adjudication` — resolves contradictions; requires `rationale`

Optional `started_at` / `ended_at` (`xsd:dateTime`). Optional `rationale` on any activity.

## Forbidden

- Extra keys
- New `@type` values
- Locator classes, viewpoint subclasses, or domain slots on these nodes
- Treating inferred absence as a measured value
- `agent` on an activity, or `performed_by` on an entity
