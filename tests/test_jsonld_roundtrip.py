"""JSON-LD expansion must keep every profile key."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pyld import jsonld

from pygrits import context_path, dump, load, stamp

EXAMPLES = Path(__file__).parent.parent / "examples"

_SKIP_KEYS = {"@context", "@graph", "@id", "@type"}
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"


def _ctx_terms() -> dict[str, Any]:
    return json.loads(context_path().read_text(encoding="utf-8"))["@context"]


def _expand_curie(ctx: dict[str, Any], compact: str) -> str:
    if compact.startswith("http://") or compact.startswith("https://"):
        return compact
    prefix, sep, local = compact.partition(":")
    if sep and prefix in ctx and isinstance(ctx[prefix], str):
        return ctx[prefix] + local
    return compact


def _term_iri(ctx: dict[str, Any], term: str) -> str | None:
    spec = ctx[term]
    if spec == "@id":
        return None
    if isinstance(spec, str):
        return _expand_curie(ctx, spec)
    iri = spec.get("@id")
    if iri == "@id":
        return None
    return _expand_curie(ctx, iri)


def _used_keys(obj: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key not in _SKIP_KEYS:
                keys.add(key)
            keys |= _used_keys(value)
    elif isinstance(obj, list):
        for item in obj:
            keys |= _used_keys(item)
    return keys


def _predicates(node: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("@"):
                if key == "@list":
                    for item in value:
                        found |= _predicates(item)
                continue
            found.add(key)
            found |= _predicates(value)
    elif isinstance(node, list):
        for item in node:
            found |= _predicates(item)
    return found


def _expand_example(data: dict[str, Any]) -> list[Any]:
    ctx = _ctx_terms()
    doc = {**data, "@context": ctx}
    return jsonld.expand(doc)


def test_example_keys_are_all_in_context() -> None:
    ctx = _ctx_terms()
    data = dump(load(EXAMPLES / "kcat.jsonld"))
    missing = _used_keys(data) - set(ctx)
    assert not missing, f"keys missing from context: {sorted(missing)}"


def test_expansion_keeps_every_used_predicate() -> None:
    ctx = _ctx_terms()
    data = dump(load(EXAMPLES / "kcat.jsonld"))
    expected = set()
    for key in _used_keys(data):
        iri = _term_iri(ctx, key)
        if iri is not None:
            expected.add(iri)
    expanded = _expand_example(data)
    got = _predicates(expanded)
    dropped = expected - got
    assert not dropped, f"predicates dropped on expand: {sorted(dropped)}"


def test_source_expands_to_id_and_sha256() -> None:
    ctx = _ctx_terms()
    data = dump(load(EXAMPLES / "kcat.jsonld"))
    expanded = _expand_example(data)
    primary = _expand_curie(ctx, "prov:hadPrimarySource")
    sha256 = _expand_curie(ctx, "grits:sha256")
    sources = []
    for node in expanded:
        for obj in node.get(primary, []):
            sources.append(obj)
    assert sources
    for source in sources:
        assert source.get("@id") == "file://paper.txt"
        assert source[sha256][0]["@value"] == "b" * 64


def test_stamped_content_hash_survives_expansion() -> None:
    ctx = _ctx_terms()
    data = dump(stamp(load(EXAMPLES / "kcat.jsonld")))
    expanded = _expand_example(data)
    hashed = _expand_curie(ctx, "grits:contentHash")
    assert hashed in _predicates(expanded)
