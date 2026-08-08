#!/usr/bin/env python3
"""Ouroboros PDF build.

Rebuilt 2026-08-02. The original was sandbox-only and lost to a reset, which
froze the published PDFs while the markdown moved on. This version is committed
to the repository so that does not happen again.

Usage:
    python3 build.py vision   # OUROBOROS_VISION_v2.md  -> OUROBOROS_VISION_v2.pdf
    python3 build.py brief    # OUROBOROS_IN_BRIEF.md   -> OUROBOROS_IN_BRIEF.pdf
    python3 build.py both

Requires: weasyprint, markdown, the Spectral TTFs in ./fonts, and the sigil
PNGs from the repository assets directory.

    pip install weasyprint markdown --break-system-packages
    curl -fsSLO https://raw.githubusercontent.com/google/fonts/main/ofl/spectral/Spectral-Regular.ttf
    (and Light, Medium, SemiBold, Bold, Italic, SemiBoldItalic, into ./fonts)

The Google Fonts zip endpoint does not return a usable archive; pull the
individual TTFs from the path above.
"""

import io
import os
import re
import sys

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("OURO_REPO", os.path.join(HERE, "repo"))

VARIANTS = {
    "vision": {
        "src": "OUROBOROS_VISION_v2.md",
        "out": "OUROBOROS_VISION_v2.pdf",
        "sigil": "assets/ouroboros-sigil-hollow.png",
        "cover_title": "Ouroboros",
        "designator": "",
        "title_page_title": "Ouroboros",
        "body_class": "vision",
    },
    "brief": {
        "src": "OUROBOROS_IN_BRIEF.md",
        "out": "OUROBOROS_IN_BRIEF.pdf",
        "sigil": "assets/ouroboros-sigil-core.png",
        "cover_title": "Ouroboros",
        "designator": "In Brief",
        "title_page_title": "Ouroboros in Brief",
        "body_class": "brief",
    },
}

SUBTITLE_VISION = ("Self-Auditing Governance That Starts at Community Scale "
                   "and Grows Only by Consent")
SUBTITLE_BRIEF = "The whole idea in five minutes"

LICENSE_LINE = "Released under Creative Commons Attribution-ShareAlike 4.0"
REPO_URL = "github.com/Preston2012/ouroboros"
REPO_URL_BASE = "https://github.com/Preston2012/ouroboros/blob/main/"
AUTHOR = "Preston T. Winters"
AUTHOR_LINE = "Authored by Preston T. Winters with Claude (Anthropic)"


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def split_front_matter(text):
    """Return (front_matter, body). Front matter is everything before the first
    horizontal rule on its own line. Both source documents use that shape."""
    parts = re.split(r"\n---+\s*\n", text, maxsplit=1)
    if len(parts) != 2:
        raise SystemExit("could not find the front-matter rule in the source")
    return parts[0], parts[1]


def detect_version(front):
    m = re.search(r"Version\s+(\d+\.\d+)", front)
    return m.group(1) if m else ""


def render_body(body_md):
    # Relative links work on GitHub and are dead in a downloaded PDF, which is
    # the file most people actually keep. Rewrite them to absolute repository
    # URLs so the PDFs stand alone.
    body_md = re.sub(r'\]\(\./', "](" + REPO_URL_BASE, body_md)
    body_md = re.sub(r'\]\(\.\./', "](" + REPO_URL_BASE, body_md)

    # Source markdown is deliberately plain ASCII so it greps cleanly and
    # copies safely. Typographic quotes are produced here at render time
    # instead. Dash and ellipsis substitution stays off: this project does not
    # use em dashes anywhere, and smarty would introduce them from "--".
    return markdown.markdown(
        body_md,
        extensions=["tables", "attr_list", "sane_lists", "md_in_html", "smarty"],
        extension_configs={"smarty": {"smart_quotes": True,
                                      "smart_dashes": False,
                                      "smart_ellipses": False,
                                      "smart_angled_quotes": False}},
        output_format="html5",
    )


def build(variant):
    cfg = VARIANTS[variant]
    src = os.path.join(REPO, cfg["src"])
    out = os.path.join(REPO, cfg["out"])
    sigil = os.path.join(REPO, cfg["sigil"])
    for p in (src, sigil):
        if not os.path.exists(p):
            raise SystemExit("missing input: %s" % p)

    front, body_md = split_front_matter(read(src))
    version = detect_version(front)
    subtitle = SUBTITLE_VISION if variant == "vision" else SUBTITLE_BRIEF
    body_html = render_body(body_md)

    # The version and provenance lines from the source front matter carry
    # forward onto the title page verbatim, so the PDF never disagrees with
    # the markdown about what version it is.
    front_lines = [l.strip().strip("*") for l in front.splitlines()
                   if l.strip().startswith("*")]
    # Drop any front-matter line that merely restates the subtitle already
    # printed above it, so the title page does not say the same thing twice.
    front_lines = [l for l in front_lines
                   if not l.lower().startswith(subtitle.lower())]
    meta_html = "".join(
        '<div class="%s">%s</div>' % ("strongline" if i == 0 else "quiet", l)
        for i, l in enumerate(front_lines))

    html = """<!DOCTYPE html>
<html lang="en" class="%(body_class)s">
<head><meta charset="utf-8"><title>%(cover_title)s</title></head>
<body>

<section class="cover">
  <div class="cover-inner">
    <img src="%(sigil)s" alt="">
    <h1>%(cover_title)s</h1>
    <div class="desig">%(designator)s</div>
    <div class="sub">%(subtitle)s</div>
    <div class="rule"></div>
    <div class="ver">Version %(version)s</div>
    <div class="byline">%(author)s</div>
  </div>
</section>

<section class="titlepage">
  <h1>%(title_page_title)s</h1>
  <div class="sub">%(subtitle)s</div>
  <div class="rule"></div>
  <div class="meta">
    %(meta)s
    <div class="quiet">%(author_line)s</div>
    <div class="quiet">%(license)s</div>
    <div class="quiet">%(url)s</div>
  </div>
</section>

<section class="body">
%(body)s
</section>

</body></html>""" % {
        "body_class": cfg["body_class"],
        "cover_title": cfg["cover_title"],
        "designator": cfg["designator"],
        "title_page_title": cfg["title_page_title"],
        "subtitle": subtitle,
        "sigil": "file://" + sigil,
        "version": version,
        "author": AUTHOR,
        "author_line": AUTHOR_LINE,
        "license": LICENSE_LINE,
        "url": REPO_URL,
        "meta": meta_html,
        "body": body_html,
    }

    # FontConfiguration is mandatory. Without it WeasyPrint silently ignores
    # every @font-face rule and falls back, which is how the previously
    # published PDFs lost Spectral without anyone noticing.
    font_config = FontConfiguration()
    css = CSS(filename=os.path.join(HERE, "ouroboros.css"), font_config=font_config)
    HTML(string=html, base_url=HERE).write_pdf(
        out, stylesheets=[css], font_config=font_config)
    print("built %s (version %s)" % (out, version))
    return out


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    targets = list(VARIANTS) if which == "both" else [which]
    for t in targets:
        if t not in VARIANTS:
            raise SystemExit("unknown variant: %s" % t)
        build(t)


if __name__ == "__main__":
    main()
