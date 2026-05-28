"""
Deterministic, field-local composition of pygrits epistemic layers.

A ``ViewpointDirective`` and the operational layers (``ExtractionProfile``,
``VocabularyPack``, ``ReasoningPolicy``) each declare an explicit, semantically
named parent slot and a ``composition_mode``. ``compose_viewpoint`` folds each
layer's own parent chain — parents first — into a single frozen
``ComposedViewpointDirective``.

This is structural composition, not object-oriented inheritance and not a
policy engine:

- The caller passes an explicit ``registry`` mapping id -> layer instance.
  There is no global state and no implicit runtime parent lookup.
- Each field has a fixed, documented merge rule (see the ``_merge_*`` helpers).
- Resolution is deterministic: same inputs produce a byte-identical result, so
  the existing ``canonical_hash_instance`` pipeline gives a stable identity.

The composed result is still a viewpoint-level interpretive contract (a
``ComposedViewpointDirective`` is a ``ViewpointDirective``), hashed by the one
canonical pipeline. No second identity system is introduced.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import TypeVar

from pygrits.core import (
    ComposedViewpointDirective,
    CompositionMode,
    ContentReference,
    ExtractionProfile,
    Object,
    ReasoningPolicy,
    ViewpointDirective,
    VocabularyPack,
)

__all__ = [
    "CompositionError",
    "resolve_viewpoint",
    "resolve_extraction_profile",
    "resolve_vocabulary_pack",
    "resolve_reasoning_policy",
    "compose_viewpoint",
]

T = TypeVar("T", bound=Object)

# Composition modes each layer type is permitted to declare. Avoids artificial
# symmetry: not every mode is meaningful for every layer.
_ALLOWED_MODES: dict[type, frozenset[CompositionMode]] = {
    ViewpointDirective: frozenset(
        {CompositionMode.additive, CompositionMode.restrictive, CompositionMode.overriding}
    ),
    ExtractionProfile: frozenset({CompositionMode.additive, CompositionMode.overriding}),
    VocabularyPack: frozenset({CompositionMode.additive, CompositionMode.isolated}),
    ReasoningPolicy: frozenset({CompositionMode.additive, CompositionMode.restrictive}),
}

_PARENT_ATTR: dict[type, str] = {
    ViewpointDirective: "parent_viewpoint_ids",
    ExtractionProfile: "parent_extraction_profile_ids",
    VocabularyPack: "parent_vocabulary_pack_ids",
    ReasoningPolicy: "parent_reasoning_policy_ids",
}


class CompositionError(Exception):
    """Raised on cycles, unknown layer ids, type mismatches, or unsupported modes."""


# ----------------------------------------------------------------------
# Chain collection — explicit registry, parents-first, cycle-detected
# ----------------------------------------------------------------------

def _collect_chain(
    target_id: str,
    registry: Mapping[str, Object],
    layer_type: type[T],
) -> list[T]:
    """
    Walk the explicit parent slot of ``layer_type`` from ``target_id``, returning
    instances in deterministic parents-first order with duplicates removed.

    Raises ``CompositionError`` on an unknown id, a type mismatch, a disallowed
    composition mode, or a cycle.
    """
    parent_attr = _PARENT_ATTR[layer_type]
    allowed = _ALLOWED_MODES[layer_type]
    order: list[T] = []
    done: set[str] = set()
    visiting: set[str] = set()

    def visit(node_id: str) -> None:
        if node_id in done:
            return
        if node_id in visiting:
            raise CompositionError(f"composition cycle detected at {node_id!r}")
        node = registry.get(node_id)
        if node is None:
            raise CompositionError(f"unknown layer id: {node_id!r}")
        if not isinstance(node, layer_type):
            raise CompositionError(
                f"id {node_id!r} is {type(node).__name__}, expected {layer_type.__name__}"
            )
        # composition_mode is stored as its string value (use_enum_values=True);
        # str-enum equality keeps membership checks against CompositionMode valid.
        mode = node.composition_mode or CompositionMode.additive
        if mode not in allowed:
            raise CompositionError(
                f"{layer_type.__name__} {node_id!r} declares composition_mode "
                f"{str(mode)!r}, which it does not support"
            )
        visiting.add(node_id)
        for parent_id in getattr(node, parent_attr) or []:
            visit(parent_id)
        visiting.discard(node_id)
        done.add(node_id)
        order.append(node)

    visit(target_id)
    return order


# ----------------------------------------------------------------------
# Field-local merge primitives
# ----------------------------------------------------------------------

def _ref_key(ref: ContentReference) -> tuple[str, str, str]:
    return (ref.uri, ref.sha256, str(ref.hash_mode))


def _append_dedup(
    acc: Sequence,
    new: Iterable,
    key: Callable,
) -> list:
    out = list(acc)
    seen = {key(x) for x in out}
    for item in new:
        k = key(item)
        if k not in seen:
            seen.add(k)
            out.append(item)
    return out


def _merge_list(acc: list, new, mode: CompositionMode, key: Callable) -> list:
    """additive/restrictive -> union+dedup; overriding -> child replaces; isolated -> child only."""
    new_list = list(new or [])
    if mode == CompositionMode.isolated:
        return new_list
    if mode == CompositionMode.overriding:
        return new_list if (new is not None) else list(acc)
    return _append_dedup(acc, new_list, key)


def _merge_scalar(acc, new, mode: CompositionMode):
    """isolated -> child only; otherwise most-derived non-null wins."""
    if mode == CompositionMode.isolated:
        return new
    return new if new is not None else acc


def _or_bool(acc: bool | None, new: bool | None) -> bool | None:
    if acc is None:
        return new
    if new is None:
        return acc
    return acc or new


def _and_bool(acc: bool | None, new: bool | None) -> bool | None:
    if acc is None:
        return new
    if new is None:
        return acc
    return acc and new


def _merge_allow_bool(acc, new, mode: CompositionMode):
    """Permission flags: AND under restrictive (narrowing), OR under additive."""
    if mode == CompositionMode.isolated:
        return new
    if mode == CompositionMode.overriding:
        return new if new is not None else acc
    if mode == CompositionMode.restrictive:
        return _and_bool(acc, new)
    return _or_bool(acc, new)


def _merge_tighten_bool(acc, new, mode: CompositionMode):
    """Preservation/grounding flags only tighten: OR (except explicit override)."""
    if mode == CompositionMode.isolated:
        return new
    if mode == CompositionMode.overriding:
        return new if new is not None else acc
    return _or_bool(acc, new)


def _str_key(s: str) -> str:
    return s


# ----------------------------------------------------------------------
# Per-layer chain resolution
# ----------------------------------------------------------------------

def resolve_viewpoint(target_id: str, registry: Mapping[str, Object]) -> ViewpointDirective:
    """Fold a ViewpointDirective's parent chain into a single resolved directive."""
    chain = _collect_chain(target_id, registry, ViewpointDirective)
    leaf = chain[-1]

    prompts: list = []
    exemplars: list = []
    vocabulary_refs: list = []
    imposed: list = []
    should_not_claim: list = []
    target_schema = None
    directive_name = None
    scope = None
    summary = None

    for node in chain:
        mode = node.composition_mode or CompositionMode.additive
        prompts = _merge_list(prompts, node.prompts, mode, _ref_key)
        exemplars = _merge_list(exemplars, node.exemplars, mode, _ref_key)
        vocabulary_refs = _merge_list(vocabulary_refs, node.vocabulary_refs, mode, _ref_key)
        imposed = _merge_list(imposed, node.imposed_should_not_claim, mode, _str_key)
        should_not_claim = _merge_list(should_not_claim, node.should_not_claim, mode, _str_key)
        target_schema = _merge_scalar(target_schema, node.target_schema, mode)
        directive_name = _merge_scalar(directive_name, node.directive_name, mode)
        scope = _merge_scalar(scope, node.scope, mode)
        summary = _merge_scalar(summary, node.summary, mode)

    return ViewpointDirective(
        id=leaf.id,
        type=leaf.type,
        viewpoint_directive_id=leaf.viewpoint_directive_id,
        provenance=_resolution_provenance(chain),
        should_not_claim=should_not_claim or list(leaf.should_not_claim or []),
        directive_name=directive_name or leaf.directive_name,
        parent_viewpoint_ids=[n.id for n in chain[:-1]],
        prompts=prompts or None,
        exemplars=exemplars or None,
        vocabulary_refs=vocabulary_refs or None,
        target_schema=target_schema,
        imposed_should_not_claim=imposed or None,
        scope=scope,
        summary=summary,
    )


