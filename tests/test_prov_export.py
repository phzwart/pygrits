"""PROV-O / P-Plan RDF export from the example bundle."""

from __future__ import annotations

from pathlib import Path

import yaml
from rdflib import URIRef
from rdflib.namespace import PROV, RDF

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
PPLAN_CORRESPONDS_TO_STEP = URIRef("http://purl.org/net/p-plan#correspondsToStep")


def _load_bundle():
    from pygrits import (
        Activity,
        Entity,
        EvidenceRecord,
        NegativeEvidenceRecord,
        ViewpointDirective,
    )

    mapping = (
        ("01_viewpoint.yaml", ViewpointDirective),
        ("02_evidence_line_range.yaml", EvidenceRecord),
        ("03_negative_evidence.yaml", NegativeEvidenceRecord),
        ("04_derivation_activity.yaml", Activity),
        ("05_entity_kcat_landscape.yaml", Entity),
    )
    grits = []
    for name, cls in mapping:
        with open(EXAMPLES_DIR / name) as f:
            grits.append(cls(**yaml.safe_load(f)))
    return grits


def test_example_exports_prov_triples() -> None:
    from pygrits.rdf import to_graph

    g = to_graph(_load_bundle())
    assert len(list(g.triples((None, PROV.used, None)))) >= 1
    assert len(list(g.triples((None, PROV.generated, None)))) >= 1
    assert len(list(g.triples((None, PROV.wasGeneratedBy, None)))) >= 1
    assert len(list(g.triples((None, PROV.hadPrimarySource, None)))) >= 1
    assert len(list(g.triples((None, RDF.type, PROV.Entity)))) >= 1

    assert len(list(g.triples((None, PPLAN_CORRESPONDS_TO_STEP, None)))) >= 1
