---
search:
  boost: 5.0
---

# Slot: needs 

<div data-search-exclude markdown="1">



URI: [isom:needs](https://w3id.org/isom/needs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Object](Object.md) | Participant in reasoning |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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


* [ParticipationReady](ParticipationReady.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:needs |
| native | isom:needs |




## LinkML Source

<details>
```yaml
name: needs
in_subset:
- ParticipationReady
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Object
domain_of:
- Object
range: string
multivalued: true

```
</details></div>