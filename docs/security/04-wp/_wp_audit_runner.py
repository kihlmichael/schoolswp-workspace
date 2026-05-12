"""Runner that loads WP_API_* from .claude/settings.local.json without echoing values.

The Novamira MCP server block in settings.local.json contains:
    "novamira-schoolswp-com": {
        "env": { "WP_API_URL": "...", "WP_API_USERNAME": "...", "WP_API_PASSWORD": "..." }
    }

We extract those keys, write them to a temp .env file scoped to this process,
then invoke _wp_audit.py via subprocess so the values never appear in tool output.
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

if len(sys.argv) < 3:
    print("usage: python _wp_audit_runner.py <settings.local.json> <mcp_server_key> [output_json]")
    sys.exit(1)

settings_path = Path(sys.argv[1]).resolve()
mcp_key = sys.argv[2]
out_json = sys.argv[3] if len(sys.argv) > 3 else "wp-audit-output.json"

with open(settings_path, "r", encoding="utf-8") as f:
    settings = json.load(f)

if mcp_key == "top-level":
    env_block = settings.get("env", {})
else:
    mcp_servers = settings.get("mcpServers", {})
    if mcp_key not in mcp_servers:
        print(f"ERROR: MCP server key not found: {mcp_key}")
        print(f"Available keys: {sorted(mcp_servers.keys())}")
        sys.exit(2)
    env_block = mcp_servers[mcp_key].get("env", {})

wp_keys = {k: v for k, v in env_block.items() if k.startswith("WP_") or k.startswith("WORDPRESS_")}

if not wp_keys:
    print(f"ERROR: no WP_* keys in env block of {mcp_key}")
    print(f"Available keys: {sorted(env_block.keys())}")
    sys.exit(3)

print(f"loaded {len(wp_keys)} WP_* keys from {mcp_key}: {sorted(wp_keys.keys())}")

api_url = wp_keys.get("WP_API_URL", "")
if not api_url:
    print("ERROR: WP_API_URL is missing")
    sys.exit(4)

if api_url.endswith("/wp-json/") or api_url.endswith("/wp-json"):
    api_url = api_url.rstrip("/").rsplit("/wp-json", 1)[0]
elif "/wp-json/" in api_url:
    api_url = api_url.split("/wp-json/", 1)[0]

print(f"audit base URL (derived): {api_url}")

with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False, encoding="utf-8") as tmp:
    for k, v in wp_keys.items():
        tmp.write(f"{k}={v}\n")
    tmp_path = tmp.name

try:
    audit_script = Path(__file__).parent / "_wp_audit.py"
    result = subprocess.run(
        [sys.executable, str(audit_script), tmp_path, api_url, out_json],
        check=False,
        capture_output=True,
        text=True,
    )
    print("STDOUT:")
    print(result.stdout)
    if result.returncode != 0:
        print("STDERR:")
        print(result.stderr)
        sys.exit(result.returncode)
finally:
    try:
        os.unlink(tmp_path)
    except Exception as e:
        print(f"WARN: temp file not removed ({tmp_path}): {e}")
