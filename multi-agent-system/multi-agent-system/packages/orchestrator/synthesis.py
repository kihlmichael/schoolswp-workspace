import json
import os
import re

from anthropic import AsyncAnthropic

client = AsyncAnthropic()

_SYNTHESIS_SYSTEM = """Tu es un senior tech lead. Tu reçois les outputs JSON de plusieurs agents spécialisés.

TA MISSION :
1. Identifier les recommendations dupliquées → ne garder qu'une seule (la plus précise)
2. Identifier les conflits entre agents → les signaler explicitement dans "conflicts"
3. Prioriser les actions par impact business (high/medium/low)
4. Extraire les insights qui concernent plusieurs domaines en même temps
5. Proposer les 3 prochaines actions immédiates

FORMAT DE RÉPONSE (JSON strict) :
{
  "summary": "<1-2 phrases résumant la situation globale>",
  "priority_actions": [
    {
      "action": "<action concrète>",
      "owner": "front|back|seo|cross",
      "priority": "high|medium|low",
      "rationale": "<pourquoi cette priorité>"
    }
  ],
  "conflicts": [
    "<description du conflit inter-agents avec les agents concernés>"
  ],
  "cross_domain_insights": [
    "<observation qui impacte plusieurs domaines simultanément>"
  ],
  "next_steps": [
    "<action immédiate #1>",
    "<action immédiate #2>",
    "<action immédiate #3>"
  ]
}

RÈGLES :
- Max 7 priority_actions
- Si un agent a confidence < 0.7 → signaler dans conflicts avec mention "low confidence"
- Les next_steps sont ordonnés par dépendances techniques (ex: back avant front si front dépend de back)
- IMPORTANT : réponds en JSON pur, SANS bloc markdown, SANS texte avant ou après"""


async def synthesize(agent_outputs: dict) -> dict:
    model = os.getenv("MODEL_SYNTHESIZER", "claude-sonnet-4-6")

    synthesis_input = json.dumps(agent_outputs, ensure_ascii=False, indent=2)

    response = await client.messages.create(
        model=model,
        max_tokens=2500,
        system=_SYNTHESIS_SYSTEM,
        messages=[{"role": "user", "content": synthesis_input}],
    )

    text = response.content[0].text if response.content else ""

    # Essai 1 : JSON brut
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # Essai 2 : blocs ```json ... ``` (non-greedy + newlines)
    for match in re.finditer(r"```(?:json)?\s*\n([\s\S]*?)\n\s*```", text):
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            continue

    # Essai 3 : stack-based — trouve TOUS les objets {} valides et retourne le plus grand.
    # Contrairement à une regex, gère l'imbrication arbitraire (priority_actions contient
    # des objets imbriqués → la regex à 2 niveaux retournait un sous-objet au lieu de la racine).
    candidates: list[dict] = []
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start >= 0:
                try:
                    candidates.append(json.loads(text[start : i + 1]))
                except json.JSONDecodeError:
                    pass
    if candidates:
        # Retourne l'objet avec le plus de clés de premier niveau (= l'objet racine)
        return max(candidates, key=lambda x: len(x))

    # Fallback dégradé
    return {
        "summary": text[:500] if text else "Synthèse indisponible",
        "priority_actions": [],
        "conflicts": ["Synthèse non structurée — parsing JSON échoué"],
        "cross_domain_insights": [],
        "next_steps": [],
    }
