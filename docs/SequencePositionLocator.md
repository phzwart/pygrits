---
search:
  boost: 10.0
---

# Class: SequencePositionLocator 


_Position range within a reference sequence._



<div data-search-exclude markdown="1">



URI: [grits:SequencePositionLocator](https://w3id.org/grits/SequencePositionLocator)





```mermaid
 classDiagram
    class SequencePositionLocator
    click SequencePositionLocator href "../SequencePositionLocator/"
      Locator <|-- SequencePositionLocator
        click Locator href "../Locator/"
      
      SequencePositionLocator : locator_type
        
      SequencePositionLocator : reference_sequence_id
        
      SequencePositionLocator : seq_end
        
      SequencePositionLocator : seq_start
        
      
```





## Inheritance
* [Locator](Locator.md)
    * **SequencePositionLocator**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [reference_sequence_id](reference_sequence_id.md) | 1 <br/> [String](String.md) |  | direct |
| [seq_start](seq_start.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [seq_end](seq_end.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [locator_type](locator_type.md) | 1 <br/> [String](String.md) | Class name of the concrete Locator subclass (e | [Locator](Locator.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | grits:SequencePositionLocator |
| native | grits:SequencePositionLocator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SequencePositionLocator
description: Position range within a reference sequence.
from_schema: https://w3id.org/grits/core
is_a: Locator
attributes:
  reference_sequence_id:
    name: reference_sequence_id
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - SequencePositionLocator
    required: true
  seq_start:
    name: seq_start
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - SequencePositionLocator
    range: integer
    required: true
  seq_end:
    name: seq_end
    from_schema: https://w3id.org/grits/core
    rank: 1000
    domain_of:
    - SequencePositionLocator
    range: integer
    required: true

```
</details>

### Induced

<details>
```yaml
name: SequencePositionLocator
description: Position range within a reference sequence.
from_schema: https://w3id.org/grits/core
is_a: Locator
attributes:
  reference_sequence_id:
    name: reference_sequence_id
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: SequencePositionLocator
    domain_of:
    - SequencePositionLocator
    range: string
    required: true
  seq_start:
    name: seq_start
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: SequencePositionLocator
    domain_of:
    - SequencePositionLocator
    range: integer
    required: true
  seq_end:
    name: seq_end
    from_schema: https://w3id.org/grits/core
    rank: 1000
    owner: SequencePositionLocator
    domain_of:
    - SequencePositionLocator
    range: integer
    required: true
  locator_type:
    name: locator_type
    description: Class name of the concrete Locator subclass (e.g. CharRangeLocator).
    from_schema: https://w3id.org/grits/core
    rank: 1000
    designates_type: true
    owner: SequencePositionLocator
    domain_of:
    - Locator
    range: string
    required: true

```
</details></div>