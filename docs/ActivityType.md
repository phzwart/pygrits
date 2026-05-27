---
search:
  boost: 2.0
---


# Enum: ActivityType 




_Structural type of an Activity (hyperedge in the topology)._



<div data-search-exclude markdown="1">

URI: [isom:ActivityType](https://w3id.org/isom/ActivityType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SYNTHESIS_EDGE | None | Inputs + assumptions → new synthesis entity |
| SUPPORT_EDGE | None | Evidence → claim/synthesis it supports |
| CONTRADICTION_EDGE | None | Evidence → claim/synthesis it contradicts |
| COMPATIBILITY_EDGE | None | Records a compatibility judgment over entities |
| VALIDATION_EDGE | None | Validating entity → entity it validates |
| ACTION_EDGE | None | Action entity with inputs and output entities |
| ADJUDICATION_EDGE | None | Resolves a set of CONTRADICTION_EDGEs |




## Slots

| Name | Description |
| ---  | --- |
| [activity_type](activity_type.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core






## LinkML Source

<details>
```yaml
name: ActivityType
description: Structural type of an Activity (hyperedge in the topology).
from_schema: https://w3id.org/isom/core
rank: 1000
permissible_values:
  SYNTHESIS_EDGE:
    text: SYNTHESIS_EDGE
    description: Inputs + assumptions → new synthesis entity.
  SUPPORT_EDGE:
    text: SUPPORT_EDGE
    description: Evidence → claim/synthesis it supports.
  CONTRADICTION_EDGE:
    text: CONTRADICTION_EDGE
    description: Evidence → claim/synthesis it contradicts.
  COMPATIBILITY_EDGE:
    text: COMPATIBILITY_EDGE
    description: Records a compatibility judgment over entities.
  VALIDATION_EDGE:
    text: VALIDATION_EDGE
    description: Validating entity → entity it validates.
  ACTION_EDGE:
    text: ACTION_EDGE
    description: Action entity with inputs and output entities.
  ADJUDICATION_EDGE:
    text: ADJUDICATION_EDGE
    description: Resolves a set of CONTRADICTION_EDGEs.

```
</details>

</div>