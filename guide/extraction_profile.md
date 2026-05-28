# ExtractionProfile

## Purpose

An `ExtractionProfile` defines **extraction and grounding semantics**: how finely content is decomposed, how densely claims are anchored in evidence, what locator fidelity is expected, and which content kinds require verbatim preservation or mandatory grounding.

It answers: *how* to extract — not *what* may be claimed (ViewpointDirective) or *what inference* is allowed (ReasoningPolicy).

## What it is

`ExtractionProfile` is a subclass of `OperationalLayer`, which is a subclass of `Object`. Reusable foundational profiles reference the bootstrap meta-viewpoint (`viewpoint_directive_id: vpt:meta-v0`).

```
Object
└── OperationalLayer
    └── ExtractionProfile
```

Supported composition modes: `additive`, `overriding`.

## Key fields

### Inherited from OperationalLayer / Object / Grit

`layer_name`, `composition_mode`, `parent_extraction_profile_ids`, full discipline contract.

### ExtractionProfile-specific

| Field | Type | Description |
|-------|------|-------------|
| `granularity` | `ExtractionGranularity` | `coarse`, `standard`, `detailed`, `exhaustive` |
| `evidence_density` | `EvidenceDensity` | `sparse`, `standard`, `dense` |
| `locator_fidelity` | `LocatorFidelity` | `document`, `section`, `paragraph`, `span`, `char` |
| `preserve_numeric_values` | boolean | Reported numbers must be preserved verbatim |
| `preserve_uncertainty_language` | boolean | Hedging language must be preserved verbatim |
| `require_char_level_locators` | boolean | Anchored content requires character-level locators |
| `preserve_content_kinds` | CurieOrUri[] | Content kinds whose content must be preserved (viewpoint-supplied CURIEs) |
| `require_grounding_for_content_kinds` | CurieOrUri[] | Content kinds that must have an evidence record |
| `high_fidelity_content_kinds` | CurieOrUri[] | Content kinds requiring high-fidelity locators and verbatim preservation |

Content kinds (`pp:measurement`, `pp:equation`, …) are opaque CURIEs in core. Viewpoints assign meaning. Core assigns no document or domain semantics.

This layer carries **no infrastructure settings** — no retry, OCR, chunking, parallelism, transport, or cache concerns.

## Relationships

```
ViewpointDirective → composed with ExtractionProfile via compose_viewpoint()
ExtractionProfile  → parent_extraction_profile_ids (composition chain)
EvidenceRecord     → shaped by extraction semantics (locator fidelity, grounding density)
```

## Why it exists

Grounding requirements vary by task. A literature survey needs coarse document-level anchors; a regulatory submission needs character-level locators on every numeric claim. `ExtractionProfile` carries these requirements independently of admissibility rules, so the same viewpoint pairs with a `detailed` or `coarse` profile without duplicating prompts.

In the k_cat example, a `detailed` profile with `require_grounding_for_content_kinds: [pp:measurement]` and `locator_fidelity: char` ensures every reported k_cat has a character-level anchor — making fabrication detectable.

## Minimal example

```python
from pygrits import ExtractionProfile

profile = ExtractionProfile(
    id="ep:detailed-extraction-v0",
    type="grits:extraction_profile",
    viewpoint_directive_id="vpt:meta-v0",
    provenance="hand-authored detailed extraction profile v0",
    should_not_claim=[],
    layer_name="extraction_profile:detailed:v0",
    composition_mode="additive",
    granularity="detailed",
    evidence_density="dense",
    locator_fidelity="char",
    preserve_numeric_values=True,
    preserve_uncertainty_language=True,
    require_char_level_locators=True,
    require_grounding_for_content_kinds=["pp:measurement"],
    high_fidelity_content_kinds=["pp:measurement", "pp:equation"],
)
```

YAML equivalent: [`viewpoints/paper_parsing_v0/examples/02_detailed_extraction_profile.yaml`](../viewpoints/paper_parsing_v0/examples/02_detailed_extraction_profile.yaml).
