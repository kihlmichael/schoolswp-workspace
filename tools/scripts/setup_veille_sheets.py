"""Setup the Google Sheet "schoolsWP - Veille Concurrence" structure.

- Renames existing tab `veille-concurrence` → `plugins-utilises`
- Creates 5 new tabs with headers and (when applicable) seed rows:
    `_input-plugins`           (23 outils du Vault outils-recommandes.md)
    `_input-concurrents`       (8 sites éditoriaux FR)
    `_input-locale`            (vide, peuplé par W208a)
    `concurrents-editoriaux`   (output W207, vide)
    `concurrence-locale-grand-est` (output W208 phase 2 future, vide)

Idempotent: skips creation if a tab already exists, only updates headers if missing.

Auth: uses the `gws` CLI (Google Workspace CLI) — must be logged in via `gws auth login`.

Usage:
    py tools/scripts/setup_veille_sheets.py
    py tools/scripts/setup_veille_sheets.py --dry-run   # preview without writing
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

SHEET_ID = "1kOJZBpcKP3rz_TTrjxZcdHP4YhEa-QZLaba3HCCJTR0"
GWS = shutil.which("gws") or r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"

TABS = {
    "plugins-utilises": {
        "headers": [
            "date",
            "concurrent",
            "url",
            "annee_fondation",
            "funding_status",
            "money_raised",
            "features_top3",
            "pricing_range",
            "positive_pct",
            "top_pros",
            "top_cons",
            "last_news",
        ],
        "rename_from": "veille-concurrence",
        "seed_rows": [],
    },
    "_input-plugins": {
        "headers": ["name", "url", "category", "priority"],
        "seed_rows": [
            ["EasyHoster", "https://www.easyhoster.com", "Hébergement", 1],
            ["JP Blocks", "https://jpblocks.com", "Page builder", 2],
            ["FluentCart", "https://fluentcart.com", "Suite Fluent", 1],
            ["FluentBoards", "https://fluentboards.com", "Suite Fluent", 2],
            ["FluentForms", "https://fluentforms.com", "Suite Fluent", 1],
            ["FluentCRM", "https://fluentcrm.com", "Suite Fluent", 1],
            ["FluentSupport", "https://fluentsupport.com", "Suite Fluent", 2],
            ["FluentBooking", "https://fluentbooking.com", "Suite Fluent", 2],
            ["FluentAffiliate", "https://fluentaffiliate.com", "Suite Fluent", 2],
            ["FlyingPress", "https://flyingpress.com", "Performance", 1],
            ["Perfmatters", "https://perfmatters.io", "Performance", 2],
            ["Rank Math", "https://rankmath.com", "SEO", 1],
            ["SureRank", "https://surerank.com", "SEO", 2],
            ["Otomatic AI", "https://otomatic.ai", "SEO", 3],
            ["Groundhogg", "https://www.groundhogg.io", "CRM", 2],
            ["Ninja Tables", "https://ninjatables.com", "Productivité", 2],
            ["OttoKit", "https://ottokit.com", "Automatisation", 1],
            ["LinkCentral", "https://linkcentral.app", "Affiliation", 3],
            ["TutorLMS", "https://tutorlms.com", "LMS", 1],
            ["Amelia WP", "https://wpamelia.com", "Réservations", 3],
            ["Bertha.AI", "https://bertha.ai", "IA", 3],
            ["BuddyBoss", "https://www.buddyboss.com", "Communauté", 3],
            ["Divi Lover", "https://divi-lover.com", "Design", 3],
        ],
    },
    "_input-concurrents": {
        "headers": ["name", "url", "category"],
        "seed_rows": [
            ["WPMarmite", "https://wpmarmite.com", "Blog WP francophone"],
            ["WP Formation", "https://wpformation.com", "Blog WP / formation"],
            ["Web and SEO", "https://webandseo.fr", "Blog WP / SEO"],
            ["Tutoriels LWS", "https://tutoriels.lws.fr", "Blog hébergeur LWS"],
            ["WP Origami", "https://wporigami.com", "Blog WP / dev"],
            ["Capitaine WP", "https://capitainewp.io", "Blog WP / dev"],
            ["Live Mentor", "https://livementor.com", "École en ligne"],
            ["WP Chef", "https://wpchef.fr", "Formation WP"],
        ],
    },
    "_input-locale": {
        "headers": [
            "date_identified",
            "query",
            "domain",
            "url",
            "title",
            "description",
            "validated",
        ],
        "seed_rows": [],
    },
    "concurrents-editoriaux": {
        "headers": [
            "date",
            "site_name",
            "url",
            "founded_year",
            "pillars",
            "audience_geography",
            "publication_freq",
            "top_keywords",
            "latest_articles",
            "monetization",
            "newsletter",
            "social_followers",
            "has_lead_magnet",
        ],
        "seed_rows": [],
    },
    "concurrence-locale-grand-est": {
        "headers": [
            "date",
            "name",
            "url",
            "services_proposes",
            "pricing_range",
            "zone_intervention",
            "references_clients",
            "channels_acquisition",
        ],
        "seed_rows": [],
    },
}


def gws(*args: str, json_payload: dict | None = None, params: dict | None = None) -> dict:
    cmd = [GWS, *args]
    if params is not None:
        cmd += ["--params", json.dumps(params)]
    if json_payload is not None:
        cmd += ["--json", json.dumps(json_payload)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.exit(f"ERROR running {' '.join(cmd[:6])}...\n{r.stderr}\n{r.stdout[:500]}")
    out = r.stdout.strip()
    if not out:
        return {}
    # gws prefixes status messages on stderr; stdout is the JSON
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        # Skip leading lines until JSON starts
        lines = out.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("{") or line.startswith("["):
                return json.loads("\n".join(lines[i:]))
        sys.exit(f"Could not parse gws output:\n{out[:500]}")


def get_sheet_structure() -> dict[str, int]:
    """Return mapping of tab title -> sheetId."""
    data = gws(
        "sheets",
        "spreadsheets",
        "get",
        params={"spreadsheetId": SHEET_ID, "fields": "sheets(properties(sheetId,title))"},
    )
    return {s["properties"]["title"]: s["properties"]["sheetId"] for s in data.get("sheets", [])}


def batch_update(requests: list[dict]) -> dict:
    return gws(
        "sheets",
        "spreadsheets",
        "batchUpdate",
        params={"spreadsheetId": SHEET_ID},
        json_payload={"requests": requests},
    )


def values_update(range_a1: str, values: list[list]) -> dict:
    return gws(
        "sheets",
        "spreadsheets",
        "values",
        "update",
        params={
            "spreadsheetId": SHEET_ID,
            "range": range_a1,
            "valueInputOption": "USER_ENTERED",
        },
        json_payload={"values": values},
    )


def values_get(range_a1: str) -> list[list]:
    data = gws(
        "sheets",
        "spreadsheets",
        "values",
        "get",
        params={"spreadsheetId": SHEET_ID, "range": range_a1},
    )
    return data.get("values", [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    print("Checking gws auth...")
    structure = get_sheet_structure()
    print(f"  Existing tabs: {list(structure.keys())}")

    actions = []

    # 1. Rename veille-concurrence -> plugins-utilises (if needed)
    rename_from = TABS["plugins-utilises"].get("rename_from")
    if rename_from and rename_from in structure and "plugins-utilises" not in structure:
        actions.append(
            {
                "type": "rename",
                "from": rename_from,
                "to": "plugins-utilises",
                "sheetId": structure[rename_from],
            }
        )

    # 2. Create missing tabs
    for tab_name in TABS.keys():
        if tab_name not in structure and tab_name != "plugins-utilises":
            actions.append({"type": "create", "title": tab_name})
        elif tab_name == "plugins-utilises" and rename_from not in structure and "plugins-utilises" not in structure:
            actions.append({"type": "create", "title": tab_name})

    print(f"\nPlanned actions: {len(actions)}")
    for a in actions:
        print(f"  - {a}")

    if args.dry_run:
        print("\n--dry-run, exiting without writing")
        return 0

    # Apply renames + creates in one batchUpdate
    requests = []
    for a in actions:
        if a["type"] == "rename":
            requests.append(
                {
                    "updateSheetProperties": {
                        "properties": {"sheetId": a["sheetId"], "title": a["to"]},
                        "fields": "title",
                    }
                }
            )
        elif a["type"] == "create":
            requests.append({"addSheet": {"properties": {"title": a["title"]}}})

    if requests:
        print(f"\nApplying {len(requests)} structure changes...")
        batch_update(requests)
        print("  done")

    # Refresh structure after creates/renames
    structure = get_sheet_structure()

    # 3. Set headers + seed rows for each tab
    for tab_name, conf in TABS.items():
        if tab_name not in structure:
            print(f"  WARN: tab {tab_name} not found after creation, skipping")
            continue
        existing = values_get(f"'{tab_name}'!1:1")
        if existing and existing[0] == conf["headers"]:
            print(f"  {tab_name}: headers already correct, skipping headers")
        else:
            print(f"  {tab_name}: writing headers ({len(conf['headers'])} cols)")
            values_update(f"'{tab_name}'!A1", [conf["headers"]])

        if conf["seed_rows"]:
            existing_rows = values_get(f"'{tab_name}'!A2:A")
            if existing_rows:
                print(f"  {tab_name}: {len(existing_rows)} rows already present, skipping seed")
            else:
                print(f"  {tab_name}: seeding {len(conf['seed_rows'])} rows")
                values_update(f"'{tab_name}'!A2", conf["seed_rows"])

    print("\nDone. Final structure:")
    final = get_sheet_structure()
    for name in final:
        print(f"  - {name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
