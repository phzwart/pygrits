---
search:
  boost: 5.0
---

# Slot: composition_mode 


_How this layer folds against its declared parents during resolution. Defaults to additive._



<div data-search-exclude markdown="1">



URI: [grits:composition_mode](https://w3id.org/grits/composition_mode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |
| [Composable](Composable.md) | Mixin granting a layer a composition_mode |  no  |
| [OperationalLayer](OperationalLayer.md) | Abstract base for composable operational/interpretive layers that are not the... |  no  |
| [ExtractionProfile](ExtractionProfile.md) | Extraction/grounding semantics: how finely content is decomposed, how densely... |  no  |
| [VocabularyPack](VocabularyPack.md) | Namespace/ontology binding surface: the vocabulary references, ontology refer... |  no  |
| [ReasoningPolicy](ReasoningPolicy.md) | Inferential permission surface: what synthesis, inference, normalization, and... |  no  |
| [ComposedViewpointDirective](ComposedViewpointDirective.md) | The frozen result of composing a ViewpointDirective with optional ExtractionP... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CompositionMode](CompositionMode.md) |
| Domain Of | [Composable](Composable.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `string(additive)` |
| Owner | [Composable](Composable.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:composition_mode |
| native | grits:composition_mode |




## LinkML Source

<details>
```yaml
name: composition_mode
description: How this layer folds against its declared parents during resolution.
  Defaults to additive.
from_schema: https://w3id.org/grits/core
rank: 1000
ifabsent: string(additive)
owner: Composable
domain_of:
- Composable
range: CompositionMode

```
</details></div>