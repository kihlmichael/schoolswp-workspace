# SOP-00 — Master Orchestrator

## Identite

| Champ | Valeur |
|---|---|
| Nom | Pipeline LinkedIn Prospecting from Post URL |
| Version | V4 |
| Objectif | Transformer l'URL d'un post LinkedIn en leads scores, messages personnalises et rapport HTML |
| Declencheur | URL de post LinkedIn fournie (formulaire / webhook / manuel) |
| Frequence | A la demande ou par batch |
| Operateur | n8n / Make / pipeline custom |

## Resultat attendu

- Leads enrichis et scores
- Messages personnalises par lead qualifie
- Rapport HTML lisible
- JSON final exploitable par CRM / Airtable / Notion

## Outils requis

| Outil | Role | Phase |
|---|---|---|
| Apify | Scraping post + commentaires | Phase 1 |
| Unipile | Recuperation commentateurs + enrichissement profils | Phase 2-3 |
| Claude | Analyse intention + scoring + messages + rapport | Phase 2, 5, 6, 7, 8 |
| Hunter.io | Verification email (optionnel) | Phase 7 |
| n8n / Make | Orchestration | Toutes |

## Sequence des phases

```
Phase 1 — SOP-01 : Collecte Apify
       |
Phase 2 — SOP-02 : Analyse intention (Claude)
       |
Phase 3 — SOP-03 : Enrichissement Unipile
       |
Phase 4 — SOP-04 : Qualification ICP
       |
Phase 5 — SOP-05 : Scoring commercial (Claude)
       |
Phase 6 — SOP-06 : Messages personnalises (Claude)
       |
Phase 7 — SOP-07 : Verification email Hunter (optionnel)
       |
Phase 8 — SOP-08 : Rapport final JSON + HTML (Claude)
```

## Points de controle

| Apres phase | Validation |
|---|---|
| Phase 1 | Au moins 1 commentaire exploitable |
| Phase 2 | Au moins 1 lead avec intention detectee |
| Phase 3 | Au moins 1 lead enrichi |
| Phase 4 | Au moins 1 lead qualified |
| Phase 5 | Scores calcules pour tous les leads |
| Phase 6 | Messages generes pour tous les qualified |
| Phase 8 | JSON + HTML produits et coherents |

## Gestion volumetrie

- Unipile pagine a 100 commentateurs/page
- Si > 100 commentaires : boucler sur les pages
- Si > 500 commentaires : limiter aux 200 plus pertinents (tri par intention)
- Retry : max 3 tentatives par appel API, backoff exponentiel

## Variables globales

Voir README.md pour la liste complete des variables.
