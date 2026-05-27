---
search:
  boost: 5.0
---

# Slot: synthesis_link_ids 


_Backward pointers to Activities that referenced this Object as input or output._



<div data-search-exclude markdown="1">



URI: [isom:synthesis_link_ids](https://w3id.org/isom/synthesis_link_ids)
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
| self | isom:synthesis_link_ids |
| native | isom:synthesis_link_ids |




## LinkML Source

<details>
```yaml
name: synthesis_link_ids
description: Backward pointers to Activities that referenced this Object as input
  or output.
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