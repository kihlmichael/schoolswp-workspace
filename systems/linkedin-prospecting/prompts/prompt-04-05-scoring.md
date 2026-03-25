# Prompt SOP-04 + SOP-05 — Qualification ICP + Scoring commercial

> A utiliser dans un noeud Claude dedie, apres l'enrichissement Unipile.
> Input : enriched_leads + intent_analysis + contexte metier. Output : leads scores et classes.

---

Tu executes la SOP-04 (Qualification ICP) et la SOP-05 (Scoring commercial).

## Objectif

Pour chaque lead enrichi :
1. Attribuer un statut de qualification (qualified / review / rejected)
2. Calculer un score detaille sur 100
3. Definir une action recommandee

## Input

### Leads enrichis

```json
{{enriched_leads_json}}
```

### Analyse d'intention

```json
{{intent_analysis_json}}
```

### Contexte metier

- offre = {{offre}}
- icp_principal = {{icp_principal}}
- roles_cibles = {{roles_cibles}}
- secteurs_cibles = {{secteurs_cibles}}
- tailles_entreprise_cibles = {{tailles_entreprise_cibles}}
- exclusions = {{exclusions}}
- signaux_forts = {{signaux_forts}}
- signaux_faibles = {{signaux_faibles}}
- score_contact_threshold = {{score_contact_threshold}}
- score_review_threshold = {{score_review_threshold}}

## Grille de scoring

| Critere | Max |
|---|---|
| ICP fit | /30 |
| Role / seniorite | /20 |
| Secteur | /15 |
| Intention | /20 |
| Completude donnees | /10 |
| Bonus contextuel | /5 |
| **Total** | **/100** |

### Detail ICP fit (/30)

- 25-30 : correspondance quasi parfaite
- 15-24 : bonne correspondance, 1-2 ecarts mineurs
- 5-14 : correspondance partielle
- 0-4 : hors ICP

### Detail role (/20)

- 18-20 : decideur direct (C-level, VP, Director)
- 12-17 : influenceur fort (Head, Manager senior)
- 6-11 : operateur utile (Senior, Lead)
- 0-5 : role non pertinent ou non identifie

### Detail secteur (/15)

- 13-15 : secteur cible prioritaire
- 7-12 : secteur adjacent ou compatible
- 0-6 : hors cible

### Detail intention (/20)

- 16-20 : besoin explicite
- 10-15 : interet implicite
- 4-9 : engagement faible
- 0-3 : aucun signal

### Detail completude (/10)

- 8-10 : profil riche (ratio >= 0.8)
- 5-7 : profil correct (0.5-0.79)
- 2-4 : profil pauvre (< 0.5)
- 0-1 : donnees insuffisantes

### Detail bonus (/5)

- 4-5 : forte coherence post + commentaire + offre
- 2-3 : coherence moyenne
- 0-1 : pas de lien specifique

## Regles de qualification

```
qualified = NOT IN exclusions AND (role pertinent OR secteur cible) AND (intent >= medium OR profil tres pertinent)
review = NOT IN exclusions AND (donnees partielles OR intent faible OR secteur non confirme)
rejected = IN exclusions OR (role hors cible AND secteur hors cible) OR intent = no_intent + profil non pertinent
```

## Seuils d'action

- `contact_now` : score >= {{score_contact_threshold}} (defaut 70)
- `manual_review` : score >= {{score_review_threshold}} (defaut 45) et < contact
- `ignore` : score < {{score_review_threshold}}

## Format de sortie

Retourne **uniquement** un JSON strict :

```json
{
  "summary_stats": {
    "total_scored": 0,
    "qualified_count": 0,
    "review_count": 0,
    "rejected_count": 0,
    "avg_score_qualified": 0,
    "max_score": 0
  },
  "qualified_leads": [
    {
      "lead_id": "",
      "full_name": "",
      "current_role": "",
      "current_company": "",
      "industry": "",
      "qualification_status": "qualified",
      "qualification_reason": "",
      "icp_fit_score": 0,
      "role_seniority_score": 0,
      "industry_score": 0,
      "intent_score": 0,
      "data_completeness_score": 0,
      "contextual_bonus_score": 0,
      "final_score": 0,
      "recommended_action": "contact_now"
    }
  ],
  "review_leads": [],
  "rejected_leads": [],
  "warnings": []
}
```

## Regles strictes

- Pas de texte hors du JSON
- Score justifie pour chaque lead
- `qualification_reason` obligatoire (1-2 phrases)
- Les exclusions sont eliminatoires
