#!/usr/bin/env python3
"""
Upload d'un fichier local vers un dossier Google Drive — schoolsWP.

Resout le probleme de taille du MCP create_file (base64 inline) en passant par
le CLI `gws` (Google Workspace) qui streame le fichier en multipart. Convient
aux PDF, images, zip et autres binaires volumineux.

S'appuie sur l'auth du projet : le CLI `gws` gere lui-meme le token (keyring +
GOOGLE_WORKSPACE_CLI_CLIENT_ID/SECRET). Aucun secret n'est lu ni affiche ici.
Si `gws auth status` renvoie token_valid:false, relancer `gws auth login`.

Usage :
  .venv/Scripts/python tools/scripts/gdrive-upload.py <fichier> --folder <ID>
  .venv/Scripts/python tools/scripts/gdrive-upload.py doc.pdf --folder 1ab... --name "Mon doc.pdf"
  .venv/Scripts/python tools/scripts/gdrive-upload.py photo.png --folder 1ab... --mime image/png

Options :
  --folder ID    Dossier Drive cible (obligatoire)
  --name NAME    Nom du fichier sur Drive (defaut : nom du fichier local)
  --mime TYPE    Type MIME source (defaut : detection auto via extension)
  --google-doc   Convertir a l'import en Google Doc (markdown/html/txt -> Doc)

Exemple conversion :
  .venv/Scripts/python tools/scripts/gdrive-upload.py script.md --folder 1ab... --google-doc --name "Mon script"
"""

import argparse
import json
import mimetypes
import os
import shutil
import subprocess
import sys


def find_gws():
    """Localise le binaire gws : env GWS_BIN, PATH, ou chemin npm par defaut."""
    env_bin = os.environ.get("GWS_BIN")
    if env_bin and os.path.isfile(env_bin):
        return env_bin
    found = shutil.which("gws")
    if found:
        return found
    default = os.path.join(
        os.environ.get("APPDATA", ""), "npm", "gws.cmd"
    )
    if os.path.isfile(default):
        return default
    print("ERREUR : binaire 'gws' introuvable (ni GWS_BIN, ni PATH, ni npm).")
    sys.exit(1)


def run_gws(gws, args):
    """Appelle gws en args-list (shell=False) pour eviter le mangle JSON Windows."""
    p = subprocess.run(
        [gws] + args, capture_output=True, text=True, encoding="utf-8", shell=False
    )
    if p.returncode != 0:
        print(f"  ERREUR gws (exit {p.returncode}) : {p.stderr.strip()[:500]}")
        return None
    out = p.stdout
    i = out.find("{")
    return json.loads(out[i:]) if i != -1 else {}


def main():
    parser = argparse.ArgumentParser(description="Upload un fichier local vers un dossier Google Drive via gws.")
    parser.add_argument("file", help="Chemin du fichier local a uploader")
    parser.add_argument("--folder", required=True, help="ID du dossier Drive cible")
    parser.add_argument("--name", help="Nom du fichier sur Drive (defaut : nom local)")
    parser.add_argument("--mime", help="Type MIME source (defaut : detection auto)")
    parser.add_argument(
        "--google-doc",
        action="store_true",
        help="Convertir a l'import en Google Doc (source markdown/html/txt -> Google Doc)",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"ERREUR : fichier introuvable : {args.file}")
        sys.exit(1)

    name = args.name or os.path.basename(args.file)
    ext = os.path.splitext(args.file)[1].lower()
    source_mime = (
        args.mime
        or mimetypes.guess_type(args.file)[0]
        or ("text/markdown" if ext in (".md", ".markdown") else "application/octet-stream")
    )
    target_mime = "application/vnd.google-apps.document" if args.google_doc else source_mime
    # Un Google Doc n'a pas d'extension : on retire celle du nom auto en mode conversion.
    if args.google_doc and not args.name and ext:
        name = os.path.splitext(name)[0]
    size_kb = os.path.getsize(args.file) / 1024
    gws = find_gws()

    print("=" * 60)
    print("  UPLOAD DRIVE (via gws)")
    print("=" * 60)
    print(f"  Fichier : {args.file} ({size_kb:.0f} Ko)")
    print(f"  Nom     : {name}")
    print(f"  Source  : {source_mime}")
    print(f"  Cible   : {target_mime}")
    print(f"  Dossier : {args.folder}")

    meta = {"name": name, "parents": [args.folder], "mimeType": target_mime}
    print("\n  Upload...")
    res = run_gws(
        gws,
        [
            "drive", "files", "create",
            "--upload", os.path.abspath(args.file),
            "--upload-content-type", source_mime,
            "--json", json.dumps(meta),
        ],
    )
    if not res or not res.get("id"):
        print("\n  ECHEC. Verifier `gws auth status` (token_valid).")
        sys.exit(1)

    file_id = res["id"]
    print("  OK\n")
    print("=" * 60)
    print(f"  ID   : {file_id}")
    print(f"  Nom  : {res.get('name', name)}")
    print(f"  Lien : https://drive.google.com/file/d/{file_id}/view")
    print("=" * 60)


if __name__ == "__main__":
    main()
