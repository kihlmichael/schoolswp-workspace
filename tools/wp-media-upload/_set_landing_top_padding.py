"""Restore vertical padding above the first rowlayout on the landing page
2867562 and inject a per-page custom CSS rule that guarantees breathing room
between the schoolsWP header and the hero rowlayout.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SETTINGS = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/settings.local.json")

# Scoped to this page (`_kad_blocks_custom_css` is already a per-page meta,
# but we add the body class anchor for extra specificity since Kadence
# inlines this CSS into the page head, after the theme stylesheet).
CUSTOM_CSS = """\
body.page-id-2867562 .entry-content > .wp-block-kadence-rowlayout:first-child > .kt-row-column-wrap,
body.page-id-2867562 .single-content > .wp-block-kadence-rowlayout:first-child > .kt-row-column-wrap,
body.page-id-2867562 .kb-row-layout-id2867562_b9c9f2-5c > .kt-row-column-wrap {
  padding-top: clamp(112px, 12vw, 192px) !important;
}
"""

PATCH = {
    "_kad_post_vertical_padding": "default",
    "_kad_blocks_custom_css": CUSTOM_CSS,
}


def load_wp():
    raw = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = raw["env"]
    url = env["WP_API_URL"].rstrip("/")
    if url.endswith("/wp-json"):
        base = url
    elif "/wp-json" in url:
        base = url.split("/wp-json")[0] + "/wp-json"
    else:
        base = f"{url}/wp-json"
    return base, (env["WP_API_USERNAME"], env["WP_API_PASSWORD"])


def main(page_id: int) -> int:
    base, auth = load_wp()
    payload = {"meta": PATCH}
    r = requests.post(
        f"{base}/wp/v2/pages/{page_id}",
        json=payload,
        auth=auth,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=60,
    )
    if r.status_code not in (200, 201):
        print(f"FAIL HTTP {r.status_code}: {r.text[:500]}", file=sys.stderr)
        return 2
    data = r.json()
    meta = data.get("meta") or {}
    print("Applied:")
    print(f"  _kad_post_vertical_padding = {meta.get('_kad_post_vertical_padding')!r}")
    print(f"  _kad_blocks_custom_css len = {len(meta.get('_kad_blocks_custom_css') or '')} chars")
    print(f"\nlink: {data.get('link')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1])))
