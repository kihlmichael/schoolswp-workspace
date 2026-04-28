"""Bootstrap du Google Sheet veille editoriale (crée les 7 onglets + headers).

Equivalent Python du veille-sheets-bootstrap.gs pour eviter de passer par Apps Script.

Usage : python tools/scripts/sheets-bootstrap-veille.py [--check]
  --check : lit l'etat actuel du sheet (onglets presents) sans rien modifier
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
TOKEN_FILE = SCRIPT_DIR / "token-sheets-veille.json"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SHEET_ID = "17qVIZh56gLj_Agsf2UFp_0_u6-X9UIJIxjlr4F5CIc0"

TABS = {
    "sources": [
        "source_id", "source_name", "brand_name", "source_type", "source_url",
        "collection_method", "priority_level", "collection_frequency_hours",
        "is_active", "last_collected_at", "error_count_7d", "notes",
    ],
    "raw_items": [
        "raw_id", "source_id", "ingested_at", "source_published_at",
        "source_url", "canonical_url", "email_message_id",
        "title_raw", "excerpt_raw", "body_raw", "hash_raw",
        "language", "fetch_status",
    ],
    "canonical_items": [
        "item_id", "cluster_key", "primary_brand", "primary_product",
        "version_detected", "event_type", "impact_level", "release_date",
        "first_seen_at", "last_seen_at",
        "headline_normalized", "summary_normalized", "key_points",
        "offer_type", "offer_deadline", "links_primary",
        "source_count",
        "impact_score", "freshness_score", "audience_fit_score",
        "actionability_score", "novelty_score",
        "business_value_score", "pedagogical_value_score", "noise_penalty",
        "editorial_score", "confidence_score",
        "status_editorial", "reason_rejected",
    ],
    "item_sources": [
        "item_source_id", "item_id", "raw_id", "source_role",
    ],
    "newsletter_issues": [
        "issue_id", "issue_number", "period_start", "period_end",
        "theme_main", "editorial_angle", "status",
        "draft_doc_url", "sent_at", "open_rate", "click_rate",
    ],
    "issue_items": [
        "issue_item_id", "issue_id", "item_id", "section_type", "display_order",
        "editor_note_fait", "editor_note_pourquoi", "editor_note_pour_qui",
        "editor_note_retenir", "performance_note",
    ],
    "incidents": [
        "incident_id", "detected_at", "source_id", "severity", "message", "resolved_at",
    ],
}


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
    return build("sheets", "v4", credentials=creds)


def list_existing_tabs(svc) -> list[str]:
    meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    return [s["properties"]["title"] for s in meta.get("sheets", [])]


def bootstrap(svc):
    existing = list_existing_tabs(svc)
    print(f"[INFO] Onglets existants: {existing}")

    to_create = [t for t in TABS if t not in existing]
    requests = [{"addSheet": {"properties": {"title": t}}} for t in to_create]

    if requests:
        svc.spreadsheets().batchUpdate(
            spreadsheetId=SHEET_ID, body={"requests": requests}
        ).execute()
        print(f"[OK] Crees: {to_create}")
    else:
        print("[OK] Tous les onglets existent deja")

    # Ecrire les headers (override systematique pour uniformiser)
    for tab, headers in TABS.items():
        svc.spreadsheets().values().update(
            spreadsheetId=SHEET_ID,
            range=f"{tab}!A1:{chr(64+len(headers))}1",
            valueInputOption="RAW",
            body={"values": [headers]},
        ).execute()
        print(f"[OK] Headers ecrits: {tab} ({len(headers)} cols)")

    # Supprimer Sheet1 / Feuille 1 si existe
    meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    for s in meta.get("sheets", []):
        title = s["properties"]["title"]
        if title in ("Sheet1", "Feuille 1") and len(meta["sheets"]) > 1:
            svc.spreadsheets().batchUpdate(
                spreadsheetId=SHEET_ID,
                body={"requests": [{"deleteSheet": {"sheetId": s["properties"]["sheetId"]}}]},
            ).execute()
            print(f"[OK] Supprime: {title}")


if __name__ == "__main__":
    svc = get_service()
    if "--check" in sys.argv:
        tabs = list_existing_tabs(svc)
        print(f"Onglets presents ({len(tabs)}): {tabs}")
        missing = [t for t in TABS if t not in tabs]
        if missing:
            print(f"Manquants: {missing}")
        else:
            print("Tous les onglets requis sont presents.")
    else:
        bootstrap(svc)
        print("\n[DONE] Sheet bootstrape. Tu peux relancer le workflow n8n.")
