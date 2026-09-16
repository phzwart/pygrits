# pygrits

Closed PROV-O + Web Annotation emit profile and validator. Agents dump a JSON-LD graph; this package checks it.

- [Profile terms](ns/) — `https://phzwart.github.io/pygrits/ns#`
- [grits.ttl](ns/grits.ttl) — machine-readable vocabulary
- [Source](https://github.com/phzwart/pygrits) — `PROFILE.md`, context, schema, validator

Types stay `prov:` / `oa:`. The keys this profile adds (`how`, `kind`, `rationale`, `result`, digests, …) have IRIs on the namespace page so they survive JSON-LD expansion.
