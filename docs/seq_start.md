---
search:
  boost: 5.0
---

# Slot: seq_start 

<div data-search-exclude markdown="1">



URI: [isom:seq_start](https://w3id.org/isom/seq_start)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequencePositionLocator](SequencePositionLocator.md) | Position range within a reference biological sequence |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [SequencePositionLocator](SequencePositionLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SequencePositionLocator](SequencePositionLocator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:seq_start |
| native | isom:seq_start |




## LinkML Source

<details>
```yaml
name: seq_start
from_schema: https://w3id.org/isom/core
rank: 1000
owner: SequencePositionLocator
domain_of:
- SequencePositionLocator
range: integer
required: true

```
</details></div>