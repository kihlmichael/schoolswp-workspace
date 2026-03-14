from __future__ import annotations

from agents.base import BaseContentAgent

_SYSTEM = """Tu es le Data Strategist de schoolsWP — analyste SEO et business senior.

MISSION : Produire le Dashboard KPI Éditorial schoolsWP.
Un tableau de pilotage stratégique — pas décoratif.
En 30 secondes : où tu gagnes, où tu perds, où tu dois publier, où tu dois optimiser.

━━━ SCORE ÉCOSYSTÈME schoolsWP ━━━

Indicateur central mensuel /100 :
Score Écosystème = (Autorité_moy × 0.3) + (ROI_norm × 0.3) + (SEO_croissance × 0.2) + (LLM_moy × 0.2)

- Autorité_moy    : moyenne des scores pilier /100
- ROI_norm        : (ROI_moyen_articles / 9) × 100
- SEO_croissance  : estimation trafic/croissance fournie ou 50 (neutre) si absent
- LLM_moy         : moyenne scores LLM-SEO × 10 (pour /100)

━━━ DIAGNOSTICS PAR VALEUR ━━━

Piliers (/100) :
  < 50   : 🔴 Faible         — urgence critique
  50–70  : 🟡 En construction — développer
  70–85  : 🟢 Solide         — consolider
  > 85   : 💎 Dominant       — maintenir

Score Écosystème (/100) :
  < 40   : 🔴 Critique
  40–60  : 🟡 En développement
  60–75  : 🟢 Croissance active
  > 75   : 💎 Machine d'autorité

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

## Dashboard KPI Éditorial — schoolsWP
### Période : [période fournie ou "Analyse ponctuelle"]

---

### Score Écosystème schoolsWP

```
┌─────────────────────────────────────────┐
│  Score Écosystème : XX/100              │
│  [🔴 Critique | 🟡 Développement |      │
│   🟢 Croissance | 💎 Machine]           │
│                                         │
│  Autorité    XX/100  × 0.30 = XX.X      │
│  ROI contenu XX/100  × 0.30 = XX.X      │
│  SEO growth  XX/100  × 0.20 = XX.X      │
│  LLM score   XX/100  × 0.20 = XX.X      │
└─────────────────────────────────────────┘
```

---

### 1. Vue Macro — Vision 360°

| KPI | Valeur | Évolution | Diagnostic |
|-----|--------|-----------|------------|
| Trafic organique | X | +/- X% | ... |
| CTR moyen | X% | ... | ... |
| Articles publiés | X | ... | ... |
| Score Autorité global | X/100 | ... | ... |
| Score LLM-SEO moyen | X/10 | ... | ... |
| Score ROI moyen articles | X.X/9 | ... | ... |
| Articles Priorité A | X | ... | ... |
| Clusters actifs | X | ... | ... |

> [Insight macro : 2 lignes — ce qui domine, ce qui freine]

---

### 2. Index Autorité par Pilier

| Pilier | Score /100 | Statut | Tendance | Priorité |
|--------|-----------|--------|----------|---------|
| SEO WordPress | XX | 🔴/🟡/🟢/💎 | ↑↓→ | Renforcer / Maintenir |
| LMS WordPress | XX | ... | ... | ... |
| CRM WordPress | XX | ... | ... | ... |
| Automatisation | XX | ... | ... | ... |
| Performance | XX | ... | ... | ... |
| E-commerce | XX | ... | ... | ... |

**Pilier le plus faible** : [pilier] — action immédiate : [1 ligne]
**Pilier dominant** : [pilier] — à capitaliser : [1 ligne]

---

### 3. KPI ROI Contenu

Tableau des articles analysés, classés par Score ROI décroissant :

| # | Article | SEO | Biz | Auth | Effort | ROI | Priorité |
|---|---------|-----|-----|------|--------|-----|---------|
| 1 | ... | X | X | X | X | X.X | 🔥 A |

**Quick wins identifiés** :
1. [Titre] — ROI X.X — [pourquoi rapide]
2. [Titre] — ROI X.X — [pourquoi rapide]

**Articles à mettre à jour en priorité** :
- [Titre] — [raison : score faible ou angle périmé]

---

### 4. KPI LLM & Citations IA

| Article | Extractibilité | Clarté | Autorité | Score LLM |
|---------|---------------|--------|----------|-----------|
| ... | X/10 | X/10 | X/10 | X/10 |

**Score moyen LLM-SEO** : X.X/10
**Objectif** : > 8/10
**Articles sous le seuil** : X articles à optimiser avec `--skip-llm` désactivé

---

### 5. KPI Cocon & Maillage

| Pilier | Satellites | Liens internes | Profondeur | Cohérence | Diagnostic |
|--------|-----------|---------------|------------|-----------|-----------|
| LMS | X/X | X/X | X | X/10 | Cluster / Orphelins |

**Densité maillage globale** : X/10
**Risque** : [articles orphelins sans cluster ?]

---

### Alertes stratégiques

| Priorité | Alerte | Action |
|---------|--------|--------|
| 🔴 Urgente | ... | ... |
| 🟡 Court terme | ... | ... |

---

### 3 actions immédiates

En fonction du Score Écosystème et des KPI :

1. **[Action]** — Agent : `[module.cli]` — Impact estimé : +X pts Score Écosystème
2. **[Action]** — Agent : `[module.cli]` — Impact estimé : +X pts
3. **[Action]** — Agent : `[module.cli]` — Impact estimé : +X pts

---

RÈGLES :
- Si une donnée est absente, indique "N/D" et estime par défaut plutôt que de bloquer
- Chaque diagnostic doit avoir une action associée — pas de constat sans suite
- Le Score Écosystème doit montrer le calcul explicite
- Tutoiement systématique dans les recommandations
- Commence directement par le H2. Zéro commentaire préliminaire."""


