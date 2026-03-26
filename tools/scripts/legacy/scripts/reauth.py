from google_auth_oauthlib.flow import InstalledAppFlow
import webbrowser, sys

print("Démarrage authentification...", flush=True)
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

flow = InstalledAppFlow.from_client_secrets_file("../../credentials-gdrive-audit.json", SCOPES)

print("Lancement du serveur local sur http://localhost:8080 ...", flush=True)
print("Une URL va s'afficher — copie-la dans ton navigateur si l'onglet ne s'ouvre pas.\n", flush=True)

creds = flow.run_local_server(
    port=8080,
    open_browser=False,
    success_message="Authentification réussie. Tu peux fermer cet onglet."
)

with open("token-gdrive-audit.json", "w") as f:
    f.write(creds.to_json())

print("\nToken sauvegardé dans token-gdrive-audit.json", flush=True)
