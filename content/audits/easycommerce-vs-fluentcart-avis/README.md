# easycommerce-vs-fluentcart-avis

- **URL** : `https://schoolswp.com/?p=2978852` (brouillon / non publie)
- **Post ID** : 2978852
- **Mot-cle cible** : easycommerce vs fluentcart
- **Statut** : refonte-appliquee-live (corrections appliquées sur le brouillon le 2026-06-21, reste en draft)

## Historique des snapshots

| Date                                 | Trigger                                                                    | Statut                 | Synthese                              |
| ------------------------------------ | -------------------------------------------------------------------------- | ---------------------- | ------------------------------------- |
| [2026-06-21](2026-06-21/synthese.md) | Demande Michael (audit SEO pre-publication + mot-cle, thruuu en parallele) | refonte-appliquee-live | [synthese.md](2026-06-21/synthese.md) |

## Refonte appliquée live (2026-06-21)

4 paliers appliqués sur le brouillon (backups postmeta base64 réversibles) : (1) catégorie E-commerce + tags + meta ; (2) tutoiement complet (vous 20→0) + heading FAQ FR + "sans effort"→0 ; (2.5) corrections factuelles (4,7 étoiles / 132 API / crédits / 25 % / 7 % / 3x softés ou attribués) ; (3) désambiguïsation + 2 disclosures affiliés + "pour qui" + Sources ; (4) 3 schemas JSON-LD (FAQPage + 2 SoftwareApplication). Image à la une déjà posée 21/06 (attach 2979807). Code promo schoolsWP20 conservé. Reste optionnel : images inline + recalcul Rank Math + retrait noindex à la publication.

## Quick win cluster - FAQPage sur /avis-fluentcart-wordpress/ (2026-06-22)

Action de cluster (cf. synthèse §11) : ajout d'un schema **FAQPage** (4 Q/R, reflétant mot pour mot l'accordéon Kadence visible) sur la page **post 1505872** `/avis-fluentcart-wordpress/` (live, ranke #8, n'avait aucun schema FAQ). Injecté en bloc `wp:html` en fin de contenu, backup `_schoolswp_faqschema_backup_20260622`. Piège résolu : `wp_update_post` dé-slashe le JSON → fix via `wp_slash()`. JSON validé stocké + rendu. Trace : `2026-06-21/_build_faqschema_fluentcart.py`.

## Pass brand complet sur /avis-fluentcart-wordpress/ (2026-06-22)

Suite à la demande de Michael (« respecter absolument le brand »), pass brand complet sur le post 1505872 (cf. synthèse §12) : **62 remplacements** (tutoiement complet, imperatifs, nous/notre, "sans effort", em-dash, "scalabilité"→"montée en charge"). Schema FAQPage **régénéré au tutoiement** (schema = texte visible). Texte visible 100% conforme (vous/votre/vos/nous/notre/sans-effort/em-dash/scalab = 0 ; seuls résidus = slugs d'ancre invisibles). Backup `_schoolswp_brand_backup_20260622`. Trace : `_build_brand_pass_fluentcart.py` + `_brand_pairs.b64` + `_brand_schemablock.b64`.

## Vérification Google + alerte de suivi (2026-06-22)

Rich Results Test : 3 éléments valides (Article, Breadcrumb, Organisation), 0 erreur. **FAQPage non listé = normal** (dépréciation Google 2023) mais confirmé présent en live (cf. synthèse §13). **Alerte mensuelle posée** : workflow n8n `uxCImeo2jFONMk5O` (Schedule `17 9 22 * *` → Telegram bot FluentCart) qui rappelle de vérifier GSC + indexation + citation GEO vs baseline de juin.

## Resume

Brouillon de 3261 mots, bonne base (structure 8 H2 / 10 H3, table comparative, 14 liens internes). Mot-cle cible a **0 volume** (FR & US) : asset GEO + cluster + first-mover, pas un play volume. schoolsWP ranke deja page 1 (pos ~7) sur le champ FluentCart via `/avis-fluentcart-wordpress/`.

Bloquants avant publication : 0 schema JSON-LD, 0 image, categorie "Non classe", vouvoiement massif (20 "vous"), heading FAQ en anglais, "sans effort" x2, disclosure affilies absente.

GEO (thruuu integre) : schoolsWP cite par **Google AI Mode (2x)** mais **absent de ChatGPT & Gemini** ; easycommerce.dev domine le narratif LLM (ChatGPT 3x / Gemini 4x). Benchmark SERP : concurrents ~2300-2600 mots avec 10-67 images ; seul EDD (#3) a un FAQPage schema. Cible GEO = se faire citer par ChatGPT & Gemini (schema + desambiguisation EasyCommerce + FAQ extractible).

## Livrables

- Google Sheet : `schoolsWP - Volumes SEO - EasyCommerce vs FluentCart - 2026-06-21` (Drive)
- `2026-06-21/synthese.md`, `audit-onpage.csv`, `seo-volumes-google-sheet.csv`, `dataforseo-serp-fr.json`, `geo-citations.csv`, `article-current-snapshot.html`, `thruuu-raw/serp-analysis.xlsx`
