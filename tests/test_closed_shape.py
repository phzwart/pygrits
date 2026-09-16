from __future__ import annotations

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from pygrits import (
    Activity,
    Bundle,
    Entity,
    Plan,
    context_path,
    load,
    profile_path,
    profile_text,
    schema_path,
)

_HEX = "a" * 64


def test_extra_field_on_entity_fails() -> None:
    with pytest.raises(ValidationError):
        Entity(id="ent:t", plan="plan:t", nonsense="no")


def test_missing_plan_on_entity_fails() -> None:
    with pytest.raises(ValidationError):
        Entity(id="ent:t", summary="x")


def test_missing_used_on_activity_fails() -> None:
    with pytest.raises(ValidationError):
        Activity(id="act:t", plan="plan:t", kind="derivation")


def test_unknown_node_type_fails() -> None:
    with pytest.raises(ValueError, match="unknown node"):
        Bundle.model_validate(
            {
                "@context": "pygrits/context.jsonld",
                "@graph": [{"@id": "x:t", "@type": "prov:Agent", "name": "no"}],
            }
        )


def test_unknown_selector_type_fails() -> None:
    with pytest.raises(ValueError, match="unknown selector"):
        Entity.model_validate(
            {
                "@id": "evi:t",
                "@type": "prov:Entity",
                "plan": "plan:t",
                "target": {"selector": {"@type": "oa:LineRangeSelector", "path": "x"}},
            }
        )


def test_malformed_sha256_fails() -> None:
    with pytest.raises(ValidationError):
        Plan(id="plan:t", name="t", prompt_digest="not-a-hash", schema_digest=_HEX)


def test_load_json_string() -> None:
    raw = json.dumps(
        {
            "@context": "pygrits/context.jsonld",
            "@graph": [
                {
                    "@id": "plan:t",
                    "@type": "prov:Plan",
                    "name": "t",
                    "prompt_digest": _HEX,
                    "schema_digest": _HEX,
                }
            ],
        }
    )
    bundle = load(raw)
    assert bundle.graph[0].id == "plan:t"


def test_profile_is_the_directive() -> None:
    text = profile_text()
    assert "prov:Entity" in text
    assert "prov:Activity" in text
    assert "prov:Plan" in text
    assert "oa:TextQuoteSelector" in text
    assert "result" in text
    root = Path(__file__).parent.parent / "PROFILE.md"
    assert root.read_text(encoding="utf-8") == profile_path().read_text(encoding="utf-8")


def test_context_only_uses_existing_vocabs() -> None:
    ctx = json.loads(context_path().read_text())["@context"]
    allowed = {
        "http://www.w3.org/ns/prov#",
        "http://www.w3.org/ns/oa#",
        "http://purl.org/dc/terms/",
        "http://www.w3.org/2001/XMLSchema#",
        "http://schema.org/",
    }
    iris = []
    for value in ctx.values():
        if isinstance(value, str) and value.startswith("http"):
            iris.append(value)
        elif isinstance(value, dict):
            iri = value.get("@id", "")
            if iri.startswith("http"):
                iris.append(iri)
    for iri in iris:
        assert any(iri.startswith(base) for base in allowed), iri
    assert "w3id.org/grits" not in json.dumps(ctx)


def test_schema_is_closed() -> None:
    schema = json.loads(schema_path().read_text())
    assert schema["additionalProperties"] is False
    assert schema["$defs"]["entity"]["allOf"][1]["additionalProperties"] is False
