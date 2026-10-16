# Reproduce Chapters II and III

The ZIP preserves a selected portable project tree. Its root contains
`MANIFEST.sha256`; the campaign is
`GEN4/voli_chapter3_source_field1_20261015/`. The editable Chapter II and III
sources, fonts, dependency locks, delivered PDFs, original input PDFs, exact
operands, derivations and selected authenticated native receipts are included.

From a fresh extraction, run:

```bash
python3 -B GEN4/voli_chapter3_source_field1_20261015/reproduce.py
```

This first verifies every manifest member and the initial file set, then uses
only the Python standard library to replay the independent source, uniform
coupling, radial, field-energy, clock and kernel checks; regenerate the exact
cube graph fixture; and authenticate/read the completed native outputs. It
does not start Duck, a mathematical engine, a service, a physical experiment,
an installation or a network connection. The retained native calls remain
evidence from their original two180-second research windows.

The source checks comprise2,040 source assertions,23 uniform-response
assertions,312 radial assertions,52 static-field assertions,822 clock
assertions,47 correlated-phase assertions and45 kernel/frozen-input
assertions:3,341 in total. The correlated-phase supplement uses the original
six-lane bounds and frozen physical anchor; it preserves the native-bound
`clock/RESULTS.json` byte-for-byte and launches no additional native calls.
Native matrix-entry,
interval-equation and custody checks are reported separately by
`verify_native.py`. Its targets are eleven actual native outputs and four
authenticated local-retrieval receipts; it obtains counts from completed
receipts rather than treating a prepared plan as execution.

Replay rewrites derived verification reports. Before repeating replay in that
same working copy, either extract a fresh copy or explicitly use
`--skip-manifest`. The original manifest applies to the delivered bytes before
those derived outputs are regenerated. Source-bound operands must remain
unchanged. `--source-only` is a development preflight that omits native
readback and reports `SOURCE_ONLY_PASS`, rather than a complete replay verdict.

## Optional PDF reproduction

PDF verification requires the already installed Python3.12 packages pinned in
both `chapter2/requirements-pdf.lock` and `chapter3/requirements-pdf.lock`.
No packages are installed by replay. An optional manually created environment
can be populated from that lock with the user's usual package source.
Then, in a fresh extraction, run:

```bash
python3 -B GEN4/voli_chapter3_source_field1_20261015/reproduce.py --pdf
```

The two PDF verifiers check content, vector equations, embedded fonts and
layout, and build each manuscript in a separate temporary directory with a
fresh equation cache. Each rebuilt PDF must be byte-identical to its delivered
counterpart. Main PDFs are not overwritten. The separate retained visual-QA
records describe the parent's page review; automated layout checks are not
reported as that visual review.

## Evidence selection and original paths

`SOURCE_DEPENDENCIES.json` binds retained files to their original project paths,
hashes, byte counts and roles. Original absolute paths inside scientific
receipts are preserved. Portable readback maps only the declared original
project prefix into the extraction root.

Helper records are accepted only when the original path is under the exact
scratch prefix in `RAM_CUSTODY.json` and the same relative file is listed in
both that manifest and `HELPER_READBACK.json`, with matching SHA-256 and byte
count. `RECEIPT_CUSTODY_RELOCATIONS.json` records every selected relocation.
Basename searches and guessed retained paths are not used.

The portable archive is a **selected evidence subset**. It retains the complete
original custody manifests while copying only helper files actually needed for
the selected receipts. The complete runtime and retained-RAM tree remain in
the original project. Bulk R3 state/object stores and checkpoints are not
included. Prepared, unlaunched predecessor attempts remain identified as such;
their metadata is not counted as native science.

Fresh native reexecution is a separate explicit action. It requires the
qualified installed project/runtime, capability discovery, a fresh run identity,
original source bindings and the declared resource/cycle policy. The portable
replay command neither supplies a replacement runtime nor relaunches an old
completed or prepared campaign. The builder and replay perform no I9 access,
commit or synchronization.