def resolve_extraction_profile(
    target_id: str, registry: Mapping[str, Object]
) -> ExtractionProfile:
    """Fold an ExtractionProfile's parent chain into a single resolved profile."""
    chain = _collect_chain(target_id, registry, ExtractionProfile)
    leaf = chain[-1]

    should_not_claim: list = []
    preserve_kinds: list = []
    grounding_kinds: list = []
    high_fidelity_kinds: list = []
    granularity = None
    evidence_density = None
    locator_fidelity = None
    preserve_numeric = None
    preserve_uncertainty = None
    require_char = None

    for node in chain:
        mode = node.composition_mode or CompositionMode.additive
        should_not_claim = _merge_list(should_not_claim, node.should_not_claim, mode, _str_key)
        preserve_kinds = _merge_list(preserve_kinds, node.preserve_content_kinds, mode, _str_key)
        grounding_kinds = _merge_list(
            grounding_kinds, node.require_grounding_for_content_kinds, mode, _str_key
        )
        high_fidelity_kinds = _merge_list(
            high_fidelity_kinds, node.high_fidelity_content_kinds, mode, _str_key
        )
        granularity = _merge_scalar(granularity, node.granularity, mode)
        evidence_density = _merge_scalar(evidence_density, node.evidence_density, mode)
        locator_fidelity = _merge_scalar(locator_fidelity, node.locator_fidelity, mode)
        preserve_numeric = _merge_tighten_bool(preserve_numeric, node.preserve_numeric_values, mode)
        preserve_uncertainty = _merge_tighten_bool(
            preserve_uncertainty, node.preserve_uncertainty_language, mode
        )
        require_char = _merge_tighten_bool(require_char, node.require_char_level_locators, mode)

    return ExtractionProfile(
        id=leaf.id,
        type=leaf.type,
        viewpoint_directive_id=leaf.viewpoint_directive_id,
        provenance=_resolution_provenance(chain),
        should_not_claim=should_not_claim or list(leaf.should_not_claim or []),
        layer_name=leaf.layer_name,
        parent_extraction_profile_ids=[n.id for n in chain[:-1]],
        granularity=granularity,
        evidence_density=evidence_density,
        locator_fidelity=locator_fidelity,
        preserve_numeric_values=preserve_numeric,
        preserve_uncertainty_language=preserve_uncertainty,
        require_char_level_locators=require_char,
        preserve_content_kinds=preserve_kinds or None,
        require_grounding_for_content_kinds=grounding_kinds or None,
        high_fidelity_content_kinds=high_fidelity_kinds or None,
    )


