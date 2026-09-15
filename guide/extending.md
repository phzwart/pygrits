# Extending pygrits

1. Import `pygrits/core` (or the bundled `core.yaml`) from your LinkML schema.
2. Subclass **Entity** with typed attributes for your domain.
3. Subclass **Scope** (or **NotesOnlyScope**) for conditions under which claims apply.
4. Optionally subclass **Activity** when you need typed hyperedge metadata.
5. Ship a **ViewpointDirective** YAML with evidence-type CURIEs and constraints.

Keep JSON out of string slots: if a field needs structure, model it as LinkML classes.

Validate bundles with:

```python
from pygrits import validate_bundle
validate_bundle(list_of_grits)
```

Export PROV triples with `pygrits[rdf]` and `to_graph(grits)`.
