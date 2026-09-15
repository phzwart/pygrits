"""Content hash integrity and stamping behavior."""

from __future__ import annotations

from pathlib import Path

import yaml

from pygrits import Entity, canonical_hash_instance, compute_content_hash, stamp

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def _load_entity() -> Entity:
    with open(EXAMPLES_DIR / "05_entity_kcat_landscape.yaml") as f:
        return Entity(**yaml.safe_load(f))


def test_content_hash_excluded_from_canonical_bytes() -> None:
    base = _load_entity()
    once = stamp(base)
    twice = stamp(once)
    assert once.content_hash == twice.content_hash
    assert canonical_hash_instance(base) == canonical_hash_instance(twice)


def test_stamping_is_idempotent() -> None:
    base = _load_entity()
    assert stamp(base).content_hash == stamp(stamp(base)).content_hash


def test_field_change_changes_content_hash() -> None:
    base = _load_entity()
    h0 = compute_content_hash(base)
    changed = base.model_copy(update={"agent": "other-agent/1.0"})
    assert compute_content_hash(changed) != h0
