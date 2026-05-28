---
search:
  boost: 5.0
---

# Slot: layer_name 


_Human-readable name (e.g. extraction_profile:detailed:v0). Combined with content hash, this gives identity-by-declaration._



<div data-search-exclude markdown="1">



URI: [grits:layer_name](https://w3id.org/grits/layer_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OperationalLayer](OperationalLayer.md) | Abstract base for composable operational/interpretive layers that are not the... |  no  |
| [ExtractionProfile](ExtractionProfile.md) | Extraction/grounding semantics: how finely content is decomposed, how densely... |  no  |
| [VocabularyPack](VocabularyPack.md) | Namespace/ontology binding surface: the vocabulary references, ontology refer... |  no  |
| [ReasoningPolicy](ReasoningPolicy.md) | Inferential permission surface: what synthesis, inference, normalization, and... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OperationalLayer](OperationalLayer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OperationalLayer](OperationalLayer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:layer_name |
| native | grits:layer_name |




## LinkML Source

<details>
```yaml
name: layer_name
description: Human-readable name (e.g. extraction_profile:detailed:v0). Combined with
  content hash, this gives identity-by-declaration.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: OperationalLayer
domain_of:
- OperationalLayer
range: string
required: true

```
</details></div>