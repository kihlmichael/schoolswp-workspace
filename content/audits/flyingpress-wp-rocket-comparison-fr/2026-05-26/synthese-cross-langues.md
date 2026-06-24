# Synthèse cross-langues — FlyingPress vs WP Rocket (FR / DE / EN)

**Date** : 2026-05-26
**Articles** :

- 🇫🇷 [FR — `/comparaison-flyingpress-wp-rocket/`](./audit.md) (post 52819)
- 🇩🇪 [DE — `/de/vergleich-flyingpress-wp-rocket/`](../../flyingpress-wp-rocket-comparison-de/2026-05-26/audit.md) (post 343161)
- 🇬🇧 [EN — `/en/flyingpress-wp-rocket-comparison/`](../../flyingpress-wp-rocket-comparison-en/2026-05-26/J14-routine-outcome.md) (post 343156, refondu 2026-05-12, patches J+14 2026-05-26)

---

## 0. Mise à jour J+30 (2026-06-25) - bilan tri-langues live

> Bloc ajouté le 2026-06-25 (re-audit J+30 DE, capture 2026-06-24). Tout ce qui suit ce bloc est le snapshot d'origine du 2026-05-26, conservé tel quel. SERP live refaite sur les 3 langues (action P3 #15 de ce document).

**Position live `flyingpress vs wp rocket` au 2026-06-24 (DataForSEO serp_organic_live_advanced)** :

| Langue   | Position schoolsWP au 2026-05-26 | **Position au 2026-06-24 (live)**                                                    | Lecture                                                                                                                                     |
| -------- | -------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 🇫🇷 fr_FR | 🏆 #1 featured snippet           | 🏆 **#1 organique** (devant wp-rocket.me)                                            | Maintenu. Pas d'AI Overview observé.                                                                                                        |
| 🇩🇪 de_DE | 🔴 Absent top 12                 | 🏆 **#1 organique** (devant wp-rocket.me + tous les EN)                              | **Gain majeur** : la refonte DE native a converti. Détail : [audit DE J+30](../../flyingpress-wp-rocket-comparison-de/2026-06-25/audit.md). |
| 🇬🇧 en_US | ~pos 4-5 (J+14)                  | 🔴 **Absent de la page 1 (top ~11)** + **AI Overview actif sans citation schoolsWP** | À creuser dans un re-audit EN dédié (régression possible ou pos 12-30). Gap GEO EN.                                                         |

**Lecture stratégique** :

- L'hypothèse du 2026-05-26 (« 9/12 du top SERP DE est en anglais : opportunité réelle pour un contenu DE natif frais ») est **validée** : le contenu DE natif a pris la #1 sur une SERP anglo-dominée et vieillissante.
- **FR et DE tiennent tous les deux la #1.** L'asymétrie de performance suit toujours l'asymétrie de qualité produit, mais DE a rattrapé FR.
- **Point de vigilance EN** : schoolsWP n'est plus visible en page 1 EN et l'AI Overview en_US (actif) cite wp-rocket.me, commercegurus, onlinemediamasters, wpservice, Reddit, LinkedIn mais **pas schoolsWP**. C'est le seul des 3 marchés où l'AIO est servi, et schoolsWP n'y est pas éligible. Recommandation : programmer un re-audit EN dédié (position exacte + travail GEO pour viser la citation AIO).

**Correctifs DE appliqués au J+30** (decision Michael, capture J-1) :

- P1 : retrait du résiduel evergreen « 2025 » dans la description de l'attachment 350864 (backup postmeta `_schoolswp_bak_att_desc_20260624`).
- P2 : mu-plugin `schoolswp-affiliate-cloaks.php` v1.1.1 -> v1.2.0 : les variantes localisées `/de|en|fr/flyingpress/` et `/wp-rocket/` (auparavant 301 cassé vers une review) sont normalisées vers le slug canonique pour que ClickWhale gère le redirect (tracking + nofollow/sponsored préservés). **Cela résout le risque transversal n°4 de la section 6 ci-dessous** (« Cloak affiliate : vérifier que /flyingpress/ et /wp-rocket/ routent correctement depuis /de/... Polylang-aware »). Backup wp_option `schoolswp_bak_mu_affiliate_cloaks_20260624`.

