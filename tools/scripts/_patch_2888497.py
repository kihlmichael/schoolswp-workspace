#!/usr/bin/env python3
"""Build patched content + slug for post 2888497 (DE).

Patches applied (P1 + P2 automatable):
  1. CTA text "Get my discount" -> "Ninja Tables Pro testen"  (x2)
  2. CTA link /fluentcrm -> /ninja-tables/                    (x2)
  3. "Nachdem wir uns mit den Grundlagen..." -> singular voice
  4. "Nachdem wir nun ... wollen wir uns..."  -> singular voice
  5. En-dash " - " -> ": "                                    (x1)
  6. Inject Rank Math TOC block after intro callout
  7. Slug: ninja-tables-datatables-grose-datensatze -> grosse-datensaetze

Writes content/articles/_workspace/post-2888497-patched.html for diffing.
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "articles" / "_workspace" / "post-2888497-current.json"
OUT_HTML = ROOT / "content" / "articles" / "_workspace" / "post-2888497-patched.html"
OUT_DIFF = ROOT / "content" / "articles" / "_workspace" / "post-2888497-diff.txt"

NEW_SLUG = "ninja-tables-datatables-grosse-datensaetze"

# -- Patch table --------------------------------------------------------
# Each entry: (search, replace, expected_count). expected_count=None to skip count check.
PATCHES = [
    # 1) CTA text
    (
        '"text":"Get my discount"',
        '"text":"Ninja Tables Pro testen"',
        2,
    ),
    # 2) CTA link (json side)
    (
        '"link":"https://schoolswp.com/fluentcrm"',
        '"link":"https://schoolswp.com/ninja-tables/"',
        2,
    ),
    # 2b) CTA link (html side) - check if any <a href> still points there
    (
        'href="https://schoolswp.com/fluentcrm"',
        'href="https://schoolswp.com/ninja-tables/"',
        None,
    ),
    # 3) singular voice - intro of section "3 Einstellungen"
    (
        "Nachdem wir uns mit den Grundlagen von Ninja Tables befasst haben",
        "Nachdem ich Ihnen die Grundlagen von Ninja Tables gezeigt habe",
        1,
    ),
    # 4) singular voice - between sections (combined sentence)
    (
        "Nachdem wir nun die technische Überlegenheit festgestellt haben, wollen wir uns ansehen",
        "Nachdem die technische Überlegenheit klar ist, zeige ich Ihnen jetzt",
        1,
    ),
    # 5) en-dash
    (
        "dem Import – ein gewaltiger",
        "dem Import: ein gewaltiger",
        1,
    ),
]

# -- TOC insertion point ------------------------------------------------
# Insert just before the first H2 "Warum die Ninja Tables DataTables-Engine..."
TOC_BLOCK = (
    "\n\n<!-- wp:rank-math/toc-block "
    '{"title":"Inhaltsverzeichnis","collapsible":true,"collapsibleByDefault":false,"listStyle":"ul",'
    '"excludeHeadings":{"h1":true,"h4":true,"h5":true,"h6":true}} -->\n'
    '<div class="wp-block-rank-math-toc-block"><h2>Inhaltsverzeichnis</h2></div>\n'
    "<!-- /wp:rank-math/toc-block -->\n\n"
)

TOC_ANCHOR_BEFORE = "<!-- wp:heading -->\n<h2 class=\"wp-block-heading\""
# We'll find the FIRST H2 wrapper and insert TOC before it. The kadence callout intro must end first.


def main():
    d = json.loads(SRC.read_text(encoding="utf-8"))
    content = d.get("content", {}).get("raw", "")
    original_len = len(content)

    diff_lines = []
    diff_lines.append(f"# Patch report for post 2888497")
    diff_lines.append(f"original content length: {original_len} chars\n")

    for search, replace, expected in PATCHES:
        cnt = content.count(search)
        if expected is not None and cnt != expected:
            diff_lines.append(
                f"!! count mismatch for: {search[:80]!r}  found={cnt} expected={expected}"
            )
            if cnt == 0:
                continue  # nothing to do
        content = content.replace(search, replace)
        diff_lines.append(f"OK x{cnt}: {search[:60]!r}  ->  {replace[:60]!r}")

    # TOC insertion: find first H2 wp-block
    # Look for pattern: kadence/column closing of the intro callout, then first H2 wrapper.
    # Safer: anchor on the title text of the first H2.
    first_h2_marker = "Warum die Ninja Tables DataTables-Engine den entscheidenden Unterschied macht"
    # Find the position of this text, then walk backward to find the H2 block opening
    idx = content.find(first_h2_marker)
    if idx < 0:
        diff_lines.append("!! could not locate first H2 anchor (TOC insertion skipped)")
    else:
        # Walk back to find "<!-- wp:" comment that introduces the H2 block (kadence/heading or core/heading)
        back_block = content.rfind("<!-- wp:", 0, idx)
        if back_block < 0:
            diff_lines.append("!! could not find wp comment before H2 (TOC insertion skipped)")
        else:
            content = content[:back_block] + TOC_BLOCK + content[back_block:]
            diff_lines.append(
                f"OK TOC inserted at offset {back_block} (before first H2 wp-block)"
            )

    OUT_HTML.write_text(content, encoding="utf-8")
    diff_lines.append(f"\npatched length: {len(content)} chars (delta {len(content)-original_len:+d})")
    OUT_DIFF.write_text("\n".join(diff_lines), encoding="utf-8")

    print("\n".join(diff_lines))
    print(f"\n[write] {OUT_HTML}")
    print(f"[write] {OUT_DIFF}")
    print(f"[slug] new -> {NEW_SLUG}")


if __name__ == "__main__":
    main()
