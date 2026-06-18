#!/usr/bin/env python3
"""Translate Ninja Tables table 2891625 rows FR -> DE via REST /item/update.

Per reference_ninja_tables_rest.md, /item/update was reportedly "silent" on v1.
We're on v2 here, test then fallback to delete+create if update doesn't stick.
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
TABLE_ID = 2891625
BASE = f"https://schoolswp.com/wp-json/ninjatables/v2/tables/{TABLE_ID}"

# Translation map indexed by row id (positions 1-4 in current state)
TRANSLATIONS = {
    1522: {"critere": "Geschwindigkeit", "classique": "Schwankend", "data_tables": "Sofort"},
    1523: {"critere": "Speicher",        "classique": "Browser",    "data_tables": "Server"},
    1524: {"critere": "Datenmenge",      "classique": "< 500",      "data_tables": "> 1000"},
    1525: {"critere": "SEO",             "classique": "Schwer",     "data_tables": "Leicht"},
}


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8"))["env"]
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http(method, url, auth, payload=None):
    headers = {
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-nt/1.0",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"_raw": body[:500]}


def fetch_rows(auth):
    st, d = http("GET", f"{BASE}/item", auth)
    if st != 200:
        print(f"[error] GET items HTTP {st}: {d}", file=sys.stderr)
        sys.exit(1)
    return d.get("data", [])


def main():
    user, pw = load_creds()
    auth = auth_header(user, pw)

    print("=== BEFORE ===")
    before = fetch_rows(auth)
    for row in before:
        print(f"  id={row['id']} pos={row['position']} values={row['values']}")
    print()

    # Try POST /item/update with several payload shapes
    # Shape A: {id, values}
    # Shape B: {id, value_critere, value_classique, ...} (legacy)
    # Shape C: {id, ...flat values}
    update_url = f"{BASE}/item/update"

    for row_id, new_values in TRANSLATIONS.items():
        # Find current row
        current = next((r for r in before if r["id"] == row_id), None)
        if not current:
            print(f"[skip] row {row_id} not in current table")
            continue

        payload = {
            "id": row_id,
            "values": new_values,
            "position": current["position"],
            "settings": current.get("settings", {}),
        }
        st, resp = http("POST", update_url, auth, payload=payload)
        print(f"[update] row {row_id} HTTP {st}: {json.dumps(resp, ensure_ascii=False)[:200]}")

    print()
    print("=== AFTER (re-fetch) ===")
    after = fetch_rows(auth)
    all_ok = True
    for row in after:
        expected = TRANSLATIONS.get(row["id"])
        if expected:
            status = "✓" if row["values"] == expected else "✗"
            if row["values"] != expected:
                all_ok = False
        else:
            status = "?"
        print(f"  id={row['id']} pos={row['position']} {status} values={row['values']}")

    if all_ok:
        print("\n[result] ALL ROWS TRANSLATED ✓")
        sys.exit(0)
    else:
        print("\n[result] update path silent or incomplete — fallback needed")
        sys.exit(1)


if __name__ == "__main__":
    main()
