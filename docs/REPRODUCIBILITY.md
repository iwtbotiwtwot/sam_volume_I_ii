# Reproducing Chapter II

Use Python 3.11 or 3.12 from the repository root. Core checks use only Python's
standard library and run offline. A clean clone carries the required source
operands and retained evidence; it needs neither the original SAM checkout nor
a native worker. PDF rendering has separate optional dependencies.

## Scientific commands

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/reproduce.py
python scripts/verify_native.py
python scripts/verify_repository.py
```

For an isolated environment, perform the editable installation as follows:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Dependency installation is a setup step; the scientific commands themselves
need no network. The test runner is standard-library `unittest`.

| Route | What it does | Main report |
|---|---|---|
| Unit tests | Scientific identities, input validation and integrity regression checks | Terminal test report |
| `scripts/reproduce.py` | Compact independent reference calculations using fixed exact operands | `build/reproduction.json` |
| `scripts/verify_native.py` | Selected-byte integrity, isolated retained-checker replay and native receipt/readback verification | `build/native_verification.json` |
| `scripts/verify_repository.py` | Public manuscript, operands, source assets and evidence bindings | Terminal integrity report |

The compact calculation and retained-checker route have different scopes.
The first demonstrates independently implemented consequences. The second
replays source-law, closure, protocol, measurement, native readback and custody
checks against the original retained outputs. Neither performs a new native
scientific campaign or physical experiment.

The reference API is under [`src/sam_chapter2/`](../src/sam_chapter2/):

| Module | Independent calculation |
|---|---|
| `memory.py` | Source-metric residual certificates and finite-time error envelopes |
| `radial.py` | Exact Dirichlet operator, Green inverse and shell flux/energy |
| `phase.py` | Correlated phase bounds and separate independent-band threshold |
| `sampling.py` | Rational logarithm/shot bounds, difference-Hankel minors and decision thresholds |
| `reference.py` | Paid forward/reverse/wait account and reference-phase unwrapping |
| `_exact.py` | Exact rational intervals and shared input validation |

Inputs are exact rational values or declared rational intervals. Compact API
fixtures demonstrate the formulas; full literal spin/source certificates and
original native returns remain in the separate retained replay. API examples
do not replace that evidence with fitted numerical values.

For selected evidence integrity without the full replay:

```bash
python scripts/verify_native.py --integrity-only
```

Failures return a nonzero exit status. Generated reports remain in `build/`,
which is excluded from version control. Frozen `evidence/` remains unchanged.

## Retained-checker replay scope

The wrapper authenticates the selected evidence inventory, stages a disposable
copy, runs eight physical-development checks and nine source-to-field offline
checks, and collects their reports. The initial complete replay returned:

| Measure | Observed result |
|---|---:|
| Scientific assertions | 42,961 |
| Native outputs independently received | 22 |
| Native readback checks | 32,304 |
| Authenticated source-domain calls | 64: 58 evaluations and 6 inverse checks |
| Authenticated local retrieval receipts | 8 |
| New native operations | 0 |

These measures are separate; adding them would not produce a meaningful test
count. Earlier bridge/continuation totals in retained historical reports are
not automatically counted again by the present replay.

The selected export omits global research SQLite corpora. One physical legacy
cycle predicate is adapted under a strict AST check to compare its retained
digest against launch configuration/original metadata; its original bytes
remain frozen. The report records one adaptation and
`legacy_cycle_index_bytes_checked: false`. Seven other physical scripts and
the nine source-to-field scripts run unchanged. The original source-to-field
root ZIP-manifest step is skipped after verifying the new selected manifest.
The public replay does not claim to authenticate unshipped database bytes.
See [native evidence](NATIVE_EVIDENCE.md) and [provenance](PROVENANCE.md).

## PDF build

Use Python 3.12 for the pinned typesetting environment:

```bash
python -m pip install -r requirements-pdf.lock
python scripts/build_pdf.py --output build/Chapter_II.pdf
python scripts/verify_pdf.py build/Chapter_II.pdf
```

The reviewed PDF is `manuscript/Chapter_II.pdf`. Editable text is
`manuscript/chapter_II.md`; executable page-construction sources are under
`manuscript/source/`. Bundled fonts include their full upstream notices.
No system font or original host path is required.

To check deterministic output with the same environment:

```bash
python scripts/build_pdf.py --output build/Chapter_II_repeat.pdf
cmp build/Chapter_II.pdf build/Chapter_II_repeat.pdf
```

PDF text and structural checks complement visual inspection. Vector equation
shapes need image review; extracted text alone cannot verify their mathematics.
For scientific changes, the appropriate derivation and operand checks remain
necessary even if the page looks unchanged.

## Interpreting successful results

A mathematical identity, a certified native interval, an independent retained
readback, a manifest check, a PDF check and an experimental shot have different
roles. A successful repository run reproduces its stated calculations and
checks its selected custody. It does not supply physical epsilon in SI units,
a material controller, measured detector fidelity, a stabilized minimum spin
closure or an undeclared gravity coupling.

The [model](MODEL.md), [proof guide](PROOFS.md) and
[open work](OPEN_WORK.md) retain those physical and mathematical interfaces.
