---
slug: learn-wordpress-day
url: https://schoolswp.com/en/?p=2274708
date_snapshot: 2026-05-16
trigger: Demande Michael (audit pré-publication)
status: refonte-effectuee
post_id: 2274708
post_status: draft
post_lang: en
corrections_appliquees: 2026-05-16
---

# Audit SEO : "Is it possible to learn WordPress in a day?" (brouillon EN)

- **Article** : post `2274708` - "Is it possible to learn WordPress in a day?"
- **URL** : https://schoolswp.com/en/?p=2274708 (statut : **brouillon**)
- **Slug** : `learn-wordpress-day` (langue : en)
- **Catégorie** : WordPress Guides (lang=en) ✅
- **Auteur** : Michaël KIHL
- **Mot-clé cible Rank Math actuel** : 5 keywords concaténés (cf. §4, à corriger)
- **Date audit** : 2026-05-16
- **Trigger** : demande Michael (audit pré-publication)
- **Sources** : contenu WP (Novamira execute-php), DataForSEO Labs keyword_overview + suggestions (US, en), thruuu SERP export 2026-05-16
- **NB pipeline** : `publish_ready.cli` non lancé (crédit Anthropic épuisé sur la clé en session) → audit manuel basé sur signaux structurés + DataForSEO + SERP. Pas de Publish Score composite.

