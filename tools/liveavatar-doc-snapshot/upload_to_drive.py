#!/usr/bin/env python3
"""Mirror a local snapshot directory to Google Drive, preserving the folder structure.

Uses the `gws` CLI (Google Workspace, OAuth refresh token already configured on this host).
Find-or-create for every folder so the script is idempotent for FOLDERS. Files are uploaded
fresh on each run, so point --parent at a NEW dated folder for monthly history rather than
re-running into the same target (which would duplicate files).

Usage:
  python upload_to_drive.py --src <dir> --parent <drive_folder_id> --name <folder_name>

Example (LiveAvatar, into schoolsWP-hub/HeyGen):
  python upload_to_drive.py --src snapshots/2026-07-01 --parent <heygen_id> --name 2026-07-01
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

FOLDER_MIME = "application/vnd.google-apps.folder"


def find_gws() -> str:
    env_bin = os.environ.get("GWS_BIN")
    if env_bin and os.path.isfile(env_bin):
        return env_bin
    found = shutil.which("gws")
    if found:
        return found
    default = os.path.join(os.environ.get("APPDATA", ""), "npm", "gws.cmd")
    if os.path.isfile(default):
        return default
    print("ERREUR : binaire 'gws' introuvable.")
    sys.exit(1)


GWS = find_gws()


def run_gws(args: list[str]) -> dict | None:
    p = subprocess.run([GWS] + args, capture_output=True, text=True, encoding="utf-8", shell=False)
    if p.returncode != 0:
        print(f"  ERREUR gws (exit {p.returncode}) : {p.stderr.strip()[:400]}")
        return None
    out = p.stdout
    i = out.find("{")
    return json.loads(out[i:]) if i != -1 else {}


def mime_of(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in (".md", ".markdown"):
        return "text/markdown"
    if ext == ".txt":
        return "text/plain"
    if ext == ".json":
        return "application/json"
    return mimetypes.guess_type(str(path))[0] or "application/octet-stream"


def find_folder(name: str, parent_id: str) -> str | None:
    q = f"name = '{name}' and '{parent_id}' in parents and mimeType = '{FOLDER_MIME}' and trashed = false"
    res = run_gws(["drive", "files", "list", "--params", json.dumps({"q": q, "fields": "files(id,name)"})])
    if res and res.get("files"):
        return res["files"][0]["id"]
    return None


def ensure_folder(name: str, parent_id: str) -> str:
    fid = find_folder(name, parent_id)
    if fid:
        return fid
    meta = {"name": name, "parents": [parent_id], "mimeType": FOLDER_MIME}
    res = run_gws(["drive", "files", "create", "--json", json.dumps(meta)])
    if not res or not res.get("id"):
        raise RuntimeError(f"echec creation dossier {name}")
    return res["id"]


def upload_file(path: Path, parent_id: str) -> str | None:
    meta = {"name": path.name, "parents": [parent_id], "mimeType": mime_of(path)}
    res = run_gws(
        [
            "drive",
            "files",
            "create",
            "--upload",
            str(path),
            "--upload-content-type",
            mime_of(path),
            "--json",
            json.dumps(meta),
        ]
    )
    return res.get("id") if res else None


def main() -> None:
    ap = argparse.ArgumentParser(description="Mirror a local dir to Google Drive via gws.")
    ap.add_argument("--src", required=True, help="Local source directory")
    ap.add_argument("--parent", required=True, help="Drive parent folder id")
    ap.add_argument("--name", required=True, help="Name of the root folder to create under parent")
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_dir():
        print(f"ERREUR : source introuvable {src}")
        sys.exit(1)

    root_id = ensure_folder(args.name, args.parent)
    print(f"Root folder '{args.name}': {root_id}")
    folder_cache: dict[str, str] = {"": root_id}

    def ensure_path(rel: str) -> str:
        rel = rel.replace("\\", "/").strip("/")
        if rel in folder_cache:
            return folder_cache[rel]
        cur_id = folder_cache[""]
        parent = ""
        for part in rel.split("/"):
            parent = (parent + "/" + part).strip("/")
            if parent in folder_cache:
                cur_id = folder_cache[parent]
            else:
                cur_id = ensure_folder(part, cur_id)
                folder_cache[parent] = cur_id
        return cur_id

    n_ok = n_fail = 0
    files = sorted(p for p in src.rglob("*") if p.is_file())
    for i, fpath in enumerate(files, 1):
        rel_dir = str(fpath.parent.relative_to(src))
        if rel_dir == ".":
            rel_dir = ""
        fid = upload_file(fpath, ensure_path(rel_dir))
        rel_file = str(fpath.relative_to(src)).replace("\\", "/")
        if fid:
            n_ok += 1
            print(f"  [{i}/{len(files)}] OK   {rel_file}")
        else:
            n_fail += 1
            print(f"  [{i}/{len(files)}] FAIL {rel_file}")
        time.sleep(0.1)

    print(f"\n=== Done: {n_ok} uploaded, {n_fail} failed. ===")
    print(f"Folder: https://drive.google.com/drive/folders/{root_id}")
    if n_fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
