# Audit FR — /comparaison-flyingpress-wp-rocket/

**Date** : 2026-05-26
**Post ID** : 52819
**Permalink** : <https://schoolswp.com/comparaison-flyingpress-wp-rocket/>
**Slug** : `comparaison-flyingpress-wp-rocket`
**Langue** : `fr` (Polylang)
**Statut** : publish
**Date publication** : 2024-06-05
**Dernière modification** : 2026-04-28
**Word count** : 2 095
**Translations Polylang** : `fr→52819 | en→343156 | de→343161`

---

## 1. Synthèse exécutive

**Verdict global** : ✅ **Article performant, à polir (pas à refondre)**.

| Axe | État | Action |
|---|---|---|
| SERP fr_FR | 🟢 Featured snippet #1 stable depuis mars 2026 | Protéger |
| On-page SEO Rank Math | 🟢 Title / meta / focus kw OK | OK |
| Schemas | 🟢 VideoObject + BlogPosting + FAQPage | OK |
| Body content | 🟡 2 095 mots, 19 H, FAQ 7 questions, sain | Densifier sur cas pratiques |
| Internal linking | 🟢 9 liens internes, ancres descriptives | Renforcer côté cocon cache |
| Featured image | 🔴 Metadata contient « 2024 » 3 fois | Patch evergreen |
| Brand compliance | 🔴 4 em-dash + 1 en-dash dans body | Patch BRAND_RULES |
| Conversion | 🟡 2 boutons Kadence (FlyingPress + WP Rocket) | OK, à monitorer |

**Position SERP `flyingpress vs wp rocket` (FR, France)** : **featured_snippet #1** + URL apparaît également en organic via le snippet, devant wp-rocket.me (vendor concurrent), mcstarters.com, wpkube, sayansamanta. Position stable sur les 3 snapshots historical_serp (2026-02-12 hors top 10 → 2026-03-27 #1 featured → 2026-05-12 #1 featured maintenu).

---

## 2. Rank Math on-page

### Métadonnées

| Champ | Valeur | Compliance |
|---|---|---|
| Post title | `FlyingPress vs WP Rocket ⚡ Lequel booste mieux WordPress ?` | ✅ Pas de dash, emoji modéré |
| RM title | `FlyingPress vs WP Rocket 2026 : verdict d'un pro WP (+ test)` | ✅ |
| RM description | `FlyingPress vs WP Rocket 2026 : benchmark réel, prix, compatibilité. Verdict d'un pro WordPress + guide pour migrer sans casser ton site (5 minutes).` | ✅ 168 chars, dans la cible |
| RM focus keyword | `flyingpress vs wp rocket,wp rocket vs flyingpress` | ✅ Alignement parfait avec query |
| Canonical | `(vide → auto)` | ✅ |
| Robots | `(vide → index, follow)` | ✅ |
| Pillar content | `(vide)` | 🟡 À évaluer (pas un pilier mais sub-cluster cache) |

### Schemas présents

- ✅ `rank_math_schema_VideoObject` (intro Presto Player)
- ✅ `rank_math_schema_BlogPosting`
- ✅ `rank_math_schema_FAQPage` (7 questions, toutes FR)

**FAQ FR (extraits)** :

1. Quel est le plugin le plus rapide entre FlyingPress et WP Rocket ?
2. FlyingPress est-il meilleur que WP Rocket ?
3. Est-ce que FlyingPress propose une version gratuite ?
4. WP Rocket est-il plus complet ?
5. Puis-je tester ces plugins avant achat ?
6. Quels sont les concurrents gratuits ?
7. Peut-on utiliser FlyingPress et WP Rocket ensemble ?

