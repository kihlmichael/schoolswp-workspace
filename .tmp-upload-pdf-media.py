"""One-shot: upload a single PDF to WP media library via REST. Disposable.

Reads WP_API_* from project .env (script reads secrets, not the operator).
Prints only non-secret diagnostics + the resulting source_url on success.
"""

import sys
from pathlib import Path

import requests
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

ROOT = Path(__file__).resolve().parent
env = {**dotenv_values(ROOT / ".env")}

raw_url = (env.get("WP_API_URL") or "").rstrip("/")
user = env.get("WP_API_USERNAME") or ""
pwd = env.get("WP_API_PASSWORD") or ""

missing = [k for k, v in [("WP_API_URL", raw_url), ("WP_API_USERNAME", user), ("WP_API_PASSWORD", pwd)] if not v]
if missing:
    print("MISSING_ENV:", ", ".join(missing))
    sys.exit(2)

if raw_url.endswith("/wp-json"):
    base = raw_url
elif "/wp-json" in raw_url:
    base = raw_url.split("/wp-json")[0] + "/wp-json"
else:
    base = raw_url + "/wp-json"

pdf = ROOT / "content" / "lead-magnets" / "welcome-template-fluentcrm" / "Template-Welcome-FluentCRM-schoolsWP.pdf"
if not pdf.exists():
    print("PDF_NOT_FOUND:", pdf)
    sys.exit(2)

endpoint = f"{base}/wp/v2/media"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/json, */*",
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
    "Content-Disposition": 'attachment; filename="template-welcome-fluentcrm-schoolswp.pdf"',
    "Content-Type": "application/pdf",
}

print("ENDPOINT:", endpoint)
print("PDF_SIZE_BYTES:", pdf.stat().st_size)

try:
    with pdf.open("rb") as fh:
        resp = requests.post(
            endpoint,
            headers=headers,
            data=fh,
            auth=HTTPBasicAuth(user, pwd),
            timeout=120,
        )
except requests.RequestException as exc:
    print("REQUEST_ERROR:", type(exc).__name__, str(exc)[:200])
    sys.exit(1)

ctype = resp.headers.get("content-type", "")
print("HTTP_STATUS:", resp.status_code)
print("CONTENT_TYPE:", ctype)

if "application/json" in ctype:
    try:
        j = resp.json()
    except ValueError:
        print("JSON_PARSE_FAILED, first 300 chars:")
        print(resp.text[:300])
        sys.exit(1)
    if resp.status_code in (200, 201):
        print("OK_MEDIA_ID:", j.get("id"))
        print("OK_SOURCE_URL:", j.get("source_url"))
        print("OK_LINK:", j.get("link"))
    else:
        print("API_ERROR_CODE:", j.get("code"))
        print("API_ERROR_MESSAGE:", str(j.get("message"))[:200])
else:
    # Likely an anti-bot challenge / WAF HTML page
    snippet = resp.text[:300].replace("\n", " ")
    print("NON_JSON_BODY (first 300 chars):")
    print(snippet)
