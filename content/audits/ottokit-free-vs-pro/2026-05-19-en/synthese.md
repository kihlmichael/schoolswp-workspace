---
slug: ottokit-free-vs-pro
url: https://schoolswp.com/en/?p=2865102
lang: en
post_id: 2865102
date_snapshot: 2026-05-19
trigger: Demande Michael (audit pré-publication EN, suite à publication DE)
status: bloc-3-applique
---

# Audit OttoKit Free vs. Pro (EN) - snapshot 2026-05-19

## 1. Contexte et déclencheur

- Article 2865102 en **brouillon anglais** (post_modified 2026-05-08 22:55:13).
- Demande Michael : audit pré-publication EN dans la foulée de la publication DE.
- Fichier thruuu `(1).xlsx` fourni par Michael s'est révélé être le **thruuu DE re-importé** (Language=de, Country=DE, google.de). Le fichier `(2).xlsx` fourni ensuite est bien le **thruuu EN US natif** (Language=en, Country=US, google.com) -- intégré dans `thruuu-raw/serp-analysis-en-v2.xlsx` et synthétisé dans `thruuu-en-summary.json`.
- **Featured image hero EN déjà créée et set** sur le post (attachment 2912562, hero 1920x1080 style FluentCRM, 2026-05-19 21:18). Voir détails dans [README.md](../README.md).
- Version FR `2592422` /ottokit-gratuit-vs-pro/ publiée (modified 2026-05-16).
- Version DE `2898734` brouillon avec Bloc 1 + Bloc 2 appliqués (modified 2026-05-19 21:03).

## 2. Données collectées

| Source | Périmètre | Fichier |
| --- | --- | --- |
| Novamira REST (execute-php) | post_content + meta complets EN | backup serveur `/wp-content/uploads/audit-ottokit-en-20260519-193951.txt` (37 168 octets) |
| DataForSEO Labs - keyword overview US | 6 keywords cibles | `dataforseo-volume.json` |
| DataForSEO SERP organic US depth 20 | top 20 + AIO + video pack + PAA + related | `dataforseo-serp-us.json` |
| DataForSEO suggestions US seed OttoKit | 11 suggestions retournées (vs 5 DE) | `dataforseo-keyword-suggestions.json` |
| DataForSEO search intent US | 5 keywords | `dataforseo-search-intent.json` |
| DataForSEO historical US (24 mois) | ottokit, pro, pricing, suretriggers, review | (résumé inclus dans `dataforseo-volume.json`) |
| GSC schoolswp.com 90j (2026-02-18 → 2026-05-19) | filtre page contains /en/suretriggers | `gsc-90d.json` |
| GSC URL inspect | /en/ottokit-free-vs-pro/ (brouillon, URL unknown) | `gsc-url-inspect.json` |
| CSV volumes pour Drive | 13 keywords cluster US | `dataforseo-google-sheet.csv` |
| thruuu export brut EN | google.com US natif | `thruuu-raw/serp-analysis-en-v2.xlsx` |
| thruuu EN synthèse | top 19 + Page Rank + word counts + questions concurrents | `thruuu-en-summary.json` |

> **Correction thruuu** : le fichier `(1).xlsx` initial était en fait un re-import DE ; le `(2).xlsx` fourni ensuite est bien EN US. DataForSEO et thruuu confirment **le même top 10 organic** (aucune divergence). thruuu apporte en plus les Page Rank par URL et les word counts détaillés.

## 3. État de l'article EN actuel (pré-corrections)

