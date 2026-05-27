# isom_core 

Schema for the Interactive Scientific Object Model (ISOM).
Defines the three classes of Entity (Object, Activity, EvidenceRecord), the ViewpointDirective construct, and primitives (ContentReference, Scope, Locator hierarchy, structured Confidence). All entities share the discipline contract (identity, type, viewpoint, provenance, should_not_claim) and differ by role. The schema implements the ISOM spec v0.
This is a v0.1 draft schema covering the vertical slice needed for the first implementation milestone (NaCl-style epistemically-disciplined refusal). It does not yet model speech acts, reactions, threads, communities, wiki statement objects, or the harmonization process. Those are deferred to v0.2.

URI: https://w3id.org/isom/core