---

## 1. État SERP comparé

| Langue   | Volume keyword principal      | Position schoolsWP                                  | Visibilité top 10 | AI Overview                |
| -------- | ----------------------------- | --------------------------------------------------- | ----------------- | -------------------------- |
| 🇫🇷 fr_FR | 110/mois (-99% YoY)           | **🏆 #1 featured snippet** stable depuis 2026-03-27 | ✅ Présent        | Non observé live           |
| 🇬🇧 en_US | (à mesurer J+14 post-refonte) | (en cours de monitoring J+14, baseline ~pos 4-5)    | ✅ Présent        | À monitorer                |
| 🇩🇪 de_DE | 10/mois (-50% YoY)            | 🔴 **Absent top 12**                                | 🔴 Absent         | ⚠ AI Overview asynch actif |

**Lecture** :

- L'asymétrie de performance suit exactement l'asymétrie de qualité produit. FR a le contenu le plus mûr (2024 → patches successifs), EN a été refondu il y a 14 jours, DE a été dupliqué de FR sans traduction.
- Le marché FR est en décroissance (-99% YoY) mais schoolsWP y détient une position de force (FS). Le marché DE est minuscule (10/mois) mais 9/12 du top SERP est en anglais : l'opportunité est réelle pour un contenu DE natif frais.

---

## 2. État on-page comparé

| Axe                          | FR (52819)           | DE (343161)                                  | EN (343156)                                  |
| ---------------------------- | -------------------- | -------------------------------------------- | -------------------------------------------- |
| Status                       | publish              | publish                                      | publish                                      |
| Word count                   | 2 095                | 1 304 (mais FR pur)                          | (~équivalent EN traduit)                     |
| Last modified                | 2026-04-28           | 2026-05-13                                   | 2026-05-26                                   |
| Langue body                  | ✅ FR natif          | 🔴 **FR (déclaré DE)**                       | ✅ EN natif (post-refonte)                   |
| Post title langue            | ✅ FR                | 🔴 FR                                        | ✅ EN                                        |
| RM title langue              | ✅ FR                | 🔴 FR                                        | ✅ EN                                        |
| RM meta langue               | ✅ FR                | 🔴 FR                                        | ✅ EN                                        |
| Headings 19                  | ✅ FR                | 🔴 FR                                        | ✅ EN                                        |
| FAQ schema                   | ✅ 7 Q&A FR          | ✅ 7 Q&A DE (seule partie traduite)          | ✅ 7 Q&A EN (Q5 patché 2026-05-26)           |
| Schemas (Video / Blog / FAQ) | ✅✅✅               | ✅✅✅                                       | ✅✅✅                                       |
| Featured image               | 🔴 metadata « 2024 » | 🔴 metadata « 2025 » + en-dash               | ✅ patché 2026-05-26 (sans année, sans dash) |
| Internal links count         | 9 (vers FR)          | 4 (3 vers FR + 1 affilié externe ancre vide) | (à recompter)                                |
| Kadence buttons (CTA)        | 2                    | **0**                                        | (à recompter)                                |
| Em-dash dans body            | 4 🔴                 | 0 ✅                                         | 0 ✅ (patché)                                |
| En-dash                      | 1 body 🔴            | 1 title 🔴                                   | 0 ✅                                         |
| Cloak affiliate `/go/`       | 0 ✅                 | 0 ✅ (mais 1 lien direct externe)            | 0 ✅                                         |

---

## 3. Forces transversales

