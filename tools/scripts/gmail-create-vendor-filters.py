"""Cree des filtres Gmail natifs qui auto-labelisent les emails fabricants WP.

Execute une seule fois : cree N filtres (un par chunk de ~25 domaines) qui appliquent
automatiquement le label '📰 Newsletters' aux emails entrants des VENDORS listes
dans gmail-label-wp-vendors.py.

Usage :
  python tools/scripts/gmail-create-vendor-filters.py                  # dry-run
  python tools/scripts/gmail-create-vendor-filters.py --apply          # cree les filtres
  python tools/scripts/gmail-create-vendor-filters.py --list           # liste les filtres existants
  python tools/scripts/gmail-create-vendor-filters.py --delete-schoolswp  # supprime les filtres crees par ce script
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("pip install google-api-python-client google-auth-oauthlib")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
CREDENTIALS_FILE = SCRIPT_DIR / "credentials-gdrive-audit.json"
TOKEN_FILE = SCRIPT_DIR / "token-gmail-filters.json"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.settings.basic",
]

LABEL_ID = "Label_5722837123959833844"  # 📰 Newsletters
CHUNK_SIZE = 25  # domaines par filtre (Gmail query limit ~1500 chars)
FILTER_TAG = "schoolsWP-veille-auto"  # tag pour retrouver nos filtres (stocke dans les labels added ? non, dans description via Vacation ? Gmail filter n'a pas de champ description... on repere via le contenu de la query)


def get_service():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")
    return build("gmail", "v1", credentials=creds)


def load_vendors():
    main = SCRIPT_DIR / "gmail-label-wp-vendors.py"
    spec = importlib.util.spec_from_file_location("main", main)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.VENDORS


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def build_query(domains):
    return " OR ".join(f"from:{d}" for d in domains)


def list_filters(svc):
    resp = svc.users().settings().filters().list(userId="me").execute()
    return resp.get("filter", [])


def delete_schoolswp_filters(svc):
    filters = list_filters(svc)
    deleted = 0
    for f in filters:
        query = (f.get("criteria") or {}).get("query", "")
        action = f.get("action") or {}
        # Reconnait nos filtres : labelId cible = LABEL_ID + query contient au moins 5 "from:"
        if LABEL_ID in action.get("addLabelIds", []) and query.count("from:") >= 5:
            svc.users().settings().filters().delete(userId="me", id=f["id"]).execute()
            print(f"  [DEL] filter {f['id']}: {query[:80]}...")
            deleted += 1
    print(f"[OK] {deleted} filtres supprimes")


def create_filters(svc, vendors, apply=False):
    chunk_list = list(chunks(vendors, CHUNK_SIZE))
    print(f"Vendors: {len(vendors)}  |  Chunks: {len(chunk_list)} (max {CHUNK_SIZE}/chunk)")

    existing_queries = set()
    if apply:
        for f in list_filters(svc):
            q = (f.get("criteria") or {}).get("query", "")
            if q:
                existing_queries.add(q)

    created = 0
    for i, group in enumerate(chunk_list, 1):
        query = build_query(group)
        print(f"\n[Chunk {i}/{len(chunk_list)}] {len(group)} domaines | query {len(query)} chars")
        print(f"  domaines : {group[0]} ... {group[-1]}")

        if not apply:
            continue

        if query in existing_queries:
            print(f"  [SKIP] filtre deja existant")
            continue

        body = {
            "criteria": {"query": query},
            "action": {"addLabelIds": [LABEL_ID]},
        }
        svc.users().settings().filters().create(userId="me", body=body).execute()
        print(f"  [CREE]")
        created += 1

    if apply:
        print(f"\n[OK] {created} nouveaux filtres crees")
    else:
        print(f"\n[DRY-RUN] Ajoute --apply pour creer ces {len(chunk_list)} filtres")


def main():
    svc = get_service()
    if "--list" in sys.argv:
        for f in list_filters(svc):
            q = (f.get("criteria") or {}).get("query", "")[:100]
            labels = (f.get("action") or {}).get("addLabelIds", [])
            print(f"{f['id']} | labels={labels} | q={q!r}")
        return
    if "--delete-schoolswp" in sys.argv:
        delete_schoolswp_filters(svc)
        return
    vendors = load_vendors()
    create_filters(svc, vendors, apply="--apply" in sys.argv)


if __name__ == "__main__":
    main()
