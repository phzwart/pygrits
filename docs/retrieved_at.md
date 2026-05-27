---
search:
  boost: 5.0
---

# Slot: retrieved_at 


_Last successful integrity verification timestamp._



<div data-search-exclude markdown="1">



URI: [isom:retrieved_at](https://w3id.org/isom/retrieved_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentReference](ContentReference.md) | Content-addressed reference to externally stored content |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Iso8601](Iso8601.md) |
| Domain Of | [ContentReference](ContentReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | isom:retrieved_at |
| native | isom:retrieved_at |




## LinkML Source

<details>
```yaml
name: retrieved_at
description: Last successful integrity verification timestamp.
from_schema: https://w3id.org/isom/core
rank: 1000
owner: ContentReference
domain_of:
- ContentReference
range: Iso8601
required: false

```
</details></div>