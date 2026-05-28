---
search:
  boost: 5.0
---

# Slot: require_grounding_for_content_kinds 


_Content kinds (viewpoint-supplied CURIEs) that must be grounded in an evidence record._



<div data-search-exclude markdown="1">



URI: [grits:require_grounding_for_content_kinds](https://w3id.org/grits/require_grounding_for_content_kinds)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExtractionProfile](ExtractionProfile.md) | Extraction/grounding semantics: how finely content is decomposed, how densely... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CurieOrUri](CurieOrUri.md) |
| Domain Of | [ExtractionProfile](ExtractionProfile.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ExtractionProfile](ExtractionProfile.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:require_grounding_for_content_kinds |
| native | grits:require_grounding_for_content_kinds |




## LinkML Source

<details>
```yaml
name: require_grounding_for_content_kinds
description: Content kinds (viewpoint-supplied CURIEs) that must be grounded in an
  evidence record.
from_schema: https://w3id.org/grits/core
rank: 1000
owner: ExtractionProfile
domain_of:
- ExtractionProfile
range: CurieOrUri
multivalued: true

```
</details></div>