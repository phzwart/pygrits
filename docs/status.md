---
search:
  boost: 5.0
---

# Slot: status 

<div data-search-exclude markdown="1">



URI: [grits:status](https://w3id.org/grits/status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompatibilityJudgment](CompatibilityJudgment.md) | A recorded compatibility judgment over a set of grits/evidence |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CompatibilityStatus](CompatibilityStatus.md) |
| Domain Of | [CompatibilityJudgment](CompatibilityJudgment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CompatibilityJudgment](CompatibilityJudgment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:status |
| native | grits:status |




## LinkML Source

<details>
```yaml
name: status
from_schema: https://w3id.org/grits/core
rank: 1000
owner: CompatibilityJudgment
domain_of:
- CompatibilityJudgment
range: CompatibilityStatus
required: true

```
</details></div>