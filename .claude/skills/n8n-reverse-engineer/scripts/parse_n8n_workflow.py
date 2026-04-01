"""
parse_n8n_workflow.py — Parseur automatique d'exports JSON n8n.

Extrait d'un workflow n8n exporté :
- inventaire des noeuds (type, nom, disabled, credentials)
- graphe de connexions
- expressions n8n trouvées
- prompts IA (OpenAI, Anthropic, etc.)
- code embarqué (noeuds Code)
- appels HTTP (endpoints, méthodes, headers)
- credentials référencés
- sub-workflows référencés (Execute Workflow)

Usage:
    python parse_n8n_workflow.py workflow.json
    python parse_n8n_workflow.py workflow.json --output report.md
    python parse_n8n_workflow.py folder/ --all
"""

import json
import re
import sys
from pathlib import Path


def load_workflow(path: str) -> dict:
    """Charge un fichier JSON n8n."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def extract_expressions(obj, path="") -> list[dict]:
    """Trouve toutes les expressions n8n (={{ ... }}) dans un objet."""
    results = []
    if isinstance(obj, str):
        matches = re.findall(r"=\{\{(.+?)\}\}", obj, re.DOTALL)
        for m in matches:
            results.append({"path": path, "expression": m.strip()})
    elif isinstance(obj, dict):
        for k, v in obj.items():
            results.extend(extract_expressions(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            results.extend(extract_expressions(v, f"{path}[{i}]"))
    return results


def extract_prompts(node: dict) -> list[dict]:
    """Extrait les prompts IA des noeuds OpenAI, Anthropic, LangChain, etc."""
    prompts = []
    node_type = node.get("type", "")
    params = node.get("parameters", {})

    # OpenAI Chat / ChatOpenAI
    if "openai" in node_type.lower() or "chatOpenAi" in node_type:
        # System message
        if "options" in params:
            sys_msg = params["options"].get("systemMessage", "")
            if sys_msg:
                prompts.append({"type": "system", "text": sys_msg, "source": "options.systemMessage"})
        # Messages array
        if "messages" in params:
            msgs = params["messages"]
            if isinstance(msgs, dict) and "values" in msgs:
                for msg in msgs["values"]:
                    role = msg.get("role", "user")
                    content = msg.get("content", "")
                    if content:
                        prompts.append({"type": role, "text": content, "source": "messages.values"})
        # Direct prompt field
        if "prompt" in params:
            p = params["prompt"]
            if isinstance(p, dict) and "values" in p:
                for val in p["values"]:
                    prompts.append({"type": "user", "text": val.get("content", ""), "source": "prompt.values"})
            elif isinstance(p, str) and p:
                prompts.append({"type": "user", "text": p, "source": "prompt"})
        # Text field
        if "text" in params and isinstance(params["text"], str):
            prompts.append({"type": "user", "text": params["text"], "source": "text"})

    # Anthropic
    if "anthropic" in node_type.lower():
        for field in ["systemMessage", "system"]:
            val = params.get(field, "") or params.get("options", {}).get(field, "")
            if val:
                prompts.append({"type": "system", "text": val, "source": field})
        if "messages" in params:
            msgs = params["messages"]
            if isinstance(msgs, list):
                for msg in msgs:
                    prompts.append(
                        {"type": msg.get("role", "user"), "text": msg.get("content", ""), "source": "messages"}
                    )

    # Generic: chercher dans tous les champs de type texte long
    if not prompts:
        for key in ["text", "prompt", "systemMessage", "userMessage", "content", "instructions"]:
            val = params.get(key, "")
            if isinstance(val, str) and len(val) > 50:
                prompts.append({"type": "unknown", "text": val, "source": key})

    return prompts


def extract_code(node: dict) -> dict | None:
    """Extrait le code des noeuds Code/Function."""
    params = node.get("parameters", {})
    # n8n Code node
    js_code = params.get("jsCode", "")
    py_code = params.get("pythonCode", "")
    # Legacy Function node
    func_code = params.get("functionCode", "")

    code = js_code or py_code or func_code
    if code:
        lang = "python" if py_code else "javascript"
        return {"language": lang, "code": code, "lines": code.count("\n") + 1}
    return None


def extract_http_details(node: dict) -> dict | None:
    """Extrait les détails des noeuds HTTP Request."""
    params = node.get("parameters", {})
    if node.get("type", "") not in [
        "n8n-nodes-base.httpRequest",
        "@n8n/n8n-nodes-langchain.httpRequest",
    ]:
        return None

    details = {
        "method": params.get("method", "GET"),
        "url": params.get("url", ""),
        "authentication": params.get("authentication", "none"),
    }

    # Headers
    headers = params.get("headerParameters", {})
    if isinstance(headers, dict) and "parameters" in headers:
        details["headers"] = headers["parameters"]

    # Body
    body = params.get("body", "")
    body_params = params.get("bodyParameters", {})
    if body:
        details["body"] = body
    if body_params:
        details["bodyParameters"] = body_params

    # JSON body
    json_body = params.get("jsonBody", "")
    if json_body:
        details["jsonBody"] = json_body

    # Send body
    details["sendBody"] = params.get("sendBody", False)
    details["contentType"] = params.get("contentType", "")

    return details


def analyze_workflow(data: dict) -> dict:
    """Analyse complète d'un workflow n8n."""
    # Gère les deux formats : export direct ou wrappé dans un tableau
    if isinstance(data, list):
        data = data[0] if data else {}

    nodes = data.get("nodes", [])
    connections = data.get("connections", {})
    wf_name = data.get("name", "Unknown")
    wf_id = data.get("id", "N/A")
    wf_active = data.get("active", False)
    wf_tags = [t.get("name", "") for t in data.get("tags", [])]

    report = {
        "name": wf_name,
        "id": wf_id,
        "active": wf_active,
        "tags": wf_tags,
        "node_count": len(nodes),
        "nodes": [],
        "connections_summary": [],
        "credentials_referenced": [],
        "expressions": [],
        "prompts": [],
        "code_nodes": [],
        "http_calls": [],
        "sub_workflows": [],
        "triggers": [],
        "disabled_nodes": [],
    }

    seen_credentials = set()

    for node in nodes:
        name = node.get("name", "")
        ntype = node.get("type", "")
        disabled = node.get("disabled", False)
        params = node.get("parameters", {})

        node_info = {
            "name": name,
            "type": ntype,
            "disabled": disabled,
            "position": node.get("position", []),
        }
        report["nodes"].append(node_info)

        if disabled:
            report["disabled_nodes"].append(name)

        # Triggers
        if "trigger" in ntype.lower() or "webhook" in ntype.lower():
            report["triggers"].append({"name": name, "type": ntype, "params_keys": list(params.keys())})

        # Credentials
        creds = node.get("credentials", {})
        for cred_type, cred_data in creds.items():
            cred_name = cred_data.get("name", cred_data.get("id", "unknown"))
            key = f"{cred_type}:{cred_name}"
            if key not in seen_credentials:
                seen_credentials.add(key)
                report["credentials_referenced"].append(
                    {
                        "type": cred_type,
                        "name": cred_name,
                        "used_by": name,
                    }
                )

        # Expressions
        exprs = extract_expressions(params, f"nodes['{name}'].parameters")
        report["expressions"].extend(exprs)

        # Prompts
        found_prompts = extract_prompts(node)
        for p in found_prompts:
            p["node"] = name
        report["prompts"].extend(found_prompts)

        # Code
        code = extract_code(node)
        if code:
            code["node"] = name
            report["code_nodes"].append(code)

        # HTTP
        http = extract_http_details(node)
        if http:
            http["node"] = name
            report["http_calls"].append(http)

        # Sub-workflows
        if "executeWorkflow" in ntype.lower() or "execute workflow" in ntype.lower():
            wf_ref = params.get("workflowId", params.get("workflow", {}).get("value", ""))
            report["sub_workflows"].append({"node": name, "workflow_id": wf_ref})

    # Connections
    for source_node, outputs in connections.items():
        if isinstance(outputs, dict):
            for output_key, targets in outputs.items():
                if isinstance(targets, list):
                    for target_group in targets:
                        if isinstance(target_group, list):
                            for conn in target_group:
                                target = conn.get("node", "")
                                report["connections_summary"].append(f"{source_node} → {target}")
                        elif isinstance(target_group, dict):
                            target = target_group.get("node", "")
                            report["connections_summary"].append(f"{source_node} → {target}")

    return report


