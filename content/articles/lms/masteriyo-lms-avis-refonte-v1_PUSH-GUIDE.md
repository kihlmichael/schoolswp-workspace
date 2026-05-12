---
parent: masteriyo-lms-avis-refonte-v1.md
type: push-guide
date: 2026-05-07
target_url: https://schoolswp.com/masteriyo-lms-avis/
---

# Guide de push WP — masteriyo-lms-avis refonte v1.1

Ce guide détaille les étapes pour pousser la refonte v1.1 sur l'article publié `/masteriyo-lms-avis/` de schoolswp.com. Le push se fait en mode manuel via l'éditeur Gutenberg (Code editor) puisque le MCP Novamira n'est pas exposé dans la session courante.

## Pré-requis

- Backup HTML article actuel : `content/articles/lms/_backup/2026-05-07_masteriyo-lms-avis-original.html` (97 KB, fait 2026-05-07)
- Draft final markdown : `masteriyo-lms-avis-refonte-v1.md` (4362 mots)
- HTML Gutenberg-ready : `masteriyo-lms-avis-refonte-v1_gutenberg-ready.html` (45 KB)
- Snippet schema Review : `content/decisions/masteriyo-arbitrage-2026-05-06_schema-review-snippet.md`

## Étape 1 — Backup additionnel via Gutenberg (5 min)

Avant tout push, capturer le contenu actuel sur WP :

1. Aller dans wp-admin et ouvrir l'article `/masteriyo-lms-avis/` en édition
2. Top right Gutenberg : trois petits points → Editeur de code (Code editor)
3. Tout sélectionner et copier
4. Coller dans `content/articles/lms/_backup/2026-05-07_masteriyo-lms-avis-gutenberg-original.html`
5. Repasser en Editeur visuel

Note : ce backup est complémentaire du backup HTML curl. Il préserve la structure Gutenberg native incluant les blocs Kadence custom des CTAs actuels.

## Étape 2 — Push du nouveau contenu (10 min)

1. Toujours dans Gutenberg, repasser en Editeur de code
2. Effacer tout le contenu existant
3. Ouvrir `masteriyo-lms-avis-refonte-v1_gutenberg-ready.html` dans VS Code
4. Tout copier
5. Coller dans l'éditeur de code Gutenberg
6. Ne pas sauvegarder encore. Repasser en Editeur visuel
7. Vérifier visuellement :
   - Hero image en haut (logo Masteriyo)
   - Encadré "À retenir" en blockquote
   - Image principale Masteriyo
   - 13 H2 + 35 H3 dans la TOC
   - 13 images Masteriyo en place
   - Tableau récap 6 LMS x 10 critères
   - Section "Pourquoi je suis passé à Tutor LMS" (NEW)
   - Section "Migration Masteriyo vers Tutor LMS" (NEW)
   - FAQ 7 questions

## Étape 3 — Ré-insérer les CTAs Kadence (10 min)

Le HTML Gutenberg-ready contient 4 commentaires HTML marqueurs CTA. Ces commentaires sont des placeholders, pas des blocs Kadence fonctionnels. Tu dois remplacer chaque commentaire par un vrai bloc Kadence :

### CTA 1 - après la section "Pourquoi je suis passé à Tutor LMS"

Juste après le paragraphe italique de disclosure affiliée :

- Ajouter un bloc Kadence Advanced Button (palette9 vers palette1, gradient 135 deg, flèche fas_arrow-right, shadow + hover inversion)
- Texte : "Tester Tutor LMS 3.0+"
- URL : https://schoolswp.com/tutor-lms/ (cloak interne ClickWhale, headers sponsored)
- Pattern : voir mémoire `feedback_kadence_cta_template.md`

### CTA 2 + 3 - fin de la section "Mon verdict final"

Juste après le paragraphe italique de disclosure affiliée :

- CTA principal Kadence Advanced Button : "Tester Tutor LMS 3.0+" vers https://schoolswp.com/tutor-lms/
- CTA secondaire Kadence Advanced Button (style soft) : "Découvrir Masteriyo" vers https://schoolswp.com/masteriyo/

Important : copier les blocs Kadence depuis le backup Gutenberg étape 1 plutôt que de les recréer from scratch. Ça garantit que le styling reste identique au reste du site.

## Étape 4 — Title + meta description Rank Math (5 min)

Saisie manuelle Gutenberg (cf. mémoire `feedback_rank_math_via_plugin_only.md`).

Sidebar Rank Math :

