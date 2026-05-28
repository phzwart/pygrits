---
search:
  boost: 5.0
---

# Slot: locator_type 


_Class name of the concrete Locator subclass (e.g. CharRangeLocator)._



<div data-search-exclude markdown="1">



URI: [grits:locator_type](https://w3id.org/grits/locator_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Locator](Locator.md) | Polymorphic locator into a source artifact |  no  |
| [CharRangeLocator](CharRangeLocator.md) | Character range within extracted text of a source artifact |  no  |
| [BboxLocator](BboxLocator.md) | Axis-aligned bounding box on a rasterized page |  no  |
| [SequencePositionLocator](SequencePositionLocator.md) | Position range within a reference sequence |  no  |
| [ProcessingLogLineLocator](ProcessingLogLineLocator.md) | Line range within a processing log |  no  |
| [TableCellLocator](TableCellLocator.md) | A specific cell within an extracted table |  no  |
| [FileRegionLocator](FileRegionLocator.md) | Byte range within an opaque binary artifact |  no  |
| [CompositeLocator](CompositeLocator.md) | A locator that combines multiple sub-locators |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Locator](Locator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Designates Type | Yes |
| Owner | [Locator](Locator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:locator_type |
| native | grits:locator_type |




## LinkML Source

<details>
```yaml
name: locator_type
description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
from_schema: https://w3id.org/grits/core
rank: 1000
designates_type: true
owner: Locator
domain_of:
- Locator
range: string
required: true

```
</details></div>