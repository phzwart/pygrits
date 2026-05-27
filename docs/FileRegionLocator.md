---
search:
  boost: 10.0
---

# Class: FileRegionLocator 


_Byte range within an opaque binary artifact._



<div data-search-exclude markdown="1">



URI: [isom:FileRegionLocator](https://w3id.org/isom/FileRegionLocator)





```mermaid
 classDiagram
    class FileRegionLocator
    click FileRegionLocator href "../FileRegionLocator/"
      Locator <|-- FileRegionLocator
        click Locator href "../Locator/"
      
      FileRegionLocator : byte_end
        
      FileRegionLocator : byte_start
        
      FileRegionLocator : locator_type
        
      
```





## Inheritance
* [Locator](Locator.md)
    * **FileRegionLocator**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [byte_start](byte_start.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [byte_end](byte_end.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [locator_type](locator_type.md) | 1 <br/> [String](String.md) | Class name of the concrete Locator subclass (e | [Locator](Locator.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:FileRegionLocator |
| native | isom:FileRegionLocator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FileRegionLocator
description: Byte range within an opaque binary artifact.
from_schema: https://w3id.org/isom/core
is_a: Locator
attributes:
  byte_start:
    name: byte_start
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - FileRegionLocator
    range: integer
    required: true
  byte_end:
    name: byte_end
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - FileRegionLocator
    range: integer
    required: true

```
</details>

### Induced

<details>
```yaml
name: FileRegionLocator
description: Byte range within an opaque binary artifact.
from_schema: https://w3id.org/isom/core
is_a: Locator
attributes:
  byte_start:
    name: byte_start
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: FileRegionLocator
    domain_of:
    - FileRegionLocator
    range: integer
    required: true
  byte_end:
    name: byte_end
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: FileRegionLocator
    domain_of:
    - FileRegionLocator
    range: integer
    required: true
  locator_type:
    name: locator_type
    description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
    from_schema: https://w3id.org/isom/core
    rank: 1000
    designates_type: true
    owner: FileRegionLocator
    domain_of:
    - Locator
    range: string
    required: true

```
</details></div>