→ Cohérent EN J+14 (où Q5 a été patchée pour l'anglais : `Can I test these plugins before buying?`). Aucune action FAQ FR.

---

## 3. Structure éditoriale

### Headings (19 total)

```
H2 Benchmark : Le test de vitesse en conditions réelles
H2 Fonctionnalités clés : FlyingPress et WP Rocket au banc d'essai
  H3 Optimisation du chargement et Core Web Vitals
  H3 Mise en cache avancée
  H3 Optimisation des images et vidéos
  H3 Base de données et scripts
  H3 Interface et configuration
H2 Compatibilité : S'intègrent-ils bien à ton écosystème WordPress ?
H2 Tarification : Lequel offre le meilleur rapport qualité/prix ?
H2 Avantages et inconvénients : Le récapitulatif
H2 Avantages de FlyingPress
H2 Inconvénients de FlyingPress
H2 Points forts de WP Rocket
H2 Limites de WP Rocket
H2 Alternatives à FlyingPress et WP Rocket
H2 FAQ : Questions fréquentes
H2 Conclusion : Alors, FlyingPress ou WP Rocket pour ton site ?
  H3 Pour qui est FlyingPress ?
  H3 Pour qui est WP Rocket ?
```

**Lecture** : structure comparative classique, complète. Légère asymétrie : Avantages/Inconvénients en H2 plats au lieu de paires H2 → H3 sous-jacents (cf. la version DE qui utilise des H3 ✅). Pas bloquant pour le SEO.

**Gap potentiel** : pas de section « cas pratiques » par typologie de site (e-commerce WooCommerce, page builder Elementor/Divi) — alors que la version DE en a (même si bordélique en français résiduel). Hypothèse : enrichir le FR avec ces cas pratiques pourrait étendre la longue traîne.

---

## 4. Featured image

- **Attachment ID** : 52829
- **URL** : `/wp-content/uploads/2024/06/flyingpress-vs-wp-rocket-comparatif-2024.jpg`
- **Alt** : `Comparaison FlyingPress versus WP Rocket en 2024 par schoolsWP.` 🔴
- **Title** : `FlyingPress vs WP Rocket : Le guide comparatif 2024 pour les utilisateurs WordPress.` 🔴
- **Caption** : `Découvrez les avantages de FlyingPress sur WP Rocket dans notre analyse complète de 2024.` 🔴
- **Description** : `... pour choisir le meilleur plugin de performance WordPress en 2024. ... le guide, proposé par schoolsWP, est conçu pour aider les créateurs de sites WordPress à prendre une décision éclairée basée sur les avis et analyses les plus récents.` 🔴

🔴 **Violation evergreen** ([feedback_evergreen_slugs.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/feedback_evergreen_slugs.md)) : 4 occurrences de `2024` dans la metadata (alt, title, caption, 2× description).

**Action recommandée** : patch metadata via `update_post_meta` + `wpdb->update` sur l'attachment 52829 (même pattern que EN J+14, [J14-routine-outcome.md](../../flyingpress-wp-rocket-comparison-en/2026-05-26/J14-routine-outcome.md#3-featured-image-metadata-attachment-348847)) :

- Alt : `Comparaison FlyingPress versus WP Rocket par schoolsWP.`
- Title : `FlyingPress vs WP Rocket : Le guide comparatif pour les utilisateurs WordPress.`
- Caption : `Découvrez les avantages de FlyingPress sur WP Rocket dans notre analyse complète.`
- Description : retirer 2 occurrences `de 2024` + `en 2024`

**Bonus** : régénérer le visuel via le pipeline `tools/html-to-png/featured-images-flyingpress-wp-rocket/` (template `slide-flyingpress-vs-wp-rocket.html` brand-grade, déjà utilisé pour EN). Slug-cible attachment : conserver le chemin existant `/2024/06/flyingpress-vs-wp-rocket-comparatif-2024.jpg` ou push nouveau slug `flyingpress-vs-wp-rocket-wordpress-cache.jpg` (à arbitrer : le filename actuel n'est pas critique mais reste evergreen-incompatible).

---

## 5. Internal linking

**9 liens internes** détectés :

| URL | Anchor | Status |
|---|---|---|
| `schoolswp.com/flyingpress/` | `→ Tester FlyingPress` | ✅ Cloak affiliate |
| `schoolswp.com/wp-rocket` | `→ Voir WP Rocket` | ✅ Cloak affiliate |
| `schoolswp.com/flyingpress-avis/` | `avis FlyingPress complet` | ✅ Cocon FlyingPress |
| `schoolswp.com/quest-ce-que-wp-rocket-plugin` | `WP Rocket` | ✅ Cocon WP Rocket |
| `schoolswp.com/perfmatters-plugin-wordpress-pour-ameliorer-la-vitesse-de-son-site` | `Perfmatters` | ✅ Cocon perf |
| `schoolswp.com/nettoyer-base-de-donnees-wordpress` | `nettoyer les révisions d'articles` | ✅ Cocon DB |
| `schoolswp.com/flyingpress/` | `👀 Voir les offres FlyingPress` | ✅ CTA cloak |
| `schoolswp.com/wp-rocket` | `🔧 Découvrir les tarifs WP Rocket` | ✅ CTA cloak |
| `schoolswp.com/flyingpress-vs-perfmatters/` | `FlyingPress vs Perfmatters : concurrents ou complémentaires ?` | ✅ Cocon comparatif |

**Maillage cohérent** ✅. Pas de lien cassé, pas de chevauchement.

**Opportunités de maillage entrant** (à valider) :
- Article pilier « plugins cache » futur ([project_cache_plugins_pillar.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/project_cache_plugins_pillar.md)) → quand publié, lier vers cet article en sous-cluster
- Articles `flyingpress-avis/`, `quest-ce-que-wp-rocket-plugin/` → vérifier qu'ils linkent en retour vers ce comparatif

---

## 6. Brand compliance

| Règle | Constat | Action |
|---|---|---|
| Em-dash U+2014 interdit | 🔴 **4 occurrences dans body** | Remplacer par ` : ` ou ` - ` |
| En-dash U+2013 interdit | 🔴 **1 occurrence dans body** | Idem |
| Tutoiement | ✅ « ton site », « tu » présents | OK |
| Mots interdits (disruptif, hack...) | ✅ Aucun détecté | OK |
| `schoolsWP` capitalization | ✅ | OK |
| Liens affiliés sans `/go/` | ✅ 0 `/go/` paths | OK |
| Évite « 2024 » année figée | 🔴 2 occurrences body + 4 metadata image | Patch evergreen |

**Total brand violations** : 5 dashes + 6 mentions 2024 = 11 points à corriger via mu-plugin push pattern + update_post_meta image.

---

## 7. SERP — état du marché FR

**Live SERP `flyingpress vs wp rocket` (fr_FR, France, 2026-05-26)** :

| Pos | Type | Domaine | URL |
|---|---|---|---|
| **1 (FS)** | **featured_snippet** | **schoolswp.com** | **`/comparaison-flyingpress-wp-rocket/`** |
| 2 | organic | reddit.com | `r/Wordpress 9mo` |
| 3 | video pack | YouTube (4 vidéos) | GigaBits, Ask Simon, Site Starters, Amit Tiwari |
| 4 | organic | wp-rocket.me | `/flyingpress-vs-wp-rocket/` ⚠ |
| 5 | organic | mcstarters.com | `/blog/flyingpress-vs-wp-rocket/` |
| 6 | organic | wpkube.com | `/flyingpress-review/` |
| 7 | organic | sayansamanta.com | `/flyingpress-review/` |
| 8 | organic | wpdiscounts.io | `/blog/flyingpress-vs-wp-rocket-vs-nitropack/` |
| 9 | organic | wpalpha.io | `/flyingpress-review/` |

**Lecture stratégique** :

- 🏆 **Position 1 featured snippet maintenue** — c'est de la valeur SERP majeure (CTR ~30-40% sur un FS bien framé)
- ⚠ wp-rocket.me (le vendor concurrent direct) est en position 4 organic en anglais sur SERP FR → AI Overview susceptible de tirer ce contenu vendor ; bonne raison de maintenir l'autorité du contenu schoolsWP
- ⚠ Pas de page builder FR dans le top 10 (que des reviews internationales en anglais) → opportunité éditoriale : densifier le cas pratique « migration WP Rocket → FlyingPress en 5 minutes » qui peut prendre la position 2 organic
- ⚠ Video pack en position 3 → opportunité d'embed YouTube schoolsWP côté FR (cf. version EN avec VideoObject schema actif)

**Snapshot historical_serp** :

- 2026-02-12 : schoolsWP hors top 10
- 2026-03-27 : schoolsWP #1 featured snippet ✅ (montée significative entre fev et mars)
- 2026-05-12 : #1 featured snippet maintenu ✅

→ La position est neuve (3 mois) mais stable. Protéger en priorité.

---

## 8. DataForSEO — performance du domaine schoolswp.com sur le marché FR

(Voir [dataforseo-ranked-keywords-fr.json](./dataforseo-ranked-keywords-fr.json) — dump brut, et [Sheet Drive](https://drive.google.com/file/d/1gomlWLhIcJTajphZupQlN1wDcUf_SyE6y8UVzwwOlwU/view) — exploitable Sheets.)

- **100 keywords ranked** (cap DataForSEO)
- **25 keywords top 3** (dont `5euros com avis`, `buddyboss`, `wishlist member`)
- **75 keywords top 4-10**
- **Volume cumulé** : **32 550** searches/mois
- **0 featured snippet trackés dans l'export** (le FS sur "flyingpress vs wp rocket" n'apparaît pas dans l'API DataForSEO Labs ranked — c'est observé via SERP live)

**Keywords liés à la page cible présents dans l'export domain-wide** :

| Keyword | Rank | Volume | URL cible |
|---|---|---|---|
| flyingpress cloudflare | 5 | 90 | `/comparaison-flyingpress-wp-rocket/` |

→ La page capture surtout le focus principal via le FS (non tracké en organic rank). Hors FS, son organic dans l'export DataForSEO est limité à 1 keyword (long-tail). C'est un signal : la page tire toute sa visibilité du FS. **Si le FS tombe, on perd la quasi-totalité du trafic** — risque concentré.

### Keyword overview focus

| Keyword | Vol/mois | Trend Y | Difficulty | Intent |
|---|---|---|---|---|
| `flyingpress vs wp rocket` | 110 | -99% YoY ⚠ | (LOW) | commercial |
| `wp rocket vs flyingpress` | (idem cluster) | - | - | - |
| `flyingpress` | 480 | -33% | 9 | navigational |
| `wp rocket` | 2 900 | -33% | 7 | informational |
| `meilleur plugin cache wordpress` | 110 | -98% YoY ⚠ | (LOW) | commercial |
| `comparaison flyingpress wp rocket` | (n/a, pas retourné) | - | - | - |

**Lecture** :

- Le marché de la requête principale est en **décroissance forte YoY (-99%)** — pic 720/mois en juin 2025, retombé à 10/mois depuis juillet 2025. La position #1 actuelle (110/mois moy) reste valable mais le potentiel à 12 mois s'érode.
- `wp rocket` reste 2 900/mois en France → opportunité maillage interne depuis `/quest-ce-que-wp-rocket-plugin/` vers ce comparatif (la page WP Rocket capture le trafic informationnel et redirige vers le comparatif)
- `meilleur plugin cache wordpress` (110/mois, -98% YoY) → opportunité H2 explicite « Le meilleur plugin cache WordPress » au sein de l'article

---

## 9. Thruuu — audit comparatif SERP

**Statut** : ✅ **Lancé 2026-05-26**. Exports :

- Audit on-page : `Expor_audit_6a1567086d4d2c2ae024950b.docx` (audit ID `6a1567086d4d2c2ae024950b`)
- SERP analysis 17 résultats : `thruuu_export_flyingpress vs wp rocket_2026-5-26 (1).xlsx` (google.fr / fr / FR / 26 mai 2026)

### 9.1 Verdict thruuu on-page

| Check | Status | Détail thruuu |
|---|---|---|
| Wordcount | ✅ success | 2 511 mots (SERP avg 2 142) — dans la range |
| Image count | ✅ success | 14 images (SERP avg 14) — pile |
| Page Rank Score | ✅ success | 28 (SERP 35) — légèrement sous mais OK |
| Page freshness | ✅ success | « a month ago » (SERP avg 24 days) |
| Title length | ✅ success | 60 char |
| Title pixel width | ✅ success | dans la cible |
| Title contains exact keyword | ✅ success | « FlyingPress vs WP Rocket » match exact |
| Description length | ✅ success | 148 char |
| Questions in headings | ✅ success | 7 questions (SERP avg 2) — excellent |
| Unique angle in copy | ✅ success | « Verdict d'un pro WP » différenciant |
| Common headings missing | 🔴 error | 5 headings communs SERP absents de la page |
| Less frequent inspiration headings | 🔴 error | Outline pourrait s'enrichir |
| Most frequent terms | 🔴 error | Cluster terminologique sous-couvert (sur termes EN, voir 9.4) |

### 9.2 Position thruuu confirmée

| Pos | Type | Domaine | Word count | Page Rank | Images |
|---|---|---|---|---|---|
| **1** | **featured_snippet** | **schoolswp.com** | **2 519** | 7 690 822 | 14 |
| 2 | social | reddit.com | 77 | 279 | 2 |
| 3 | article | wp-rocket.me | 1 248 | 3 446 | 6 |
| 4 | video | (YouTube) | - | - | - |
| 5 | article | mcstarters.com | 2 390 | 8 325 475 | 2 |
| 6 | article | **webandseo.fr** 🇫🇷 | **3 885** | 30 290 941 | 44 |
| 7 | article | wpkube.com | 2 867 | 3 072 694 | 32 |
| 8 | article | wpdiscounts.io | 1 848 | 22 224 541 | 7 |
| 9 | article | sayansamanta.com | 3 790 | 9 589 046 | 15 |
| 10 | article | wpservice.pro | 2 512 | 1 350 657 | 10 |

**Featured snippet extract retenu par Google** :

> En résumé : FlyingPress est souvent plus simple à configurer, plus rapide dès l'activation et redoutable sur les Core Web Vitals. De son côté, WP Rocket propose plus de réglages avancés et une meilleur(e) [...nettoyer ta base de données]

→ Le passage souligné en featured snippet vient du H2 « Conclusion » + « Benchmark » — c'est là que Google a trouvé la réponse synthétique. **À protéger en priorité dans les patches P0.**

### 9.3 Concurrent #6 : webandseo.fr — opportunité

`webandseo.fr/flyingpress/` (`Avis FlyingPress 2026 : une meilleure alternative à WP Rocket ?`) — **3 885 mots, 44 images, page rank 30M** : c'est le seul gros concurrent FR natif dans le top 10, et il fait quasi 2× le word count de schoolsWP avec 3× plus d'images.

H2 de webandseo.fr qu'on n'a pas :

- « Avantages et inconvénients de FlyingPress »
- « Prix de FlyingPress »
- « L'utilité d'une extension comme FlyingPress »
- « La dernière création de Gijo Varghese »
- « FlyingCDN : le CDN intégré à FlyingPress »
- « Service client de FlyingPress »
- « Les meilleures alternatives à FlyingPress en 2026 »
- « Avis d'utilisateurs de FlyingPress »

→ Plusieurs sont déjà couverts sous une forme différente dans la version schoolsWP. Les vrais gaps : **FlyingCDN dédié**, **Gijo Varghese (créateur)**, **Avis utilisateurs** (témoignages).

### 9.4 Most Frequent Terms — analyse

Termes que schoolsWP **a** ✅ : flyingpress, wp, rocket, wp rocket, plugin, performance, wordpress, page, image, web, core web, web vitals, flyingpress vs, flyingpress vs wp, core web vitals, vs wp rocket, support.

Termes flaggés ❌ par thruuu mais qui sont **EN** (donc non-pertinents pour le FR) :
`it`, `if you`, `you can`, `flyingpress is`, `your website`, `of the`, `image optimization` (EN), `rocket is`, `the best`, `wp rocket is`.

→ **Ces 10 erreurs « Most frequent terms » sont des faux positifs** : Google a indexé schoolsWP en featured snippet sans avoir besoin de ces termes EN. Pas d'action.

### 9.5 Common headings missing (thruuu)

5 H2/H3 communs sur le SERP que schoolsWP n'a pas :

| Heading | Occurrences SERP | Recommandation |
|---|---|---|
| Flyingpress vs wp rocket | 4 | Présent sous forme adjacente (H1) — pas d'action |
| Wp rocket | 2 | Le H2 « Points forts de WP Rocket » couvre — OK |
| Nitropack | 2 | À considérer : section « Alternatives » pourrait nommer NitroPack |
| Table of contents | 2 | TOC : on n'en a pas en visuel mais Rank Math gère — à voir |
| Who should use flyingpress | 2 | On a déjà « Pour qui est FlyingPress ? » et « Pour qui est WP Rocket ? » — OK |

→ Faux positifs majoritaires. Seul gap réel : **mentionner NitroPack** dans la section Alternatives (1-2 lignes suffisent, sans changer de structure).

### 9.6 AI Recommendations thruuu (à arbitrer)

**Titres alternatifs proposés** :

- Comparatif 2026 : FlyingPress ou WP Rocket ?
- Meilleur plugin 2026 : FlyingPress contre WP Rocket
- FlyingPress vs WP Rocket : Le guide ultime 2026
- Quel plugin choisir en 2026 : FlyingPress ou WP Rocket ?
- 2026 : FlyingPress surpasse-t-il WP Rocket ?

→ Le titre actuel `FlyingPress vs WP Rocket 2026 : verdict d'un pro WP (+ test)` (60 chars) est jugé bon par thruuu. Pas de raison de changer (le FS détenu prouve que Google aime le wording).

**Outline enrichments proposés (AI)** :

- Témoignages d'utilisateurs (Ce que disent les utilisateurs)
- Comparaison des performances : Études de cas
- Les meilleures pratiques d'optimisation avec FlyingPress et WP Rocket
- Impact sur le SEO : Qu'est-ce qui est le mieux ?
- Comment choisir entre FlyingPress et WP Rocket ?
- Mise à jour de fonctionnalités : Ce qui a changé récemment
- Comparaison avec d'autres plugins de cache populaires
- Réponses aux préoccupations communes : Les mythes autour de FlyingPress et WP Rocket

→ **Pépite** : « Témoignages d'utilisateurs » et « Études de cas » sont absents de l'article, et c'est exactement ce que wp-rocket.me met en avant (`A Few Words from Users Who Tried Both Plugins`). Action P1 : ajouter une mini-section témoignages ou citer 2-3 retours utilisateurs en encart.

**Keywords additionnels suggérés** : optimisation performance, plugin wordpress, comparatif plugins, vitesse chargement, meilleur plugin, flyingpress avantages, wp rocket avis, configuration wp rocket, flyingpress configuration, plugin cache, optimisation images, performances web, caching wordpress, flyingpress test, wp rocket fonctionnalités, vitesse wordpress, analyse vitesse, plugins de cache, benchmark flyingpress, plugin vitesse, core web performance, meilleures pratiques wordpress, flyingpress performance, wp rocket alternatives, impact optimisation.

→ Globalement déjà couverts par le wording naturel de l'article. Pas d'action ciblée.

### 9.7 Search Volume thruuu (FR)

| Métrique | Valeur thruuu |
|---|---|
| Search Volume FR | 110/mois |
| Competition | LOW (index 25) |
| Pic monthly | 720 (mai 2025), 480 (juin 2025) |
| Plancher | 10/mois (juillet 2025 → avril 2026) |

→ Cohérent avec DataForSEO section 8. La page est positionnée mais l'érosion du marché est confirmée.

### 9.8 Related Searches (thruuu FR)

8 related extraites :

1. Flyingpress vs wp rocket reddit
2. FlyingPress pricing
3. WP Rocket Alternative
4. Super page Cache vs WP Rocket
5. WP Fastest Cache vs WP Rocket
6. WP Rocket pricing
7. Is WP Rocket worth it
8. SpeedyCache vs LiteSpeed Cache

→ Cluster opportunités longue traîne. `WP Rocket Alternative` (2 900/mois sur `wp rocket` parent) mérite un H3 « Alternatives à WP Rocket » dans la section Alternatives (action P1 light).

---

## 10. Recommandations priorisées

### P0 — Patch immédiat (sécurise le FS + brand compliance)

1. **Featured image** : patch metadata attachment 52829 (alt, title, caption, description) → retirer toutes les occurrences `2024` (cf. section 4 pour le wording cible). Pattern : `wpdb->update` + `update_post_meta('_wp_attachment_image_alt', ...)`.
2. **Body em-dash + en-dash** : retirer les 4 em-dash (U+2014) + 1 en-dash (U+2013) du `post_content`. Pattern : `wpdb->update wp_posts.post_content` (pas `wp_update_post` pour éviter `wp_unslash`, cf. [feedback_wp_update_post_unslash_kadence.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/feedback_wp_update_post_unslash_kadence.md)).
3. **Body 2024 → 2026** : 2 occurrences de `2024` dans le corps texte (hors metadata image). Localiser avec `grep -n 2024` après extraction du body, remplacer une par une.

### P1 — Densification éditoriale (étend la longue traîne)

4. **Section cas pratiques** : ajouter un H2 « Pour quel type de site WordPress ? » avec 2 H3 (e-commerce WooCommerce, page builder Elementor/Divi), inspiré de la version DE (mais en rédaction native FR, pas traduit). Cibles : `flyingpress woocommerce`, `wp rocket woocommerce`, `flyingpress elementor`.
5. **H2 explicite « meilleur plugin cache WordPress »** : capter le keyword secondaire (110/mois, -98% YoY mais résiduel).
6. **Embed YouTube** : ajouter un embed YouTube (si une vidéo schoolsWP existe ou peut être produite) pour challenger le video pack rang 3.

### P2 — Renforcement cocon (à coordonner avec article pilier futur)

7. **Article pilier cache** ([project_cache_plugins_pillar.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/project_cache_plugins_pillar.md)) : quand publié, lier vers ce comparatif depuis le H2 « Alternatives WP Rocket ». **Ne pas** lier depuis le H2 « Alternatives » des avis cache existants tant que le pilier n'est pas en place (cf. mémoire).
8. **Liens entrants** : vérifier que `flyingpress-avis/` et `quest-ce-que-wp-rocket-plugin/` linkent en retour vers ce comparatif (audit Link Whisper).

### P3 — Surveillance (KPI)

9. **GSC monitoring 14j** filtre page = `/comparaison-flyingpress-wp-rocket/` :
   - Cible : maintenir CTR ≥ 5% sur le FS (vs CTR organic top 1 ~30%)
   - Alert si position FS sort
   - Alert si CTR < 3% sur `flyingpress vs wp rocket` (signal AI Overview qui mange le FS)
10. **Re-audit J+30** (2026-06-25) : vérifier que les patches P0 ont été appliqués + que le FS est toujours détenu.

---

## 11. État avant patch (snapshot)

Voir données ci-dessus + dump brut [dataforseo-ranked-keywords-fr.json](./dataforseo-ranked-keywords-fr.json).

État final post-patch journalisé dans [state-after.json](./state-after.json).

---

## 12. Patches appliqués (J+0, 2026-05-26)

**Statut** : ✅ **P0 FR complet**. Routine exécutée par Claude Code cloud agent ~11:25.

### 12.1 Faux positifs documentés (NE PAS patcher)

L'audit initial avait flaggé 4 em-dash + 2 occurrences « 2024 » dans le body. **Audit affiné** :

| Catégorie | Count | Verdict | Raison |
|---|---|---|---|
| Em-dash U+2014 dans body | 4 | ❌ **NE PAS toucher** | Tous artefacts structurels Kadence : data-attributes (`USE_PARENT_DEFAULT_WIDTH`), accordion controls (`kt-blocks-accordion-icon-trigger`), JSON config (`displayShadow`). Non visibles à l'écran. Patcher casserait les blocs. |
| « 2024 » dans body | 2 | ❌ **NE PAS toucher** | Les 2 occurrences sont dans `"datePublished": "2024-06-05"` de 2 schemas JSON-LD Review (FlyingPress + WP Rocket). Date de publication originale légitime. `dateModified` déjà à 2026. Patcher casserait les rich results. |

### 12.2 Patches réellement appliqués

#### Attachment 52829 (featured image)

| Champ | Avant | Après |
|---|---|---|
| Title | `FlyingPress vs WP Rocket : Le guide comparatif 2024 pour les utilisateurs WordPress.` | `FlyingPress vs WP Rocket : Le guide comparatif pour les utilisateurs WordPress.` |
| Alt | `Comparaison FlyingPress versus WP Rocket en 2024 par schoolsWP.` | `Comparaison FlyingPress versus WP Rocket par schoolsWP.` |
| Caption | `Découvrez les avantages de FlyingPress sur WP Rocket dans notre analyse complète de 2024.` | `Découvrez les avantages de FlyingPress sur WP Rocket dans notre analyse complète.` |
| Description (occurences `2024`) | 1 | 0 ✓ |

Méthode : `$wpdb->update wp_posts` + `update_post_meta('_wp_attachment_image_alt', ...)`.

#### Body 52819 (post_content)

| Cible | Avant | Après |
|---|---|---|
| `alt=` d'image inline (1 en-dash U+2013) | `alt="flyingpress avis 2026 – plugin de cache WordPress..."` | `alt="flyingpress avis 2026 - plugin de cache WordPress..."` |
| SHA256 post_content | `e3adf3651cfd4f5a1f2f5c6058fd52eec9417a6bf68dbdcf89e367b6072fdac2` | `0fa586f0892f56af5974a997bbbc8cec7751698315842bd6aa8b71a2ea244d4f` |
| Diff bytes | - | -2 |
| En-dash count body | 1 | 0 ✓ |

Méthode : `$wpdb->update wp_posts.post_content` (pas `wp_update_post` pour éviter `wp_unslash`, cf. [feedback_wp_update_post_unslash_kadence.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/feedback_wp_update_post_unslash_kadence.md)).

### 12.3 Protection FS vérifiée intacte

- H2 Benchmark : `Benchmark : Le test de vitesse en conditions réelles` ✓ inchangé
- H2 Conclusion : `Conclusion : Alors, FlyingPress ou WP Rocket pour ton site ?` ✓ inchangé
- Paragraphes immédiatement post-H2 : non touchés (pas de patch dans ces zones)

### 12.4 Cache purges + verify prod

- FlyingPress hooks : `flying_press_purge_url`, `flying_press_purge_post`, `fp_purge_url` ✓
- FlyingPress disk : `index.html.gz` (94 955 b) + `index.json.gz` (15 585 b) supprimés manuellement ✓
- `clean_post_cache()` post + attachment ✓
- WP Rocket : non actif sur ce site

**Round-trip prod (`?nocache={ts}`)** :

| Check | Résultat |
|---|---|
| HTTP code | 200 |
| Body length | 433 348 bytes |
| Nouveau alt attachment présent | ✓ |
| Ancien `2024 par schoolsWP` absent | ✓ |
| Ancien en-dash `– plugin de cache` absent | ✓ |
| Nouveau tiret simple `- plugin de cache` présent | ✓ |

### 12.5 KPI baseline 2026-05-26 pour suivi J+14 / J+30

- Position SERP `flyingpress vs wp rocket` (fr_FR) : **#1 featured snippet** (stable depuis 2026-03-27)
- Target J+14 (2026-06-09) : maintenir #1 FS
- Target J+30 (2026-06-25) : re-audit complet + nouveau `state-after.json`
- Alerte si CTR < 3% sur query principale

Données complètes : [state-after.json](./state-after.json).

---

*Audit produit 2026-05-26 par Claude Code (cloud agent). Pattern : `content/audits/<slug>/<YYYY-MM-DD>/` ([reference_audits_registry.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/reference_audits_registry.md)). Cross-langues : [audit DE](../../flyingpress-wp-rocket-comparison-de/2026-05-26/audit.md), [trace EN J+14](../../flyingpress-wp-rocket-comparison-en/2026-05-26/J14-routine-outcome.md).*