- Title (60 chars max, < 580 px) : `Masteriyo LMS Avis 2026 : je suis passé à Tutor LMS`
- Meta description (155 chars max) : `J'ai testé Masteriyo LMS pendant 6 mois. Voici ses points forts, ses limites pour mes besoins, et pourquoi je suis passé à Tutor LMS sur schoolsWP.`
- Focus keyword : `masteriyo lms avis` (préserve l'asset position 4.5)
- Vérifier le score SEO Rank Math, viser 80+

Avant de sauvegarder : vérifier le rendu pixels du title via un outil SERP snippet checker. Cible : <580 px (l'ancien faisait 586,4 px et était tronqué).

## Étape 5 — Schema Review (15 min)

Cause du problème : aucun schema Review/Product dans le `@graph` actuel. Solution complète + snippet JSON-LD prêt à coller dans `content/decisions/masteriyo-arbitrage-2026-05-06_schema-review-snippet.md`.

Méthode rapide :

1. Sidebar Rank Math, onglet Schema
2. Bouton Add Schema, choisir Review
3. Remplir les champs avec les valeurs du snippet (note 4,5/5 personnelle, itemReviewed = SoftwareApplication Masteriyo LMS, reviewBody court)
4. Save

## Étape 6 — Vérifications avant publication (5 min)

Avant de cliquer Mettre à jour :

- Toutes les images chargées correctement
- CTAs Kadence visuels conformes au reste du site
- Tableau récap LMS rendu correctement (6 colonnes)
- Aucune coquille flagrante (relecture rapide)
- Title pixels-safe vérifié
- Score Rank Math > 80
- Schema Review configuré

## Étape 7 — Publication + GSC re-crawl (5 min)

1. Cliquer Mettre à jour
2. Vider le cache LiteSpeed/FlyingPress (réflexe schoolsWP)
3. Aller sur https://schoolswp.com/masteriyo-lms-avis/ en navigation privée pour vérifier le rendu live
4. Aller sur GSC, URL inspect /masteriyo-lms-avis/, Tester l'URL en direct, Demander une indexation
5. Vérifier https://search.google.com/test/rich-results et attendre que Review apparaisse dans les types détectés (peut prendre 1-3 semaines pour le rich snippet réel)

## Étape 8 — Update audit + snapshot baseline (5 min)

1. Update `content/audits/masteriyo-lms-avis/README.md` : passer le statut à `publie`, ajouter ligne dans l'historique
2. Programmer un snapshot J+30 (autour de 2026-06-07) dans `content/audits/masteriyo-lms-avis/2026-06-07/`
3. Ajouter un trigger remote (skill schedule) pour rappel du snapshot J+30 (optionnel)

## Plan de rollback

Si le push casse quelque chose en production :

### Rollback rapide via Gutenberg

1. Repasser en Editeur de code
2. Effacer tout
3. Coller le contenu de `content/articles/lms/_backup/2026-05-07_masteriyo-lms-avis-gutenberg-original.html` (le backup étape 1)
4. Mettre à jour

### Rollback via WP Revisions

WP garde automatiquement les révisions. Sidebar Document, Révisions, choisir la révision pré-push, Restaurer.

### Rollback via fichier HTML curl (dernier recours)

Le fichier `_backup/2026-05-07_masteriyo-lms-avis-original.html` contient le HTML rendu (pas du Gutenberg). À utiliser uniquement si Revisions et backup Gutenberg sont indisponibles, en re-créant manuellement les blocs depuis le HTML.

## Après publication — actions de suivi

| Action | Quand | Comment |
| --- | --- | --- |
| Vérifier indexation GSC | J+1 | URL inspect /masteriyo-lms-avis/, attendre coverage Submitted and indexed |
| Vérifier Review rich snippet | J+7 à J+21 | Test Rich Results, GSC URL inspect rich_results detected_types |
| Vérifier positions queries | J+30 | GSC search analytics 30j sur les 8 queries du baseline |
| Snapshot J+30 | 2026-06-07 | Nouveau dossier `content/audits/masteriyo-lms-avis/2026-06-07/` + `_diff.md` |
| Mesurer CTR delta | J+30 | Cible : 0% à 3-8% |
| Conversions affiliate | J+30 | Tracking ClickWhale /tutor-lms/ |
| Audit cluster perdants enchaîné | si bande passante | mission `cluster-perdants-arbitrage` (Tunnel vente, EasyCommerce, SEOKEY) |

## Estimation effort total

- Étape 1 (backup) : 5 min
- Étape 2 (push) : 10 min
- Étape 3 (CTAs Kadence) : 10 min
- Étape 4 (Rank Math) : 5 min
- Étape 5 (Schema Review) : 15 min
- Étape 6 (vérifs) : 5 min
- Étape 7 (publication + GSC) : 5 min
- Étape 8 (update audit) : 5 min

Total : 60 min (1h focus).

## Si tu préfères industrialiser

Si à terme tu veux automatiser ce flux pour tous les articles (refonte v2, v3, autres avis), on peut :

1. Créer un tool `tools/wp-push-refonte/cli.py` qui pousse via WP REST API natif (App Password Michael KIHL Pro) ou via le mu-plugin Novamira
2. Le tool gère : backup pre-push, push content, schema injection, vérification post-push
3. Pattern réutilisable sur les 7+ articles d'avis schoolsWP qui ont probablement le même bug schema
