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


linkml_meta = LinkMLMeta({'default_prefix': 'de',
     'default_range': 'string',
     'description': 'Viewpoint vocabulary for document and data extraction '
                    'pipelines. Declares evidence-type CURIEs for anchored content '
                    'kinds (text spans, figures, tables, etc.). These are '
                    'document-extraction concepts, not domain-specific scientific '
                    'content kinds.',
     'id': 'https://w3id.org/grits/viewpoints/document_extraction_v0',
     'imports': ['linkml:types', '../src/pygrits/core'],
     'license': 'BSD-3-Clause',
     'name': 'document_extraction_v0',
     'prefixes': {'de': {'prefix_prefix': 'de',
                         'prefix_reference': 'https://w3id.org/grits/viewpoints/document_extraction_v0/'},
                  'grits': {'prefix_prefix': 'grits',
                            'prefix_reference': 'https://w3id.org/grits/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'viewpoints/document_extraction_v0.yaml',
     'title': 'Document Extraction Viewpoint v0'} )

class HashMode(str, Enum):
    raw_bytes = "raw_bytes"
    linkml_canonical_jcs = "linkml_canonical_jcs"


class ActivityType(str, Enum):
    """
    Role of an Activity edge. Four values, no more.
    """
    derivation = "derivation"
    """
    Inputs -> new Entity. The workhorse. prov:Derivation.
    """
    support = "support"
    """
    Evidence -> Entity it supports. No output Entity.
    """
    contradiction = "contradiction"
    """
    Evidence -> Entity it contradicts. No output Entity.
    """
    adjudication = "adjudication"
    """
    Resolves a set of contradiction Activities. Output is a curator decision Entity.
    """


class EvidenceLabel(str, Enum):
    """
    How a claim relates to its evidence. One axis, four values.
    """
    direct = "direct"
    """
    Source states it. Locator points at the statement.
    """
    derived = "derived"
    """
    Follows by explicit reasoning from direct claims. Rationale required.
    """
    inferred = "inferred"
    """
    Plausible reading with no stated rationale in any source.
    """
    unknown = "unknown"
    """
    Slot is needed and no source fills it.
    """


class ReviewState(str, Enum):
    machine_generated = "machine_generated"
    curator_reviewed = "curator_reviewed"
    disputed = "disputed"
    retracted = "retracted"


class ConfidenceBasis(str, Enum):
    self_report = "self_report"
    conformal = "conformal"
    bayesian = "bayesian"
    heuristic = "heuristic"


class NegativeResult(str, Enum):
    absent = "absent"
    weak_signal = "weak_signal"
    excluded = "excluded"
    inconclusive = "inconclusive"


class DocumentExtractionEvidenceType(str, Enum):
    """
    Evidence-type vocabulary for document extraction. Values are emitted as de:<term> CURIEs on EvidenceRecord.evidence_type.
    """
    text_span = "text_span"
    """
    Verbatim text span extracted from a source artifact.
    """
    figure = "figure"
    """
    Figure or image region in a source artifact.
    """
    table = "table"
    """
    Extracted table structure.
    """
    table_cell = "table_cell"
    """
    Individual table cell content.
    """
    bbox_region = "bbox_region"
    """
    Arbitrary bounding-box region on a rasterized page.
    """
    processing_log_line = "processing_log_line"
    """
    Line or range in a processing log.
    """
    metadata_field = "metadata_field"
    """
    Document metadata field (title, author, DOI, etc.).
    """



class ContentReference(ConfiguredBaseModel):
    """
    Content-addressed reference. Identity is uri + sha256 + hash_mode.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    uri: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference'], 'slot_uri': 'schema:contentUrl'} })
    sha256: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })
    hash_mode: HashMode = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference']} })
    media_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ContentReference'], 'slot_uri': 'schema:encodingFormat'} })


class Scope(ConfiguredBaseModel):
    """
    Viewpoint-supplied conditions under which a node's statements apply. Subclass to add typed dimensions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/grits/core'})

    scope_type: Literal["Scope"] = Field(default="Scope", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Scope']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Scope']} })


