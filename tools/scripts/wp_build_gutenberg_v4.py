#!/usr/bin/env python3
"""
Build a proper Gutenberg-block version of v4 content for post 52944.

Inputs:
  - content/articles/lms-pilier/v4-optimized.html  (raw HTML draft)
  - content/articles/lms-pilier/backups/52944-pre-v4-*.json  (Kadence callout + TOC)

Output:
  - content/articles/lms-pilier/v4-gutenberg.html

Approach:
  - Drop the breadcrumb and manual TOC (will use Kadence TOC block instead)
  - Drop H1 (Gutenberg uses post_title, no H1 in body)
  - Drop <section> wrappers (not a Gutenberg construct)
  - Convert <p> to wp:paragraph, <h2>/<h3> to wp:heading, <ul>/<li> to wp:list
  - Preserve the Kadence callout from original at its original position (post-intro)
  - Insert Kadence TOC block from original after callout
  - Wrap FAQ items (with itemprop microdata) in wp:html blocks
  - End with the rank_math_rich_snippet shortcode (preserved from original)
"""

import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_HTML = ROOT / "content" / "articles" / "lms-pilier" / "v4-optimized.html"
BACKUP_GLOB = str(ROOT / "content" / "articles" / "lms-pilier" / "backups" / "52944-pre-v4-*.json")
OUT = ROOT / "content" / "articles" / "lms-pilier" / "v4-gutenberg.html"


def load_kadence_blocks():
    """Extract the Kadence rowlayout callout, TOC block, and shortcode from backup."""
    backup_files = sorted(glob.glob(BACKUP_GLOB))
    raw = json.loads(Path(backup_files[-1]).read_text(encoding="utf-8"))["content"]["raw"]

    # 1) Kadence rowlayout callout (depth-balanced extraction)
    start = raw.find("<!-- wp:kadence/rowlayout")
    depth = 0
    i = start
    while i < len(raw):
        if raw.startswith("<!-- wp:kadence/rowlayout", i):
            depth += 1
        elif raw.startswith("<!-- /wp:kadence/rowlayout -->", i):
            depth -= 1
            if depth == 0:
                end = i + len("<!-- /wp:kadence/rowlayout -->")
                break
        i += 1
    callout = raw[start:end]

    # 2) Kadence TOC self-closing block
    toc_m = re.search(r"<!-- wp:kadence/tableofcontents[^/]*?/-->", raw)
    toc = toc_m.group(0) if toc_m else ""

    # 3) RM rich snippet shortcode block
    sc_m = re.search(r"<!-- wp:shortcode -->\s*\[rank_math_rich_snippet[^\]]*\]\s*<!-- /wp:shortcode -->", raw)
    sc = sc_m.group(0) if sc_m else ""

    return callout, toc, sc


def strip_html_comments(s):
    return re.sub(r"<!--.*?-->", "", s, flags=re.DOTALL)


def parse_v4_sections(html):
    """Strip wrapping comments and <section>, return ordered HTML element list."""
    html = strip_html_comments(html)
    # Remove <section> tags but keep content
    html = re.sub(r"</?section[^>]*>", "", html)
    # Remove H1 (post_title handles it)
    html = re.sub(r"<h1[^>]*>.*?</h1>", "", html, flags=re.DOTALL)
    # Remove the breadcrumb paragraph (contains "Vous êtes ici")
    html = re.sub(r"<p[^>]*>Vous êtes ici.*?</p>", "", html, flags=re.DOTALL)
    # Remove the manual sommaire <h2>Sommaire</h2><ul>...</ul>
    html = re.sub(r"<h2[^>]*>Sommaire</h2>\s*<ul[^>]*>.*?</ul>", "", html, flags=re.DOTALL)
    return html


