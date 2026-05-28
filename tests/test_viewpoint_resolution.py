"""
Deterministic composition of epistemic layers.

These tests pin the field-local merge rules, the parents-first ordering, stable
identity under the one canonical pipeline, and the failure modes (cycles,
unknown ids, unsupported modes). They also confirm the shipped example layers
compose into a hashable ComposedViewpointDirective.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pygrits import (
    ComposedViewpointDirective,
    CompositionError,
    CompositionMode,
    ContentReference,
    ExtractionProfile,
    HashMode,
    ReasoningPolicy,
    ViewpointDirective,
    VocabularyPack,
    canonical_hash_instance,
    compose_viewpoint,
    resolve_extraction_profile,
    resolve_reasoning_policy,
    resolve_viewpoint,
    resolve_vocabulary_pack,
)

META = "vpt:meta-v0"


def _ref(uri: str) -> ContentReference:
    return ContentReference(uri=uri, sha256="a" * 64, hash_mode=HashMode.raw_bytes)


def _meta_directive() -> ViewpointDirective:
    return ViewpointDirective(
        id=META,
        type="grits:viewpoint_directive",
        viewpoint_directive_id=META,
        provenance="bootstrap",
        should_not_claim=["meta-rule"],
        directive_name="viewpoint:meta:v0",
    )


def _vp(
    vid: str,
    *,
    parents: list[str] | None = None,
    mode: CompositionMode = CompositionMode.additive,
    prompts: list[str] | None = None,
    vocab: list[str] | None = None,
    snc: list[str] | None = None,
    target: str | None = None,
) -> ViewpointDirective:
    return ViewpointDirective(
        id=vid,
        type="grits:viewpoint_directive",
        viewpoint_directive_id=META,
        provenance="p",
        should_not_claim=snc if snc is not None else [f"{vid}-rule"],
        directive_name=vid,
        composition_mode=mode,
        parent_viewpoint_ids=parents or [],
        prompts=[_ref(u) for u in (prompts or [])] or None,
        vocabulary_refs=[_ref(u) for u in (vocab or [])] or None,
        target_schema=_ref(target) if target else None,
    )


def _ep(
    eid: str,
    *,
    parents: list[str] | None = None,
    mode: CompositionMode = CompositionMode.additive,
    kinds: list[str] | None = None,
    preserve_numeric: bool | None = None,
) -> ExtractionProfile:
    return ExtractionProfile(
        id=eid,
        type="grits:extraction_profile",
        viewpoint_directive_id=META,
        provenance="p",
        should_not_claim=[],
        layer_name=eid,
        composition_mode=mode,
        parent_extraction_profile_ids=parents or [],
        preserve_content_kinds=kinds,
        preserve_numeric_values=preserve_numeric,
    )


def _vocab(
    vid: str,
    *,
    parents: list[str] | None = None,
    mode: CompositionMode = CompositionMode.additive,
    namespaces: list[str] | None = None,
) -> VocabularyPack:
    return VocabularyPack(
        id=vid,
        type="grits:vocabulary_pack",
        viewpoint_directive_id=META,
        provenance="p",
        should_not_claim=[],
        layer_name=vid,
        composition_mode=mode,
        parent_vocabulary_pack_ids=parents or [],
        active_namespaces=namespaces,
    )


def _rpol(
    rid: str,
    *,
    parents: list[str] | None = None,
    mode: CompositionMode = CompositionMode.additive,
    allow_speculative: bool | None = None,
) -> ReasoningPolicy:
    return ReasoningPolicy(
        id=rid,
        type="grits:reasoning_policy",
        viewpoint_directive_id=META,
        provenance="p",
        should_not_claim=[],
        layer_name=rid,
        composition_mode=mode,
        parent_reasoning_policy_ids=parents or [],
        allow_speculative_inference=allow_speculative,
    )


def _registry(*layers) -> dict:
    return {layer.id: layer for layer in layers}


# -------- ordering + determinism + hashing --------

def test_composition_ordering_is_parents_first() -> None:
    reg = _registry(
        _meta_directive(),
        _vp("vpt:a", parents=[META], prompts=["file://a"]),
        _vp("vpt:b", parents=["vpt:a"], prompts=["file://b"]),
    )
    resolved = resolve_viewpoint("vpt:b", reg)
    uris = [p.uri for p in resolved.prompts]
    assert uris == ["file://a", "file://b"]


def test_resolution_is_deterministic_and_hash_stable() -> None:
    reg = _registry(
        _meta_directive(),
        _vp("vpt:a", parents=[META], prompts=["file://a"]),
        _ep("ep:x", kinds=["pp:equation"]),
    )
    c1 = compose_viewpoint("vpt:a", reg, extraction_profile_id="ep:x")
    c2 = compose_viewpoint("vpt:a", reg, extraction_profile_id="ep:x")
    assert c1.model_dump() == c2.model_dump()
    assert canonical_hash_instance(c1) == canonical_hash_instance(c2)
    assert c1.id == c2.id


def test_composed_result_is_hashable_composed_directive() -> None:
    reg = _registry(_meta_directive(), _vp("vpt:a", parents=[META]))
    composed = compose_viewpoint("vpt:a", reg)
    assert isinstance(composed, ComposedViewpointDirective)
    assert canonical_hash_instance(composed).startswith("sha256:")
    assert composed.id.startswith("vpt:composed:")


# -------- duplicate elimination --------

def test_duplicate_refs_and_strings_are_deduped() -> None:
    reg = _registry(
        _meta_directive(),
        _vp("vpt:a", parents=[META], vocab=["file://r1"], snc=["dup"]),
        _vp("vpt:b", parents=["vpt:a"], vocab=["file://r1", "file://r2"], snc=["dup"]),
    )
    resolved = resolve_viewpoint("vpt:b", reg)
    assert [r.uri for r in resolved.vocabulary_refs] == ["file://r1", "file://r2"]
    assert resolved.should_not_claim.count("dup") == 1


# -------- additive vs overriding --------

def test_additive_unions_content_kinds() -> None:
    reg = _registry(
        _ep("ep:base", kinds=["pp:a"]),
        _ep("ep:child", parents=["ep:base"], mode=CompositionMode.additive, kinds=["pp:b"]),
    )
    resolved = resolve_extraction_profile("ep:child", reg)
    assert resolved.preserve_content_kinds == ["pp:a", "pp:b"]


def test_overriding_replaces_content_kinds() -> None:
    reg = _registry(
        _ep("ep:base", kinds=["pp:a"]),
        _ep("ep:child", parents=["ep:base"], mode=CompositionMode.overriding, kinds=["pp:b"]),
    )
    resolved = resolve_extraction_profile("ep:child", reg)
    assert resolved.preserve_content_kinds == ["pp:b"]


# -------- restrictive narrowing --------

def test_restrictive_reasoning_ands_permissions() -> None:
    reg = _registry(
        _rpol("rpol:base", allow_speculative=True),
        _rpol(
            "rpol:child",
            parents=["rpol:base"],
            mode=CompositionMode.restrictive,
            allow_speculative=False,
        ),
    )
    resolved = resolve_reasoning_policy("rpol:child", reg)
    assert resolved.allow_speculative_inference is False


# -------- isolated --------

def test_isolated_drops_inherited_content_but_keeps_source_ids() -> None:
    reg = _registry(
        _vocab("voc:base", namespaces=["mse"]),
        _vocab(
            "voc:child",
            parents=["voc:base"],
            mode=CompositionMode.isolated,
            namespaces=["pp"],
        ),
    )
    resolved = resolve_vocabulary_pack("voc:child", reg)
    assert resolved.active_namespaces == ["pp"]
    assert resolved.parent_vocabulary_pack_ids == ["voc:base"]


# -------- nested inheritance --------

def test_nested_three_level_chain_materializes_and_flattens() -> None:
    reg = _registry(
        _meta_directive(),
        _vp("vpt:a", parents=[META], prompts=["file://a"]),
        _vp("vpt:b", parents=["vpt:a"], prompts=["file://b"]),
        _vp("vpt:c", parents=["vpt:b"], prompts=["file://c"]),
    )
    composed = compose_viewpoint("vpt:c", reg)
    assert [p.uri for p in composed.prompts] == ["file://a", "file://b", "file://c"]
    assert composed.source_viewpoint_ids == [META, "vpt:a", "vpt:b", "vpt:c"]


# -------- failure modes --------

def test_cycle_detection_raises() -> None:
    reg = _registry(
        _vp("vpt:a", parents=["vpt:b"]),
        _vp("vpt:b", parents=["vpt:a"]),
    )
    with pytest.raises(CompositionError):
        resolve_viewpoint("vpt:a", reg)


def test_unknown_id_raises() -> None:
    reg = _registry(_vp("vpt:a", parents=["vpt:missing"]))
    with pytest.raises(CompositionError):
        resolve_viewpoint("vpt:a", reg)


def test_unsupported_mode_raises() -> None:
    # VocabularyPack supports only additive and isolated.
    reg = _registry(_vocab("voc:bad", mode=CompositionMode.overriding))
    with pytest.raises(CompositionError):
        resolve_vocabulary_pack("voc:bad", reg)


def test_type_mismatch_raises() -> None:
    reg = _registry(_ep("ep:x"))
    with pytest.raises(CompositionError):
        resolve_viewpoint("ep:x", reg)


# -------- shipped example layers --------

EXAMPLES_DIR = (
    Path(__file__).parent.parent / "viewpoints" / "paper_parsing_v0" / "examples"
)

EXAMPLE_CLASSES = {
    "01_generic_paper_parse_view.yaml": ViewpointDirective,
    "02_detailed_extraction_profile.yaml": ExtractionProfile,
    "03_materials_vocabulary_pack.yaml": VocabularyPack,
    "04_conservative_reasoning_policy.yaml": ReasoningPolicy,
}


def _load(name: str, cls: type):
    with open(EXAMPLES_DIR / name) as f:
        return cls(**yaml.safe_load(f))


@pytest.mark.parametrize("filename,cls", EXAMPLE_CLASSES.items())
def test_example_layers_validate(filename: str, cls: type) -> None:
    instance = _load(filename, cls)
    assert instance.id is not None
    assert instance.viewpoint_directive_id == META


def test_example_layers_compose_into_hashable_artifact() -> None:
    layers = [_meta_directive()]
    layers += [_load(name, cls) for name, cls in EXAMPLE_CLASSES.items()]
    reg = {layer.id: layer for layer in layers}

    composed = compose_viewpoint(
        "vpt:generic-paper-parse-v0",
        reg,
        extraction_profile_id="ep:detailed-extraction-v0",
        vocabulary_pack_id="voc:materials-science-v0",
        reasoning_policy_id="rpol:conservative-v0",
    )
    assert isinstance(composed, ComposedViewpointDirective)
    assert composed.resolved_extraction_profile.preserve_content_kinds == [
        "pp:equation",
        "pp:measurement",
    ]
    assert composed.resolved_reasoning_policy.allow_speculative_inference is False
    assert composed.resolved_vocabulary_pack.active_namespaces == ["mse"]
    assert "mse" not in str(composed.source_viewpoint_ids)  # vocabulary stays in its layer
    assert canonical_hash_instance(composed).startswith("sha256:")
