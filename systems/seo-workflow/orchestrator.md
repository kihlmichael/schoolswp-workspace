# Orchestrateur SEO — schoolsWP

## Rôle

Agent de coordination du workflow SEO 10-tâches. Décide l'ordre d'exécution, valide les outputs, gère les blocages.

## Règles d'orchestration

1. Tâches séquentielles : T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8 → T9 → T10
2. Blocage : si T_n échoue, arrêter et alerter avant T_n+1
3. Outputs : chaque tâche écrit dans un onglet Google Sheets dédié
4. Validation : vérifier que l'onglet n'est pas vide avant de passer à la suite

## Inputs / Outputs

| Tâche | Input | Output | Onglet Sheets |
|-------|-------|--------|---------------|
| T1 | sitemap.xml | CSV URLs | T1_INVENTAIRE |
| T2 | T1 + GSC API | Opportunités | T2_OPPORTUNITES |
| T3 | T1 | Issues techniques | T3_AUDIT_TECH |
| T4 | T2 | Gaps SERP | T4_SERP |
| T5 | T4 + concurrent | Delta keywords | T5_GAP |
| T6 | T5 | Briefs | T6_BRIEFS |
| T7 | T1 + scores | Articles à optim | T7_OPTIM |
| T8 | T1 + T7 | Plan maillage | T8_MAILLAGE |
| T9 | T7 | Blocs E-E-A-T | T9_EEAT |
| T10 | Tout | Backlog priorisé | T10_ROADMAP |

## Critères de validation par tâche

- T1 : >= 50 URLs dans l'onglet
- T2 : >= 5 opportunités identifiées
- T3 : rapport généré (même si 0 issue)
- T4-T10 : onglet non vide

## Gestion des blocages

- Timeout 30min par tâche
- Retry 1x sur échec API
- Discord alert si blocage persistant
- Continuer à T_n+1 uniquement si T_n validée
