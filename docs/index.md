# pygrits Core Schema

Core schema for pygrits. Defines Grit role classes (Object, Activity, EvidenceRecord), ViewpointDirective, and structural primitives (ContentReference, opaque Scope marker, Locator hierarchy, structured Confidence). All grits share the discipline contract (identity, type, viewpoint, provenance, should_not_claim) and differ by role. Domain vocabulary is supplied by viewpoint schemas that import or extend this core.

URI: https://w3id.org/grits/core

Name: pygrits_core



## Classes

| Class | Description |
| --- | --- |
| [CompatibilityJudgment](CompatibilityJudgment.md) | A recorded compatibility judgment over a set of grits/evidence |
| [Confidence](Confidence.md) | Structured confidence carrying calibration metadata |
| [ContentReference](ContentReference.md) | Content-addressed reference to externally stored content |
| [Grit](Grit.md) | Abstract base for all pygrits graph nodes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Activity](Activity.md) | Hyperedge |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EvidenceRecord](EvidenceRecord.md) | Anchor unit |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NegativeEvidenceRecord](NegativeEvidenceRecord.md) | First-class record of a search that returned no result under stated scope |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Object](Object.md) | Subject node |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ViewpointDirective](ViewpointDirective.md) | The interpretive frame under which grits are extracted |
| [Locator](Locator.md) | Polymorphic locator into a source artifact |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BboxLocator](BboxLocator.md) | Axis-aligned bounding box on a rasterized page |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CharRangeLocator](CharRangeLocator.md) | Character range within extracted text of a source artifact |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CompositeLocator](CompositeLocator.md) | A locator that combines multiple sub-locators |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FileRegionLocator](FileRegionLocator.md) | Byte range within an opaque binary artifact |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessingLogLineLocator](ProcessingLogLineLocator.md) | Line range within a processing log |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequencePositionLocator](SequencePositionLocator.md) | Position range within a reference sequence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TableCellLocator](TableCellLocator.md) | A specific cell within an extracted table |
| [Scope](Scope.md) | Container for viewpoint-supplied scope dimensions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NotesOnlyScope](NotesOnlyScope.md) | Scope marker with only free-form notes; no domain dimensions |



## Slots

| Slot | Description |
| --- | --- |
| [activity_type](activity_type.md) |  |
| [admissibility_rationale](admissibility_rationale.md) | Why this Activity is valid given its inputs and viewpoint |
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
| [compared_grit_ids](compared_grit_ids.md) |  |
| [compatibility_judgments](compatibility_judgments.md) |  |
| [confidence](confidence.md) |  |
| [confidence_basis](confidence_basis.md) |  |
| [confidence_domain](confidence_domain.md) | The input domain where the calibration applies |
| [directive_name](directive_name.md) | Human-readable name (e |
| [evidence_record_ids](evidence_record_ids.md) | References to EvidenceRecord grits anchoring this Object's claims |
| [evidence_type](evidence_type.md) | CURIE identifying the kind of scientific content the locator anchors |
| [exemplars](exemplars.md) |  |
| [extracted_content](extracted_content.md) |  |
| [extraction_confidence](extraction_confidence.md) |  |
| [extraction_method](extraction_method.md) |  |
| [failure_modes](failure_modes.md) |  |
| [features](features.md) | Viewpoint-defined structured payload, serialized as a JSON string in v1 |
| [generation_mode](generation_mode.md) | Free-form descriptor of the process that generated this grit (parser name + v... |
| [hash_mode](hash_mode.md) | How the sha256 was computed |
| [id](id.md) | Canonical grit identifier |
| [imposed_should_not_claim](imposed_should_not_claim.md) | should_not_claim rules this directive imposes on every grit extracted under i... |
| [inputs](inputs.md) | Input grit IDs consumed by this Activity |
| [lifecycle_state](lifecycle_state.md) |  |
| [lineage](lineage.md) |  |
| [locator](locator.md) |  |
| [locator_type](locator_type.md) | Class name of the concrete Locator subclass (e |
| [log_line_end](log_line_end.md) |  |
| [log_line_start](log_line_start.md) |  |
| [media_type](media_type.md) | MIME type for disambiguation |
| [members](members.md) |  |
| [methods](methods.md) |  |
| [normalized_payload](normalized_payload.md) | Viewpoint-defined structured payload, serialized as a JSON string in v1 |
| [notes](notes.md) | Free-text scope clarification |
| [observations](observations.md) |  |
| [operation_link_ids](operation_link_ids.md) | Backward pointers to ACTION_EDGE Activities involving this Object |
| [outputs](outputs.md) | New grits produced by this Activity |
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
| [should_not_claim](should_not_claim.md) | Epistemic boundaries this grit must respect |
| [source_artifact_ref](source_artifact_ref.md) | Single source artifact this evidence is extracted from |
| [source_artifact_refs](source_artifact_refs.md) | ContentReferences to the source artifacts this Object derives from |
| [status](status.md) |  |
| [summary](summary.md) |  |
| [synthesis_link_ids](synthesis_link_ids.md) | Backward pointers to Activities that referenced this Object as input or outpu... |
| [table_id](table_id.md) |  |
| [target_schema](target_schema.md) | Reference to the LinkML schema (or schema profile) this directive commits to |
| [type](type.md) | For Object and EvidenceRecord, a CURIE into a viewpoint vocabulary |
| [uncertainties](uncertainties.md) |  |
| [unspecified_items](unspecified_items.md) | Dimensions or claims not bound under the current viewpoint |
| [uri](uri.md) | Locator (file path, https URL, did: |
| [value](value.md) | Numeric confidence; semantics depend on confidence_basis |
| [viewpoint_directive_id](viewpoint_directive_id.md) | Viewpoint under which calibration was performed |
| [vocabulary_refs](vocabulary_refs.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ActivityType](ActivityType.md) | Structural type of an Activity (hyperedge in the topology) |
| [CompatibilityStatus](CompatibilityStatus.md) | Outcome of a compatibility judgment |
| [ConfidenceBasis](ConfidenceBasis.md) | Source semantics of a confidence value |
| [EpistemicStatus](EpistemicStatus.md) | Epistemic label on a consequential statement |
| [HashMode](HashMode.md) | How a ContentReference's sha256 is computed |
| [LifecycleState](LifecycleState.md) | Lifecycle state of a grit |
| [LineageType](LineageType.md) | Independence classification of an evidence record |
| [RefusalState](RefusalState.md) | Five-state refusal taxonomy |
| [ReviewState](ReviewState.md) | Epistemic maturity of a derived grit |


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
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [GritId](GritId.md) | Canonical grit identifier of the form scheme:value, where scheme is one of ob... |
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
| [ExtendedProfile](ExtendedProfile.md) | Object fields for extended descriptive payload (summary, features, observatio... |
| [Full](Full.md) | Full object surface including reported_claims, methods, assumptions, uncertai... |
| [MVE](MVE.md) | Minimum viable grit |
