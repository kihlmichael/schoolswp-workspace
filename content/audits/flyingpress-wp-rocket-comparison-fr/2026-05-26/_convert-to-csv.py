"""Convert DataForSEO ranked_keywords JSON dumps to CSV for Sheets upload."""
import json
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

CASES = [
    {
        "json": ROOT / "flyingpress-wp-rocket-comparison-fr" / "2026-05-26" / "dataforseo-ranked-keywords-fr.json",
        "csv": ROOT / "flyingpress-wp-rocket-comparison-fr" / "2026-05-26" / "dataforseo-ranked-keywords-fr.csv",
        "label": "schoolswp.com FR (France, fr)",
    },
    {
        "json": ROOT / "flyingpress-wp-rocket-comparison-de" / "2026-05-26" / "dataforseo-ranked-keywords-de.json",
        "csv": ROOT / "flyingpress-wp-rocket-comparison-de" / "2026-05-26" / "dataforseo-ranked-keywords-de.csv",
        "label": "schoolswp.com DE (Germany, de)",
    },
]


def safe_get(d, *keys, default=None):
    for k in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(k, None)
        if d is None:
            return default
    return d


for case in CASES:
    raw = case["json"].read_text(encoding="utf-8")
    # The dump may be the MCP-wrapped envelope or the raw items array; normalise.
    data = json.loads(raw)
    if isinstance(data, dict) and "tasks" in data:
        items = []
        for task in data.get("tasks", []):
            for result in task.get("result", []) or []:
                items.extend(result.get("items", []) or [])
    elif isinstance(data, dict) and "items" in data:
        items = data["items"]
    elif isinstance(data, list):
        items = data
    else:
        items = []

    rows = []
    for it in items:
        kw_data = it.get("keyword_data", {}) or {}
        kw_info = kw_data.get("keyword_info", {}) or {}
        kw_intent = kw_data.get("search_intent_info", {}) or {}
        ranked = it.get("ranked_serp_element", {}) or {}
        serp = ranked.get("serp_item", {}) or {}

        rows.append({
            "keyword": kw_data.get("keyword"),
            "rank_group": serp.get("rank_group"),
            "rank_absolute": serp.get("rank_absolute"),
            "type": serp.get("type"),
            "search_volume": kw_info.get("search_volume"),
            "cpc": kw_info.get("cpc"),
            "competition_level": kw_info.get("competition_level"),
            "kw_difficulty": kw_data.get("keyword_properties", {}).get("keyword_difficulty"),
            "intent": kw_intent.get("main_intent"),
            "ranked_url": serp.get("url"),
            "ranked_title": (serp.get("title") or "")[:120],
            "etv": ranked.get("etv"),
            "estimated_paid_traffic_cost": ranked.get("estimated_paid_traffic_cost"),
            "last_updated": kw_info.get("last_updated_time"),
        })

    # Sort by search_volume desc, then rank_group asc
    rows.sort(key=lambda r: (-(r["search_volume"] or 0), r["rank_group"] or 999))

    case["csv"].write_text("", encoding="utf-8")
    with case["csv"].open("w", encoding="utf-8", newline="") as f:
        if rows:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(f"[OK] {case['label']}: {len(rows)} rows -> {case['csv'].name}")
