---
search:
  boost: 5.0
---

# Slot: generation_mode 


_Free-form descriptor of the process that generated this entity (parser name + version, viewpoint name + version, LLM model + tier)._



<div data-search-exclude markdown="1">



URI: [isom:generation_mode](https://w3id.org/isom/generation_mode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Entity](Entity.md) | Abstract base for all ISOM entities |  no  |
| [Object](Object.md) | Participant in reasoning |  no  |
| [Activity](Activity.md) | Transformation |  no  |
| [EvidenceRecord](EvidenceRecord.md) | Grounded data anchored to a single source artifact via a typed locator |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |  no  |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Entity](Entity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:generation_mode |
| native | isom:generation_mode |




## LinkML Source

<details>
```yaml
name: generation_mode
description: Free-form descriptor of the process that generated this entity (parser
  name + version, viewpoint name + version, LLM model + tier).
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Entity
domain_of:
- Entity
range: string

```
</details></div>