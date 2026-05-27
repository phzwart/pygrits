---
search:
  boost: 5.0
---

# Slot: type 


_For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. isom:activity_type/synthesis_edge)._



<div data-search-exclude markdown="1">



URI: [isom:type](https://w3id.org/isom/type)
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
| Range | [CurieOrUri](CurieOrUri.md) |
| Domain Of | [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Entity](Entity.md) |








## In Subsets


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:type |
| native | isom:type |




## LinkML Source

<details>
```yaml
name: type
description: For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For
  Activity, a CURIE corresponding to the ActivityType value (e.g. isom:activity_type/synthesis_edge).
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Entity
domain_of:
- Entity
range: CurieOrUri
required: true

```
</details></div>