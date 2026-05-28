---
search:
  boost: 5.0
---

# Slot: log_line_start 

<div data-search-exclude markdown="1">



URI: [grits:log_line_start](https://w3id.org/grits/log_line_start)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessingLogLineLocator](ProcessingLogLineLocator.md) | Line range within a processing log |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ProcessingLogLineLocator](ProcessingLogLineLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ProcessingLogLineLocator](ProcessingLogLineLocator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:log_line_start |
| native | grits:log_line_start |




## LinkML Source

<details>
```yaml
name: log_line_start
from_schema: https://w3id.org/grits/core
rank: 1000
owner: ProcessingLogLineLocator
domain_of:
- ProcessingLogLineLocator
range: integer
required: true

```
</details></div>