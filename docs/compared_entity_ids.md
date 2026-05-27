---
search:
  boost: 5.0
---

# Slot: compared_entity_ids 

<div data-search-exclude markdown="1">



URI: [isom:compared_entity_ids](https://w3id.org/isom/compared_entity_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompatibilityJudgment](CompatibilityJudgment.md) | A recorded compatibility judgment over a set of entities/evidence |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EntityId](EntityId.md) |
| Domain Of | [CompatibilityJudgment](CompatibilityJudgment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CompatibilityJudgment](CompatibilityJudgment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:compared_entity_ids |
| native | isom:compared_entity_ids |




## LinkML Source

<details>
```yaml
name: compared_entity_ids
from_schema: https://w3id.org/isom/core
rank: 1000
owner: CompatibilityJudgment
domain_of:
- CompatibilityJudgment
range: EntityId
required: true
multivalued: true

```
</details></div>