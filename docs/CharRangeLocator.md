---
search:
  boost: 10.0
---

# Class: CharRangeLocator 


_Character range within extracted text of a source artifact._



<div data-search-exclude markdown="1">



URI: [grits:CharRangeLocator](https://w3id.org/grits/CharRangeLocator)





```mermaid
 classDiagram
    class CharRangeLocator
    click CharRangeLocator href "../CharRangeLocator/"
      Locator <|-- CharRangeLocator
        click Locator href "../Locator/"
      
      CharRangeLocator : char_end
        
      CharRangeLocator : char_start
        
      CharRangeLocator : locator_type
        
      CharRangeLocator : page
        
      
```





## Inheritance
* [Locator](Locator.md)
    * **CharRangeLocator**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [char_start](char_start.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [char_end](char_end.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [page](page.md) | 0..1 <br/> [Integer](Integer.md) |  | direct |
| [locator_type](locator_type.md) | 1 <br/> [String](String.md) | Class name of the concrete Locator subclass (e | [Locator](Locator.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:CharRangeLocator |
| native | grits:CharRangeLocator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CharRangeLocator
description: Character range within extracted text of a source artifact.
from_schema: https://w3id.org/grits/core
is_a: Locator
attributes:
  char_start:
    name: char_start
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CharRangeLocator
    range: integer
    required: true
  char_end:
    name: char_end
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CharRangeLocator
    range: integer
    required: true
  page:
    name: page
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - CharRangeLocator
    - BboxLocator
    range: integer

```
</details>

### Induced

<details>
```yaml
name: CharRangeLocator
description: Character range within extracted text of a source artifact.
from_schema: https://w3id.org/grits/core
is_a: Locator
attributes:
  char_start:
    name: char_start
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CharRangeLocator
    domain_of:
    - CharRangeLocator
    range: integer
    required: true
  char_end:
    name: char_end
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CharRangeLocator
    domain_of:
    - CharRangeLocator
    range: integer
    required: true
  page:
    name: page
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: CharRangeLocator
    domain_of:
    - CharRangeLocator
    - BboxLocator
    range: integer
  locator_type:
    name: locator_type
    description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
    from_schema: https://w3id.org/grits/core
    rank: 1000
    designates_type: true
    owner: CharRangeLocator
    domain_of:
    - Locator
    range: string
    required: true

```
</details></div>