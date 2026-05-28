# Interactive Scientific Object Model — Core Schema

Schema for the Interactive Scientific Object Model (ISOM).
Defines the three classes of Entity (Object, Activity, EvidenceRecord), the ViewpointDirective construct, and structural primitives (ContentReference, opaque Scope marker, Locator hierarchy, structured Confidence). All entities share the discipline contract (identity, type, viewpoint, provenance, should_not_claim) and differ by role. Domain vocabulary (scope dimensions, evidence types, entity kinds) is supplied by viewpoint schemas that import or extend this core.
This is a v0.2 schema covering the vertical slice needed for the first implementation milestone (NaCl-style epistemically-disciplined refusal). It does not yet model speech acts, reactions, threads, communities, wiki statement objects, or the harmonization process.

URI: https://w3id.org/isom/core

Name: isom_core



## Classes

| Class | Description |
| --- | --- |
| [CompatibilityJudgment](CompatibilityJudgment.md) | A recorded compatibility judgment over a set of entities/evidence |
| [Confidence](Confidence.md) | Structured confidence carrying calibration metadata |
| [ContentReference](ContentReference.md) | Content-addressed reference to externally stored content |
| [Entity](Entity.md) | Abstract base for all ISOM entities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Activity](Activity.md) | Transformation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EvidenceRecord](EvidenceRecord.md) | Grounded data anchored to a single source artifact via a typed locator |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Object](Object.md) | Participant in reasoning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which entities are extracted |
| [Locator](Locator.md) | Polymorphic locator into a source artifact |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BboxLocator](BboxLocator.md) | Axis-aligned bounding box on a rasterized page |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CharRangeLocator](CharRangeLocator.md) | Character range within extracted text of a source artifact |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CompositeLocator](CompositeLocator.md) | A locator that combines multiple sub-locators |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FileRegionLocator](FileRegionLocator.md) | Byte range within an opaque binary artifact |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessingLogLineLocator](ProcessingLogLineLocator.md) | Line range within a processing log |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequencePositionLocator](SequencePositionLocator.md) | Position range within a reference biological sequence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TableCellLocator](TableCellLocator.md) | A specific cell within an extracted table |
| [Scope](Scope.md) | Container for viewpoint-supplied scope dimensions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NotesOnlyScope](NotesOnlyScope.md) | Scope marker with only free-form notes; no domain dimensions |



## Slots

