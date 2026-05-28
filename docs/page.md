---
search:
  boost: 5.0
---

# Slot: page 

<div data-search-exclude markdown="1">



URI: [grits:page](https://w3id.org/grits/page)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CharRangeLocator](CharRangeLocator.md) | Character range within extracted text of a source artifact |  no  |
| [BboxLocator](BboxLocator.md) | Axis-aligned bounding box on a rasterized page |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CharRangeLocator](CharRangeLocator.md), [BboxLocator](BboxLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:page |
| native | grits:page |




## LinkML Source

<details>
```yaml
name: page
domain_of:
- CharRangeLocator
- BboxLocator
range: string

```
</details></div>