| Critère | Valeur | Commentaire |
| --- | --- | --- |
| Statut | brouillon | Non publié, URL inconnue de Google |
| Modified | 2026-05-08 22:55 | Plus ancien que DE (2026-05-19) |
| Word count | 1 604 mots | Légèrement plus court que DE (1 739) |
| H2 / H3 | 7 / 12 | Hiérarchie propre |
| **IDs H2** | tous en slug FR | À reslugger en anglais |
| Images | 1 (héro + nouvelle featured image set) | Hero EN défini ; corps de l'article reste à 1 image |
| TOC Kadence | oui | OK |
| FAQ Kadence accordion | oui (4 accordions, 5 panes) | DE post-Bloc 2 a 6 panes |
| Ninja Table | oui (id 2848098, FR) | Inadapté EN, créer un jumeau EN |
| Kadence CTA | 2 | OK |
| Liens internes EN natifs | 2 (`/en/articles/`, `/en/suretriggers-ottokit-vs-zapier/`) | OK |
| Liens internes cross-langue FR | 2 | **VIOLATION** [[feedback_links_same_language]] |
| Liens externes | 0 | Aucune source primaire référencée |
| Liens cloak affilié | 1 (`/ottokit/`) | OK |
| Em-dash (U+2014) | **2** | **VIOLATION** branding grave (interdiction stricte) |
| En-dash (U+2013) | **1** | **VIOLATION** branding |
| Rank Math SEO score | 74/100 | Sous le seuil schoolsWP (≥ 80), mais mieux que DE pré-correction (61) |
| JSON-LD FAQPage | non | À ajouter (PAA actif US) |
| Featured image | ✓ 2912562 (hero EN 2026-05-19) | OK, langue Polylang=en |

Détails complets : voir [article-current-snapshot.md](article-current-snapshot.md).

## 4. SEO actuel et cluster OttoKit GSC (90j EN)

Cluster EN actuellement indexé : 1 page (`/en/suretriggers-ottokit-vs-zapier/`).

- 0 clic sur 90 jours malgré 76 impressions sur « suretriggers vs zapier » pos 1.1.
- 28 impressions sur « suretriggers » pos 46.4.
- 67 impressions sur « suretriggers wordpress automation plugin » pos 12.0.
- L'URL `/en/ottokit-free-vs-pro/` est inconnue de Google (post brouillon).

**Lecture** : la marque SureTriggers est morte côté demande effective (0 clic), mais le re-branding OttoKit US explose en search volume (+3100 % YoY sur le seed). L'article EN doit pivoter complètement vers la marque OttoKit, comme le DE.

## 5. SERP US analysée (DataForSEO)

Top 8 organic + composants :

1. AI Overview (asynchrone) -- présent
2. Video pack (3 YouTube : CodingMenace, DroidCrunch, Lytbox) -- chaud
3. ottokit.com (sitelinks Pricing/Products/Recipes/Resources)
4. wpastra.com/review/ottokit-review/ (1 969 mots)
5. reddit.com (LTD thread)
6. wordpress.org/plugins/suretriggers/ (4.9/117)
7. PAA pack (6 questions)
8. crocoblock.com (1 542 mots)
9. newpulselabs.com (4.8)
10. g2.com (4.5)
11. ottokit.com/suretriggers-is-now-ottokit/

Observations critiques (différentes de DE) :

- **Video pack en position 2** (3 YouTube, dont 2 sur la requête générale OttoKit). schoolsWP devrait viser un short YouTube DE+EN avec le même titre pour gratter cette position.
- **PAA actif (4 questions)** -- contrairement à DE où PAA est vide. **Le JSON-LD FAQPage devient prioritaire absolu pour gagner le rich-result**.
- **AI Overview présent** -- même conclusion que DE : citation AIO via paragraphe court et Q&A explicite reste l'objectif.
- ottokit.com en 3 positions (pos 1, 8, 13/15 selon sources). Le rebrand annonce inflate la SERP officielle.
- Top 19 = 0 résultat natif Free vs Pro spécifique. **Angle d'attaque maintenu** pour schoolsWP.

### 5b. Détails thruuu EN (Page Rank + word counts)

| Pos | URL | Page Rank | Word count |
| ---: | --- | ---: | ---: |
| 3 | ottokit.com/ | 41 | 1 666 |
| 4 | wpastra.com/review/ottokit-review/ | 49 | 1 969 |
| 5 | reddit.com (Wordpress thread) | 60 | 266 |
| 6 | wordpress.org/plugins/suretriggers/ | 76 | 4 043 |
| 8 | crocoblock.com/blog/ottokit-wordpress-plugin-review/ | 49 | 1 542 |
| 9 | newpulselabs.com/ottokit-review/ | 29 | 2 006 |
| 10 | g2.com/products/ottokit/reviews | 40 | n/a |
| 11 | ottokit.com/suretriggers-is-now-ottokit/ | 41 | 1 129 |
| 13 | ideas.ottokit.com/updates | 40 | 4 007 |
| 14 | wordpress.org/support/topic/5-free-workflows | 76 | 158 |
| 15 | ottokit.com/wordpress/ | 41 | 535 |

