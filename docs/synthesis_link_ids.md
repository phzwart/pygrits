---
search:
  boost: 5.0
---

# Slot: synthesis_link_ids 


_Backward pointers to Activities that referenced this Object as input or output._



<div data-search-exclude markdown="1">



URI: [grits:synthesis_link_ids](https://w3id.org/grits/synthesis_link_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Object](Object.md) | Subject node |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GritId](GritId.md) |
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


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:synthesis_link_ids |
| native | grits:synthesis_link_ids |




## LinkML Source

<details>
```yaml
name: synthesis_link_ids
description: Backward pointers to Activities that referenced this Object as input
  or output.
in_subset:
- Full
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Object
domain_of:
- Object
range: GritId
multivalued: true

```
</details></div>