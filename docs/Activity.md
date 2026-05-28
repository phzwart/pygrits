---
search:
  boost: 10.0
---

# Class: Activity 


_Transformation. Consumes input entities, applies an interpretation under stated assumptions, emits output entities. Hyperedge in the hyperDAG topology. Activities do not participate in conversations — they record how a step of reasoning happened._



<div data-search-exclude markdown="1">



URI: [prov:Activity](http://www.w3.org/ns/prov#Activity)





```mermaid
 classDiagram
    class Activity
    click Activity href "../Activity/"
      Entity <|-- Activity
        click Entity href "../Entity/"
      
      Activity : activity_type
        
          
    
        
        
        Activity --> "1" ActivityType : activity_type
        click ActivityType href "../ActivityType/"
    

        
      Activity : admissibility_rationale
        
      Activity : assumptions
        
      Activity : compatibility_judgments
        
          
    
        
        
        Activity --> "*" CompatibilityJudgment : compatibility_judgments
        click CompatibilityJudgment href "../CompatibilityJudgment/"
    

        
      Activity : confidence
        
          
    
        
        
        Activity --> "0..1" Confidence : confidence
        click Confidence href "../Confidence/"
    

        
      Activity : generation_mode
        
      Activity : id
        
      Activity : inputs
        
      Activity : lifecycle_state
        
          
    
        
        
        Activity --> "0..1" LifecycleState : lifecycle_state
        click LifecycleState href "../LifecycleState/"
    

        
      Activity : outputs
        
      Activity : provenance
        
      Activity : review_state
        
          
    
        
        
        Activity --> "0..1" ReviewState : review_state
        click ReviewState href "../ReviewState/"
    

        
      Activity : scope
        
          
    
        
        
        Activity --> "0..1" Scope : scope
        click Scope href "../Scope/"
    

        
      Activity : should_not_claim
        
      Activity : type
        
      Activity : viewpoint_directive_id
        
      
```





## Inheritance
* [Entity](Entity.md)
    * **Activity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [prov:Activity](http://www.w3.org/ns/prov#Activity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [activity_type](activity_type.md) | 1 <br/> [ActivityType](ActivityType.md) |  | direct |
| [inputs](inputs.md) | 1..* <br/> [EntityId](EntityId.md) | Input entity IDs consumed by this Activity | direct |
| [outputs](outputs.md) | * <br/> [EntityId](EntityId.md) | New entities produced by this Activity | direct |
| [assumptions](assumptions.md) | * <br/> [String](String.md) |  | direct |
| [admissibility_rationale](admissibility_rationale.md) | 0..1 <br/> [String](String.md) | Why this Activity is valid given its inputs and viewpoint | direct |
| [compatibility_judgments](compatibility_judgments.md) | * <br/> [CompatibilityJudgment](CompatibilityJudgment.md) |  | direct |
| [confidence](confidence.md) | 0..1 <br/> [Confidence](Confidence.md) |  | direct |
| [id](id.md) | 1 <br/> [EntityId](EntityId.md) | Canonical entity identifier | [Entity](Entity.md) |
| [type](type.md) | 1 <br/> [CurieOrUri](CurieOrUri.md) | For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary | [Entity](Entity.md) |
| [viewpoint_directive_id](viewpoint_directive_id.md) | 1 <br/> [EntityId](EntityId.md) | Reference to the ViewpointDirective that shaped this entity | [Entity](Entity.md) |
| [provenance](provenance.md) | 1 <br/> [String](String.md) | Provenance description for v1 | [Entity](Entity.md) |
| [should_not_claim](should_not_claim.md) | 1..* <br/> [String](String.md) | Epistemic boundaries this entity must respect | [Entity](Entity.md) |
| [scope](scope.md) | 0..1 <br/> [Scope](Scope.md) | Optional but recommended | [Entity](Entity.md) |
| [review_state](review_state.md) | 0..1 <br/> [ReviewState](ReviewState.md) |  | [Entity](Entity.md) |
| [lifecycle_state](lifecycle_state.md) | 0..1 <br/> [LifecycleState](LifecycleState.md) |  | [Entity](Entity.md) |
| [generation_mode](generation_mode.md) | 0..1 <br/> [String](String.md) | Free-form descriptor of the process that generated this entity (parser name +... | [Entity](Entity.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Activity |
| native | isom:Activity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Activity
description: Transformation. Consumes input entities, applies an interpretation under
  stated assumptions, emits output entities. Hyperedge in the hyperDAG topology. Activities
  do not participate in conversations — they record how a step of reasoning happened.
from_schema: https://w3id.org/isom/core
is_a: Entity
attributes:
  activity_type:
    name: activity_type
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - Activity
    range: ActivityType
    required: true
  inputs:
    name: inputs
    description: Input entity IDs consumed by this Activity.
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - Activity
    range: EntityId
    required: true
    multivalued: true
  outputs:
    name: outputs
    description: New entities produced by this Activity. May be empty for declarative
      edges (SUPPORT, CONTRADICTION) whose output is the Activity itself.
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - Activity
    range: EntityId
    multivalued: true
  assumptions:
    name: assumptions
    from_schema: https://w3id.org/isom/core
    domain_of:
    - CompatibilityJudgment
    - Object
    - Activity
    range: string
    multivalued: true
  admissibility_rationale:
    name: admissibility_rationale
    description: Why this Activity is valid given its inputs and viewpoint.
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - Activity
    range: string
  compatibility_judgments:
    name: compatibility_judgments
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - Activity
    range: CompatibilityJudgment
    multivalued: true
    inlined: true
    inlined_as_list: true
  confidence:
    name: confidence
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - Activity
    range: Confidence
    inlined: true
class_uri: prov:Activity

```
</details>

### Induced

<details>
```yaml
name: Activity
description: Transformation. Consumes input entities, applies an interpretation under
  stated assumptions, emits output entities. Hyperedge in the hyperDAG topology. Activities
  do not participate in conversations — they record how a step of reasoning happened.
from_schema: https://w3id.org/isom/core
is_a: Entity
attributes:
  activity_type:
    name: activity_type
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Activity
    range: ActivityType
    required: true
  inputs:
    name: inputs
    description: Input entity IDs consumed by this Activity.
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Activity
    range: EntityId
    required: true
    multivalued: true
  outputs:
    name: outputs
    description: New entities produced by this Activity. May be empty for declarative
      edges (SUPPORT, CONTRADICTION) whose output is the Activity itself.
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Activity
    range: EntityId
    multivalued: true
  assumptions:
    name: assumptions
    from_schema: https://w3id.org/isom/core
    owner: Activity
    domain_of:
    - CompatibilityJudgment
    - Object
    - Activity
    range: string
    multivalued: true
  admissibility_rationale:
    name: admissibility_rationale
    description: Why this Activity is valid given its inputs and viewpoint.
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Activity
    range: string
  compatibility_judgments:
    name: compatibility_judgments
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Activity
    range: CompatibilityJudgment
    multivalued: true
    inlined: true
    inlined_as_list: true
  confidence:
    name: confidence
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Activity
    range: Confidence
    inlined: true
  id:
    name: id
    description: Canonical entity identifier.
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    identifier: true
    owner: Activity
    domain_of:
    - Entity
    range: EntityId
    required: true
  type:
    name: type
    description: For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary.
      For Activity, a CURIE corresponding to the ActivityType value (e.g. isom:activity_type/synthesis_edge).
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: CurieOrUri
    required: true
  viewpoint_directive_id:
    name: viewpoint_directive_id
    description: Reference to the ViewpointDirective that shaped this entity. The
      bootstrap meta-viewpoint and the blank-slate viewpoint are valid references;
      absence is not.
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    owner: Activity
    domain_of:
    - Confidence
    - CompatibilityJudgment
    - Entity
    range: EntityId
    required: true
  provenance:
    name: provenance
    description: Provenance description for v1. Future versions will model provenance
      as structured edges into the hyperDAG; for now a free-form string is accepted
      to allow ingestion bundles from upstream extraction tools.
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: string
    required: true
  should_not_claim:
    name: should_not_claim
    description: Epistemic boundaries this entity must respect. Combination of per-class
      defaults plus directive-imposed rules from the viewpoint.
    in_subset:
    - MVE
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: string
    required: true
    multivalued: true
  scope:
    name: scope
    description: Optional but recommended. Viewpoint-supplied scope dimensions describing
      the conditions under which this entity's statements apply. The core Scope marker
      carries no domain dimensions; load a viewpoint schema to populate them.
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: Scope
    inlined: true
  review_state:
    name: review_state
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: ReviewState
  lifecycle_state:
    name: lifecycle_state
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: LifecycleState
  generation_mode:
    name: generation_mode
    description: Free-form descriptor of the process that generated this entity (parser
      name + version, viewpoint name + version, LLM model + tier).
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: Activity
    domain_of:
    - Entity
    range: string
class_uri: prov:Activity

```
</details></div>