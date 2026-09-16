"""Closed emit shapes. Field names are the JSON keys; @context maps the PROV/OA ones."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

_ID = r"^[a-z]+:[A-Za-z0-9._:-]+$"
_SHA256 = r"^[a-f0-9]{64}$"

How = Literal["quote", "derived", "inferred", "unknown"]
Result = Literal["absent", "weak", "excluded", "inconclusive"]
Kind = Literal["derivation", "support", "contradiction", "adjudication"]


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class ContentRef(_Strict):
    """Content-addressed artifact. sha256 is hex of the raw bytes."""

    uri: str
    sha256: str = Field(pattern=_SHA256)
    media_type: str | None = None


class TextQuoteSelector(_Strict):
    type: Literal["oa:TextQuoteSelector"] = Field(default="oa:TextQuoteSelector", alias="@type")
    exact: str
    prefix: str | None = None
    suffix: str | None = None


class TextPositionSelector(_Strict):
    type: Literal["oa:TextPositionSelector"] = Field(
        default="oa:TextPositionSelector", alias="@type"
    )
    start: int = Field(ge=0)
    end: int = Field(ge=0)


class DataPositionSelector(_Strict):
    type: Literal["oa:DataPositionSelector"] = Field(
        default="oa:DataPositionSelector", alias="@type"
    )
    start: int = Field(ge=0)
    end: int = Field(ge=0)


class FragmentSelector(_Strict):
    type: Literal["oa:FragmentSelector"] = Field(default="oa:FragmentSelector", alias="@type")
    value: str
    conforms_to: str | None = Field(default=None, alias="conformsTo")


Selector = TextQuoteSelector | TextPositionSelector | DataPositionSelector | FragmentSelector

_SELECTOR_TYPES: dict[str, type[Selector]] = {
    "oa:TextQuoteSelector": TextQuoteSelector,
    "oa:TextPositionSelector": TextPositionSelector,
    "oa:DataPositionSelector": DataPositionSelector,
    "oa:FragmentSelector": FragmentSelector,
}


def parse_selector(data: dict[str, Any] | Selector) -> Selector:
    if isinstance(data, _Strict):
        return data  # type: ignore[return-value]
    raw_type = data.get("@type", data.get("type"))
    cls = _SELECTOR_TYPES.get(raw_type) if isinstance(raw_type, str) else None
    if cls is None:
        raise ValueError(f"unknown selector @type: {raw_type!r}")
    return cls.model_validate(data)


class Target(_Strict):
    has_source: str | None = Field(default=None, alias="hasSource")
    selector: Selector

    @model_validator(mode="before")
    @classmethod
    def _coerce_selector(cls, data: Any) -> Any:
        if isinstance(data, dict) and isinstance(data.get("selector"), dict):
            data = {**data, "selector": parse_selector(data["selector"])}
        return data


class NodeBase(_Strict):
    id: str = Field(alias="@id", pattern=_ID)
    content_hash: str | None = Field(default=None, pattern=_SHA256)
    agent: str | None = None


class Plan(NodeBase):
    type: Literal["prov:Plan"] = Field(default="prov:Plan", alias="@type")
    name: str
    prompt_digest: str = Field(pattern=_SHA256)
    schema_digest: str = Field(pattern=_SHA256)


class Entity(NodeBase):
    type: Literal["prov:Entity"] = Field(default="prov:Entity", alias="@type")
    plan: str = Field(pattern=_ID)
    source: ContentRef | None = None
    target: Target | None = None
    how: How | None = None
    rationale: str | None = None
    result: Result | None = None
    payload: str | None = None
    summary: str | None = None


class Activity(NodeBase):
    type: Literal["prov:Activity"] = Field(default="prov:Activity", alias="@type")
    plan: str = Field(pattern=_ID)
    kind: Kind
    used: list[str] = Field(min_length=1)
    generated: list[str] = Field(default_factory=list)


Node = Plan | Entity | Activity

_NODE_TYPES: dict[str, type[Node]] = {
    "prov:Plan": Plan,
    "prov:Entity": Entity,
    "prov:Activity": Activity,
}


def parse_node(data: dict[str, Any] | Node) -> Node:
    if isinstance(data, NodeBase):
        return data  # type: ignore[return-value]
    raw_type = data.get("@type", data.get("type"))
    cls = _NODE_TYPES.get(raw_type) if isinstance(raw_type, str) else None
    if cls is None:
        raise ValueError(f"unknown node @type: {raw_type!r}")
    return cls.model_validate(data)


class Bundle(_Strict):
    context: Any = Field(alias="@context")
    graph: list[Node] = Field(alias="@graph", min_length=1)

    @model_validator(mode="before")
    @classmethod
    def _coerce_graph(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data
        key = "@graph" if "@graph" in data else "graph" if "graph" in data else None
        if key is None:
            return data
        nodes = data[key]
        if isinstance(nodes, list):
            data = {**data, key: [parse_node(n) if isinstance(n, dict) else n for n in nodes]}
        return data
