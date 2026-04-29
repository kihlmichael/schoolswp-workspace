"""Debug ElevenLabs 403: verifie le compte, les voix dispos et le voice_id config."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")
VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "")

if not API_KEY:
    print("ERR: ELEVENLABS_API_KEY missing in .env")
    sys.exit(1)

print(f"key suffix: ...{API_KEY[-6:]}")
print(f"voice_id: {VOICE_ID}")

headers = {"xi-api-key": API_KEY, "Accept": "application/json"}

print("\n=== /v1/user ===")
r = requests.get("https://api.elevenlabs.io/v1/user", headers=headers, timeout=30)
print(f"status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    print(f"  tier: {data.get('subscription', {}).get('tier', '?')}")
    print(f"  char_count: {data.get('subscription', {}).get('character_count', '?')}")
    print(f"  char_limit: {data.get('subscription', {}).get('character_limit', '?')}")
else:
    print(f"  body: {r.text[:300]}")

print("\n=== /v1/voices (sample 10) ===")
r = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers, timeout=30)
print(f"status: {r.status_code}")
if r.status_code == 200:
    voices = r.json().get("voices", [])
    print(f"  total: {len(voices)}")
    for v in voices[:10]:
        labels = v.get("labels", {}) or {}
        lang = labels.get("language") or labels.get("accent") or "?"
        print(f"  - {v['voice_id']}  {v['name']:30}  lang={lang}")
    matched = [v for v in voices if v["voice_id"] == VOICE_ID]
    if matched:
        print(f"\n  configured voice FOUND: {matched[0]['name']}")
    else:
        print(f"\n  ERROR: configured voice_id {VOICE_ID} NOT in account")
else:
    print(f"  body: {r.text[:300]}")
