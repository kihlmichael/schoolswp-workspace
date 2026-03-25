# SOP-03 — Enrichissement Unipile

## Objectif

Recuperer tous les commentateurs via Unipile (pagination 100/page) puis enrichir chaque profil.

## Input

- Liste `raw_leads[]` issue de SOP-01 + SOP-02
- URL profil LinkedIn ou nom du commentateur

## Outil

Unipile API

## Traitement

### Etape 1 — Recuperation des commentateurs

- Unipile recupere tous les commentateurs du post
- Pagination : 100 commentateurs par page
- Boucler jusqu'a epuisement des pages

### Etape 2 — Enrichissement profil complet

Pour chaque commentateur, recuperer :

| Champ | Description | Priorite |
|---|---|---|
| `first_name` | Prenom | obligatoire |
| `last_name` | Nom | obligatoire |
| `full_name` | Nom complet | obligatoire |
| `linkedin_profile_url` | URL profil | obligatoire |
| `headline` | Titre LinkedIn | obligatoire |
| `current_role` | Poste actuel | obligatoire |
| `seniority_estimated` | Niveau hierarchique estime | important |
| `current_company` | Entreprise actuelle | obligatoire |
| `company_domain` | Domaine web entreprise | important |
| `industry` | Secteur d'activite | important |
| `location` | Localisation | utile |
| `company_size` | Taille entreprise | utile |
| `profile_summary` | Resume profil | utile |

### Etape 3 — Estimation de seniorite

Mapper le titre vers un niveau :

| Niveau | Titres typiques |
|---|---|
| `c_level` | CEO, CTO, CMO, COO, CFO |
| `vp` | VP, Vice President |
| `director` | Director, Directeur |
| `head` | Head of, Responsable |
| `manager` | Manager, Chef de projet |
| `senior` | Senior, Lead |
| `mid` | Consultant, Specialist, Analyst |
| `junior` | Junior, Stagiaire, Assistant |
| `unknown` | Non identifiable |

### Etape 4 — Calcul de completude

```
data_completeness_ratio = champs_remplis / champs_totaux
```

Seuils :
- >= 0.8 : profil riche
- 0.5 - 0.79 : profil correct
- < 0.5 : profil pauvre

### Etape 5 — Mapping source/enrichi

Fusionner les donnees Apify (commentaire, intention) avec les donnees Unipile (profil).

Regles :
- Matching par `linkedin_profile_url` (prioritaire)
- Fallback par `full_name` si URL manquante
- Si collision ou ambiguite : marquer `manual_review_required: true`

## Cas d'echec

| Erreur | Action |
|---|---|
| Profil introuvable | Marquer `enrichment_status: "not_found"`, garder le lead |
| Enrichissement partiel | Garder le lead, calculer completude |
| Rate limit Unipile | Retry avec backoff, max 3 |
| URL profil absente | Tenter matching par nom, sinon marquer review |

## Output

Voir `schemas/enriched-lead.json`
