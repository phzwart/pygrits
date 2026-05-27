---
search:
  boost: 5.0
---

# Slot: outputs 


_New entities produced by this Activity. May be empty for declarative edges (SUPPORT, CONTRADICTION) whose output is the Activity itself._



<div data-search-exclude markdown="1">



URI: [isom:outputs](https://w3id.org/isom/outputs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) | Transformation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EntityId](EntityId.md) |
| Domain Of | [Activity](Activity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Activity](Activity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:outputs |
| native | isom:outputs |




## LinkML Source

<details>
```yaml
name: outputs
description: New entities produced by this Activity. May be empty for declarative
  edges (SUPPORT, CONTRADICTION) whose output is the Activity itself.
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Activity
domain_of:
- Activity
range: EntityId
multivalued: true

```
</details></div>