| Slot | Description |
| --- | --- |
| [action_link_ids](action_link_ids.md) | Backward pointers to ACTION_EDGE Activities involving this Object |
| [activity_type](activity_type.md) |  |
| [admissibility_rationale](admissibility_rationale.md) | Why this Activity is valid given its inputs and viewpoint |
| [affordances](affordances.md) |  |
| [assumptions](assumptions.md) |  |
| [bbox_x0](bbox_x0.md) |  |
| [bbox_x1](bbox_x1.md) |  |
| [bbox_y0](bbox_y0.md) |  |
| [bbox_y1](bbox_y1.md) |  |
| [byte_end](byte_end.md) |  |
| [byte_start](byte_start.md) |  |
| [calibration_scope](calibration_scope.md) | The data distribution under which the confidence was calibrated |
| [char_end](char_end.md) |  |
| [char_start](char_start.md) |  |
| [checked_scope_dimensions](checked_scope_dimensions.md) |  |
| [cited_from](cited_from.md) | Identifier or marker for prior evidence this record derives from or cites |
| [col](col.md) |  |
| [compared_entity_ids](compared_entity_ids.md) |  |
| [compatibility_judgments](compatibility_judgments.md) |  |
| [confidence](confidence.md) |  |
| [confidence_basis](confidence_basis.md) |  |
| [confidence_domain](confidence_domain.md) | The input domain where the calibration applies |
| [directive_name](directive_name.md) | Human-readable name (e |
| [evidence_record_ids](evidence_record_ids.md) | References to EvidenceRecord entities anchoring this Object's claims |
| [evidence_type](evidence_type.md) | CURIE identifying the kind of scientific content the locator anchors |
| [exemplars](exemplars.md) |  |
| [extracted_content](extracted_content.md) |  |
| [extraction_confidence](extraction_confidence.md) |  |
| [extraction_method](extraction_method.md) |  |
| [failure_modes](failure_modes.md) |  |
| [features](features.md) | Viewpoint-defined structured payload, serialized as a JSON string in v1 |
| [gaps](gaps.md) |  |
| [generation_mode](generation_mode.md) | Free-form descriptor of the process that generated this entity (parser name +... |
| [hash_mode](hash_mode.md) | How the sha256 was computed |
| [id](id.md) | Canonical entity identifier |
| [imposed_should_not_claim](imposed_should_not_claim.md) | should_not_claim rules this directive imposes on every entity extracted under... |
| [inputs](inputs.md) | Input entity IDs consumed by this Activity |
| [lifecycle_state](lifecycle_state.md) |  |
| [lineage](lineage.md) |  |
| [locator](locator.md) |  |
| [locator_type](locator_type.md) | Class name of the concrete Locator subclass (e |
| [log_line_end](log_line_end.md) |  |
| [log_line_start](log_line_start.md) |  |
| [media_type](media_type.md) | MIME type for disambiguation |
| [members](members.md) |  |
| [methods](methods.md) |  |
| [needs](needs.md) |  |
| [normalized_payload](normalized_payload.md) | Viewpoint-defined structured payload, serialized as a JSON string in v1 |
| [notes](notes.md) | Free-text scope clarification |
| [observations](observations.md) |  |
| [offers](offers.md) |  |
| [outputs](outputs.md) | New entities produced by this Activity |
| [page](page.md) |  |
| [prompts](prompts.md) |  |
| [provenance](provenance.md) | Provenance description for v1 |
| [rationale](rationale.md) |  |
| [reference_sequence_id](reference_sequence_id.md) |  |
| [reported_claims](reported_claims.md) |  |
| [result](result.md) | One of `absent`, `weak_signal`, `excluded`, `inconclusive` |
| [retrieved_at](retrieved_at.md) | Last successful integrity verification timestamp |
| [review_state](review_state.md) |  |
| [row](row.md) |  |
| [scope](scope.md) | Optional but recommended |
| [scope_type](scope_type.md) | Class name of the concrete Scope subclass (e |
| [search_confidence](search_confidence.md) |  |
| [search_method](search_method.md) |  |
| [search_scope](search_scope.md) |  |
| [search_timestamp](search_timestamp.md) |  |
| [seq_end](seq_end.md) |  |
| [seq_start](seq_start.md) |  |
| [sha256](sha256.md) | Integrity check on the content |
| [should_not_claim](should_not_claim.md) | Epistemic boundaries this entity must respect |
| [source_artifact_ref](source_artifact_ref.md) | Single source artifact this evidence is extracted from |
| [source_artifact_refs](source_artifact_refs.md) | ContentReferences to the source artifacts this Object derives from |
| [status](status.md) |  |
| [summary](summary.md) |  |
| [synthesis_link_ids](synthesis_link_ids.md) | Backward pointers to Activities that referenced this Object as input or outpu... |
| [table_id](table_id.md) |  |
| [target_schema](target_schema.md) | Reference to the LinkML schema (or schema profile) this directive commits to |
| [type](type.md) | For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary |
| [uncertainties](uncertainties.md) |  |
| [uri](uri.md) | Locator (file path, https URL, did: |
| [value](value.md) | Numeric confidence; semantics depend on confidence_basis |
| [viewpoint_directive_id](viewpoint_directive_id.md) | Viewpoint under which calibration was performed |
| [vocabulary_refs](vocabulary_refs.md) |  |
| [wiki_link_ids](wiki_link_ids.md) | Backward pointers to wiki statement Objects citing this Object |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ActivityType](ActivityType.md) | Structural type of an Activity (hyperedge in the topology) |
| [CompatibilityStatus](CompatibilityStatus.md) | Outcome of a compatibility judgment |
| [ConfidenceBasis](ConfidenceBasis.md) | Source semantics of a confidence value |
| [EpistemicStatus](EpistemicStatus.md) | Epistemic label on a consequential statement |
| [HashMode](HashMode.md) | How a ContentReference's sha256 is computed |
| [LifecycleState](LifecycleState.md) | Lifecycle state of an entity |
| [LineageType](LineageType.md) | Independence classification of an evidence record |
| [RefusalState](RefusalState.md) | Five-state refusal taxonomy |
| [ReviewState](ReviewState.md) | Epistemic maturity of a derived entity |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [CurieOrUri](CurieOrUri.md) | A CURIE or URI identifying a vocabulary term |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [EntityId](EntityId.md) | Canonical entity identifier of the form scheme:value, where scheme is one of ... |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Iso8601](Iso8601.md) | ISO 8601 datetime string |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sha256Hex](Sha256Hex.md) | Hex-encoded SHA-256, lowercase, 64 chars |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Full](Full.md) | Full object surface including reported_claims, methods, assumptions, uncertai... |
| [MVE](MVE.md) | Minimum viable entity |
| [ParticipationReady](ParticipationReady.md) | Object fields needed for community participation (offers, needs, gaps, featur... |
