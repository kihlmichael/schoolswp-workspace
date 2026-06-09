#!/usr/bin/env python
"""Push de la refonte du post 2969375 (SureDash vs Fluent Community).

Lit le contenu Gutenberg local (post_content.html, octets exacts incluant
les \\u002d des gradients Kadence), pousse via WP REST API (auth depuis .env,
jamais affiche le secret). Modele : push_2289936_refonte.py.

Sortie : diagnostics non sensibles uniquement.
"""

import os
import pathlib
import sys
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[2]

# --- charge .env (sans l'afficher) ---
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
            return env[n], n
    return None, None


url, url_key = pick("WP_API_URL", "WP_URL", "WP_SITE_URL", "WORDPRESS_URL")
user, user_key = pick("WP_USER", "WP_USERNAME", "WP_LOGIN", "WORDPRESS_USER")
pwd, pwd_key = pick("WP_PASS", "WP_APP_PASSWORD", "WP_PASSWORD", "WP_APP_PW", "WORDPRESS_APP_PASSWORD")

print("=== creds presence ===")
print("url_key:", url_key, "| value:", url if url else None)
print("user_key:", user_key, "| user present:", bool(user))
print("pwd_key:", pwd_key, "| pwd present:", bool(pwd))

if not (user and pwd):
    print("\nNO_USABLE_CREDS - variables WP REST absentes de .env. Stop (fallback Novamira).")
    sys.exit(2)

_u = urlparse(url or "https://schoolswp.com")
base = f"{_u.scheme}://{_u.netloc}"
endpoint = f"{base}/wp-json/wp/v2/posts/2969375"

# --- contenu (octets exacts, pas de remplacement de backslash : preserver \\u002d) ---
src = ROOT / "content/articles/suredash-vs-fluent-community/post_content.html"
content = src.read_text(encoding="utf-8")
assert "\\n" not in content, "backslash-n inattendu dans le contenu"
assert "var(\\u002d\\u002d" in content, "gradient \\u002d manquant"
assert 'ninja_tables id="2974047"' in content
print("\ncontent bytes:", len(content.encode("utf-8")), "| backslashes:", content.count("\\"))

payload = {
    "content": content,
    "title": "SureDash vs Fluent Community : quel plugin communauté WordPress choisir ?",
    "slug": "suredash-vs-fluent-community",
    "excerpt": "SureDash ou Fluent Community pour ta communauté WordPress ? On compare l'écosystème, le LMS, l'app mobile, les tarifs et le profil idéal de chacun.",
    "status": "draft",
    "categories": [1655, 1661, 1668],
}

try:
    import requests  # noqa: E402
    from requests.auth import HTTPBasicAuth  # noqa: E402
except ImportError:
    print("requests absent")
    sys.exit(3)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Content-Type": "application/json",
}
print("\nPOST", endpoint)
r = requests.post(endpoint, json=payload, auth=HTTPBasicAuth(user, pwd), headers=headers, timeout=200)
print("status:", r.status_code)
ct = r.headers.get("content-type", "")
if "application/json" in ct:
    j = r.json()
    if isinstance(j, dict) and j.get("id"):
        rc = j.get("content", {})
        rendered = rc.get("raw") or rc.get("rendered") or ""
        print("OK id:", j.get("id"), "| slug:", j.get("slug"), "| status:", j.get("status"))
        print("title:", (j.get("title") or {}).get("rendered"))
        print("categories:", j.get("categories"))
        print("content_len_returned:", len(rendered))
        print("has_ninja_2974047:", "2974047" in rendered)
        print("has_cta_fluent:", "schoolswp.com/fluentcommunity/" in rendered)
        print("has_cta_suredash:", "suredash.com" in rendered)
        print("has_gradient_escaped:", "u002d" in rendered)
    else:
        print("ERROR json:", str(j)[:600])
else:
    print("NON-JSON response (anti-bot / cloudflare?). First 300 chars:")
    print(r.text[:300])
