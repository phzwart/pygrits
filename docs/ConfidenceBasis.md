---
search:
  boost: 2.0
---


# Enum: ConfidenceBasis 




_Source semantics of a confidence value._



<div data-search-exclude markdown="1">

URI: [grits:ConfidenceBasis](https://w3id.org/grits/ConfidenceBasis)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| parser_self_report | None | Vendor-provided model self-report; typically uncalibrated |
| conformal | None | PAC coverage under exchangeability; calibrated to operational rate |
| bayesian | None | Posterior-derived; calibrated under priors and model assumptions |
| heuristic | None | Ad hoc; basis must be documented in calibration_scope |
| aggregated | None | Combined over heterogeneous evidence; combination method must be declared |




## Slots

| Name | Description |
| ---  | --- |
| [confidence_basis](confidence_basis.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/grits/core






## LinkML Source

<details>
```yaml
name: ConfidenceBasis
description: Source semantics of a confidence value.
from_schema: https://w3id.org/grits/core
rank: 1000
permissible_values:
  parser_self_report:
    text: parser_self_report
    description: Vendor-provided model self-report; typically uncalibrated.
  conformal:
    text: conformal
    description: PAC coverage under exchangeability; calibrated to operational rate.
  bayesian:
    text: bayesian
    description: Posterior-derived; calibrated under priors and model assumptions.
  heuristic:
    text: heuristic
    description: Ad hoc; basis must be documented in calibration_scope.
  aggregated:
    text: aggregated
    description: Combined over heterogeneous evidence; combination method must be
      declared.

```
</details>

</div>