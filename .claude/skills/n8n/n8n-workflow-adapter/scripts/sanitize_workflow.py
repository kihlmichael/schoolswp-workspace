"""Sanitize an external n8n workflow for schoolsWP import.

Input: a workflow .json file (from enescingoz, n8n.io, or any external source).
Output: a sanitized .json with schoolsWP credential IDs, conventions, and hygiene.

This script performs the mechanical substitutions. It does NOT decide credential
mappings for ambiguous cases — those are flagged to stderr for the human operator.

Usage:
    py sanitize_workflow.py input.json --out output.json
    py sanitize_workflow.py input.json --out output.json --workflow-name wp-auto-tag-posts-W201
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import uuid
from pathlib import Path

CREDENTIAL_MAPPING_BY_ID = {
    "ANTHROPIC_API": "anthropic-main",
    "SUPABASE_API": "supabase-schoolswp",
    "WORDPRESS_API": "wp-schoolswp-main",
    "GMAIL_API": "gmail-michael-perso",
    "GOOGLE_SHEETS_API": "google-sheets-schoolswp",
    "GOOGLE_DRIVE_API": "google-drive-schoolswp",
    "DISCORD_API": "discord-webhook-schoolswp",
}

CREDENTIAL_MAPPING_BY_TYPE = {
    "anthropicApi": "anthropic-main",
    "supabaseApi": "supabase-schoolswp",
    "wordpressApi": "wp-schoolswp-main",
    "gmailOAuth2": "gmail-michael-perso",
    "googleSheetsOAuth2Api": "google-sheets-schoolswp",
    "googleDriveOAuth2Api": "google-drive-schoolswp",
    "discordWebhookApi": "discord-webhook-schoolswp",
}

CREDENTIAL_FLAG_BY_ID = {
    "OPENAI_API": "stack schoolsWP = Anthropic par défaut, confirmer si OpenAI vraiment voulu",
    "COHERE_API": "Cohere non configuré côté instance, proposer alternative",
    "PINECONE_API": "Pinecone non configuré, proposer swap vers Supabase vector",
    "TELEGRAM_BOT": "9 bots actifs, demander lequel",
    "NOTION_API": "vérifier si compte Notion à connecter",
    "AIRTABLE_API": "non configuré par défaut",
    "HUBSPOT_API": "pas dans la stack schoolsWP",
    "MAILCHIMP_API": "pas dans la stack, FluentCRM à la place via webhook",
    "SENDGRID_API": "pas dans la stack schoolsWP",
    "SLACK_API": "pas de Slack schoolsWP, swap vers Discord webhook",
}

CREDENTIAL_FLAG_BY_TYPE = {
    "openAiApi": "stack schoolsWP = Anthropic par défaut, confirmer si OpenAI vraiment voulu",
    "cohereApi": "Cohere non configuré côté instance, proposer alternative",
    "pineconeApi": "Pinecone non configuré, proposer swap vers Supabase vector",
    "telegramApi": "9 bots actifs, demander lequel",
    "notionApi": "vérifier si compte Notion à connecter",
    "airtableApi": "non configuré par défaut",
    "hubspotApi": "pas dans la stack schoolsWP",
    "mailchimpApi": "pas dans la stack, FluentCRM à la place via webhook",
    "sendGridApi": "pas dans la stack schoolsWP",
    "slackApi": "pas de Slack schoolsWP, swap vers Discord webhook",
}

URL_REPLACEMENTS = {
    "https://example.com": "https://schoolswp.com",
    "https://yoursite.com": "https://schoolswp.com",
    "http://example.com": "https://schoolswp.com",
}

MODEL_HINTS = {
    "gpt-4-turbo": "claude-sonnet-4-6",
    "gpt-4o": "claude-sonnet-4-6",
    "gpt-4": "claude-sonnet-4-6",
    "gpt-3.5-turbo": "claude-haiku-4-5-20251001",
}

STICKY_NOTE_PLACEHOLDER = re.compile(r"^Placeholder for\s+", re.IGNORECASE)


def load_workflow(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: invalid JSON in {path}: {e}")


def validate_structure(wf: dict) -> list[str]:
    issues = []
    for key in ("name", "nodes", "connections"):
        if key not in wf:
            issues.append(f"missing key: {key}")
    if "nodes" in wf and not isinstance(wf["nodes"], list):
        issues.append("'nodes' is not a list")
    return issues


def sanitize_credentials(wf: dict, report: dict) -> None:
    for node in wf.get("nodes", []):
        creds = node.get("credentials")
        if not creds:
            continue
        for cred_type, cred_info in list(creds.items()):
            if not isinstance(cred_info, dict):
                continue
            cred_id = cred_info.get("id", "")
            node_name = node.get("name", "?")

            if cred_id in CREDENTIAL_MAPPING_BY_ID:
                new_id = CREDENTIAL_MAPPING_BY_ID[cred_id]
                cred_info["id"] = new_id
                cred_info["name"] = new_id
                report["credentials_remapped"].append(f"{node_name}: [{cred_type}] id={cred_id} -> {new_id}")
                continue
            if cred_id in CREDENTIAL_FLAG_BY_ID:
                report["credentials_flagged"].append(
                    f"{node_name}: [{cred_type}] id={cred_id} ({CREDENTIAL_FLAG_BY_ID[cred_id]})"
                )
                continue

            if cred_type in CREDENTIAL_MAPPING_BY_TYPE:
                new_id = CREDENTIAL_MAPPING_BY_TYPE[cred_type]
                cred_info["id"] = new_id
                cred_info["name"] = new_id
                report["credentials_remapped"].append(f"{node_name}: [{cred_type}] -> {new_id}")
                continue
            if cred_type in CREDENTIAL_FLAG_BY_TYPE:
                report["credentials_flagged"].append(
                    f"{node_name}: [{cred_type}] ({CREDENTIAL_FLAG_BY_TYPE[cred_type]})"
                )


def strip_placeholder_sticky_notes(wf: dict, report: dict) -> None:
    nodes = wf.get("nodes", [])
    keep = []
    removed = 0
    for node in nodes:
        if node.get("type") == "n8n-nodes-base.stickyNote":
            content = (node.get("parameters") or {}).get("content", "")
            if STICKY_NOTE_PLACEHOLDER.match(content):
                removed += 1
                continue
        keep.append(node)
    wf["nodes"] = keep
    if removed:
        report["sticky_notes_removed"] = removed


def replace_urls(wf: dict, report: dict) -> None:
    raw = json.dumps(wf, ensure_ascii=False)
    count = 0
    for old, new in URL_REPLACEMENTS.items():
        occ = raw.count(old)
        if occ:
            raw = raw.replace(old, new)
            count += occ
    if count:
        report["urls_replaced"] = count
        new_wf = json.loads(raw)
        wf.clear()
        wf.update(new_wf)


def regenerate_webhook_paths(wf: dict, report: dict) -> None:
    changed = 0
    for node in wf.get("nodes", []):
        if node.get("type") == "n8n-nodes-base.webhook":
            params = node.setdefault("parameters", {})
            old_path = params.get("path", "")
            new_path = str(uuid.uuid4())
            params["path"] = new_path
            changed += 1
            report["webhook_paths_regenerated"].append(
                f"{node.get('name', '?')}: {old_path or '(empty)'} -> {new_path}"
            )
    if changed:
        report["webhook_paths_count"] = changed


def flag_llm_models(wf: dict, report: dict) -> None:
    for node in wf.get("nodes", []):
        params = node.get("parameters") or {}
        model = params.get("model")
        if isinstance(model, str) and model in MODEL_HINTS:
            report["llm_model_hints"].append(f"{node.get('name', '?')}: {model} -> suggested {MODEL_HINTS[model]}")


def rename_workflow(wf: dict, new_name: str | None, report: dict) -> None:
    if new_name:
        report["workflow_renamed"] = f"{wf.get('name', '?')} -> {new_name}"
        wf["name"] = new_name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to input workflow .json")
    parser.add_argument("--out", required=True, help="Path to output .json")
    parser.add_argument(
        "--workflow-name", default=None, help="New workflow name (convention: <domaine>-<verbe>-<sujet>-W<num>)"
    )
    parser.add_argument("--force", action="store_true", help="Overwrite output if it exists")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.out)

    if not in_path.exists():
        sys.exit(f"ERROR: input not found: {in_path}")
    if out_path.exists() and not args.force:
        sys.exit(f"ERROR: output exists, use --force to overwrite: {out_path}")

    wf = load_workflow(in_path)
    issues = validate_structure(wf)
    if issues:
        sys.exit("ERROR: invalid workflow structure:\n  " + "\n  ".join(issues))

    report = {
        "input": str(in_path),
        "output": str(out_path),
        "credentials_remapped": [],
        "credentials_flagged": [],
        "sticky_notes_removed": 0,
        "urls_replaced": 0,
        "webhook_paths_regenerated": [],
        "webhook_paths_count": 0,
        "llm_model_hints": [],
        "workflow_renamed": None,
    }

    strip_placeholder_sticky_notes(wf, report)
    sanitize_credentials(wf, report)
    replace_urls(wf, report)
    regenerate_webhook_paths(wf, report)
    flag_llm_models(wf, report)
    rename_workflow(wf, args.workflow_name, report)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(wf, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
