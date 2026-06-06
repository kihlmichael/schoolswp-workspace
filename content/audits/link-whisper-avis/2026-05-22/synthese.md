---
slug: link-whisper-avis
url: https://schoolswp.com/link-whisper-avis/
date_snapshot: 2026-05-22
trigger: Demande Michaël - audit complet avec vraie data GSC + DataForSEO + thruuu (suite du sprint refresh LinkWhisper)
status: refonte-appliquee
---

# Audit Link Whisper - snapshot 2026-05-22

> Cet audit complète et **corrige** le diagnostic du sprint refresh `core/tasks/plans/linkwhisper-refresh-sprint.md`. Conclusion principale : le sprint visait `linkwhisper avis`, un mot-clé sans volume réel. La vraie data GSC réoriente la cible et la nature de l'intervention.

## 1. Contexte & déclencheur

L'article `/link-whisper-avis/` (post ID 58166, publié 2026-03-26, modifié 2026-03-29) est une page d'avis sur le plugin LinkWhisper, outil de la stack officielle schoolsWP et levier d'affiliation (code partenaire `schoolsWP10`).

Le sprint refresh ouvert en session Cowork ciblait `linkwhisper avis` avec un objectif « position top 20 sous 14 jours ». Un brief de réécriture complète a été produit et validé (`core/tasks/plans/linkwhisper-rewrite-brief.md`, Option B). Avant de lancer la réécriture, cet audit refait le diagnostic avec de la vraie data Google Search Console, DataForSEO et thruuu.

## 2. Données collectées

| Source | Périmètre | Date |
| --- | --- | --- |
| Google Search Console (MCP) | Page `/link-whisper-avis/`, 90 jours (2026-02-21 -> 2026-05-22), requêtes + tendance + URL inspection | 2026-05-22 |
| DataForSEO (API directe) | Volumes FR, related, suggestions, SERP organique, search intent | 2026-05-22 |
| thruuu | Audit on-page + SERP top 18 sur `linkwhisper avis` (google.fr, desktop, FR) | 2026-05-22 |
| WP REST | Contenu publié actuel (`article-current-snapshot.md`) | 2026-05-22 |

Fichiers bruts colocalisés dans ce dossier : `gsc-90d.json`, `gsc-trend-daily.json`, `gsc-url-inspect.json`, `dataforseo-*.json`, `dataforseo-google-sheet.csv`, `thruuu-raw/`.

Google Sheet des volumes : **schoolsWP - Volumes SEO - Link Whisper - 2026-05-22** (`https://docs.google.com/spreadsheets/d/1WfZf_tIQ_2UjmkWaBEVIcmbcsZ_a97edTEz0lI4Wug8/`).

## 3. État de l'article

- **Titre SEO (balise title)** : `🚀 Link Whisper Avis 2026 : Outil SEO incontournable ?` (54 caractères)
- **H1** : `Link Whisper : Le Plugin WordPress Ultime pour Votre Maillage Interne ?`
- **Meta description** : `Découvrez si Link Whisper est le meilleur plugin de maillage interne en 2026. Avis, fonctionnalités et alternatives pour booster votre SEO !` (140 caractères)
- **Longueur** : 2567 mots (comptage thruuu) / 2918 mots (comptage WP) - dans la moyenne SERP (2417)
- **Images** : 20 (moyenne SERP : 20)
- **Structure** : 9 H2, 7 H3. Plan : Résumé d'expérience 4,5/5, Prix, Pour qui, Avantages, Correction liens brisés, Alternatives, Avis clients, Avis final.
- **Schema présent dans le code** : Place, EducationalOrganization, Organization, WebSite, ImageObject, BreadcrumbList, WebPage, Person, BlogPosting.
- **Schema validé par Google (URL inspection)** : **Breadcrumbs uniquement**. Pas de Review/AggregateRating ni FAQPage reconnu, malgré la note 4,5/5 affichée et les 7 titres-questions.

