---
search:
  boost: 5.0
---

# Slot: evidence_type 


_CURIE identifying the kind of scientific content the locator anchors. No core-supplied permissible values; viewpoints supply the evidence-type vocabulary they use._



<div data-search-exclude markdown="1">



URI: [grits:evidence_type](https://w3id.org/grits/evidence_type)
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
| Range | [CurieOrUri](CurieOrUri.md) |
| Domain Of | [EvidenceRecord](EvidenceRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EvidenceRecord](EvidenceRecord.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:evidence_type |
| native | grits:evidence_type |




## LinkML Source

<details>
```yaml
name: evidence_type
description: CURIE identifying the kind of scientific content the locator anchors.
  No core-supplied permissible values; viewpoints supply the evidence-type vocabulary
  they use.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: EvidenceRecord
domain_of:
- EvidenceRecord
range: CurieOrUri

```
</details></div>