---
search:
  boost: 5.0
---

# Slot: result 


_One of `absent`, `weak_signal`, `excluded`, `inconclusive`._



<div data-search-exclude markdown="1">



URI: [grits:result](https://w3id.org/grits/result)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [NegativeEvidenceRecord](NegativeEvidenceRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [NegativeEvidenceRecord](NegativeEvidenceRecord.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:result |
| native | grits:result |




## LinkML Source

<details>
```yaml
name: result
description: One of `absent`, `weak_signal`, `excluded`, `inconclusive`.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: NegativeEvidenceRecord
domain_of:
- NegativeEvidenceRecord
range: string
required: true

```
</details></div>