État technique (URL inspection GSC) : indexée (PASS, « Submitted and indexed »), canonical correct, crawl mobile autorisé. **Dernier crawl Googlebot : 2026-04-23** (il y a environ un mois). Seulement **2 liens internes** pointent vers la page (`/slug-wordpress/`, `/seo-wordpress/`).

## 4. SEO actuel - le constat central (GSC 90 jours)

**Total page** : 1343 impressions, **3 clics**, CTR **0,22 %**, position moyenne **13,9**.

Répartition par requête (28 requêtes nommées, 1137 impressions ; les 206 impressions restantes = requêtes rares masquées par GSC) :

| Requête | Impressions | Clics | Position |
| --- | --- | --- | --- |
| `linkwhisper` | 632 | 0 | **20,6** |
| `link whisper` | 384 | **1** | **8,6** |
| `link whisper wordpress` | 22 | 0 | 5,4 |
| `linkwisper` (typo) | 9 | 0 | 6,1 |
| `link whisper plugin` | 9 | 0 | 5,9 |
| autres longue traîne / typos | < 10 chacune | 0 | variable |

**Trois faits qui changent tout :**

1. **`linkwhisper avis` n'existe pas dans GSC.** Sur 90 jours, **aucune requête contenant « avis »** ne génère d'impression mesurable. Croisé avec DataForSEO (aucun volume mesurable sur `linkwhisper avis` / `link whisper avis`) et thruuu (onglet Search Volume vide) : le mot-clé que le sprint voulait conquérir est un **mot-clé fantôme**. La page est déjà #2 dessus (thruuu + SERP DataForSEO live le confirment), et cela ne rapporte rien parce que personne ne le tape.

2. **Le vrai trafic potentiel est sur deux requêtes** : `linkwhisper` (632 impressions, position 20,6, volume 480/mois, intention navigationnelle) et `link whisper` (384 impressions, position 8,6, volume 390/mois, intention informationnelle). `link whisper` est la **seule** requête qui a produit un clic en 90 jours.

3. **La page ne convertit quasiment rien** : 3 clics pour 1343 impressions. Le goulot n'est pas la qualité du contenu, c'est la **position** : `linkwhisper` est en page 2-3 (structurellement 0 clic possible) et `link whisper` est en bas de page 1 (CTR plancher). La position quotidienne oscille violemment (min 4,6 / max 37) sans tendance nette - signe d'une page aux signaux faibles que Google n'arrive pas à situer.

## 5. SERP analysée (thruuu + DataForSEO)

SERP `linkwhisper avis` (google.fr, FR, 22 mai) - schoolsWP est **#2** :

| Pos | Domaine | Mots | Note |
| --- | --- | --- | --- |
| 1 | blogdumoderateur.com | **313** | Fiche annuaire très courte |
| **2** | **schoolswp.com** | **2567** | Le résultat éditorial le plus complet du top |
| 3 | youtube.com | - | Vidéo |
| 4 | appvizer.fr | 778 | Annuaire SaaS |
| 5 | debugbar.com | 1295 | Article 2023 |
| 6 | netbooster.fr | 1359 | Article 2022 |
| 7 | fr.wordpress.org | 7074 | Page officielle plugin |
| 8 | busilearn.fr | 2618 | Avis e-commerce |
| 10-11 | webandseo.fr | 3084 | Article + vidéo, MAJ 2025 |

**Audit on-page thruuu : quasiment tout au vert.** Word count bon, nombre d'images bon, Page Rank dans la fourchette des concurrents (28 vs SERP 31), longueur de titre et de meta bonnes, 7 questions dans les titres (moyenne SERP : 3), « angle unique » salué, couverture des termes fréquents bonne. **Une seule erreur** : le titre contient `link whisper avis` mais pas l'exact match `linkwhisper avis` (remarque mineure, sans enjeu réel vu le point 4.1).

