"""Flip a Kadence page into 'landing page full-screen' mode by patching
the Kadence post-meta fields exposed in the editor's Page Layout panel.

Sets:
  _kad_post_header           -> false (already false on this page)
  _kad_post_footer           -> false (already false on this page)
  _kad_post_title            -> "hide"
  _kad_post_layout           -> "fullwidth"
  _kad_post_content_style    -> "unboxed"
  _kad_post_feature          -> "hide"   # don't show the featured image banner
  _kad_post_vertical_padding -> "hide"
  _kad_post_transparent      -> "enable" # makes the (already hidden) header transparent if user re-enables

Usage:
  .venv/Scripts/python tools/wp-media-upload/_set_kadence_landing.py 2867562
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SETTINGS = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/settings.local.json")

LANDING_META: dict[str, object] = {
    "_kad_post_header": False,
    "_kad_post_footer": False,
    "_kad_post_title": "hide",
    "_kad_post_layout": "fullwidth",
    "_kad_post_content_style": "unboxed",
    "_kad_post_feature": "hide",
    "_kad_post_vertical_padding": "hide",
    "_kad_post_transparent": "enable",
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
    headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

    payload = {"meta": LANDING_META}
    print(f"PATCH {base}/wp/v2/pages/{page_id}")
    print(f"  meta payload: {json.dumps(LANDING_META, ensure_ascii=False)}")

    r = requests.post(
        f"{base}/wp/v2/pages/{page_id}",
        json=payload,
        auth=auth,
        headers=headers,
        timeout=60,
    )
    if r.status_code not in (200, 201):
        print(f"FAIL HTTP {r.status_code}: {r.text[:500]}", file=sys.stderr)
        return 2

    data = r.json()
    meta = data.get("meta") or {}
    print("\nApplied meta (server-side echo):")
    for key in LANDING_META:
        print(f"  {key}: {meta.get(key, '<<missing>>')}")
    print(f"\nstatus={data.get('status')}  link={data.get('link')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1])))