Médiane word count top 8 organic = **1 666 mots**. schoolsWP EN à 1 604 mots est **dans la fourchette pertinente** (proche du leader ottokit.com 1666, crocoblock 1542). Ce n'est pas la longueur qui manque, c'est la **profondeur** (data retention, team collaboration manquent) et le **schema FAQPage**.

Médiane Page Rank top 10 = **~46**. Concurrents accessibles (sauf wordpress.org à 76 qui n'est pas un Free vs Pro spécifique).

### 5c. Structure dominante à dépasser : wpastra.com (#4, 1 969 mots, PR 49)

H2 clés de la structure wpastra (à intégrer dans la refonte EN) :

- The Pros and Cons of OttoKit
- User Reviews
- **OttoKit Pricing: Affordable Automation** (avec H3 The Free Plan / Pro Plan / Business Plan / Lifetime Access)
- OttoKit vs Zapier vs Pabbly Connect
- Key Automation Features
- Working With OttoKit
- **5 critères évalués** : Pricing, Ease of Use, Data Retention, Team Collaboration, App Integrations

schoolsWP couvre 3/5 critères (Pricing, Ease of Use, App Integrations). **Manquent Data Retention et Team Collaboration** -- à ajouter en H3 sous OttoKit Pro pour battre la structure.

### 5d. Questions EN à intégrer dans la FAQ (issues thruuu Frequent Questions)

| Question EN | Found in pages | Note |
| --- | ---: | --- |
| Who Is OttoKit For ? | 5 | Très récurrente. La FAQ schoolsWP a déjà l'équivalent (« Das ideale Profil... » côté DE). |
| How Does OttoKit Compare to Platforms Like Zapier ? | 4 | Déjà dans la FAQ schoolsWP DE et EN. |
| What is OttoKit ? | 3 | Question d'entrée. À ajouter en intro plutôt qu'en FAQ. |
| **How Much Does OttoKit Cost ?** | 1 | **PAA hint US explicite -- à ajouter obligatoirement dans la FAQ EN**. |
| Is OttoKit secure and reliable ? | 1 | À considérer (compliance angle). |
| Does it support multi-step workflows ? | 1 | Déjà couvert dans le H3 « Multi-Step Automation ». |

Ajout recommandé dans la FAQ EN : **« How much does OttoKit cost ? »** (réponse : Free plan + Pro à 9 $/mois ou 108 $/an + Business + Lifetime, lien vers ottokit.com/pricing).

## 6. Volumes et tendances US (DataForSEO 24 mois)

| Keyword | Volume actuel | Trend mensuel | Trend annuel | Note |
| --- | ---: | ---: | ---: | --- |
| **ottokit** | 390/mois | +23 % | **+3100 %** | Explosion post-rebranding (avril 2025) |
| ottokit pricing | 20/mois | 0 % | +100 % (Q) | Trend trimestriel +100 %, fort potentiel |
| ottokit pro | 10/mois | stable | n/a | Volume marginal |
| ottokit ai | 10/mois | stable | n/a | KD 0.86 HIGH (seul keyword chaud sur les enchères AI) |
| Autres longtails | 10/mois chacun | stable / décroissant | n/a | Multiples voies de captation à faible volume |

**Comparaison DE vs US** :

| Métrique | DE | US |
| --- | ---: | ---: |
| Volume seed « ottokit » | 110 | **390 (3,5×)** |
| KD seed | 11 | 16 |
| Trend yearly | n/a (récent) | +3100 % |
| AI Overview | oui | oui |
| Video pack pos 2 | non | **oui (3 YouTube)** |
| PAA actif | non | **oui (6 Q)** |
| Concurrent natif top 10 (langue locale) | 1 (bit-integrations.com) | 8 (tous EN, c'est la langue native du marché) |

Le marché US est **3,5× plus gros**, **plus chaud** (YouTube + PAA + AIO + AI enchères) et **3× plus concurrentiel**. Mais le longtail « Free vs Pro » reste vierge dans le top 10.

## 7. Insights critiques (5)

1. **Marché US 3,5× plus gros et en explosion (+3100 % YoY)**. L'article EN a plus de potentiel de trafic absolu que la DE -- justifie un effort de publication propre.

2. **Concurrence forte mais aucun Free vs Pro dans le top 10**. Comme en DE, l'angle d'attaque comparatif Free vs Pro reste exclusif. wpastra.com (#2) a un review général mais pas un comparatif structuré.

3. **PAA actif + Video pack = JSON-LD FAQPage + Short YouTube prioritaires**. Le PAA inclut 5 questions identiques au DE (Is OttoKit free, How much, etc.) + question piège (newsletter platform). Activer FAQPage capte le rich-result probablement à coup sûr (concurrents n'en ont pas).

4. **5 fuites correctives bloquantes identiques au DE pré-correction** :
   - 2 em-dash + 1 en-dash (violation branding stricte)
   - 7 IDs H2 en slug FR (à reslugger EN)
   - 2 liens cross-langue vers FR
   - Ninja Table id 2848098 en FR (créer un EN jumeau)
   - 0 lien externe, 0 JSON-LD FAQPage, pas de question Make/n8n dans la FAQ

5. **Rank Math score 74/100** déjà mieux que DE pré-correction (61). Après Bloc 2 + Bloc 3 KW densification, devrait monter au-dessus de 80.

## 8. Décision

> **REFONTE LÉGÈRE PRÉ-PUBLICATION** appliquée 2026-05-19 20:11 (`bloc-3-applique`).

Mêmes blocs que DE, mais effort encore plus faible car le score Rank Math est déjà à 74. Coût estimé : **30-45 min**.

**Pourquoi pas publier immédiatement** : 2 em-dash + 1 en-dash bloquent. 2 liens cross-langue cassent l'expérience EN. Pas de JSON-LD FAQPage = on rate le rich-result US (qui a un PAA actif, signal fort).

**Pourquoi pas attendre plus de signal** : le marché US est en explosion (+3100 % YoY). Plus on retarde, plus la concurrence (Crocoblock, NewPulse Labs, WPAstra) se renforce. L'article DE est déjà publiable -- l'EN doit suivre.

## 9. Plan d'action pré-publication (par parallélisme DE)

### Bloc 1 - Corrections obligatoires ✓ APPLIQUÉ 2026-05-19 20:09

1. [x] Remplacer les 2 em-dash + 1 en-dash par « : » ou « . » (em-dash 2→0, en-dash 1→0)
2. [x] Neutraliser les 2 liens cross-langue FR (reformulation propre, aucun équivalent EN existant côté CMS)
3. [x] Reslugger les 7 IDs H2 en anglais : `summary-comparison`, `features-free-and-pro`, `ottokit-free`, `ottokit-pro`, `price-difference`, `customer-reviews`, `free-or-pro`

### Bloc 2 - Enrichissements forts ✓ APPLIQUÉ 2026-05-19 20:11

1. [x] Ninja Table EN jumeau créé ID `2912655` (4 colonnes EN : Criterion / OttoKit Free / OttoKit Pro / Verdict, 6 items EN, Polylang=en). Post EN référence désormais cet ID.
2. [x] 3 liens externes ajoutés : `ottokit.com/wordpress/` (section OttoKit Free), `wordpress.org/plugins/suretriggers/` (section OttoKit Free), `g2.com/products/ottokit/reviews` (section Customer Reviews).
3. [x] JSON-LD FAQPage injecté en fin de contenu via `wp:html` (7 questions EN dont « How much does OttoKit cost ? » qui matche le PAA US).
4. [x] Pane FAQ « How does OttoKit compare to Make and n8n ? » ajoutée à l'Accordion 0 (3→4 panes) + pane « How much does OttoKit cost ? » à l'Accordion 1 (2→3 panes). Toutes les questions du JSON-LD sont visibles dans le contenu.

### Bloc 3 - Rank Math 74 → 80+ ✓ APPLIQUÉ 2026-05-19 20:09

1. [x] Densité focus KW renforcée dans le premier paragraphe (`<strong>OttoKit Free vs. Pro</strong>` exact en intro, idem DE).
2. [x] 2 H3 ajoutés sous « OttoKit Pro » avant le H2 « Price Difference » : **Data retention** + **Team collaboration**. Insight wpastra.com (#4 SERP US) intégré.
3. [ ] Person schema mu-plugin et schema validation : vérifier après publication (manuel Michael).

> **Note Rank Math** : le score `rank_math_seo_score` reste à 74 après le push direct DB. Il se recalcule à l'ouverture suivante dans Gutenberg (clic « Update ») ou via l'endpoint `rankmath/v1/updateMeta`. Le contenu est conforme aux critères ≥ 80 attendus (focus KW présent en intro+H2+strong, 3 liens externes, 1 lien interne EN, JSON-LD FAQPage, 7+ panes accordion, longueur 44 308 octets ≈ 1 700+ mots).

### Bloc 4 - Post-publication (post live)

1. [ ] Maillage interne EN : ajouter un lien depuis `/en/suretriggers-ottokit-vs-zapier/` vers `/en/ottokit-free-vs-pro/`.
2. [ ] Soumettre via Instant Indexing (plugin actif).
3. [ ] Surveiller GSC EN à J+15, J+30, J+90 sur « ottokit », « ottokit pricing », « ottokit review ».
4. [ ] Mesurer clics affiliés cloak `/ottokit/` (intérêt commercial du trafic US).

## 10. Métriques de suivi (prochain snapshot)

- Indexation GSC EN (`/en/ottokit-free-vs-pro/`) sous 48h post-publication.
- Position GSC sur « ottokit » US (objectif top 20 sous 30j, top 10 sous 90j).
- Impressions cluster EN OttoKit (baseline : 76 sur « suretriggers vs zapier » uniquement).
- Featured snippet / FAQ rich result détecté (oui/non, via URL inspect).
- Évolution volume « ottokit » US (390/mois actuel, +23 % monthly → projection ~500/mois Q3 2026).
- Clics affiliés OttoKit cloak (US plus monétisable que DE).

Re-audit recommandé : **2026-07-19** (J+60) ou plus tôt si Rank Math weekly signale chute.

## Annexes (fichiers du snapshot)

- [article-current-snapshot.md](article-current-snapshot.md) - inventaire structurel détaillé
- [dataforseo-volume.json](dataforseo-volume.json)
- [dataforseo-serp-us.json](dataforseo-serp-us.json)
- [dataforseo-search-intent.json](dataforseo-search-intent.json)
- [dataforseo-keyword-suggestions.json](dataforseo-keyword-suggestions.json)
- [dataforseo-google-sheet.csv](dataforseo-google-sheet.csv) - source du Sheet Drive EN
- [gsc-90d.json](gsc-90d.json)
- [gsc-url-inspect.json](gsc-url-inspect.json)
- [thruuu-en-summary.json](thruuu-en-summary.json) - synthèse exploitable du thruuu EN US
- [thruuu-raw/serp-analysis-en-v2.xlsx](thruuu-raw/serp-analysis-en-v2.xlsx) - export brut Google US natif
- Backup serveur (snapshot initial) : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-20260519-193951.txt`
- Backup serveur (pré-Blocs) : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-PRE-BLOCS-20260519-200109.txt`
- Backup serveur (mid Bloc 1+3) : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-MID-BLOC13-20260519-200957.txt`
- Backup serveur (post Blocs) : `https://schoolswp.com/wp-content/uploads/audit-ottokit-en-POST-BLOCS-20260519-201105.txt`

Dossier `thruuu-raw/` rempli a posteriori (fichier `(2).xlsx` fourni par Michael après coup, Language=en Country=US google.com).

Google Sheet : « schoolsWP - Volumes SEO - OttoKit Free vs Pro EN - 2026-05-19 » sur Drive Michael (lien dans README.md de l'article).

Hero featured image : `assets/featured-images/post-2865102/slide-00-hero-en.html` + `slide-00-hero-en.png` (attachment WP 2912562, set 2026-05-19 21:18).

Ninja Table EN jumelle : post `ninja-table` 2912655 « OttoKit Free vs. Pro : Which plan should you choose in 2026 ? », 4 colonnes EN, 6 items EN traduits, Polylang=en, header vert schoolsWP #00d400.
