# ViewpointDirective

A **ViewpointDirective** is a flat interpretive contract. It subclasses **Entity** and maps to `prov:Plan`. There is no inheritance chain of viewpoints: domain-free extraction uses a minimal directive whose main content is `name`.

## Fields

- `name` (required)
- `prompts`, `exemplars`, `vocabularies` — content-addressed refs
- `target_schema` — LinkML schema for extracted nodes
- `constraints` — rules applied to every node under this viewpoint

Every grit records `viewpoint_id` pointing at the directive that shaped it.

## Shipped viewpoint

`document_extraction_v0` declares evidence-type CURIEs for document extraction (`de:text_span`, `de:table`, …). Import it from domain schemas; core stays vocabulary-free.
