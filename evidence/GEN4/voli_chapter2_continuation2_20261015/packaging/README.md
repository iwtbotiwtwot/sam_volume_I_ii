# Portable research deliverable

Run `python3 GEN4/voli_chapter2_continuation2_20261015/packaging/build_bundle.py` from the project tree after the delivery records and final PDF exist. It writes the requested ZIP and PDF into Downloads, with its receipt in `packaging/BUNDLE.json`.

`--stage-only` prepares `/tmp/sam-chapter2-continuation-portable-stage/sam_chapter2` and verifies every staged checksum without publishing either file. Replay changes derived reports, so verify `MANIFEST.sha256` before running `reproduce.py`, and rebuild the stage before final ZIP publication.

The bundle preserves all 180 declared original memory source files, the direct Chapter I/II dependencies, original native requests/receipts, and the authenticated local source-search index. It omits Duck installations, checkpoints and worker runtime trees. Five original helper receipts are copied from retained RAM custody only when the original receipt hash, RAM_CUSTODY entry and HELPER_READBACK entry all agree. Scientific receipts are never rewritten.

Offline reproduction uses Python's standard library and launches zero native calculations. PDF generation has its separate pinned dependencies and bundled fonts in `chapter/`.
