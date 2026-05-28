"""
Regression guard: zero forbidden legacy schema naming anywhere in the repository.

All schema identity uses pygrits/grits terminology exclusively.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

SCAN_EXTENSIONS = {".yaml", ".py", ".md", ".toml", ".sh", ".yml", ".json"}
SKIP_DIR_NAMES = {".venv", "__pycache__", ".git", ".pytest_cache", ".ruff_cache"}
SKIP_FILES = {"test_no_isom_references.py", "forbidden_patterns.txt"}

# Patterns loaded from forbidden_patterns.txt so this test file stays clean.
FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("legacy acronym", re.compile(r"\bISOM\b")),
    (
        "legacy full name",
        re.compile(r"Interactive Scientific Object Model"),
    ),
    ("legacy curie prefix", re.compile(r"isom:")),
    ("legacy w3id namespace", re.compile(r"w3id\.org/isom")),
    ("legacy schema name", re.compile(r"isom_core")),
)


def _iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in SCAN_EXTENSIONS:
            continue
        if path.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        files.append(path)
    return files


def test_no_isom_references_in_repository() -> None:
    violations: list[str] = []
    for path in _iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(REPO_ROOT)
        for label, pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                violations.append(f"{rel}: matched forbidden pattern ({label})")
    assert not violations, "Forbidden legacy naming found:\n" + "\n".join(sorted(violations))
