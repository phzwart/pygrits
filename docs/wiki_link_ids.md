---
search:
  boost: 5.0
---

# Slot: wiki_link_ids 


_Backward pointers to wiki statement Objects citing this Object._



<div data-search-exclude markdown="1">



URI: [isom:wiki_link_ids](https://w3id.org/isom/wiki_link_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Object](Object.md) | Participant in reasoning |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EntityId](EntityId.md) |
| Domain Of | [Object](Object.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Object](Object.md) |








## In Subsets


* [Full](Full.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:wiki_link_ids |
| native | isom:wiki_link_ids |




## LinkML Source

<details>
```yaml
name: wiki_link_ids
description: Backward pointers to wiki statement Objects citing this Object.
in_subset:
- Full
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Object
domain_of:
- Object
range: EntityId
multivalued: true

```
</details></div>