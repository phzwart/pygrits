---
search:
  boost: 5.0
---

# Slot: observations 

<div data-search-exclude markdown="1">



URI: [grits:observations](https://w3id.org/grits/observations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Object](Object.md) | Subject node |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |






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


* [ExtendedProfile](ExtendedProfile.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:observations |
| native | grits:observations |




## LinkML Source

<details>
```yaml
name: observations
in_subset:
- ExtendedProfile
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Object
domain_of:
- Object
range: string
multivalued: true

```
</details></div>