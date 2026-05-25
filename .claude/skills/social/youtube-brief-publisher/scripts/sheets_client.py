import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]


def get_google_credentials():
    """
    Loads Google credentials. Supports:
    1. Active OAuth2 user token from local files (e.g., token-gdrive-migration.json, token-sheets-veille.json)
    2. Interactive OAuth2 InstalledAppFlow using credentials-gdrive-audit.json (if token is expired/invalid).
    3. Service Account JSON from env var GOOGLE_APPLICATION_CREDENTIALS_JSON or GOOGLE_APPLICATION_CREDENTIALS file.
    """
    # 1. Tente de charger un token OAuth2 existant (très probable et fonctionnel sur ce système)
    token_dirs = [
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
            "tools",
            "scripts",
        ),
        os.path.join(os.getcwd(), "tools", "scripts"),
    ]

    token_files = ["token-gdrive-migration.json", "token-sheets-veille.json", "token-cci-v2.json"]

    for token_dir in token_dirs:
        for token_file in token_files:
            token_path = os.path.join(token_dir, token_file)
            if os.path.exists(token_path):
                try:
                    from google.auth.transport.requests import Request
                    from google.oauth2.credentials import Credentials

                    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
                    if creds and creds.valid:
                        return creds
                    if creds and creds.expired and creds.refresh_token:
                        print(f"[INFO] Rafraîchissement du token OAuth2 existant depuis : {token_file}")
                        creds.refresh(Request())
                        with open(token_path, "w", encoding="utf-8") as f:
                            f.write(creds.to_json())
                        return creds
                except Exception as e:
                    print(f"[WARNING] Impossible de rafraîchir {token_file} ({e}), tentative de ré-autorisation...")

    # 2. Si le token est invalide ou absent, tenter le flux interactif InstalledAppFlow
    for token_dir in token_dirs:
        creds_path = os.path.join(token_dir, "credentials-gdrive-audit.json")
        if os.path.exists(creds_path):
            try:
                from google_auth_oauthlib.flow import InstalledAppFlow

                print(f"[INFO] Lancement du flux d'autorisation OAuth2 interactif avec {creds_path}...")
                flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                creds = flow.run_local_server(port=0)

                # Sauvegarde le nouveau token pour les prochaines exécutions
                target_token_path = os.path.join(token_dir, "token-gdrive-migration.json")
                with open(target_token_path, "w", encoding="utf-8") as f:
                    f.write(creds.to_json())
                print(f"[SUCCESS] Nouveau token enregistré dans : {target_token_path}")
                return creds
            except Exception as e:
                print(f"[WARNING] Échec du flux interactif OAuth2 : {e}")

    # 3. Fallback sur le Service Account JSON si aucun token utilisateur n'est disponible
    cred_env = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if cred_env and not cred_env.startswith("__"):
        try:
            cred_info = json.loads(cred_env)
            return service_account.Credentials.from_service_account_info(cred_info, scopes=SCOPES)
        except json.JSONDecodeError:
            if os.path.exists(cred_env):
                return service_account.Credentials.from_service_account_file(cred_env, scopes=SCOPES)

    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if cred_path and os.path.exists(cred_path):
        return service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)

    raise ValueError("Aucun token utilisateur OAuth2 valide trouvé dans 'tools/scripts' ni Service Account configuré.")


def get_sheets_service():
    creds = get_google_credentials()
    return build("sheets", "v4", credentials=creds)


def get_all_rows(spreadsheet_id, sheet_tab="Untitled"):
    """
    Returns all values from the Google Sheet range A:L.
    """
    svc = get_sheets_service()
    range_name = f"{sheet_tab}!A:L"
    res = svc.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return res.get("values", [])


def append_received_row(spreadsheet_id, sheet_tab, date_iso, url, brief_user, video_id, language="francais"):
    """
    Appends a new received row to the Google Sheet.
    A:date | B:url | C:brief_user | D:video_id | E:language | F:status
    """
    svc = get_sheets_service()
    range_name = f"{sheet_tab}!A:F"
    values = [[date_iso, url, brief_user, video_id, language, "received"]]

    body = {"values": values}
    print(f"[INFO] Ingestion de la demande dans Sheets (Video ID: {video_id})...")
    res = (
        svc.spreadsheets()
        .values()
        .append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body,
        )
        .execute()
    )
    print("[SUCCESS] Nouvelle ligne insérée dans Sheets.")
    return res


