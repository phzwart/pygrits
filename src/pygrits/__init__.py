"""pygrits — closed PROV-O + Web Annotation emit profile and validator."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pygrits.canonical import (
    canonical_bytes_for_instance,
    canonical_hash_bytes,
    canonical_hash_instance,
    compute_content_hash,
    stamp,
    verify_content_reference,
)
from pygrits.models import (
    Activity,
    Bundle,
    ContentRef,
    DataPositionSelector,
    Entity,
    FragmentSelector,
    Plan,
    Target,
    TextPositionSelector,
    TextQuoteSelector,
    parse_node,
)
from pygrits.resources import context_path, profile_path, profile_text, schema_path
from pygrits.validate import BundleValidationError, validate, validate_bundle

__version__ = "0.6.1"


def load(src: str | Path | dict[str, Any]) -> Bundle:
    if isinstance(src, dict):
        return Bundle.model_validate(src)
    path = Path(src)
    if path.exists():
        return Bundle.model_validate(json.loads(path.read_text(encoding="utf-8")))
    return Bundle.model_validate(json.loads(src))


def dump(bundle: Bundle, path: str | Path | None = None) -> dict[str, Any]:
    data = bundle.model_dump(mode="json", by_alias=True, exclude_none=True)
    if path is not None:
        Path(path).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return data


__all__ = [
    "__version__",
    "Activity",
    "Bundle",
    "BundleValidationError",
    "ContentRef",
    "DataPositionSelector",
    "Entity",
    "FragmentSelector",
    "Plan",
    "Target",
    "TextPositionSelector",
    "TextQuoteSelector",
    "canonical_bytes_for_instance",
    "canonical_hash_bytes",
    "canonical_hash_instance",
    "compute_content_hash",
    "context_path",
    "dump",
    "load",
    "parse_node",
    "profile_path",
    "profile_text",
    "schema_path",
    "stamp",
    "validate",
    "validate_bundle",
    "verify_content_reference",
]
