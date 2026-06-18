#!/usr/bin/env python
"""Upload des 2 logos (SureDash, FluentCommunity) en media WP via REST.

Lit les creds depuis .env (jamais affichees). Cree l'attachment (raw body),
puis pose title/alt_text/caption. Sortie : id + source_url par logo.
Modele : push_2969375_refonte.py.
"""

import os
import pathlib
import sys
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[2]

env = {}
for p in [ROOT / ".env", ROOT / "agents" / ".env"]:
    if p.exists():
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
env.update({k: v for k, v in os.environ.items()})


def pick(*names):
    for n in names:
        if env.get(n):
            return env[n]
    return None


url = pick("WP_API_URL", "WP_URL", "WP_SITE_URL", "WORDPRESS_URL")
user = pick("WP_USER", "WP_USERNAME", "WP_LOGIN", "WORDPRESS_USER")
pwd = pick("WP_PASS", "WP_APP_PASSWORD", "WP_PASSWORD", "WP_APP_PW", "WORDPRESS_APP_PASSWORD")
if not (user and pwd):
    print("NO_USABLE_CREDS")
    sys.exit(2)

_u = urlparse(url or "https://schoolswp.com")
base = f"{_u.scheme}://{_u.netloc}"
media_ep = f"{base}/wp-json/wp/v2/media"

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    print("requests absent")
    sys.exit(3)

auth = HTTPBasicAuth(user, pwd)
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

LOGOS = [
    {
        "path": ROOT / "assets/featured-images/_logos-2969375/slide-01-suredash.png",
        "filename": "suredash-logo.png",
        "title": "Logo SureDash",
        "alt": "Logo SureDash",
    },
    {
        "path": ROOT / "assets/featured-images/_logos-2969375/slide-02-fluent-word.png",
        "filename": "fluentcommunity-logo.png",
        "title": "Logo FluentCommunity",
        "alt": "Logo FluentCommunity",
    },
]

for lo in LOGOS:
    data = lo["path"].read_bytes()
    headers = {
        "User-Agent": ua,
        "Content-Type": "image/png",
        "Content-Disposition": f'attachment; filename="{lo["filename"]}"',
    }
    r = requests.post(media_ep, data=data, auth=auth, headers=headers, timeout=120)
    if r.status_code not in (200, 201):
        print(f"{lo['filename']} UPLOAD_FAIL {r.status_code} {r.text[:200]}")
        continue
    j = r.json()
    mid = j.get("id")
    # pose title / alt / caption
    r2 = requests.post(
        f"{media_ep}/{mid}",
        json={"title": lo["title"], "alt_text": lo["alt"], "caption": lo["title"]},
        auth=auth,
        headers={"User-Agent": ua, "Content-Type": "application/json"},
        timeout=60,
    )
    j2 = r2.json() if "application/json" in r2.headers.get("content-type", "") else {}
    src = (j2.get("source_url") if isinstance(j2, dict) else None) or j.get("source_url")
    print(f"{lo['filename']} OK id={mid} src={src}")