def format_markdown(report: dict, filepath: str) -> str:
    """Formate le rapport en Markdown."""
    lines = []
    lines.append(f"# Rapport d'extraction — {report['name']}")
    lines.append("")
    lines.append(f"**Fichier source** : `{filepath}`")
    lines.append(f"**ID workflow** : `{report['id']}`")
    lines.append(f"**Actif** : {'oui' if report['active'] else 'non'}")
    lines.append(f"**Tags** : {', '.join(report['tags']) or 'aucun'}")
    lines.append(f"**Nombre de noeuds** : {report['node_count']}")
    lines.append("")

    # Triggers
    lines.append("## Triggers")
    if report["triggers"]:
        for t in report["triggers"]:
            lines.append(f"- **{t['name']}** (`{t['type']}`)")
    else:
        lines.append("- Aucun trigger detecte")
    lines.append("")

    # Noeuds
    lines.append("## Noeuds (ordre du JSON)")
    lines.append("")
    lines.append("| # | Nom | Type | Disabled |")
    lines.append("|---|-----|------|----------|")
    for i, n in enumerate(report["nodes"], 1):
        dis = "oui" if n["disabled"] else ""
        lines.append(f"| {i} | {n['name']} | `{n['type']}` | {dis} |")
    lines.append("")

    # Connexions
    lines.append("## Connexions")
    for c in report["connections_summary"]:
        lines.append(f"- {c}")
    lines.append("")

    # Credentials
    lines.append("## Credentials references")
    if report["credentials_referenced"]:
        lines.append("")
        lines.append("| Type | Nom | Utilise par |")
        lines.append("|------|-----|------------|")
        for c in report["credentials_referenced"]:
            lines.append(f"| `{c['type']}` | {c['name']} | {c['used_by']} |")
    else:
        lines.append("- Aucun credential reference")
    lines.append("")

    # Expressions
    lines.append(f"## Expressions n8n ({len(report['expressions'])} trouvees)")
    if report["expressions"]:
        for e in report["expressions"]:
            lines.append(f"- `{e['path']}` : `={{{{ {e['expression']} }}}}`")
    lines.append("")

    # Prompts
    lines.append(f"## Prompts IA ({len(report['prompts'])} trouves)")
    for i, p in enumerate(report["prompts"], 1):
        lines.append(f"### Prompt {i} — {p['node']} ({p['type']})")
        lines.append(f"Source : `{p['source']}`")
        lines.append("```")
        lines.append(p["text"][:2000])
        if len(p["text"]) > 2000:
            lines.append(f"\n[... tronque, {len(p['text'])} caracteres au total]")
        lines.append("```")
        lines.append("")

    # Code
    lines.append(f"## Code embarque ({len(report['code_nodes'])} noeuds)")
    for c in report["code_nodes"]:
        lines.append(f"### {c['node']} ({c['language']}, {c['lines']} lignes)")
        lines.append(f"```{c['language']}")
        lines.append(c["code"])
        lines.append("```")
        lines.append("")

    # HTTP
    lines.append(f"## Appels HTTP ({len(report['http_calls'])} trouves)")
    if report["http_calls"]:
        for h in report["http_calls"]:
            lines.append(f"### {h['node']}")
            lines.append(f"- **Methode** : `{h['method']}`")
            lines.append(f"- **URL** : `{h['url']}`")
            lines.append(f"- **Auth** : `{h['authentication']}`")
            if h.get("headers"):
                lines.append(f"- **Headers** : `{json.dumps(h['headers'], ensure_ascii=False)}`")
            if h.get("jsonBody"):
                lines.append("- **Body JSON** :")
                lines.append(f"```json\n{h['jsonBody']}\n```")
            lines.append("")

    # Sub-workflows
    lines.append(f"## Sub-workflows ({len(report['sub_workflows'])} references)")
    for s in report["sub_workflows"]:
        lines.append(f"- **{s['node']}** → workflow ID `{s['workflow_id']}`")
    lines.append("")

    # Noeuds desactives
    if report["disabled_nodes"]:
        lines.append(f"## Noeuds desactives ({len(report['disabled_nodes'])})")
        for d in report["disabled_nodes"]:
            lines.append(f"- {d}")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_n8n_workflow.py <fichier.json> [--output report.md] [--all]")
        sys.exit(1)

    target = Path(sys.argv[1])
    output_path = None

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    files = []
    if target.is_dir():
        files = sorted(target.glob("*.json"))
    elif target.is_file():
        files = [target]
    else:
        print(f"Erreur : {target} n'existe pas")
        sys.exit(1)

    all_reports = []
    for f in files:
        try:
            data = load_workflow(str(f))
            report = analyze_workflow(data)
            md = format_markdown(report, str(f))
            all_reports.append(md)
            print(
                f"[OK] {f.name} — {report['node_count']} noeuds, {len(report['prompts'])} prompts, {len(report['expressions'])} expressions"
            )
        except (json.JSONDecodeError, KeyError) as e:
            print(f"[ERREUR] {f.name} — {e}")

    if all_reports:
        full_report = "\n\n---\n\n".join(all_reports)
        if output_path:
            Path(output_path).write_text(full_report, encoding="utf-8")
            print(f"\nRapport sauvegarde : {output_path}")
        else:
            print("\n" + full_report)


if __name__ == "__main__":
    main()