def update_ready_row(spreadsheet_id, sheet_tab, video_id, brief_schoolswp, title_fr, description_fr, tags_fr):
    """
    Finds the row by video_id and updates it with the generated brief and SEO metadata.
    Updates columns G:J (G:brief_schoolswp, H:title_fr, I:description_fr, J:tags_fr)
    and column F (status -> "ready").
    """
    svc = get_sheets_service()
    rows = get_all_rows(spreadsheet_id, sheet_tab)

    if not rows:
        raise ValueError("Google Sheet vide ou inaccessible.")

    # Recherche de l'index de ligne correspondant au video_id (colonne D, index 3)
    target_row_idx = None
    for idx, row in enumerate(rows):
        if len(row) > 3 and row[3] == video_id:
            target_row_idx = idx + 1  # Google Sheets est 1-indexé
            break

    if not target_row_idx:
        raise ValueError(f"Impossible de trouver une ligne correspondant à l'ID vidéo : {video_id}")

    print(f"[INFO] Mise à jour des métadonnées SEO dans Sheets à la ligne {target_row_idx}...")

    # 1. Mettre à jour le statut en "ready" (Colonne F, index 5)
    svc.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_tab}!F{target_row_idx}",
        valueInputOption="USER_ENTERED",
        body={"values": [["ready"]]},
    ).execute()

    # 2. Mettre à jour les colonnes G à J (Brief, Titre, Description, Tags)
    values = [[brief_schoolswp, title_fr, description_fr, tags_fr]]

    svc.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_tab}!G{target_row_idx}:J{target_row_idx}",
        valueInputOption="USER_ENTERED",
        body={"values": values},
    ).execute()

    print("[SUCCESS] Données éditoriales injectées dans Google Sheets.")
    return True


def read_ready_rows(spreadsheet_id, sheet_tab="Untitled"):
    """
    Reads all rows from the spreadsheet that have status == "ready" and return them as a list of dicts.
    """
    rows = get_all_rows(spreadsheet_id, sheet_tab)
    if not rows:
        return []

    headers = rows[0]
    ready_items = []

    for idx, row in enumerate(rows[1:], start=2):
        # Mappe la ligne sous forme de dictionnaire pour plus de lisibilité
        row_dict = {}
        for col_idx, header in enumerate(headers):
            row_dict[header] = row[col_idx] if col_idx < len(row) else ""

        row_dict["_row_number"] = idx

        # Vérifie si le statut est "ready"
        if row_dict.get("status") == "ready":
            ready_items.append(row_dict)

    return ready_items


def update_published_row(spreadsheet_id, sheet_tab, video_id, published_at_iso):
    """
    Marks the row corresponding to video_id as status="published" and sets published_at.
    """
    svc = get_sheets_service()
    rows = get_all_rows(spreadsheet_id, sheet_tab)

    target_row_idx = None
    for idx, row in enumerate(rows):
        if len(row) > 3 and row[3] == video_id:
            target_row_idx = idx + 1
            break

    if not target_row_idx:
        raise ValueError(f"Impossible de trouver l'ID vidéo {video_id} pour finaliser la publication.")

    print(f"[INFO] Clôture de la publication pour {video_id} à la ligne {target_row_idx}...")

    # Met à jour le status en "published" (Colonne F, index 5)
    svc.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_tab}!F{target_row_idx}",
        valueInputOption="USER_ENTERED",
        body={"values": [["published"]]},
    ).execute()

    # Met à jour published_at (Colonne L, index 11)
    svc.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_tab}!L{target_row_idx}",
        valueInputOption="USER_ENTERED",
        body={"values": [[published_at_iso]]},
    ).execute()

    print("[SUCCESS] Ligne mise à jour à 'published'.")
    return True
