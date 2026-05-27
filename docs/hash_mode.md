---
search:
  boost: 5.0
---

# Slot: hash_mode 


_How the sha256 was computed._



<div data-search-exclude markdown="1">



URI: [isom:hash_mode](https://w3id.org/isom/hash_mode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentReference](ContentReference.md) | Content-addressed reference to externally stored content |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [HashMode](HashMode.md) |
| Domain Of | [ContentReference](ContentReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentReference](ContentReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:hash_mode |
| native | isom:hash_mode |




## LinkML Source

<details>
```yaml
name: hash_mode
description: How the sha256 was computed.
from_schema: https://w3id.org/isom/core
rank: 1000
owner: ContentReference
domain_of:
- ContentReference
range: HashMode
required: true

```
</details></div>