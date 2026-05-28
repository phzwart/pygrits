---
search:
  boost: 5.0
---

# Slot: type 


_For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge)._



<div data-search-exclude markdown="1">



URI: [grits:type](https://w3id.org/grits/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Grit](Grit.md) | Abstract base for all pygrits graph nodes |  no  |
| [Object](Object.md) | Subject node |  no  |
| [Activity](Activity.md) | Hyperedge |  no  |
| [EvidenceRecord](EvidenceRecord.md) | Anchor unit |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |  no  |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |
| [OperationalLayer](OperationalLayer.md) | Abstract base for composable operational/interpretive layers that are not the... |  no  |
| [ExtractionProfile](ExtractionProfile.md) | Extraction/grounding semantics: how finely content is decomposed, how densely... |  no  |
| [VocabularyPack](VocabularyPack.md) | Namespace/ontology binding surface: the vocabulary references, ontology refer... |  no  |
| [ReasoningPolicy](ReasoningPolicy.md) | Inferential permission surface: what synthesis, inference, normalization, and... |  no  |
| [ComposedViewpointDirective](ComposedViewpointDirective.md) | The frozen result of composing a ViewpointDirective with optional ExtractionP... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CurieOrUri](CurieOrUri.md) |
| Domain Of | [Grit](Grit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Grit](Grit.md) |








## In Subsets


* [MVE](MVE.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:type |
| native | grits:type |




## LinkML Source

<details>
```yaml
name: type
description: For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For
  Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).
in_subset:
- MVE
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Grit
domain_of:
- Grit
range: CurieOrUri
required: true

```
</details></div>