---
search:
  boost: 10.0
---

# Class: ComposedViewpointDirective 


_The frozen result of composing a ViewpointDirective with optional ExtractionProfile, VocabularyPack, and ReasoningPolicy layers. Still a viewpoint-level interpretive contract (and still hashed by the one canonical pipeline), it inlines the resolved operational layers and records the flattened source chains for inspectability. Produced by compose_viewpoint(); not hand-authored._



<div data-search-exclude markdown="1">



URI: [grits:ComposedViewpointDirective](https://w3id.org/grits/ComposedViewpointDirective)





```mermaid
 classDiagram
    class ComposedViewpointDirective
    click ComposedViewpointDirective href "../ComposedViewpointDirective/"
      ViewpointDirective <|-- ComposedViewpointDirective
        click ViewpointDirective href "../ViewpointDirective/"
      
      ComposedViewpointDirective : assumptions
        
      ComposedViewpointDirective : composition_mode
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" CompositionMode : composition_mode
        click CompositionMode href "../CompositionMode/"
    

        
      ComposedViewpointDirective : directive_name
        
      ComposedViewpointDirective : evidence_record_ids
        
      ComposedViewpointDirective : exemplars
        
          
    
        
        
        ComposedViewpointDirective --> "*" ContentReference : exemplars
        click ContentReference href "../ContentReference/"
    

        
      ComposedViewpointDirective : features
        
      ComposedViewpointDirective : generation_mode
        
      ComposedViewpointDirective : id
        
      ComposedViewpointDirective : imposed_should_not_claim
        
      ComposedViewpointDirective : lifecycle_state
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" LifecycleState : lifecycle_state
        click LifecycleState href "../LifecycleState/"
    

        
      ComposedViewpointDirective : methods
        
      ComposedViewpointDirective : observations
        
      ComposedViewpointDirective : operation_link_ids
        
      ComposedViewpointDirective : parent_viewpoint_ids
        
      ComposedViewpointDirective : prompts
        
          
    
        
        
        ComposedViewpointDirective --> "*" ContentReference : prompts
        click ContentReference href "../ContentReference/"
    

        
      ComposedViewpointDirective : provenance
        
      ComposedViewpointDirective : reported_claims
        
      ComposedViewpointDirective : resolved_extraction_profile
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" ExtractionProfile : resolved_extraction_profile
        click ExtractionProfile href "../ExtractionProfile/"
    

        
      ComposedViewpointDirective : resolved_reasoning_policy
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" ReasoningPolicy : resolved_reasoning_policy
        click ReasoningPolicy href "../ReasoningPolicy/"
    

        
      ComposedViewpointDirective : resolved_vocabulary_pack
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" VocabularyPack : resolved_vocabulary_pack
        click VocabularyPack href "../VocabularyPack/"
    

        
      ComposedViewpointDirective : review_state
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" ReviewState : review_state
        click ReviewState href "../ReviewState/"
    

        
      ComposedViewpointDirective : scope
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" Scope : scope
        click Scope href "../Scope/"
    

        
      ComposedViewpointDirective : should_not_claim
        
      ComposedViewpointDirective : source_artifact_refs
        
          
    
        
        
        ComposedViewpointDirective --> "*" ContentReference : source_artifact_refs
        click ContentReference href "../ContentReference/"
    

        
      ComposedViewpointDirective : source_extraction_profile_ids
        
      ComposedViewpointDirective : source_reasoning_policy_ids
        
      ComposedViewpointDirective : source_viewpoint_ids
        
      ComposedViewpointDirective : source_vocabulary_pack_ids
        
      ComposedViewpointDirective : summary
        
      ComposedViewpointDirective : synthesis_link_ids
        
      ComposedViewpointDirective : target_schema
        
          
    
        
        
        ComposedViewpointDirective --> "0..1" ContentReference : target_schema
        click ContentReference href "../ContentReference/"
    

        
      ComposedViewpointDirective : type
        
      ComposedViewpointDirective : uncertainties
        
      ComposedViewpointDirective : unspecified_items
        
      ComposedViewpointDirective : viewpoint_directive_id
        
      ComposedViewpointDirective : vocabulary_refs
        
          
    
        
        
        ComposedViewpointDirective --> "*" ContentReference : vocabulary_refs
        click ContentReference href "../ContentReference/"
    

        
      
```





## Inheritance
* [Grit](Grit.md)
    * [Object](Object.md)
        * [ViewpointDirective](ViewpointDirective.md) [ [Composable](Composable.md)]
            * **ComposedViewpointDirective**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [resolved_extraction_profile](resolved_extraction_profile.md) | 0..1 <br/> [ExtractionProfile](ExtractionProfile.md) | The resolved extraction profile, if one was composed | direct |
| [resolved_vocabulary_pack](resolved_vocabulary_pack.md) | 0..1 <br/> [VocabularyPack](VocabularyPack.md) | The resolved vocabulary pack, if one was composed | direct |
| [resolved_reasoning_policy](resolved_reasoning_policy.md) | 0..1 <br/> [ReasoningPolicy](ReasoningPolicy.md) | The resolved reasoning policy, if one was composed | direct |
| [source_viewpoint_ids](source_viewpoint_ids.md) | * <br/> [GritId](GritId.md) | Flattened, parents-first chain of viewpoint directive ids that were composed | direct |
| [source_extraction_profile_ids](source_extraction_profile_ids.md) | * <br/> [GritId](GritId.md) | Flattened, parents-first chain of extraction profile ids that were composed | direct |
| [source_vocabulary_pack_ids](source_vocabulary_pack_ids.md) | * <br/> [GritId](GritId.md) | Flattened, parents-first chain of vocabulary pack ids that were composed | direct |
| [source_reasoning_policy_ids](source_reasoning_policy_ids.md) | * <br/> [GritId](GritId.md) | Flattened, parents-first chain of reasoning policy ids that were composed | direct |
| [directive_name](directive_name.md) | 1 <br/> [String](String.md) | Human-readable name (e | [ViewpointDirective](ViewpointDirective.md) |
| [parent_viewpoint_ids](parent_viewpoint_ids.md) | * <br/> [GritId](GritId.md) | ViewpointDirective ids this directive composes from, parents-first | [ViewpointDirective](ViewpointDirective.md) |
| [prompts](prompts.md) | * <br/> [ContentReference](ContentReference.md) |  | [ViewpointDirective](ViewpointDirective.md) |
| [exemplars](exemplars.md) | * <br/> [ContentReference](ContentReference.md) |  | [ViewpointDirective](ViewpointDirective.md) |
| [vocabulary_refs](vocabulary_refs.md) | * <br/> [ContentReference](ContentReference.md) |  | [ViewpointDirective](ViewpointDirective.md) |
| [target_schema](target_schema.md) | 0..1 <br/> [ContentReference](ContentReference.md) | Reference to the LinkML schema (or schema profile) this directive commits to | [ViewpointDirective](ViewpointDirective.md) |
| [imposed_should_not_claim](imposed_should_not_claim.md) | * <br/> [String](String.md) | should_not_claim rules this directive imposes on every grit extracted under i... | [ViewpointDirective](ViewpointDirective.md) |
| [composition_mode](composition_mode.md) | 0..1 <br/> [CompositionMode](CompositionMode.md) | How this layer folds against its declared parents during resolution | [Composable](Composable.md) |
| [source_artifact_refs](source_artifact_refs.md) | * <br/> [ContentReference](ContentReference.md) | ContentReferences to the source artifacts this Object derives from | [Object](Object.md) |
| [evidence_record_ids](evidence_record_ids.md) | * <br/> [GritId](GritId.md) | References to EvidenceRecord grits anchoring this Object's claims | [Object](Object.md) |
| [summary](summary.md) | 0..1 <br/> [String](String.md) |  | [Object](Object.md) |
| [features](features.md) | 0..1 <br/> [String](String.md) | Viewpoint-defined structured payload, serialized as a JSON string in v1 | [Object](Object.md) |
| [observations](observations.md) | * <br/> [String](String.md) |  | [Object](Object.md) |
| [unspecified_items](unspecified_items.md) | * <br/> [String](String.md) | Dimensions or claims not bound under the current viewpoint | [Object](Object.md) |
| [reported_claims](reported_claims.md) | * <br/> [String](String.md) |  | [Object](Object.md) |
| [methods](methods.md) | * <br/> [String](String.md) |  | [Object](Object.md) |
| [assumptions](assumptions.md) | * <br/> [String](String.md) |  | [Object](Object.md) |
| [uncertainties](uncertainties.md) | * <br/> [String](String.md) |  | [Object](Object.md) |
| [synthesis_link_ids](synthesis_link_ids.md) | * <br/> [GritId](GritId.md) | Backward pointers to Activities that referenced this Object as input or outpu... | [Object](Object.md) |
| [operation_link_ids](operation_link_ids.md) | * <br/> [GritId](GritId.md) | Backward pointers to ACTION_EDGE Activities involving this Object | [Object](Object.md) |
| [id](id.md) | 1 <br/> [GritId](GritId.md) | Canonical grit identifier | [Grit](Grit.md) |
| [type](type.md) | 1 <br/> [CurieOrUri](CurieOrUri.md) | For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary | [Grit](Grit.md) |
| [viewpoint_directive_id](viewpoint_directive_id.md) | 1 <br/> [GritId](GritId.md) | Reference to the ViewpointDirective that shaped this grit | [Grit](Grit.md) |
| [provenance](provenance.md) | 1 <br/> [String](String.md) | Provenance description for v1 | [Grit](Grit.md) |
| [should_not_claim](should_not_claim.md) | 1..* <br/> [String](String.md) | Epistemic boundaries this grit must respect | [Grit](Grit.md) |
| [scope](scope.md) | 0..1 <br/> [Scope](Scope.md) | Optional but recommended | [Grit](Grit.md) |
| [review_state](review_state.md) | 0..1 <br/> [ReviewState](ReviewState.md) |  | [Grit](Grit.md) |
| [lifecycle_state](lifecycle_state.md) | 0..1 <br/> [LifecycleState](LifecycleState.md) |  | [Grit](Grit.md) |
| [generation_mode](generation_mode.md) | 0..1 <br/> [String](String.md) | Free-form descriptor of the process that generated this grit (parser name + v... | [Grit](Grit.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:ComposedViewpointDirective |
| native | grits:ComposedViewpointDirective |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComposedViewpointDirective
description: The frozen result of composing a ViewpointDirective with optional ExtractionProfile,
  VocabularyPack, and ReasoningPolicy layers. Still a viewpoint-level interpretive
  contract (and still hashed by the one canonical pipeline), it inlines the resolved
  operational layers and records the flattened source chains for inspectability. Produced
  by compose_viewpoint(); not hand-authored.
from_schema: https://w3id.org/grits/core
is_a: ViewpointDirective
attributes:
  resolved_extraction_profile:
    name: resolved_extraction_profile
    description: The resolved extraction profile, if one was composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: ExtractionProfile
    inlined: true
  resolved_vocabulary_pack:
    name: resolved_vocabulary_pack
    description: The resolved vocabulary pack, if one was composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: VocabularyPack
    inlined: true
  resolved_reasoning_policy:
    name: resolved_reasoning_policy
    description: The resolved reasoning policy, if one was composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: ReasoningPolicy
    inlined: true
  source_viewpoint_ids:
    name: source_viewpoint_ids
    description: Flattened, parents-first chain of viewpoint directive ids that were
      composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  source_extraction_profile_ids:
    name: source_extraction_profile_ids
    description: Flattened, parents-first chain of extraction profile ids that were
      composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  source_vocabulary_pack_ids:
    name: source_vocabulary_pack_ids
    description: Flattened, parents-first chain of vocabulary pack ids that were composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  source_reasoning_policy_ids:
    name: source_reasoning_policy_ids
    description: Flattened, parents-first chain of reasoning policy ids that were
      composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ComposedViewpointDirective
description: The frozen result of composing a ViewpointDirective with optional ExtractionProfile,
  VocabularyPack, and ReasoningPolicy layers. Still a viewpoint-level interpretive
  contract (and still hashed by the one canonical pipeline), it inlines the resolved
  operational layers and records the flattened source chains for inspectability. Produced
  by compose_viewpoint(); not hand-authored.
from_schema: https://w3id.org/grits/core
is_a: ViewpointDirective
attributes:
  resolved_extraction_profile:
    name: resolved_extraction_profile
    description: The resolved extraction profile, if one was composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: ExtractionProfile
    inlined: true
  resolved_vocabulary_pack:
    name: resolved_vocabulary_pack
    description: The resolved vocabulary pack, if one was composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: VocabularyPack
    inlined: true
  resolved_reasoning_policy:
    name: resolved_reasoning_policy
    description: The resolved reasoning policy, if one was composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: ReasoningPolicy
    inlined: true
  source_viewpoint_ids:
    name: source_viewpoint_ids
    description: Flattened, parents-first chain of viewpoint directive ids that were
      composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  source_extraction_profile_ids:
    name: source_extraction_profile_ids
    description: Flattened, parents-first chain of extraction profile ids that were
      composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  source_vocabulary_pack_ids:
    name: source_vocabulary_pack_ids
    description: Flattened, parents-first chain of vocabulary pack ids that were composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  source_reasoning_policy_ids:
    name: source_reasoning_policy_ids
    description: Flattened, parents-first chain of reasoning policy ids that were
      composed.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ComposedViewpointDirective
    range: GritId
    multivalued: true
  directive_name:
    name: directive_name
    description: Human-readable name (e.g. viewpoint:materials_science:v1). Combined
      with content hash, this gives identity-by-declaration.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    range: string
    required: true
  parent_viewpoint_ids:
    name: parent_viewpoint_ids
    description: ViewpointDirective ids this directive composes from, parents-first.
      Resolution is explicit (the caller supplies the registry); there is no implicit
      runtime parent lookup.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    range: GritId
    multivalued: true
  prompts:
    name: prompts
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    range: ContentReference
    multivalued: true
    inlined: true
    inlined_as_list: true
  exemplars:
    name: exemplars
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    range: ContentReference
    multivalued: true
    inlined: true
    inlined_as_list: true
  vocabulary_refs:
    name: vocabulary_refs
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    - VocabularyPack
    range: ContentReference
    multivalued: true
    inlined: true
    inlined_as_list: true
  target_schema:
    name: target_schema
    description: Reference to the LinkML schema (or schema profile) this directive
      commits to.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    range: ContentReference
    inlined: true
  imposed_should_not_claim:
    name: imposed_should_not_claim
    description: should_not_claim rules this directive imposes on every grit extracted
      under it. Combined with per-class defaults at extraction time.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - ViewpointDirective
    range: string
    multivalued: true
  composition_mode:
    name: composition_mode
    description: How this layer folds against its declared parents during resolution.
      Defaults to additive.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    ifabsent: string(additive)
    owner: ComposedViewpointDirective
    domain_of:
    - Composable
    range: CompositionMode
  source_artifact_refs:
    name: source_artifact_refs
    description: ContentReferences to the source artifacts this Object derives from.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: ContentReference
    multivalued: true
    inlined: true
    inlined_as_list: true
  evidence_record_ids:
    name: evidence_record_ids
    description: References to EvidenceRecord grits anchoring this Object's claims.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: GritId
    multivalued: true
  summary:
    name: summary
    in_subset:
    - ExtendedProfile
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
  features:
    name: features
    description: Viewpoint-defined structured payload, serialized as a JSON string
      in v1. The viewpoint's vocabulary determines the shape. Later versions may use
      a typed Any with viewpoint-declared schemas.
    in_subset:
    - ExtendedProfile
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
  observations:
    name: observations
    in_subset:
    - ExtendedProfile
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
    multivalued: true
  unspecified_items:
    name: unspecified_items
    description: Dimensions or claims not bound under the current viewpoint.
    in_subset:
    - ExtendedProfile
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
    multivalued: true
  reported_claims:
    name: reported_claims
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
    multivalued: true
  methods:
    name: methods
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
    multivalued: true
  assumptions:
    name: assumptions
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    owner: ComposedViewpointDirective
    domain_of:
    - CompatibilityJudgment
    - Object
    - Activity
    range: string
    multivalued: true
  uncertainties:
    name: uncertainties
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: string
    multivalued: true
  synthesis_link_ids:
    name: synthesis_link_ids
    description: Backward pointers to Activities that referenced this Object as input
      or output.
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: GritId
    multivalued: true
  operation_link_ids:
    name: operation_link_ids
    description: Backward pointers to ACTION_EDGE Activities involving this Object.
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Object
    range: GritId
    multivalued: true
  id:
    name: id
    description: Canonical grit identifier.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    identifier: true
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: GritId
    required: true
  type:
    name: type
    description: For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary.
      For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: CurieOrUri
    required: true
  viewpoint_directive_id:
    name: viewpoint_directive_id
    description: Reference to the ViewpointDirective that shaped this grit. The bootstrap
      meta-viewpoint and the blank-slate viewpoint are valid references; absence is
      not.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    owner: ComposedViewpointDirective
    domain_of:
    - Confidence
    - CompatibilityJudgment
    - Grit
    range: GritId
    required: true
  provenance:
    name: provenance
    description: Provenance description for v1. Future versions will model provenance
      as structured edges into the hyperDAG; for now a free-form string is accepted
      to allow ingestion bundles from upstream extraction tools.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: string
    required: true
  should_not_claim:
    name: should_not_claim
    description: Epistemic boundaries this grit must respect. Combination of per-class
      defaults plus directive-imposed rules from the viewpoint.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: string
    required: true
    multivalued: true
  scope:
    name: scope
    description: Optional but recommended. Viewpoint-supplied scope dimensions describing
      the conditions under which this grit's statements apply. The core Scope marker
      carries no domain dimensions; load a viewpoint schema to populate them.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: Scope
    inlined: true
  review_state:
    name: review_state
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: ReviewState
  lifecycle_state:
    name: lifecycle_state
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: LifecycleState
  generation_mode:
    name: generation_mode
    description: Free-form descriptor of the process that generated this grit (parser
      name + version, viewpoint name + version, LLM model + tier).
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ComposedViewpointDirective
    domain_of:
    - Grit
    range: string

```
</details></div>