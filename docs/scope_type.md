---
search:
  boost: 5.0
---

# Slot: scope_type 


_Class name of the concrete Scope subclass (e.g. NotesOnlyScope)._



<div data-search-exclude markdown="1">



URI: [grits:scope_type](https://w3id.org/grits/scope_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Scope](Scope.md) | Container for viewpoint-supplied scope dimensions |  no  |
| [NotesOnlyScope](NotesOnlyScope.md) | Scope marker with only free-form notes; no domain dimensions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Scope](Scope.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Designates Type | Yes |
| Owner | [Scope](Scope.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:scope_type |
| native | grits:scope_type |




## LinkML Source

<details>
```yaml
name: scope_type
description: Class name of the concrete Scope subclass (e.g. NotesOnlyScope).
from_schema: https://w3id.org/grits/core
rank: 1000
designates_type: true
owner: Scope
domain_of:
- Scope
range: string
required: true

```
</details></div>