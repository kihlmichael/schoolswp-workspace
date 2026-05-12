---
parent: masteriyo-arbitrage-2026-05-06.md
type: draft-section
section: 8 - Migration Masteriyo vers Tutor LMS
target_words: 300
date_drafted: 2026-05-07
sources:
  - vault: 08_sources/plugins-wordpress/tutor-lms/docs/2026-05-04_tutor-lms-doc_11-migration_*.md (5 fichiers)
  - constat: pas de Migration Tool officiel Masteriyo dans Tutor LMS (LearnDash + LearnPress + LifterLMS uniquement)
---

# Draft section 8 - Migration Masteriyo vers Tutor LMS

> Ce snippet est destiné à être inséré comme section 8 de l'article refondu `/masteriyo-lms-avis/`. Ton tutoiement, voix "je", évite les marketing words. Conforme règle 31 BRAND_RULES.md (respect du concurrent).

---

## Migration Masteriyo vers Tutor LMS : ce qu'il faut savoir

Si tu utilises déjà Masteriyo et que tu envisages de basculer sur Tutor LMS, voici ce que tu dois savoir avant de te lancer.

### Pas de migration tool automatique

Tutor LMS propose un **Migration Tool officiel** qui couvre LearnDash, LearnPress et LifterLMS. **Masteriyo n'en fait pas partie aujourd'hui** (sources : [docs.themeum.com/tutor-lms/migration](https://docs.themeum.com/tutor-lms/migration/), avril 2026).

Concrètement, ça veut dire qu'il n'y a pas de bouton "Migrer depuis Masteriyo" dans Tutor LMS. La bascule se fait à la main, étape par étape.

### L'approche que je recommande : double-run progressif

Plutôt qu'un big-bang risqué, je préfère la méthode progressive :

1. **Backup complet** du site (BackupBuddy, UpdraftPlus, ou cron serveur).
2. **Installer Tutor LMS** sur un environnement de staging.
3. **Recréer les cours** dans Tutor : la structure Cours / Modules / Leçons / Quiz est conceptuellement très proche de celle de Masteriyo. Compter 30-60 min par cours pour un import propre.
4. **Re-paramétrer le paiement** : si tu utilises Stripe/PayPal natif Masteriyo, Tutor 3.0+ propose un eCommerce natif équivalent (ou WooCommerce si tu préfères). Voir mon [guide eCommerce natif Tutor LMS](/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/).
5. **Inscrire à nouveau les apprenants** : export CSV depuis Masteriyo, import via Tutor LMS Tools (ou plugin User Import dédié).
6. **Période de double-run** : laisse Masteriyo actif pendant 2-4 semaines, le temps que tes apprenants se familiarisent avec la nouvelle interface.
7. **Bascule définitive** quand le nouveau système tourne sans accroc, puis désactivation Masteriyo.

### Données qui ne migrent pas automatiquement

- Avis cours (à reposter manuellement si pertinents)
- Historique de progression individuelle (à recréer ou à accepter de perdre)
- Certificats déjà délivrés (PDF à archiver côté apprenant)

### Quand ça vaut le coup, quand non

**Ça vaut le coup si** : tu prévois d'ajouter des subscriptions natives, des bundles, ou de scaler vers une marketplace multi-formateurs. Ce sont les angles où Tutor 3.0+ creuse l'écart.

**Ça ne vaut pas le coup si** : tu as un seul cours, peu d'apprenants, et la simplicité de Masteriyo te convient. Reste sur Masteriyo, ne migre pas pour migrer.

---

## Notes pour l'intégration

- **Liens internes** : pointer vers `/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/` (article principal Tutor LMS FR) sur le mot "Tutor 3.0+" ou "eCommerce natif".
- **CTA** : à la fin de cette section, soft-CTA vers le cloak `schoolswp.com/tutor-lms/` pour ceux qui veulent tester Tutor LMS Pro.
- **Longueur réelle** : ~310 mots (vs 300 visés). À ajuster selon contexte global.
- **Captures à ajouter** : 1-2 captures de l'écran "Tutor LMS > Tools" pour montrer le Migration Tool (même s'il ne couvre pas Masteriyo, ça illustre la philosophie de l'outil) - source possible : sprint corpus.
- **Disclaimer** : si plus tard Themeum ajoute Masteriyo au Migration Tool, mettre à jour cette section. À monitorer via le watcher `tools/check-tutor-docs-changes/check.ps1` (mémoire `reference_tool_tutor_docs_watcher.md`).