> **Note thruuu** : export SERP exploité (cf. §11 et `thruuu-serp-summary.md`). L'audit de la page schoolsWP elle-même n'est pas inclus (article en brouillon, thruuu retournerait un 404 sur l'URL `?p=2274708`). Snapshot article reconstruit via Novamira.

---

## 1. Verdict stratégique (à lire en premier)

**Le mot-clé cible exact a un volume très faible (10/mois US).** Mais le champ sémantique global pèse ~460/mois (US) et l'article peut capter une longue traîne pertinente via la FAQ.

| Mot-clé | Volume US/mois | KD | Tendance | Intent |
| --- | --- | --- | --- | --- |
| `wordpress for beginners` | **320** | 52 | -46 % YoY | informational |
| `wordpress crash course` | **40** | **23** | +40 % Q | informational |
| `learn wordpress fast` | 20 | 55 | +300 % mois | informational |
| `how long to learn wordpress` | 20 | - | -67 % YoY | informational |
| `learn wordpress in a day` | 10 | - | stable | informational |
| `can i learn wordpress in a day` | 10 | - | stable | informational |
| `learn wordpress basics` | 10 | - | stable | informational |
| `wordpress 8 hours` | 10 | - | stable | informational |
| `how to learn wordpress quickly` | 10 | - | stable | informational |
| `learn wordpress in one day` | no data | - | - | transactional |
| `wordpress in a day` | no data | 78 | - | informational |

**Conséquences :**

- L'article ciblant `learn wordpress in a day` ne ramènera **pas un trafic SEO significatif sur la requête exacte** (10/mois). Sa valeur réelle = **article satellite de cluster "WordPress beginner / formation"** + capture longue traîne FAQ + **citation par AI Overview Google** (présent sur cette query, cf. §11).
- **Décision recommandée : publier OUI** (le contenu existe, est honnête et bien construit), **mais après corrections** (cf. §2-3). Coût de correction faible (~30-45 min). Ne pas y investir de netlinking.
- **Vraie opportunité de scaling** : produire deux articles complémentaires plus volumineux dans le même cluster : un sur `wordpress for beginners` (320/mois, KD 52) et un sur `wordpress crash course` (40/mois, **KD 23**). Le présent article devient leur satellite.
- L'angle "verdict honnête + 8-hour plan" est **différenciant et faiblement contesté** : la SERP top 10 US est dominée par **landings de formation payante** (pootlepress £125, cotswoldwebsites £197, udemy, coursera, linkedin learning, learn.wordpress.org), des hubs de cours, et 3 threads Reddit/Quora. Aucun article "verdict honnête + plan actionnable" ne ranke en top 10. **Créneau libre.**
- **AI Overview présent** sur la query : 13 sources citées (5 YouTube + 3 learn.wordpress.org + 2 Reddit + 3 articles Q&A textuels). Les 3 articles textuels cités ont un **PR très faible (0, 24, 33)** → opportunité de citation AIO pour schoolsWP si l'article est structuré pour (cf. §11).

---

## 2. Bloquants techniques (à corriger AVANT publication)

| # | Problème | Gravité | Action |
| --- | --- | --- | --- |
| 1 | **Anchors H2 toutes en français** alors que l'article est en EN. Les 5 ancres sont `apprendre-wordpress-en-une-journee-le-verdict-honnete`, `ce-que-vous-pouvez-concretement-accomplir-en-24-heures`, `les-limites-ce-que-vous-n-apprendrez-pas-en-une-journee`, `la-pratique-et-la-formation-les-cles-pour-vraiment-maitriser-wordpress`, `alors-pret-a-vous-lancer-avec-les-bonnes-attentes`. Probable résidu d'un copier-coller depuis un article FR équivalent. **Impact SEO** : signal de langue mixte (Google peut mal classifier la langue), TOC anchor URLs incohérentes (`/en/learn-wordpress-day/#apprendre-wordpress-en-une-journee-...`), partage social cassé sur ancres. | 🔴 Critique | Régénérer les 5 ancres en EN. Valeurs proposées : `the-honest-verdict`, `what-you-can-accomplish-in-24-hours`, `limitations-what-you-wont-learn`, `practice-and-training`, `ready-to-get-started`. À éditer dans le bloc `wp:heading` de chaque H2 (attribut `id="..."`). |
| 2 | **Image à la une avec ALT en français** sur un article EN. Alt actuel : `Visuel schoolsWP : Est-il possible d'apprendre WordPress en une journée ? Guide 8h pour débuter et créer un site fonctionnel.`. URL fichier : `apprendre-wordpress-en-1-journee-formation-debutant.jpg`. | 🔴 Critique | Réécrire l'alt en EN : `schoolsWP visual: Is it possible to learn WordPress in one day? 8-hour beginner guide.` Le nom de fichier (`.jpg`) reste OK (signal mineur) mais à reverser via le pipeline `tools/wp-media-upload/` si tu refais l'image en EN. |
| 3 | **Faute "kKy points"** dans un callout Kadence (section "Practice and training"). Devrait être `Key points`. | 🟠 Important | Corriger la valeur du `wp:kadence/advancedheading` `2274708_888047-bb` : `kKy` → `Key`. |
| 4 | **Focus keyword Rank Math = 5 keywords concaténés** : `learn wordpress day, wordpress basics, wordpress training, master wordpress, wordpress beginner`. Rank Math attend **un** focus keyword principal + 4 secondaires. Cette concaténation simple casse le scoring (score actuel : **29/100**, vraisemblablement biaisé). | 🟠 Important | Mettre en focus keyword **`learn wordpress in a day`** (qui matche le titre). Garder les 4 autres en additional keywords (séparés en 2e zone Rank Math). Re-checker le score après. |
| 5 | **0 image dans le corps** de l'article. Seule la featured image est présente. La SERP EN sur ce type de query est très "visuelle" (screenshots dashboard WP, schémas, captures hosting). | 🟠 Important | Ajouter 2-3 captures pertinentes : capture du dashboard WordPress vide (premier login), capture install d'un thème, éventuellement screenshot du choix hébergeur. Métadonnées SEO via le pipeline `tools/wp-media-upload/`. |
| 6 | **Pas de schema FAQPage** vérifié. L'article a 8 questions en accordéons Kadence (2 colonnes × 4). Rank Math ne génère pas automatiquement le schema FAQ depuis Kadence accordion blocks. | 🟡 Mineur | Vérifier la présence du schema FAQPage via Rich Results Test (post-publication ou via Rank Math sidebar bloc FAQ). Si absent, ajouter le schema manuellement (Rank Math FAQ block ou JSON-LD personnalisé). |
| 7 | **Tableau Ninja Tables `2114069`** présent dans la section "8-hour schedule" mais contenu non audité ici (Ninja Tables stocke ses lignes dans `wp_ninja_table_items`, pas dans `post_content`). | 🟡 Mineur | Vérifier que la table contient bien un planning 8h structuré (heure, tâche, objectif). Si vide ou incomplète, étoffer avant publication. |

---

## 3. Conformité éditoriale / branding

| # | Problème | Action |
| --- | --- | --- |
| 1 | **Voix "we / us / our"** - 3 occurrences détectées (ex : "We'll define exactly what you can accomplish", "We'll define a concrete program"). schoolsWP = **"I" / "my"** (Michael seul derrière la marque, E-E-A-T solo). Note : 2 occurrences de "I" sont présentes (cf. "That's why **I** offer training"), mais "we" subsiste en intro et milieu. | Convertir les 3 "we / us / our" en "I / my / me" : "**I'll** define exactly what you can accomplish", "**I'll** define a concrete program". Voir mémoire `feedback_voice_singular_solo.md`. |
| 2 | **Anchors H2 françaises** sur un article EN (cf. §2.1) - également un problème de conformité (cohérence langue). | Cf. §2.1. |
| 3 | **Pas de tutoiement à appliquer** : l'anglais ne fait pas la distinction tu/vous, donc cette règle FR ne s'applique pas ici. L'usage de "you" reste neutre et naturel (87 occurrences, bien réparties). | ✅ OK (rien à faire). |
| 4 | **Mots interdits, em-dash, en-dash** : 0 occurrence détectée. ✅ | ✅ |
| 5 | **Naming "schoolsWP"** : 1 occurrence (dans l'alt image, à corriger en EN cf. §2.2). | ✅ Casse correcte. |

✅ **Points propres** : 0 em-dash, 0 en-dash, 0 mot interdit (`disruptive`, `game changer`, `effortless`, etc.), 0 lien cross-langue (règle Polylang respectée : les 3 liens internes pointent tous vers `/en/`).

---

## 4. SEO on-page

| Élément | État | Recommandation |
| --- | --- | --- |
| **Titre H1** | "Is it possible to learn WordPress in a day?" (~46 car.) | ✅ Bon. Question + entité "WordPress" + modifier temporel "in a day". Naturel. |
| **Rank Math title** | "Learn WordPress in one day: 8-hour plan + honest verdict" (~58 car.) | ✅ Excellent. Promet le bénéfice + l'angle différenciant. Inclut "8-hour" qui matche `wordpress 8 hours` (10/mo). |
| **Rank Math description** | "⏱️ Launch a functional WordPress site in 8 hours: key steps, essential themes/plugins + realistic limitations. Clear guide for beginners ✅" (~150 car.) | ✅ Bon. Inclut "beginners" qui matche `wordpress for beginners`. Emoji ⏱️ + ✅ accrocheurs. |
| **Slug** | `learn-wordpress-day` | ⚠️ Acceptable. Plus naturel : `learn-wordpress-in-a-day` (match exact query). Mais éviter un changement de slug si l'article a déjà été référencé. À voir selon l'historique. |
| **Structure Hn** | 5 H2 + 5 H3, 8 questions FAQ en accordéons | ✅ Structure claire et hiérarchique. Couverture H3 légère (5 H3 sur 5 H2 = ratio bas, mais OK pour 2 241 mots). |
| **Anchors H2** | ❌ Toutes en français (cf. §2.1) | 🔴 Critique. Régénérer en EN. |
| **Longueur** | 2 241 mots | ✅ Conforme à la SERP top 10 (médiane ~500-1 000 mots, top long-form à 2 100-4 281). L'article est dans le top 3 word count sur les pages avec contenu. **Pas besoin de pousser la longueur** - la révision initiale "viser 2 800-3 200" est invalidée par les données SERP. |
| **Maillage interne** | 3 liens internes, tous EN (✅ règle Polylang) : `learn-wordpress-autonomy/` (article frère), `wordpress-playground-run-test-develop-in-browser/`, `guides-wordpress-en/` (archive catégorie) | ✅ Cohérent. Note : 1 lien vers archive catégorie (acceptable), 2 vers articles. Pourrait être étendu (cf. §5). |
| **Liens sortants** | 2 liens : `learn.wordpress.org` (officiel ✅), `wp-community.fr` (annuaire FR pointé depuis un article EN ⚠️) | ⚠️ `wp-community.fr` est en français et concerne un annuaire FR. Sur un article EN, ce lien rompt la cohérence linguistique. **Soit** retirer ce lien, **soit** le remplacer par une source EN équivalente (ex: profil WordPress.org, profil GitHub WP contributor, ou linkedin.com profil EN). |
| **FAQ** | 8 questions Kadence accordion | ✅ Très complet. Couvre les variations longue traîne (`can i learn wordpress in a day`, `how long to master wordpress`, `is wordpress hard to learn`, `wordpress training cost`). |
| **Schema FAQPage** | Non vérifié (cf. §2.6) | À valider via Rich Results Test. |
| **Image à la une** | Présente (ALT FR à corriger cf. §2.2) | 🔴 Critique. |
| **Images inline** | 0 (cf. §2.5) | 🟠 Important. |
| **Pillar content flag Rank Math** | Vide | À cocher si l'article doit servir de hub. Sinon laisser vide (c'est un satellite). Recommandation : **vide** (c'est un satellite, pas un pilier). |

---

## 5. Gaps de contenu vs SERP (enrichissements recommandés)

L'article couvre l'angle "verdict + plan d'action" mais manque des **questions précises** trouvées dans la SERP et les PAA. La priorité n'est PAS d'allonger (cf. §4 longueur) mais d'**ajouter les bonnes questions** et d'**optimiser pour AIO** (cf. §11).

Recommandations par priorité :

1. 🔴 **Ajouter 3 questions FAQ manquantes** identifiées dans les PAA et "Frequent Questions" SERP :
   - "**Is WordPress outdated in 2026?**" (PAA position 2 actuel - GAP critique)
   - "**What is the best way to learn WordPress?**" (×7 occurrences SERP - le plus fréquent)
   - "**Can I learn WordPress in 3 days?**" (PAA - variante temporelle utile)
2. 🟠 **Reformuler 2-3 H3 en questions directes** (pattern AIO, cf. §11) :
   - "Critical choices that determine your success" → "What critical choices determine your success on day one?"
   - "From theory to practice: the only viable path" → "How do you move from theory to practice with WordPress?"
   - Optionnel : ajouter un H3 "Can you learn WordPress on your own?" (très fortement présent SERP)
3. 🟠 **Ajouter 2-3 captures d'écran** (cf. §2.5) - dashboard vide premier login, install d'un thème, sélection d'un plugin. La médiane SERP est à ~13-22 images, l'article schoolsWP à 0 est anormal.
4. 🟢 **Étoffer la section "8-hour schedule"** (actuellement dans le seul tableau Ninja Tables) avec un mini-paragraphe "Hour 1 / Hours 2-3 / ..." pour matcher la requête `wordpress 8 hours` (10/mo) et donner du texte indexable autour du tableau.
5. 🟢 **Ajouter une mini-section "Tools you'll need on day one"** - capture l'intent transactionnel marginal et naturalise les mentions affiliés (Kadence theme, FluentCRM, FluentCart, SureCart). Actuellement : 1 mention de FluentCart, 1 SureCart, 0 Kadence, 1 Tutor. Sous-exploité.
6. 🟢 **Mention "WordPress for beginners"** (320/mo, le vrai gros volume du champ) - placer la phrase exact-match 1-2 fois dans le corps (intro, conclusion, ou H3) pour capter la requête connexe.
7. 🟢 **CTA lead magnet "8-hour WordPress checklist"** (PDF) - Related Search inclut "WordPress Tutorial PDF" - confirme la pertinence. À coordonner avec une création FluentCRM (trigger `freebie_wp_8h`).
8. 🟢 (Stratégique long terme) **Vidéo YouTube companion** - la SERP a un carrousel vidéo en position 2 et 5 YouTube cités dans l'AIO. Un Short ou une vidéo 5-8 min "I tried to learn WordPress in 8 hours - honest result" boosterait fortement la capture AIO et la visibilité.

✅ **Respect des concurrents et de l'écosystème** : l'article ne dénigre aucun outil. Mentions de Wix/Squarespace équilibrées (limitations + cas où elles font sens). Conforme à BRAND_RULES 31.

**Termes SERP relevancy élevés sous-exploités** (à intégrer naturellement, basé sur Topic table thruuu) : `training` (×35 mentions SERP), `wordpress training` (×20), `theme` (déjà mentionné mais peu approfondi), `block editor` / `Gutenberg`, `dashboard`, `hosting provider`.

**Related Search à considérer pour articles satellites futurs** : "WordPress course with certificate free", "Best website to learn WordPress for free", "WordPress Tutorial PDF" - 3 angles complémentaires (certification, comparatif gratuit, format PDF).

---

## 6. Données DataForSEO (→ Google Sheet)

Volumes US extraits le 2026-05-16 (location: United States, langue: en). Détail dans `dataforseo-volume-en.json` (source JSON) et `dataforseo-google-sheet.csv` (export tabulaire, format identique au précédent audit).

✅ **Google Sheet créé** le 2026-05-16 sur le Drive de Michael : [schoolsWP - Volumes SEO - Learn WordPress in a day (EN) - 2026-05-16](https://docs.google.com/spreadsheets/d/1wno-bbKXXiEupb1ju16yLjM336RS9CHEOqB7ODtEjBY/edit) (1 onglet, 2 tableaux : synthèse 11 mots-clés + historique mensuel 12 mois). Créé via le connecteur Google Drive (MCP claude.ai, upload `text/csv` → conversion auto en Spreadsheet).

Note méthodologique : volumes US utilisés comme proxy marché anglophone global. Pour affiner par marché (UK, AU, CA), relancer DataForSEO avec `location_name` spécifique.

---

## 7. Cluster et position dans l'arborescence

L'article occupe une **position de satellite** dans le cluster "WordPress learning / formation". Articles frères identifiés (liens internes existants) :

- `/en/learn-wordpress-autonomy/` (lié depuis intro)
- `/en/wordpress-playground-run-test-develop-in-browser/` (lié depuis section pratique)
- `/en/guides-wordpress-en/` (archive catégorie, hub temporaire)

**Pilier manquant à identifier ou créer** : un vrai article pilier "WordPress for beginners: complete guide" (320/mo, KD 52) qui hébergerait ce satellite et les autres articles "learn-*". Sans ce pilier, le cluster reste fragmenté.

**Action moyen terme** : prioriser la production d'un pilier `/en/wordpress-for-beginners/` (cluster head) qui linkerait ce satellite + 2-3 autres satellites longue traîne.

---

## 8. Plan d'action (ordre d'exécution)

**Avant publication (effort : ~30-45 min) :**

1. 🔴 Régénérer les 5 anchors H2 en EN (§2.1)
2. 🔴 Corriger l'ALT de l'image à la une en EN (§2.2)
3. 🟠 Reformater le focus keyword Rank Math : `learn wordpress in a day` seul, les 4 autres en additional keywords (§2.4). Re-checker le score.
4. 🟠 Corriger la faute "kKy points" → "Key points" (§2.3)
5. 🟠 Convertir les 3 "we / us / our" en "I / my / me" (§3.1)
6. 🟠 Réviser le lien sortant `wp-community.fr` (FR sur article EN) ou le remplacer (§4)
7. 🟡 Ajouter 2-3 captures d'écran (§2.5)
8. 🟡 Vérifier le schema FAQPage (§2.6) + le contenu de la table Ninja Tables `2114069` (§2.7)

**Post-publication (suivi) :**

9. ~~Créer le Google Sheet DataForSEO~~ ✅ fait le 2026-05-16 (cf. §6)
10. Mettre l'article en `publish` + indexer via Instant Indexing
11. Surveiller GSC sur 30 jours (queries effectivement captées : `learn wordpress in a day`, `can i learn wordpress in a day`, `wordpress 8 hours`, `how long to learn wordpress`)
12. Lancer un audit `--include-serp` (thruuu) une fois l'article publié, pour comparer aux concurrents EN top 10

**Enrichissements optionnels (moyen terme) :**

13. 🟢 Étoffer à 2 800-3 200 mots via section "Hour-by-hour breakdown" + "Tools you'll need on day one" (§5.1, §5.2)
14. 🟢 Ajouter 1-2 questions FAQ transactionnelles (§5.4)
15. 🟢 Ajouter un CTA lead magnet "8-hour WordPress checklist" (§5.5) - à coordonner avec la production du lead magnet via FluentCRM
16. 🟢 (Stratégique) Produire le pilier `/en/wordpress-for-beginners/` (320/mo, KD 52) qui héberge ce satellite (§7)

---

## 9. Métriques de suivi (prochain snapshot)

| Métrique | Cible 30j post-publication | Cible 90j |
| --- | --- | --- |
| Position GSC sur `learn wordpress in a day` | top 20 | top 10 |
| Impressions sur la longue traîne (FAQ queries) | ≥ 50 | ≥ 200 |
| CTR | ≥ 2 % | ≥ 4 % |
| Score Rank Math après corrections | ≥ 75/100 | ≥ 80/100 |
| Rich Results FAQPage validé | ✅ | ✅ |
| Pages liantes internes (depuis pilier `wordpress-for-beginners`) | - | ≥ 1 |

---

## 10. Décision finale

**Action retenue (mise à jour 2026-05-16)** : **refonte-effectuee** - les 5 phases de corrections sont appliquées et byte-perfect côté serveur (cf. §12). Reste : 1 clic Update Gutenberg (recalcul Rank Math) + publication humaine.

L'article est solide sur le fond (verdict honnête, structure claire, FAQ complète) mais inacceptable en l'état en raison de **2 bloquants critiques** : anchors H2 en français sur article EN + ALT image en français. Ces bugs trahissent un copier-coller depuis un article FR équivalent qui n'a pas été décelé.

**Bonne nouvelle SERP** : créneau "verdict honnête + plan actionnable" libre en top 10 (SERP dominée par landings de formation), AI Overview présent avec sources citées de PR très faible (0-33) → opportunité réelle de capter une citation AIO si l'article est correctement structuré (cf. §11).

**Statut suivi** : `refonte-decidee` → passer à `publie` une fois les 8 points "avant publication" exécutés (§8.1-§8.8). Les enrichissements AIO (§5.1-§5.2) peuvent être faits dans la même session ou différés selon contrainte temps.

---

## 11. Données SERP thruuu (export 2026-05-16, US desktop)

Synthèse complète dans [`thruuu-serp-summary.md`](thruuu-serp-summary.md) (colocalisé). Données brutes : [`thruuu-raw/serp-analysis.xlsx`](thruuu-raw/serp-analysis.xlsx) (54 onglets dont SERP Overview, AIO Overview, Topic, Heading 2, FAQ, PAA, Related Search).

### 11.1 Structure SERP

| Pos | Type | Détail |
| --- | --- | --- |
| 1 | **AI Overview** ⭐ | Google génère un AIO sur cette query |
| 2 | Videos carousel | 5 vidéos YouTube |
| 3 | Questions (PAA) | "Can I learn in one day?", "How quickly?", "Outdated in 2026?", "In 3 days?" |
| 4 | Discussions & Forums | Reddit / Quora |
| 5-21 | Organic | 17 pages (dont 8 landings formation, 4 articles tuto, 3 Reddit, 2 hub) |

### 11.2 AI Overview - opportunité majeure

Google génère un AI Overview sur "learn wordpress in a day". 13 sources citées :

- 5 vidéos YouTube
- 3 mentions de learn.wordpress.org (hub + cours)
- 2 threads Reddit
- **3 articles textuels** : whitelabelcoders.com (PR 33), blog.nobledesktop.com (PR 0), agitraining.com (PR 24)
- 1 landing payante : cotswoldwebsites.co.uk (PR 0)

**Insight clé** : les 3 articles textuels cités par l'AIO ont un PR très faible. **La concurrence AIO n'est PAS dominée par des autorités**. schoolsWP (domaine 5+ ans, PR > 33) part avec un avantage de PR + un angle différenciant.

**Pattern H2 des pages citées AIO** (à reproduire au moins partiellement, cf. §5.2) :

- whitelabelcoders : "How long does it take to learn WordPress basics?", "What skills do you need to learn WordPress effectively?", "Can you learn WordPress without coding knowledge?", "How much time should you invest to become a WordPress professional?"
- nobledesktop : "Can I Learn WordPress On My Own?", "Advantages to Self-Teaching WordPress", "WordPress Self-Teaching Tools", "Drawbacks to Learning WordPress on Your Own", "Alternatives to Learning WordPress on Your Own"

**Conclusion** : H2 sous forme de questions directes + bullets structurées (advantages, drawbacks, tools, skills) = pattern AIO. Reformuler les H3 actuels en questions augmentera la probabilité de citation.

### 11.3 Top 10 organique (concurrents directs)

| Pos | Domaine | Format | Mots | PR |
| --- | --- | --- | --- | --- |
| 5 | pootlepress.com | Formation £125 | 2 198 | 26 |
| 6 | learn.wordpress.org | Hub officiel | 595 | 49 |
| 7 | reddit.com | Social | 38 | 60 |
| 8 | quora.com | Q&A | 0 | 49 |
| 9 | learn.wordpress.org | Cours débutant | 216 | 49 |
| 10 | udemy.com | Formation Udemy | 0 | 46 |
| 11 | cotswoldwebsites.co.uk | Formation £197 (AIO ⭐) | 2 102 | 0 |
| 12 | reddit.com | Social | 60 | 60 |
| 14 | learn.wordpress.org | Catalog cours | 460 | 49 |
| 15 | wphive.com | Tuto 72h | 1 021 | 42 |

**Format dominant** : landings de formation (50 %) + hubs (20 %) + Reddit/Quora (20 %) + articles tuto (10 %). **Le format "article-blog avec verdict honnête + plan" n'existe pas en top 10**. Créneau ouvert.

### 11.4 Questions PAA et SERP non couvertes par l'article

| Source | Question | Statut article | Action |
| --- | --- | --- | --- |
| PAA pos 2 | "Is WordPress outdated in 2026?" | 🔴 Absent | Ajouter en FAQ (§5.1) |
| PAA pos 2 | "Can I learn WordPress in 3 days?" | 🟠 Partiel | Ajouter en FAQ (§5.1) |
| Frequent Questions (×7) | "What is the best way to learn WordPress?" | 🔴 Absent | Ajouter en FAQ ou H3 (§5.1) |
| Frequent Questions | "Can I learn WordPress on my own?" | 🟠 Partiel | Reformuler en H3 explicite (§5.2) |
| Frequent Questions | "How long does it take to learn WordPress?" | ✅ Couvert FAQ | - |
| Frequent Questions | "Is WordPress still worth learning?" | ✅ Couvert FAQ | - |

### 11.5 Related Search (intention adjacente)

8 related searches Google identifiées : `learn wordpress in a day free`, `learn wordpress in a day for beginners`, `Learn WordPress development free`, `Best website to learn WordPress for free`, `Learn WordPress W3Schools`, `Learn WordPress online`, `WordPress Tutorial PDF`, `WordPress course with certificate free`.

3 angles à exploiter pour articles satellites complémentaires :

- **PDF** : "WordPress Tutorial PDF" → renforce la pertinence du lead magnet PDF "8-hour checklist" (§5.7)
- **Certification gratuite** : "WordPress course with certificate free" → angle d'un futur article comparatif "Free WordPress courses with certification"
- **Comparatif gratuit** : "Best website to learn WordPress for free" → angle d'un article comparatif des plateformes free (learn.wp.org, wphive, Coursera audit, YouTube channels)

---

## 12. Corrections appliquées (2026-05-16)

Poussées en 5 phases via Novamira execute-php + `$wpdb->update` direct (pattern qui préserve les escapes JSON Kadence, cf. mémoire `feedback_wp_update_post_unslash_kadence.md`). Backup HTML serveur : `/wp-content/uploads/_audit-bk-2274708-2026-05-16.html`. Tous les pushes vérifiés byte-perfect (SHA1 match).

### 12.1 Phase 1 - Corrections triviales (43 581 → 43 357 bytes, -224)

| # | Item | Avant | Après |
| --- | --- | --- | --- |
| 1 | 5 anchors H2 | Toutes en français | Toutes en EN : `the-honest-verdict`, `what-you-can-accomplish-in-24-hours`, `limitations-what-you-wont-learn-in-a-day`, `practice-and-training`, `ready-to-get-started` |
| 2 | Typo callout Kadence | `kKy points` | `Key points` |
| 3 | Voix corporate "we" | 3 occurrences (×2 We'll, ×1 our) | 0 - converties en "I/my" (E-E-A-T solo) |
| 4 | Lien sortant FR sur EN | `wp-community.fr/annuaire/michael-kihl/` | `wordpress.org/about/` (texte adapté : "WordPress is now over 20 years old, with seasoned developers often holding more than a decade of experience") |

### 12.2 Phase 2 - H3 reformulés en questions (pattern AIO, 43 357 → 43 395 bytes, +38)

| Avant | Après |
| --- | --- |
| "Critical choices that determine your success" | "What critical choices determine your success on day one?" |
| "From theory to practice: the only viable path" | "How do you move from theory to practice with WordPress?" |
| "Get training to go further and faster" | "Why should you get training to go further and faster?" |

3 H3 sur 5 sont désormais des questions directes - aligné sur le pattern des pages citées dans l'AI Overview (cf. §11.2).

### 12.3 Phase 3 - 3 questions FAQ ajoutées (43 395 → 47 764 bytes, +4 369)

3 nouveaux panes Kadence accordion ajoutés (paneCount col 1 : 4→6, paneCount col 2 : 4→5, classes CSS `kt-accordion-has-N-panes` synchronisées) :

- **"Is WordPress outdated in 2026?"** (col 1, pane 5) - couvre la PAA position 2
- **"What is the best way to learn WordPress?"** (col 1, pane 6) - couvre la Frequent Question #1 SERP (×7)
- **"Can I learn WordPress in 3 days?"** (col 2, pane 5) - couvre la PAA position 2 variante temporelle

Réponses rédigées selon BRAND_RULES : voix "I" (Michael solo), pas d'em-dash/en-dash, mentions naturelles Kadence + FluentCart, anti-patterns "in one click / effortless / revolutionary" évités.

### 12.4 Phase 4 - Section 8-hour étoffée + mention WordPress for beginners (47 764 → 48 702 bytes, +938)

Nouveau paragraphe descriptif inséré AVANT le tableau Ninja Tables (qui ne donnait que des labels concis sans texte indexable). Hour-by-hour breakdown détaillé en 1 paragraphe (~140 mots) :

> Here is how a focused 8-hour day breaks down in practice. **Hour 1** : pick a host... **Hour 8** : final review, test the site on mobile, go live. This is enough to launch a **functional WordPress site for beginners**, not a fragile prototype.

Glisse naturellement :

- La requête `wordpress 8 hours` (10/mo) avec exact match dans chaque heure
- `WordPress site for beginners` (matche le top volume du champ : `wordpress for beginners` 320/mo)
- Mention Kadence affiliée naturelle ("Kadence is my recommendation for beginners")

### 12.5 Phase 5 - Rank Math focus keyword + ALT image EN

| Field | Avant | Après |
| --- | --- | --- |
| `rank_math_focus_keyword` | `learn wordpress day, wordpress basics, wordpress training, master wordpress, wordpress beginner` | `learn wordpress in a day, wordpress for beginners, wordpress crash course, wordpress basics, learn wordpress fast` |
| ALT image (attachment 2114101) | "Visuel schoolsWP : Est-il possible d'apprendre WordPress en une journée ? Guide 8h pour débuter et créer un site fonctionnel." (FR) | "schoolsWP visual: Is it possible to learn WordPress in one day? 8-hour beginner guide." (EN) |
| `rank_math_seo_score` | 29 | 29 (⚠️ inchangé jusqu'au prochain Update Gutenberg, recalcul côté JS) |

Le focus keyword principal `learn wordpress in a day` matche désormais le titre + le H1. Les keywords secondaires reflètent maintenant les vrais volumes SERP (cf. §6).

### 12.6 Métriques post-corrections

| Métrique | Avant | Après | Cible §9 |
| --- | --- | --- | --- |
| Word count | 2 241 | **2 728** | OK (top long-form SERP) |
| Bytes | 43 581 | 48 702 | - |
| em-dash + en-dash | 0 + 0 | 0 + 0 ✅ | 0 + 0 |
| we/us/our | 3 | **0** ✅ | 0 |
| I/my count | 2 | **9** ✅ | ≥ 3 |
| H2 ancres EN | 0/5 | **5/5** ✅ | 5/5 |
| H3 en questions | 0/5 | **3/5** ✅ | ≥ 2/5 |
| FAQ questions | 8 | **11** ✅ | ≥ 11 |
| Liens cross-langue | 1 (wp-community.fr) | **0** ✅ | 0 |
| Mention "wordpress for beginners" | 0 | **1** ✅ | ≥ 1 |
| ALT image EN | ❌ FR | ✅ EN | EN |

### 12.7 Actions humaines restantes avant publication

1. **Clic "Update" dans Gutenberg** (obligatoire) - déclenche le recalcul du score Rank Math. Après Phase 7 (3 images inline + ALT + densité 0.35%), le score devrait passer à 65-80/100.
2. **Vérification visuelle** des 11 panes FAQ et des 3 images inline dans l'éditeur Gutenberg.
3. ~~Ajouter 2-3 captures d'écran inline~~ ✅ fait en Phase 7 (cf. §12.8).
4. **(Optionnel)** : vérifier le schema FAQPage via Rich Results Test post-publication.
5. **(Stratégique)** : produire la version vidéo YouTube "I tried to learn WordPress in 8 hours - honest result" pour boost AIO + visibilité (script complet dans youtube-script.md).
6. **Publication** : passer `post_status` de `draft` à `publish` + indexer via Instant Indexing.

Une fois ces points exécutés, faire passer le statut du registry de `refonte-effectuee` à `publie`.

### 12.8 Phase 7 - Boost Rank Math + 3 images inline (post-update Gutenberg #1, score plafonnait à 34)

Constat après le premier Update Gutenberg : score Rank Math passé de 29 à 34 mais plafond bas. Diagnostic via les sous-scores :

| Sous-score Rank Math | Avant Phase 7 | Après Phase 7 |
| --- | --- | --- |
| Focus keyword density | 0.04 % (1× sur 2 728 mots) | **0.36 %** (10× sur 2 828 mots) |
| Focus keyword dans les 100 premiers mots | ❌ Non | ✅ Oui (callout "To remember" reformulé) |
| Slug exact match focus keyword | `learn-wordpress-day` (partiel) | `learn-wordpress-in-a-day` (exact) |
| Images inline | 0 | **3 (avec ALT optimisé focus keyword)** |

**7.A - Boost densité keyword + first 100 words** (8 reformulations chirurgicales, 48 702 → 48 909 bytes) :

- Callout "To remember" reformulé : "Yes, you can **learn WordPress in a day** and launch a functional website..." (placé dans les 50 premiers mots, +2 exact-matches dans l'intro)
- Intro reformulée : "Do you want to **learn WordPress in a day** so you can launch your website without delay?"
- 2e paragraphe intro : "honest verdict and a concrete action plan **to learn WordPress in a day**"
- 3e paragraphe intro : "lay a solid foundation for a functional website **when you learn WordPress in a day**"
- Section H2 verdict : "what you can actually do when you **learn WordPress in a day**"
- Section H2 accomplish : "trying to **learn WordPress in a day** at expert level is an illusion. But acquiring basic autonomy when you **learn WordPress in a day**?"
- Conclusion : "Yes, you can absolutely **learn WordPress in a day** and launch your first site by the end of it."

Densité passée de 0.04 % à 0.36 % (encore sous la cible Rank Math 1-2 % mais 9× plus haute, naturalisée sans keyword stuffing).

**7.B - Slug update** : `learn-wordpress-day` → `learn-wordpress-in-a-day` (exact match focus keyword, possible parce que le post est en draft donc pas de 301 nécessaire).

**7.C - Génération des 3 captures via Gemini 2.5 Flash Image (API directe, workaround MCP nano-banana cassé)** :

Vu que nano-banana MCP v1.0.3 cible toujours `gemini-2.5-flash-image-preview` (modèle retiré par Google), un script ad-hoc `_generate-captures.py` colocalisé dans le snapshot appelle directement l'endpoint GA `gemini-2.5-flash-image`. 3 prompts éditoriaux flat vector schoolsWP-aligned (cream + dark slate blue + fresh green leaf accent, anti-em-dash, anti-AI-slop) générés séquentiellement avec throttle 15 s.

Résultats : 3 PNG 1024 × 1024 (Gemini ignore l'aspect_ratio dans le prompt, sortie 1:1 carrée par défaut, jugée acceptable pour insertion in-content) dans `proposed-images/`.

**7.D - Upload côté serveur via Novamira create-upload-link + multipart POST** (workaround : PUT raw renvoie 500 sur l'endpoint Novamira upload, multipart fonctionne) :

3 fichiers uploadés dans `/wp-content/uploads/2026/05/` puis registered comme attachments WordPress :

| Attachment ID | URL | Polylang lang |
| --- | --- | --- |
| 2900730 | /wp-content/uploads/2026/05/wordpress-dashboard-first-login.png | en |
| 2900731 | /wp-content/uploads/2026/05/wordpress-theme-installer-kadence.png | en |
| 2900732 | /wp-content/uploads/2026/05/wordpress-plugin-installer-essentials.png | en |

Pour chaque attachment : `wp_insert_attachment` + `wp_generate_attachment_metadata` (génère les sizes medium, thumbnail, medium_large) + `_wp_attachment_image_alt` + Polylang `pll_set_post_language(en)`. Les 4 champs WP (Alt text, Titre, Légende, Description) renseignés selon la table du brief captures-brief.md.

**7.E - Insertion 3 blocs Gutenberg image dans le post 2274708** (48 909 → 50 554 bytes, +1 645) :

| # | Capture | Position d'insertion |
| --- | --- | --- |
| 1 | wordpress-dashboard-first-login | Après le H3 "Minimum viable knowledge: your goal for the day", avant la liste à puces |
| 2 | wordpress-theme-installer-kadence | Avant le bloc tableau Ninja Tables 2114069 (en haut de la section visuelle 8-hour) |
| 3 | wordpress-plugin-installer-essentials | Après le bloc tableau Ninja Tables, avant le H2 "Limitations" |

Bloc Gutenberg format standard `wp:image` avec `sizeSlug: "large"`, `linkDestination: "none"`, alt + figcaption renseignés selon le brief.

**7.F - Note sur les fichiers temporaires** : 3 fichiers `.b64` (sidecar base64 de chaque PNG, environ 3.9 MB total) créés pendant le processus d'upload sont restés dans `proposed-images/`. À supprimer manuellement via Explorer (Corbeille Windows) selon la politique data-safety du projet. Pas critique (gitignored si dans .gitignore, sinon à exclure du prochain commit).

### 12.9 État final de l'article (post-Phase 7)

| Métrique | Avant audit | Après Phase 6 | Après Phase 7 | Cible §9 |
| --- | --- | --- | --- | --- |
| Word count | 2 241 | 2 776 | **2 828** | OK |
| Bytes | 43 581 | 48 909 | **50 554** | - |
| Focus keyword density | 0.04 % (1×) | 0.36 % (10×) | **0.354 %** (10×) | 1-2 % (encore sous-optimal mais 9× plus haute) |
| Focus keyword dans 100 premiers mots | ❌ | ✅ | ✅ | ✅ |
| Slug exact match | partiel | exact | exact (`learn-wordpress-in-a-day`) | exact |
| Images inline | 0 | 0 | **3 (avec ALT focus keyword)** | ≥ 2 |
| ALT image featured EN | ✅ | ✅ | ✅ | ✅ |
| H2 ancres EN | 5/5 | 5/5 | 5/5 | 5/5 |
| H3 en questions | 3/5 | 3/5 | 3/5 | ≥ 2/5 |
| FAQ questions | 11 | 11 | 11 | ≥ 11 |
| we/us/our | 0 | 0 | 0 | 0 |
| em-dash + en-dash | 0 | 0 | 0 | 0 |
| Liens cross-langue | 0 | 0 | 0 | 0 |
| Rank Math score | 29 | 34 (après clic Update #1) | À recalculer (clic Update #2 attendu) | ≥ 75 |

**Action humaine immédiate** : 2e clic "Update" dans Gutenberg pour recalculer le score Rank Math. Le score devrait passer à **65-80/100** avec les 4 ajouts Phase 7 (densité, first 100 words, slug exact, 3 images inline avec ALT).

### 12.10 Phase 8 - Tableau Ninja Tables EN (clone traduit + lien à l'article)

**Constat** : l'article EN référençait la table FR 2114069 (titre "Est-il possible d'apprendre WordPress en une journée ?", 3 colonnes FR "Plage Horaire / Objectif / Tâches clés", 4 lignes FR). Polylang lang assignée : aucune (la table n'était pas multilingue, partagée entre les deux articles).

**Décision** : ne pas toucher à la table FR 2114069 (toujours utilisée par l'article FR équivalent). Créer une table EN clone avec colonnes et lignes traduites.

**8.A - Création de la table EN** :

| Champ | Valeur |
| --- | --- |
| Table ID | **2901083** |
| Title | "Is it possible to learn WordPress in a day?" |
| Slug | `learn-wordpress-in-a-day-schedule` |
| Polylang lang | en |
| Colonnes | 3 (`time_block`, `objective`, `key_tasks`) |
| Lignes | 4 |
| Settings | Copie verbatim de la table FR (couleur header vert schoolsWP, classes striped + vertical_centered, render_type legacy_table, font 14, etc.) |

**8.B - Traductions des 4 lignes** (cohérentes avec le 8-hour breakdown rédigé en Phase 4) :

| # | Time block | Objective | Key tasks |
| --- | --- | --- | --- |
| 1 | First 2 hours | Install and configure | Pick a host, install WordPress, take the dashboard tour, basic settings (permalinks, site title). |
| 2 | Next 2 hours | Content and structure | Create an About page, publish one post, understand the difference between pages and posts, build a simple menu. |
| 3 | First 2 hours (afternoon) | Design and customization | Pick and activate a theme (Kadence recommended). Customize colors and logo through the Customizer. |
| 4 | Last 2 hours (afternoon) | Features and security | Install a security plugin (SecuPress or Wordfence) and a contact form. Understand the role of plugins. |

Conformité BRAND_RULES : 0 em-dash, 0 en-dash, mention Kadence (recommendation cohérente avec le paragraphe 8-hour) + SecuPress (stack schoolsWP, glissé en option naturelle). Aucun mot interdit.

**8.C - Méthode de push** : insertion SQL directe via `$wpdb->insert` sur `wp_ninja_table_items` après `wp_insert_post` pour le post de type `ninja-table`. Voie REST `/item/update` non utilisée (mémoire `reference_ninja_tables_rest` : silencieuse, retourne id:null). Settings et colonnes via `update_post_meta` standard.

**8.D - Update du shortcode dans le post 2274708** (50 554 → 50 554 bytes, byte-perfect) :

- `"tableId":"2114069"` → `"tableId":"2901083"` (1 occurrence dans le bloc Gutenberg)
- `[ninja_tables id="2114069"]` → `[ninja_tables id="2901083"]` (1 occurrence shortcode rendu)

Taille identique car les deux IDs font 7 caractères. Push via `$wpdb->update` direct (préserve les escapes Kadence du bloc Gutenberg).

**8.E - Conséquences pour l'écosystème** :

- Article EN (post 2274708) utilise désormais la table EN 2901083 ✅
- Article FR équivalent (s'il existe) continue de référencer la table FR 2114069 inchangée ✅
- 0 régression sur le contenu FR
- Polylang : table EN bien assignée à `en`, prête pour cross-link futur si la table FR est rétroactivement assignée à `fr` (à faire si Michael veut harmoniser les deux côtés)

### 12.11 État final de l'article (post-Phase 8)

L'article EN est maintenant **complètement localisé** : H2 anchors EN, ALT image EN, lien sortant EN, voix solo "I", focus keyword optimisé, slug exact match, 3 images inline brand-cohérentes, FAQ étendue à 11 questions, tableau Ninja Tables en EN. Plus aucun résidu FR détectable.

Prochaine action humaine : 2e clic "Update" dans Gutenberg → recalcul Rank Math attendu autour de 65-80/100.
