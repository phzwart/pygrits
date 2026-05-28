---
search:
  boost: 10.0
---

# Class: NegativeEvidenceRecord 


_First-class record of a search that returned no result under stated scope. Distinct from `unknown` (question not considered) and from `not_searched` (in scope but not attempted)._



<div data-search-exclude markdown="1">



URI: [grits:NegativeEvidenceRecord](https://w3id.org/grits/NegativeEvidenceRecord)





```mermaid
 classDiagram
    class NegativeEvidenceRecord
    click NegativeEvidenceRecord href "../NegativeEvidenceRecord/"
      EvidenceRecord <|-- NegativeEvidenceRecord
        click EvidenceRecord href "../EvidenceRecord/"
      
      NegativeEvidenceRecord : cited_from
        
      NegativeEvidenceRecord : evidence_type
        
      NegativeEvidenceRecord : extracted_content
        
      NegativeEvidenceRecord : extraction_confidence
        
          
    
        
        
        NegativeEvidenceRecord --> "0..1" Confidence : extraction_confidence
        click Confidence href "../Confidence/"
    

        
      NegativeEvidenceRecord : extraction_method
        
      NegativeEvidenceRecord : generation_mode
        
      NegativeEvidenceRecord : id
        
      NegativeEvidenceRecord : lifecycle_state
        
          
    
        
        
        NegativeEvidenceRecord --> "0..1" LifecycleState : lifecycle_state
        click LifecycleState href "../LifecycleState/"
    

        
      NegativeEvidenceRecord : lineage
        
          
    
        
        
        NegativeEvidenceRecord --> "0..1" LineageType : lineage
        click LineageType href "../LineageType/"
    

        
      NegativeEvidenceRecord : locator
        
          
    
        
        
        NegativeEvidenceRecord --> "1" Locator : locator
        click Locator href "../Locator/"
    

        
      NegativeEvidenceRecord : normalized_payload
        
      NegativeEvidenceRecord : provenance
        
      NegativeEvidenceRecord : result
        
      NegativeEvidenceRecord : review_state
        
          
    
        
        
        NegativeEvidenceRecord --> "0..1" ReviewState : review_state
        click ReviewState href "../ReviewState/"
    

        
      NegativeEvidenceRecord : scope
        
          
    
        
        
        NegativeEvidenceRecord --> "0..1" Scope : scope
        click Scope href "../Scope/"
    

        
      NegativeEvidenceRecord : search_confidence
        
          
    
        
        
        NegativeEvidenceRecord --> "0..1" Confidence : search_confidence
        click Confidence href "../Confidence/"
    

        
      NegativeEvidenceRecord : search_method
        
      NegativeEvidenceRecord : search_scope
        
      NegativeEvidenceRecord : search_timestamp
        
      NegativeEvidenceRecord : should_not_claim
        
      NegativeEvidenceRecord : source_artifact_ref
        
          
    
        
        
        NegativeEvidenceRecord --> "1" ContentReference : source_artifact_ref
        click ContentReference href "../ContentReference/"
    

        
      NegativeEvidenceRecord : type
        
      NegativeEvidenceRecord : viewpoint_directive_id
        
      
```





## Inheritance
* [Grit](Grit.md)
    * [EvidenceRecord](EvidenceRecord.md)
        * **NegativeEvidenceRecord**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [search_method](search_method.md) | 1 <br/> [String](String.md) |  | direct |
| [search_scope](search_scope.md) | 0..1 <br/> [String](String.md) |  | direct |
| [search_timestamp](search_timestamp.md) | 0..1 <br/> [Iso8601](Iso8601.md) |  | direct |
| [search_confidence](search_confidence.md) | 0..1 <br/> [Confidence](Confidence.md) |  | direct |
| [result](result.md) | 1 <br/> [String](String.md) | One of `absent`, `weak_signal`, `excluded`, `inconclusive` | direct |
| [source_artifact_ref](source_artifact_ref.md) | 1 <br/> [ContentReference](ContentReference.md) | Single source artifact this evidence is extracted from | [EvidenceRecord](EvidenceRecord.md) |
| [locator](locator.md) | 1 <br/> [Locator](Locator.md) |  | [EvidenceRecord](EvidenceRecord.md) |
| [extracted_content](extracted_content.md) | 0..1 <br/> [String](String.md) |  | [EvidenceRecord](EvidenceRecord.md) |
| [normalized_payload](normalized_payload.md) | 0..1 <br/> [String](String.md) | Viewpoint-defined structured payload, serialized as a JSON string in v1 | [EvidenceRecord](EvidenceRecord.md) |
| [evidence_type](evidence_type.md) | 0..1 <br/> [CurieOrUri](CurieOrUri.md) | CURIE identifying the kind of scientific content the locator anchors | [EvidenceRecord](EvidenceRecord.md) |
| [extraction_method](extraction_method.md) | 0..1 <br/> [String](String.md) |  | [EvidenceRecord](EvidenceRecord.md) |
| [extraction_confidence](extraction_confidence.md) | 0..1 <br/> [Confidence](Confidence.md) |  | [EvidenceRecord](EvidenceRecord.md) |
| [lineage](lineage.md) | 0..1 <br/> [LineageType](LineageType.md) |  | [EvidenceRecord](EvidenceRecord.md) |
| [cited_from](cited_from.md) | 0..1 <br/> [String](String.md) | Identifier or marker for prior evidence this record derives from or cites | [EvidenceRecord](EvidenceRecord.md) |
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
| self | grits:NegativeEvidenceRecord |
| native | grits:NegativeEvidenceRecord |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NegativeEvidenceRecord
description: First-class record of a search that returned no result under stated scope.
  Distinct from `unknown` (question not considered) and from `not_searched` (in scope
  but not attempted).
from_schema: https://w3id.org/grits/core
is_a: EvidenceRecord
attributes:
  search_method:
    name: search_method
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - NegativeEvidenceRecord
    range: string
    required: true
  search_scope:
    name: search_scope
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - NegativeEvidenceRecord
    range: string
  search_timestamp:
    name: search_timestamp
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - NegativeEvidenceRecord
    range: Iso8601
  search_confidence:
    name: search_confidence
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - NegativeEvidenceRecord
    range: Confidence
    inlined: true
  result:
    name: result
    description: One of `absent`, `weak_signal`, `excluded`, `inconclusive`.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - NegativeEvidenceRecord
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: NegativeEvidenceRecord
description: First-class record of a search that returned no result under stated scope.
  Distinct from `unknown` (question not considered) and from `not_searched` (in scope
  but not attempted).
from_schema: https://w3id.org/grits/core
is_a: EvidenceRecord
attributes:
  search_method:
    name: search_method
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - NegativeEvidenceRecord
    range: string
    required: true
  search_scope:
    name: search_scope
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - NegativeEvidenceRecord
    range: string
  search_timestamp:
    name: search_timestamp
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - NegativeEvidenceRecord
    range: Iso8601
  search_confidence:
    name: search_confidence
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - NegativeEvidenceRecord
    range: Confidence
    inlined: true
  result:
    name: result
    description: One of `absent`, `weak_signal`, `excluded`, `inconclusive`.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - NegativeEvidenceRecord
    range: string
    required: true
  source_artifact_ref:
    name: source_artifact_ref
    description: Single source artifact this evidence is extracted from.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: ContentReference
    required: true
    inlined: true
  locator:
    name: locator
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: Locator
    required: true
    inlined: true
  extracted_content:
    name: extracted_content
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: string
  normalized_payload:
    name: normalized_payload
    description: Viewpoint-defined structured payload, serialized as a JSON string
      in v1.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: string
  evidence_type:
    name: evidence_type
    description: CURIE identifying the kind of scientific content the locator anchors.
      No core-supplied permissible values; viewpoints supply the evidence-type vocabulary
      they use.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: CurieOrUri
  extraction_method:
    name: extraction_method
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: string
  extraction_confidence:
    name: extraction_confidence
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: Confidence
    inlined: true
  lineage:
    name: lineage
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: LineageType
  cited_from:
    name: cited_from
    description: Identifier or marker for prior evidence this record derives from
      or cites. May be `unknown_external` when citation resolution has not happened.
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - EvidenceRecord
    range: string
  id:
    name: id
    description: Canonical grit identifier.
    in_subset:
    - MVE
    from_schema: https://w3id.org/grits/core
    rank: 1000
    identifier: true
    owner: NegativeEvidenceRecord
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
    owner: NegativeEvidenceRecord
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
    owner: NegativeEvidenceRecord
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
    owner: NegativeEvidenceRecord
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
    owner: NegativeEvidenceRecord
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
    owner: NegativeEvidenceRecord
    domain_of:
    - Grit
    range: Scope
    inlined: true
  review_state:
    name: review_state
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - Grit
    range: ReviewState
  lifecycle_state:
    name: lifecycle_state
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - Grit
    range: LifecycleState
  generation_mode:
    name: generation_mode
    description: Free-form descriptor of the process that generated this grit (parser
      name + version, viewpoint name + version, LLM model + tier).
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: NegativeEvidenceRecord
    domain_of:
    - Grit
    range: string

```
</details></div>