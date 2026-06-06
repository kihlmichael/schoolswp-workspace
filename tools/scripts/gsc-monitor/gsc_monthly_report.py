#!/usr/bin/env python3
"""
GSC monthly pillar monitoring for schoolsWP.

Pulls GSC data for each pillar URL listed in pillars.yaml, computes deltas
vs the previous 28-day window, and publishes a markdown report:
  - to Discord (webhook)
  - to Telegram (bot @schoolswp_bot)
  - to disk (content/audits/gsc-monthly/YYYY-MM.md)

Usage:
  .venv/Scripts/python tools/scripts/gsc-monitor/gsc_monthly_report.py [--dry-run]

Env vars required (sourced from .claude/settings.local.json):
  DISCORD_WEBHOOK_ROUTINES  : Discord webhook URL for #schoolswp-routines channel
  TELEGRAM_BOT_TOKEN         : @schoolswp_bot token
  TELEGRAM_CHAT_ID_MICHAEL   : Michael's chat ID

GSC access is via the gsc-mcp server already configured in .mcp.json. This script
acts as a local fallback / orchestration shim; the cron remote agent will reuse
the same logic via gsc-mcp tool calls directly.
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SETTINGS = ROOT / ".claude" / "settings.local.json"
PILLARS_YAML = Path(__file__).parent / "pillars.yaml"
ARCHIVE_DIR = ROOT / "content" / "audits" / "gsc-monthly"


def load_env():
    return json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})


def parse_yaml_simple(text):
    """Minimal YAML parser sufficient for pillars.yaml structure (no pyyaml dep)."""
    import re
    out = {"pillars": [], "notifications": {}, "alerts": {}}
    current_list = None
    current_item = None
    current_section = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        # top-level keys
        m = re.match(r"^(\w[\w_-]*):\s*(.*)$", line)
        if m and not line.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            if key == "site":
                out["site"] = val
            elif key == "pillars":
                current_list = out["pillars"]
                current_section = "pillars"
            elif key == "notifications":
                current_section = "notifications"
            elif key == "alerts":
                current_section = "alerts"
            continue
        # list item start
        m = re.match(r"^\s*-\s+(\w[\w_-]*):\s*(.*)$", line)
        if m and current_section == "pillars":
            if current_item:
                current_list.append(current_item)
            current_item = {m.group(1): _coerce(m.group(2))}
            continue
        # nested key under item or section
        m = re.match(r"^\s+(\w[\w_-]*):\s*(.*)$", line)
        if m:
            k, v = m.group(1), _coerce(m.group(2).strip())
            if current_section == "pillars" and current_item is not None:
                current_item[k] = v
            elif current_section in ("notifications", "alerts"):
                # treat all nested as flat for these
                out[current_section][k] = v
            continue
    if current_item:
        current_list.append(current_item)
    return out


def _coerce(val):
    if val.lower() in ("true", "yes"):
        return True
    if val.lower() in ("false", "no"):
        return False
    if val.isdigit():
        return int(val)
    if val.startswith('"') and val.endswith('"'):
        return val[1:-1]
    return val


def fetch_gsc_via_mcp_proxy(site_url, page_url, start_date, end_date):
    """Stub: the cron remote agent will call gsc-mcp directly via MCP tools.
    Local runs print a placeholder unless GSC_OAUTH credentials are present.
    """
    # When invoked locally without OAuth, return a placeholder structure.
    # The real implementation runs as a remote agent prompt that calls
    # mcp__gsc-mcp__get_search_analytics with site_url + page filter.
    return {
        "page": page_url,
        "start": start_date,
        "end": end_date,
        "clicks": None,
        "impressions": None,
        "ctr": None,
        "position": None,
        "stub": True,
    }


def compute_delta(curr, prev):
    if curr is None or prev is None:
        return None
    if prev == 0:
        return None if curr == 0 else float("inf")
    return round((curr - prev) / prev * 100, 1)


def build_report(pillars, site_url, period_curr, period_prev):
    """Build the markdown report. Stub data when offline."""
    today = date.today().isoformat()
    lines = [
        f"# Rapport GSC mensuel schoolsWP — {today}",
        "",
        f"**Site** : {site_url}  ",
        f"**Période actuelle** : {period_curr[0]} → {period_curr[1]} (28j)  ",
        f"**Période M-1** : {period_prev[0]} → {period_prev[1]} (28j)",
        "",
        "## Piliers suivis",
        "",
        "| # | Pilier | Clics | Δ vs M-1 | Position | Δ rang | Notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, p in enumerate(pillars, 1):
        url = p.get("url", "")
        label = p.get("label", p.get("id", "?"))
        if not url:
            lines.append(f"| {i} | {label} | - | - | - | - | ⚠️ URL non renseignée |")
            continue
        # Stub data — real agent fills via gsc-mcp
        lines.append(
            f"| {i} | [{label}]({url}) | _stub_ | _stub_ | _stub_ | _stub_ | "
            f"{'✓' if p.get('confirmed') else '⚠️ à vérifier'} |"
        )
    lines.append("")
    lines.append("## Alertes")
    lines.append("")
    lines.append("_Aucune (script local — alertes générées par la routine remote uniquement)._")
    lines.append("")
    lines.append("---")
    lines.append("_Généré localement par gsc_monthly_report.py — pour le rapport mensuel automatique, voir la routine `gsc-monitor-monthly` programmée via /schedule._")
    return "\n".join(lines)


def post_discord(webhook_url, content):
    if not webhook_url:
        print("[discord] no webhook configured, skipping")
        return
    payload = json.dumps({"content": content[:1900]}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url, data=payload, method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            print(f"[discord] HTTP {r.status}")
    except urllib.error.HTTPError as e:
        print(f"[discord] error {e.code}: {e.read()[:200]}")


def post_telegram(bot_token, chat_id, text):
    if not bot_token or not chat_id:
        print("[telegram] missing token or chat_id, skipping")
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": text[:3900],
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST",
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            print(f"[telegram] HTTP {r.status}")
    except urllib.error.HTTPError as e:
        print(f"[telegram] error {e.code}: {e.read()[:200]}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Skip Discord/Telegram, write file only")
    args = parser.parse_args()

    env = load_env()
    config = parse_yaml_simple(PILLARS_YAML.read_text(encoding="utf-8"))
    pillars = config["pillars"]
    site_url = config.get("site", "https://schoolswp.com/")

    today = date.today()
    end_curr = today.replace(day=1) - timedelta(days=1)
    start_curr = end_curr - timedelta(days=27)
    end_prev = start_curr - timedelta(days=1)
    start_prev = end_prev - timedelta(days=27)

    report = build_report(
        pillars, site_url,
        (start_curr.isoformat(), end_curr.isoformat()),
        (start_prev.isoformat(), end_prev.isoformat()),
    )

    # Write archive
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = ARCHIVE_DIR / f"{today.strftime('%Y-%m')}.md"
    archive_path.write_text(report, encoding="utf-8")
    print(f"[archive] wrote {archive_path}")

    if args.dry_run:
        print("[dry-run] skipping Discord + Telegram")
        print()
        print(report[:2000])
        return

    post_discord(env.get("DISCORD_WEBHOOK_ROUTINES"), report)
    post_telegram(env.get("TELEGRAM_BOT_TOKEN"), env.get("TELEGRAM_CHAT_ID_MICHAEL"), report)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
