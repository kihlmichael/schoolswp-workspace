# SOP-05 — Scoring commercial

## Objectif

Attribuer un score sur 100 a chaque lead pour prioriser les actions.

## Outil

Claude (prompt `prompts/prompt-04-05-scoring.md`)

## Structure du score

| Critere | Points max | Description |
|---|---|---|
| ICP fit | /30 | Correspondance globale avec l'ICP |
| Role / seniorite | /20 | Niveau de decision ou d'influence |
| Secteur | /15 | Pertinence du secteur d'activite |
| Intention | /20 | Force du signal detecte dans le commentaire |
| Completude | /10 | Richesse des donnees profil |
| Bonus contextuel | /5 | Alignement post + commentaire + profil |

## Detail de calcul

### ICP fit (/30)

| Score | Condition |
|---|---|
| 25-30 | Correspondance quasi parfaite avec l'ICP |
| 15-24 | Bonne correspondance, 1-2 ecarts mineurs |
| 5-14 | Correspondance partielle |
| 0-4 | Hors ICP |

### Role / seniorite (/20)

| Score | Condition |
|---|---|
| 18-20 | Decideur direct (C-level, VP, Director) |
| 12-17 | Influenceur fort (Head, Manager senior) |
| 6-11 | Operateur utile (Senior, Lead) |
| 0-5 | Role non pertinent ou non identifie |

### Secteur (/15)

| Score | Condition |
|---|---|
| 13-15 | Secteur cible prioritaire |
| 7-12 | Secteur adjacent ou compatible |
| 0-6 | Hors cible |

### Intention (/20)

| Score | Condition |
|---|---|
| 16-20 | Besoin explicite, demande concrete |
| 10-15 | Interet implicite, engagement reel |
| 4-9 | Engagement faible, reaction sociale |
| 0-3 | Aucun signal |

### Completude (/10)

| Score | Condition |
|---|---|
| 8-10 | Profil riche (completude >= 0.8) |
| 5-7 | Profil correct (0.5-0.79) |
| 2-4 | Profil pauvre (< 0.5) |
| 0-1 | Donnees insuffisantes |

### Bonus contextuel (/5)

| Score | Condition |
|---|---|
| 4-5 | Forte coherence post + commentaire + offre |
| 2-3 | Coherence moyenne |
| 0-1 | Pas de lien specifique |

## Formule

```
final_score = icp_fit + role_seniority + industry_fit + intent_score + data_completeness + contextual_bonus
```

## Seuils de decision

| Score | Action |
|---|---|
| >= 70 | `contact_now` — contacter immediatement |
| 45-69 | `manual_review` — revoir manuellement |
| 0-44 | `ignore` — rejeter |

**Note** : les seuils sont configurables via `score_contact_threshold` et `score_review_threshold`.

## Exemple

```json
{
  "lead_id": "lead_001",
  "icp_fit_score": 26,
  "role_seniority_score": 18,
  "industry_score": 15,
  "intent_score": 16,
  "data_completeness_score": 9,
  "contextual_bonus_score": 4,
  "final_score": 88,
  "recommended_action": "contact_now"
}
```
