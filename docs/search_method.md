---
search:
  boost: 5.0
---

# Slot: search_method 

<div data-search-exclude markdown="1">



URI: [grits:search_method](https://w3id.org/grits/search_method)
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
| self | grits:search_method |
| native | grits:search_method |




## LinkML Source

<details>
```yaml
name: search_method
from_schema: https://w3id.org/grits/core
rank: 1000
owner: NegativeEvidenceRecord
domain_of:
- NegativeEvidenceRecord
range: string
required: true

```
</details></div>