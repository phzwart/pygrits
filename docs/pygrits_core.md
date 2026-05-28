# pygrits_core 

Core schema for pygrits. Defines Grit role classes (Object, Activity, EvidenceRecord), ViewpointDirective, and structural primitives (ContentReference, opaque Scope marker, Locator hierarchy, structured Confidence). All grits share the discipline contract (identity, type, viewpoint, provenance, should_not_claim) and differ by role. Domain vocabulary is supplied by viewpoint schemas that import or extend this core.

URI: https://w3id.org/grits/core