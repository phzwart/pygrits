---
search:
  boost: 2.0
---


# Enum: CompositionMode 




_How a composable layer folds against its declared parents during deterministic resolution. Selected per layer; not every layer type supports every mode._



<div data-search-exclude markdown="1">

URI: [grits:CompositionMode](https://w3id.org/grits/CompositionMode)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| additive | None | Child contributes additional content without removing inherited content |
| restrictive | None | Child narrows the admissible space relative to its parents |
| overriding | None | Child intentionally replaces inherited values for overlapping fields |
| isolated | None | Child inherits no operational content from parents; parent ids are retained o... |




## Slots

| Name | Description |
| ---  | --- |
| [composition_mode](composition_mode.md) | How this layer folds against its declared parents during resolution |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core






## LinkML Source

<details>
```yaml
name: CompositionMode
description: How a composable layer folds against its declared parents during deterministic
  resolution. Selected per layer; not every layer type supports every mode.
from_schema: https://w3id.org/grits/core
rank: 1000
permissible_values:
  additive:
    text: additive
    description: Child contributes additional content without removing inherited content.
      List fields union (dedup); most-derived non-null wins for scalars. The default
      for most composition.
  restrictive:
    text: restrictive
    description: Child narrows the admissible space relative to its parents. Constraint
      lists union; permission booleans combine by logical AND.
  overriding:
    text: overriding
    description: Child intentionally replaces inherited values for overlapping fields.
      Used sparingly and remains highly visible in resolved artifacts.
  isolated:
    text: isolated
    description: Child inherits no operational content from parents; parent ids are
      retained only as source references for provenance.

```
</details>

</div>