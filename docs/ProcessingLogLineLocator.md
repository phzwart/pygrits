---
search:
  boost: 10.0
---

# Class: ProcessingLogLineLocator 


_Line range within a processing log._



<div data-search-exclude markdown="1">



URI: [grits:ProcessingLogLineLocator](https://w3id.org/grits/ProcessingLogLineLocator)





```mermaid
 classDiagram
    class ProcessingLogLineLocator
    click ProcessingLogLineLocator href "../ProcessingLogLineLocator/"
      Locator <|-- ProcessingLogLineLocator
        click Locator href "../Locator/"
      
      ProcessingLogLineLocator : locator_type
        
      ProcessingLogLineLocator : log_line_end
        
      ProcessingLogLineLocator : log_line_start
        
      
```





## Inheritance
* [Locator](Locator.md)
    * **ProcessingLogLineLocator**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [log_line_start](log_line_start.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [log_line_end](log_line_end.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [locator_type](locator_type.md) | 1 <br/> [String](String.md) | Class name of the concrete Locator subclass (e | [Locator](Locator.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:ProcessingLogLineLocator |
| native | grits:ProcessingLogLineLocator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessingLogLineLocator
description: Line range within a processing log.
from_schema: https://w3id.org/grits/core
is_a: Locator
attributes:
  log_line_start:
    name: log_line_start
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ProcessingLogLineLocator
    range: integer
    required: true
  log_line_end:
    name: log_line_end
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - ProcessingLogLineLocator
    range: integer
    required: true

```
</details>

### Induced

<details>
```yaml
name: ProcessingLogLineLocator
description: Line range within a processing log.
from_schema: https://w3id.org/grits/core
is_a: Locator
attributes:
  log_line_start:
    name: log_line_start
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ProcessingLogLineLocator
    domain_of:
    - ProcessingLogLineLocator
    range: integer
    required: true
  log_line_end:
    name: log_line_end
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: ProcessingLogLineLocator
    domain_of:
    - ProcessingLogLineLocator
    range: integer
    required: true
  locator_type:
    name: locator_type
    description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
    from_schema: https://w3id.org/grits/core
    rank: 1000
    designates_type: true
    owner: ProcessingLogLineLocator
    domain_of:
    - Locator
    range: string
    required: true

```
</details></div>