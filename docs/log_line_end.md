---
search:
  boost: 5.0
---

# Slot: log_line_end 

<div data-search-exclude markdown="1">



URI: [isom:log_line_end](https://w3id.org/isom/log_line_end)
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


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:log_line_end |
| native | isom:log_line_end |




## LinkML Source

<details>
```yaml
name: log_line_end
from_schema: https://w3id.org/isom/core
rank: 1000
owner: ProcessingLogLineLocator
domain_of:
- ProcessingLogLineLocator
range: integer
required: true

```
</details></div>