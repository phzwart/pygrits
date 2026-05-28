---
search:
  boost: 5.0
---

# Slot: char_end 

<div data-search-exclude markdown="1">



URI: [grits:char_end](https://w3id.org/grits/char_end)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CharRangeLocator](CharRangeLocator.md) | Character range within extracted text of a source artifact |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [CharRangeLocator](CharRangeLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CharRangeLocator](CharRangeLocator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:char_end |
| native | grits:char_end |




## LinkML Source

<details>
```yaml
name: char_end
from_schema: https://w3id.org/grits/core
rank: 1000
owner: CharRangeLocator
domain_of:
- CharRangeLocator
range: integer
required: true

```
</details></div>