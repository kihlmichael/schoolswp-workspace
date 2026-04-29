"""PreToolUse hook: block secret-leak patterns in .mcp.json.

Bloque toute ecriture sur .mcp.json qui reintroduit ${VAR} dans args ou
dans headers (non-http). Ces patterns sont substitues par Claude Code au
moment du `claude mcp list`, ce qui fait fuiter les secrets dans le JSONL
transcript (incidents 2026-04-21 + 2026-04-29).

Pattern canonique : passer par un launcher .mjs dans tools/mcp-servers/
qui lit les secrets depuis settings.local.json et spawn le binaire avec
le secret en arg cote child process (invisible a mcp list).

Exit 0 = allow, Exit 2 = block (stderr message shown to Claude)
"""

from __future__ import annotations

import json
import re
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_name = payload.get("tool_name", "")
    if tool_name not in ("Edit", "Write"):
        return 0

    tool_input = payload.get("tool_input", {}) or {}
    file_path = (tool_input.get("file_path") or "").replace("\\", "/")

    if not file_path.endswith("/.mcp.json"):
        return 0

    # Edit: new_string (partial). Write: content (full).
    content = tool_input.get("content") or tool_input.get("new_string") or ""

    var_pattern = re.compile(r"\$\{[A-Z][A-Z0-9_]*\}")
    violations: list[str] = []

    try:
        cfg = json.loads(content)
        servers = cfg.get("mcpServers", {}) if isinstance(cfg, dict) else {}
        for name, entry in servers.items():
            if not isinstance(entry, dict):
                continue
            for arg in entry.get("args", []) or []:
                if isinstance(arg, str) and var_pattern.search(arg):
                    m = var_pattern.search(arg)
                    violations.append(f"{name}.args contains {m.group(0)}")
            headers = entry.get("headers", {}) or {}
            if isinstance(headers, dict):
                is_http = entry.get("type") == "http"
                if not is_http:
                    for hname, hval in headers.items():
                        if isinstance(hval, str) and var_pattern.search(hval):
                            m = var_pattern.search(hval)
                            violations.append(f"{name}.headers.{hname} contains {m.group(0)}")
    except json.JSONDecodeError:
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if not var_pattern.search(line):
                continue
            ctx = " ".join(lines[max(0, i - 3) : i + 1])
            if '"args"' in ctx or '"headers"' in ctx or "Authorization" in line:
                m = var_pattern.search(line)
                violations.append(f"line {i + 1}: {m.group(0)} near args/headers")

    if not violations:
        return 0

    msg_lines = [
        "BLOCKED: .mcp.json reintroduces ${VAR} substitution in args/headers.",
        "",
        "These patterns are resolved at `claude mcp list` time and the resolved",
        "secret appears in cleartext in the JSONL transcript (incidents 2026-04-21",
        "+ 2026-04-29).",
        "",
        "Violations:",
    ]
    msg_lines.extend(violations)
    msg_lines.extend(
        [
            "",
            "Canonical fix: route the MCP through a launcher .mjs in",
            "tools/mcp-servers/ that reads the secret from",
            ".claude/settings.local.json and spawns the real binary with the",
            "secret as an arg on the child process (invisible to mcp list).",
            "",
            "Reference launchers:",
            "- tools/mcp-servers/_launch-fluent.mjs (5 Fluent ecosystem)",
            "- tools/mcp-servers/_launch-rapidapi.mjs (4 RapidAPI hosts)",
            "- tools/mcp-servers/_launch-discord.mjs (mcp-discord)",
        ]
    )
    print("\n".join(msg_lines), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
