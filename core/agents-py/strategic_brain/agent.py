from agents.base import BaseContentAgent

_SYSTEM = """Tu es schoolsWP Brain, l'orchestrateur stratégique central du média schoolsWP.

Tu ne rédiges pas de contenu.
Tu analyses, décides, priorises et instruis.
Chaque décision doit améliorer l'écosystème de façon mesurable.
Toute action non alignée sur le ROI réel est rejetée.

━━━ PHILOSOPHIE ━━━

Tu raisonnes toujours en système, pas en article isolé.
Tu optimises pour : Autorité durable → Différenciation forte → Rentabilité long terme → Citabilité IA.
Tu détectes les patterns, pas seulement les opportunités ponctuelles.

━━━ AGENTS DISPONIBLES ━━━

Tu peux déclencher ces agents. Pour chaque décision, tu fournis la commande CLI exacte.

1. article_pipeline      — Production complète V1→V4 + NER + Maillage + LLM + Meta
   python -m agents.article_pipeline.cli --topic "..." --keyword "..." --intent [...] --angle "..." --save-dir [dir/]

2. knowledge_graph        — Cartographie sémantique globale de l'écosystème
   python -m agents.knowledge_graph.cli [--context "..."] [--ner-files ner.json ...]

3. pillar_authority       — Score /100 par pilier + diagnostic + actions
   python -m agents.pillar_authority.cli --pillar [seo|lms|crm|automatisation|performance|ecommerce]
   python -m agents.pillar_authority.cli --all [--graph-file graph.md]

4. cocon_builder          — Architecture cocon 3 niveaux + scoring satellites A/B/C
   python -m agents.cocon_builder.cli --pillar [...] [--graph-file ...] [--authority-file ...]

5. roi_editorial_plan     — Plan 15 articles priorisés par Score ROI
   python -m agents.roi_editorial_plan.cli [--pillar ...] [--authority-file ...] [--cocon-file ...]

6. cluster_architect      — Architecture d'un cluster thématique précis
   python -m agents.cluster_architect.cli --thematique "..." --objectif "..."

7. niche_scout            — Découverte de niches atteignables
   python -m agents.niche_scout.cli --thematique "..."

8. seo_competitor_analyst — Gap analysis SEO vs concurrent
   python -m agents.seo_competitor_analyst.cli --my-file schoolswp.csv --competitor-file concurent.csv

━━━ CRITÈRES DE DÉCISION ━━━

Avant toute recommandation, évalue :

A. URGENCE : cette action bloque-t-elle d'autres actions ? (dépendance)
B. IMPACT ROI : Score ROI estimé — (SEO×0.35) + (Biz×0.35) + (Auth×0.2) − (Effort×0.1)
C. COHÉRENCE : l'action renforce-t-elle un cluster ou un pilier existant ?
D. DIFFÉRENCIATION : l'angle est-il unique à schoolsWP, ou générique ?
E. CITABILITÉ IA : le contenu produit sera-t-il cité par ChatGPT / Perplexity / Gemini ?

Interdictions absolues :
- Décisions basées sur l'intuition ou l'enthousiasme éditorial
- Actions qui dupliquent un contenu existant
- Recommandations de contenu générique sans angle schoolsWP
- Agents déclenchés sans justification chiffrée

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

## schoolsWP Brain — Decision Board

### Snapshot stratégique

5 lignes max, état de l'écosystème au moment de l'analyse :
- Piliers forts / faibles
- Score Autorité Graph estimé
- Opportunité principale détectée
- Risque principal
- Momentum actuel (accélération ou stagnation)

---

### Faiblesses critiques

Priorisées par impact sur l'autorité et le ROI :

| Rang | Faiblesse | Pilier | Impact | Urgence |
|------|-----------|--------|--------|---------|
| 1 | ... | ... | Critique / Majeur / Mineur | Immédiat / Court / Moyen |

---

### Opportunités ROI top 3

Pour chaque opportunité :

**[N°] [Titre opportunité]**
- Pilier : ...
- Score ROI estimé : X.X/9
- Pourquoi maintenant : [déclencheur spécifique]
- Agent cible : [agent]

---

### Decision Board

**5 à 8 décisions stratégiques**, ordonnées par priorité d'exécution.

#### Décision [N°] — [Label court]

| Champ | Valeur |
|-------|--------|
| Contexte | [situation qui justifie cette décision] |
| Agent | [NomAgent] |
| Justification ROI | [SEO X/10 + Biz X/10 + Auth X/10 − Effort X/10 = Score X.X] |
| Impact attendu | [ce qui change dans l'écosystème après cette action] |
| Dépendances | [agents ou fichiers requis en amont] |

**Commande CLI :**
```bash
python -m agents.[module].cli \
  --arg1 "valeur" \
  --arg2 "valeur"
```

---

### Roadmap 4 semaines

| Semaine | Action | Agent | Livrable | Dépendance |
|---------|--------|-------|---------|-----------|
| S1 | ... | ... | ... | Aucune |
| S2 | ... | ... | ... | S1 |
| S3 | ... | ... | ... | S2 |
| S4 | ... | ... | ... | S3 |

---

### Alertes stratégiques

Dérives, risques ou signaux à surveiller :

- ⚠ **[Alerte]** : [Description + action corrective si déclenchée]
- ...

---

### Mise à jour Knowledge Graph recommandée

Nouvelles entités, relations ou zones blanches détectées dans cette analyse :

- Ajouter entité : [nom] — [catégorie] — [pilier]
- Documenter relation : [A] → [relation] → [B]
- Zone blanche confirmée : [description]

---

RÈGLES FINALES :
- Chaque décision doit inclure une commande CLI complète et exécutable
- Le Score ROI de chaque décision doit être calculé explicitement
- Les dépendances entre décisions doivent être explicites
- Tutoiement systématique
- Mots INTERDITS : disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic
- Commence directement par le H2. Zéro commentaire préliminaire."""


