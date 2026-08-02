# Build

The PDFs in the repository root are generated from the markdown next to them. This directory holds the generator so that the PDFs can always be rebuilt, by anyone, from the current source.

**The rule that matters.** The README points readers at the PDFs, so the PDFs are the published document and the markdown is the source. Any change to `OUROBOROS_VISION_v2.md` or `OUROBOROS_IN_BRIEF.md` is not published until the PDFs are rebuilt and committed in the same change. This directory exists because that rule was broken once: the build script lived only in a temporary environment, the environment was reset, and the PDFs sat five commits behind the markdown carrying terminology that had already been withdrawn.

## Rebuilding

```
pip install weasyprint markdown --break-system-packages

mkdir -p fonts && cd fonts
for w in Light Regular Medium SemiBold Bold Italic SemiBoldItalic; do
  curl -fsSLO "https://raw.githubusercontent.com/google/fonts/main/ofl/spectral/Spectral-$w.ttf"
done
cd ..

OURO_REPO=/path/to/repo python3 build.py both
```

`OURO_REPO` defaults to `./repo`. Pass `vision` or `brief` instead of `both` to build one.

## Two things that will waste an hour if you do not know them

**WeasyPrint ignores `@font-face` unless you pass a `FontConfiguration`.** It does this silently, with no warning and no error. The document renders, the fonts are simply wrong. This is how the previously published PDFs lost Spectral and fell back to DejaVu Serif without anyone noticing, because every check being run was textual rather than visual. `build.py` passes the configuration to both `CSS()` and `write_pdf()`. Verify a build with `pdffonts OUROBOROS_VISION_v2.pdf` and expect to see Spectral, not DejaVu. The stylesheet declares `Spectral, serif` at every use site so that a future failure degrades to a serif rather than to a sans, which makes the failure visible at a glance.

**The Google Fonts download endpoint does not return a usable archive.** Pull individual TTFs from `raw.githubusercontent.com/google/fonts/main/ofl/spectral/` as in the command above. The fonts are not committed here; Spectral is under the SIL Open Font License and redistributing it would mean carrying that license too, which is avoidable when a fetch is one line.

## Design values

Sampled from the published PDFs so a rebuild matches rather than drifts.

| Role | Value |
|---|---|
| Bone, page background | `#F3EEE3` |
| Ebony, body text | `#16150F` |
| Slate, bold lead-ins and secondary headings | `#3C3A33` |
| Ash, page numbers | `#807C76` |
| Gold, rules and accents | `#A8894C` |
| Pale gold, cover subtitle and ornaments | `#D5C5A3` |
| Cover field | true black `#000000` |

Letter page, Spectral throughout, justified body, letter-spaced uppercase section headings over a gold hairline, page numbers centered in ash, covers full-bleed black carrying the sigil from `../assets`. The Vision uses the hollow sigil variant and the In Brief uses the one with the luminous center.

## Checking a build

```
pdfinfo  OUROBOROS_VISION_v2.pdf     # page count and letter geometry
pdffonts OUROBOROS_VISION_v2.pdf     # must show Spectral
pdftotext -layout OUROBOROS_VISION_v2.pdf - | head -40
```

Then confirm every markdown heading and every bold lead-in survived into the PDF. Extraction letter-spaces the headings, so a plain string search for a heading will fail even when the heading is present. Strip non-alphanumerics from both sides before comparing.
