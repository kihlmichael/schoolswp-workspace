import json

from packages.memory.store import get_recent_decisions, save_decision

# ── Tool definitions ───────────────────────────────────────────────────────────

MEMORY_TOOLS = [
    {
        "name": "recall_decisions",
        "description": (
            "Rappelle les N dernières décisions prises par cet agent dans des runs précédents. "
            "Utiliser pour éviter de répéter des erreurs ou pour s'appuyer sur l'expérience passée."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de décisions à rappeler (défaut: 3, max: 10)",
                    "default": 3,
                }
            },
            "required": [],
        },
    },
    {
        "name": "save_decision",
        "description": (
            "Persiste une décision importante en mémoire pour les runs futurs. "
            "Utiliser pour les décisions structurantes (choix d'architecture, patterns, warnings récurrents)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "decision": {
                    "type": "string",
                    "description": "La décision prise (concise, actionnable)",
                },
                "reasoning": {
                    "type": "string",
                    "description": "Pourquoi cette décision a été prise",
                },
                "confidence": {
                    "type": "number",
                    "description": "Niveau de confiance 0.0-1.0",
                },
            },
            "required": ["decision", "reasoning", "confidence"],
        },
    },
]


# ── Tool handlers ──────────────────────────────────────────────────────────────

async def handle_memory_tool(
    tool_name: str, tool_input: dict, agent: str, run_id: str
) -> str:
    if tool_name == "recall_decisions":
        limit = min(int(tool_input.get("limit", 3)), 10)
        decisions = await get_recent_decisions(agent, limit)
        if not decisions:
            return "[NO PAST DECISIONS]"
        return json.dumps(decisions, ensure_ascii=False, indent=2)

    if tool_name == "save_decision":
        await save_decision(
            run_id=run_id,
            agent=agent,
            decision=tool_input["decision"],
            reasoning=tool_input["reasoning"],
            confidence=float(tool_input["confidence"]),
        )
        return "[DECISION SAVED]"

    return f"[UNKNOWN TOOL] {tool_name}"