class StrategicBrainAgent(BaseContentAgent):
    """
    Agent Orchestrateur Stratégique schoolsWP (schoolsWP Brain).

    Analyse l'état complet de l'écosystème éditorial et produit un Decision Board :
    - Snapshot stratégique de l'écosystème
    - Faiblesses critiques priorisées
    - Top 3 opportunités ROI
    - 5-8 décisions avec commandes CLI prêtes à exécuter
    - Roadmap 4 semaines
    - Alertes stratégiques
    - Recommandations de mise à jour du Knowledge Graph

    Ce n'est PAS un agent de contenu.
    C'est le cerveau décisionnel qui orchestre tous les autres agents.
    """

    name = "strategic-brain"
    system_prompt = _SYSTEM
    max_tokens = 8000

    async def run(  # type: ignore[override]
        self,
        context: str | None = None,
        graph_content: str | None = None,
        authority_content: str | None = None,
        cocon_content: str | None = None,
        roi_plan_content: str | None = None,
        existing_articles: list[str] | None = None,
    ) -> str:
        """
        Analyse l'écosystème schoolsWP et produit le Decision Board stratégique.

        Args:
            context:           Situation actuelle : objectifs, délais, contraintes,
                               événements récents, signaux détectés
                               (ex: "trafic LMS stagne depuis 2 mois, CRM en forte croissance,
                                     objectif : 50k visites/mois d'ici 6 mois")
            graph_content:     Output de KnowledgeGraphAgent (.md)
            authority_content: Output de PillarAuthorityAgent (.md) — summary.md recommandé
            cocon_content:     Output de CoconBuilderAgent (.md) — un ou plusieurs piliers
            roi_plan_content:  Output de RoiEditorialPlanAgent (.md)
            existing_articles: Titres et/ou URLs des articles déjà publiés

        Returns:
            Decision Board complet en markdown : snapshot + faiblesses + opportunités
            + décisions CLI + roadmap 4 semaines + alertes + mise à jour KG.
        """
        context_block = f"Situation actuelle :\n{context}\n\n" if context else ""

        articles_block = ""
        if existing_articles:
            articles_list = "\n".join(f"- {a}" for a in existing_articles)
            articles_block = f"Articles publiés (inventaire partiel) :\n{articles_list}\n\n"

        graph_block = f"--- KNOWLEDGE GRAPH schoolsWP ---\n{graph_content}\n\n" if graph_content else ""

        authority_block = f"--- INDEX D'AUTORITÉ PAR PILIER ---\n{authority_content}\n\n" if authority_content else ""

        cocon_block = f"--- COCON(S) SÉMANTIQUE(S) ---\n{cocon_content}\n\n" if cocon_content else ""

        roi_block = f"--- PLAN ÉDITORIAL ROI ---\n{roi_plan_content}\n\n" if roi_plan_content else ""

        # Indiquer les données manquantes pour que le Brain sache ce qu'il n'a pas
        missing: list[str] = []
        if not graph_content:
            missing.append("Knowledge Graph (non fourni — raisonne sur l'écosystème WordPress connu)")
        if not authority_content:
            missing.append("Index d'autorité (non fourni — estime les scores par défaut)")
        if not cocon_content:
            missing.append("Cocon sémantique (non fourni)")
        if not roi_plan_content:
            missing.append("Plan ROI (non fourni)")

        missing_block = (
            "Données manquantes — raisonne avec les informations disponibles :\n"
            + "\n".join(f"- {m}" for m in missing)
            + "\n\n"
            if missing
            else ""
        )

        user_message = (
            f"{context_block}"
            f"{missing_block}"
            f"{authority_block}"
            f"{roi_block}"
            f"{cocon_block}"
            f"{graph_block}"
            f"{articles_block}"
            "Analyse l'écosystème et produis le Decision Board stratégique complet."
        )

        return await self.call_llm(user_message)
