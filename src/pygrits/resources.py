"""Paths to bundled LinkML and JSON Schema artifacts."""

from __future__ import annotations

from importlib import resources
from pathlib import Path


def _pkg_path(*parts: str) -> Path:
    with resources.as_file(resources.files("pygrits").joinpath(*parts)) as p:
        return Path(p)


def schema_path() -> Path:
    return _pkg_path("core.yaml")


def json_schema_path() -> Path:
    return _pkg_path("core.schema.json")


def viewpoint_schema_path(name: str) -> Path:
    filename = f"{name}.yaml" if not name.endswith(".yaml") else name
    with resources.as_file(
        resources.files("pygrits.viewpoints").joinpath(filename)
    ) as p:
        return Path(p)


def viewpoint_json_schema_path(name: str) -> Path:
    basename = name.removesuffix(".yaml").removesuffix(".schema.json")
    with resources.as_file(
        resources.files("pygrits.viewpoints").joinpath(f"{basename}.schema.json")
    ) as p:
        return Path(p)
