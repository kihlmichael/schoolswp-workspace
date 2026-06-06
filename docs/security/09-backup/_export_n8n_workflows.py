"""Export all n8n workflows to local JSON snapshot.

Reads N8N_API_KEY + N8N_API_URL from .claude/settings.local.json (top-level env).
Outputs each workflow as a separate JSON file to ./n8n-snapshot-YYYY-MM-DD/.
Never echoes the API key.
"""
import json
import os
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("ERROR: pip install requests")
    sys.exit(2)

HERE = Path(__file__).parent
SETTINGS_PATH = Path(r"d:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\settings.local.json")

with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
    settings = json.load(f)

env = settings.get("env", {})
api_url = env.get("N8N_API_URL", "").rstrip("/")
api_key = env.get("N8N_API_KEY", "")

if not api_url or not api_key:
    print(f"ERROR: N8N_API_URL / N8N_API_KEY missing in {SETTINGS_PATH}")
    sys.exit(3)

print(f"Target: {api_url}")
print(f"Key last4: ...{api_key[-4:]}")

session = requests.Session()
session.headers.update({
    "X-N8N-API-KEY": api_key,
    "Accept": "application/json",
})

today = date.today().isoformat()
out_dir = HERE / f"n8n-snapshot-{today}"
out_dir.mkdir(parents=True, exist_ok=True)

print(f"Output: {out_dir}")

print("\n[1/3] Fetching workflow list...")
r = session.get(f"{api_url}/api/v1/workflows?limit=250", timeout=60)
r.raise_for_status()
data = r.json()
workflows = data.get("data", [])
print(f"  Found: {len(workflows)} workflows")

print("\n[2/3] Fetching full content for each workflow...")
ok_count = 0
err_count = 0
for i, w in enumerate(workflows, 1):
    wid = w.get("id")
    raw_name = w.get("name") or ""
    wname = "".join(c if (c.isalnum() or c in "-_") else "-" for c in raw_name)[:80].strip("-")
    try:
        rf = session.get(f"{api_url}/api/v1/workflows/{wid}", timeout=60)
        rf.raise_for_status()
        full = rf.json()
        out_path = out_dir / f"{wid}__{wname}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(full, f, indent=2, ensure_ascii=False)
        print(f"  [{i}/{len(workflows)}] OK {wid} {wname[:40]}")
        ok_count += 1
    except Exception as e:
        print(f"  [{i}/{len(workflows)}] ERR {wid}: {str(e)[:80]}")
        err_count += 1

print("\n[3/3] Fetching credentials list (metadata only, no secret values)...")
try:
    rc = session.get(f"{api_url}/api/v1/credentials/schema", timeout=30)
except Exception:
    pass

try:
    rc = session.get(f"{api_url}/api/v1/credentials", timeout=30)
    if rc.ok:
        creds_meta = rc.json()
        out_path = out_dir / "_credentials-metadata.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(creds_meta, f, indent=2, ensure_ascii=False)
        print(f"  Credentials metadata saved ({rc.headers.get('Content-Length', 'n/a')} bytes)")
    else:
        print(f"  Credentials list returned {rc.status_code} (expected on n8n cloud or basic plan)")
except Exception as e:
    print(f"  Credentials skip: {str(e)[:80]}")

# Manifest
manifest = {
    "snapshot_date": today,
    "n8n_api_url": api_url,
    "workflows_total": len(workflows),
    "workflows_ok": ok_count,
    "workflows_err": err_count,
    "note": "Workflows JSON only. Credentials encrypted by n8n cannot be exported via REST API (by design). Restore via n8n UI > import + recreate credentials.",
}
with open(out_dir / "_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

total_size = sum(f.stat().st_size for f in out_dir.iterdir())
print(f"\nDONE. {ok_count} OK, {err_count} ERR, total {total_size // 1024} KB in {out_dir}")
