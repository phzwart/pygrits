---
search:
  boost: 5.0
---

# Slot: should_not_claim 


_Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint._



<div data-search-exclude markdown="1">



URI: [grits:should_not_claim](https://w3id.org/grits/should_not_claim)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Grit](Grit.md) | Abstract base for all pygrits graph nodes |  no  |
| [Object](Object.md) | Subject node |  no  |
| [Activity](Activity.md) | Hyperedge |  no  |
| [EvidenceRecord](EvidenceRecord.md) | Anchor unit |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Grit](Grit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Grit](Grit.md) |








## In Subsets


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:should_not_claim |
| native | grits:should_not_claim |




## LinkML Source

<details>
```yaml
name: should_not_claim
description: Epistemic boundaries this grit must respect. Combination of per-class
  defaults plus directive-imposed rules from the viewpoint.
in_subset:
- MVE
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Grit
domain_of:
- Grit
range: string
required: true
multivalued: true

```
</details></div>