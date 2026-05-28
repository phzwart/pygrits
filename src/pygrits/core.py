from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "0.3.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'grits',
     'default_range': 'string',
     'description': 'Core schema for pygrits. Defines Grit role classes (Object, '
                    'Activity, EvidenceRecord), ViewpointDirective, and structural '
                    'primitives (ContentReference, opaque Scope marker, Locator '
                    'hierarchy, structured Confidence). All grits share the '
                    'discipline contract (identity, type, viewpoint, provenance, '
                    'should_not_claim) and differ by role. Domain vocabulary is '
                    'supplied by viewpoint schemas that import or extend this '
                    'core.',
     'id': 'https://w3id.org/grits/core',
     'imports': ['linkml:types'],
     'license': 'TBD',
     'name': 'pygrits_core',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'grits': {'prefix_prefix': 'grits',
                            'prefix_reference': 'https://w3id.org/grits/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/pygrits/core.yaml',
     'subsets': {'ExtendedProfile': {'description': 'Object fields for extended '
                                                    'descriptive payload (summary, '
                                                    'features, observations, '
                                                    'unspecified_items).',
                                     'from_schema': 'https://w3id.org/grits/core',
                                     'name': 'ExtendedProfile'},
                 'Full': {'description': 'Full object surface including '
                                         'reported_claims, methods, assumptions, '
                                         'uncertainties, and backward-pointer link '
                                         'lists (synthesis_link_ids, '
                                         'operation_link_ids).',
                          'from_schema': 'https://w3id.org/grits/core',
                          'name': 'Full'},
                 'MVE': {'description': 'Minimum viable grit. The irreducible '
                                        'discipline contract fields plus the '
                                        'class-specific minimum required for '
                                        'validation. Instances missing any '
                                        'MVE-tagged required slot fail validation.',
                         'from_schema': 'https://w3id.org/grits/core',
                         'name': 'MVE'}},
     'title': 'pygrits Core Schema',
     'types': {'CurieOrUri': {'base': 'str',
                              'description': 'A CURIE or URI identifying a '
                                             'vocabulary term.',
                              'from_schema': 'https://w3id.org/grits/core',
                              'name': 'CurieOrUri',
                              'uri': 'xsd:anyURI'},
               'GritId': {'base': 'str',
                          'description': 'Canonical grit identifier of the form '
                                         'scheme:value, where scheme is one of '
                                         'obj, act, evi, vpt, src. Hash-derived '
                                         'where applicable. Identity is by '
                                         'declaration plus content hash (for '
                                         'ContentReference-bearing grits like '
                                         'ViewpointDirective).',
                          'from_schema': 'https://w3id.org/grits/core',
                          'name': 'GritId',
                          'pattern': '^[a-z]+:[A-Za-z0-9._:-]+$',
                          'uri': 'xsd:string'},
               'Iso8601': {'base': 'str',
                           'description': 'ISO 8601 datetime string.',
                           'from_schema': 'https://w3id.org/grits/core',
                           'name': 'Iso8601',
                           'uri': 'xsd:dateTime'},
               'Sha256Hex': {'base': 'str',
                             'description': 'Hex-encoded SHA-256, lowercase, 64 '
                                            'chars.',
                             'from_schema': 'https://w3id.org/grits/core',
                             'name': 'Sha256Hex',
                             'pattern': '^[a-f0-9]{64}$',
                             'uri': 'xsd:string'}}} )

class HashMode(str, Enum):
    """
    How a ContentReference's sha256 is computed.
    """
    raw_bytes = "raw_bytes"
    """
    SHA-256 of the file bytes as stored.
    """
    linkml_canonical_jcs = "linkml_canonical_jcs"
    """
    LinkML normalize → JSON via LinkML mapping → RFC 8785 JCS → SHA-256.
    """


class ActivityType(str, Enum):
    """
    Structural type of an Activity (hyperedge in the topology).
    """
    SYNTHESIS_EDGE = "SYNTHESIS_EDGE"
    """
    Inputs + assumptions → new synthesis grit.
    """
    SUPPORT_EDGE = "SUPPORT_EDGE"
    """
    Evidence → claim/synthesis it supports.
    """
    CONTRADICTION_EDGE = "CONTRADICTION_EDGE"
    """
    Evidence → claim/synthesis it contradicts.
    """
    COMPATIBILITY_EDGE = "COMPATIBILITY_EDGE"
    """
    Records a compatibility judgment over grits.
    """
    VALIDATION_EDGE = "VALIDATION_EDGE"
    """
    Validating grit → grit it validates.
    """
    ACTION_EDGE = "ACTION_EDGE"
    """
    Operation grit with inputs and output grits.
    """
    ADJUDICATION_EDGE = "ADJUDICATION_EDGE"
    """
    Resolves a set of CONTRADICTION_EDGEs.
    """


