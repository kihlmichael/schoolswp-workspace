# Audit SEO : TablePress vs WP Table Builder (brouillon)

- **Article** : post `2881499` - "TablePress vs WP Table Builder : le comparatif 2026"
- **URL** : https://schoolswp.com/?p=2881499 (statut : **brouillon**)
- **Slug** : `tablepress-wp-table-builder-comparatif`
- **Mot-clé cible** : `tablepress wp table builder` (focus keyword Rank Math actuel)
- **Date audit** : 2026-05-14
- **Trigger** : demande Michael (audit pré-publication)
- **Sources** : contenu WP (Novamira), thruuu SERP export 2026-05-14, DataForSEO (Google Ads + Labs)

> **Avertissement données thruuu** : thruuu a scrapé l'URL `?p=2881499` alors que l'article est en brouillon. Il a donc analysé une **page 404** (titre "404 - Oups !", 30 mots, 2 images). Tout le fichier DOCX `audit-article` est **inexploitable** (les "erreurs" sont celles du 404, pas de l'article). Seul le **XLSX SERP** est valide et utilisé ici.

---

## 1. Verdict stratégique (à lire en premier)

**Le mot-clé cible n'a quasiment aucun volume de recherche en France.**

| Mot-clé | Volume FR/mois | Tendance an. | KD | Intention |
| --- | --- | --- | --- | --- |
| `tablepress vs wp table builder` | aucune donnée (~0) | - | - | - |
| `tablepress wp table builder` | aucune donnée (~0) | - | - | - |
| `tablepress` | 110 | **-47 %** | 29 | transactionnelle |
| `wp table builder` | 20 | **-50 %** | 53 | transactionnelle |
| `plugin tableau wordpress` | 10 | -50 % | 48 | transactionnelle |
| `créer tableau wordpress` | 10 | - | - | informationnelle |

Tout le champ sémantique est en **déclin marqué** (-47 % à -50 % sur 12 mois). Le mot-clé exact "vs" ne génère pas de données mesurables.

**Conséquences :**
- L'article ne ramènera **pas de trafic SEO direct significatif**. Sa valeur réelle = **article satellite de cluster** : il complète le maillage "tableaux WordPress" (avec `/ninja-tables-avis.../`), couvre la longue traîne et les requêtes de marque, et peut capter du GEO/AIO (réponses IA).
- **Décision recommandée : publier OUI** (coût faible, complète le cocon), **mais ne pas y investir de netlinking** ni d'effort de scaling. C'est un article de complétude, pas un pilier.
- **La SERP FR ne contient AUCUN vrai comparatif "X vs Y"** : elle est dominée par les pages outils (wordpress.org, tablepress.org), des tutoriels (WPMarmite) et des listicles (IONOS, GravityKit, wpmet, Ninja Tables). L'intention dominante est navigationnelle/transactionnelle. Le format "comparatif" est donc un **angle différenciant** mais légèrement décalé par rapport à l'intention réelle - d'où l'intérêt d'ajouter une dimension "tuto / comment faire" (voir §5).

---

## 2. Bloquants techniques (à corriger AVANT publication)

> **Correction 2026-05-14 (post-audit)** : l'item 1 d'origine (« tableau Ninja Tables vide ») était un **faux positif** de l'audit. La première vérification interrogeait le mauvais emplacement de stockage (`get_post_meta '_ninja_table_rows'`) ; les lignes Ninja Tables sont en réalité dans la table SQL `wp_ninja_table_items`. La table `2893460` contient **4 lignes** (Mode mobile, Facilité de réglage, Rendu visuel, Accessibilité). Elle n'est donc **pas vide** et n'est **pas un bloquant**. L'enrichissement reste recommandé (voir §5).

| # | Problème | Gravité | Action |
| --- | --- | --- | --- |
| 1 | ~~Tableau Ninja Tables vide~~ → **FAUX POSITIF** (cf. encadré ci-dessus). La table `2893460` contient 4 lignes ; elles sont juste **succinctes** (réponses d'un mot : « Sobre », « Automatique »...). | 🟢 Enrichissement | Étoffer la table de 4 → ~10-12 lignes avec des critères plus parlants (prix, import/export, perf, version gratuite, support, idéal pour...). Non bloquant. |
| 2 | **Meta Rank Math vides** - `rank_math_title` vide, `rank_math_description` vide. Score Rank Math : **31/100**. | 🔴 Critique | Renseigner dans la sidebar Rank Math (jamais via REST/SQL - règle projet). Valeurs proposées au §4. |
| 3 | **Catégorie "Non classé"** | 🟠 Important | Classer dans une vraie catégorie (probablement `Design WordPress` ou une catégorie "Plugins"). |
| 4 | **0 image dans le corps** (la moyenne SERP est de 22 images/page) | 🟠 Important | Ajouter 2-3 captures réelles : interface TablePress (type tableur), interface WP Table Builder (glisser-déposer), éventuellement un écran de prix. Métadonnées SEO via le pipeline `tools/wp-media-upload/`. |
| 5 | **8x `<meta charset="utf-8">` parasites** injectés dans les titres/paragraphes des accordéons FAQ (résidu de copier-coller) | 🟡 Mineur | Nettoyer les 8 occurrences dans les blocs `kadence/pane`. |
| 6 | Accordéon colonne 2 : `paneCount:3` déclaré mais **2 panes** réellement présents | 🟡 Mineur | Corriger `paneCount` à 2 ou ajouter le 3e pane (recommandé : ajouter une question, voir §5). |

---

## 3. Conformité éditoriale / branding (bloquant)

| # | Problème | Action |
| --- | --- | --- |
| 1 | **Vouvoiement systématique** - 34 occurrences (`vous` ×8, `votre` ×10, `vos` ×16). schoolsWP impose le **tutoiement**. L'article entier est en "vous", sauf 1 "toi" isolé dans le H2 de la FAQ → incohérence + violation de marque. | Convertir **tout** l'article en tutoiement (`vous`→`tu`, `votre`→`ton/ta`, `vos`→`tes`). |
| 2 | **Voix "nous/notre"** - "Nous comparons ici", "Résumé de **notre** comparaison", "**Notre** recommandation". schoolsWP = **"je"** (Michael seul derrière la marque, E-E-A-T). | Convertir en "je / mon / ma" : "Résumé de **mon** comparatif", "**Ma** recommandation", "**Je** compare ici...". |
| 3 | **Insertion forcée du mot-clé** - "Nous comparons ici **tablepress wp table builder**" : exact-match maladroit en minuscules, nuit au naturel et à la lisibilité. | Reformuler : "Je compare ici **TablePress et WP Table Builder** pour identifier...". |

✅ **Points propres** : 0 em-dash, 0 en-dash, 0 mot interdit (`disruptif`, `game changer`, `sans effort`, etc.). Densité mots-clés naturelle (`tablepress` ×35, `wp table builder` ×29, bien répartis).

---

## 4. SEO on-page

| Élément | État | Recommandation |
| --- | --- | --- |
| **Titre** | "TablePress vs WP Table Builder : le comparatif 2026" (~50 car.) | Bon (2 entités présentes). À reprendre tel quel dans Rank Math title. |
| **Rank Math title** | ❌ vide | Renseigner : `TablePress vs WP Table Builder : le comparatif 2026` |
| **Rank Math description** | ❌ vide (l'extrait WP est rempli mais pas le champ Rank Math) | Renseigner, en tutoiement : `Tu hésites entre TablePress et WP Table Builder pour tes tableaux WordPress ? Compare performance, design et prix pour bien choisir.` (~150 car.) |
| **Slug** | `tablepress-wp-table-builder-comparatif` | ✅ Conforme (pas d'année, pas de "schoolswp"). |
| **Structure Hn** | 8 H2 + 9 H3, pas de H1 dans le corps (correct : le titre = H1) | ✅ Logique et complète. |
| **Longueur** | 1 906 mots (moyenne SERP : 2 714) | Un peu court. Viser **2 400-2 700 mots** via les enrichissements du §5. |
| **Maillage interne** | 4 liens, tous valides, tous FR (règle Polylang ✅) : `ninja-tables-avis` (post ✅), `tastewp-avis` (post ✅), `design-wordpress` (archive **catégorie** ✅), `performance-wordpress` (archive **catégorie** ✅) | OK. Note : 2 liens pointent vers des **archives de catégorie** plutôt que des articles piliers - acceptable mais préférer un article pilier si disponible (transmet plus de pertinence topique). |
| **Liens sortants** | ❌ 0 | Les concurrents en ont. Ajouter 1-2 liens sortants d'autorité (`tablepress.org`, `wordpress.org/plugins/wp-table-builder/`) en `target="_blank"` → rassure E-E-A-T. |
| **FAQ** | 5 questions en accordéons Kadence | Bien. ⚠️ Vérifier le **schema FAQPage** : les accordéons Kadence ne sont pas auto-détectés par Rank Math. Si pas de schema FAQ généré, l'ajouter (bloc FAQ Rank Math ou schema manuel). |
| **Image à la une** | ✅ présente (`tablepress-vs-wp-table-builder-comparatif.jpg`) | OK. |

---

## 5. Gaps de contenu vs SERP (enrichissements recommandés)

La SERP FR couvre des sujets absents de l'article. Recommandations par priorité :

1. **Étoffer le tableau comparatif** (cf. §2.1) - la table `2893460` a 4 lignes très succinctes ; passer à ~10-12 lignes avec des critères plus parlants (prix, import/export, perf, version gratuite, support, idéal pour...).
2. **Ajouter une section "Comment créer ton premier tableau"** - mini-tuto par plugin (3-4 étapes chacun). L'intention "how to use" / "installation" est **très présente dans la SERP** (WPMarmite, library.illinois.edu, docs WP Table Builder). Cela rapproche l'article de l'intention réelle et ajoute ~400-500 mots.
3. **Ajouter 2-3 captures d'écran** (cf. §2.4).
4. **Compléter la FAQ** (passer de 5 à 6 questions, ce qui résout aussi le bug §2.6). Idées issues des "related searches" thruuu :
   - "TablePress ou WP Table Builder : lequel est gratuit ?"
   - "Quelles alternatives à TablePress et WP Table Builder ?" (renvoyer vers `ninja-tables-avis`)
5. **Mini-section "Et les alternatives ?"** - la SERP mentionne beaucoup Ninja Tables / wpDataTables. L'article cite déjà Ninja Tables en lien ; un court paragraphe dédié renforcerait la couverture sémantique.

✅ **Respect du concurrent** : l'article est équilibré - il donne des cas d'usage clairs et valorisants pour **chaque** plugin (TablePress = données massives/technique, WP Table Builder = design/affiliation). Conforme à l'esprit BRAND_RULES 31. Bon point.

**Termes fréquents SERP sous-exploités** (à intégrer naturellement) : `responsive`, `import/export`, `shortcode`, `CSS`, `pagination`, `tri/filtrage`, `Elementor` (compat page builders).

---

## 6. Données DataForSEO (→ Google Sheet)

Volumes extraits le 2026-05-14 (localisation France, langue fr). Détail dans :
- `dataforseo-synthese-mots-cles.csv` (10 mots-clés : volume, concurrence, CPC, KD, intention, tendance)
- `dataforseo-volume-mensuel-12mois.csv` (historique 12 mois pour les 4 mots-clés ayant des données)
- `gws-batchupdate-payload.json` (payload prêt à pousser vers Google Sheets)

✅ **Google Sheet créé** le 2026-05-14 sur le Drive de Michael : [schoolsWP - Volumes SEO - TablePress vs WP Table Builder](https://docs.google.com/spreadsheets/d/1EP6BNsGLTN17hWYC-HdWGwCtRljnsRNlVqo3AspmF6k/edit) (1 onglet, 2 tableaux : synthèse 10 mots-clés + historique mensuel 12 mois). Créé via le connecteur Google Drive de claude.ai — la CLI `gws` est HS (token OAuth révoqué, `invalid_grant` ; `gws auth login` n'a pas suffi, `credentials.enc` inchangé → re-auth gws à investiguer séparément).

---

## 7. Plan d'action (ordre d'exécution)

**Avant publication :**
1. 🔴 Renseigner Rank Math title + description (valeurs §4).
2. 🔴 Convertir tout l'article en tutoiement + voix "je" + reformuler le mot-clé forcé de l'intro.
3. 🔴 Nettoyer les 8 `<meta charset>` parasites + corriger `paneCount`.
4. 🟠 Classer dans une vraie catégorie.
5. 🟠 Ajouter 2-3 captures d'écran.
6. 🟢 Étoffer la table Ninja Tables `2893460` (4 lignes → ~10-12, critères plus parlants).
7. 🟡 Ajouter 1-2 liens sortants d'autorité + vérifier le schema FAQ.
8. 🟢 (Optionnel mais recommandé) Enrichir à ~2 400-2 700 mots (section tuto + FAQ + alternatives).

**Hors article :**
9. Créer le Google Sheet DataForSEO après re-auth `gws`.

**Stratégique :** ne pas planifier de netlinking sur cet article (volume trop faible). Le garder comme satellite du cluster "tableaux WordPress".
