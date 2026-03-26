import os
from pathlib import Path

DECISIONS_DIR = Path(os.getenv("DECISIONS_DIR", "./data/decisions"))

# ── Tool definitions (format Anthropic Tool Use) ──────────────────────────────

# list_files retiré des outils par défaut : il pousse les agents à lire
# les fichiers des runs précédents et épuise leurs tours sans produire d'output.
# write_file retiré des outils par défaut : le bloc tool_use embarque le contenu
# markdown dans la RÉPONSE du modèle → consomme le budget max_tokens et provoque
# stop_reason=max_tokens avant que l'agent produise son JSON final.
# Utiliser save_decision (mémoire SQLite) pour la persistance à la place.
FILESYSTEM_TOOLS = [
    {
        "name": "read_file",
        "description": (
            "Lit un fichier spécifique dans le répertoire de décisions. "
            "Utiliser uniquement si tu connais déjà le chemin exact."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Chemin relatif sous data/decisions/ (ex: 'abc123/front.md')",
                }
            },
            "required": ["path"],
        },
    },
]


# ── Tool handlers ──────────────────────────────────────────────────────────────

async def handle_filesystem_tool(tool_name: str, tool_input: dict) -> str:
    if tool_name == "read_file":
        path = DECISIONS_DIR / tool_input["path"]
        if path.exists() and path.is_file():
            return path.read_text(encoding="utf-8")
        return f"[NOT FOUND] {tool_input['path']}"

    if tool_name == "write_file":
        path = DECISIONS_DIR / tool_input["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(tool_input["content"], encoding="utf-8")
        return f"[WRITTEN] {tool_input['path']}"

    if tool_name == "list_files":
        run_id = tool_input.get("run_id", "")
        base = DECISIONS_DIR / run_id if run_id else DECISIONS_DIR
        if base.exists():
            files = [str(f.relative_to(DECISIONS_DIR)) for f in base.rglob("*") if f.is_file()]
            return "\n".join(files) if files else "[EMPTY]"
        return "[DIR NOT FOUND]"

    return f"[UNKNOWN TOOL] {tool_name}"
