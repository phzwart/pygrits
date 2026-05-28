# isom_core 

Schema for the Interactive Scientific Object Model (ISOM).
Defines the three classes of Entity (Object, Activity, EvidenceRecord), the ViewpointDirective construct, and structural primitives (ContentReference, opaque Scope marker, Locator hierarchy, structured Confidence). All entities share the discipline contract (identity, type, viewpoint, provenance, should_not_claim) and differ by role. Domain vocabulary (scope dimensions, evidence types, entity kinds) is supplied by viewpoint schemas that import or extend this core.
This is a v0.2 schema covering the vertical slice needed for the first implementation milestone (NaCl-style epistemically-disciplined refusal). It does not yet model speech acts, reactions, threads, communities, wiki statement objects, or the harmonization process.

URI: https://w3id.org/isom/core