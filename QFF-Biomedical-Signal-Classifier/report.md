# QFF Biomedical Signal Classifier Report

## Benchmark evidence

The repository already contains benchmark result tables under `results/tables/`.
The observed processor resource summaries are:

| Processor | Physical qubits | Logical qubits | Circuit depth | CX gates | Two-qubit gates |
| --- | ---: | ---: | ---: | ---: | ---: |
| Processor A | 5 | 4 | 57 | 17 | 17 |
| Processor B | 9 | 4 | 25 | 8 | 8 |

The corresponding operation counts in `processor_AB_metrics.csv` are:

- Processor A: `rz=63`, `sx=34`, `cx=17`
- Processor B: `rz=38`, `sx=22`, `cx=8`

These values are copied from the existing benchmark artifacts; no new
experimental result is generated here.

The current `src/` modules do not generate these CSV or PNG artifacts. Their
provenance is therefore historical or notebook-based and remains unverified
until the experiment is reproduced in an approved environment.

## Verification required

- `processors/processor_A.json` and `processors/processor_B.json` exist but
  are currently empty. Their official challenge configuration must be restored
  or verified before using them as executable backend definitions.
- The benchmark tables do not provide coupling maps, basis-gate constraints,
  calibration data, or official processor identifiers. Those settings remain
  unverified and are intentionally not invented.
- The official challenge dataset split, scoring rules, and hardware/noise
  settings must be checked against the challenge specification.

## Existing artifacts

The existing notebook and result CSV/PNG files are preserved. This structure
change does not create a notebook, dataset, graph, or experimental result.
