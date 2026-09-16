# pygrits namespace

`https://phzwart.github.io/pygrits/ns#` — the properties the pygrits emit profile adds on top of PROV-O and Web Annotation. Machine-readable: [grits.ttl](grits.ttl).

| term | meaning |
|---|---|
| `plan` | the `prov:Plan` this node was produced under (sub-property of `prov:wasInfluencedBy`) |
| `how` | quote / derived / inferred / unknown |
| `kind` | derivation / support / contradiction / adjudication |
| `rationale` | stated reasoning |
| `result` | absent / weak / excluded / inconclusive |
| `payloadSchema` | IRI of the domain schema |
| `payloadRef` | content-addressed domain document |
| `contentHash`, `promptDigest`, `schemaDigest`, `sha256` | SHA-256 hex digests |
