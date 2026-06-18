"""Push title + meta + content vers post 54381 sur schoolswp.com.

Utilise les credentials WP du .env via python-dotenv.
N'imprime JAMAIS les credentials dans les logs.
"""
import os, sys, json, base64, urllib.request, urllib.parse, urllib.error
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

POST_ID = 54381
SITE = "https://schoolswp.com"

NEW_TITLE = "Linkuma avis 2026 : 7,5/10 après plusieurs mois de test"
NEW_META = (
    "Test Linkuma 2026 sur schoolsWP : qualité des spots, tarifs dès 7€ HT, "
    "alternatives, code promo. Verdict honnête pour freelance WordPress. 🔗"
)


def get_creds():
    user = os.environ.get('WP_USERNAME') or os.environ.get('WP_USER')
    pwd = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_PASSWORD')
    if not user or not pwd:
        # try novamira-style env
        user = user or os.environ.get('WP_API_USERNAME')
        pwd = pwd or os.environ.get('WP_API_PASSWORD')
    if not user or not pwd:
        print("[ERROR] WP credentials not found in env. "
              "Expected WP_USERNAME + WP_APP_PASSWORD")
        sys.exit(1)
    return user, pwd


def auth_header(user: str, pwd: str) -> dict:
    token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
    return {"Authorization": f"Basic {token}", "User-Agent": "Mozilla/5.0", "Accept": "application/json"}


def call(url: str, method: str, headers: dict, body: bytes | None = None, timeout: int = 180) -> tuple[int, str]:
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')
    except Exception as e:
        return -1, str(e)


def main():
    user, pwd = get_creds()
    headers = auth_header(user, pwd)
    headers_json = {**headers, "Content-Type": "application/json"}

    # Load content
    content_path = Path(__file__).parent / "post-54381-v2-content.html"
    with open(content_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[INFO] Loaded content: {len(content)} chars")

    # === Step 1: Push title + content via WP REST ===
    url = f"{SITE}/index.php?rest_route=/wp/v2/posts/{POST_ID}"
    payload = json.dumps({
        "title": NEW_TITLE,
        "content": content,
    }, ensure_ascii=False).encode("utf-8")
    print(f"[STEP 1] POST {url} (content+title, {len(payload)} bytes)")
    status, resp = call(url, "POST", headers_json, payload, timeout=240)
    print(f"[STEP 1] HTTP {status}")
    if status != 200:
        print(f"[STEP 1] Response: {resp[:1000]}")
        sys.exit(2)
    try:
        data = json.loads(resp)
        print(f"[STEP 1] OK — id={data.get('id')} modified={data.get('modified')}")
        print(f"[STEP 1] Title now: {data.get('title', {}).get('rendered', '')[:120]}")
    except Exception:
        print(f"[STEP 1] OK (could not parse JSON), len={len(resp)}")

    # === Step 2: Update Rank Math meta description ===
    url_rm = f"{SITE}/index.php?rest_route=/rankmath/v1/updateMeta"
    payload_rm = json.dumps({
        "objectID": POST_ID,
        "objectType": "post",
        "meta": {
            "rank_math_description": NEW_META,
            "rank_math_title": NEW_TITLE,
        }
    }, ensure_ascii=False).encode("utf-8")
    print(f"[STEP 2] POST {url_rm} (Rank Math meta)")
    status_rm, resp_rm = call(url_rm, "POST", headers_json, payload_rm, timeout=60)
    print(f"[STEP 2] HTTP {status_rm}")
    print(f"[STEP 2] Response: {resp_rm[:500]}")

    print("\n[DONE] Push completed.")
    print(f"  View live: {SITE}/avis-sur-linkuma/")
    print(f"  Edit: {SITE}/wp-admin/post.php?post={POST_ID}&action=edit")


if __name__ == "__main__":
    main()