class LifecycleState(str, Enum):
    """
    Lifecycle state of a grit.
    """
    ingested = "ingested"
    parsed = "parsed"
    evidence_extracted = "evidence_extracted"
    interaction_ready = "interaction_ready"
    active = "active"
    synthesized = "synthesized"
    deprecated = "deprecated"
    superseded = "superseded"
    retracted = "retracted"


class ReviewState(str, Enum):
    """
    Epistemic maturity of a derived grit.
    """
    unreviewed = "unreviewed"
    machine_generated = "machine_generated"
    curator_reviewed = "curator_reviewed"
    experimentally_validated = "experimentally_validated"
    disputed = "disputed"
    deprecated = "deprecated"


class EpistemicStatus(str, Enum):
    """
    Epistemic label on a consequential statement.
    """
    direct_evidence = "direct_evidence"
    reported_by_source = "reported_by_source"
    extracted = "extracted"
    computed = "computed"
    inferred = "inferred"
    synthesized = "synthesized"
    speculative = "speculative"
    negative_evidence = "negative_evidence"
    out_of_viewpoint = "out_of_viewpoint"
    action_proposal = "action_proposal"
    contradicted = "contradicted"
    unresolved = "unresolved"
    deprecated = "deprecated"
    unknown = "unknown"


class LineageType(str, Enum):
    """
    Independence classification of an evidence record.
    """
    independent = "independent"
    derived = "derived"
    duplicated = "duplicated"
    cited = "cited"
    computational = "computational"


class RefusalState(str, Enum):
    """
    Five-state refusal taxonomy. Distinct from EpistemicStatus — RefusalState answers "did we look, and what did we find?", EpistemicStatus answers "what kind of statement is this?".
    """
    unknown = "unknown"
    """
    Question not considered.
    """
    not_searched = "not_searched"
    """
    Question in scope, but retrieval not attempted.
    """
    searched_absent = "searched_absent"
    """
    Retrieval attempted under stated scope and value absent.
    """
    out_of_viewpoint = "out_of_viewpoint"
    """
    Question may be answerable but the extracting viewpoint did not commit to it. Proposes viewpoint extension as next action.
    """
    contradicted = "contradicted"
    """
    Answer was found but is refuted by other evidence; no current usable answer until adjudication.
    """


class CompatibilityStatus(str, Enum):
    """
    Outcome of a compatibility judgment.
    """
    compatible = "compatible"
    conditionally_compatible = "conditionally_compatible"
    incompatible = "incompatible"
    unknown = "unknown"


class ConfidenceBasis(str, Enum):
    """
    Source semantics of a confidence value.
    """
    parser_self_report = "parser_self_report"
    """
    Vendor-provided model self-report; typically uncalibrated.
    """
    conformal = "conformal"
    """
    PAC coverage under exchangeability; calibrated to operational rate.
    """
    bayesian = "bayesian"
    """
    Posterior-derived; calibrated under priors and model assumptions.
    """
    heuristic = "heuristic"
    """
    Ad hoc; basis must be documented in calibration_scope.
    """
    aggregated = "aggregated"
    """
    Combined over heterogeneous evidence; combination method must be declared.
    """



