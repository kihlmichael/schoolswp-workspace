"""Build manifest for enescingoz/awesome-n8n-templates.

Parses the GitHub tree API to list all .json templates, and optionally
downloads each one to extract integration and trigger metadata.

Usage:
    py build_manifest.py            # fast: names + categories only
    py build_manifest.py --deep     # slow: download each JSON, extract node types
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

import requests

REPO = "enescingoz/awesome-n8n-templates"
BRANCH = "main"
TREE_API = f"https://api.github.com/repos/{REPO}/git/trees/{BRANCH}?recursive=1"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

CATEGORY_DIRS = {
    "WordPress",
    "Gmail_and_Email_Automation",
    "Telegram",
    "Slack",
    "Discord",
    "WhatsApp",
    "Notion",
    "OpenAI_and_LLMs",
    "Airtable",
    "Google_Drive_and_Google_Sheets",
    "Forms_and_Surveys",
    "PDF_and_Document_Processing",
    "devops",
    "HR_and_Recruitment",
    "AI_Research_RAG_and_Data_Analysis",
    "Instagram_Twitter_Social_Media",
    "Database_and_Storage",
    "Other",
    "Other_Integrations_and_Use_Cases",
}

INTEGRATION_PATTERNS = {
    "wordpress": r"n8n-nodes-base\.wordpress",
    "openai": r"n8n-nodes-langchain\.(lmChatOpenAi|embeddingsOpenAi)",
    "anthropic": r"n8n-nodes-langchain\.lmChatAnthropic",
    "supabase": r"n8n-nodes-langchain\.vectorStoreSupabase|n8n-nodes-base\.supabase",
    "pinecone": r"n8n-nodes-langchain\.vectorStorePinecone",
    "gmail": r"n8n-nodes-base\.gmail",
    "telegram": r"n8n-nodes-base\.telegram",
    "slack": r"n8n-nodes-base\.slack",
    "discord": r"n8n-nodes-base\.discord",
    "notion": r"n8n-nodes-base\.notion",
    "airtable": r"n8n-nodes-base\.airtable",
    "google_sheets": r"n8n-nodes-base\.googleSheets",
    "google_drive": r"n8n-nodes-base\.googleDrive",
    "webhook": r"n8n-nodes-base\.webhook",
    "schedule_trigger": r"n8n-nodes-base\.scheduleTrigger",
    "http_request": r"n8n-nodes-base\.httpRequest",
    "cohere": r"n8n-nodes-langchain\.embeddingsCohere",
    "ollama": r"n8n-nodes-langchain\.(lmChatOllama|embeddingsOllama)",
    "deepseek": r"deepseek",
}

TRIGGER_PATTERNS = {
    "webhook": r"n8n-nodes-base\.webhook",
    "schedule": r"n8n-nodes-base\.scheduleTrigger",
    "manual": r"n8n-nodes-base\.manualTrigger",
    "gmail_trigger": r"n8n-nodes-base\.gmailTrigger",
    "telegram_trigger": r"n8n-nodes-base\.telegramTrigger",
    "wordpress_trigger": r"n8n-nodes-base\.wordpressTrigger",
}


def fetch_tree(session: requests.Session) -> list[dict]:
    r = session.get(TREE_API, timeout=30)
    r.raise_for_status()
    data = r.json()
    if data.get("truncated"):
        print("WARNING: tree is truncated, manifest may be incomplete", file=sys.stderr)
    return data["tree"]


def fetch_raw(session: requests.Session, path: str) -> str | None:
    url = f"{RAW_BASE}/{quote(path)}"
    r = session.get(url, timeout=30)
    if r.status_code != 200:
        return None
    return r.text


def extract_matches(patterns: dict[str, str], content: str) -> list[str]:
    matches = []
    for name, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            matches.append(name)
    return matches


def build_entry(node: dict, deep: bool, session: requests.Session) -> dict | None:
    if node["type"] != "blob":
        return None
    path = node["path"]
    if not path.endswith(".json"):
        return None
    parts = path.split("/")
    if len(parts) < 2:
        return None
    category = parts[0]
    if category not in CATEGORY_DIRS:
        return None
    size_kb = round(node["size"] / 1024, 1)
    entry = {
        "name": Path(path).stem,
        "category": category,
        "path": path,
        "raw_url": f"{RAW_BASE}/{quote(path)}",
        "size_kb": size_kb,
        "integrations": [],
        "triggers": [],
    }
    if deep:
        raw = fetch_raw(session, path)
        if raw:
            entry["integrations"] = extract_matches(INTEGRATION_PATTERNS, raw)
            entry["triggers"] = extract_matches(TRIGGER_PATTERNS, raw)
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deep", action="store_true", help="Download each JSON to extract integrations/triggers (slow)"
    )
    parser.add_argument("--out", default=None, help="Output path (default: <skill_dir>/data/enescingoz-manifest.json)")
    args = parser.parse_args()

    default_out = Path(__file__).parent.parent / "data" / "enescingoz-manifest.json"
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "schoolswp-n8n-template-finder/1.0"})

    print(f"Fetching tree from {REPO}...", file=sys.stderr)
    tree = fetch_tree(session)

    templates = []
    for node in tree:
        entry = build_entry(node, args.deep, session)
        if entry:
            templates.append(entry)
            if args.deep:
                print(f"  indexed: {entry['name'][:60]}", file=sys.stderr)

    templates.sort(key=lambda t: (t["category"], t["name"].lower()))

    manifest = {
        "source_repo": REPO,
        "source_branch": BRANCH,
        "total": len(templates),
        "deep": args.deep,
        "categories": sorted({t["category"] for t in templates}),
        "templates": templates,
    }
    out_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Indexed {len(templates)} templates across {len(manifest['categories'])} categories", file=sys.stderr)
    print(f"Manifest written to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
