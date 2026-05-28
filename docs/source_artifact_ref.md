---
search:
  boost: 5.0
---

# Slot: source_artifact_ref 


_Single source artifact this evidence is extracted from._



<div data-search-exclude markdown="1">



URI: [grits:source_artifact_ref](https://w3id.org/grits/source_artifact_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvidenceRecord](EvidenceRecord.md) | Anchor unit |  no  |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContentReference](ContentReference.md) |
| Domain Of | [EvidenceRecord](EvidenceRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EvidenceRecord](EvidenceRecord.md) |








## In Subsets


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:source_artifact_ref |
| native | grits:source_artifact_ref |




## LinkML Source

<details>
```yaml
name: source_artifact_ref
description: Single source artifact this evidence is extracted from.
in_subset:
- MVE
from_schema: https://w3id.org/grits/core
rank: 1000
owner: EvidenceRecord
domain_of:
- EvidenceRecord
range: ContentReference
required: true
inlined: true

```
</details></div>