**Gaps de structure vs SERP** (titres les plus fréquents chez les concurrents, absents de la page) :
- `Link Whisper c'est quoi ?` / `What is Link Whisper ?` : titre H2 le plus fréquent de toute la SERP (14 occurrences). La page n'a pas de section « définition » claire.
- H2 dédié aux **fonctionnalités** : chez les concurrents c'est un H2 à part ; sur la page elles sont enterrées en H3 sous « avantages ».
- Pas de **bloc FAQ structuré** (les concurrents en ont, et c'est un déclencheur de rich result).

Terme NLP manquant signalé par thruuu : `google search console` (0 occurrence sur la page, 2-3 chez les concurrents).

**Tendance du volume (DataForSEO, 14 mois)** : `link whisper` a culminé à **1900** en mars 2025, puis chute à 90-170 fin 2025, rebond à 480 en février-mars 2026, retombé à **170** en avril 2026. Le cluster est en **déclin structurel** (environ -80 % vs pic). Volume courant retenu : `link whisper` 390/mois, `linkwhisper` 480/mois. KD 7 dans les deux cas (facile).

## 6. Insights critiques

1. **Le sprint refresh visait la mauvaise cible.** `linkwhisper avis` = 0 volume. La page y est déjà #2 pour rien. Le brief de réécriture complète (`linkwhisper-rewrite-brief.md`) repose donc sur une prémisse fausse et ne doit pas être exécuté tel quel.

2. **La vraie cible est `link whisper`** (informationnel, 390/mois, KD 7, position actuelle 8,6). L'amener en top 5 est le gain réaliste et atteignable. `linkwhisper` (navigationnel, 480/mois, position 20,6) est un objectif secondaire plus dur : sur une requête navigationnelle, Google privilégie le site officiel et wordpress.org.

3. **Le problème n'est pas le contenu, ce sont les signaux.** L'audit thruuu est quasi tout vert. Ce qui bloque la page : seulement 2 liens internes entrants, dernier crawl il y a un mois, aucun rich result hors fil d'Ariane, position instable. Ce sont des leviers techniques et de maillage, pas de rédaction.

4. **CTR plombé par l'absence d'étoiles dans la SERP.** La page affiche une note 4,5/5 dans son contenu mais aucun schema Review/AggregateRating n'est validé par Google. Un rich result étoiles sur une page d'avis est le levier CTR le plus rentable ici.

5. **Plafond de trafic faible : calibrer l'effort.** Le cluster est en déclin (-80 % depuis le pic). Même en top 5 sur `link whisper`, l'ordre de grandeur réaliste est environ 30-40 clics/mois. La page reste une money page d'affiliation à entretenir, mais elle ne justifie pas une réécriture lourde de 10-12 h.

## 7. Décision

**Refresh léger ciblé (technique + signal). PAS la réécriture complète du brief existant.**

Justification : le contenu est déjà compétitif (thruuu quasi tout vert, #2 SERP, 2567 mots dans la moyenne). Le déficit est sur les signaux (maillage, schema, fraîcheur de crawl) et sur le ciblage du mot-clé. Une réécriture complète sur la base du brief actuel investirait 10-12 h sur une prémisse de mot-clé fausse, pour un plafond de trafic faible. Principe : changement chirurgical, effort calibré sur le potentiel.

Ce qui reste **valable** dans le travail du sprint : les chiffres d'expérience réelle de Michaël (195 liens internes créés, 449 articles analysés, 207 clics trackés, 144 liens cassés détectés) et les encarts Kadence Option B. Ces éléments renforcent l'E-E-A-T et sont à intégrer dans le refresh léger, indépendamment du reste du brief.

**Arbitrage final : Michaël.** Cet audit recommande ; la validation du périmètre (refresh léger vs réécriture) lui revient.

## 8. Plan d'action (refresh léger, effort estimé 3-4 h)

1. **Maillage interne (levier #1)** : passer de 2 à 8-10 liens internes contextuels vers `/link-whisper-avis/` depuis des articles SEO / maillage interne / plugins WordPress. Ancres variées autour de « link whisper » et « maillage interne ». -> sub-agent `radar`. Vérif : compter les liens entrants après coup.
2. **Titre SEO** : retirer l'emoji 🚀 et l'année « 2026 » figée, garder « Link Whisper » et « avis » en tête. Cible orientée `link whisper`, pas `linkwhisper avis`. Modif via Gutenberg/Rank Math, jamais via API. Vérif : balise title rendue.
3. **Schema Review + FAQPage** : exposer la note 4,5/5 en AggregateRating valide + ajouter un vrai bloc FAQ structuré. Vérif : URL inspection -> rich results doivent lister Review et FAQ.
4. **Enrichissement chirurgical du contenu** : ajouter un H2 « Link Whisper, c'est quoi ? » (définition courte, titre le plus fréquent de la SERP), remonter les fonctionnalités en H2 dédié, ajouter une section FAQ répondant aux questions fréquentes de la SERP, glisser le terme `google search console`. Intégrer les encarts Kadence Option B avec les chiffres d'expérience réels. Pas de réécriture du corps existant.
5. **Signal de fraîcheur** : après publication, date « dernière mise à jour » + URL inspection GSC -> demande d'indexation + ping IndexNow.

## 9. Métriques de suivi (prochain snapshot)

KPI recalibrés sur les vrais mots-clés (abandon de l'objectif « top 20 sur linkwhisper avis ») :

1. **Position `link whisper`** : 8,6 -> objectif **top 5**.
2. **Position `linkwhisper`** : 20,6 -> objectif **top 10**.
3. **Clics page 90 j** : 3 -> objectif **> 20**.
4. **Rich results** : Breadcrumbs seul -> objectif **Breadcrumbs + Review + FAQ** validés.
5. **Liens internes entrants** : 2 -> objectif **8-10**.

Prochain snapshot conseillé : 4 à 6 semaines après le refresh (vers 2026-07-01). Créer alors un `_diff.md` comparant positions, requêtes et rich results à ce snapshot.

## 10. Exécution du déploiement (2026-05-22, soir)

Refresh léger appliqué en production. Détail :

| Action | Statut | Détail |
| --- | --- | --- |
| Contenu refondu + H1 | Fait | Post 58166, 32 062 caractères, push WP REST `2026-05-22T19:00`. H1 : `Link Whisper : le plugin WordPress qui automatise ton maillage interne`. 15/15 vérifications structurelles (10 H2, 12 H3, 2 CTA, 3 encarts, FAQ, section « c'est quoi », gradient Kadence intact). |
| Rank Math | Fait | Titre SEO `Link Whisper : mon avis après 21 mois de maillage interne` + meta description reciblée + focus keyword `link whisper`. Appliqué via `rankmath/v1/updateMeta`, vérifié sur le HTML public. |
| Maillage interne | Fait | 8 liens entrants contextuels ajoutés (objectif 8-10 atteint). Vague 1 : `thot-seo-avis`, `avis-linkcentral-wordpress`, `core-web-vitals-wordpress`, `changer-extension-seo-wordpress`. Vague 2 : `surerank-avis-plugin-seo`, `avis-chatseo-test-complet`, `wisewand-avis-redaction-seo`, `avis-skoatch`. Total entrant : 6 existants + 8 = environ 14. Optionnel `wisewand-vs-skoatch` non fait. Backups dans `sandbox-workspace/linking-backups/`. |
| Date de MAJ | Fait | `post_modified` = 2026-05-22 (mis à jour par le push de contenu). |
| Inspection GSC | Fait | Page indexée, verdict PASS. Dernier crawl Googlebot 2026-04-23 (antérieur à la refonte). Détail : `gsc-post-refresh-inspect.json`. |
| Schema Review + FAQPage | En attente | Novamira MCP cassé : application manuelle dans Rank Math par Michaël. Valeurs exactes : `schema-rank-math-spec.md`. |

**Bloqueur résolu en cours de session** : schoolswp.com était derrière un challenge anti-bot JS (openresty) qui empêchait tout push automatisé. Michaël a fait lever la protection côté hébergeur avant le déploiement.

**Action manuelle restante pour Michaël** :

1. Ajouter les schemas Review + FAQPage dans Rank Math (cf. `schema-rank-math-spec.md`).
2. Demander une indexation de l'URL dans GSC (l'API ne permet pas le recrawl prioritaire).

## 11. Compléments 2026-05-22 (2e passe)

Demandes complémentaires de Michaël après le déploiement initial :

| Action | Statut | Détail |
| --- | --- | --- |
| Image à la une FR | Fait | Ancien visuel en allemand remplacé par un hero éditorial FR (style validé OttoKit) : carte verdict 4,5/5 + chiffres schoolsWP. Media `2932527`, alt + titre SEO. Ancien media DE `58636` orphelin, supprimé depuis (cf. section 12). Source : `assets/featured-images/post-58166/`. |
| FAQ en accordéon Kadence | Fait | Section FAQ texte (H2 + 6 H3/paragraphes) remplacée par une rangée Kadence (2 accordéons, 6 panes) fournie par Michaël, traduite en FR, remplie avec les 6 Q/R. Round-trip byte-exact. |
| Bloc Ninja Tables | Fait | Shortcode `[ninja_tables id="58431"]` remplacé par le bloc `ninja-tables/guten-block` (table 58431 inchangée). |
| Lien maillage #9 | Fait | `wisewand-vs-skoatch` lie désormais l'article. Total maillage entrant : **9 liens** ajoutés cette session. |
| Schema | Fait | `BlogPosting` + `Review` (4,5/5, SoftwareApplication Link Whisper) + `FAQPage` (6 Q/R) appliqués via l'endpoint Rank Math `updateSchemas`. Vérifié : JSON-LD public = 1 de chaque, zéro doublon. La FAQPage est imbriquée sous `BlogPosting.subjectOf` (comportement standard Rank Math, valide). |

Méthode schema retenue : REST `rankmath/v1/updateSchemas` (Novamira indisponible). Détail technique consigné dans la mémoire `reference_rank_math_schema_postmeta`.

## 12. Compléments 2026-05-22 (3e passe : versions DE/EN + planification du snapshot)

Nettoyage du visuel hérité et planification du point de contrôle prévu en section 9.

| Action | Statut | Détail |
| --- | --- | --- |
| Image à la une DE | Fait | L'article DE #58572 (`/de/link-whisper-erfahrungsbericht/`) utilisait encore le visuel `58636` (texte allemand, ancien style). Remplacé par un hero éditorial DE au style validé (titre « mein Test », carte « Mein Fazit » 4,5/5). Media `2932818`. Source : `assets/featured-images/post-58166/slide-00-hero-de.html`. |
| Image à la une EN | Fait | L'article EN #58580 (`/en/link-whisper-review/`) utilisait lui aussi `58636` : un visuel à texte allemand sur une page anglaise, soit une incohérence de langue. Remplacé par un hero éditorial EN (titre « my review », carte « My verdict » 4.5/5). Media `2932822`. Source : `assets/featured-images/post-58166/slide-00-hero-en.html`. |
| Suppression media 58636 | Fait | Après réassignation vérifiée des deux articles et contrôle qu'aucune page ne référence plus le visuel, le media `58636` a été supprimé (`DELETE force=true`, HTTP 404 confirmé). |
| Snapshot 2026-07-01 | Programmé | Le point de contrôle de la section 9 (4 à 6 semaines après le refresh) est planifié via une routine Claude Code distante one-shot : `trig_01LgU9Ei26gwnBuEuMMhjftQ`, déclenchement 2026-07-01 à 09:00 Paris. La routine scaffolde le dossier `2026-07-01/` et prépare la checklist des mesures GSC et DataForSEO à relever, l'agent distant n'ayant pas accès à ces deux sources. |

Les trois versions linguistiques de l'article Link Whisper (FR #58166, DE #58572, EN #58580) partagent désormais le même hero éditorial, chacune dans sa langue. Pipeline images : mémoire `featured-images-via-html-playwright-fallback-ia`.
