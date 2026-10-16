# Companion Chapter II source-to-field update

This reader preserves all forty sections of the completed twenty-page
`voli_chapter2_physical3_20261015` reader and appends sections41-48, four pages,
from the Chapter III source-field campaign. The abstract is updated. The
previous scientific source/closure values remain frozen in FINAL_CLOSURE.json.
The prior source [12] still identifies the completed physical-development
packet; [13] identifies the new source, radial, energy and clock results.

The full previous scientific evidence remains in its preserved portable ZIP.
That predecessor is not replaced by these manuscript sources. The parent
campaign archive includes predecessor custody/dependency records and the new
checks. Use root reproduce.py for scientific replay.

Build with the pinned reportlab/matplotlib/svglib/PDF environment:

    python3 chapter2/build_pdf.py
    python3 chapter2/verify_pdf.py

The output is
`output/pdf/SAM_Volume_I_Chapter_II_Source_to_Field_Update_20261015.pdf`.
Both commands work after relocation. Bundled fonts and FINAL_CLOSURE.json are
the only non-code build inputs. PDF_VERIFICATION.json records section/layout
checks and a fresh-cache, byte-identical rebuild; visual review is recorded
separately after page-image inspection.