1. **Schema layer cohérent** : VideoObject + BlogPosting + FAQPage présents sur les 3 langues. Pas de chantier schema à mener cross-langues.
2. **FAQ schema réellement traduit en DE** : seul vrai signal de traduction sur le post DE. Inversion : sur FR/EN les FAQ sont récents ; sur DE elles étaient (involontairement) en avance.
3. **Maillage de marque** : `/flyingpress/` et `/wp-rocket/` sont des slugs cloak universels qui fonctionnent pour les 3 langues (Polylang-aware via mu-plugin schoolswp-affiliate-cloaks).
4. **Structure éditoriale DE** : (paradoxe) le post DE — bien que rédigé en FR — a une **meilleure architecture** que le FR original : H3 imbriqués sous Avantages/Inconvénients + cas pratiques par typologie de site. **Cette structure est à rétro-fitter sur le FR en P1**.

---

## 4. Gaps transversaux

### 4.1 Brand compliance evergreen (3 langues)

- 🔴 **EN** : était en avance jusqu'à 2026-05-26 (4 patches J+14 dont featured image sans « 2025 » et sans dash) → ✅ état actuel propre
- 🔴 **FR** : metadata image contient 4× « 2024 » + body contient 4 em-dash + 1 en-dash + 2× « 2024 » résiduels → **à patcher**
- 🔴 **DE** : metadata image contient « 2025 » + 1 en-dash dans post_title + 1 en-dash dans image title → **à patcher**

**Pattern de patch unifié** : `wpdb->update` sur `wp_posts.post_content` et `wp_posts.post_title` + `update_post_meta('_wp_attachment_image_alt', ...)` + `wpdb->update` sur attachment post_title/post_excerpt/post_content. Idéntique au pattern EN J+14 ([J14-routine-outcome.md](../../flyingpress-wp-rocket-comparison-en/2026-05-26/J14-routine-outcome.md)).

### 4.2 Featured image visuelle

