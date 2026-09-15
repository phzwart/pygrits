# Activity

An **Activity** is a hyperedge: it **uses** input grit ids and may **generate** output entity ids. It subclasses **Grit** and maps to `prov:Activity`.

## Activity types

| Type | Role |
|------|------|
| `derivation` | Inputs (entities and/or evidence) → new entity |
| `support` | Evidence supports an entity; **no outputs** |
| `contradiction` | Evidence contradicts an entity; **no outputs** |
| `adjudication` | Resolves contradictions → curator decision entity |

`validate_bundle()` rejects `outputs` on `support` and `contradiction`.

## Slots

- `inputs` (required) — `prov:used`
- `outputs` — `prov:generated`
- `plan_step` — optional P-Plan step CURIE (`pplan:correspondsToStep`)
- `rationale` — why this activity is admissible
- `confidence` — structured confidence block
- `started_at` / `ended_at` — activity interval

Find edges by querying activities; nodes do not store backward pointers.
