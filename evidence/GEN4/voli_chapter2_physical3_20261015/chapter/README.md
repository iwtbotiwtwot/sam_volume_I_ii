# Editable Chapter II physical-development reader

`content.py` is the editable manuscript. `continuation_content.py` and
`previous_content.py` preserve prior reader sources; the first fourteen sections
are reused verbatim. `content.py` reads the source-approved closure summary from
`../closure/FINAL_CLOSURE.json`. Retain that file beside this chapter when
building a standalone copy. No scientific runtime imports are needed to render.

Use Python3.12 with `requirements-pdf.lock`. The bundled font files and their
copyright notices travel with this source. The renderer is unchanged from the
qualified previous build, with its identity recorded in INHERITED_RENDERER.json.

```
python chapter/build_pdf.py
python chapter/verify_pdf.py
```

The build uses deterministic PDF metadata and writes
`output/pdf/SAM_Volume_I_Chapter_II_Physical_Development_Draft_20261015.pdf`.
`LAYOUT.json` records forty non-overflowing column frames. Equation widths are
checked during the build, including a minimum effective size of8.1points.
`verify_pdf.py` checks page/section preservation, embedded fonts, source hashes
and a byte-identical fresh-cache relocated build. It is an artifact check,
not a scientific or native computation. Render with Poppler and visually inspect
pages after meaningful content changes; PDF_VERIFICATION.json records the
completed visual review of this version.
