---
search:
  boost: 10.0
---

# Class: CompatibilityJudgment 


_A recorded compatibility judgment over a set of grits/evidence._



<div data-search-exclude markdown="1">



URI: [grits:CompatibilityJudgment](https://w3id.org/grits/CompatibilityJudgment)





```mermaid
 classDiagram
    class CompatibilityJudgment
    click CompatibilityJudgment href "../CompatibilityJudgment/"
      CompatibilityJudgment : assumptions
        
      CompatibilityJudgment : checked_scope_dimensions
        
      CompatibilityJudgment : compared_grit_ids
        
      CompatibilityJudgment : rationale
        
      CompatibilityJudgment : status
        
          
    
        
        
        CompatibilityJudgment --> "1" CompatibilityStatus : status
        click CompatibilityStatus href "../CompatibilityStatus/"
    

        
      CompatibilityJudgment : viewpoint_directive_id
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [compared_grit_ids](compared_grit_ids.md) | 1..* <br/> [GritId](GritId.md) |  | direct |
| [checked_scope_dimensions](checked_scope_dimensions.md) | * <br/> [String](String.md) |  | direct |
| [assumptions](assumptions.md) | * <br/> [String](String.md) |  | direct |
| [rationale](rationale.md) | 0..1 <br/> [String](String.md) |  | direct |
| [status](status.md) | 1 <br/> [CompatibilityStatus](CompatibilityStatus.md) |  | direct |
| [viewpoint_directive_id](viewpoint_directive_id.md) | 0..1 <br/> [GritId](GritId.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Activity](Activity.md) | [compatibility_judgments](compatibility_judgments.md) | range | [CompatibilityJudgment](CompatibilityJudgment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:CompatibilityJudgment |
| native | grits:CompatibilityJudgment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompatibilityJudgment
description: A recorded compatibility judgment over a set of grits/evidence.
from_schema: https://w3id.org/grits/core
attributes:
  compared_grit_ids:
    name: compared_grit_ids
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CompatibilityJudgment
    range: GritId
    required: true
    multivalued: true
  checked_scope_dimensions:
    name: checked_scope_dimensions
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CompatibilityJudgment
    range: string
    multivalued: true
  assumptions:
    name: assumptions
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CompatibilityJudgment
    - Object
    - Activity
    range: string
    multivalued: true
  rationale:
    name: rationale
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CompatibilityJudgment
    range: string
  status:
    name: status
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CompatibilityJudgment
    range: CompatibilityStatus
    required: true
  viewpoint_directive_id:
    name: viewpoint_directive_id
    from_schema: https://w3id.org/grits/core
    domain_of:
    - Confidence
    - CompatibilityJudgment
    - Grit
    range: GritId

```
</details>

### Induced

<details>
```yaml
name: CompatibilityJudgment
description: A recorded compatibility judgment over a set of grits/evidence.
from_schema: https://w3id.org/grits/core
attributes:
  compared_grit_ids:
    name: compared_grit_ids
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CompatibilityJudgment
    domain_of:
    - CompatibilityJudgment
    range: GritId
    required: true
    multivalued: true
  checked_scope_dimensions:
    name: checked_scope_dimensions
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CompatibilityJudgment
    domain_of:
    - CompatibilityJudgment
    range: string
    multivalued: true
  assumptions:
    name: assumptions
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CompatibilityJudgment
    domain_of:
    - CompatibilityJudgment
    - Object
    - Activity
    range: string
    multivalued: true
  rationale:
    name: rationale
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CompatibilityJudgment
    domain_of:
    - CompatibilityJudgment
    range: string
  status:
    name: status
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CompatibilityJudgment
    domain_of:
    - CompatibilityJudgment
    range: CompatibilityStatus
    required: true
  viewpoint_directive_id:
    name: viewpoint_directive_id
    from_schema: https://w3id.org/grits/core
    owner: CompatibilityJudgment
    domain_of:
    - Confidence
    - CompatibilityJudgment
    - Grit
    range: GritId

```
</details></div>