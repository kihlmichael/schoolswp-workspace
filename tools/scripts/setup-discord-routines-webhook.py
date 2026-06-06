#!/usr/bin/env python3
"""
Provisionne ou récupère le webhook Discord `schoolsWP-Routines` sur le channel
#alerts du serveur schoolsWP, puis écrit `DISCORD_ROUTINES_WEBHOOK=<url>` dans
le .env racine du projet.

Idempotent : si un webhook du même nom existe déjà sur le channel, le réutilise.

Prérequis : `DISCORD_BOT_TOKEN` présent dans `.env` racine, et bot membre du
guild avec la permission Manage Webhooks sur le channel cible.

Usage :
  .venv/Scripts/python tools/scripts/setup-discord-routines-webhook.py
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
CHANNEL_ID = "1495148872312422622"  # #alerts du guild schoolsWP
WEBHOOK_NAME = "schoolsWP-Routines"
ENV_KEY = "DISCORD_ROUTINES_WEBHOOK"


def main() -> int:
    if not ENV_FILE.exists():
        print(f"ERREUR : .env introuvable ({ENV_FILE})", file=sys.stderr)
        return 1

    env = ENV_FILE.read_text(encoding="utf-8")
    m = re.search(r"^DISCORD_BOT_TOKEN=(.+)$", env, re.M)
    if not m:
        print("ERREUR : DISCORD_BOT_TOKEN absent du .env", file=sys.stderr)
        return 1
    token = m.group(1).strip().strip('"')

    headers_auth = {"Authorization": f"Bot {token}"}
    base = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/webhooks"

    # GET existing webhooks on the channel
    try:
        req = urllib.request.Request(base, headers=headers_auth, method="GET")
        existing = json.loads(urllib.request.urlopen(req).read())
    except Exception as e:
        print(f"ERREUR : GET webhooks a echoue ({e})", file=sys.stderr)
        return 1

    match = next((w for w in existing if w.get("name") == WEBHOOK_NAME), None)
    if match:
        webhook = match
        print(f"webhook '{WEBHOOK_NAME}' existant trouve (id {webhook['id']})")
    else:
        try:
            req = urllib.request.Request(
                base,
                data=json.dumps({"name": WEBHOOK_NAME}).encode(),
                headers={**headers_auth, "Content-Type": "application/json"},
                method="POST",
            )
            webhook = json.loads(urllib.request.urlopen(req).read())
        except Exception as e:
            print(f"ERREUR : creation webhook a echoue ({e})", file=sys.stderr)
            return 1
        print(f"webhook '{WEBHOOK_NAME}' cree (id {webhook['id']})")

    if not webhook.get("token"):
        print("ERREUR : webhook recu sans token (permissions insuffisantes ?)", file=sys.stderr)
        return 1

    url = f"https://discord.com/api/webhooks/{webhook['id']}/{webhook['token']}"

    # Update .env (replace if key exists, else append)
    new_line = f"{ENV_KEY}={url}"
    if re.search(rf"^{ENV_KEY}=", env, re.M):
        env = re.sub(rf"^{ENV_KEY}=.*$", new_line, env, flags=re.M)
        action = "mis a jour"
    else:
        env = env.rstrip("\n") + "\n" + new_line + "\n"
        action = "ajoute"

    ENV_FILE.write_text(env, encoding="utf-8")
    print(f"OK : {ENV_KEY} {action} dans .env")
    return 0


if __name__ == "__main__":
    sys.exit(main())