class NotesOnlyScope(Scope):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    scope_type: Literal["NotesOnlyScope"] = Field(default="NotesOnlyScope", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Scope']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Scope']} })


class Locator(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/grits/core'})

    locator_type: Literal["Locator"] = Field(default="Locator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class CharRangeLocator(Locator):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    char_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator']} })
    char_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator']} })
    page: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator', 'BboxLocator']} })
    locator_type: Literal["CharRangeLocator"] = Field(default="CharRangeLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class LineRangeLocator(Locator):
    """
    Line range in a text file (source code, notebook cell, log).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    path: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['LineRangeLocator']} })
    line_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['LineRangeLocator']} })
    line_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['LineRangeLocator']} })
    locator_type: Literal["LineRangeLocator"] = Field(default="LineRangeLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class BboxLocator(Locator):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    page: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CharRangeLocator', 'BboxLocator']} })
    bbox_x0: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    bbox_y0: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    bbox_x1: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    bbox_y1: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BboxLocator']} })
    locator_type: Literal["BboxLocator"] = Field(default="BboxLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class TableCellLocator(Locator):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    table_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TableCellLocator']} })
    row: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TableCellLocator']} })
    col: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TableCellLocator']} })
    locator_type: Literal["TableCellLocator"] = Field(default="TableCellLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class SequencePositionLocator(Locator):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    reference_sequence_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SequencePositionLocator']} })
    seq_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SequencePositionLocator']} })
    seq_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SequencePositionLocator']} })
    locator_type: Literal["SequencePositionLocator"] = Field(default="SequencePositionLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class FileRegionLocator(Locator):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    byte_start: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FileRegionLocator']} })
    byte_end: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FileRegionLocator']} })
    locator_type: Literal["FileRegionLocator"] = Field(default="FileRegionLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class CompositeLocator(Locator):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    members: Optional[list[Union[Locator,CharRangeLocator,LineRangeLocator,BboxLocator,TableCellLocator,SequencePositionLocator,FileRegionLocator,CompositeLocator]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompositeLocator']} })
    locator_type: Literal["CompositeLocator"] = Field(default="CompositeLocator", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Locator']} })


class Confidence(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    confidence_basis: ConfidenceBasis = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })
    calibration_scope: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Confidence']} })


class EvidenceLink(ConfiguredBaseModel):
    """
    A labelled edge from an Entity to an EvidenceRecord. The label lives here, not on the record, because one record can support a claim directly and another only by inference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core'})

    evidence_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceLink']} })
    label: EvidenceLabel = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceLink']} })
    rationale: Optional[str] = Field(default=None, description="""Required when label is derived or inferred. Enforce in a validator, not in the schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceLink', 'Activity']} })


class Grit(ConfiguredBaseModel):
    """
    Base for all nodes. Immutable once written. id is declared; content_hash is an integrity check computed over all other fields and excluded from canonicalization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/grits/core'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    content_hash: Optional[str] = Field(default=None, description="""Excluded from canonical bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    viewpoint_id: str = Field(default=..., description="""ViewpointDirective that shaped this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generated_by: Optional[str] = Field(default=None, description="""Activity that produced this node, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasGeneratedBy'} })
    agent: Optional[str] = Field(default=None, description="""Software or person that produced this node (name+version, or ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasAttributedTo'} })
    created_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:generatedAtTime'} })
    review_state: Optional[ReviewState] = Field(default=ReviewState.machine_generated, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'ifabsent': 'string(machine_generated)'} })
    scope: Optional[Union[Scope,NotesOnlyScope,DocumentExtractionScope]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    caveats: Optional[list[str]] = Field(default=None, description="""Optional free-text limits on use. Not a substitute for typed slots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class Entity(Grit):
    """
    A subject node — a claim, a document, a measurement, a plan element. Domain schemas subclass this with typed slots. Formerly Object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity', 'from_schema': 'https://w3id.org/grits/core'})

    plan_variable: Optional[str] = Field(default=None, description="""Type-level variable this entity instantiates, when a plan graph exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'pplan:correspondsToVariable'} })
    derived_from: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'prov:wasDerivedFrom'} })
    sources: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'prov:hadPrimarySource'} })
    evidence: Optional[list[EvidenceLink]] = Field(default=None, description="""Labelled links to EvidenceRecords.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    summary: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    content_hash: Optional[str] = Field(default=None, description="""Excluded from canonical bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    viewpoint_id: str = Field(default=..., description="""ViewpointDirective that shaped this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generated_by: Optional[str] = Field(default=None, description="""Activity that produced this node, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasGeneratedBy'} })
    agent: Optional[str] = Field(default=None, description="""Software or person that produced this node (name+version, or ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasAttributedTo'} })
    created_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:generatedAtTime'} })
    review_state: Optional[ReviewState] = Field(default=ReviewState.machine_generated, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'ifabsent': 'string(machine_generated)'} })
    scope: Optional[Union[Scope,NotesOnlyScope,DocumentExtractionScope]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    caveats: Optional[list[str]] = Field(default=None, description="""Optional free-text limits on use. Not a substitute for typed slots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class Activity(Grit):
    """
    Hyperedge. Consumes Entities/EvidenceRecords, may emit Entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity', 'from_schema': 'https://w3id.org/grits/core'})

    activity_type: ActivityType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    inputs: list[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'slot_uri': 'prov:used'} })
    outputs: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'slot_uri': 'prov:generated'} })
    plan_step: Optional[str] = Field(default=None, description="""Type-level step this activity executes, when a plan graph exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'slot_uri': 'pplan:correspondsToStep'} })
    rationale: Optional[str] = Field(default=None, description="""Why this activity is admissible given its inputs and viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceLink', 'Activity']} })
    confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    started_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'slot_uri': 'prov:startedAtTime'} })
    ended_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'slot_uri': 'prov:endedAtTime'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    content_hash: Optional[str] = Field(default=None, description="""Excluded from canonical bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    viewpoint_id: str = Field(default=..., description="""ViewpointDirective that shaped this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generated_by: Optional[str] = Field(default=None, description="""Activity that produced this node, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasGeneratedBy'} })
    agent: Optional[str] = Field(default=None, description="""Software or person that produced this node (name+version, or ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasAttributedTo'} })
    created_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:generatedAtTime'} })
    review_state: Optional[ReviewState] = Field(default=ReviewState.machine_generated, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'ifabsent': 'string(machine_generated)'} })
    scope: Optional[Union[Scope,NotesOnlyScope,DocumentExtractionScope]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    caveats: Optional[list[str]] = Field(default=None, description="""Optional free-text limits on use. Not a substitute for typed slots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class EvidenceRecord(Grit):
    """
    Anchor into one source artifact via a typed locator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity', 'from_schema': 'https://w3id.org/grits/core'})

    source: ContentReference = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord'], 'slot_uri': 'prov:hadPrimarySource'} })
    locator: Union[Locator,CharRangeLocator,LineRangeLocator,BboxLocator,TableCellLocator,SequencePositionLocator,FileRegionLocator,CompositeLocator] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extracted_content: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    evidence_type: Optional[str] = Field(default=None, description="""Viewpoint-supplied CURIE for the kind of content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extraction_confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    content_hash: Optional[str] = Field(default=None, description="""Excluded from canonical bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    viewpoint_id: str = Field(default=..., description="""ViewpointDirective that shaped this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generated_by: Optional[str] = Field(default=None, description="""Activity that produced this node, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasGeneratedBy'} })
    agent: Optional[str] = Field(default=None, description="""Software or person that produced this node (name+version, or ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasAttributedTo'} })
    created_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:generatedAtTime'} })
    review_state: Optional[ReviewState] = Field(default=ReviewState.machine_generated, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'ifabsent': 'string(machine_generated)'} })
    scope: Optional[Union[Scope,NotesOnlyScope,DocumentExtractionScope]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    caveats: Optional[list[str]] = Field(default=None, description="""Optional free-text limits on use. Not a substitute for typed slots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class NegativeEvidenceRecord(EvidenceRecord):
    """
    A search under stated scope that returned nothing. First-class absence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/core',
         'slot_usage': {'locator': {'name': 'locator', 'required': False}}})

    search_method: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    search_scope: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    result: NegativeResult = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['NegativeEvidenceRecord']} })
    source: ContentReference = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord'], 'slot_uri': 'prov:hadPrimarySource'} })
    locator: Optional[Union[Locator,CharRangeLocator,LineRangeLocator,BboxLocator,TableCellLocator,SequencePositionLocator,FileRegionLocator,CompositeLocator]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extracted_content: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    evidence_type: Optional[str] = Field(default=None, description="""Viewpoint-supplied CURIE for the kind of content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    extraction_confidence: Optional[Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    content_hash: Optional[str] = Field(default=None, description="""Excluded from canonical bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    viewpoint_id: str = Field(default=..., description="""ViewpointDirective that shaped this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generated_by: Optional[str] = Field(default=None, description="""Activity that produced this node, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasGeneratedBy'} })
    agent: Optional[str] = Field(default=None, description="""Software or person that produced this node (name+version, or ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasAttributedTo'} })
    created_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:generatedAtTime'} })
    review_state: Optional[ReviewState] = Field(default=ReviewState.machine_generated, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'ifabsent': 'string(machine_generated)'} })
    scope: Optional[Union[Scope,NotesOnlyScope,DocumentExtractionScope]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    caveats: Optional[list[str]] = Field(default=None, description="""Optional free-text limits on use. Not a substitute for typed slots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class ViewpointDirective(Entity):
    """
    Flat interpretive contract. No viewpoint inheritance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Plan', 'from_schema': 'https://w3id.org/grits/core'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective'], 'slot_uri': 'schema:name'} })
    prompts: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    exemplars: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    vocabularies: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    target_schema: Optional[ContentReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    constraints: Optional[list[str]] = Field(default=None, description="""Rules imposed on every node extracted under this viewpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ViewpointDirective']} })
    plan_variable: Optional[str] = Field(default=None, description="""Type-level variable this entity instantiates, when a plan graph exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'pplan:correspondsToVariable'} })
    derived_from: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'prov:wasDerivedFrom'} })
    sources: Optional[list[ContentReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'prov:hadPrimarySource'} })
    evidence: Optional[list[EvidenceLink]] = Field(default=None, description="""Labelled links to EvidenceRecords.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    summary: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    content_hash: Optional[str] = Field(default=None, description="""Excluded from canonical bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    viewpoint_id: str = Field(default=..., description="""ViewpointDirective that shaped this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    generated_by: Optional[str] = Field(default=None, description="""Activity that produced this node, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasGeneratedBy'} })
    agent: Optional[str] = Field(default=None, description="""Software or person that produced this node (name+version, or ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:wasAttributedTo'} })
    created_at: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'slot_uri': 'prov:generatedAtTime'} })
    review_state: Optional[ReviewState] = Field(default=ReviewState.machine_generated, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit'], 'ifabsent': 'string(machine_generated)'} })
    scope: Optional[Union[Scope,NotesOnlyScope,DocumentExtractionScope]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })
    caveats: Optional[list[str]] = Field(default=None, description="""Optional free-text limits on use. Not a substitute for typed slots.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Grit']} })


class DocumentExtractionScope(NotesOnlyScope):
    """
    Scope for document extraction; no scientific domain dimensions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/grits/viewpoints/document_extraction_v0'})

    scope_type: Literal["DocumentExtractionScope"] = Field(default="DocumentExtractionScope", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Scope']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Scope']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ContentReference.model_rebuild()
Scope.model_rebuild()
NotesOnlyScope.model_rebuild()
Locator.model_rebuild()
CharRangeLocator.model_rebuild()
LineRangeLocator.model_rebuild()
BboxLocator.model_rebuild()
TableCellLocator.model_rebuild()
SequencePositionLocator.model_rebuild()
FileRegionLocator.model_rebuild()
CompositeLocator.model_rebuild()
Confidence.model_rebuild()
EvidenceLink.model_rebuild()
Grit.model_rebuild()
Entity.model_rebuild()
Activity.model_rebuild()
EvidenceRecord.model_rebuild()
NegativeEvidenceRecord.model_rebuild()
ViewpointDirective.model_rebuild()
DocumentExtractionScope.model_rebuild()
