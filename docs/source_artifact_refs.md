---
search:
  boost: 5.0
---

# Slot: source_artifact_refs 


_ContentReferences to the source artifacts this Object derives from._



<div data-search-exclude markdown="1">



URI: [isom:source_artifact_refs](https://w3id.org/isom/source_artifact_refs)
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
| Range | [ContentReference](ContentReference.md) |
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


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:source_artifact_refs |
| native | isom:source_artifact_refs |




## LinkML Source

<details>
```yaml
name: source_artifact_refs
description: ContentReferences to the source artifacts this Object derives from.
in_subset:
- MVE
from_schema: https://w3id.org/isom/core
rank: 1000
owner: Object
domain_of:
- Object
range: ContentReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>