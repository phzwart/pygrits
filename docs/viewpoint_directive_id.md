---
search:
  boost: 5.0
---

# Slot: viewpoint_directive_id 

<div data-search-exclude markdown="1">



URI: [isom:viewpoint_directive_id](https://w3id.org/isom/viewpoint_directive_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Confidence](Confidence.md) | Structured confidence carrying calibration metadata |  no  |
| [CompatibilityJudgment](CompatibilityJudgment.md) | A recorded compatibility judgment over a set of entities/evidence |  no  |
| [Entity](Entity.md) | Abstract base for all ISOM entities |  no  |
| [Object](Object.md) | Participant in reasoning |  no  |
| [Activity](Activity.md) | Transformation |  no  |
| [EvidenceRecord](EvidenceRecord.md) | Grounded data anchored to a single source artifact via a typed locator |  no  |
| [ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |  no  |
| [NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Confidence](Confidence.md), [CompatibilityJudgment](CompatibilityJudgment.md), [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:viewpoint_directive_id |
| native | isom:viewpoint_directive_id |




## LinkML Source

<details>
```yaml
name: viewpoint_directive_id
domain_of:
- Confidence
- CompatibilityJudgment
- Entity
range: string

```
</details></div>