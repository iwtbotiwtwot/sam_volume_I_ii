# Chapter III source-to-field pass and Chapter II interface revision

Start with REPORT.md and the two PDFs under output/pdf/. ChapterIII has14pages;
the companion ChapterII has24pages and preserves its preceding40sections.

- source/: actual Si29 effects, declared finite cube, exact uniform-coupling response.
- radial/: finite conductance source/field/flux/force and controlled radial limit.
- energy/: static domain/minimum/pair-force proofs and ChapterI free-field example.
- clock/: complete-H response, six-lane diagnostics and correlated phase bounds.
- core/: exact kernel checks and frozen CR004 arithmetic.
- chapter2/,chapter3/: editable readers, embedded fonts, pinned requirements and QA.
- inputs/: preserved PDFs, exact corpus snapshot and capabilities.
- verify_native.py: independent native receipt/source/interval readback, no execution.
- reproduce.py and REPRODUCIBILITY.md: portable offline checks; optional PDF rebuild.

Actual science run: GEN4/duck_gen6_local/runs/chapter3-source-field-20261015-03.
Mode:Connections;6controllers/3helpers;profileA;two180-second windows. Parent and
allfour selected targets retained. No automatic third round or repeat. Completed
receipts outrank older STATUS snapshots. Read FOLLOW_UP.md for the precise next
physical coupling/localization work; this folder is not permission to relaunch.

Runtime concurrency qualification is a separate engineering campaign:
GEN4/duck_dual_session_topology1_20261015, H002640. It does not count as chapter
scientific evidence. It preserves the mathematical core and verifies two sessions
on disjoint CPU sets with only per-core leases.

Sean Brady:originator/conceptual director. OpenAI ChatGPT and Codex:research
collaborators. No commit, publication, sync or I9 operation is part of this pass.
