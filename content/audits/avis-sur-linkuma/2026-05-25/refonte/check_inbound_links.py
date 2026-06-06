"""Inspecte les articles candidats pour le maillage entrant vers /avis-sur-linkuma/.

Cherche :
- Liens existants vers /avis-sur-linkuma/
- Sections où un lien serait naturel (mentions Linkuma, sections "Alternatives", H2 netlinking, etc.)
"""
import os, sys, json, base64, urllib.request

sys.stdout.reconfigure(encoding='utf-8')

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

SITE = "https://schoolswp.com"
TARGETS = [
    "linksgarden-avis",
    "link-whisper-avis",
    "thot-seo-avis",
    "seo-wordpress",
]


def get_creds():
    user = os.environ.get('WP_USERNAME') or os.environ.get('WP_USER') or os.environ.get('WP_API_USERNAME')
    pwd = os.environ.get('WP_APP_PASSWORD') or os.environ.get('WP_PASSWORD') or os.environ.get('WP_API_PASSWORD')
    return user, pwd


def main():
    user, pwd = get_creds()
    if not user or not pwd:
        print("[ERROR] WP credentials not in env")
        sys.exit(1)
    token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
    headers = {"Authorization": f"Basic {token}", "User-Agent": "Mozilla/5.0", "Accept": "application/json"}

    for slug in TARGETS:
        url = f"{SITE}/index.php?rest_route=/wp/v2/posts&slug={slug}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                arr = json.loads(r.read())
            if not arr:
                print(f"\n=== /{slug}/ NOT FOUND (search wider) ===")
                continue
            post = arr[0]
            pid = post['id']
            title = post['title']['rendered']
            content = post['content']['raw'] if 'raw' in post['content'] else post['content']['rendered']
            print(f"\n=== /{slug}/  (id={pid}) ===")
            print(f"  title: {title[:80]}")
            print(f"  content chars: {len(content)}")
            print(f"  /avis-sur-linkuma/ count: {content.count('/avis-sur-linkuma/')}")
            print(f"  Linkuma mentions: {content.lower().count('linkuma')}")
            # Try to locate sections
            import re
            for m in re.finditer(r'<h([23])[^>]*>([^<]{0,80})', content):
                print(f"    H{m.group(1)}: {m.group(2).strip()}")
        except Exception as e:
            print(f"  ERROR {slug}: {e}")


if __name__ == "__main__":
    main()
