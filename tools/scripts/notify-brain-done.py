"""Envoie une notif Discord (bot REST API) + Telegram quand brain.bat termine.

Réutilise le bot Discord existant (apps/discord-orchestrator) via DISCORD_BOT_TOKEN
et route par statut :
    - status=ok   → DISCORD_CHANNEL_OUTPUTS (livrables)
    - status=fail → DISCORD_CHANNEL_ALERTS (erreurs)
    - fallback    → DISCORD_CHANNEL_LOGS

Réutilise aussi les 4 bots Telegram existants (agents/telegram-claude/.env).
Par défaut : TELEGRAM_TOKEN_STUDIO (thématique content factory). Override via
TELEGRAM_NOTIF_TOKEN dans .env projet si tu veux forcer un autre bot (RADAR/FLOW/PULSE).

Skip silencieux si une variable manque — ne bloque jamais l'exit code de brain.bat.

Appelé depuis brain.bat en fin de pipeline :
    python tools/scripts/notify-brain-done.py --keyword "..." --pillar LMS \
        --status ok --duration 180 --exit-code 0
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DISCORD_API = "https://discord.com/api/v10"


def load_env(env_path: Path) -> dict[str, str]:
    if not env_path.exists():
        return {}
    out: dict[str, str] = {}
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def post_json(url: str, payload: dict, headers: dict | None = None, timeout: int = 10) -> tuple[int, str]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = ""
        try:
            body = exc.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        return exc.code, f"{exc.reason} — {body}" if body else exc.reason
    except Exception as exc:
        return 0, str(exc)


def build_embed(args: argparse.Namespace) -> tuple[str, dict]:
    status_icon = {"ok": "✅", "fail": "❌", "warn": "⚠️"}.get(args.status, "ℹ️")
    color = {"ok": 0x2ECC71, "fail": 0xE74C3C, "warn": 0xF1C40F}.get(args.status, 0x3498DB)
    title = f"{status_icon} brain.bat — {args.status.upper()}"

    fields = []
    if args.keyword:
        fields.append({"name": "Mot-clé", "value": f"`{args.keyword}`", "inline": True})
    if args.pillar:
        fields.append({"name": "Pillar", "value": f"`{args.pillar}`", "inline": True})
    if args.intent:
        fields.append({"name": "Intent", "value": f"`{args.intent}`", "inline": True})
    if args.duration:
        mins, secs = divmod(int(args.duration), 60)
        fields.append({"name": "Durée", "value": f"{mins}m {secs}s", "inline": True})
    if args.exit_code:
        fields.append({"name": "Exit code", "value": f"`{args.exit_code}`", "inline": True})

    embed = {"title": title, "color": color, "fields": fields}

    # Version Markdown pour Telegram (pas de embeds natifs)
    md_lines = [f"*{title}*", ""]
    for f in fields:
        md_lines.append(f"• {f['name']} : {f['value']}")
    markdown = "\n".join(md_lines)

    return markdown, embed


def notify_discord(token: str, channel_id: str, embed: dict) -> None:
    url = f"{DISCORD_API}/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {token}",
        "User-Agent": "DiscordBot (https://github.com/kihlmichael/schoolswp-telegram-agents, 1.0)",
    }
    status, detail = post_json(url, {"embeds": [embed]}, headers=headers)
    if status >= 300:
        print(f"[notify] Discord KO ({status}): {detail[:200]}", file=sys.stderr)
    else:
        print(f"[notify] Discord OK -> channel {channel_id}")


def notify_telegram(token: str, chat_id: str, markdown: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": markdown,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }
    status, detail = post_json(url, payload)
    if status >= 300:
        print(f"[notify] Telegram KO ({status}): {detail[:200]}", file=sys.stderr)
    else:
        print("[notify] Telegram OK")


def pick_discord_channel(env: dict, status: str) -> str:
    """Route par statut avec fallback LOGS."""
    by_status = {
        "ok": "DISCORD_CHANNEL_OUTPUTS",
        "fail": "DISCORD_CHANNEL_ALERTS",
        "warn": "DISCORD_CHANNEL_ALERTS",
    }
    primary = by_status.get(status, "DISCORD_CHANNEL_LOGS")
    return env.get(primary) or env.get("DISCORD_CHANNEL_LOGS") or ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Notif Discord + Telegram post-brain.bat")
    parser.add_argument("--keyword", default="")
    parser.add_argument("--pillar", default="")
    parser.add_argument("--intent", default="")
    parser.add_argument("--status", default="ok", choices=["ok", "fail", "warn"])
    parser.add_argument("--duration", type=int, default=0, help="Durée en secondes")
    parser.add_argument("--exit-code", type=int, default=0)
    args = parser.parse_args()

    # Cascade de chargement : agents/telegram-claude/.env < .env projet < process env
    tg_claude_env = load_env(PROJECT_ROOT / "agents" / "telegram-claude" / ".env")
    env = {**tg_claude_env, **load_env(PROJECT_ROOT / ".env"), **os.environ}
    markdown, embed = build_embed(args)

    # Discord via bot REST API
    discord_token = env.get("DISCORD_BOT_TOKEN", "")
    discord_channel = pick_discord_channel(env, args.status)
    if discord_token and discord_channel:
        notify_discord(discord_token, discord_channel, embed)
    else:
        print("[notify] DISCORD_BOT_TOKEN ou channel cible absent — skip Discord")

    # Telegram : override explicite > fallback STUDIO (content factory)
    tg_token = env.get("TELEGRAM_NOTIF_TOKEN") or env.get("TELEGRAM_TOKEN_STUDIO", "")
    tg_chat = env.get("TELEGRAM_NOTIF_CHAT_ID", "")
    if tg_token and tg_chat:
        notify_telegram(tg_token, tg_chat, markdown)
    elif tg_token:
        print("[notify] TELEGRAM_NOTIF_CHAT_ID absent — skip Telegram (token trouvé)")
    else:
        print("[notify] Aucun token Telegram disponible — skip Telegram")

    return 0


if __name__ == "__main__":
    sys.exit(main())
