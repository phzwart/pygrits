---
search:
  boost: 5.0
---

# Slot: target_schema 


_Reference to the LinkML schema (or schema profile) this directive commits to._



<div data-search-exclude markdown="1">



URI: [isom:target_schema](https://w3id.org/isom/target_schema)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContentReference](ContentReference.md) |
| Domain Of | [ViewpointDirective](ViewpointDirective.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ViewpointDirective](ViewpointDirective.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:target_schema |
| native | isom:target_schema |




## LinkML Source

<details>
```yaml
name: target_schema
description: Reference to the LinkML schema (or schema profile) this directive commits
  to.
from_schema: https://w3id.org/isom/core
rank: 1000
owner: ViewpointDirective
domain_of:
- ViewpointDirective
range: ContentReference
inlined: true

```
</details></div>