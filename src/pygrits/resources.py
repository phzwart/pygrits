"""
Runtime accessors for files shipped inside the pygrits package.

The LinkML source schema (``core.yaml``) and the generated JSON Schema
(``core.schema.json``) are bundled with the wheel. Downstream code that
needs to validate instances using the LinkML toolchain — or feed the
JSON Schema to a non-Python validator — should use these accessors
rather than guessing at install paths.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path


def schema_path() -> Path:
    """Return the on-disk path to the bundled LinkML schema (core.yaml)."""
    with resources.as_file(resources.files("pygrits").joinpath("core.yaml")) as p:
        return Path(p)


def json_schema_path() -> Path:
    """Return the on-disk path to the bundled JSON Schema (core.schema.json)."""
    with resources.as_file(
        resources.files("pygrits").joinpath("core.schema.json")
    ) as p:
        return Path(p)


def viewpoint_schema_path(name: str) -> Path:
    """Return the on-disk path to a bundled viewpoint LinkML schema.

    ``name`` is the viewpoint basename without extension, e.g.
    ``"materials_science_v0"`` resolves ``pygrits/viewpoints/materials_science_v0.yaml``.
    """
    filename = f"{name}.yaml" if not name.endswith(".yaml") else name
    with resources.as_file(
        resources.files("pygrits.viewpoints").joinpath(filename)
    ) as p:
        return Path(p)


def viewpoint_json_schema_path(name: str) -> Path:
    """Return the on-disk path to a bundled viewpoint JSON Schema."""
    basename = name.removesuffix(".yaml").removesuffix(".schema.json")
    filename = f"{basename}.schema.json"
    with resources.as_file(
        resources.files("pygrits.viewpoints").joinpath(filename)
    ) as p:
        return Path(p)
