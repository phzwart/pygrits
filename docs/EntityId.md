---
search:
  boost: 1.0
---# Type: EntityId 




_Canonical entity identifier of the form scheme:value, where scheme is one of obj, act, evi, vpt, src. Hash-derived where applicable. Identity is by declaration plus content hash (for ContentReference-bearing entities like ViewpointDirective)._



<div data-search-exclude markdown="1">

URI: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

## Type Properties

| Property | Value |
| --- | --- |
| Base | `str` |
| Type URI | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
## Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]+:[A-Za-z0-9._:-]+$` |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | xsd:string |
| native | isom:EntityId |




</div>