Le pipeline brand existe déjà : `tools/html-to-png/featured-images-flyingpress-wp-rocket/` ([reference_html_to_png_tools.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/reference_html_to_png_tools.md)) + template `slide-flyingpress-vs-wp-rocket.html` brand-strict (vert #00D400, Inter, sans date).

→ Une seule régénération (1920x1080, JPG q=92) **peut servir aux 3 langues** : on garde un visuel evergreen unique multilingue. Slugs/permalinks d'attachment différents (1 par langue Polylang), mais même fichier source HTML.

**Action P1** : régénérer le visuel une fois, propager via 3 uploads multipart Novamira (pattern J+14 confirmé pour EN).

### 4.3 Internal linking DE → DE

- FR linke vers FR (9 liens cohérents)
- EN linke vers EN (à vérifier post-refonte 2026-05-12)
- DE linke **vers FR** (3 liens internes pointent slug FR sans `/de/`)

🔴 **Conséquence** : aucun signal d'écosystème DE pour Google. La page DE est orpheline du cluster DE.

**Action P0 DE** : recâbler les 3 liens internes DE vers leurs équivalents `/de/...` quand ils existent, sinon laisser FR (mieux qu'un lien cassé).

### 4.4 Conversion CTA

| Langue | Boutons Kadence            |
| ------ | -------------------------- |
| FR     | 2 ✅                       |
| EN     | (à recompter post-refonte) |
| DE     | **0** 🔴                   |

**Action P0 DE** : ajouter 2 boutons Kadence brand-strict (palette9/1, gradient #00D400 vert) vers `/flyingpress/` et `/wp-rocket/`. Pattern : [reference_kadence_email_button_pattern.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/feedback_kadence_cta_template.md).

### 4.5 Structure éditoriale FR pauvre vs DE

Le DE (en français) a une structure plus moderne : cas pratiques par typologie de site (WooCommerce, page builder).

**Action P1 FR** : refactorer le FR pour ajouter ces H2 « Cas pratiques » avec H3 pour e-commerce et page builder. C'est un enrichissement éditorial, pas une refonte (le contenu actuel reste valable).

---

## 5. Hiérarchie d'actions cross-langues

### 🔴 P0 (semaine du 2026-05-26)

**Routine FR** (patch on-the-fly) :

1. Patch attachment 52829 (retirer 4× « 2024 » de alt/title/caption/description)
2. Patch `wp_posts.post_content` post 52819 (retirer 4 em-dash + 1 en-dash + 2× « 2024 »)
3. Cache purges (flying_press_purge_post, fp_purge_url, rocket_clean_post, clean_post_cache)
4. Re-soumettre Inspect URL GSC

**Routine DE** (refonte) :

1. **Décision Michaël** : confirmer Option A (refondre body en DE natif). Si Option B/C, alors les étapes suivantes deviennent caduques.
2. Si Option A : commander traduction native via Traduire Sans Migraine + relecture, ou faire traduire le brief par un LLM (Claude / Gemini DE) puis relecture humaine.
3. Patch post_title + RM title + RM meta_description en DE natif.
4. Patch les 19 headings (mapping suggéré dans [audit DE section 5](../../flyingpress-wp-rocket-comparison-de/2026-05-26/audit.md#5-structure-éditoriale--19-headings-tous-en-français)).
5. Patch attachment 350864 (retirer en-dash + « 2025 »).
6. Ajouter 2 boutons Kadence brand-strict.
7. Remplacer lien affilié direct par cloak `/flyingpress/`.
8. Recâbler 3 liens internes FR → DE équivalents.
9. Cache purges + Inspect URL GSC.

**Pas d'action EN** : EN a déjà reçu ses patches J+14 le 2026-05-26.

### 🟡 P1 (semaine du 2026-06-02)

10. **Régénérer le visuel featured brand** via tools/html-to-png/, propager aux 3 attachments (52829 FR, 348847 EN déjà fait, 350864 DE).
11. **Enrichir structure FR** avec H2 « Cas pratiques » (WooCommerce, page builder).
12. **Lancer thruuu sur DE** post-refonte pour calibrage SERP top 10.

### 🟢 P2 (semaine du 2026-06-09)

13. **Article pilier cache plugins** (cf. [project_cache_plugins_pillar.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/project_cache_plugins_pillar.md)) : créer le hub pilier, lier les 3 langues vers ce comparatif.
14. **Audit Link Whisper** : vérifier que `/flyingpress-avis/`, `/quest-ce-que-wp-rocket-plugin/`, `/flyingpress-vs-perfmatters/` linkent en retour vers le comparatif.

### 🔵 P3 (re-audit J+30, 2026-06-25)

15. Refaire SERP live FR + DE + EN.
16. Comparer position FR (FS #1 maintenu ?), DE (entrée top 30 ?), EN (KPI J+14 mesurés ?).
17. Lancer `state-after.json` dans chacun des 3 dossiers d'audit pour clôturer la boucle.

---

## 6. Risques transversaux à surveiller

1. **AI Overview EN + DE** : si AIO commence à servir une réponse directement sans clic vers la page, le FS #1 FR est protégé tant que France n'active pas l'AIO sur cette query (à monitorer mensuellement).
2. **Décroissance du marché** : `flyingpress vs wp rocket` est en -99% YoY FR et -50% YoY DE. Si la tendance continue, le ROI éditorial diminue. Garder le contenu evergreen pour absorber le résiduel + servir les requêtes longue traîne (`flyingpress vs wp rocket reddit`, `wp rocket alternatives`, `meilleur plugin cache wordpress`).
3. **Cohérence Polylang** : si on bouge l'un des 3 posts, vérifier que la triade `pll_get_post_translations` reste cohérente (52819 ↔ 343156 ↔ 343161).
4. **Cloak affiliate** : vérifier que `/flyingpress/` et `/wp-rocket/` routent correctement depuis `/de/...` (Polylang-aware ? sinon créer `/de/flyingpress/` et `/de/wp-rocket/` côté mu-plugin schoolswp-affiliate-cloaks).
5. **CTR FS FR** : un FS bien framé donne 30-40% CTR. Vérifier mensuellement le CTR query `flyingpress vs wp rocket` filtre page `/comparaison-flyingpress-wp-rocket/` dans GSC. Alerte si CTR < 15% (signe d'AIO ou de FS perdu).

---

## 6 bis. Validation thruuu (2026-05-26)

Les audits thruuu (lancés sur les deux URLs en cours d'audit) **confirment indépendamment** les diagnostics on-page de la section 4 et apportent 4 insights additionnels :

### 6 bis.1 Asymétrie SERP confirmée par thruuu

| Métrique thruuu           | FR                            | DE                                        |
| ------------------------- | ----------------------------- | ----------------------------------------- |
| Position détectée         | **#1 featured_snippet** ✅    | Absent top 20 (✘ sur la page 1 google.de) |
| Word count schoolsWP      | 2 511 mots (SERP avg 2 142) ✓ | 1 742 mots (SERP avg 1 974) borderline    |
| Image count               | 14 (SERP avg 14) ✓            | **5 (SERP avg 20)** 🔴                    |
| Title length              | 60 chars ✓                    | 72 chars 🔴 (cible <60)                   |
| Title pixel               | OK                            | 656.6 px 🔴 (cible <580)                  |
| Meta desc length          | 148 ✓                         | 228 🔴 (cible <160)                       |
| Questions in headings     | 7 (SERP avg 2) ✓              | 10 (SERP avg 1) ✓                         |
| Page Rank Score           | 28 vs SERP 35 — sous mais OK  | 28 vs SERP 38 — sous                      |
| « SERP very competitive » | non flagué                    | **oui** 🔴                                |

→ thruuu valide le verdict opérationnel : **FR à polir / DE à refondre**. Les 4 erreurs critiques DE (title trop long, meta trop longue, images sous-couvertes, SERP très compétitif) sont objectivement mesurables.

### 6 bis.2 Featured snippet FR — l'extrait retenu

Google sert ce passage comme featured_snippet sur `flyingpress vs wp rocket` (fr_FR) :

> En résumé : FlyingPress est souvent plus simple à configurer, plus rapide dès l'activation et redoutable sur les Core Web Vitals. De son côté, WP Rocket propose plus de réglages avancés et une meilleur(e) [...nettoyer ta base de données]

→ **L'extrait vient du H2 Conclusion + H2 Benchmark.** Toute modification de ces deux H2 + leur paragraphe d'amorce **mettrait le FS en péril**. À documenter dans le runbook P0 FR pour les patches body em/en-dash : ne pas toucher au texte du H2 Conclusion ni de la première phrase du H2 Benchmark.

### 6 bis.3 Concurrents à benchmarker (révélés par thruuu)

**FR pos 6 — `webandseo.fr/flyingpress/`** : 3 885 mots, **44 images**, page rank 30M. Seul vrai concurrent FR natif dans le top 10. H2 manquants chez schoolsWP : FlyingCDN dédié, Gijo Varghese (créateur), Avis utilisateurs (témoignages).

**DE pos 14 — `dowebwork.de/wp-rocket-einstellungen/`** : 5 405 mots, **65 images**, contenu fleuve **uniquement sur les réglages WP Rocket**. Indication stratégique forte : la SERP DE valorise les contenus **réglages techniques + Q&A** (vs SERP FR qui valorise le comparatif synthétique). Pour percer en DE, ajouter une section **« Optimale Einstellungen »** avec sous-sections Cloudflare, Autoptimize, WP Super Cache.

**DE pos 6 — `techboys.de/flyingpress-review`** : 2 602 mots, 37 images, structure proche d'un test/review. Benchmark direct de positionnement (rang 6 atteint avec contenu 2023 jamais mis à jour).

### 6 bis.4 Wording DE prêt à l'emploi (livré par thruuu AI)

**Titles DE proposés (60 chars cibles, 0 dash, 0 année figée)** :

- `FlyingPress oder WP Rocket: Beste Cache-Lösung 2026?`
- `WP Rocket vs FlyingPress: Welcher ist der Beste?`
- `Caching im Vergleich: FlyingPress oder WP Rocket?`
- `FlyingPress & WP Rocket: Tests und Preisvergleiche 2026`
- `FlyingPress gegen WP Rocket: Die beste Wahl für Websites?`

**Meta descriptions DE proposées (< 160 chars)** :

- `Entscheide zwischen FlyingPress und WP Rocket! Vergleiche Geschwindigkeit, Funktionen und Preise für deine optimale WordPress-Performance.`
- `FlyingPress oder WP Rocket? Finde heraus, welches Caching-Plugin deine Website schneller macht. Jetzt vergleichen!`

**Vocabulaire DE manquant à intégrer dans la refonte body** :

Funktionen, Cache-Plugin, Geschwindigkeit, Nutzer/Benutzer, Bildoptimierung, Performance-Plugin, kostenlos, Optimierung, Ladezeiten, Bewertung.

→ **L'AI thruuu a déjà mâché le brief de traduction DE** : ces extraits sont à passer tels quels au traducteur (humain ou LLM DE natif) pour brand-stricter la refonte. Économie estimée : 30-60 min de brief.

### 6 bis.5 Insights enrichissement contenu — pour les 3 langues

Thruuu a remonté pour les **deux** versions les mêmes sections **manquantes** :

- **Témoignages utilisateurs** (Ce que disent les utilisateurs / What users say) — absent FR + DE, présent en force chez wp-rocket.me (« A Few Words from Users Who Tried Both Plugins »)
- **Études de cas** (Performance comparison case studies) — absent FR + DE
- **NitroPack** mentionné explicitement (déjà cité comme alternative mais sans H3 dédié)

→ Trois enrichissements P1 cross-langues qui doivent figurer dans la **structure éditoriale cible** (à appliquer en DE post-refonte, et en FR en P1 polish).

---

## 7. Arborescence audits

```
content/audits/
├── flyingpress-wp-rocket-comparison-en/
│   ├── 2026-05-12/                 ← push refonte EN initiale (J+0)
│   │   ├── state-before.json
│   │   ├── state-after.json
│   │   ├── decision.md
│   │   ├── patch-body-en.md
│   │   ├── payload-pairs.json
│   │   ├── live-fr-blocks.json
│   │   ├── sheet-v5-build.csv
│   │   └── ... (8 artefacts pipeline refonte)
│   └── 2026-05-26/
│       └── J14-routine-outcome.md  ← routine J+14 + patches (body FR résiduel + FAQ Q5 + featured image)
│
├── flyingpress-wp-rocket-comparison-fr/
│   └── 2026-05-26/                 ← audit créé aujourd'hui
│       ├── audit.md
│       ├── synthese-cross-langues.md  ← ce fichier
│       └── dataforseo-ranked-keywords-fr.json
│
└── flyingpress-wp-rocket-comparison-de/
    └── 2026-05-26/                 ← audit créé aujourd'hui
        ├── audit.md
        └── dataforseo-ranked-keywords-de.json
```

---

## 8. Decision required de Michaël

| #   | Question                                          | Options                                 | Recommandation                                                     |
| --- | ------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------ |
| 1   | Patcher FR P0 (image + dashes + 2024 résiduels) ? | GO / SKIP                               | **GO** — risque bas, protège FS                                    |
| 2   | Refondre DE en allemand natif ?                   | A (refondre) / B (noindex) / C (delete) | **A** — cohérent avec marché DE (34 keywords ranked schoolswp.com) |
| 3   | Régénérer visuel brand cross-langues ?            | GO / SKIP                               | **GO P1** — pipeline existant, faible coût                         |
| 4   | Enrichir FR avec H2 cas pratiques ?               | GO / SKIP                               | **GO P1** — bénéfice longue traîne                                 |
| 5   | Re-audit J+30 (2026-06-25) ?                      | GO / SKIP                               | **GO** — verrouille la boucle                                      |

---

_Synthèse produite 2026-05-26 par Claude Code (cloud agent). Source de vérité = les 3 audits référencés en tête._
