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
version = "0.1.0"


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


linkml_meta = LinkMLMeta({'default_prefix': 'coord',
     'default_range': 'string',
     'description': 'Example viewpoint for coordination-layer Object fields moved '
                    'out of core. Adds required_inputs, declared_contributions, '
                    'available_operations, and citation_link_ids to Object.',
     'id': 'https://w3id.org/grits/viewpoints/coordination_v0',
     'imports': ['linkml:types', '../src/pygrits/core'],
     'license': 'BSD-3-Clause',
     'name': 'coordination_v0',
     'prefixes': {'coord': {'prefix_prefix': 'coord',
                            'prefix_reference': 'https://w3id.org/grits/viewpoints/coordination_v0/'},
                  'grits': {'prefix_prefix': 'grits',
                            'prefix_reference': 'https://w3id.org/grits/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'viewpoints/coordination_v0.yaml',
     'title': 'Coordination Viewpoint v0'} )

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


class CompositionMode(str, Enum):
    """
    How a composable layer folds against its declared parents during deterministic resolution. Selected per layer; not every layer type supports every mode.
    """
    additive = "additive"
    """
    Child contributes additional content without removing inherited content. List fields union (dedup); most-derived non-null wins for scalars. The default for most composition.
    """
    restrictive = "restrictive"
    """
    Child narrows the admissible space relative to its parents. Constraint lists union; permission booleans combine by logical AND.
    """
    overriding = "overriding"
    """
    Child intentionally replaces inherited values for overlapping fields. Used sparingly and remains highly visible in resolved artifacts.
    """
    isolated = "isolated"
    """
    Child inherits no operational content from parents; parent ids are retained only as source references for provenance.
    """


class ExtractionGranularity(str, Enum):
    """
    How finely an extraction profile expects content to be decomposed.
    """
    coarse = "coarse"
    standard = "standard"
    detailed = "detailed"
    exhaustive = "exhaustive"


class EvidenceDensity(str, Enum):
    """
    How densely an extraction profile expects claims to be grounded in evidence.
    """
    sparse = "sparse"
    standard = "standard"
    dense = "dense"


class LocatorFidelity(str, Enum):
    """
    The locator granularity an extraction profile expects on anchored content.
    """
    document = "document"
    section = "section"
    paragraph = "paragraph"
    span = "span"
    char = "char"



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
    notes: Optional[str] = Field(default=None, description="""Free-text scope clarification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Scope', 'ReasoningPolicy']} })


class NotesOnlyScope(Scope):
    """
    Scope marker with only free-form notes; no domain dimensions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    scope_type: Literal["NotesOnlyScope"] = Field(default="NotesOnlyScope", description="""Class name of the concrete Scope subclass (e.g. NotesOnlyScope).""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Scope']} })
    notes: Optional[str] = Field(default=None, description="""Free-text scope clarification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Scope', 'ReasoningPolicy']} })


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
    assumptions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment', 'Activity']} })
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


class Object(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/viewpoints/coordination_v0'})

    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


class Activity(Grit):
    """
    Hyperedge. Consumes input grits, applies an interpretation under stated assumptions, emits output grits. Records a transform step in the hyperDAG topology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity', 'from_schema': 'https://w3id.org/grits/core'})

    activity_type: ActivityType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'in_subset': ['MVE']} })
    inputs: list[str] = Field(default=..., description="""Input grit IDs consumed by this Activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'in_subset': ['MVE']} })
    outputs: Optional[list[str]] = Field(default=None, description="""New grits produced by this Activity. May be empty for declarative edges (SUPPORT, CONTRADICTION) whose output is the Activity itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    assumptions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompatibilityJudgment', 'Activity']} })
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


class Composable(ConfiguredBaseModel):
    """
    Mixin granting a layer a composition_mode. Parent references are NOT in this mixin — each composable class declares its own semantically explicit parent slot (parent_viewpoint_ids, parent_extraction_profile_ids, etc.).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core', 'mixin': True})

    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })


class ViewpointDirective(Composable, Object):
    """
    The interpretive frame under which grits are extracted. Itself an Object — a ViewpointDirective has its own viewpoint_directive_id (the bootstrap meta-viewpoint, or itself for the meta-viewpoint). Carries prompts, exemplars, vocabulary references, target schema, and the should_not_claim rules it imposes on extracted grits. Composable against parent viewpoint directives. Supported composition modes: additive, restrictive, overriding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core', 'mixins': ['Composable']})

    directive_name: str = Field(default=..., description="""Human-readable name (e.g. viewpoint:materials_science:v1). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    parent_viewpoint_ids: Optional[list[str]] = Field(default=None, description="""ViewpointDirective ids this directive composes from, parents-first. Resolution is explicit (the caller supplies the registry); there is no implicit runtime parent lookup.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    prompts: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    exemplars: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    vocabulary_refs: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective', 'VocabularyPack']} })
    target_schema: Optional[ContentReference] = Field(default=None, description="""Reference to the LinkML schema (or schema profile) this directive commits to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    imposed_should_not_claim: Optional[list[str]] = Field(default=None, description="""should_not_claim rules this directive imposes on every grit extracted under it. Combined with per-class defaults at extraction time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })
    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


class OperationalLayer(Composable, Object):
    """
    Abstract base for composable operational/interpretive layers that are not themselves viewpoint directives (ExtractionProfile, VocabularyPack, ReasoningPolicy). Inherits the full Object/Grit discipline. Reusable foundational layers set viewpoint_directive_id to the bootstrap meta-viewpoint (vpt:meta-v0).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/grits/core',
         'mixins': ['Composable']})

    layer_name: str = Field(default=..., description="""Human-readable name (e.g. extraction_profile:detailed:v0). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalLayer']} })
    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })
    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


class ExtractionProfile(OperationalLayer):
    """
    Extraction/grounding semantics: how finely content is decomposed, how densely claims are grounded, and what locator fidelity is expected. Core understands only abstract content kinds identified by CURIEs; the semantic meaning of those CURIEs is supplied by viewpoint vocabularies. This layer carries no infrastructure settings (no retry, OCR, chunking, parallelism, transport, or cache concerns). Supported composition modes: additive, overriding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    parent_extraction_profile_ids: Optional[list[str]] = Field(default=None, description="""ExtractionProfile ids this profile composes from, parents-first.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    granularity: Optional[ExtractionGranularity] = Field(default=None, description="""How finely content should be decomposed during extraction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    evidence_density: Optional[EvidenceDensity] = Field(default=None, description="""How densely claims should be grounded in evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    locator_fidelity: Optional[LocatorFidelity] = Field(default=None, description="""Expected locator granularity for anchored content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    preserve_numeric_values: Optional[bool] = Field(default=None, description="""Whether reported numeric values must be preserved verbatim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    preserve_uncertainty_language: Optional[bool] = Field(default=None, description="""Whether uncertainty/hedging language must be preserved verbatim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    require_char_level_locators: Optional[bool] = Field(default=None, description="""Whether anchored content requires character-level locators.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    preserve_content_kinds: Optional[list[str]] = Field(default=None, description="""Content kinds (viewpoint-supplied CURIEs) whose content must be preserved. Core assigns no meaning to these CURIEs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    require_grounding_for_content_kinds: Optional[list[str]] = Field(default=None, description="""Content kinds (viewpoint-supplied CURIEs) that must be grounded in an evidence record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    high_fidelity_content_kinds: Optional[list[str]] = Field(default=None, description="""Content kinds (viewpoint-supplied CURIEs) requiring high-fidelity locators and verbatim preservation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionProfile']} })
    layer_name: str = Field(default=..., description="""Human-readable name (e.g. extraction_profile:detailed:v0). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalLayer']} })
    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })
    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


class VocabularyPack(OperationalLayer):
    """
    Namespace/ontology binding surface: the vocabulary references, ontology references, and active CURIE-prefix namespaces a layer makes available. Ontology-neutral in core — the actual terms live in external referenced content. Supported composition modes: additive, isolated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    parent_vocabulary_pack_ids: Optional[list[str]] = Field(default=None, description="""VocabularyPack ids this pack composes from, parents-first.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VocabularyPack']} })
    vocabulary_refs: Optional[list[ContentReference]] = Field(default=None, description="""Content-addressed references to vocabulary definitions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective', 'VocabularyPack']} })
    ontology_refs: Optional[list[ContentReference]] = Field(default=None, description="""Content-addressed references to ontology definitions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VocabularyPack']} })
    active_namespaces: Optional[list[str]] = Field(default=None, description="""CURIE-prefix namespaces this pack activates (e.g. \"pp\", \"mse\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['VocabularyPack']} })
    layer_name: str = Field(default=..., description="""Human-readable name (e.g. extraction_profile:detailed:v0). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalLayer']} })
    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })
    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


class ReasoningPolicy(OperationalLayer):
    """
    Inferential permission surface: what synthesis, inference, normalization, and adjudication a layer permits. Governs reasoning freedom only — it does not control extraction behavior. Supported composition modes: additive, restrictive.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    parent_reasoning_policy_ids: Optional[list[str]] = Field(default=None, description="""ReasoningPolicy ids this policy composes from, parents-first.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReasoningPolicy']} })
    allow_speculative_inference: Optional[bool] = Field(default=None, description="""Whether speculative inference is permitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReasoningPolicy']} })
    allow_cross_document_synthesis: Optional[bool] = Field(default=None, description="""Whether synthesis across multiple documents is permitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReasoningPolicy']} })
    allow_ontology_normalization: Optional[bool] = Field(default=None, description="""Whether ontology normalization is permitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReasoningPolicy']} })
    enable_contradiction_adjudication: Optional[bool] = Field(default=None, description="""Whether contradiction adjudication is enabled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReasoningPolicy']} })
    notes: Optional[str] = Field(default=None, description="""Free-text clarification of the reasoning posture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Scope', 'ReasoningPolicy']} })
    layer_name: str = Field(default=..., description="""Human-readable name (e.g. extraction_profile:detailed:v0). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationalLayer']} })
    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })
    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


class ComposedViewpointDirective(ViewpointDirective):
    """
    The frozen result of composing a ViewpointDirective with optional ExtractionProfile, VocabularyPack, and ReasoningPolicy layers. Still a viewpoint-level interpretive contract (and still hashed by the one canonical pipeline), it inlines the resolved operational layers and records the flattened source chains for inspectability. Produced by compose_viewpoint(); not hand-authored.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    resolved_extraction_profile: Optional[ExtractionProfile] = Field(default=None, description="""The resolved extraction profile, if one was composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    resolved_vocabulary_pack: Optional[VocabularyPack] = Field(default=None, description="""The resolved vocabulary pack, if one was composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    resolved_reasoning_policy: Optional[ReasoningPolicy] = Field(default=None, description="""The resolved reasoning policy, if one was composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    source_viewpoint_ids: Optional[list[str]] = Field(default=None, description="""Flattened, parents-first chain of viewpoint directive ids that were composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    source_extraction_profile_ids: Optional[list[str]] = Field(default=None, description="""Flattened, parents-first chain of extraction profile ids that were composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    source_vocabulary_pack_ids: Optional[list[str]] = Field(default=None, description="""Flattened, parents-first chain of vocabulary pack ids that were composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    source_reasoning_policy_ids: Optional[list[str]] = Field(default=None, description="""Flattened, parents-first chain of reasoning policy ids that were composed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComposedViewpointDirective']} })
    directive_name: str = Field(default=..., description="""Human-readable name (e.g. viewpoint:materials_science:v1). Combined with content hash, this gives identity-by-declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    parent_viewpoint_ids: Optional[list[str]] = Field(default=None, description="""ViewpointDirective ids this directive composes from, parents-first. Resolution is explicit (the caller supplies the registry); there is no implicit runtime parent lookup.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    prompts: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    exemplars: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    vocabulary_refs: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective', 'VocabularyPack']} })
    target_schema: Optional[ContentReference] = Field(default=None, description="""Reference to the LinkML schema (or schema profile) this directive commits to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    imposed_should_not_claim: Optional[list[str]] = Field(default=None, description="""should_not_claim rules this directive imposes on every grit extracted under it. Combined with per-class defaults at extraction time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    composition_mode: Optional[CompositionMode] = Field(default=CompositionMode.additive, description="""How this layer folds against its declared parents during resolution. Defaults to additive.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Composable'], 'ifabsent': 'string(additive)'} })
    required_inputs: Optional[list[str]] = Field(default=None, description="""Inputs or dependencies this Object declares as required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    declared_contributions: Optional[list[str]] = Field(default=None, description="""Outputs or data this Object declares as available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    available_operations: Optional[list[str]] = Field(default=None, description="""Operations downstream consumers may invoke on this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })
    citation_link_ids: Optional[list[str]] = Field(default=None, description="""Backward pointers to grits that cite this Object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Object']} })


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
NegativeEvidenceRecord.model_rebuild()
Composable.model_rebuild()
ViewpointDirective.model_rebuild()
OperationalLayer.model_rebuild()
ExtractionProfile.model_rebuild()
VocabularyPack.model_rebuild()
ReasoningPolicy.model_rebuild()
ComposedViewpointDirective.model_rebuild()
