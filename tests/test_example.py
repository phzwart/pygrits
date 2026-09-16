from __future__ import annotations

from pathlib import Path

from pygrits import dump, load, stamp, validate
from pygrits.models import Activity, Entity, Plan

EXAMPLES = Path(__file__).parent.parent / "examples"


def test_kcat_bundle_validates() -> None:
    bundle = load(EXAMPLES / "kcat.jsonld")
    validate(bundle)
    assert [type(n) for n in bundle.graph] == [Plan, Entity, Entity, Activity, Entity]
    activity = bundle.graph[3]
    assert isinstance(activity, Activity)
    assert activity.generated == ["ent:landscape"]
    assert "evi:s1" in activity.used


def test_dump_roundtrip() -> None:
    bundle = load(EXAMPLES / "kcat.jsonld")
    again = load(dump(bundle))
    assert [n.id for n in again.graph] == [n.id for n in bundle.graph]


def test_stamp_example() -> None:
    bundle = load(EXAMPLES / "kcat.jsonld")
    stamped = stamp(bundle)
    validate(stamped)
    for node in stamped.graph:
        assert node.content_hash is not None
