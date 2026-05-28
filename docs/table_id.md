---
search:
  boost: 5.0
---

# Slot: table_id 

<div data-search-exclude markdown="1">



URI: [grits:table_id](https://w3id.org/grits/table_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TableCellLocator](TableCellLocator.md) | A specific cell within an extracted table |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TableCellLocator](TableCellLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TableCellLocator](TableCellLocator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:table_id |
| native | grits:table_id |




## LinkML Source

<details>
```yaml
name: table_id
from_schema: https://w3id.org/grits/core
rank: 1000
owner: TableCellLocator
domain_of:
- TableCellLocator
range: string
required: true

```
</details></div>