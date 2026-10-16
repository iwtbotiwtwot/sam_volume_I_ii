# Chapter II physical development and verification

Start with `REPORT.md` and the reader draft under `output/pdf/`. The editable
chapter is in `chapter/`; technical derivations and compact certificates are in
`closure/`, `protocol/`, `measurement/`, and `certificates/`. Original
Chapter I/II source records and the preceding continuation remain preserved.
Sean Brady is originator and conceptual director; OpenAI ChatGPT and Codex are
research collaborators and co-authors.

The actual finite-N spin calculation now determines that the seven-dimensional
enlargement has residual rank two in all 54 original preparations. Every one
requires at least ten invariant coordinates. The selected V001_BASE continuation
reaches fourteen independent source functions, with its thirteen-dimensional
span still noninvariant. These are exact full-source bounds, with an explicit
invariant exchangeable count-space upper closure; the smallest invariant
dimension has not been assigned. The global higher residual moments are not
replaced by auxiliary 20-site moments or invented numerical values.

The paid reference protocol includes forward Write, reverse Write, source wait,
and external entry/release. A source wait retains its reference Hamiltonian.
Signed switch-work cancellation is kept separate from apparatus cost. The
measurement protocol distinguishes eight expectation samples from repeated
experimental shots, and supplies preparation, readout, timing, statistical and
phase-unwrapping requirements. Physical calibration and apparatus realization
remain explicit receiving assignments, rather than completed experiments.

## Offline replay

After extracting the portable ZIP, change into `sam_chapter2/` and verify its
root manifest before replay, because replay regenerates derived summaries:

```sh
sha256sum -c MANIFEST.sha256
python3 -B GEN4/voli_chapter2_physical3_20261015/reproduce.py
```

The scientific replay uses only Python's standard library and starts zero
native operations. It checks exact source identities, retained point-minor
certificates, the worked protocol, and readback of the retained Duck receipts.
The separate source-session and cache audits can also be replayed:

```sh
python3 -B GEN4/voli_chapter2_physical3_20261015/closure/verify_cache_semantics.py
python3 -B GEN4/voli_chapter2_physical3_20261015/packaging/verify_domain_provenance.py
```

`closure/FINAL_CLOSURE.json` records the exact coverage and highest certified
rank for each original preparation. Its offline inverse-row witnesses retain
positive full-Gibbs residual bounds. `packaging/DOMAIN_PROVENANCE_VERIFICATION.json`
authenticates source-session inputs, outputs, original preparation hashes and
frozen executed-code snapshots. Earlier incomplete attempts remain recorded and
are assigned no scientific return. Native inverse checks and source evaluations
have separate provenance from independent offline certificate arithmetic.

## Optional PDF rebuild

Use Python 3.12, the pinned rendering dependencies and bundled fonts:

```sh
cd GEN4/voli_chapter2_physical3_20261015
python3 -m venv .venv-pdf
.venv-pdf/bin/pip install -r chapter/requirements-pdf.lock
.venv-pdf/bin/python -B chapter/build_pdf.py
```

The generated PDF is
`output/pdf/SAM_Volume_I_Chapter_II_Physical_Development_Draft_20261015.pdf`.
The chapter's verification record binds reader content, rendering source,
layout and PDF bytes. Rendering dependencies are unnecessary for scientific
replay; the installed research runtime is not recreated by this packet.

## Portable evidence and delivery build

The release preserves project-relative source paths. `SOURCE_DEPENDENCIES.json`
binds original paths to retained bytes; `RECEIPT_CUSTODY_RELOCATIONS.json` keeps
only manifest-listed, hash-matched helper receipts. The predecessor ZIP is
validated completely before extraction. `predecessor_metadata/` preserves its
original root metadata, and all predecessor scientific payloads and PDFs remain
unchanged. Native object stores, runtime copies and worker checkpoints are
excluded; exact source-session calls, frozen code and task envelopes are kept.

The delivery builder requires the previously released continuation ZIP with
SHA-256 `39d339b049e5580b11c4f2c7ec85ad687452c40e6e8e674411e9f8ac7e5e8d93`.
It accepts `--stage-only`, `--stage-root`, `--destination`, and the exact
`--history-entry` path. Its deterministic ZIP manifest authenticates every file.
The builder launches no scientific execution, installation, commit, sync or
repository publication.

The new Duck Connections cycle uses two 180-second admission windows and the
local indexed research corpus. Completed runs, bounded failures, custody and
resource release are documented in `REPORT.md` and the preserved receipts.
