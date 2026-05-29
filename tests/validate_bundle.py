#!/usr/bin/env python3
"""Validate a pygrits bundle YAML against the schema."""
import sys

sys.path.insert(0, "src")
import yaml

from pygrits.core import (
    Activity,
    ComposedViewpointDirective,
    EvidenceRecord,
    ExtractionProfile,
    NegativeEvidenceRecord,
    Object,
    ReasoningPolicy,
    ViewpointDirective,
    VocabularyPack,
)


def validate_bundle(path):
    with open(path) as f:
        doc = yaml.safe_load(f)
    errors, ok = [], {}
    checks = [
        ("viewpoints", ViewpointDirective),
        ("extraction_profiles", ExtractionProfile),
        ("vocabulary_packs", VocabularyPack),
        ("reasoning_policies", ReasoningPolicy),
        ("composed_viewpoints", ComposedViewpointDirective),
        ("objects", Object),
        ("activities", Activity),
    ]
    for section, cls in checks:
        for i, item in enumerate(doc.get(section, [])):
            try:
                cls(**item)
                ok[cls.__name__] = ok.get(cls.__name__, 0) + 1
            except Exception as e:
                errors.append(f"{section}[{i}] ({item.get('id', '?')}): {e}")
    for i, item in enumerate(doc.get("evidence_records", [])):
        cls = NegativeEvidenceRecord if "result" in item else EvidenceRecord
        try:
            cls(**item)
            ok[cls.__name__] = ok.get(cls.__name__, 0) + 1
        except Exception as e:
            errors.append(f"evidence_records[{i}] ({item.get('id', '?')}): {e}")
    return ok, errors


if __name__ == "__main__":
    for path in sys.argv[1:]:
        ok, errors = validate_bundle(path)
        total = sum(ok.values())
        print(f"=== {path} ===")
        for k, v in sorted(ok.items()):
            print(f"  OK  {k}: {v}")
        print(f"  TOTAL: {total} grits")
        if errors:
            print(f"  ERRORS ({len(errors)}):")
            for e in errors:
                print(f"    {e}")
        else:
            print("  ERRORS: 0")
