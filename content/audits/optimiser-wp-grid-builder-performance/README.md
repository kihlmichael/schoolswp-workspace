# optimiser-wp-grid-builder-performance - index audits

- **URL** : https://schoolswp.com/?p=2969994 (brouillon, FR) - slug `optimiser-wp-grid-builder-performance`
- **post_id** : 2969994
- **Mot-clé cible** : `optimiser wp grid builder` / `wp grid builder core web vitals` (0 volume isolé mesuré)
- **Pilier** : performance / cache (WP Grid Builder)
- **Statut courant** : `refonte-decidee` (Option B : asset GEO/AEO standalone)

## Historique des snapshots

| Date                                                     | Trigger                           | Sources                                | Décision                                              | Synthèse                                                                      |
| -------------------------------------------------------- | --------------------------------- | -------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------- |
| [2026-06-04](2026-06-04/keyword-data-dfs-ubersuggest.md) | Demande Michaël (pré-publication) | DataForSEO + Ubersuggest + thruuu (×2) | Garder en asset GEO standalone, optimiser citation IA | [keyword-data-dfs-ubersuggest.md](2026-06-04/keyword-data-dfs-ubersuggest.md) |

## Résumé du dernier audit (2026-06-04)

Angle « optimisation perf / CWV » = **0 volume Google** (DataForSEO + Ubersuggest). Mais **divergence SEO contre GEO** : Google lit « optimiser wp grid builder » comme du tuto/review, les moteurs IA le lisent comme une question de **performance** (WP Rocket, LiteSpeed, Imagify cités). L'avis schoolsWP classe déjà **#4-5** sur les requêtes WPGB, d'où un risque de cannibalisation pour un standalone SEO.

**Décision (Option B)** : garder 2969994 comme **asset GEO/AEO**, optimisé pour la citation moteur IA (sections par métrique LCP/INP/CLS, réglages WPGB, écosystème d'outils, FAQ + schema FAQPage), intent différencié de l'avis, maillage croisé serré avec `/avis-wp-grid-builder/`.

## Actions

- [x] 2026-06-04 : audit data (DataForSEO + Ubersuggest + thruuu ×2), Google Sheet, décision Option B
- [x] 2026-06-04 : refonte GEO appliquée via WP REST (fallback, Novamira instable). Snapshot avant : [current-draft-snapshot.html](2026-06-04/current-draft-snapshot.html) ; version poussée : [new-draft.html](2026-06-04/new-draft.html). **Vérifié en prod** : blocs Kadence + CSS intacts, Ninja Table préservée, structure équilibrée.
  - [x] Tutoiement complet (article était 100 % vouvoiement) + nettoyage balises `<meta charset>` parasites
  - [x] Section H2 « Comment mesurer l'impact » (PageSpeed, GTmetrix, Lighthouse, Web Vitals, Query Monitor)
  - [x] Outils images dans section LCP (Imagify, ShortPixel, WebP/AVIF)
  - [x] LiteSpeed Cache ajouté (section cache)
  - [x] Lien interne article -> `/avis-wp-grid-builder/`
  - [ ] **FAQPage schema** (accordéon Kadence présent mais sans schema) : postmeta Rank Math -> nécessite Novamira (REST ignore la meta RM)
  - [ ] **Meta description** encore en vouvoiement (« ralentit votre site ? Corrigez... ») -> tutoiement, postmeta Rank Math -> Novamira
  - [ ] Lien réciproque avis -> article : à poser **après publication** (sinon lien vers un brouillon)
- [x] 2026-06-04 : 2 boutons CTA Kadence (template advancedbtn + singlebtn, gradient hex brand `#00d400 -> #00a100`, icône flèche, `_blank`) pointant vers le cloak ClickWhale `/wp-grid-builder/` (-> wpgridbuilder.com/?ref=648). Emplacements : mi-article avant le H2 « Choisir la bonne méthode de chargement », et juste avant la FAQ. Vérifié en prod : 2 advancedbtn / 2 singlebtn / 2 liens cloak, gradient hex rendu, **0 fuite `u002d`**, blocs équilibrés, Ninja Table préservée.
- [x] 2026-06-04 : catégorie corrigée `Non classé` (1095) -> **`WP Grid Builder` (2510)**, sous « Design & Constructeurs de pages » (1688), cohérente avec l'avis publié 2942620 (même catégorie). La taxonomie schoolsWP est organisée par plugin (pas par thème), donc l'angle perf reste classé sous le plugin.
- [ ] Captures d'écran du plugin à intégrer (liste fournie à Michaël le 2026-06-04 : indexeur, lazy load Card Builder, taille image carte, cache facettes, chargement conditionnel des assets, mode de pagination, Flyout mobile). Réglages image obligatoires : centré + lien aucun + légende visible en italique.
- [ ] Validation humaine avant publication (article toujours en brouillon)

> Word count après refonte : ~1890 mots (modeste ; pour un asset GEO la citabilité prime sur la longueur).

> Données détaillées : [2026-06-04/keyword-data-dfs-ubersuggest.md](2026-06-04/keyword-data-dfs-ubersuggest.md). Google Sheet (DFS + Ubersuggest) : [lien](https://docs.google.com/spreadsheets/d/1bF1IzgCq7x7ArfYREycUKVbCOTbibKsfOF_1nqVWwN8/edit).
