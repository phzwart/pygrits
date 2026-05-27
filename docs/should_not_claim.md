---
search:
  boost: 5.0
---

# Slot: should_not_claim 


_Epistemic boundaries this entity must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint._



<div data-search-exclude markdown="1">



URI: [isom:should_not_claim](https://w3id.org/isom/should_not_claim)
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
| Range | [String](String.md) |
| Domain Of | [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
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
| self | isom:should_not_claim |
| native | isom:should_not_claim |




## LinkML Source

<details>
```yaml
name: should_not_claim
description: Epistemic boundaries this entity must respect. Combination of per-class
  defaults plus directive-imposed rules from the viewpoint.
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Entity
domain_of:
- Entity
range: string
required: true
multivalued: true

```
</details></div>