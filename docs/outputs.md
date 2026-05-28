---
search:
  boost: 5.0
---

# Slot: outputs 


_New grits produced by this Activity. May be empty for declarative edges (SUPPORT, CONTRADICTION) whose output is the Activity itself._



<div data-search-exclude markdown="1">



URI: [grits:outputs](https://w3id.org/grits/outputs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) | Hyperedge |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GritId](GritId.md) |
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


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:outputs |
| native | grits:outputs |




## LinkML Source

<details>
```yaml
name: outputs
description: New grits produced by this Activity. May be empty for declarative edges
  (SUPPORT, CONTRADICTION) whose output is the Activity itself.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Activity
domain_of:
- Activity
range: GritId
multivalued: true

```
</details></div>