---
slug: learn-wordpress-one-day
url: https://schoolswp.com/en/?p=2289537
url_cible: https://schoolswp.com/en/learn-wordpress-one-day/
post_id: 2289537
lang: en
status_article: draft
date_snapshot: 2026-06-02
trigger: Demande Michaël (audit pré-publication d'un brouillon EN refondu)
status: doublon-consolidé
decision: "Option A (fusion) exécutée le 2026-06-02 — voir README.md de l'article"
decision_doc: null
thruuu: à fournir par Michaël (SERP uniquement, l'audit page thruuu = 404 sur un brouillon)
---

# Audit SEO : « Is it possible to learn WordPress in a day? » (EN)

> Snapshot du 2026-06-02. Brouillon EN `post 2289537`, slug `learn-wordpress-one-day`.
> **Audit = lecture seule.** Il observe et recommande, il ne pilote pas. La décision finale reste à toi (et ira dans `content/decisions/`).

## 1. Contexte et déclencheur

Tu as refondu un article EN « apprendre WordPress en une journée » en un nouveau brouillon (post 2289537). Sur la session précédente, on lui a posé une image à la une neuve (att 2969739) et doublé sa table Ninja en EN (table 2969740). Avant publication, tu veux un audit SEO + l'analyse DataForSEO.

**Alerte remontée pendant la collecte** : ce brouillon est un **doublon** d'un article EN **déjà publié** sur le même sujet (voir §6). C'est le point le plus important de cet audit.

## 2. Données collectées

| Source     | Scope                                               | Fichier                                                  |
| ---------- | --------------------------------------------------- | -------------------------------------------------------- |
| On-page    | `post_content` via Novamira (defuddle KO sur draft) | `article-current-snapshot.md`                            |
| DataForSEO | Volumes US/EN (10 kw)                               | `dataforseo-volume.json` + `dataforseo-google-sheet.csv` |
| DataForSEO | SERP `learn wordpress in a day` (US/EN)             | `dataforseo-serp-en.json`                                |
| DataForSEO | Search intent (6 kw)                                | `dataforseo-search-intent.json`                          |
| DataForSEO | Keyword suggestions (seed exact)                    | `dataforseo-keyword-suggestions.json`                    |
| GSC        | URL inspect + 90j (URL publiée)                     | `gsc-url-inspect.json`, `gsc-90d.json`                   |
| thruuu     | SERP export                                         | `thruuu-raw/` (à fournir par toi)                        |

> Note langue : DataForSEO est interrogé en **anglais / US** (pas FR), proxy du marché anglophone. Le volume mondial EN est supérieur aux chiffres US.

## 3. État de l'article (on-page)

- **Statut** : draft, EN, URL provisoire `/en/?p=2289537`, URL cible probable `/en/learn-wordpress-one-day/`.
- **Longueur** : 2 240 mots (le sibling publié en fait 2 828 : ce brouillon est **plus court de ~20 %**).
- **Structure** : 7 H2 + 4 H3, claire et logique (verdict, ce qu'on peut faire, limites, pratique/formation, conclusion, FAQ).
- **FAQ** : 9 questions/réponses bien rédigées (excellent pour l'AEO et les PAA).
- **Table** : planning 8h via Ninja Tables EN (`[ninja_tables id="2969740"]`), OK.
- **Image à la une** : att 2969739 (hero brand, evergreen). **Mais 0 image dans le corps** sur 2 240 mots.
- **Liens internes** : 3, tous EN→EN et pertinents (learn-wordpress-autonomy, wordpress-playground, guides-wordpress-en). Densité faible pour un guide de ce calibre.
- **Liens externes** : 2 - `learn.wordpress.org` (OK, autorité) et `www.wp-community.fr` (**annuaire FR dans un article EN** : incohérence de langue).
- **Meta title** : « Learn WordPress in one day: 8-hour plan + honest verdict » (~57 car., bon).
- **Meta description** : commence par ⏱️, finit par ✅, ~150 car. (correct pour le CTR).
- **Schema** : aucun schema custom Rank Math (`rank_math_schema_*` vide) → seul l'Article par défaut s'applique. **Pas de FAQPage schema** alors que 9 Q/A sont prêtes.

### Points on-page à corriger (avant toute publication)

1. **Focus keyword bourré** : le champ Rank Math contient 5 expressions séparées par des virgules (`learn wordpress day, wordpress basics, wordpress training, master wordpress, wordpress beginner`). Le mot-clé primaire `learn wordpress day` est bancal (manque « in a »). → Mettre **un seul** focus keyword primaire propre : `learn wordpress in a day` (et laisser les variantes en secondaires si tu veux, mais en les écrivant correctement).
2. **0 image dans le corps** : ajouter au moins 1-2 visuels (le planning 8h en visuel, une capture du tableau de bord) avec `alt` contenant le mot-clé.
3. **FAQPage schema absent** : activer le schema FAQ Rank Math sur le bloc FAQ (les 9 Q/A existent déjà). Levier AEO direct.
4. **Lien externe FR** (`wp-community.fr`) dans un article EN : remplacer par un équivalent EN ou retirer (règle « liens dans la même langue »).
5. **Maillage interne faible** : pas de lien sur les entités citées (Kadence, Wordfence, hébergeur, FluentCart, SureCart, WooCommerce). Plusieurs ancres naturelles inexploitées.
6. **Date dans la FAQ** : « Is learning WordPress still relevant in 2026? » va vieillir. Préférer une formulation evergreen.

## 4. SEO actuel (GSC)

- **Brouillon 2289537** : non indexable (draft).
- **Sibling EN publié (2274708, `/en/learn-wordpress-in-a-day/`)** : statut Google **« Discovered - currently not indexed »**, **0 impression / 0 clic sur 90 jours**.
- Google connaît l'URL (via le sitemap + 1 lien interne depuis `fastpixel-review-wordpress-speed`) mais ne l'a pas encore indexée.

**Lecture** : on est en **pré-traction totale** sur ce sujet en EN. Le problème n°1 n'est pas « optimiser pour mieux ranker » mais « faire indexer une URL propre et unique ». Multiplier les URLs identiques aggrave précisément ce blocage.

## 5. SERP analysée (`learn wordpress in a day`, US/EN)

- **AI Overview** en position 1 → jeu **GEO/AEO**. L'encadré réponse en tête d'article (« Yes, for the basics... ») est exactement le bon format pour être cité.
- **Video pack** (cours YouTube 8-10h) en position 1 → forte intention vidéo.
- **Forums** (Reddit « can i learn wordpress in 3 days? », Quora) en top → l'angle honnête/expérientiel est valorisé (ton verdict bien calibré).
- **2 formations payantes** en top 10 (Cotswold « Learn WordPress In A Day Course », Pootlepress) → intention transactionnelle réelle. Le **CTA formation schoolsWP est parfaitement aligné**.
- Autres : learn.wordpress.org (x2), wpmudev (7-day challenge), Quora.

**Volumes** (US, mensuel) :

| Mot-clé                                     | Volume      | Concurrence  | Intent          |
| ------------------------------------------- | ----------- | ------------ | --------------- |
| learn wordpress                             | 480         | MEDIUM       | info            |
| how to learn wordpress                      | 480         | MEDIUM       | info            |
| wordpress for beginners                     | 320         | MEDIUM       | info            |
| **is wordpress hard to learn**              | **90**      | **LOW (11)** | info            |
| how long does it take to learn wordpress    | 40          | LOW          | info/commercial |
| wordpress crash course                      | 40          | MEDIUM       | info            |
| learn wordpress fast                        | 20          | LOW          | info            |
| **learn wordpress in a day** (cible exacte) | **10**      | MEDIUM       | transac/info    |
| can i learn wordpress in a day              | 10 (déclin) | -            | info            |

**Intent** : la requête exacte penche **transactionnel** (0,97) - les gens cherchent une formation. Le reste du cluster est informationnel. Mix info + transac = le format « guide honnête + CTA formation » est le bon.

## 6. Insight critique n°1 : cannibalisation / doublon EN

Il existe **deux articles EN au titre identique, même sujet, même mot-clé** :

| Post                       | Statut     | Slug / URL                      | Mots  | Image à la une |
| -------------------------- | ---------- | ------------------------------- | ----- | -------------- |
| **2274708**                | **publié** | `/en/learn-wordpress-in-a-day/` | 2 828 | 2968995        |
| **2289537** (ce brouillon) | draft      | `/en/learn-wordpress-one-day/`  | 2 240 | 2969739        |

- 2274708 est le **membre EN officiel** du groupe Polylang (en=2274708, de=2274709, fr=2112488). 2289537 **n'est pas relié** au groupe (cf. audit session précédente).
- **Même schéma en DE** : 2274709 (publié) + 2289536 (draft). À traiter en miroir.
- Publier 2289537 sur une 2ᵉ URL = duplicate content + cannibalisation + dilution du jus de lien, sur un sujet **déjà non indexé**. C'est le pire moment pour ajouter une URL concurrente.

**Le slug `learn-wordpress-in-a-day` (publié) est meilleur que `learn-wordpress-one-day`** : il colle au mot-clé exact (« in a day ») et c'est lui qui a la (faible) notoriété Google actuelle.

## 7. Insights critiques (synthèse)

1. **Doublon EN à résoudre AVANT toute publication** (§6). Bloquant.
2. **Pré-traction** : 0 indexation sur le sujet EN. Priorité = indexation d'**une** URL propre + maillage interne entrant.
3. **Jeu AEO/AI Overview** plus que volume : la requête exacte pèse 10/mo, mais l'AI Overview, les PAA et le cluster (« is wordpress hard to learn » 90, « how long to learn » 40, « learn wordpress » 480) sont le vrai gisement. La FAQ + l'encadré réponse sont des atouts à exploiter avec le **FAQPage schema**.
4. **Intention transactionnelle confirmée** : 2 formations payantes en SERP. Le CTA formation/guides schoolsWP est aligné ; le renforcer.
5. **On-page perfectible** mais sain : focus keyword à nettoyer, images à ajouter, FAQ schema à activer, lien FR à corriger, maillage à densifier.

## 8. Décision (à arbitrer par toi)

L'audit recommande de **NE PAS publier 2289537 comme nouvelle URL séparée**. Trois options :

- **Option A (recommandée) - Fusion dans l'existant** : porter les améliorations de 2289537 dans le post **publié 2274708** (qui garde son URL `/en/learn-wordpress-in-a-day/`, son historique, son groupe Polylang et son meilleur slug). Puis passer 2289537 en corbeille. Idem DE (fusionner 2289536 → 2274709). Zéro risque de cannibalisation, on capitalise sur l'URL connue de Google.
- **Option B - Bascule canonique** : faire de 2289537 la version canonique, publier sur `/en/learn-wordpress-in-a-day/` (réutiliser le slug existant), 301 de l'ancien, et relier le groupe Polylang. Plus lourd, gain SEO nul vs A.
- **Option C - Statu quo** : laisser 2289537 en brouillon, ne rien publier. Aucun gain.

> Mon avis : **Option A**. Le brouillon 2289537 a une bonne image et une table EN propre, mais il est plus court (2 240 vs 2 828 mots) et son slug est moins bon. Le plus rapide et le plus sûr : transférer ses bons éléments (image 2969739, table 2969740, encadré réponse) dans 2274708, puis archiver le doublon.

## 9. Plan d'action (si Option A)

1. **Décider** l'option (doc dans `content/decisions/`).
2. Sur **2274708** (publié) :
   - Nettoyer le focus keyword → `learn wordpress in a day` (primaire unique).
   - Activer le **FAQPage schema** sur le bloc FAQ.
   - Ajouter 1-2 images corps (planning 8h, capture dashboard) + `alt`.
   - Remplacer le lien `wp-community.fr` par un équivalent EN.
   - Densifier le maillage interne (Kadence, Wordfence, hébergeur, FluentCart, guides).
   - Reprendre l'image à la une 2969739 et la table EN 2969740 si meilleures que l'existant.
   - Ajouter 2-3 liens internes **entrants** depuis d'autres pages EN (pour pousser l'indexation).
3. **2289537** → corbeille (après transfert). Idem DE (2289536 → 2274709).
4. Demander l'**indexation** de `/en/learn-wordpress-in-a-day/` (Instant Indexing / GSC).
5. thruuu : SERP export par toi → `thruuu-raw/` (l'audit page thruuu est inutile sur ce sujet, pas de draft à scraper).

## 10. Métriques de suivi (prochain snapshot)

- Indexation `/en/learn-wordpress-in-a-day/` (Discovered → Indexed).
- Premières impressions/clics GSC sur le cluster (`learn wordpress`, `is wordpress hard to learn`, `how long to learn wordpress`).
- Présence en AI Overview / PAA sur les requêtes du cluster.
- Position sur « learn wordpress in a day » et variantes.
- Clics sortants vers les pages formation/guides (intention transac).

---

_Sources brutes colocalisées dans ce dossier. Snapshot figé : toute nouvelle data ira dans un snapshot daté ultérieur._
