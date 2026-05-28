---
search:
  boost: 5.0
---

# Slot: features 


_Viewpoint-defined structured payload, serialized as a JSON string in v1. The viewpoint's vocabulary determines the shape. Later versions may use a typed Any with viewpoint-declared schemas._



<div data-search-exclude markdown="1">



URI: [grits:features](https://w3id.org/grits/features)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Object](Object.md) | Subject node |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |
| [OperationalLayer](OperationalLayer.md) | Abstract base for composable operational/interpretive layers that are not the... |  no  |
| [ExtractionProfile](ExtractionProfile.md) | Extraction/grounding semantics: how finely content is decomposed, how densely... |  no  |
| [VocabularyPack](VocabularyPack.md) | Namespace/ontology binding surface: the vocabulary references, ontology refer... |  no  |
| [ReasoningPolicy](ReasoningPolicy.md) | Inferential permission surface: what synthesis, inference, normalization, and... |  no  |
| [ComposedViewpointDirective](ComposedViewpointDirective.md) | The frozen result of composing a ViewpointDirective with optional ExtractionP... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Object](Object.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | grits:features |
| native | grits:features |




## LinkML Source

<details>
```yaml
name: features
description: Viewpoint-defined structured payload, serialized as a JSON string in
  v1. The viewpoint's vocabulary determines the shape. Later versions may use a typed
  Any with viewpoint-declared schemas.
in_subset:
- ExtendedProfile
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Object
domain_of:
- Object
range: string

```
</details></div>