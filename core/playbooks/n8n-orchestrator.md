# schoolsWP OS — n8n Orchestrator (Multi-Agents)

But
- 1 demande -> router -> 3-5 agents -> synthese -> QA -> sorties

Architecture
Entree -> Router -> Agents (parallele) -> Synthese -> QA -> Sorties

A) Anthropic (Claude) — reglages
Modeles
- Router (leger) : Sonnet
- Agents metier : Sonnet
- Synthese finale : Opus (premium) ou Sonnet
- QA : Sonnet

Parametres
- Temperature : Router/QA 0.1-0.2 | Agents 0.2-0.4 | Synthese 0.2-0.3
- Max tokens : Router 600-1200 | Agents 2000-4000 | Synthese 2500-6000 | QA 1200-2500
- Stop sequences : optionnel (ex. couper apres "## Required fixes")
- Format sortie : sections Markdown fixes

Note n8n
- Attention au schema des tools custom (patterns stricts)

B) OpenAI — reglages
Modeles
- Router : GPT-5 mini
- Agents metier : GPT-5 mini (ou modele qualite)
- Synthese finale : modele qualite ou GPT-5 mini
- QA : GPT-5 mini (temp basse)

Parametres
- Temperature : Router/QA 0.1-0.2 | Agents 0.2-0.4 | Synthese 0.2-0.3
- Max tokens : Router 600-1200 | Agents 2000-4000 | Synthese 2500-6000 | QA 1200-2500
- Response format : JSON pour Router/QA si possible

C) Workflow n8n minimal (squelette)
- Webhook (POST)
- Set: Normalize Input
- Function: Intent Router
- IF SEO -> SEO Agent (LLM)
- IF WP -> WP Agent (LLM)
- IF Automation -> Automation Agent (LLM)
- IF Monetization -> Monetization Agent (LLM)
- Merge (Wait All)
- SYNTHESIZER (LLM)
- QA (LLM)
- IF QA PASS

Payload d'entree (standard)
{
  "mission": "Creer une landing page schoolsWP + maillage + CTA + sequence email",
  "context": {
    "site": "schoolswp.com",
    "stack": "WP + FluentCRM + RankMath",
    "constraints": ["FR", "ton schoolsWP", "vite", "scalable"],
    "goal_kpi": "leads emails"
  },
  "data": {
    "urls": ["https://..."],
    "gsc": null,
    "notes": "cible: apprendre WordPress + freelance"
  }
}

D) Cheap mode vs Full mode
Cheap mode : Router -> 2 agents (SEO + Monetization) -> Synthese -> QA
Full mode : Router -> SEO + WP + Automation + Monetization -> Synthese -> QA -> boucle fixes

E) Solidifier la boucle QA
- Ajouter un Set qui extrait PASS/FAIL via regex
- Si FAIL, renvoyer vers SYNTHESIZER avec fixes injectees

F) Dupliquer pour OpenAI
- Dupliquer chaque node Anthropic en OpenAI
- Garder les prompts
- Appliquer les memes temperatures / max tokens
- Option : Router + QA en JSON pour piloter les IF nodes
