# SOP-07 — Verification email Hunter

## Objectif

Determiner quels leads envoyer a Hunter.io pour verification email, et traiter le retour.

## Prerequis

- `enable_hunter` = true
- Cle API Hunter configuree

## Conditions de declenchement

Lancer Hunter **uniquement** pour les leads qui remplissent :

1. `qualification_status` = qualified
2. `final_score` >= `score_contact_threshold`
3. `current_company` identifiable
4. `company_domain` disponible OU deductible
5. `first_name` + `last_name` exploitables

## Priorite Hunter

| Priorite | Condition |
|---|---|
| `high` | Score >= 85 |
| `medium` | Score 70-84 |
| `low` | Ne pas lancer Hunter |

## Traitement

1. Verifier `enable_hunter`
2. Filtrer les leads eligibles
3. Pour chaque lead eligible :
   - Envoyer `first_name`, `last_name`, `company_domain` a Hunter
   - Recuperer `email`, `confidence_score`, `source_type`
4. Classer le resultat

## Interpretation du retour

| Confidence Hunter | Statut |
|---|---|
| >= 80 | `verified` — email exploitable |
| 50-79 | `probable` — a confirmer |
| < 50 | `uncertain` — ne pas utiliser |
| Pas de resultat | `not_found` |

## Output

```json
{
  "lead_id": "lead_001",
  "hunter_priority": "high",
  "email_lookup_status": "success",
  "email": "jane@acme.com",
  "email_confidence": 92,
  "email_source_type": "pattern_match",
  "email_usable": true
}
```

## Cas d'echec

| Erreur | Action |
|---|---|
| API Hunter indisponible | Skip, marquer `email_lookup_status: "api_error"` |
| Rate limit | Retry avec backoff |
| Domaine non trouve | Marquer `not_found`, continuer |
| Nom ambigu | Tenter, marquer `uncertain` si confiance basse |
