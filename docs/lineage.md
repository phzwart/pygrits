---
search:
  boost: 5.0
---

# Slot: lineage 

<div data-search-exclude markdown="1">



URI: [grits:lineage](https://w3id.org/grits/lineage)
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
| Range | [LineageType](LineageType.md) |
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
| self | grits:lineage |
| native | grits:lineage |




## LinkML Source

<details>
```yaml
name: lineage
from_schema: https://w3id.org/grits/core
rank: 1000
owner: EvidenceRecord
domain_of:
- EvidenceRecord
range: LineageType

```
</details></div>