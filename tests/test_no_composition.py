"""Guard against re-introducing the 0.4 composition layer."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
FORBIDDEN = (
    "composition_mode",
    "parent_",
    "ExtractionProfile",
    "VocabularyPack",
    "ReasoningPolicy",
)


def test_no_composition_tokens_in_core_and_src() -> None:
    paths = [REPO_ROOT / "src" / "pygrits" / "core.yaml"]
    paths.extend((REPO_ROOT / "src").rglob("*.py"))
    violations: list[str] = []
    for path in paths:
        if path.name == "test_no_composition.py":
            continue
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN:
            if token == "parent_":
                if re.search(r"parent_", text):
                    violations.append(f"{path.relative_to(REPO_ROOT)}: {token}")
            elif token in text:
                violations.append(f"{path.relative_to(REPO_ROOT)}: {token}")
    assert not violations, "Forbidden composition tokens:\n" + "\n".join(sorted(violations))
