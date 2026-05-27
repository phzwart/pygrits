---
search:
  boost: 10.0
---

# Class: TableCellLocator 


_A specific cell within an extracted table._



<div data-search-exclude markdown="1">



URI: [isom:TableCellLocator](https://w3id.org/isom/TableCellLocator)





```mermaid
 classDiagram
    class TableCellLocator
    click TableCellLocator href "../TableCellLocator/"
      Locator <|-- TableCellLocator
        click Locator href "../Locator/"
      
      TableCellLocator : col
        
      TableCellLocator : locator_type
        
      TableCellLocator : row
        
      TableCellLocator : table_id
        
      
```





## Inheritance
* [Locator](Locator.md)
    * **TableCellLocator**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [table_id](table_id.md) | 1 <br/> [String](String.md) |  | direct |
| [row](row.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [col](col.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [locator_type](locator_type.md) | 1 <br/> [String](String.md) | Class name of the concrete Locator subclass (e | [Locator](Locator.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | isom:TableCellLocator |
| native | isom:TableCellLocator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TableCellLocator
description: A specific cell within an extracted table.
from_schema: https://w3id.org/isom/core
is_a: Locator
attributes:
  table_id:
    name: table_id
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - TableCellLocator
    required: true
  row:
    name: row
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - TableCellLocator
    range: integer
    required: true
  col:
    name: col
    from_schema: https://w3id.org/isom/core
    rank: 1000
    domain_of:
    - TableCellLocator
    range: integer
    required: true

```
</details>

### Induced

<details>
```yaml
name: TableCellLocator
description: A specific cell within an extracted table.
from_schema: https://w3id.org/isom/core
is_a: Locator
attributes:
  table_id:
    name: table_id
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: TableCellLocator
    domain_of:
    - TableCellLocator
    range: string
    required: true
  row:
    name: row
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: TableCellLocator
    domain_of:
    - TableCellLocator
    range: integer
    required: true
  col:
    name: col
    from_schema: https://w3id.org/isom/core
    rank: 1000
    owner: TableCellLocator
    domain_of:
    - TableCellLocator
    range: integer
    required: true
  locator_type:
    name: locator_type
    description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
    from_schema: https://w3id.org/isom/core
    rank: 1000
    designates_type: true
    owner: TableCellLocator
    domain_of:
    - Locator
    range: string
    required: true

```
</details></div>