---
search:
  boost: 5.0
---

# Slot: normalized_payload 


_Viewpoint-defined structured payload, serialized as a JSON string in v1._



<div data-search-exclude markdown="1">



URI: [grits:normalized_payload](https://w3id.org/grits/normalized_payload)
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
| Range | [String](String.md) |
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
| self | grits:normalized_payload |
| native | grits:normalized_payload |




## LinkML Source

<details>
```yaml
name: normalized_payload
description: Viewpoint-defined structured payload, serialized as a JSON string in
  v1.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: EvidenceRecord
domain_of:
- EvidenceRecord
range: string

```
</details></div>