---
search:
  boost: 5.0
---

# Slot: scope 


_Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this entity's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them._



<div data-search-exclude markdown="1">



URI: [isom:scope](https://w3id.org/isom/scope)
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
| Range | [Scope](Scope.md) |
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
| self | isom:scope |
| native | isom:scope |




## LinkML Source

<details>
```yaml
name: scope
description: Optional but recommended. Viewpoint-supplied scope dimensions describing
  the conditions under which this entity's statements apply. The core Scope marker
  carries no domain dimensions; load a viewpoint schema to populate them.
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Entity
domain_of:
- Entity
range: Scope
inlined: true

```
</details></div>