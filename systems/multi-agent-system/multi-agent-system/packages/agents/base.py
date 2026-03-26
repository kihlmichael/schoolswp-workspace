import json
import os
import re

from anthropic import AsyncAnthropic

from packages.tools.filesystem import FILESYSTEM_TOOLS, handle_filesystem_tool
from packages.tools.memory_tools import MEMORY_TOOLS, handle_memory_tool

client = AsyncAnthropic()

# Noms des tools qui vont vers le handler filesystem
_FS_TOOLS = {"read_file"}
# Noms des tools qui vont vers le handler mémoire
_MEM_TOOLS = {"recall_decisions", "save_decision"}

def _parse_json(text: str) -> dict | None:
    """
    Parse JSON depuis un texte qui peut contenir des blocs markdown.
    Stratégie : brut → bloc ```json (non-greedy) → dernier objet JSON valide.
    """
    # 1. JSON brut direct
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # 2. Tous les blocs ```json ... ``` ou ``` ... ``` (non-greedy + newlines obligatoires)
    #    Non-greedy s'arrête au premier ``` de fermeture — correct pour un seul bloc JSON.
    #    Si le modèle ajoute du texte après le bloc, ça ne pollue pas la capture.
    for match in re.finditer(r"```(?:json)?\s*\n([\s\S]*?)\n\s*```", text):
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            continue

    # 3. Dernier recours : scan des objets JSON dans le texte (du plus long au plus court)
    for match in re.finditer(r"\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}", text):
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            continue

    return None


_FALLBACK_OUTPUT = {
    "domain": "unknown",
    "confidence": 0.0,
    "recommendations": [],
    "warnings": ["Max tool-use iterations atteint sans output structuré"],
    "depends_on": [],
    "tool_calls_made": [],
}


class BaseAgent:
    """
    Agent de base avec boucle Tool Use.
    Hériter et définir : name, system_prompt, extra_tools.
    """

    name: str = "base"
    system_prompt: str = ""
    extra_tools: list = []

    def get_tools(self) -> list:
        return FILESYSTEM_TOOLS + MEMORY_TOOLS + self.extra_tools

    async def run(
        self,
        task: str,
        run_id: str,
        context: dict | None = None,
        token_budget: int | None = None,
    ) -> dict:
        max_tokens = token_budget or int(os.getenv("AGENT_TOKEN_BUDGET", 2000))
        model = os.getenv("MODEL_ORCHESTRATOR", "claude-sonnet-4-6")
        tools = self.get_tools()

        # Enrichit le prompt avec le contexte inter-agents si fourni
        task_content = task
        if context:
            ctx_str = json.dumps(context, ensure_ascii=False, indent=2)
            task_content = f"CONTEXTE DES AUTRES AGENTS:\n{ctx_str}\n\nTÂCHE:\n{task}"

        messages = [{"role": "user", "content": task_content}]
        tool_calls_made: list[str] = []

        # Boucle Tool Use — max 4 tours : recall (1) + write (1) + save (1) + output (1)
        for _ in range(4):
            # Après 2 tool calls : désactive les tools → force le modèle à produire du texte
            api_kwargs: dict = {
                "model": model,
                "max_tokens": max_tokens,
                "system": self.system_prompt,
                "messages": messages,
            }
            if len(tool_calls_made) < 2:
                api_kwargs["tools"] = tools

            response = await client.messages.create(**api_kwargs)

            if response.stop_reason == "end_turn":
                # Extrait le texte final
                text = next(
                    (b.text for b in response.content if hasattr(b, "text") and b.text),
                    "",
                )
                parsed = _parse_json(text)
                if parsed is not None:
                    parsed["tool_calls_made"] = tool_calls_made
                    return parsed
                # Dernier recours : wrap le texte brut
                return {
                    "domain": self.name,
                    "confidence": 0.5,
                    "recommendations": [text] if text else [],
                    "warnings": ["Output non JSON — parsing dégradé"],
                    "depends_on": [],
                    "tool_calls_made": tool_calls_made,
                }

            if response.stop_reason == "tool_use":
                tool_results = []

                for block in response.content:
                    if block.type != "tool_use":
                        continue

                    tool_calls_made.append(block.name)

                    if block.name in _FS_TOOLS:
                        result_str = await handle_filesystem_tool(block.name, block.input)
                    elif block.name in _MEM_TOOLS:
                        result_str = await handle_memory_tool(
                            block.name, block.input, self.name, run_id
                        )
                    else:
                        result_str = f"[UNHANDLED TOOL] {block.name}"

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result_str,
                    })

                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})

            elif response.stop_reason == "max_tokens":
                # Réponse tronquée : tenter d'extraire un JSON partiel du texte généré
                partial = next(
                    (b.text for b in response.content if hasattr(b, "text") and b.text), ""
                )
                parsed = _parse_json(partial)
                if parsed is not None:
                    parsed["tool_calls_made"] = tool_calls_made
                    parsed.setdefault("warnings", []).append("Réponse tronquée (max_tokens)")
                    return parsed
                # Pas de JSON récupérable : sortir proprement
                break

            else:
                break  # stop_reason inconnu → sort proprement

        return {**_FALLBACK_OUTPUT, "domain": self.name, "tool_calls_made": tool_calls_made}
