# SAM Volume I, Chapter II

**Retention, accumulation, and the finite ledger**

This repository accompanies the 24-page, 48-section Chapter II development
edition of 15 October 2026. It includes the reviewed manuscript, editable
sources, mathematical derivations, exact operands and certificates, independent
code, tests, and retained evidence for offline reproduction. It follows the
publication structure of [Chapter I](https://github.com/iwtbotiwtwot/sam_volume_I_i).

**[Read Chapter II](manuscript/Chapter_II.pdf)** ·
[Editable manuscript](manuscript/chapter_II.md) ·
[Model and scope](docs/MODEL.md) ·
[Proof guide](docs/PROOFS.md) ·
[Reproduction](docs/REPRODUCIBILITY.md) ·
[Source provenance](docs/PROVENANCE.md)

Sean Brady is the originator and conceptual director. OpenAI ChatGPT and Codex
are AI research collaborators and co-authors.

## What the chapter develops

A present address, a predictive source state, an accumulated history and an
outgoing field preserve different information. Chapter II makes those
distinctions executable using the original Write source, Chapter I's actual
interacting clocks, the full finite spin source, and specified receiving
instruments.

- **Shared-source predictions.** A matched individual lane has exactly the
  corresponding two-level dynamics. The complete source also links six lanes
  and protected intersector coherences through one source parameter and one
  physical frequency scale. A finite-record test separates the specified
  protected signal from closed autonomous two-state dynamics with a fixed
  linear receiver.
- **Actual spin nonclosure.** The seven-dimensional span has complementary
  rank two in all 54 original preparations. Every preparation requires at
  least ten invariant coordinates; the selected deeper preparation requires
  at least fourteen. An exact finite invariant upper space is constructed.
  The smallest invariant closure has not stabilized.
- **A paid reference protocol.** Forward Write, reverse Write, wait, entry and
  release retain original positive durations, actual clock phase, reference
  winding, energy and individual work exchanges. Signed net work and apparatus
  cost remain different quantities.
- **A measurement protocol.** Eight expectation values are estimated from
  repeated fresh preparations with separate preparation, evolution, readout,
  timing, calibration and sampling requirements. The useful fixed cadence has
  a sufficient count of 819,751 measurements per time, conditional on its
  stated error budget.
- **History and source costs.** Compact certificates establish the minimum
  additive counter count, ABBA/BAAB event offsets and every compatible pure
  endpoint cost for the selected diagnostic record.
- **A source-to-field interface.** The appended sections distinguish a whole
  energy account from a diagnostic minimum, construct finite spatial receiving
  examples, and test declared couplings against actual source receivers.

**The test result suggests strong contact with the concept.**

These are source-bound mathematical results and specified receiving protocols.
The manuscript keeps physical preparation, units, spatial incidence, external
coupling and apparatus performance explicit. Its development status and open
interfaces are summarized in [open work](docs/OPEN_WORK.md).

## Quick start

Use Python 3.11 or 3.12 from the repository root. The core verification uses
only the Python standard library:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/reproduce.py
python scripts/verify_native.py
python scripts/verify_repository.py
```

After the editable installation, the commands operate on bundled operands and retained evidence. They start no
GEN6 workers and require no SAM installation. Generated reports go to `build/`.
See [reproduction](docs/REPRODUCIBILITY.md) for each route and
[retained native evidence](docs/NATIVE_EVIDENCE.md) for its scope.

## Rebuild the manuscript

Use Python 3.12 and the pinned rendering dependencies:

```bash
python -m pip install -r requirements-pdf.lock
python scripts/build_pdf.py --output build/Chapter_II.pdf
python scripts/verify_pdf.py build/Chapter_II.pdf
```

The editable sources, bundled fonts and renderer travel with the repository.
The checked-in PDF preserves the reviewed edition. PDF structure/text checks
complement visual review; they do not independently verify vector equations.

## Repository map

| Location | Contents |
|---|---|
| `manuscript/` | Reviewed Chapter II PDF and editable manuscript sources |
| `src/` | Standalone mathematical reference implementation |
| `data/` | Compact exact operands and source bindings |
| `evidence/` | Selected frozen source artifacts, certificates, receipts and original verification code |
| `scripts/` | Scientific reproduction, retained-output replay, integrity and PDF commands |
| `tests/` | Scientific and evidence-integrity regression checks |
| `docs/` | Model, proofs, provenance, reproduction, validation, licensing and open work |
| `assets/fonts/` | Bundled Noto fonts and their upstream notices |

The public evidence inventory defines the files actually shipped. Original
manifests retain their historical scope, which can include artifacts outside
this selected export. [Provenance](docs/PROVENANCE.md) explains that boundary;
an upstream path is not a dependency on the original machine.

## Edition and scientific scope

The published reader is the **H002641 source-to-field update**: it preserves
the preceding 40 Chapter II sections and adds sections 41–48. It retains the
physical-development closure and apparatus results under their original
bindings. Later Chapter III local-action, angular-energy, quantum-source and
orbital developments are separate work and are not silently added here.

See [validation](docs/VALIDATION.md) for recorded checks and
[contributing](CONTRIBUTING.md) for evidence-preserving changes. Scientific
checks, original native checks, independent readback assertions, PDF checks
and experimental shots have separate counts and meanings.

The complete selected-evidence replay passes **42,961 scientific assertions**
and **32,304 native readback checks**, receiving 22 retained mathematical
outputs. These are offline verification counts; they are separate from the
experimental measurements specified in the chapter.

## Attribution and license

Citation metadata is in [CITATION.cff](CITATION.cff). Original software uses
[MIT](LICENSE). The manuscript, documentation and original research material
use [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Third-party fonts retain their own
license. See [licensing and attribution](docs/LICENSING.md) and
[author roles](AUTHORS.md) for component scope and the credit statement.
