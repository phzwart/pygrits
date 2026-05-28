---
search:
  boost: 10.0
---

# Class: ViewpointDirective 


_The interpretive frame under which grits are extracted. Itself an Object — a ViewpointDirective has its own viewpoint_directive_id (the bootstrap meta-viewpoint, or itself for the meta-viewpoint). Carries prompts, exemplars, vocabulary references, target schema, and the should_not_claim rules it imposes on extracted grits. Composable against parent viewpoint directives. Supported composition modes: additive, restrictive, overriding._



<div data-search-exclude markdown="1">



URI: [grits:ViewpointDirective](https://w3id.org/grits/ViewpointDirective)





```mermaid
 classDiagram
    class ViewpointDirective
    click ViewpointDirective href "../ViewpointDirective/"
      Composable <|-- ViewpointDirective
        click Composable href "../Composable/"
      Object <|-- ViewpointDirective
        click Object href "../Object/"
      

      ViewpointDirective <|-- ComposedViewpointDirective
        click ComposedViewpointDirective href "../ComposedViewpointDirective/"
      

      ViewpointDirective : assumptions
        
      ViewpointDirective : composition_mode
        
          
    
        
        
        ViewpointDirective --> "0..1" CompositionMode : composition_mode
        click CompositionMode href "../CompositionMode/"
    

        
      ViewpointDirective : directive_name
        
      ViewpointDirective : evidence_record_ids
        
      ViewpointDirective : exemplars
        
          
    
        
        
        ViewpointDirective --> "*" ContentReference : exemplars
        click ContentReference href "../ContentReference/"
    

        
      ViewpointDirective : features
        
      ViewpointDirective : generation_mode
        
      ViewpointDirective : id
        
      ViewpointDirective : imposed_should_not_claim
        
      ViewpointDirective : lifecycle_state
        
          
    
        
        
        ViewpointDirective --> "0..1" LifecycleState : lifecycle_state
        click LifecycleState href "../LifecycleState/"
    

        
      ViewpointDirective : methods
        
      ViewpointDirective : observations
        
      ViewpointDirective : operation_link_ids
        
      ViewpointDirective : parent_viewpoint_ids
        
      ViewpointDirective : prompts
        
          
    
        
        
        ViewpointDirective --> "*" ContentReference : prompts
        click ContentReference href "../ContentReference/"
    

        
      ViewpointDirective : provenance
        
      ViewpointDirective : reported_claims
        
      ViewpointDirective : review_state
        
          
    
        
        
        ViewpointDirective --> "0..1" ReviewState : review_state
        click ReviewState href "../ReviewState/"
    

        
      ViewpointDirective : scope
        
          
    
        
        
        ViewpointDirective --> "0..1" Scope : scope
        click Scope href "../Scope/"
    

        
      ViewpointDirective : should_not_claim
        
      ViewpointDirective : source_artifact_refs
        
          
    
        
        
        ViewpointDirective --> "*" ContentReference : source_artifact_refs
        click ContentReference href "../ContentReference/"
    

        
      ViewpointDirective : summary
        
      ViewpointDirective : synthesis_link_ids
        
      ViewpointDirective : target_schema
        
          
    
        
        
        ViewpointDirective --> "0..1" ContentReference : target_schema
        click ContentReference href "../ContentReference/"
    

        
      ViewpointDirective : type
        
      ViewpointDirective : uncertainties
        
      ViewpointDirective : unspecified_items
        
      ViewpointDirective : viewpoint_directive_id
        
      ViewpointDirective : vocabulary_refs
        
          
    
        
        
        ViewpointDirective --> "*" ContentReference : vocabulary_refs
        click ContentReference href "../ContentReference/"
    

        
      
```





## Inheritance
* [Grit](Grit.md)
    * [Object](Object.md)
        * **ViewpointDirective** [ [Composable](Composable.md)]
            * [ComposedViewpointDirective](ComposedViewpointDirective.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [directive_name](directive_name.md) | 1 <br/> [String](String.md) | Human-readable name (e | direct |
| [parent_viewpoint_ids](parent_viewpoint_ids.md) | * <br/> [GritId](GritId.md) | ViewpointDirective ids this directive composes from, parents-first | direct |
| [prompts](prompts.md) | * <br/> [ContentReference](ContentReference.md) |  | direct |
| [exemplars](exemplars.md) | * <br/> [ContentReference](ContentReference.md) |  | direct |
| [vocabulary_refs](vocabulary_refs.md) | * <br/> [ContentReference](ContentReference.md) |  | direct |
| [target_schema](target_schema.md) | 0..1 <br/> [ContentReference](ContentReference.md) | Reference to the LinkML schema (or schema profile) this directive commits to | direct |
| [imposed_should_not_claim](imposed_should_not_claim.md) | * <br/> [String](String.md) | should_not_claim rules this directive imposes on every grit extracted under i... | direct |
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
| self | grits:ViewpointDirective |
| native | grits:ViewpointDirective |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViewpointDirective
description: 'The interpretive frame under which grits are extracted. Itself an Object
  — a ViewpointDirective has its own viewpoint_directive_id (the bootstrap meta-viewpoint,
  or itself for the meta-viewpoint). Carries prompts, exemplars, vocabulary references,
  target schema, and the should_not_claim rules it imposes on extracted grits. Composable
  against parent viewpoint directives. Supported composition modes: additive, restrictive,
  overriding.'
from_schema: https://w3id.org/grits/core
is_a: Object
mixins:
- Composable
attributes:
  directive_name:
    name: directive_name
    description: Human-readable name (e.g. viewpoint:materials_science:v1). Combined
      with content hash, this gives identity-by-declaration.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ViewpointDirective
    required: true
  parent_viewpoint_ids:
    name: parent_viewpoint_ids
    description: ViewpointDirective ids this directive composes from, parents-first.
      Resolution is explicit (the caller supplies the registry); there is no implicit
      runtime parent lookup.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ViewpointDirective
    range: GritId
    multivalued: true
  prompts:
    name: prompts
    from_schema: https://w3id.org/grits/core
    rank: 1000
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
    domain_of:
    - ViewpointDirective
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ViewpointDirective
description: 'The interpretive frame under which grits are extracted. Itself an Object
  — a ViewpointDirective has its own viewpoint_directive_id (the bootstrap meta-viewpoint,
  or itself for the meta-viewpoint). Carries prompts, exemplars, vocabulary references,
  target schema, and the should_not_claim rules it imposes on extracted grits. Composable
  against parent viewpoint directives. Supported composition modes: additive, restrictive,
  overriding.'
from_schema: https://w3id.org/grits/core
is_a: Object
mixins:
- Composable
attributes:
  directive_name:
    name: directive_name
    description: Human-readable name (e.g. viewpoint:materials_science:v1). Combined
      with content hash, this gives identity-by-declaration.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ViewpointDirective
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
    owner: ViewpointDirective
    domain_of:
    - ViewpointDirective
    range: GritId
    multivalued: true
  prompts:
    name: prompts
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
    domain_of:
    - Object
    range: string
  observations:
    name: observations
    in_subset:
    - ExtendedProfile
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
    domain_of:
    - Object
    range: string
    multivalued: true
  assumptions:
    name: assumptions
    in_subset:
    - Full
    from_schema: https://w3id.org/grits/core
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
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
    owner: ViewpointDirective
    domain_of:
    - Grit
    range: Scope
    inlined: true
  review_state:
    name: review_state
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ViewpointDirective
    domain_of:
    - Grit
    range: ReviewState
  lifecycle_state:
    name: lifecycle_state
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ViewpointDirective
    domain_of:
    - Grit
    range: LifecycleState
  generation_mode:
    name: generation_mode
    description: Free-form descriptor of the process that generated this grit (parser
      name + version, viewpoint name + version, LLM model + tier).
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ViewpointDirective
    domain_of:
    - Grit
    range: string

```
</details></div>