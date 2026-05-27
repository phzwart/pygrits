---
search:
  boost: 5.0
---

# Slot: lineage 

<div data-search-exclude markdown="1">



URI: [isom:lineage](https://w3id.org/isom/lineage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvidenceRecord](EvidenceRecord.md) | Grounded data anchored to a single source artifact via a typed locator |  no  |
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


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:lineage |
| native | isom:lineage |




## LinkML Source

<details>
```yaml
name: lineage
from_schema: https://w3id.org/isom/core
rank: 1000
owner: EvidenceRecord
domain_of:
- EvidenceRecord
range: LineageType

```
</details></div>