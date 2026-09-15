#!/usr/bin/env bash
# Regenerate generated artifacts from the LinkML source schema.
#
# Run this whenever src/pygrits/core.yaml or viewpoints/*.yaml changes.
# Committed: core.py, core.schema.json, core.context.jsonld, viewpoint artifacts.
# docs/ and core.ttl are generated in CI only (not committed).
#
# Requires:  pip install 'pygrits[schema]'
#
# Usage:     ./scripts/regenerate.sh

set -euo pipefail

cd "$(dirname "$0")/.."

SCHEMA="src/pygrits/core.yaml"
VIEWPOINTS_DIR="viewpoints"
VIEWPOINTS_PKG="src/pygrits/viewpoints"

if [[ ! -f "$SCHEMA" ]]; then
    echo "Schema not found: $SCHEMA" >&2
    exit 1
fi

for cmd in gen-pydantic gen-json-schema gen-jsonld-context; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Missing tool: $cmd" >&2
        echo "Install with:  pip install 'pygrits[schema]'" >&2
        exit 1
    fi
done

echo "Regenerating Pydantic models..."
gen-pydantic "$SCHEMA" > src/pygrits/core.py

echo "Regenerating JSON Schema..."
gen-json-schema "$SCHEMA" > src/pygrits/core.schema.json

echo "Regenerating JSON-LD context..."
gen-jsonld-context "$SCHEMA" > src/pygrits/core.context.jsonld

mkdir -p "$VIEWPOINTS_PKG"

if [[ -d "$VIEWPOINTS_DIR" ]]; then
    shopt -s nullglob
    for vp_schema in "$VIEWPOINTS_DIR"/*.yaml; do
        vp_name="$(basename "$vp_schema" .yaml)"
        echo "Regenerating viewpoint: $vp_name ..."
        gen-pydantic "$vp_schema" > "$VIEWPOINTS_PKG/${vp_name}.py"
        gen-json-schema "$vp_schema" > "$VIEWPOINTS_PKG/${vp_name}.schema.json"
        cp "$vp_schema" "$VIEWPOINTS_PKG/${vp_name}.yaml"
    done
    shopt -u nullglob
fi

echo
echo "Done. Run tests:  pytest"
echo "Commit changes if everything passes."
