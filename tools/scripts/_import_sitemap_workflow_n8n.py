"""One-shot import script: pousse le workflow envoyer-sitemap-google-daily.json sur n8n.

- Charge N8N_API_KEY depuis .env
- Strip champs non autorises (active, tags, pinData, meta, id) avant POST
- User-Agent Mozilla (Cloudflare bloque UA Python sur schoolswp-n8n.wp1.host)
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = PROJECT_ROOT / "systems" / "n8n" / "workflows" / "envoyer-sitemap-google-daily.json"
ALLOWED_FIELDS = {"name", "nodes", "connections", "settings", "staticData"}
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def find_in_settings(obj, key: str):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                return v
            found = find_in_settings(v, key)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = find_in_settings(item, key)
            if found is not None:
                return found
    return None


def main() -> int:
    env = load_env(PROJECT_ROOT / ".env")
    settings = json.loads((PROJECT_ROOT / ".claude" / "settings.local.json").read_text(encoding="utf-8"))

    # settings.local.json contient la cle a jour, .env est secondaire
    api_key = find_in_settings(settings, "N8N_API_KEY") or env.get("N8N_API_KEY")
    if not api_key:
        print("ERROR: N8N_API_KEY missing in settings.local.json and .env", file=sys.stderr)
        return 2

    base_url = env.get("N8N_BASE_URL", "https://schoolswp-n8n.wp1.host").rstrip("/")
    workflow = json.loads(WORKFLOW_PATH.read_text(encoding="utf-8"))
    payload = {k: v for k, v in workflow.items() if k in ALLOWED_FIELDS}

    url = f"{base_url}/api/v1/workflows"
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-N8N-API-KEY": api_key,
            "User-Agent": UA,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            text = response.read().decode("utf-8")
            print(f"STATUS: {response.status}")
            print(text)
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code} {exc.reason}", file=sys.stderr)
        print(exc.read().decode("utf-8"), file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"URL ERROR: {exc.reason}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