class ContentReference(ConfiguredBaseModel):
    """
    Content-addressed reference to externally stored content. Identity by uri + sha256 + hash_mode. At resolution time, the system fetches uri, recomputes the hash under hash_mode, and refuses to use the content if the hash does not match.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    uri: str = Field(default=..., description="""Locator (file path, https URL, did:..., cid:...).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })
    sha256: str = Field(default=..., description="""Integrity check on the content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })
    hash_mode: HashMode = Field(default=..., description="""How the sha256 was computed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })
    media_type: Optional[str] = Field(default=None, description="""MIME type for disambiguation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })
    retrieved_at: Optional[str] = Field(default=None, description="""Last successful integrity verification timestamp.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })

    @field_validator('sha256')
    def pattern_sha256(cls, v):
        pattern=re.compile(r"^[a-f0-9]{64}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sha256 format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sha256 format: {v}"
            raise ValueError(err_msg)
        return v


class Scope(ConfiguredBaseModel):
    """
    Container for viewpoint-supplied scope dimensions. The core defines no domain dimensions. Viewpoints subclass Scope in their own LinkML schemas to declare the scope commitments they populate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/grits/core'})

    scope_type: Literal["Scope"] = Field(default="Scope", description="""Class name of the concrete Scope subclass (e.g. NotesOnlyScope).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Scope']} })
    notes: Optional[str] = Field(default=None, description="""Free-text scope clarification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Scope']} })


class NotesOnlyScope(Scope):
    """
    Scope marker with only free-form notes; no domain dimensions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    scope_type: Literal["NotesOnlyScope"] = Field(default="NotesOnlyScope", description="""Class name of the concrete Scope subclass (e.g. NotesOnlyScope).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Scope']} })
    notes: Optional[str] = Field(default=None, description="""Free-text scope clarification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Scope']} })


class Locator(ConfiguredBaseModel):
    """
    Polymorphic locator into a source artifact. Describes HOW an anchor into a source artifact is shaped (character range, bounding box, sequence position, etc.), not WHAT kind of content the source contains. Discriminator is locator_type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/grits/core'})

    locator_type: Literal["Locator"] = Field(default="Locator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class CharRangeLocator(Locator):
    """
    Character range within extracted text of a source artifact.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    char_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator']} })
    char_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator']} })
    page: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator', 'BboxLocator']} })
    locator_type: Literal["CharRangeLocator"] = Field(default="CharRangeLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class BboxLocator(Locator):
    """
    Axis-aligned bounding box on a rasterized page.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    page: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator', 'BboxLocator']} })
    bbox_x0: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    bbox_y0: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    bbox_x1: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    bbox_y1: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    locator_type: Literal["BboxLocator"] = Field(default="BboxLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class SequencePositionLocator(Locator):
    """
    Position range within a reference sequence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    reference_sequence_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SequencePositionLocator']} })
    seq_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SequencePositionLocator']} })
    seq_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SequencePositionLocator']} })
    locator_type: Literal["SequencePositionLocator"] = Field(default="SequencePositionLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class ProcessingLogLineLocator(Locator):
    """
    Line range within a processing log.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    log_line_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ProcessingLogLineLocator']} })
    log_line_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ProcessingLogLineLocator']} })
    locator_type: Literal["ProcessingLogLineLocator"] = Field(default="ProcessingLogLineLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class TableCellLocator(Locator):
    """
    A specific cell within an extracted table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    table_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TableCellLocator']} })
    row: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TableCellLocator']} })
    col: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TableCellLocator']} })
    locator_type: Literal["TableCellLocator"] = Field(default="TableCellLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class FileRegionLocator(Locator):
    """
    Byte range within an opaque binary artifact.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    byte_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FileRegionLocator']} })
    byte_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FileRegionLocator']} })
    locator_type: Literal["FileRegionLocator"] = Field(default="FileRegionLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class CompositeLocator(Locator):
    """
    A locator that combines multiple sub-locators.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    members: Optional[list[Union[Locator,CharRangeLocator,BboxLocator,SequencePositionLocator,ProcessingLogLineLocator,TableCellLocator,FileRegionLocator,CompositeLocator]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompositeLocator']} })
    locator_type: Literal["CompositeLocator"] = Field(default="CompositeLocator", description="""Class name of the concrete Locator subclass (e.g. CharRangeLocator).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class Confidence(ConfiguredBaseModel):
    """
    Structured confidence carrying calibration metadata. A calibrated confidence outside its calibration_domain or under a different viewpoint is no longer calibrated — downstream consumers must downgrade to heuristic.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    value: Optional[float] = Field(default=None, description="""Numeric confidence; semantics depend on confidence_basis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    confidence_basis: ConfidenceBasis = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    calibration_scope: Optional[str] = Field(default=None, description="""The data distribution under which the confidence was calibrated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    confidence_domain: Optional[str] = Field(default=None, description="""The input domain where the calibration applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    failure_modes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    viewpoint_directive_id: Optional[str] = Field(default=None, description="""Viewpoint under which calibration was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit']} })


class CompatibilityJudgment(ConfiguredBaseModel):
    """
    A recorded compatibility judgment over a set of grits/evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    compared_grit_ids: list[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment']} })
    checked_scope_dimensions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment']} })
    assumptions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment', 'Object', 'Activity']} })
    rationale: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment']} })
    status: CompatibilityStatus = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment']} })
    viewpoint_directive_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit']} })


class Grit(ConfiguredBaseModel):
    """
    Abstract base for all pygrits graph nodes. Carries the discipline contract: identity, type, viewpoint, provenance, lifecycle, review state, should_not_claim, scope, generation mode. Three concrete role subclasses: Object, Activity, EvidenceRecord.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'prov:Entity',
         'from_schema': 'https://w3id.org/grits/core'})

    id: str = Field(default=..., description="""Canonical grit identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    type: str = Field(default=..., description="""For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    viewpoint_directive_id: str = Field(default=..., description="""Reference to the ViewpointDirective that shaped this grit. The bootstrap meta-viewpoint and the blank-slate viewpoint are valid references; absence is not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit'],
         'in_subset': ['MVE']} })
    provenance: str = Field(default=..., description="""Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    should_not_claim: list[str] = Field(default=..., description="""Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    scope: Optional[Union[Scope,NotesOnlyScope]] = Field(default=None, description="""Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this grit's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    review_state: Optional[ReviewState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    lifecycle_state: Optional[LifecycleState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generation_mode: Optional[str] = Field(default=None, description="""Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class Object(Grit):
    """
    Subject node. Holds source artifact refs, evidence refs, and descriptive payload slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    source_artifact_refs: Optional[list[ContentReference]] = Field(default=None, description="""ContentReferences to the source artifacts this Object derives from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['MVE']} })
    evidence_record_ids: Optional[list[str]] = Field(default=None, description="""References to EvidenceRecord grits anchoring this Object's claims.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['MVE']} })
    summary: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    features: Optional[str] = Field(default=None, description="""Viewpoint-defined structured payload, serialized as a JSON string in v1. The viewpoint's vocabulary determines the shape. Later versions may use a typed Any with viewpoint-declared schemas.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    observations: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    unspecified_items: Optional[list[str]] = Field(default=None, description="""Dimensions or claims not bound under the current viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    reported_claims: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    methods: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    assumptions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment', 'Object', 'Activity'],
         'in_subset': ['Full']} })
    uncertainties: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    synthesis_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to Activities that referenced this Object as input or output.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    operation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to ACTION_EDGE Activities involving this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    id: str = Field(default=..., description="""Canonical grit identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    type: str = Field(default=..., description="""For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    viewpoint_directive_id: str = Field(default=..., description="""Reference to the ViewpointDirective that shaped this grit. The bootstrap meta-viewpoint and the blank-slate viewpoint are valid references; absence is not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit'],
         'in_subset': ['MVE']} })
    provenance: str = Field(default=..., description="""Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    should_not_claim: list[str] = Field(default=..., description="""Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    scope: Optional[Union[Scope,NotesOnlyScope]] = Field(default=None, description="""Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this grit's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    review_state: Optional[ReviewState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    lifecycle_state: Optional[LifecycleState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generation_mode: Optional[str] = Field(default=None, description="""Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class Activity(Grit):
    """
    Hyperedge. Consumes input grits, applies an interpretation under stated assumptions, emits output grits. Records a transform step in the hyperDAG topology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity', 'from_schema': 'https://w3id.org/grits/core'})

    activity_type: ActivityType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'in_subset': ['MVE']} })
    inputs: list[str] = Field(default=..., description="""Input grit IDs consumed by this Activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'in_subset': ['MVE']} })
    outputs: Optional[list[str]] = Field(default=None, description="""New grits produced by this Activity. May be empty for declarative edges (SUPPORT, CONTRADICTION) whose output is the Activity itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    assumptions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment', 'Object', 'Activity']} })
    admissibility_rationale: Optional[str] = Field(default=None, description="""Why this Activity is valid given its inputs and viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    compatibility_judgments: Optional[list[CompatibilityJudgment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    id: str = Field(default=..., description="""Canonical grit identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    type: str = Field(default=..., description="""For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    viewpoint_directive_id: str = Field(default=..., description="""Reference to the ViewpointDirective that shaped this grit. The bootstrap meta-viewpoint and the blank-slate viewpoint are valid references; absence is not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit'],
         'in_subset': ['MVE']} })
    provenance: str = Field(default=..., description="""Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    should_not_claim: list[str] = Field(default=..., description="""Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    scope: Optional[Union[Scope,NotesOnlyScope]] = Field(default=None, description="""Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this grit's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    review_state: Optional[ReviewState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    lifecycle_state: Optional[LifecycleState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generation_mode: Optional[str] = Field(default=None, description="""Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class EvidenceRecord(Grit):
    """
    Anchor unit. Grounded data anchored to a single source artifact via a typed locator. Referenced by Objects' evidence_record_ids and by Activities' inputs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    source_artifact_ref: ContentReference = Field(default=..., description="""Single source artifact this evidence is extracted from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord'], 'in_subset': ['MVE']} })
    locator: Union[Locator,CharRangeLocator,BboxLocator,SequencePositionLocator,ProcessingLogLineLocator,TableCellLocator,FileRegionLocator,CompositeLocator] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord'], 'in_subset': ['MVE']} })
    extracted_content: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    normalized_payload: Optional[str] = Field(default=None, description="""Viewpoint-defined structured payload, serialized as a JSON string in v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    evidence_type: Optional[str] = Field(default=None, description="""CURIE identifying the kind of scientific content the locator anchors. No core-supplied permissible values; viewpoints supply the evidence-type vocabulary they use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extraction_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extraction_confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    lineage: Optional[LineageType] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    cited_from: Optional[str] = Field(default=None, description="""Identifier or marker for prior evidence this record derives from or cites. May be `unknown_external` when citation resolution has not happened.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    id: str = Field(default=..., description="""Canonical grit identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    type: str = Field(default=..., description="""For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    viewpoint_directive_id: str = Field(default=..., description="""Reference to the ViewpointDirective that shaped this grit. The bootstrap meta-viewpoint and the blank-slate viewpoint are valid references; absence is not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit'],
         'in_subset': ['MVE']} })
    provenance: str = Field(default=..., description="""Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    should_not_claim: list[str] = Field(default=..., description="""Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    scope: Optional[Union[Scope,NotesOnlyScope]] = Field(default=None, description="""Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this grit's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    review_state: Optional[ReviewState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    lifecycle_state: Optional[LifecycleState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generation_mode: Optional[str] = Field(default=None, description="""Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class ViewpointDirective(Object):
    """
    The interpretive frame under which grits are extracted. Itself an Object — a ViewpointDirective has its own viewpoint_directive_id (the bootstrap meta-viewpoint, or itself for the meta-viewpoint). Carries prompts, exemplars, vocabulary references, target schema, and the should_not_claim rules it imposes on extracted grits.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    directive_name: str = Field(default=..., description="""Human-readable name (e.g. viewpoint:materials_science:v1). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    prompts: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    exemplars: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    vocabulary_refs: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    target_schema: Optional[ContentReference] = Field(default=None, description="""Reference to the LinkML schema (or schema profile) this directive commits to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    imposed_should_not_claim: Optional[list[str]] = Field(default=None, description="""should_not_claim rules this directive imposes on every grit extracted under it. Combined with per-class defaults at extraction time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    source_artifact_refs: Optional[list[ContentReference]] = Field(default=None, description="""ContentReferences to the source artifacts this Object derives from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['MVE']} })
    evidence_record_ids: Optional[list[str]] = Field(default=None, description="""References to EvidenceRecord grits anchoring this Object's claims.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['MVE']} })
    summary: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    features: Optional[str] = Field(default=None, description="""Viewpoint-defined structured payload, serialized as a JSON string in v1. The viewpoint's vocabulary determines the shape. Later versions may use a typed Any with viewpoint-declared schemas.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    observations: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    unspecified_items: Optional[list[str]] = Field(default=None, description="""Dimensions or claims not bound under the current viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['ExtendedProfile']} })
    reported_claims: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    methods: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    assumptions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment', 'Object', 'Activity'],
         'in_subset': ['Full']} })
    uncertainties: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    synthesis_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to Activities that referenced this Object as input or output.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    operation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to ACTION_EDGE Activities involving this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object'], 'in_subset': ['Full']} })
    id: str = Field(default=..., description="""Canonical grit identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    type: str = Field(default=..., description="""For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    viewpoint_directive_id: str = Field(default=..., description="""Reference to the ViewpointDirective that shaped this grit. The bootstrap meta-viewpoint and the blank-slate viewpoint are valid references; absence is not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit'],
         'in_subset': ['MVE']} })
    provenance: str = Field(default=..., description="""Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    should_not_claim: list[str] = Field(default=..., description="""Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    scope: Optional[Union[Scope,NotesOnlyScope]] = Field(default=None, description="""Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this grit's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    review_state: Optional[ReviewState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    lifecycle_state: Optional[LifecycleState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generation_mode: Optional[str] = Field(default=None, description="""Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class NegativeEvidenceRecord(EvidenceRecord):
    """
    First-class record of a search that returned no result under stated scope. Distinct from `unknown` (question not considered) and from `not_searched` (in scope but not attempted).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    search_method: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    search_scope: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    search_timestamp: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    search_confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    result: str = Field(default=..., description="""One of `absent`, `weak_signal`, `excluded`, `inconclusive`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    source_artifact_ref: ContentReference = Field(default=..., description="""Single source artifact this evidence is extracted from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord'], 'in_subset': ['MVE']} })
    locator: Union[Locator,CharRangeLocator,BboxLocator,SequencePositionLocator,ProcessingLogLineLocator,TableCellLocator,FileRegionLocator,CompositeLocator] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord'], 'in_subset': ['MVE']} })
    extracted_content: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    normalized_payload: Optional[str] = Field(default=None, description="""Viewpoint-defined structured payload, serialized as a JSON string in v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    evidence_type: Optional[str] = Field(default=None, description="""CURIE identifying the kind of scientific content the locator anchors. No core-supplied permissible values; viewpoints supply the evidence-type vocabulary they use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extraction_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extraction_confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    lineage: Optional[LineageType] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    cited_from: Optional[str] = Field(default=None, description="""Identifier or marker for prior evidence this record derives from or cites. May be `unknown_external` when citation resolution has not happened.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    id: str = Field(default=..., description="""Canonical grit identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    type: str = Field(default=..., description="""For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary. For Activity, a CURIE corresponding to the ActivityType value (e.g. grits:activity_type/synthesis_edge).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    viewpoint_directive_id: str = Field(default=..., description="""Reference to the ViewpointDirective that shaped this grit. The bootstrap meta-viewpoint and the blank-slate viewpoint are valid references; absence is not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence', 'CompatibilityJudgment', 'Grit'],
         'in_subset': ['MVE']} })
    provenance: str = Field(default=..., description="""Provenance description for v1. Future versions will model provenance as structured edges into the hyperDAG; for now a free-form string is accepted to allow ingestion bundles from upstream extraction tools.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    should_not_claim: list[str] = Field(default=..., description="""Epistemic boundaries this grit must respect. Combination of per-class defaults plus directive-imposed rules from the viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'in_subset': ['MVE']} })
    scope: Optional[Union[Scope,NotesOnlyScope]] = Field(default=None, description="""Optional but recommended. Viewpoint-supplied scope dimensions describing the conditions under which this grit's statements apply. The core Scope marker carries no domain dimensions; load a viewpoint schema to populate them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    review_state: Optional[ReviewState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    lifecycle_state: Optional[LifecycleState] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generation_mode: Optional[str] = Field(default=None, description="""Free-form descriptor of the process that generated this grit (parser name + version, viewpoint name + version, LLM model + tier).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ContentReference.model_rebuild()
Scope.model_rebuild()
NotesOnlyScope.model_rebuild()
Locator.model_rebuild()
CharRangeLocator.model_rebuild()
BboxLocator.model_rebuild()
SequencePositionLocator.model_rebuild()
ProcessingLogLineLocator.model_rebuild()
TableCellLocator.model_rebuild()
FileRegionLocator.model_rebuild()
CompositeLocator.model_rebuild()
Confidence.model_rebuild()
CompatibilityJudgment.model_rebuild()
Grit.model_rebuild()
Object.model_rebuild()
Activity.model_rebuild()
EvidenceRecord.model_rebuild()
ViewpointDirective.model_rebuild()
NegativeEvidenceRecord.model_rebuild()
