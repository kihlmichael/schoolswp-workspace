# Tableau de Mapping – Dry Run Migration

**Date** : 2026-02-07
**Statut** : DRY-RUN (simulation, aucune modification effectuée)

---

## Format du tableau

| # | Ancien nom | Ancien chemin | Nouveau nom | Nouveau chemin | Confiance | Action | Notes |
|---|-----------|---------------|-------------|----------------|-----------|--------|-------|

## Légende Actions

| Action | Description |
|--------|-------------|
| RENAME | Renommer uniquement (le fichier est déjà dans le bon dossier) |
| MOVE | Déplacer uniquement (le nom est déjà conforme) |
| RENAME+MOVE | Renommer ET déplacer |
| ARCHIVE | Déplacer vers 99_ARCHIVES (doublon ou obsolète) |
| OK | Aucune action nécessaire |
| À_VALIDER | Confiance < 80%, nécessite validation humaine |

## Légende Confiance

| Niveau | Signification |
|--------|---------------|
| 90-100% | Mapping automatique fiable |
| 80-89% | Mapping probable, vérification rapide recommandée |
| 60-79% | Incertain, validation humaine requise |
| < 60% | Très incertain, probablement besoin d'infos supplémentaires |

---

## Exemples de mapping

| # | Ancien nom | Ancien chemin | Nouveau nom | Nouveau chemin | Confiance | Action | Notes |
|---|-----------|---------------|-------------|----------------|-----------|--------|-------|
| 1 | `prompt_email_bienvenue_V2.docx` | Mes Prompts/ | `2026-01-15 – Email-Bienvenue – Template – Email – V2.docx` | 02_TEMPLATES/02_Email_CRM_FluentCRM/03_LIVE | 85% | RENAME+MOVE | Date estimée depuis création fichier |
| 2 | `2026-01-20 – Article-WP-Speed – Prompt – SEO.md` | Prompts/SEO/ | `2026-01-20 – Article-WP-Speed – Prompt – SEO.md` | 03_PROMPTS/01_Editorial_SEO/03_LIVE | 100% | MOVE | Format déjà conforme |
| 3 | `landing page conversion checklist` | Brouillons/ | `2026-02-01 – Landing-Page – Checklist – Landing.md` | 01_ADMIN/02_Checklists-Qualite | 70% | À_VALIDER | Pas de date ni extension, sujet ambigu |
| 4 | `2025-12-10 – Sequence-Lancement-Plugin – Template – Email – V1.md` | Email/ | `2025-12-10 – Sequence-Lancement-Plugin – Template – Email – V1.md` | 05_MONETISATION/04_Sequences_Email | 95% | MOVE | Séquence monétisation, pas CRM générique |
| 5 | `prompt_email_bienvenue_V1.docx` | Mes Prompts/ | — | 99_ARCHIVES | 90% | ARCHIVE | Doublon de #1 (V1 remplacé par V2) |

---

## Tableau de mapping réel

_À remplir après exécution de `runAudit()` et `generateMapping()` dans le script Apps Script._
_Le Google Sheet généré automatiquement remplacera ce tableau._

| # | Ancien nom | Ancien chemin | Nouveau nom | Nouveau chemin | Confiance | Action | Notes |
|---|-----------|---------------|-------------|----------------|-----------|--------|-------|
| | | | | | | | |

---

## Validation

- [ ] Mapping relu par Michaël
- [ ] Lignes "À_VALIDER" traitées
- [ ] Doublons confirmés pour archivage
- [ ] Prêt pour exécution de `executeMigration()`

---

*schoolsWP Drive Organizer – Dry Run*
