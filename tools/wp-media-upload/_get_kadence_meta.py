"""Read current Kadence page-meta values for a given page id."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SETTINGS = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/settings.local.json")

KAD_KEYS = [
    "_kad_post_header",
    "_kad_post_footer",
    "_kad_post_title",
    "_kad_post_layout",
    "_kad_post_content_style",
    "_kad_post_feature",
    "_kad_post_feature_position",
    "_kad_post_vertical_padding",
    "_kad_post_transparent",
    "_kad_post_sidebar_id",
    "_kad_post_classname",
]


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
    r = requests.get(
        f"{base}/wp/v2/pages/{page_id}",
        params={"context": "edit"},
        auth=auth,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    r.raise_for_status()
    meta = (r.json().get("meta") or {})
    out = {k: meta.get(k, "<<missing>>") for k in KAD_KEYS}
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1])))
