# Brief de fin de session - 2026-06-02

> Sujet : article EN « Is it possible to learn WordPress in a day? » (famille de traduction EN/FR/DE).
> 3 chantiers enchaînés : image à la une + table Ninja, audit SEO, puis consolidation du doublon.

## 1. Image à la une + table Ninja EN (brouillon 2289537)

- Hero EN neuf créé : `assets/featured-images/post-2289537/slide-00-hero-en.html` → att **2969739** (titre interrogatif « in a day? »). Posé sur le brouillon 2289537 (remplaçait un vieux JPG 2289681 hors charte).
- Table FR `2114069` (planning 8h) doublée en table EN **2969740** (colonnes Time Slot / Goal / Key Tasks) ; shortcode + attribut bloc Gutenberg swappés dans le brouillon.

## 2. Audit SEO + DataForSEO (snapshot 2026-06-02)

- Dossier : `content/audits/learn-wordpress-one-day/2026-06-02/` (snapshot article, dumps DataForSEO + GSC, CSV volumes, synthèse).
- **DataForSEO (US/EN)** : cible exacte « learn wordpress in a day » = 10/mo (faible). Valeur réelle = cluster (`learn wordpress` 480, `is wordpress hard to learn` 90, `how long to learn` 40) + AEO/AI Overview. SERP = AI Overview + video pack + forums + 2 formations payantes → intention mixte info/transac, CTA formation aligné.
- **GSC** : URL publiée « Discovered - currently not indexed », 0 traction 90j.
- **Google Sheet Drive** créé : « schoolsWP - Volumes SEO - learn wordpress in a day - 2026-06-02 ».
- **Obsidian** : synthèse proposée déposée dans `00_systeme/claude-code-bridge/syntheses-proposees/`.
- **thruuu** : à fournir par Michaël (`thruuu-raw/`), non bloquant.

## 3. Constat critique + décision : doublon EN/DE (Option A, fusion)

- Découverte : le brouillon 2289537 était un **doublon** de l'article EN **publié** 2274708 (`/en/learn-wordpress-in-a-day/`). Même schéma DE (brouillon 2289536 vs publié 2274709).
- À l'inspection, les **publiés étaient déjà supérieurs** (2274708 : 2828 mots, 3 images, table EN propre 2901083, focus keyword correct).
- **Option A exécutée** (décision Michaël) :
  - Doublons **en corbeille** : 2289537 (EN) + 2289536 (DE). Table EN redondante 2969740 en corbeille.
  - **Groupe Polylang réparé** (le trash l'avait scindé) → en:2274708 / fr:2112488 / de:2274709.
  - Hero 2969739 d'abord porté sur 2274708, puis **revert** vers le hero validé **2968995** (Michaël ; finalement non bloquant). État final = 2968995. 2969739 reste en médiathèque.

## 4. Indexation

- Michaël a **demandé l'indexation** de `/en/learn-wordpress-in-a-day/` via GSC (Test en ligne 2026-06-02 09:33 : « Google a accès à cette URL », page indexable, fil d'Ariane valide, indexation demandée).

## État final live (prod)

| Élément                              | État                                                                      |
| ------------------------------------ | ------------------------------------------------------------------------- |
| EN canonique 2274708                 | publié, image à la une **2968995**, table EN 2901083, indexation demandée |
| FR 2112488 / DE 2274709              | inchangés, groupe Polylang correct                                        |
| Doublons 2289537 (EN) + 2289536 (DE) | corbeille                                                                 |
| Table redondante 2969740             | corbeille                                                                 |

## Suivi / reste à faire (non bloquant)

- Surveiller l'**indexation** (Discovered → Indexed) sur les prochains jours.
- Optionnel post-indexation : ajouter 2-3 **liens internes entrants** EN vers 2274708, envisager un **FAQPage schema** (FAQ en prose actuellement), densifier le maillage.
- Déposer l'export **thruuu SERP** dans `thruuu-raw/` si tu veux compléter le snapshot.
- Prochain snapshot d'audit : mesurer premières impressions/positions GSC sur le cluster.

## Artefacts & traces

- Audit : `content/audits/learn-wordpress-one-day/` (README + snapshot 2026-06-02 + `_registry.md`).
- Sources hero : `assets/featured-images/post-2289537/`.
- Drive : Google Sheet volumes (lien dans le README/synthèse).
- Obsidian : `syntheses-proposees/2026-06-02-audit-seo-learn-wordpress-in-a-day-EN.md`.
- Mémoire ajoutée : `reference_polylang_trash_breaks_group` (footgun trash + groupe Polylang).
