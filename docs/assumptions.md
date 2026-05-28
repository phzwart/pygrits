---
search:
  boost: 5.0
---

# Slot: assumptions 

<div data-search-exclude markdown="1">



URI: [grits:assumptions](https://w3id.org/grits/assumptions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompatibilityJudgment](CompatibilityJudgment.md) | A recorded compatibility judgment over a set of grits/evidence |  no  |
| [Object](Object.md) | Subject node |  no  |
| [Activity](Activity.md) | Hyperedge |  no  |
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
| Domain Of | [CompatibilityJudgment](CompatibilityJudgment.md), [Object](Object.md), [Activity](Activity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:assumptions |
| native | grits:assumptions |




## LinkML Source

<details>
```yaml
name: assumptions
domain_of:
- CompatibilityJudgment
- Object
- Activity
range: string

```
</details></div>