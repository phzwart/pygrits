---
search:
  boost: 5.0
---

# Slot: members 

<div data-search-exclude markdown="1">



URI: [grits:members](https://w3id.org/grits/members)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeLocator](CompositeLocator.md) | A locator that combines multiple sub-locators |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Locator](Locator.md) |
| Domain Of | [CompositeLocator](CompositeLocator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CompositeLocator](CompositeLocator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:members |
| native | grits:members |




## LinkML Source

<details>
```yaml
name: members
from_schema: https://w3id.org/grits/core
rank: 1000
owner: CompositeLocator
domain_of:
- CompositeLocator
range: Locator
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>