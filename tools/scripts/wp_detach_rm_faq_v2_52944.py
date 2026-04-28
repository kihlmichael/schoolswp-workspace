#!/usr/bin/env python3
"""
Second attempt to remove FAQPage schema from post 52944's JSON-LD output.
Try Rank Math official rich-snippet toggle keys.
"""
import json, urllib.request, urllib.error, base64, sys, re, time, gzip, io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 52944

def creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]

def auth(u, p):
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()

def rm_update(u, p, meta):
    req = urllib.request.Request(
        "https://schoolswp.com/wp-json/rankmath/v1/updateMeta",
        data=json.dumps({"objectID": POST_ID, "objectType": "post", "meta": meta}).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": auth(u, p),
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")

def public_faq_check():
    url = f"https://schoolswp.com/creer-plateforme-formation-wordpress/?nocache={int(time.time())}"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0","Cache-Control":"no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
    data = raw.decode("utf-8", errors="replace")
    faqs = len(re.findall(r'"@type"\s*:\s*"FAQPage"', data))
    qs = re.findall(r'"@type"\s*:\s*"Question"[^{]*"name"\s*:\s*"([^"]+)"', data)
    return faqs, qs

ATTEMPTS = [
    {"rank_math_rich_snippet": "off"},
    {"rank_math_rich_snippet": "article"},
    {"rank_math_snippet_name": ""},
    {"rank_math_faq_questions": ""},
    {"rank_math_schemas": ""},
    {"rank_math_rich_snippet": "off", "rank_math_snippet_faq_block": ""},
]

def main():
    u, p = creds()
    for i, meta in enumerate(ATTEMPTS, 1):
        print(f"\n[attempt {i}] meta = {meta}")
        status, resp = rm_update(u, p, meta)
        print(f"   HTTP {status}")
        c, qs = public_faq_check()
        print(f"   FAQPage count after: {c}")
        for q in qs[:3]:
            print(f"     Q: {q}")
        if c == 0:
            print(f"\n[SUCCESS] FAQPage removed after attempt {i}")
            return
    print("\n[FAIL] None of the attempts removed the FAQPage schema.")
    print("Manual cleanup required in WP Admin:")
    print("  1. Open post 52944 in Gutenberg")
    print("  2. Sidebar → Rank Math → Schema")
    print("  3. Delete the FAQ schema template entry")
    sys.exit(1)

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
