---
search:
  boost: 5.0
---

# Slot: uri 


_Locator (file path, https URL, did:..., cid:...)._



<div data-search-exclude markdown="1">



URI: [grits:uri](https://w3id.org/grits/uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentReference](ContentReference.md) | Content-addressed reference to externally stored content |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContentReference](ContentReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentReference](ContentReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:uri |
| native | grits:uri |




## LinkML Source

<details>
```yaml
name: uri
description: Locator (file path, https URL, did:..., cid:...).
from_schema: https://w3id.org/grits/core
rank: 1000
owner: ContentReference
domain_of:
- ContentReference
range: string
required: true

```
</details></div>