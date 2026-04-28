#!/usr/bin/env python3
"""
Detach Rank Math FAQPage schema template `schema-2099769` from post 52944.
The in-body microdata FAQ (itemprop itemscope) will take over.

Strategy:
 1) Try /wp-json/rankmath/v1/updateMeta with empty value for the schema meta key
 2) Fallback: core /wp/v2/posts/52944 PATCH with meta override
 3) Verify with a public render check
"""
import json, urllib.request, urllib.error, base64, sys, re, time, gzip, io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 52944
FAQ_SCHEMA_KEY = "rank_math_schema_2099769"   # derived from schema-2099769

def creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]

def auth(u, p):
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()

def hit(url, u, p, method="GET", payload=None):
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Authorization": auth(u, p),
        "Accept": "application/json",
    }
    if body:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")

def attempt_updateMeta(u, p, meta_payload):
    return hit("https://schoolswp.com/wp-json/rankmath/v1/updateMeta", u, p, "POST", {
        "objectID": POST_ID, "objectType": "post", "meta": meta_payload,
    })

def attempt_core_meta(u, p, meta_payload):
    return hit(f"https://schoolswp.com/wp-json/wp/v2/posts/{POST_ID}", u, p, "POST", {
        "meta": meta_payload,
    })

def verify_public():
    url = f"https://schoolswp.com/creer-plateforme-formation-wordpress/?nocache={int(time.time())}"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0","Cache-Control":"no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
    data = raw.decode("utf-8", errors="replace")
    faq_count = len(re.findall(r'"@type"\s*:\s*"FAQPage"', data))
    questions = re.findall(r'"@type"\s*:\s*"Question"[^{]*"name"\s*:\s*"([^"]+)"', data)
    return faq_count, questions

def main():
    u, p = creds()

    print(f"[step 1] Try /updateMeta with empty value for {FAQ_SCHEMA_KEY}")
    status, resp = attempt_updateMeta(u, p, {FAQ_SCHEMA_KEY: ""})
    print(f"        HTTP {status}")
    print(f"        {resp[:500]}")
    print()

    print("[verify 1] Re-fetch public render (cache-busted)")
    c, qs = verify_public()
    print(f"        FAQPage JSON-LD count: {c}")
    for q in qs[:5]:
        print(f"          Q: {q}")
    if c == 0:
        print("[DONE] FAQPage schema removed at step 1.")
        return

    print()
    print(f"[step 2] Try core /wp/v2/posts PATCH with {FAQ_SCHEMA_KEY}: null")
    status, resp = attempt_core_meta(u, p, {FAQ_SCHEMA_KEY: None})
    print(f"        HTTP {status}")
    print(f"        {resp[:500]}")
    print()

    print("[verify 2]")
    c, qs = verify_public()
    print(f"        FAQPage JSON-LD count: {c}")
    for q in qs[:5]:
        print(f"          Q: {q}")
    if c == 0:
        print("[DONE] FAQPage schema removed at step 2.")
        return

    print("[failed] Neither attempt removed the schema. Manual Rank Math cleanup required.")
    sys.exit(1)

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
