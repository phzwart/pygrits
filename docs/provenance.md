---
search:
  boost: 5.0
---

# Slot: provenance 


_Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools._



<div data-search-exclude markdown="1">



URI: [grits:provenance](https://w3id.org/grits/provenance)
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
| self | grits:provenance |
| native | grits:provenance |




## LinkML Source

<details>
```yaml
name: provenance
description: Provenance description for v1. Future versions will model provenance
  as structured edges into the hyperDAG; for now a free-form string is accepted to
  allow ingestion bundles from upstream extraction tools.
in_subset:
- MVE
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Grit
domain_of:
- Grit
range: string
required: true

```
</details></div>