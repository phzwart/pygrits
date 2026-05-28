"""
Regression guard: core must not define coordination-shaped social slots.

Those slots live in pygrits.viewpoints.coordination_v0 instead.
"""

from __future__ import annotations

from pygrits.resources import schema_path

FORBIDDEN_SLOT_NAMES = (
    "needs",
    "offers",
    "affordances",
    "wiki_link_ids",
    "action_link_ids",
    "gaps",
)


def test_core_yaml_has_no_social_coordination_slots() -> None:
    text = schema_path().read_text()
    for name in FORBIDDEN_SLOT_NAMES:
        assert f"{name}:" not in text, (
            f"core.yaml must not define social/coordination slot {name!r}"
        )


def test_core_module_has_no_social_coordination_slots() -> None:
    import pygrits.core as core

    for name in FORBIDDEN_SLOT_NAMES:
        assert not hasattr(core.Object, name), (
            f"core Object must not expose slot {name!r}"
        )