def resolve_vocabulary_pack(target_id: str, registry: Mapping[str, Object]) -> VocabularyPack:
    """Fold a VocabularyPack's parent chain into a single resolved pack."""
    chain = _collect_chain(target_id, registry, VocabularyPack)
    leaf = chain[-1]

    should_not_claim: list = []
    vocabulary_refs: list = []
    ontology_refs: list = []
    active_namespaces: list = []

    for node in chain:
        mode = node.composition_mode or CompositionMode.additive
        should_not_claim = _merge_list(should_not_claim, node.should_not_claim, mode, _str_key)
        vocabulary_refs = _merge_list(vocabulary_refs, node.vocabulary_refs, mode, _ref_key)
        ontology_refs = _merge_list(ontology_refs, node.ontology_refs, mode, _ref_key)
        active_namespaces = _merge_list(active_namespaces, node.active_namespaces, mode, _str_key)

    return VocabularyPack(
        id=leaf.id,
        type=leaf.type,
        viewpoint_directive_id=leaf.viewpoint_directive_id,
        provenance=_resolution_provenance(chain),
        should_not_claim=should_not_claim or list(leaf.should_not_claim or []),
        layer_name=leaf.layer_name,
        parent_vocabulary_pack_ids=[n.id for n in chain[:-1]],
        vocabulary_refs=vocabulary_refs or None,
        ontology_refs=ontology_refs or None,
        active_namespaces=active_namespaces or None,
    )


def resolve_reasoning_policy(target_id: str, registry: Mapping[str, Object]) -> ReasoningPolicy:
    """Fold a ReasoningPolicy's parent chain into a single resolved policy."""
    chain = _collect_chain(target_id, registry, ReasoningPolicy)
    leaf = chain[-1]

    should_not_claim: list = []
    allow_speculative = None
    allow_cross_doc = None
    allow_normalization = None
    enable_adjudication = None
    notes = None

    for node in chain:
        mode = node.composition_mode or CompositionMode.additive
        should_not_claim = _merge_list(should_not_claim, node.should_not_claim, mode, _str_key)
        allow_speculative = _merge_allow_bool(allow_speculative, node.allow_speculative_inference, mode)
        allow_cross_doc = _merge_allow_bool(allow_cross_doc, node.allow_cross_document_synthesis, mode)
        allow_normalization = _merge_allow_bool(
            allow_normalization, node.allow_ontology_normalization, mode
        )
        enable_adjudication = _merge_tighten_bool(
            enable_adjudication, node.enable_contradiction_adjudication, mode
        )
        notes = _merge_scalar(notes, node.notes, mode)

    return ReasoningPolicy(
        id=leaf.id,
        type=leaf.type,
        viewpoint_directive_id=leaf.viewpoint_directive_id,
        provenance=_resolution_provenance(chain),
        should_not_claim=should_not_claim or list(leaf.should_not_claim or []),
        layer_name=leaf.layer_name,
        parent_reasoning_policy_ids=[n.id for n in chain[:-1]],
        allow_speculative_inference=allow_speculative,
        allow_cross_document_synthesis=allow_cross_doc,
        allow_ontology_normalization=allow_normalization,
        enable_contradiction_adjudication=enable_adjudication,
        notes=notes,
    )


