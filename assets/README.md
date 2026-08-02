# Sigil

The mark used on the covers of the documents in this repository, in two variants.

| File | Variant | Cover |
|---|---|---|
| `ouroboros-sigil-core.png` | luminous center | `OUROBOROS_IN_BRIEF.pdf` |
| `ouroboros-sigil-hollow.png` | center removed | `OUROBOROS_VISION_v2.pdf` |

Both are 1100 by 1100 pixel RGB PNGs intended for a black field. The serpent renders dark blue-black with gold filigree and pale cyan nodes, so it needs a dark background to stay legible.

**Origin.** The image was machine-generated on 2026-06-15 from a written prompt, then prepared for the two covers. The hollow variant is the same render with the center removed by image math, which is why the two files are identical outside the middle.

**Recovery.** Until 2026-08-01 the sigil existed only inside the two published PDFs. These files were recovered from those covers with:

```
pdfimages -png -f 1 -l 1 OUROBOROS_IN_BRIEF.pdf sigil
```

They are committed here so that extraction is not needed again.

Use is governed by the `LICENSE` file at the repository root.
