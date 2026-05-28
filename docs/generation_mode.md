---
search:
  boost: 5.0
---

# Slot: generation_mode 


_Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier)._



<div data-search-exclude markdown="1">



URI: [grits:generation_mode](https://w3id.org/grits/generation_mode)
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






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Grit](Grit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Grit](Grit.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:generation_mode |
| native | grits:generation_mode |




## LinkML Source

<details>
```yaml
name: generation_mode
description: Free-form descriptor of the process that generated this grit (parser
  name + version, viewpoint name + version, LLM model + tier).
from_schema: https://w3id.org/grits/core
rank: 1000
owner: Grit
domain_of:
- Grit
range: string

```
</details></div>