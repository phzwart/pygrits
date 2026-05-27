---
search:
  boost: 10.0
---

# Class: BboxLocator 


_Axis-aligned bounding box on a rasterized page._



<div data-search-exclude markdown="1">



URI: [isom:BboxLocator](https://w3id.org/isom/BboxLocator)





```mermaid
 classDiagram
    class BboxLocator
    click BboxLocator href "../BboxLocator/"
      Locator <|-- BboxLocator
        click Locator href "../Locator/"
      
      BboxLocator : bbox_x0
        
      BboxLocator : bbox_x1
        
      BboxLocator : bbox_y0
        
      BboxLocator : bbox_y1
        
      BboxLocator : locator_type
        
      BboxLocator : page
        
      
```





## Inheritance
* [Locator](Locator.md)
    * **BboxLocator**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [page](page.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [bbox_x0](bbox_x0.md) | 1 <br/> [Float](Float.md) |  | direct |
| [bbox_y0](bbox_y0.md) | 1 <br/> [Float](Float.md) |  | direct |
| [bbox_x1](bbox_x1.md) | 1 <br/> [Float](Float.md) |  | direct |
| [bbox_y1](bbox_y1.md) | 1 <br/> [Float](Float.md) |  | direct |
| [locator_type](locator_type.md) | 1 <br/> [String](String.md) | Class name of the concrete Locator subclass (e | [Locator](Locator.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:BboxLocator |
| native | isom:BboxLocator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BboxLocator
description: Axis-aligned bounding box on a rasterized page.
from_schema: https://w3id.org/isom/core
is_a: Locator
attributes:
  page:
    name: page
    from_schema: https://w3id.org/isom/core
    domain_of:
    - CharRangeLocator
    - BboxLocator
    range: integer
    required: true
  bbox_x0:
    name: bbox_x0
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - BboxLocator
    range: float
    required: true
  bbox_y0:
    name: bbox_y0
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - BboxLocator
    range: float
    required: true
  bbox_x1:
    name: bbox_x1
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - BboxLocator
    range: float
    required: true
  bbox_y1:
    name: bbox_y1
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - BboxLocator
    range: float
    required: true

```
</details>

### Induced

<details>
```yaml
name: BboxLocator
description: Axis-aligned bounding box on a rasterized page.
from_schema: https://w3id.org/isom/core
is_a: Locator
attributes:
  page:
    name: page
    from_schema: https://w3id.org/isom/core
    owner: BboxLocator
    domain_of:
    - CharRangeLocator
    - BboxLocator
    range: integer
    required: true
  bbox_x0:
    name: bbox_x0
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: BboxLocator
    domain_of:
    - BboxLocator
    range: float
    required: true
  bbox_y0:
    name: bbox_y0
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: BboxLocator
    domain_of:
    - BboxLocator
    range: float
    required: true
  bbox_x1:
    name: bbox_x1
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: BboxLocator
    domain_of:
    - BboxLocator
    range: float
    required: true
  bbox_y1:
    name: bbox_y1
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: BboxLocator
    domain_of:
    - BboxLocator
    range: float
    required: true
  locator_type:
    name: locator_type
    description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
    from_schema: https://w3id.org/isom/core
    rank: 1000
    designates_type: true
    owner: BboxLocator
    domain_of:
    - Locator
    range: string
    required: true

```
</details></div>