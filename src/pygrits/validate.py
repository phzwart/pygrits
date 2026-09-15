"""Bundle referential integrity and semantic checks."""

from __future__ import annotations

import re
from collections.abc import Iterable

from pygrits.core import (
    Activity,
    ActivityType,
    ContentReference,
    Entity,
    EvidenceLabel,
    EvidenceRecord,
    Grit,
    ViewpointDirective,
)

_SHA256 = re.compile(r"^[a-f0-9]{64}$")


class BundleValidationError(ValueError):
    pass

def _content_refs(grit: Grit) -> list[ContentReference]:
    refs: list[ContentReference] = []
    if isinstance(grit, Entity):
        refs.extend(grit.sources or [])
    if isinstance(grit, EvidenceRecord):
        refs.append(grit.source)
    if isinstance(grit, ViewpointDirective):
        refs.extend(grit.prompts or [])
        refs.extend(grit.exemplars or [])
        refs.extend(grit.vocabularies or [])
        if grit.target_schema:
            refs.append(grit.target_schema)
    return refs


def _referenced_ids(grit: Grit) -> set[str]:
    refs = {grit.viewpoint_id}
    if grit.generated_by:
        refs.add(grit.generated_by)
    if isinstance(grit, Entity):
        refs.update(grit.derived_from or [])
        refs.update(link.evidence_id for link in grit.evidence or [])
    if isinstance(grit, Activity):
        refs.update(grit.inputs)
        refs.update(grit.outputs or [])
    return refs


def validate_bundle(grits: Iterable[Grit]) -> None:
    grit_list = list(grits)
    ids = {g.id for g in grit_list}
    for grit in grit_list:
        for ref in _content_refs(grit):
            if not _SHA256.fullmatch(ref.sha256):
                raise BundleValidationError(f"{grit.id}: invalid ContentReference sha256")
        for ref in _referenced_ids(grit):
            if ref not in ids:
                raise BundleValidationError(f"{grit.id}: missing id {ref!r} in bundle")
        if isinstance(grit, Entity):
            for link in grit.evidence or []:
                if link.label in (EvidenceLabel.derived, EvidenceLabel.inferred):
                    if not (link.rationale and link.rationale.strip()):
                        raise BundleValidationError(
                            f"{grit.id}: {link.label} evidence link requires rationale"
                        )
        if isinstance(grit, Activity) and grit.activity_type in (
            ActivityType.support,
            ActivityType.contradiction,
        ) and grit.outputs:
            raise BundleValidationError(f"{grit.id}: {grit.activity_type} must not have outputs")
