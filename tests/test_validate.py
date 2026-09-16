from __future__ import annotations

from pathlib import Path

import pytest

from pygrits import (
    Activity,
    BundleValidationError,
    ContentRef,
    Entity,
    Plan,
    Target,
    TextQuoteSelector,
    load,
    validate,
)

EXAMPLES = Path(__file__).parent.parent / "examples"

_HEX_A = "a" * 64
_HEX_B = "b" * 64
_HEX_C = "c" * 64


def _plan() -> Plan:
    return Plan(
        id="plan:t",
        name="t",
        prompt_digest=_HEX_A,
        schema_digest=_HEX_C,
    )


def _quote(eid: str = "evi:q") -> Entity:
    return Entity(
        id=eid,
        plan="plan:t",
        how="quote",
        source=ContentRef(uri="file://p.txt", sha256=_HEX_B),
        target=Target(selector=TextQuoteSelector(exact="said this")),
    )


def test_example_passes() -> None:
    validate(load(EXAMPLES / "kcat.jsonld"))


def test_dangling_used_fails() -> None:
    with pytest.raises(BundleValidationError, match="missing id"):
        validate(
            [
                _plan(),
                Activity(
                    id="act:s",
                    plan="plan:t",
                    kind="support",
                    used=["ent:missing"],
                ),
            ]
        )


def test_plan_must_be_a_plan() -> None:
    other = Entity(id="ent:not-a-plan", plan="plan:t", summary="x")
    with pytest.raises(BundleValidationError, match="not a prov:Plan"):
        validate(
            [
                _plan(),
                other,
                Entity(id="ent:y", plan="ent:not-a-plan", summary="y"),
            ]
        )


def test_inferred_without_rationale_fails() -> None:
    with pytest.raises(BundleValidationError, match="requires rationale"):
        validate(
            [
                _plan(),
                Entity(id="ent:y", plan="plan:t", how="inferred"),
            ]
        )


def test_quote_without_target_fails() -> None:
    with pytest.raises(BundleValidationError, match="quote requires"):
        validate(
            [
                _plan(),
                Entity(
                    id="evi:q",
                    plan="plan:t",
                    how="quote",
                    source=ContentRef(uri="file://p.txt", sha256=_HEX_B),
                ),
            ]
        )


def test_support_with_generated_fails() -> None:
    with pytest.raises(BundleValidationError, match="must not have generated"):
        validate(
            [
                _plan(),
                _quote(),
                Entity(id="ent:b", plan="plan:t"),
                Activity(
                    id="act:s",
                    plan="plan:t",
                    kind="support",
                    used=["evi:q"],
                    generated=["ent:b"],
                ),
            ]
        )


def test_duplicate_id_fails() -> None:
    with pytest.raises(BundleValidationError, match="duplicate"):
        validate([_plan(), Plan(id="plan:t", name="other", prompt_digest=_HEX_A, schema_digest=_HEX_C)])


def test_adjudication_without_rationale_fails() -> None:
    with pytest.raises(BundleValidationError, match="adjudication requires rationale"):
        validate(
            [
                _plan(),
                _quote(),
                Entity(id="ent:b", plan="plan:t"),
                Activity(
                    id="act:a",
                    plan="plan:t",
                    kind="adjudication",
                    used=["evi:q"],
                    generated=["ent:b"],
                ),
            ]
        )


def test_result_without_summary_fails() -> None:
    with pytest.raises(BundleValidationError, match="result requires summary"):
        validate(
            [
                _plan(),
                Entity(id="evi:none", plan="plan:t", result="absent"),
            ]
        )
