---
search:
  boost: 5.0
---

# Slot: locator 

<div data-search-exclude markdown="1">



URI: [isom:locator](https://w3id.org/isom/locator)
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
| Range | [Locator](Locator.md) |
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


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:locator |
| native | isom:locator |




## LinkML Source

<details>
```yaml
name: locator
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
owner: EvidenceRecord
domain_of:
- EvidenceRecord
range: Locator
required: true
inlined: true

```
</details></div>