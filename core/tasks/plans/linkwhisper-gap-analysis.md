# LinkWhisper Refresh — Gap Analysis (Étape 1)

> Date : 2026-05-06 · Cible : `https://schoolswp.com/link-whisper-avis/` (post 58166) · Mot-clé : `linkwhisper avis`
> Statut : diagnostic terminé, en attente de validation Michaël avant l'étape 2 (brief de réécriture).

## Sources mobilisées

| Source | Détail | Fichier brut |
| --- | --- | --- |
| WP REST | post 58166, content + structure | `linkwhisper-data/wp-post-raw.json`, `wp-post-structure.json`, `wp-post-edit.json`, `wp-post-taxonomy.json` |
| thruuu xlsx | SERP FR top 17, headings, topics, PAA | `linkwhisper-data/thruuu-key-sheets.json` |
| thruuu audit docx | recommandations automatiques + SERP scoring | `linkwhisper-data/thruuu-audit.md` |
| DataForSEO API | overview + related + suggestions + ads volume FR | `linkwhisper-data/dfs-*.json` |
| GSC | search analytics 90j + URL Inspect | inline |

> ⚠ **Limite Novamira MCP** : les tools `mcp__novamira-schoolswp-com__*` ne se chargent pas via ToolSearch. Repli effectué via WP REST natif (auth Basic depuis `.claude/settings.local.json`). Conséquence : meta Rank Math non lus directement (`meta` REST vide), mais récupérables via `rankmath/v1/getHead` à l'étape 4. Pour ce diagnostic, le title + meta description observés viennent du SERP scrap thruuu qui est plus fiable que le code source.
>
> ⚠ **Limite DFS MCP** : 401 sur `mcp__dataforseo__*`. Repli direct via `urllib` avec creds `.claude/settings.local.json`. À investiguer hors sprint (probablement variable d'env stale dans le wrapper MCP).

## 1. Snapshot article actuel

| Champ | Valeur observée |
| --- | --- |
| H1 | `Link Whisper : Le Plugin WordPress Ultime pour Votre Maillage Interne ?` |
| Title SERP | `🚀 Link Whisper Avis 2026 : Outil SEO incontournable ?` (54 char) |
| Meta description | `Découvrez si Link Whisper est le meilleur plugin de maillage interne en 2026. Avis, fonctionnalités et alternatives pour booster votre SEO !` (140 char) |
| Slug | `/link-whisper-avis/` ✅ exact match |
| Date publication | 2025-03-26 |
| Date dernière MAJ | 2026-03-29 (5 semaines) |
| Mots (rendered) | 2918 |
| Mots (thruuu compté) | 2572 |
| Headings | 9 H2 + 5 H3 = 14 (zéro question H2 directe sauf 1) |
| Catégories | Link Whisper (1798), Référencement & SEO (1794) |
| Tags | aucun |
| Schema détecté | Place, EducationalOrg, Org, Person, BlogPosting, BreadcrumbList — **pas de FAQPage**, **pas de Review/AggregateRating** |
| Référents internes (GSC) | seulement 2 (`/slug-wordpress/`, `/seo-wordpress/`) |
| Indexation | PASS, mobile crawl 2026-04-23, canonical OK |

## 2. SERP top 10 FR (`linkwhisper avis`, google.fr, desktop)

| Pos | Site | Mots | Type | Pub | Maj | Note |
| ---:| --- | ---:| --- | --- | --- | --- |
| 1 | blogdumoderateur.com/tools/link-whisper/ | 315 | listing tool | — | — | listing/landing très court ; ranke par autorité de domaine |
| **2** | **schoolswp.com/link-whisper-avis/** | **2572** | **article** | **2025-03-26** | **2026-03-29** | **nous** — schema riche, beaucoup de mots |
| 3 | YouTube vidéo | — | video | — | — | vidéo SERP feature |
| 4 | reddit.com (r/SEO, EN) | 142 | social | — | — | discussion, autorité Reddit |
| 5 | busilearn.fr | 2618 | review e-commerce | — | — | review longue, schema Product |
| 6 | webandseo.fr | 3084 | review article | 2022-06-20 | 2025-02-25 | longue + **vidéo embed** + 39 images |
| 7 | appvizer.fr | 778 | directory | — | — | autorité directory + schema SoftwareApplication |
| 8 | netbooster.fr | 1359 | review article | 2022-04-06 | 2023-11-30 | **datée >18 mois** |
| 9 | comparatif-logiciels.fr | 766 | directory | 2025-02-17 | 2025-03-08 | directory + schema Product |
| 10 | nordigital.fr | 1802 | review | 2022-01-08 | 2022-01-09 | **datée >4 ans** |

**Lecture clé** : on est positionnés #2 organique (vraie position derrière la vidéo). Trois concurrents directs (busilearn, webandseo, netbooster) sont tous des reviews 2500-3000 mots. Pas de SERP FAQ, pas de SERP People Also Ask schema sur la page actuelle (thruuu : `Has SERP FAQ: False`, `Has On Page FAQ: False`).

## 3. Volumes & intent (DataForSEO FR)

| Mot-clé | SV/mo (Ads) | SV/mo (Clickstream) | CPC | Intent | Évolution 12 mois |
| --- | ---:| ---:| ---:| --- | --- |
| linkwhisper | 480 | 454 | 2,94 € | navigational | peak 1900 (mar 2025) → 480 (déclin 75 %) |
| link whisper | 480 | 1591 | 2,94 € | informational | idem (même clé en cluster) |
| link whisper plugin | 10 | — | 7,45 € | informational | stable bas |
| plugin maillage interne wordpress | 20 | 0 | — | navigational | stable bas |
| **linkwhisper avis** | — (non listé Ads) | — | — | **commercial déduite** | **tail traffic** (visible GSC mais sous radar Ads) |
| linkwhisper review / alternative / prix / francais | non listé | — | — | — | tail |

**Clés du diagnostic volume :**
- Le brand `linkwhisper` (un mot ou deux) totalise ~960 SV/mo recherchés en France, en déclin marqué depuis le pic de mars 2025.
- `linkwhisper avis` n'a pas de volume Ads mesurable. Le trafic réel passe par `linkwhisper` brut (744 imp/90j GSC sur cette même page) et `link whisper` (341 imp/90j).
- Conclusion mot-clé : **cibler `linkwhisper` + `link whisper` + `link whisper avis` simultanément** dans title et H1, pas seulement `linkwhisper avis`.

**Related keywords à forte SV (à intégrer en sémantique / maillage) :**

| Mot-clé | SV/mo | Pertinence |
| --- | ---:| --- |
| rank math | 880 | concurrent indirect (ne refait pas la même chose mais coexiste) — H3 dédié à la cohabitation |
| rank math seo | 720 | idem |
| seopress | 480 | alternative française premium — citer dans alternatives |
| inlinks | 390 | concurrent direct (analyseur sémantique) — citer dans alternatives |
| thruuu | 260 | outil complémentaire (NER + brief) — mention possible |
| seobility | 260 | tool SEO généraliste — pas pertinent |
| aioseo | 170 | concurrent indirect (SEO plugin avec linking) |
| internal link juicer | 40 | alternative gratuite WP — citer obligatoirement |
| interlinks manager | 10 | alternative — citer |
| linkboss | 10 | alternative récente — citer |
| link whisper alternative | 10 | requête longue tail couvrir |
| link whisper coupon code | 10 | ⭐ requête transactionnelle haute intent — section dédiée |
| link whisper discount code | 10 | ⭐ idem |
| link whisper pro | 10 | section comparatif Free vs Pro |
| link whisper black friday | 10 | section saisonnière (à activer Q4) |
| link whisper appsumo | 10 | mention historique (offre passée) |

## 4. Performance GSC sur `/link-whisper-avis/` (90 derniers jours)

| Indicateur | Valeur |
| --- | ---:|
| Impressions totales | 1 211 |
| Clics totaux | 0 |
| CTR moyen | 0,0 % |

**Top requêtes amenant des impressions :**

| Query | Imp | Position | Lecture |
| --- | ---:| ---:| --- |
| linkwhisper | 744 | 22,6 | volume #1 mais position éloignée — gap principal à fermer |
| link whisper | 341 | **8,8** | déjà top 10, très proche de la page 1 — facile à pousser |
| plugin maillage interne wordpress | 19 | 21,1 | requête longue tail à capturer |
| link whisper wordpress | 18 | 5,4 | top 5 — bonne position |
| link whisper plugin | 11 | 6,2 | top 10 |
| linkwhisper plugin | 1 | 6 | tail |
| link whisper premium wordpress plugin | 7 | 3,1 | top 3 — quasi optimal |
| link whisperer | 8 | 26,9 | typo — facilement récupérable |
| linkwisper | 8 | 6,2 | typo |
| meilleur plugin wordpress maillage interne | 3 | 14 | requête commerciale forte — à pousser |
| plugin wordpress maillage ia | 3 | 27,7 | requête émergente IA |
| seo automatic links | 2 | 9,5 | top 10 |

**Observation critique** : la requête cible de la mission `linkwhisper avis` n'apparaît pas dans le top 30 GSC. Aucun signal "avis/review" n'est envoyé. Cause probable : le H1 ne contient ni `avis` ni `linkwhisper` (en un mot). Le slug fait passer le mot, mais Google indexe principalement le H1+title pour scoring.

## 5. Gaps identifiés

### 5.1 Gap d'exact match (CRITIQUE)

| Élément | État actuel | Gap | Action étape 2 |
| --- | --- | --- | --- |
| H1 | `Link Whisper : Le Plugin WordPress Ultime pour Votre Maillage Interne ?` | aucun "avis" et aucun "linkwhisper" en un mot | refondre — proposer ex. : `LinkWhisper Avis 2026 : Mon Test Après 18 Mois sur schoolsWP` |
| Title SEO | `🚀 Link Whisper Avis 2026 : Outil SEO incontournable ?` | pas d'exact match `linkwhisper avis` (un mot), emoji 🚀 = AI slop | proposer ex. : `LinkWhisper Avis 2026 : test, prix, alternatives (mon retour)` |
| Meta desc | `Découvrez si Link Whisper est le meilleur plugin de maillage interne en 2026. Avis, fonctionnalités et alternatives pour booster votre SEO !` | "découvrez si…" = formulation passive faible. Pas de chiffre concret. | refondre avec promesse + chiffre + appel commercial discret |
| URL | `/link-whisper-avis/` | parfait | **ne pas toucher** |

### 5.2 Gap de structure H2/H3

**Article actuel (9 H2 + 5 H3)** vs **PAA SERP top 8 + headings fréquents top 17 :**

| H2/H3 manquant ou mal formulé | Score gap | Présence dans SERP |
| --- | --- | --- |
| ❌ `Link Whisper c'est quoi ?` (ou `Qu'est-ce que Link Whisper ?`) | **critique** | PAA #1 (8/17 articles) |
| ❌ `Link Whisper fonctionne-t-il avec d'autres plugins ?` | **critique** | PAA #3 (5/17) |
| ❌ `Inconvénients` ou `Limites de Link Whisper` (H2 dédié) | **critique** | 2 articles SERP avec H2 dédié |
| ❌ `Quelles sont les fonctionnalités de Link Whisper ?` | important | PAA #6 (3/17) |
| ❌ `Pourquoi le maillage interne est important ?` | important | H2 fréquent SERP (2x) |
| ❌ `Link Whisper Free vs Premium : différences` | important | webandseo (pos 6) en a une, gros différenciateur |
| ❌ `Combien coûte Link Whisper ?` (variant question de "Quel est le prix") | mineur | PAA #5 (3/17) — peut être un H3 |
| ❌ Section comparative `Link Whisper vs Internal Link Juicer / Interlinks Manager / LinkBoss` | important | aucun concurrent ne le fait bien — opportunité de différenciation |
| ❌ Section retour d'expérience schoolsWP datée et chiffrée | **critique** | unique angle qu'on peut tenir vs busilearn/webandseo |
| ❌ FAQ structurée (avec schema FAQPage) | **critique** | 0/17 articles SERP n'ont SERP FAQ — fenêtre ouverte |

**Headings actuels à conserver** (déjà solides) :
- H2 Résumé de notre expérience ⭐4,5/5 (à reformuler "Mon résumé" — voir gap 5.4)
- H2 Quel est le prix de Link Whisper ?
- H2 Link Whisper, pour qui et pour quoi ?
- H2 Quels sont les avantages de Link Whisper ?
- H3 Suggestions automatiques de liens internes
- H3 Détection et correction des liens brisés
- H3 Intégration avec l'écosystème WordPress
- H2 Liens brisés (à fusionner — actuellement doublon avec l'H3 ci-dessus)
- H2 Quelles sont les alternatives à Link Whisper ?
- H2 Avis clients sur Link Whisper
- H2 Avis final
- H2 Publications similaires (auto-généré template, OK)

### 5.3 Gap de format

| Élément | Article actuel | Top 3 SERP (busilearn, webandseo) | Action |
| --- | --- | --- | --- |
| Tableau comparatif | absent (texte uniquement) | présent (busilearn, comparatif-logiciels) | ajouter — au minimum tableau plans Free vs Premium + tableau alternatives |
| Vidéo embedded | absente | webandseo (pos 6) en a une | optionnel — à creuser si Michaël a une demo enregistrée ou peut faire un Loom rapide |
| Screenshots interface 2026 | 20 images mais pas confirmé que ce sont les UI 2026 actuelles | webandseo en a 39 récents | refresh 3-4 captures clés (suggestions, dashboard, broken links, settings) |
| FAQ schema | absent (Place/Person/etc. mais pas FAQPage) | 0 SERP en a | **ajouter — fenêtre ouverte rich result** |
| Review/AggregateRating schema | absent | non détecté SERP | **ajouter (4.5/5, n_reviews)** — opportunité étoiles SERP |
| Disclosure affilié | non vérifié dans le HTML | obligatoire schoolsWP | vérifier présence + visibilité étape 4 |
| CTA principal | non identifié dans la structure | obligatoire mission | ajouter en fin d'article (essai gratuit ou lien direct schoolswp.com/link-whisper/) |

### 5.4 Gap de voix (mémoires schoolsWP)

| Élément | État actuel | Mémoire applicable | Action |
| --- | --- | --- | --- |
| `Résumé de notre expérience` | "notre" (pluriel) | `feedback_voice_singular_solo.md` | passer en singulier : `Mon résumé après X mois` |
| Tutoiement | non vérifié dans le contenu | `BRAND_RULES.md` | check étape 3 sur tout le rendered content |
| Em-dash `—` | non vérifié | `feedback_no_em_dash.md` | check + remplacement |
| Emoji 🚀 dans title | présent | feedback implicite (AI slop) | retirer |
| Phrases 8-15 mots, paragraphes 2-4 phrases | non vérifié | brief mission | check étape 3 |

### 5.5 Gap de fraîcheur

| Élément | Schoolswp | Top concurrents | Lecture |
| --- | --- | --- | --- |
| Pub date affichée | 26 mars 2025 | webandseo : 20 juin 2022 ; netbooster : 6 avr 2022 ; nordigital : 8 jan 2022 | nous sommes le **plus récent** des reviews articles top 10 ✅ |
| MAJ visible | 29 mars 2026 | webandseo : 25 fév 2025 ; netbooster : 30 nov 2023 ; nordigital : 9 jan 2022 | nous sommes le **plus à jour** ✅ — à exploiter dans le title (`mai 2026`) |

**Lecture** : on a un avantage compétitif sur la fraîcheur. Il faut le rendre visible (date "Dernière mise à jour 8 mai 2026" en évidence en haut de l'article) plutôt que de la modifier silencieusement comme c'est le cas aujourd'hui.

### 5.6 Gap de longueur

| Source | Recommandation | Notre cible |
| --- | --- | --- |
| Audit thruuu auto | "retirer 786 mots" → 1786 mots | ❌ trop bas — méconnaît le pattern review long |
| Top 3 reviews articles (busilearn 2618, schoolswp 2572, webandseo 3084) | moyenne 2758 mots | ✅ |
| **Cible étape 3** | **2700-3000 mots rendered** | maintenir le poids actuel mais **redistribuer** : retirer les passages génériques sur le maillage, ajouter inconvénients + retour d'exp + comparatifs |

### 5.7 Gap de maillage interne entrant

GSC déclare 2 référents internes : `/slug-wordpress/` et `/seo-wordpress/`. Pour une page de stack officielle schoolsWP, c'est **insuffisant**.

**À vérifier / ajouter en étape 5 (sub-agent radar)** : ancres contextuelles depuis :
- pillar SEO WordPress (existe)
- articles maillage interne (à vérifier dans le wiki)
- articles Rank Math (mémoire `reference_wp_plugin_patterns.md` : Rank Math + Link Whisper coexistent)
- guide WordPress débutant (mention plugin essentiel)
- comparatifs plugins SEO (s'il en existe)

## 6. Synthèse — 5 leviers prioritaires pour étape 2

Par ordre d'impact estimé :

1. **Refonte H1 + Title SEO** avec exact match `LinkWhisper avis` + chiffre + signal expérience perso → leve la position sur la query principale qui n'apparaît pas en GSC (signaling)
2. **Ajout 4 H2 questions manquantes** (`c'est quoi`, `fonctionne avec d'autres plugins`, `inconvénients`, `Free vs Premium`) + FAQ schema → ferme les gaps PAA et ouvre rich result FAQ
3. **Section "Mon retour d'expérience sur schoolsWP" datée + chiffrée** → unique angle, différenciation vs busilearn/webandseo qui n'ont pas de site portfolio
4. **Tableau comparatif alternatives** (Internal Link Juicer, Interlinks Manager, LinkBoss, Inlinks, SEOPress) avec critères concrets → couvre `link whisper alternative` + related DFS
5. **Maillage interne entrant** (étape 5) — passer de 2 à 7+ référents internes via sub-agent radar

## 7. KPI baseline (mesure J+14 le 2026-05-20)

État au 2026-05-06 (dernière donnée GSC fiable) :

| KPI | Baseline | Objectif J+14 |
| --- | ---:| ---:|
| Position moyenne `linkwhisper avis` | non rankée GSC top 30 (rapport Rank Math : 33) | ≤ 20 (gain ≥ 13 places) |
| Position moyenne `linkwhisper` | 22,6 | ≤ 15 |
| Position moyenne `link whisper` | 8,8 | ≤ 6 |
| Impressions 7j sur query principale | 53 (rapport Rank Math) | +30 % → 69 |
| CTR moyen page | 0 % | > 2 % |

Si 2/3 atteints à J+14 → décliner sprint sur Tunnel de vente WordPress (cf. brief mission).

## 8. Risques & garde-fous

- **Ne pas changer le slug** `/link-whisper-avis/` (mémoire `feedback_evergreen_slugs.md` + jus historique).
- **Ne pas pusher Rank Math title/desc/focus_keyword via API** — `feedback_rank_math_via_plugin_only.md`. Préparer les valeurs en étape 2, Michaël saisit dans Gutenberg en étape 4.
- **Schema** : peut être pushé via Novamira `update-post` si le MCP redevient fonctionnel, sinon via mu-plugin schoolswp existant ou JSON-LD inline (étape 4).
- **Chiffres réels schoolsWP** : pour la section retour d'expérience, attendre Michaël (durée d'usage, nb de liens créés, gain de temps perçu, conversion suggestions/acceptées). Ne **pas inventer**.
- **Mémoire `reference_wp_plugin_patterns.md`** : ne pas flagger Link Whisper comme doublon de Rank Math — ils coexistent par design.

---

**Stop diagnostic. En attente de validation Michaël avant l'étape 2 (brief de réécriture via sub-agent `radar` + `thruuu-writer`).**
