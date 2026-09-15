"""RDF export (requires pygrits[rdf])."""

from __future__ import annotations

import json
from collections.abc import Iterable
from importlib import resources
from pathlib import Path

from linkml_runtime.dumpers.rdflib_dumper import RDFLibDumper
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph

from pygrits.core import Grit
from pygrits.resources import schema_path

_ID_PREFIXES = {
    p: f"https://w3id.org/grits/id/{p}/"
    for p in ("act", "ent", "evi", "obj", "src", "vpt")
}


def _prefix_map() -> dict[str, str]:
    with resources.as_file(resources.files("pygrits").joinpath("core.context.jsonld")) as p:
        ctx = json.loads(Path(p).read_text()).get("@context") or {}
    out = {k: v for k, v in ctx.items() if not k.startswith("@") and isinstance(v, str) and v.startswith("http")}
    out.update(_ID_PREFIXES)
    return out


def to_graph(grits: Iterable[Grit]) -> Graph:
    sv = SchemaView(schema_path())
    dumper = RDFLibDumper()
    pm = _prefix_map()
    merged = Graph()
    for grit in grits:
        g = dumper.as_rdf_graph(grit, sv, prefix_map=pm)
        for t in g:
            merged.add(t)
    return merged
