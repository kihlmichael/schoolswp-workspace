# T10 — Priorisation & Roadmap finale

## Objectif

Synthétiser toutes les recommandations (T1-T9) en un plan d'action clair, dédupliqué, priorisé et planifié sur 30/60/90 jours.

## Outils clés

- Skill : `authority-domination-roadmap` (existant dans `.claude/skills/`)
- Agent Python : `agents.strategic_brain.cli`
- Google Sheets (onglet `10_Backlog`)
- Google Docs (Doc ROADMAP)

## Entrées exactes

- Tous les onglets Google Sheets remplis : `02_Hygiene` à `09_Conversion`
- `10_Backlog` pré-rempli au fil des tâches précédentes

## Étapes

1. Consolider toutes les actions des tâches T2 à T9 dans `10_Backlog`
2. Dédupliquer les actions similaires (ex : "corriger hreflang" peut apparaître en T2 et T7)
3. Scorer chaque action : Impact SEO (H/M/L) × Impact Business (H/M/L) × Effort (XS/S/M/L)
4. Classer en 3 horizons :
   - Quick wins (P1 + effort XS/S) → cette semaine ou 30j
   - Moyen terme (P2 + effort M) → 60j
   - Stratégique (P2/P3 + effort L) → 90j+
5. Rédiger le Doc ROADMAP 30/60/90j (max 1 page exécutive)
6. Lister les 5 quick wins immédiats
7. Mettre à jour `10_Backlog` avec statuts et owners

## Sorties attendues

**Fichier :** `impact_effort.csv`
**Destination :** Onglet `10_Backlog`

**Schéma CSV :**

```
id, action, categorie, impact_SEO, impact_business, effort, priorite, horizon, outils, owner, etat
```

**Valeurs categorie :** indexation | clusters | maillage | multilingue | eeat | conversion | roadmap
**Valeurs horizon :** 30j | 60j | 90j
**Valeurs etat :** todo | en-cours | done | bloque

**Doc :** `ROADMAP-30-60-90.gdoc` — 1 page max avec :

- Résumé exécutif (3 lignes)
- Quick wins immédiats (liste puces)
- Plan 30j / 60j / 90j
- Tableau de bord KPIs

## Observables

- Actions documentées dans les onglets T2 à T9 (données réelles du workflow)
- Priorités et efforts estimés dans chaque tâche

## Hypothèses à valider

- Impact réel des actions sur le trafic (À VALIDER via GSC 30-90j après implémentation)
- Capacité d'exécution réelle par semaine (À VALIDER avec l'équipe)

## Dépendances

- **Toutes les tâches T2-T9 obligatoires**

## KPIs

| KPI                         | Baseline          | Objectif                     |
| --------------------------- | ----------------- | ---------------------------- |
| Actions P1 complétées à 30j | 0%                | ≥70%                         |
| Quick wins implémentés      | 0                 | 5 dans les 15 premiers jours |
| Trafic organique total      | À VALIDER via GSC | +20-30% à 90j                |

## Effort / Priorité

- Effort : S
- Priorité : **P1** (synthèse = conditions d'exécution du reste)

## Risques / Blocages

- Trop d'actions → appliquer le filtre impact-effort strict, ne retenir que ≤15 actions en P1
- Roadmap irréaliste → valider les capacités d'exécution avant de finaliser

## Prompt agent IA

```
RÔLE : Tu es le responsable SEO de schoolsWP.com chargé de construire la roadmap d'implémentation.

OBJECTIF : Synthétiser toutes les recommandations en un plan d'action réaliste et priorisé.

INPUTS :
- Tous les onglets Google Sheets remplis (02_Hygiene à 09_Conversion)
- 10_Backlog initial

ACTIONS (dans l'ordre) :
1. Consolide toutes les actions sans doublons
2. Pour chaque action : note Impact SEO (H/M/L), Impact Business (H/M/L), Effort (XS/S/M/L)
3. Calcule un score de priorité : (Impact SEO + Impact Business) / Effort
4. Classe en urgent/P1, moyen/P2, long/P3
5. Planifie : quoi faire à 30j, 60j, 90j
6. Identifie les 5 quick wins (P1, effort ≤ S, impact H)

FORMAT DE SORTIE :
- CSV impact_effort : id, action, categorie, impact_SEO, impact_business, effort, priorite, horizon, outils, owner, etat
- Doc ROADMAP (max 1 page) : résumé exécutif + quick wins + plan 30/60/90j

CONDITIONS D'ARRÊT :
- Toutes les actions P1 ont un horizon 30j défini
- Les 5 quick wins sont identifiés et actionnables immédiatement
- La roadmap est cohérente : pas de dépendance cyclique, pas d'action orpheline
```
