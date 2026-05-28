---
search:
  boost: 5.0
---

# Slot: evidence_record_ids 


_References to EvidenceRecord grits anchoring this Object's claims._



<div data-search-exclude markdown="1">



URI: [grits:evidence_record_ids](https://w3id.org/grits/evidence_record_ids)
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


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:evidence_record_ids |
| native | grits:evidence_record_ids |




## LinkML Source

<details>
```yaml
name: evidence_record_ids
description: References to EvidenceRecord grits anchoring this Object's claims.
in_subset:
- MVE
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Object
domain_of:
- Object
range: GritId
multivalued: true

```
</details></div>