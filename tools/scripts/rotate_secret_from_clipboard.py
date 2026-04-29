"""Rotate a secret in .claude/settings.local.json from the system clipboard.

Reads the clipboard, validates the value matches the expected pattern, then writes
it to the named env key. The secret never appears on stdout or in the chat transcript.

Usage:
    python tools/scripts/rotate_secret_from_clipboard.py RAPIDAPI_KEY
    python tools/scripts/rotate_secret_from_clipboard.py DISCORD_BOT_TOKEN
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SETTINGS = PROJECT_ROOT / ".claude" / "settings.local.json"

# Validation patterns per known secret name (regex)
PATTERNS: dict[str, str] = {
    "RAPIDAPI_KEY": r"^[A-Za-z0-9]{40,80}$",
    "DISCORD_BOT_TOKEN": r"^[A-Za-z0-9_\-\.]{50,90}$",
    "GITHUB_TOKEN": r"^(ghp_|github_pat_)[A-Za-z0-9_]{20,}$",
    "FIRECRAWL_API_KEY": r"^fc-[A-Za-z0-9]{20,}$",
    "GEMINI_API_KEY": r"^AIza[A-Za-z0-9_\-]{30,}$",
}


def read_clipboard() -> str:
    """Read text clipboard via PowerShell (Windows-only)."""
    out = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", "Get-Clipboard -Raw"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return out.stdout.strip()


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    name = sys.argv[1].strip().upper()
    pattern = PATTERNS.get(name)
    if not pattern:
        print(f"ERROR: unknown secret name '{name}'. Add a regex to PATTERNS first.")
        return 2

    if not SETTINGS.exists():
        print(f"ERROR: {SETTINGS} not found")
        return 2

    try:
        value = read_clipboard()
    except subprocess.CalledProcessError as e:
        print(f"ERROR: failed to read clipboard: {e}")
        return 2

    if not value:
        print("ERROR: clipboard is empty")
        return 2

    if not re.match(pattern, value):
        print(
            f"ERROR: clipboard does not match pattern for {name}\n"
            f"  expected regex: {pattern}\n"
            f"  clipboard length: {len(value)} chars\n"
            f"  first/last 4: {value[:4]}...{value[-4:]}"
        )
        return 2

    settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = settings.setdefault("env", {})
    old = env.get(name)
    if old == value:
        print(f"OK: {name} already up to date in {SETTINGS.name} (no change)")
        return 0

    env[name] = value
    SETTINGS.write_text(
        json.dumps(settings, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    old_hint = f"{old[:4]}...{old[-4:]}" if old else "(was unset)"
    new_hint = f"{value[:4]}...{value[-4:]}"
    print(f"OK: {name} rotated in {SETTINGS.name}")
    print(f"  old: {old_hint}")
    print(f"  new: {new_hint}")
    print(f"  length: {len(value)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
