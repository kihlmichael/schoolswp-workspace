import json
import os
import re

from anthropic import AsyncAnthropic

client = AsyncAnthropic()

# Mots-clés qui déclenchent systématiquement l'agent security,
# indépendamment de la décision Haiku (fiabilité insuffisante sur cet axe).
_SECURITY_KEYWORDS = re.compile(
    r"\b("
    r"auth(?:entication|orization|entifier)?|login|logout|sign[- ]?in|sign[- ]?up"
    r"|jwt|oauth|token|secret|api[- ]?key|password|credential"
    r"|cors|xss|csrf|injection|sqli|rce|vuln"
    r"|upload|file[- ]?upload|fichier"
    r"|permission|role|acl|rbac"
    r"|wordpress[- ]admin|wp[- ]?admin|application[- ]?password"
    r"|paiement|payment|stripe|checkout"
    r"|https?|ssl|tls|certificat"
    r")\b",
    re.IGNORECASE,
)

_ROUTING_SYSTEM = """Tu es un routeur d'agents LLM. Analyse la tâche et décide quels agents spécialisés appeler.

AGENTS DISPONIBLES :
- "front"    : composants UI, React, CSS, animations, UX, performance frontend, accessibilité
- "back"     : APIs REST/GraphQL, base de données, authentification, cache, queues, endpoints
- "seo"      : meta tags, schema.org, keywords, Core Web Vitals, sitemap, contenu SEO, canonicals
- "security" : OWASP Top 10, XSS/injection, auth JWT/OAuth2, secrets, CORS, WordPress hardening, API security

RÈGLES DE ROUTING :
1. Si la tâche concerne clairement UN seul domaine → agents = [ce domaine]
2. Si la tâche est cross-domain → agents = tous les domaines pertinents
3. Si incertain → broadcast : agents = ["front", "back", "seo"]
4. Inclure "security" si la tâche mentionne : auth, login, API publique, données utilisateurs, secrets, permissions, WordPress admin, paiement, upload de fichiers
5. Décompose la tâche en sous-tâches spécifiques pour chaque agent

RÉPONDS EN JSON STRICT (aucun texte en dehors) :
{
  "agents": ["front", "back", "seo", "security"],
  "subtasks": {
    "front": "<sous-tâche spécifique au frontend, ou null>",
    "back": "<sous-tâche spécifique au backend, ou null>",
    "seo": "<sous-tâche spécifique au SEO, ou null>",
    "security": "<sous-tâche spécifique à la sécurité, ou null>"
  },
  "reasoning": "<1 phrase expliquant le choix des agents>"
}"""


async def route(task: str) -> tuple[list[str], dict[str, str]]:
    """
    Utilise Haiku (rapide + économique) pour le routing.
    Retourne (agents_to_call, subtasks_dict).
    """
    model = os.getenv("MODEL_ROUTER", "claude-haiku-4-5-20251001")

    response = await client.messages.create(
        model=model,
        max_tokens=400,
        system=_ROUTING_SYSTEM,
        messages=[{"role": "user", "content": task}],
    )

    text = response.content[0].text if response.content else ""

    try:
        result = json.loads(text)
        _VALID = {"front", "back", "seo", "security"}
        agents = [a for a in result.get("agents", []) if a in _VALID]
        subtasks = result.get("subtasks", {})
        # Nettoyage : si subtask est null/None → utilise la tâche originale
        subtasks = {k: (v if v else task) for k, v in subtasks.items()}
        if not agents:
            raise ValueError("agents list vide")
    except (json.JSONDecodeError, ValueError):
        # Fallback : broadcast sans security (évite les faux positifs)
        agents = ["front", "back", "seo"]
        subtasks = {"front": task, "back": task, "seo": task}

    # Détection par mots-clés : Haiku ne route pas fiablement vers security.
    # On l'ajoute systématiquement si la tâche contient des signaux sécurité explicites.
    if "security" not in agents and _SECURITY_KEYWORDS.search(task):
        agents.append("security")
        subtasks["security"] = subtasks.get("back", task)  # sous-tâche = contexte back

    return agents, subtasks
