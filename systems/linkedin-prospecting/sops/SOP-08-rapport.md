# SOP-08 — Rapport final

## Objectif

Produire deux livrables :
1. **JSON final** — exploitable par CRM / orchestrateur
2. **Rapport HTML** — lisible par un humain

## Outil

Claude (prompt `prompts/prompt-08-rapport.md`)

## Input

Toutes les sorties des phases precedentes :
- `post_metadata` (SOP-01)
- `intent_analysis` (SOP-02)
- `enriched_leads` (SOP-03)
- `qualified_leads`, `review_leads`, `rejected_leads` (SOP-04)
- Scores (SOP-05)
- `generated_messages` (SOP-06)
- `email_verification` (SOP-07, si active)
- `warnings` (toutes les phases)

## Structure JSON finale

Voir `schemas/final-pipeline-output.json` pour le schema complet.

## Structure HTML

### Sections obligatoires

1. **Header** — nom campagne, date, URL du post
2. **Resume du post** — auteur, texte (tronque si long), date, stats
3. **Statistiques globales** — tableau recapitulatif
4. **Leads qualifies** — tableau avec score, role, entreprise, action
5. **Leads a revoir** — tableau avec score, raison du review
6. **Leads rejetes** — nombre + principales raisons
7. **Messages generes** — 1 bloc par lead avec les 3 variantes
8. **Verification email** — tableau si Hunter active
9. **Warnings** — liste des alertes remontees

### Style HTML

- HTML simple, pas de framework externe
- CSS inline leger
- Lisible sur desktop (largeur min 900px)
- Couleurs sobres
  - Qualified : `#e8f5e9` (vert clair)
  - Review : `#fff3e0` (orange clair)
  - Rejected : `#fce4ec` (rouge clair)
- Tableaux avec bordures legeres
- Police : system font stack

### Statistiques a afficher

| Metrique | Source |
|---|---|
| Commentaires bruts | SOP-01 |
| Commentaires nettoyes | SOP-02 |
| Leads bruts | SOP-01 |
| Leads enrichis | SOP-03 |
| Leads qualifies | SOP-04 |
| Leads a revoir | SOP-04 |
| Leads rejetes | SOP-04 |
| Score moyen (qualified) | SOP-05 |
| Score max | SOP-05 |
| Messages generes | SOP-06 |
| Emails verifies | SOP-07 |

## Quality Control Checklist

- [ ] JSON final contient toutes les sections
- [ ] Nombre de leads coherent entre phases
- [ ] Tous les qualified ont un message
- [ ] Tous les scores sont calcules
- [ ] Warnings remontes
- [ ] HTML contient toutes les sections
- [ ] Aucun champ null inattendu dans le JSON
- [ ] Pas de doublons dans les listes
