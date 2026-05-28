---
search:
  boost: 5.0
---

# Slot: parent_viewpoint_ids 


_ViewpointDirective ids this directive composes from, parents-first. Resolution is explicit (the caller supplies the registry); there is no implicit runtime parent lookup._



<div data-search-exclude markdown="1">



URI: [grits:parent_viewpoint_ids](https://w3id.org/grits/parent_viewpoint_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |
| [ComposedViewpointDirective](ComposedViewpointDirective.md) | The frozen result of composing a ViewpointDirective with optional ExtractionP... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GritId](GritId.md) |
| Domain Of | [ViewpointDirective](ViewpointDirective.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ViewpointDirective](ViewpointDirective.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:parent_viewpoint_ids |
| native | grits:parent_viewpoint_ids |




## LinkML Source

<details>
```yaml
name: parent_viewpoint_ids
description: ViewpointDirective ids this directive composes from, parents-first. Resolution
  is explicit (the caller supplies the registry); there is no implicit runtime parent
  lookup.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: ViewpointDirective
domain_of:
- ViewpointDirective
range: GritId
multivalued: true

```
</details></div>