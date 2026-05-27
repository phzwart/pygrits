---
search:
  boost: 5.0
---

# Slot: id 


_Canonical entity identifier._



<div data-search-exclude markdown="1">



URI: [isom:id](https://w3id.org/isom/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Entity](Entity.md) | Abstract base for all ISOM entities |  no  |
| [Object](Object.md) | Participant in reasoning |  no  |
| [Activity](Activity.md) | Transformation |  no  |
| [EvidenceRecord](EvidenceRecord.md) | Grounded data anchored to a single source artifact via a typed locator |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |  no  |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EntityId](EntityId.md) |
| Domain Of | [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Entity](Entity.md) |








## In Subsets


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:id |
| native | isom:id |




## LinkML Source

<details>
```yaml
name: id
description: Canonical entity identifier.
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
identifier: true
owner: Entity
domain_of:
- Entity
range: EntityId
required: true

```
</details></div>