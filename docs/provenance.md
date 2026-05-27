---
search:
  boost: 5.0
---

# Slot: provenance 


_Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools._



<div data-search-exclude markdown="1">



URI: [isom:provenance](https://w3id.org/isom/provenance)
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
| self | isom:provenance |
| native | isom:provenance |




## LinkML Source

<details>
```yaml
name: provenance
description: Provenance description for v1. Future versions will model provenance
  as structured edges into the hyperDAG; for now a free-form string is accepted to
  allow ingestion bundles from upstream extraction tools.
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Entity
domain_of:
- Entity
range: string
required: true

```
</details></div>