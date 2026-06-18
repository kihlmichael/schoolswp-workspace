#!/usr/bin/env python3
"""Upload DE-translated CSV to Ninja Tables table 2891625 via multipart REST.

Both /item/update and POST /item are silent on v2 (confirmed 2026-05-13):
  - /item/update returns 200 "Cell successfully updated" but data unchanged
  - POST /item   returns 200 "Données bien enregistrées" with id:null, table unchanged

Only reliable path per memory reference_ninja_tables_rest.md = import/upload-csv.

Strategy: delete the 4 FR rows first via DELETE bulk/single, then upload the
CSV which appends 4 fresh DE rows in correct order.
"""

import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
CSV = ROOT / "content" / "articles" / "_workspace" / "table-2891625-de.csv"
TABLE_ID = 2891625
BASE = f"https://schoolswp.com/wp-json/ninjatables/v2/tables/{TABLE_ID}"
IMPORT_URL = "https://schoolswp.com/wp-json/ninjatables/v2/import/upload-csv-in-existing-table"


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8"))["env"]
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def jget(url, auth):
    req = urllib.request.Request(url, headers={
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-nt/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


def jcall(method, url, auth, payload=None):
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


def multipart_post(url, auth, fields, file_field, file_path):
    boundary = "----schoolswp" + uuid.uuid4().hex
    body = []
    for k, v in fields.items():
        body.append(f"--{boundary}".encode())
        body.append(f'Content-Disposition: form-data; name="{k}"'.encode())
        body.append(b"")
        body.append(str(v).encode("utf-8"))

    fname = os.path.basename(file_path)
    ctype = mimetypes.guess_type(fname)[0] or "text/csv"
    body.append(f"--{boundary}".encode())
    body.append(
        f'Content-Disposition: form-data; name="{file_field}"; filename="{fname}"'.encode()
    )
    body.append(f"Content-Type: {ctype}".encode())
    body.append(b"")
    body.append(Path(file_path).read_bytes())

    body.append(f"--{boundary}--".encode())
    body.append(b"")

    payload = b"\r\n".join(body)

    req = urllib.request.Request(url, data=payload, method="POST", headers={
        "Authorization": auth,
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-nt/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main():
    user, pw = load_creds()
    auth = auth_header(user, pw)

    # 1) Fetch current rows (snapshot, no destructive action yet)
    st, d = jget(f"{BASE}/item", auth)
    rows = d.get("data", [])
    initial_ids = [r["id"] for r in rows]
    print(f"[before] {len(rows)} rows, ids={initial_ids}")
    for r in rows:
        print(f"   id={r['id']} pos={r['position']} values={r['values']}")

    # 2) NON-DESTRUCTIVE upload test: try variants, observe if any adds DE rows
    candidates = [
        {"file_field": "file", "fields": {"table_id": TABLE_ID}},
        {"file_field": "ninja_table_csv", "fields": {"table_id": TABLE_ID}},
        {"file_field": "csv", "fields": {"table_id": TABLE_ID}},
        {"file_field": "file", "fields": {}},
    ]

    accepted_variant = None
    for i, cand in enumerate(candidates, 1):
        print(f"\n[upload attempt {i}] file_field={cand['file_field']} fields={cand['fields']}")
        st, body = multipart_post(IMPORT_URL, auth, cand["fields"], cand["file_field"], str(CSV))
        print(f"   HTTP {st}  body[:300]={body[:300]}")
        if st == 200 and "error" not in body.lower() and '"data"' in body:
            # Verify actual side-effect: re-fetch and check for new rows
            st2, d2 = jget(f"{BASE}/item", auth)
            new_rows = d2.get("data", [])
            new_ids = [r["id"] for r in new_rows if r["id"] not in initial_ids]
            print(f"   re-fetch: {len(new_rows)} rows total, {len(new_ids)} new")
            if new_ids:
                accepted_variant = cand
                break
            else:
                print("   no side-effect (silent), trying next variant...")
        if st != 200:
            print(f"   variant rejected ({st})")

    if not accepted_variant:
        print("\n[result] no working CSV upload variant found", file=sys.stderr)
        sys.exit(1)

    # 3) Now safe to delete the 4 original FR rows
    print(f"\n[delete] removing {len(initial_ids)} original FR rows...")
    for rid in initial_ids:
        st, resp = jcall("GET", f"{BASE}/item/delete?id={rid}", auth)
        print(f"   row {rid} delete HTTP {st}: {json.dumps(resp, ensure_ascii=False)[:120]}")

    # 4) Final state
    st, d = jget(f"{BASE}/item", auth)
    print(f"\n[after] {len(d.get('data',[]))} rows:")
    for r in d.get("data", []):
        print(f"   id={r['id']} pos={r['position']} values={r['values']}")


if __name__ == "__main__":
    main()
