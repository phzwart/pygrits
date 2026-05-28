---
search:
  boost: 5.0
---

# Slot: inputs 


_Input grit IDs consumed by this Activity._



<div data-search-exclude markdown="1">



URI: [grits:inputs](https://w3id.org/grits/inputs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) | Hyperedge |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GritId](GritId.md) |
| Domain Of | [Activity](Activity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Activity](Activity.md) |








## In Subsets


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:inputs |
| native | grits:inputs |




## LinkML Source

<details>
```yaml
name: inputs
description: Input grit IDs consumed by this Activity.
in_subset:
- MVE
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Activity
domain_of:
- Activity
range: GritId
required: true
multivalued: true

```
</details></div>