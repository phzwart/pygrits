---
search:
  boost: 5.0
---

# Slot: byte_start 

<div data-search-exclude markdown="1">



URI: [grits:byte_start](https://w3id.org/grits/byte_start)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileRegionLocator](FileRegionLocator.md) | Byte range within an opaque binary artifact |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [FileRegionLocator](FileRegionLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FileRegionLocator](FileRegionLocator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:byte_start |
| native | grits:byte_start |




## LinkML Source

<details>
```yaml
name: byte_start
from_schema: https://w3id.org/grits/core
rank: 1000
owner: FileRegionLocator
domain_of:
- FileRegionLocator
range: integer
required: true

```
</details></div>