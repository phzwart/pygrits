#!/usr/bin/env bash
# Regenerate generated artifacts from the LinkML source schema.
#
# Run this whenever src/pygrits/core.yaml changes. The generated files
# (core.py, core.schema.json, docs/) are checked into the repo so users
# don't need the LinkML toolchain to install or use pygrits.
#
# Requires:  pip install 'pygrits[schema]'   (or just  pip install linkml)
#
# Usage:     ./scripts/regenerate.sh

set -euo pipefail

cd "$(dirname "$0")/.."

SCHEMA="src/pygrits/core.yaml"

if [[ ! -f "$SCHEMA" ]]; then
    echo "Schema not found: $SCHEMA" >&2
    exit 1
fi

for cmd in gen-pydantic gen-json-schema gen-doc; do
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

echo "Regenerating docs..."
rm -rf docs
mkdir -p docs
gen-doc "$SCHEMA" -d docs

echo
echo "Done. Run tests:  pytest"
echo "Commit changes if everything passes."
