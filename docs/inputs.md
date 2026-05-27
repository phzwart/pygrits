---
search:
  boost: 5.0
---

# Slot: inputs 


_Input entity IDs consumed by this Activity._



<div data-search-exclude markdown="1">



URI: [isom:inputs](https://w3id.org/isom/inputs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) | Transformation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EntityId](EntityId.md) |
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


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:inputs |
| native | isom:inputs |




## LinkML Source

<details>
```yaml
name: inputs
description: Input entity IDs consumed by this Activity.
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Activity
domain_of:
- Activity
range: EntityId
required: true
multivalued: true

```
</details></div>