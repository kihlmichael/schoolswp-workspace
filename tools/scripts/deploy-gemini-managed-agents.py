#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
deploy-gemini-managed-agents.py -- Deploy local schoolsWP sub-agents (.claude/agents/*.md) as Gemini Managed Agents.
Usage:
  python deploy-gemini-managed-agents.py --dry-run
  python deploy-gemini-managed-agents.py --apply
  python deploy-gemini-managed-agents.py --list
  python deploy-gemini-managed-agents.py --agent pulse --apply
  python deploy-gemini-managed-agents.py --delete data-analyst --apply
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

# Ensure UTF-8 output on Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Configuration
API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
BASE_AGENT = "antigravity-preview-05-2026"
AGENTS_DIR = r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\agents"
PROJECT_ROOT = r"D:\VS Code\CLAUDE CODE\projects\schoolswp"

# Load API Key from local settings or environment
def resolve_api_key():
    # 1. Try settings.local.json first (preferred active secret storage)
    settings_path = os.path.join(PROJECT_ROOT, ".claude", "settings.local.json")
    if os.path.exists(settings_path):
        try:
            with open(settings_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                key = data.get("env", {}).get("GEMINI_API_KEY")
                if key:
                    return key
        except Exception:
            pass

    # 2. Try .env file fallback
    env_path = os.path.join(PROJECT_ROOT, ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k == "GEMINI_API_KEY" and v:
                        return v
        except Exception:
            pass

    # 3. Fallback to OS environment
    return os.environ.get("GEMINI_API_KEY")

GEMINI_API_KEY = resolve_api_key()

def get_headers():
    if not GEMINI_API_KEY:
        print("[!] ERROR: GEMINI_API_KEY is not defined in environment or .env file.")
        sys.exit(1)
    return {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY,
        "Api-Revision": "2026-05-20"
    }

def make_request(url, method="GET", data=None):
    headers = get_headers()
    req_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as res:
            if res.status in (200, 201):
                return json.loads(res.read().decode("utf-8")), None
            elif res.status == 204:
                return {}, None
            return None, f"HTTP Error {res.status}"
    except urllib.error.HTTPError as e:
        try:
            error_body = e.read().decode("utf-8")
            error_json = json.loads(error_body)
            error_msg = error_json.get("error", {}).get("message", error_body)
        except Exception:
            error_msg = e.reason
        return None, error_msg
    except Exception as e:
        return None, str(e)

def parse_yaml_frontmatter(content):
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    fm_data = {"name": "", "description": "", "model": ""}
    if not fm_match:
        return fm_data, content
    fm = fm_match.group(1)
    
    # Extract name
    nm = re.search(r"^name:\s*(.+)", fm, re.MULTILINE)
    if nm:
        fm_data["name"] = nm.group(1).strip().strip('"').strip("'")
        
    # Extract description
    dm = re.search(r"^description:\s*[|>]?[+-]?\s*([\s\S]+?)(?=\n\w|\Z)", fm, re.MULTILINE)
    if dm:
        desc = re.sub(r"\s+", " ", dm.group(1).strip())
        if (desc.startswith('"') and desc.endswith('"')) or (desc.startswith("'") and desc.endswith("'")):
            desc = desc[1:-1].strip()
        fm_data["description"] = desc
        
    # Extract model
    mm = re.search(r"^model:\s*(.+)", fm, re.MULTILINE)
    if mm:
        fm_data["model"] = mm.group(1).strip().strip('"').strip("'")

    # Clean the original frontmatter out of content
    main_content = re.sub(r"^---\s*\n.*?\n---\s*\n?", "", content, flags=re.DOTALL)
    return fm_data, main_content.strip()

def scan_local_agents(filter_agent=None):
    agents = []
    if not os.path.exists(AGENTS_DIR):
        print(f"[!] ERROR: Agents directory not found at {AGENTS_DIR}")
        sys.exit(1)
        
    for filename in sorted(os.listdir(AGENTS_DIR)):
        if not filename.endswith(".md") or filename == "INDEX.md":
            continue
            
        agent_id = filename[:-3] # drop .md
        if filter_agent and agent_id.lower() != filter_agent.lower():
            continue
            
        filepath = os.path.join(AGENTS_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"[!] Warning: Failed to read {filename}: {e}")
            continue
            
        # Strip UTF-8 BOM if present
        if content.startswith("﻿"):
            content = content.lstrip("﻿")
            
        fm_data, system_instruction = parse_yaml_frontmatter(content)
        name = fm_data["name"] or agent_id
        
        agents.append({
            "id": agent_id,
            "name": name,
            "description": fm_data["description"] or f"schoolsWP specialized agent: {name}",
            "system_instruction": system_instruction,
        })
    return agents

def get_remote_agent(agent_id):
    url = f"{API_BASE_URL}/agents/{agent_id}"
    res, err = make_request(url, "GET")
    if err:
        if "not found" in err.lower():
            return None, "NOT_FOUND"
        return None, err
    return res, None

def delete_remote_agent(agent_id):
    url = f"{API_BASE_URL}/agents/{agent_id}"
    _, err = make_request(url, "DELETE")
    return err

def create_remote_agent(agent_id, description, system_instruction):
    url = f"{API_BASE_URL}/agents"
    payload = {
        "id": agent_id,
        "base_agent": BASE_AGENT,
        "description": description,
        "system_instruction": system_instruction
    }
    res, err = make_request(url, "POST", payload)
    return res, err

def list_remote_agents():
    url = f"{API_BASE_URL}/agents"
    res, err = make_request(url, "GET")
    if err:
        return None, err
    return res.get("agents", []), None

def main():
    parser = argparse.ArgumentParser(description="Deploy local agents to Gemini API.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Preview changes without executing")
    group.add_argument("--apply", action="store_true", help="Execute deployment / actions")
    group.add_argument("--list", action="store_true", help="List registered managed agents on the account")
    
    parser.add_argument("--agent", type=str, help="Filter action to a single agent ID (ex: --agent pulse)")
    parser.add_argument("--delete", type=str, help="Delete a specific agent ID (requires --apply)")
    
    args = parser.parse_args()
    
    if args.list:
        print("\n=== Fetching Gemini Managed Agents ===")
        remote_agents, err = list_remote_agents()
        if err:
            print(f"[!] Failed to list remote agents: {err}")
            sys.exit(1)
        if not remote_agents:
            print("No managed agents found on this account.")
        else:
            print(f"Found {len(remote_agents)} managed agent(s):")
            for a in remote_agents:
                agent_id = a.get('id')
                print(f"  - {agent_id} : {a.get('description')}")
                
                # Fetch full details for accurate system_instruction & base_agent
                details, det_err = get_remote_agent(agent_id)
                if not det_err and details:
                    print(f"    Base Agent: {details.get('base_agent')}")
                    print(f"    System Instruction Length: {len(details.get('system_instruction', ''))} chars\n")
                else:
                    print(f"    Base Agent: {a.get('base_agent')}")
                    print(f"    System Instruction Length: {len(a.get('system_instruction', ''))} chars\n")
        return
        
    if args.delete:
        if not args.apply:
            print("[!] ERROR: --delete requires --apply to execute.")
            sys.exit(1)
        print(f"\n=== Deleting Agent '{args.delete}' ===")
        err = delete_remote_agent(args.delete)
        if err:
            print(f"[!] Failed to delete agent '{args.delete}': {err}")
            sys.exit(1)
        print(f"[+] Successfully deleted agent '{args.delete}' on Gemini API.")
        return

    local_agents = scan_local_agents(args.agent)
    if not local_agents:
        if args.agent:
            print(f"[!] No local agent found matching ID '{args.agent}'")
        else:
            print("[!] No local agents found to deploy.")
        sys.exit(1)

    print(f"\n=== schoolsWP Gemini Managed Agents Deployment Pipeline ===")
    print(f"Found {len(local_agents)} local agent(s) to process.\n")

    for agent in local_agents:
        print("-" * 60)
        print(f"Agent ID    : {agent['id']}")
        print(f"Name        : {agent['name']}")
        print(f"Description : {agent['description']}")
        print(f"System Inst : {len(agent['system_instruction'])} characters")
        
        # Check remote status
        if args.dry_run:
            print("[DRY-RUN] Checking status on Gemini API...")
            remote, err = get_remote_agent(agent['id'])
            if err == "NOT_FOUND":
                print("Remote Status: NOT REGISTERED (Will be CREATED)")
            elif err:
                print(f"Remote Status: UNKNOWN (API Error: {err})")
            else:
                print("Remote Status: REGISTERED (Will be RE-DEPLOYED via Delete + Create)")
            print(f"[DRY-RUN] Would submit JSON payload to {API_BASE_URL}/agents:")
            preview = {
                "id": agent['id'],
                "base_agent": BASE_AGENT,
                "description": agent['description'],
                "system_instruction": agent['system_instruction'][:120] + "..." if len(agent['system_instruction']) > 120 else agent['system_instruction']
            }
            print(json.dumps(preview, indent=2, ensure_ascii=False))
        else:
            # Active deploy
            print("Status: Querying remote server...")
            remote, err = get_remote_agent(agent['id'])
            if err and err != "NOT_FOUND":
                print(f"[!] Error querying remote agent '{agent['id']}': {err}")
                continue
                
            if remote:
                print("Status: Already registered. Deleting existing definition to re-deploy cleanly...")
                del_err = delete_remote_agent(agent['id'])
                if del_err:
                    print(f"[!] Failed to delete existing agent: {del_err}")
                    continue
                print("Status: Existing definition deleted.")
            else:
                print("Status: Not registered yet. Proceeding to creation.")
                
            print("Status: Registering Managed Agent...")
            _, create_err = create_remote_agent(agent['id'], agent['description'], agent['system_instruction'])
            if create_err:
                print(f"[!] Failed to register agent '{agent['id']}': {create_err}")
            else:
                print(f"[+] SUCCESS: Agent '{agent['id']}' successfully deployed on Gemini API!")
                
    print("\n" + "=" * 60)
    print("Deployment pipeline completed.")
    if args.dry_run:
        print("Dry-run only. No real modifications were made.")
    else:
        print("Changes applied to your Gemini API account.")
    print("=" * 60)

if __name__ == "__main__":
    main()
