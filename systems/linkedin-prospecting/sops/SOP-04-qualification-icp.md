# SOP-04 — Qualification ICP

## Objectif

Classer chaque lead enrichi selon sa correspondance avec l'ICP.

## Input

- `enriched_leads[]` issue de SOP-03
- Variables metier : `icp_principal`, `roles_cibles`, `secteurs_cibles`, `tailles_entreprise_cibles`, `exclusions`

## Statuts de qualification

### `qualified`

Le lead correspond clairement a l'ICP :
- Role pertinent (dans `roles_cibles` ou equivalent)
- Secteur cible (dans `secteurs_cibles` ou adjacent)
- Pas dans `exclusions`
- Signal d'intention utile OU profil tres pertinent

### `review`

Le lead **pourrait** etre interessant mais il manque :
- Confirmation du secteur ou du role
- Enrichissement complet
- Intention claire
- Taille d'entreprise non verifiable

### `rejected`

Le lead ne correspond pas :
- Particulier hors cible
- Etudiant (si non cible)
- Role non pertinent
- Secteur hors scope
- Commentaire sans valeur + profil hors ICP
- Match avec `exclusions`

## Regles de decision

```
SI role IN roles_cibles
   ET secteur IN secteurs_cibles (ou adjacent)
   ET NOT IN exclusions
   ET (intent >= medium OU profil tres pertinent)
=> qualified

SI role IN roles_cibles
   ET (secteur inconnu OU enrichissement partiel OU intent faible)
   ET NOT IN exclusions
=> review

SINON
=> rejected
```

## Exemples concrets

| Lead | Role | Secteur | Intent | Statut |
|---|---|---|---|---|
| Jane Doe | Head of Growth | SaaS | high | qualified |
| Marc Dupont | CEO | Agence Web | medium | qualified |
| Sophie Martin | DRH | Industrie | low | rejected (role hors cible) |
| Pierre Leroy | Consultant SEO | Inconnu | medium | review |
| Emma Garcia | Etudiante | N/A | high | rejected (profil hors cible) |

## Output

Chaque lead recoit :
- `qualification_status` : qualified / review / rejected
- `qualification_reason` : justification en 1-2 phrases
