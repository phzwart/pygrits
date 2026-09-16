"""Paths to the bundled profile, context, and JSON Schema."""

from __future__ import annotations

from importlib import resources
from pathlib import Path


def _pkg_path(*parts: str) -> Path:
    with resources.as_file(resources.files("pygrits").joinpath(*parts)) as p:
        return Path(p)


def context_path() -> Path:
    return _pkg_path("context.jsonld")


def schema_path() -> Path:
    return _pkg_path("schema.json")


def profile_path() -> Path:
    return _pkg_path("PROFILE.md")


def profile_text() -> str:
    return profile_path().read_text(encoding="utf-8")
