---
search:
  boost: 2.0
---


# Enum: RefusalState 




_Five-state refusal taxonomy. Distinct from EpistemicStatus — RefusalState answers "did we look, and what did we find?", EpistemicStatus answers "what kind of statement is this?"._



<div data-search-exclude markdown="1">

URI: [isom:RefusalState](https://w3id.org/isom/RefusalState)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| unknown | None | Question not considered |
| not_searched | None | Question in scope, but retrieval not attempted |
| searched_absent | None | Retrieval attempted under stated scope and value absent |
| out_of_viewpoint | None | Question may be answerable but the extracting viewpoint did not commit to it |
| contradicted | None | Answer was found but is refuted by other evidence; no current usable answer u... |













## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/isom/core






## LinkML Source

<details>
```yaml
name: RefusalState
description: Five-state refusal taxonomy. Distinct from EpistemicStatus — RefusalState
  answers "did we look, and what did we find?", EpistemicStatus answers "what kind
  of statement is this?".
from_schema: https://w3id.org/isom/core
rank: 1000
permissible_values:
  unknown:
    text: unknown
    description: Question not considered.
  not_searched:
    text: not_searched
    description: Question in scope, but retrieval not attempted.
  searched_absent:
    text: searched_absent
    description: Retrieval attempted under stated scope and value absent.
  out_of_viewpoint:
    text: out_of_viewpoint
    description: Question may be answerable but the extracting viewpoint did not commit
      to it. Proposes viewpoint extension as next action.
  contradicted:
    text: contradicted
    description: Answer was found but is refuted by other evidence; no current usable
      answer until adjudication.

```
</details>

</div>