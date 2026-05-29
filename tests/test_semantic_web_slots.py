"""
Tests for the semantic-web slots: instance_of, abstraction_level, payload_schema.

These slots connect grits to external ontologies. They are optional and purely
additive in v1; absence must never break validation.
"""

from __future__ import annotations

from pygrits.core import (
    CharRangeLocator,
    ContentReference,
    EvidenceRecord,
    HashMode,
    Object,
    ViewpointDirective,
)


def test_object_instance_of_accepts_curies():
    obj = Object(
        id="obj:test-instance-of-v1",
        type="grits:test",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="test",
        should_not_claim=["test"],
        source_artifact_refs=[],
        evidence_record_ids=[],
        instance_of=["CHMO:0000823", "OBI:0000070"],
    )
    assert obj.instance_of == ["CHMO:0000823", "OBI:0000070"]


def test_object_instance_of_is_optional():
    obj = Object(
        id="obj:test-no-instance-of-v1",
        type="grits:test",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="test",
        should_not_claim=["test"],
        source_artifact_refs=[],
        evidence_record_ids=[],
    )
    assert obj.instance_of is None or obj.instance_of == []


def test_evidence_record_instance_of_accepts_curies():
    evi = EvidenceRecord(
        id="evi:test-instance-of-v1",
        type="grits:test",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="test",
        should_not_claim=["test"],
        source_artifact_ref=ContentReference(
            uri="file://test",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        ),
        locator=CharRangeLocator(
            locator_type="CharRangeLocator",
            char_start=0,
            char_end=10,
        ),
        instance_of=["OBI:0000070"],
    )
    assert evi.instance_of == ["OBI:0000070"]


def test_viewpoint_abstraction_level_accepts_curie():
    vpt = ViewpointDirective(
        id="vpt:test-abstract-v1",
        type="grits:viewpoint_directive",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="test",
        should_not_claim=["test"],
        source_artifact_refs=[],
        evidence_record_ids=[],
        directive_name="TestAbstractView",
        abstraction_level="CHMO:0000823",
    )
    assert vpt.abstraction_level == "CHMO:0000823"


def test_viewpoint_abstraction_level_is_optional():
    vpt = ViewpointDirective(
        id="vpt:test-no-abstract-v1",
        type="grits:viewpoint_directive",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="test",
        should_not_claim=["test"],
        source_artifact_refs=[],
        evidence_record_ids=[],
        directive_name="TestView",
    )
    assert vpt.abstraction_level is None


def test_evidence_record_payload_schema():
    schema_ref = ContentReference(
        uri="file://schemas/raman-observation-v1.yaml",
        sha256="b" * 64,
        hash_mode=HashMode.raw_bytes,
    )
    evi = EvidenceRecord(
        id="evi:test-payload-schema-v1",
        type="grits:test",
        viewpoint_directive_id="vpt:meta-v0",
        provenance="test",
        should_not_claim=["test"],
        source_artifact_ref=ContentReference(
            uri="file://test",
            sha256="a" * 64,
            hash_mode=HashMode.raw_bytes,
        ),
        locator=CharRangeLocator(
            locator_type="CharRangeLocator",
            char_start=0,
            char_end=10,
        ),
        payload_schema=schema_ref,
    )
    assert evi.payload_schema.uri == "file://schemas/raman-observation-v1.yaml"