# ----------------------------------------------------------------------
# Top-level composition
# ----------------------------------------------------------------------

def _resolution_provenance(chain: Sequence[Object]) -> str:
    return "Resolved by composition of: " + ", ".join(n.id for n in chain)


def _composed_id(
    viewpoint_ids: list[str],
    extraction_profile_ids: list[str],
    vocabulary_pack_ids: list[str],
    reasoning_policy_ids: list[str],
) -> str:
    payload = json.dumps(
        {
            "viewpoint": viewpoint_ids,
            "extraction_profile": extraction_profile_ids,
            "vocabulary_pack": vocabulary_pack_ids,
            "reasoning_policy": reasoning_policy_ids,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:8]
    return f"vpt:composed:{digest}"


def compose_viewpoint(
    viewpoint_id: str,
    registry: Mapping[str, Object],
    *,
    extraction_profile_id: str | None = None,
    vocabulary_pack_id: str | None = None,
    reasoning_policy_id: str | None = None,
) -> ComposedViewpointDirective:
    """
    Resolve a viewpoint directive together with optional extraction profile,
    vocabulary pack, and reasoning policy layers into one frozen
    ``ComposedViewpointDirective``.

    Each layer is resolved over its own explicit parent chain (see the
    ``resolve_*`` helpers). The result inlines the resolved operational layers
    and records the flattened, parents-first source-id chains. The composed id
    is deterministic in those chains, so identical inputs yield an identical
    (and identically hashed) artifact.
    """
    resolved_viewpoint = resolve_viewpoint(viewpoint_id, registry)
    viewpoint_chain = _collect_chain(viewpoint_id, registry, ViewpointDirective)
    source_viewpoint_ids = [n.id for n in viewpoint_chain]

    resolved_extraction = None
    source_extraction_ids: list[str] = []
    if extraction_profile_id is not None:
        resolved_extraction = resolve_extraction_profile(extraction_profile_id, registry)
        source_extraction_ids = [
            n.id for n in _collect_chain(extraction_profile_id, registry, ExtractionProfile)
        ]

    resolved_vocabulary = None
    source_vocabulary_ids: list[str] = []
    if vocabulary_pack_id is not None:
        resolved_vocabulary = resolve_vocabulary_pack(vocabulary_pack_id, registry)
        source_vocabulary_ids = [
            n.id for n in _collect_chain(vocabulary_pack_id, registry, VocabularyPack)
        ]

    resolved_reasoning = None
    source_reasoning_ids: list[str] = []
    if reasoning_policy_id is not None:
        resolved_reasoning = resolve_reasoning_policy(reasoning_policy_id, registry)
        source_reasoning_ids = [
            n.id for n in _collect_chain(reasoning_policy_id, registry, ReasoningPolicy)
        ]

    composed_id = _composed_id(
        source_viewpoint_ids,
        source_extraction_ids,
        source_vocabulary_ids,
        source_reasoning_ids,
    )

    return ComposedViewpointDirective(
        id=composed_id,
        type=resolved_viewpoint.type,
        viewpoint_directive_id=resolved_viewpoint.viewpoint_directive_id,
        provenance=resolved_viewpoint.provenance,
        should_not_claim=resolved_viewpoint.should_not_claim,
        directive_name=resolved_viewpoint.directive_name,
        prompts=resolved_viewpoint.prompts,
        exemplars=resolved_viewpoint.exemplars,
        vocabulary_refs=resolved_viewpoint.vocabulary_refs,
        target_schema=resolved_viewpoint.target_schema,
        imposed_should_not_claim=resolved_viewpoint.imposed_should_not_claim,
        scope=resolved_viewpoint.scope,
        summary=resolved_viewpoint.summary,
        resolved_extraction_profile=resolved_extraction,
        resolved_vocabulary_pack=resolved_vocabulary,
        resolved_reasoning_policy=resolved_reasoning,
        source_viewpoint_ids=source_viewpoint_ids,
        source_extraction_profile_ids=source_extraction_ids or None,
        source_vocabulary_pack_ids=source_vocabulary_ids or None,
        source_reasoning_policy_ids=source_reasoning_ids or None,
    )