def to_gutenberg(html, kadence_callout, kadence_toc, rm_shortcode):
    """Walk the HTML, emit Gutenberg block markup."""
    out_parts = []

    # Tokenize top-level elements: h2, h3, p, ul, div (faq itemscope)
    # We'll use a regex that matches top-level blocks one at a time.
    # Simpler: split by major tags using lxml-like approach? Stay regex.
    pattern = re.compile(
        r"<h2[^>]*>.*?</h2>"
        r"|<h3[^>]*>.*?</h3>"
        r"|<ul[^>]*>.*?</ul>"
        r"|<p[^>]*>.*?</p>"
        r"|<div[^>]*itemscope[^>]*>.*?</div>\s*</div>\s*</div>",  # FAQ Q/R div
        re.DOTALL,
    )

    intro_done = False
    callout_inserted = False
    toc_inserted = False

    for m in pattern.finditer(html):
        chunk = m.group(0).strip()
        if not chunk:
            continue
        tag = re.match(r"<(\w+)", chunk).group(1).lower()

        if tag == "h2":
            # extract id and text
            id_m = re.search(r'id="([^"]+)"', chunk)
            txt_m = re.search(r"<h2[^>]*>(.*?)</h2>", chunk, re.DOTALL)
            txt = txt_m.group(1).strip()
            attrs = f' id="{id_m.group(1)}"' if id_m else ""
            heading = f'<!-- wp:heading -->\n<h2 class="wp-block-heading"{attrs}>{txt}</h2>\n<!-- /wp:heading -->'

            # Insert Kadence callout + TOC before the FIRST H2
            if not intro_done:
                if kadence_callout and not callout_inserted:
                    out_parts.append(kadence_callout)
                    callout_inserted = True
                if kadence_toc and not toc_inserted:
                    out_parts.append(kadence_toc)
                    toc_inserted = True
                intro_done = True
            out_parts.append(heading)

        elif tag == "h3":
            id_m = re.search(r'id="([^"]+)"', chunk)
            txt_m = re.search(r"<h3[^>]*>(.*?)</h3>", chunk, re.DOTALL)
            txt = txt_m.group(1).strip()
            attrs = f' id="{id_m.group(1)}"' if id_m else ""
            out_parts.append(
                f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading"{attrs}>{txt}</h3>\n<!-- /wp:heading -->'
            )

        elif tag == "ul":
            # Convert <ul><li>X</li>...</ul> to wp:list with wp:list-item children
            li_items = re.findall(r"<li[^>]*>(.*?)</li>", chunk, re.DOTALL)
            li_blocks = []
            for li in li_items:
                li = li.strip()
                li_blocks.append(f"<!-- wp:list-item -->\n<li>{li}</li>\n<!-- /wp:list-item -->")
            list_inner = "\n\n".join(li_blocks)
            out_parts.append(f'<!-- wp:list -->\n<ul class="wp-block-list">{list_inner}</ul>\n<!-- /wp:list -->')

        elif tag == "p":
            txt_m = re.search(r"<p[^>]*>(.*?)</p>", chunk, re.DOTALL)
            txt = txt_m.group(1).strip()
            if not txt:
                continue
            out_parts.append(f"<!-- wp:paragraph -->\n<p>{txt}</p>\n<!-- /wp:paragraph -->")

        elif tag == "div":
            # FAQ Q/R block with itemscope microdata - use wp:html
            out_parts.append(f"<!-- wp:html -->\n{chunk}\n<!-- /wp:html -->")

    # Append the rank_math_rich_snippet shortcode at the end (after FAQ)
    if rm_shortcode:
        out_parts.append(rm_shortcode)

    return "\n\n".join(out_parts) + "\n"


def main():
    html = SRC_HTML.read_text(encoding="utf-8")
    callout, toc, sc = load_kadence_blocks()
    print(f"[info] callout: {len(callout)} chars")
    print(f"[info] toc: {len(toc)} chars")
    print(f"[info] shortcode: {sc!r}")

    cleaned = parse_v4_sections(html)
    output = to_gutenberg(cleaned, callout, toc, sc)
    OUT.write_text(output, encoding="utf-8")
    print(f"[ok] wrote {OUT} ({len(output)} chars)")

    # Quick stats
    block_types = re.findall(r"<!-- wp:([a-z0-9/-]+)", output)
    from collections import Counter

    print("[stats] block types:")
    for bt, n in Counter(block_types).most_common():
        print(f"   {bt}: {n}")


if __name__ == "__main__":
    main()