class KpiDashboardAgent(BaseContentAgent):
    """
    Agent Dashboard KPI Éditorial schoolsWP.

    Agrège les données de tous les agents en un dashboard de pilotage stratégique :
    - Score Écosystème /100 (indicateur central)
    - Vue Macro 360° (8 KPI globaux)
    - Index Autorité par pilier
    - KPI ROI Contenu (Score ROI par article)
    - KPI LLM / Citations IA
    - KPI Cocon & Maillage
    - Alertes + 3 actions immédiates

    La séparation de responsabilité :
    - Le CLI parse les fichiers (scores numériques extractibles)
    - L'agent LLM interprète, diagnostique et recommande
    """

    name = "kpi-dashboard"
    system_prompt = _SYSTEM

    async def run(  # type: ignore[override]
        self,
        period: str | None = None,
        context: str | None = None,
        pillar_scores: dict[str, int] | None = None,
        article_kpis: list[dict] | None = None,
        authority_content: str | None = None,
        roi_content: str | None = None,
        cocon_content: str | None = None,
        llm_scores: list[dict] | None = None,
    ) -> str:
        """
        Génère le Dashboard KPI Éditorial complet.

        Args:
            period:           Période d'analyse (ex: "Février 2026", "S1 2026")
            context:          Données macro non extractibles automatiquement :
                              trafic, CTR, conversions, leads email
                              (ex: "trafic : 8 200 sessions/mois +12%, CTR 3.2%, 45 leads email")
            pillar_scores:    Scores piliers pré-parsés {"lms": 62, "seo": 74, ...}
                              Si absent, extrait depuis authority_content
            article_kpis:     Liste d'articles pré-parsés :
                              [{"title": "...", "seo": 8, "biz": 7, "auth": 6,
                                "effort": 5, "roi": 7.35, "priority": "A",
                                "llm_score": 7.8}]
                              Si absent, extrait depuis roi_content
            authority_content: Output brut de PillarAuthorityAgent (.md)
            roi_content:      Output brut de RoiEditorialPlanAgent (.md)
            cocon_content:    Output brut de CoconBuilderAgent (.md)
            llm_scores:       Scores LLM extraits de plusieurs articles :
                              [{"article": "...", "extractibilite": 8,
                                "clarte": 7, "autorite": 8, "global": 7.7}]

        Returns:
            Dashboard KPI complet en markdown.
        """
        period_block = f"Période : **{period}**\n\n" if period else ""
        context_block = f"Données contextuelles :\n{context}\n\n" if context else ""

        # Scores piliers structurés
        pillar_block = ""
        if pillar_scores:
            lines = "\n".join(
                f"  - {k.upper()}: {v}/100" for k, v in pillar_scores.items()
            )
            pillar_block = f"Scores piliers (pré-parsés) :\n{lines}\n\n"

        # KPI articles structurés
        articles_block = ""
        if article_kpis:
            articles_block = (
                f"KPI articles ({len(article_kpis)} articles analysés) :\n"
                + "\n".join(
                    f"  - {a.get('title', '?')} : "
                    f"SEO={a.get('seo', 'N/D')} Biz={a.get('biz', 'N/D')} "
                    f"Auth={a.get('auth', 'N/D')} Effort={a.get('effort', 'N/D')} "
                    f"ROI={a.get('roi', 'N/D')} Priorité={a.get('priority', '?')} "
                    f"LLM={a.get('llm_score', 'N/D')}"
                    for a in article_kpis
                )
                + "\n\n"
            )

        # LLM scores
        llm_block = ""
        if llm_scores:
            llm_block = (
                f"Scores LLM-SEO ({len(llm_scores)} articles) :\n"
                + "\n".join(
                    f"  - {s.get('article', '?')} : global={s.get('global', 'N/D')}/10"
                    for s in llm_scores
                )
                + "\n\n"
            )

        # Données brutes des agents (si pré-parsées non disponibles)
        authority_block = (
            f"--- INDEX AUTORITÉ PAR PILIER ---\n{authority_content}\n\n"
            if authority_content and not pillar_scores
            else ""
        )
        roi_block = (
            f"--- PLAN ROI ÉDITORIAL ---\n{roi_content}\n\n"
            if roi_content and not article_kpis
            else ""
        )
        cocon_block = (
            f"--- COCON SÉMANTIQUE ---\n{cocon_content}\n\n"
            if cocon_content
            else ""
        )

        missing = []
        if not context:
            missing.append("Données trafic/CTR/conversions (non fournies — estime ou indique N/D)")
        if not pillar_scores and not authority_content:
            missing.append("Scores piliers (non fournis — estime à partir du contexte)")
        if not article_kpis and not roi_content:
            missing.append("KPI articles (non fournis — estime avec l'écosystème connu)")

        missing_block = (
            "Données manquantes :\n" + "\n".join(f"- {m}" for m in missing) + "\n\n"
            if missing
            else ""
        )

        user_message = (
            f"{period_block}"
            f"{context_block}"
            f"{missing_block}"
            f"{pillar_block}"
            f"{articles_block}"
            f"{llm_block}"
            f"{authority_block}"
            f"{roi_block}"
            f"{cocon_block}"
            "Génère le Dashboard KPI Éditorial complet selon la structure définie."
        )

        response = await self._client.messages.create(
            model=self.model,
            max_tokens=6000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        return response.content[0].text
