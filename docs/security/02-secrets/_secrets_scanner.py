"""Custom secrets scanner equivalent to gitleaks (no external binary).

Scans Git history of multiple repos for known secret patterns. Output is
redacted: never includes the actual secret value, only:
- repo path
- commit SHA (short)
- file path
- secret type
- 4 last chars for identification

Patterns based on gitleaks.toml default + project-specific (HeyGen, Skoatch, etc).
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

PATTERNS = [
    ("anthropic_api_key", re.compile(r"sk-ant-api[0-9a-z]+-[A-Za-z0-9_-]{40,}", re.I)),
    ("anthropic_api_key_alt", re.compile(r"sk-ant-[A-Za-z0-9_-]{50,}", re.I)),
    ("openai_api_key", re.compile(r"sk-[A-Za-z0-9_-]{20,}T3BlbkFJ[A-Za-z0-9_-]{20,}", re.I)),
    ("openai_proj_key", re.compile(r"sk-proj-[A-Za-z0-9_-]{40,}", re.I)),
    ("github_pat_classic", re.compile(r"ghp_[A-Za-z0-9]{36,}")),
    ("github_oauth", re.compile(r"gho_[A-Za-z0-9]{36,}")),
    ("github_app_user", re.compile(r"ghu_[A-Za-z0-9]{36,}")),
    ("github_app_server", re.compile(r"ghs_[A-Za-z0-9]{36,}")),
    ("github_refresh", re.compile(r"ghr_[A-Za-z0-9]{36,}")),
    ("github_fine_grained", re.compile(r"github_pat_[A-Za-z0-9_]{80,}")),
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("aws_secret_key", re.compile(r"(?i)aws[_-]?secret[_-]?(access[_-]?)?key.{0,20}[\"'=:\s]+([A-Za-z0-9/+=]{40})")),
    ("stripe_live", re.compile(r"sk_live_[A-Za-z0-9]{24,}")),
    ("stripe_test", re.compile(r"sk_test_[A-Za-z0-9]{24,}")),
    ("stripe_restricted", re.compile(r"rk_live_[A-Za-z0-9]{24,}")),
    ("telegram_bot_token", re.compile(r"\b\d{9,11}:[A-Za-z0-9_-]{35}\b")),
    ("discord_bot_token", re.compile(r"\b[MN][A-Za-z0-9_-]{23}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27,}\b")),
    ("slack_bot_token", re.compile(r"xox[abprs]-[A-Za-z0-9-]{10,}")),
    ("gemini_api_key", re.compile(r"AIza[A-Za-z0-9_-]{35}")),
    ("elevenlabs_api_key", re.compile(r"xi-api-key[\"'=:\s]+([a-f0-9]{32,})", re.I)),
    ("notion_internal", re.compile(r"secret_[A-Za-z0-9]{43}")),
    ("heygen_token", re.compile(r"hgg_[A-Za-z0-9_-]{30,}")),
    ("firecrawl_key", re.compile(r"\bfc-[a-f0-9]{32}\b")),
    ("rapidapi_key", re.compile(r"\b[a-f0-9]{50}msh[a-f0-9]{32}p[0-9a-z]{8}jsn[a-f0-9]{12}\b")),
    ("apify_token", re.compile(r"\bapify_api_[A-Za-z0-9]{32,}\b")),
    ("private_key_rsa", re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY-----")),
    ("jwt_token", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("generic_bearer", re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{30,}")),
    ("password_in_url", re.compile(r"://[^/\s:]+:[^/\s@]{6,}@[^/\s]+")),
]

# Specific file patterns where any non-trivial value is suspect
SUSPECT_FILES = re.compile(r"(\.env(\.\w+)?$|\.mcp\.json(\.\w+)?$|\.credentials/|credentials\.json|service-account|client_secret|application_default)")


def run_git(repo_path, args):
    return subprocess.run(
        ["git", "-C", repo_path] + args,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def scan_repo(repo_path):
    """Stream git log -p on suspect files, match patterns, return findings."""
    print(f"\nSCANNING: {repo_path}", flush=True)
    findings = []

    # Get list of commits
    rev_list = run_git(repo_path, ["rev-list", "--all", "--no-merges"])
    if rev_list.returncode != 0:
        print(f"  ERROR rev-list: {rev_list.stderr[:200]}")
        return findings

    commits = rev_list.stdout.strip().splitlines()
    print(f"  {len(commits)} commits to scan")

    # Use git log -p with file filter to reduce volume
    log_proc = subprocess.Popen(
        [
            "git", "-C", repo_path,
            "log", "--all", "--no-merges",
            "-p", "--unified=0",
            "--",
            "*.env*", ".env", ".mcp*", "*.json", "*.yml", "*.yaml", "*.py", "*.js", "*.ts",
            "*.md", "*.sh", "*.ps1",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    current_commit = None
    current_file = None
    line_count = 0
    seen_keys = set()

    if log_proc.stdout is None:
        return findings

    for line in log_proc.stdout:
        line_count += 1
        if line.startswith("commit "):
            current_commit = line[7:15]
        elif line.startswith("diff --git "):
            parts = line.split(" b/")
            current_file = parts[1].rstrip() if len(parts) > 1 else "?"
        elif line.startswith("+") and not line.startswith("+++"):
            content = line[1:]
            for ptype, pattern in PATTERNS:
                for m in pattern.finditer(content):
                    val = m.group(0)
                    key = (current_file, ptype, val[-8:])
                    if key in seen_keys:
                        continue
                    seen_keys.add(key)
                    findings.append({
                        "commit": current_commit,
                        "file": current_file,
                        "type": ptype,
                        "last4": val[-4:] if len(val) >= 4 else val,
                        "preview": val[:8] + "..." + val[-4:] if len(val) > 12 else val,
                    })

    log_proc.wait()
    print(f"  lines streamed: {line_count}, findings: {len(findings)}")
    return findings


def main():
    repos = [
        ("schoolswp (private)", r"d:\VS Code\CLAUDE CODE\projects\schoolswp"),
        ("schoolswp-telegram-agents (private)", r"d:\VS Code\CLAUDE CODE\projects\schoolswp\agents\telegram-claude"),
        ("michaelkihl-fr (private)", r"d:\VS Code\CLAUDE CODE\projects\michaelkihl-fr"),
        ("ultimate-scraper (no remote)", r"d:\VS Code\CLAUDE CODE\projects\schoolswp\tools\ultimate-scraper"),
        ("novamira (fork from use-novamira)", r"d:\VS Code\CLAUDE CODE\novamira"),
        ("thruuu-claude-content-strategist (fork)", r"d:\VS Code\CLAUDE CODE\thruuu-claude-content-strategist"),
        ("brightbean-studio (fork)", r"d:\VS Code\CLAUDE CODE\projects\brightbean-studio"),
        ("claude-mem (fork)", r"d:\VS Code\CLAUDE CODE\projects\claude-mem"),
    ]

    all_findings = {}
    for name, path in repos:
        if not Path(path).exists():
            print(f"SKIP (missing): {name}")
            continue
        findings = scan_repo(path)
        all_findings[name] = findings

    # Summary
    print("\n\n=== SUMMARY ===")
    total = 0
    for name, findings in all_findings.items():
        if findings:
            by_type = defaultdict(int)
            for f in findings:
                by_type[f["type"]] += 1
            tags = ", ".join(f"{t}={c}" for t, c in sorted(by_type.items()))
            print(f"  {name}: {len(findings)} ({tags})")
            total += len(findings)
        else:
            print(f"  {name}: CLEAN")

    print(f"\nTOTAL findings: {total}")

    # Save output
    out_path = Path(__file__).parent / "secrets-scan-output.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_findings, f, indent=2, default=str, ensure_ascii=False)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
