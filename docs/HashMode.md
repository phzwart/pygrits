---
search:
  boost: 2.0
---


# Enum: HashMode 




_How a ContentReference's sha256 is computed._



<div data-search-exclude markdown="1">

URI: [grits:HashMode](https://w3id.org/grits/HashMode)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| raw_bytes | None | SHA-256 of the file bytes as stored |
| linkml_canonical_jcs | None | LinkML normalize → JSON via LinkML mapping → RFC 8785 JCS → SHA-256 |




## Slots

| Name | Description |
| ---  | --- |
| [hash_mode](hash_mode.md) | How the sha256 was computed |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core






## LinkML Source

<details>
```yaml
name: HashMode
description: How a ContentReference's sha256 is computed.
from_schema: https://w3id.org/grits/core
rank: 1000
permissible_values:
  raw_bytes:
    text: raw_bytes
    description: SHA-256 of the file bytes as stored.
  linkml_canonical_jcs:
    text: linkml_canonical_jcs
    description: LinkML normalize → JSON via LinkML mapping → RFC 8785 JCS → SHA-256.

```
</details>

</div>