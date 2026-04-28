---
name: seo-pipeline
description: (archivé - pipeline 10 tâches trop lourd - ne pas auto-déclencher - invocation manuelle uniquement)
---

> **Statut : archivé le 2026-04-16.**
> Ce skill (orchestration 10 tâches SEO : T1 Inventaire, T2 Crawl, T3 GSC, T4 DataForSEO, T5 Clusters, T6 Maillage, T7 Multilingue, T8 E-E-A-T, T9 Conversion, T10 Roadmap) ne se déclenche plus automatiquement.
> Raison : méga-skill trop lourd, hors périmètre naturel du cluster cocon, risque de sur-déclenchement sur "audit SEO" générique, ambiguïté avec les autres skills SEO plus ciblés.
> Réouverture possible plus tard en cluster séparé "Audit / Pipeline / Ops SEO" si certaines briques (T3 GSC, T4 DataForSEO, T8 E-E-A-T) s'avèrent utiles en skills granulaires.
> Conservation pour référence uniquement. Accès via tool `Skill` en invocation explicite.

# Pipeline SEO schoolsWP — Système d'exécution multi-agents

## Architecture

```
ORCHESTRATEUR
  ↓
Phase 0 — Audit workspace
  ↓
Phase 1 — Cartographie Skills
  ↓
Phase 2 — 10 Agents spécialisés (séquentiels)
         + 3 Agents support (transversaux)
  ↓
Phase 3 — Livrables (Sheets / Docs / Roadmap)
  ↓
Phase 4 — Contrôle qualité
```

**Source de vérité :** `projects/schoolswp/systems/seo-workflow/`
Lire chaque fiche avant d'exécuter la tâche correspondante.

---

## RÈGLES IMPÉRATIVES (toujours actives)

1. **Auditer le workspace avant toute action** — lire les fichiers existants, ne pas réinventer.
2. **Utiliser les Skills existants en priorité** — les créer seulement si aucun ne couvre le besoin.
3. **Jamais inventer de données** — toute donnée non prouvée → `[À VALIDER]`.
4. **Traçabilité obligatoire** — chaque recommandation porte son type explicitement :
   - `Observable :` donnée visible sans outil externe
   - `Hypothèse à valider :` nécessite GSC / crawl / API pour confirmer
   - `Bonne pratique :` recommandation Google Search Central ou outil SEO documenté
5. **Un agent = une responsabilité** — ne pas regrouper deux tâches dans un seul agent.
6. **Chaque agent lit seulement sa fiche** — ne pas charger tout le contexte global.
7. **Sortie structurée obligatoire** — format tableau + résumé + actions suivantes.
8. **Ne jamais bloquer sur un input manquant** — créer le placeholder, noter le blocage, continuer.

---

## PHASE 0 — Audit workspace

**Avant de démarrer, lire et mapper ce qui existe :**

```
projects/schoolswp/systems/seo-workflow/
├── orchestrator.md               ← prompt orchestrateur principal
├── tasks/01-10 *.md              ← 10 fiches tâches complètes
├── skills/
│   ├── seo-crawl-hygiene.md      → utilisée par Agent 02
│   ├── gsc-opportunity-scanner.md → utilisée par Agent 03
│   ├── hreflang-multilang-auditor.md → utilisée par Agent 07
│   └── eeat-template-builder.md  → utilisée par Agent 08
├── templates/
│   ├── sheets-schema.md          ← schémas de tous les onglets Sheets
│   └── docs-template.md          ← gabarits Google Docs
├── diagrams/
│   ├── workflow-overview.mmd
│   └── n8n-flow.mmd
├── n8n/seo-workflow.json         ← workflow n8n exporté
├── roadmap/roadmap-30-60-90.md   ← roadmap structurée
└── reports/
    ├── impact-effort-matrix.md
    └── quick-wins.md             ← QW avec suivi statut
```

**Skills Claude Code réutilisables :**

| Skill                      | Tâche           | Usage                         |
| -------------------------- | --------------- | ----------------------------- |
| `firecrawl`                | T1              | Scraping sitemap + pages      |
| `seo-audit`                | T1/T2           | Analyse SEO générale          |
| `schoolswp-fast-websearch` | T4              | Recherche concurrents via Exa |
| `n8n-workflow-patterns`    | T1-T10          | Patterns n8n                  |
| `n8n-code-javascript`      | n8n intégration | Code nodes                    |
| `geo-architect`            | T3/T5           | Clusters et GEO pipeline      |

**État des lieux à produire au démarrage :**

- Ce qui existe → ce qui peut être réutilisé → ce qui manque → ce qui va être créé

---

## PHASE 1 — Convention entrée / sortie

### Format d'entrée standard (tous agents)

```
Site : schoolsWP.com
Tâche : [nom]
Fiche : [chemin tasks/0N-xxx.md]
Données disponibles : [fichiers, exports, URLs]
Données manquantes : [À VALIDER — instruction de récupération]
```

### Format de sortie standard (tous agents)

```
## [Nom agent] — Rapport

**Résumé** (3-5 lignes)

**Tableau principal** (colonnes selon tâche)

**Top constats**
- Observable : ...
- Hypothèse à valider : ...
- Bonne pratique : ...

**Recommandations** (priorisées P1/P2/P3)

**Actions suivantes** (avec agent/outil cible)

**Blocages / données manquantes** (avec instruction récupération)
```

---

## PHASE 2 — Agents spécialisés

### Agents principaux (1 par tâche)

---

#### Agent 01 — SEO Inventory Mapper

**Fiche :** `tasks/01-inventaire-seo.md`
**Outil :** Firecrawl + skill `seo-audit`
**Sortie :** onglet `01_URL_INVENTORY`
**Gate :** ≥80% des URLs classifiées

```
Lis d'abord : tasks/01-inventaire-seo.md

RÔLE : Analyste SEO éditorial spécialisé en architecture WordPress
SITE : schoolsWP.com

INPUTS :
- Plan de site : https://schoolswp.com/plan-de-site
- Menu principal (observable)
- Pages listées en page d'accueil (observable)
[Coller ici les données récupérées]

ACTIONS :
1. Extrais toutes les URLs depuis les inputs
2. Pour chaque URL : type_page | cluster | langue | role_SEO | role_business
3. Priorise : P1 (piliers/pages money critiques) | P2 | P3
4. Note les observables (visible directement) et hypothèses (à valider via GSC/crawl)

RÈGLE DE PREUVE :
- Observable = affirmer
- Hypothèse = marquer [À VALIDER + comment vérifier]

FORMAT :
Tableau CSV : url | type_page | cluster | langue | role_SEO | role_business | priorité | observation | notes
Puis : résumé 5 lignes + liste hypothèses à valider

VALEURS type_page : hub | categorie | article | page-conversion | outil | statique
VALEURS cluster : SEO | LMS | Automatisation | Hébergement | Performance | Plugins | Affiliation | Business
VALEURS role_SEO : pilier | support | money | orpheline
VALEURS role_business : lead | affilie | vente | support | newsletter

CONDITIONS D'ARRÊT :
- Toutes les URLs classifiées
- Chaque URL a type_page + cluster + role_SEO
- Observables et hypothèses distingués explicitement
```

---

#### Agent 02 — Crawl & Index Hygiene Auditor

**Fiche :** `tasks/02-crawl-indexation.md`
**Skill :** `seo-crawl-hygiene` (dans `systems/seo-workflow/skills/`)
**Outil :** Export crawl CSV + skill `seo-audit`
**Entrées :** crawl export + `01_URL_INVENTORY`
**Sortie :** onglet `02_INDEXATION_AUDIT`
**Gate :** ≥1 action noindex/redirect identifiée

```
Lis d'abord : tasks/02-crawl-indexation.md + skills/seo-crawl-hygiene.md

RÔLE : Auditeur technique SEO spécialisé WordPress
SITE : schoolsWP.com

INPUTS :
[Coller export crawl CSV — colonnes : url, statut_http, canonical, meta_robots, inlinks]
[01_URL_INVENTORY disponible depuis T1]

ZONES À RISQUE (WordPress) :
- Archives tags, auteur, date → noindex via Rank Math
- Pages login / portail assistance → noindex ou exclusion sitemap
- Feeds RSS → noindex
- Pagination profonde → canonical vers page-1 ou noindex
- Trailing slash / www vs non-www → canonical cohérent
- Chaînes de redirections A→B→C → consolider en A→C
- Statuts 4xx sur pages P1 de 01_Inventory → critique

ACTIONS :
1. Lister par type : pages inutiles en index
2. Vérifier les statuts HTTP ≠ 200 sur pages P1
3. Détecter les canonical incorrects ou manquants
4. Pour chaque problème : décision conserve | noindex | redirect | canonical | supprime
5. Prioriser par impact SEO

FORMAT :
Tableau : url_or_pattern | risque | cause | action | impact (H/M/L) | effort (XS/S/M/L) | priorité
Section "Quick wins techniques à lancer cette semaine"
Section "À valider avec crawl complet Screaming Frog"
```

---

#### Agent 03 — GSC Opportunity Analyst

**Fiche :** `tasks/03-analyse-gsc.md`
**Skill :** `gsc-opportunity-scanner` (dans `systems/seo-workflow/skills/`)
**Outil :** Export GSC CSV (Performance + Coverage)
**Entrées :** exports GSC 28j/3m/12m + `01_URL_INVENTORY`
**Sortie :** onglet `03_GSC_ANALYSIS`
**Gate :** ≥10 mots-clés par cluster extraits

```
Lis d'abord : tasks/03-analyse-gsc.md + skills/gsc-opportunity-scanner.md

RÔLE : Consultant SEO spécialisé Google Search Console
SITE : schoolsWP.com

INPUTS :
[Coller export GSC Performance — colonnes : url, requête, impressions, clics, CTR, position]
[Si disponible : export GSC Coverage / Index]

ANALYSES PRIORITAIRES :
1. Position 4-15 + impressions > 500 → quick win CTR/position
2. Position 1-3 + CTR < 2% → problème title/meta description
3. Même requête sur 2+ URLs → cannibalisation probable [Hypothèse à valider]
4. Pages 01_Inventory P1 non visibles dans GSC → problème indexation [À VALIDER]
5. Tendances 28j vs 3m vs 12m → pages en chute ou en hausse

FORMAT :
Tableau : url | requête | impressions | clics | CTR | position | type_analyse | diagnostic | action | priorité
Top 10 quick wins GSC
Top 10 pages à retravailler
Cas probables de cannibalisation
Section Coverage (si données disponibles)
```

---

#### Agent 04 — DataForSEO Competitive Analyst

**Fiche :** `tasks/04-benchmark-dataforseo.md`
**Skill :** `schoolswp-fast-websearch` pour compléter si API indisponible
**Outil :** DataForSEO API (ou Exa WebSearch en fallback)
**Entrées :** clusters `01_URL_INVENTORY` + mots-clés `03_GSC_ANALYSIS`
**Sortie :** onglet `04_COMPETITOR_GAP`
**Gate :** ≥3 gaps concurrentiels identifiés

```
Lis d'abord : tasks/04-benchmark-dataforseo.md

RÔLE : Analyste SEO concurrentiel expert en DataForSEO
SITE : schoolsWP.com

INPUTS :
[Résultats DataForSEO API — organic competitors, keyword gap]
[Clusters identifiés en T1 : SEO | LMS | Automatisation | Hébergement | Performance | Plugins]
[Mots-clés issus de T3 (GSC)]
FALLBACK si API indisponible : utiliser skill schoolswp-fast-websearch sur les SERPs cibles

CONCURRENTS À ANALYSER (hypothèses à affiner) :
wpmarmite.com | codeinwp.com | wpbeginner.com | blogpascher.com | kinsta.com/fr

ACTIONS :
1. Identifier les concurrents SEO réels par overlap sémantique (pas seulement notoriété)
2. Pour chaque cluster P1 (SEO, LMS, Automatisation) : qui domine et pourquoi
3. Mots-clés top 3 concurrent + absent schoolsWP → gap critique
4. Angle différenciant schoolsWP à exploiter : "WordPress & Business" vs "WordPress généraliste"

RÈGLE DE PREUVE :
- Toute position concurrente = Observable si vérifiée via SERP / DataForSEO
- Volume de recherche estimé = Hypothèse à valider via DataForSEO

FORMAT :
Tableau : concurrent | cluster | mot_cle | schoolswp_présent | niveau_gap | opportunité | angle | priorité
Top opportunités par cluster (SEO, LMS, Automatisation en priorité)
Recommandations positionnement différenciant
```

---

#### Agent 05 — Cluster & Cannibalization Strategist

**Fiche :** `tasks/05-clusters-cannibalisation.md`
**Skills :** `cluster-cocon-automatique` + `topical-authority-map` + `geo-architect`
**Entrées :** `01_URL_INVENTORY` + `03_GSC_ANALYSIS` + `04_COMPETITOR_GAP`
**Sortie :** onglet `05_CLUSTERS_MAP`
**Gate :** chaque cluster P1 a une page pilier définie

```
Lis d'abord : tasks/05-clusters-cannibalisation.md

RÔLE : Expert en architecture éditoriale SEO et topical authority
SITE : schoolsWP.com

INPUTS :
[01_URL_INVENTORY — URLs classifiées par cluster]
[03_GSC_ANALYSIS — requêtes vs pages (données cannibalisation)]
[04_COMPETITOR_GAP — gaps à couvrir]

ACTIONS :
1. Pour chaque cluster : page pilier existante (ou manquante) + satellites existants
2. Requêtes GSC sur 2+ pages du même cluster → cannibalisation [À valider : voir positions réelles]
3. Pour chaque cannibalisation : garder+améliorer | fusionner+301 | définir canonical
4. Gaps par cluster (sujets non couverts, vs concurrents T4)
5. Pages /category/xxx = archives list → à transformer en pages piliers éditorialisées

VALEURS :
- complete : oui | partiel | non
- cannibal_risk : haut | moyen | faible | aucun
- action : renforcer | fusionner | rediriger | créer | archiver

FORMAT :
Tableau : cluster | pilier_url | satellites_urls | complete | cannibal_risk | gaps_keywords | action
Top 3 clusters à densifier
Top 10 contenus à fusionner / repositionner avec action recommandée
```

---

#### Agent 06 — Internal Linking Architect

**Fiche :** `tasks/06-maillage-interne.md`
**Skill :** `m1m3-urls-internal-linking`
**Entrées :** `05_CLUSTERS_MAP` + `01_URL_INVENTORY` + `03_GSC_ANALYSIS`
**Sortie :** onglet `06_INTERNAL_LINKING`
**Gate :** ≥10 liens recommandés

```
Lis d'abord : tasks/06-maillage-interne.md

RÔLE : Spécialiste maillage interne SEO pour sites WordPress monétisés
SITE : schoolsWP.com

INPUTS :
[05_CLUSTERS_MAP — structure piliers/satellites]
[01_URL_INVENTORY — pages money, hubs, articles]
[03_GSC_ANALYSIS — mots-clés cibles par page]

LOGIQUE DE MAILLAGE :
- Homepage → 5-7 pages piliers (pas seulement derniers articles) [Bonne pratique]
- Article informationnel → money page du même cluster [Observable : liens actuels]
- Page satellite → page pilier (lien "vers le haut" systématique)
- Chaque nouvel article → 3 anciens articles doivent pointer vers lui
- Liens contextuels dans le corps > liens "articles similaires" automatiques [Bonne pratique]

ACTIONS :
1. Pages P1 avec < 3 inlinks → renforcer en priorité
2. Articles sans lien vers leur pilier → ajouter lien "vers le haut"
3. Pages money sans lien depuis articles informationnels → maillage commercial manquant
4. Protocole réplicable pour chaque futur article

FORMAT :
Tableau : source | cible | type_lien | ancre_recommandée | raison_SEO | raison_business | priorité
Logique homepage | logique hub→sous-hub | logique article→money
Protocole à appliquer sur chaque nouvel article
```

---

#### Agent 07 — International SEO Auditor

**Fiche :** `tasks/07-seo-multilingue.md`
**Skill :** `hreflang-multilang-auditor` (dans `systems/seo-workflow/skills/`)
**Entrées :** `01_URL_INVENTORY` (pages EN/DE) + export crawl
**Sortie :** onglet `07_INTERNATIONAL_SEO`
**Gate :** toutes les pages FR auditées

```
Lis d'abord : tasks/07-seo-multilingue.md + skills/hreflang-multilang-auditor.md

RÔLE : Expert SEO international et multilingue spécialisé WordPress
SITE : schoolsWP.com (FR / EN / DE)

INPUTS :
[01_URL_INVENTORY — pages classifiées par langue]
[Export crawl avec colonnes hreflang, canonical, lang=]

DIAGNOSTIC À ÉTABLIR :
Observable : version FR riche vs EN/DE probablement plus faibles (à confirmer par comptage pages)
Hypothèse à valider : balises hreflang absentes ou incorrectes → Google voit des pages concurrentes
Bonne pratique : hreflang doit former une boucle complète FR→EN→DE→FR sur chaque triplet de pages

RISQUES À DÉTECTER :
1. Pages EN/DE sans hreflang → duplication perçue par Google
2. Pages EN/DE avec peu de contenu → signal qualité négatif sur le domaine
3. Consommation budget crawl sur contenu faible [Bonne pratique : noindex si < 300 mots réels]
4. Canonical EN/DE pointant vers FR → signifie que la version EN/DE est déclarée dupliquée

DÉCISION STRATÉGIQUE À FORMULER :
Option A : noindex /en/ et /de/ → concentrer 100% autorité sur FR [Recommandée si parité < 30%]
Option B : engagement total parité éditoriale → seulement si ressources disponibles

FORMAT :
Tableau : élément_analysé | type (Observable/Hypothèse/Bonne pratique) | risque | action | priorité
Checklist hreflang / canonical / structure URL
Recommandation stratégique multilingue (A ou B + justification)
```

---

#### Agent 08 — E-E-A-T Editorial Reviewer

**Fiche :** `tasks/08-eeat-credibilite.md`
**Skill :** `eeat-template-builder` (dans `systems/seo-workflow/skills/`)
**Entrées :** `01_URL_INVENTORY` pages P1 + `05_CLUSTERS_MAP` piliers
**Sortie :** onglet `08_EEAT`
**Gate :** ≥5 pages auditées

```
Lis d'abord : tasks/08-eeat-credibilite.md + skills/eeat-template-builder.md

RÔLE : Consultant SEO éditorial expert E-E-A-T sur sites WordPress monétisés
SITE : schoolsWP.com | Auteur : Michael KIHL

INPUTS :
[URLs pages piliers à auditer depuis 01_URL_INVENTORY et 05_CLUSTERS_MAP]

SIGNAUX À ÉVALUER :
Experience (E) :
- Captures backend présentes dans les articles de test [Observable]
- Mentions "dans mon cas", "sur schoolsWP", "j'ai testé" [Observable]
- Vidéos d'utilisation réelle de l'outil [Observable]

Expertise (E) :
- Bio auteur présente et complète (photo, credentials, LinkedIn) [Observable]
- Date publication + mise à jour visible [Observable]
- Sources citées, données chiffrées référencées [Observable]

Authoritativeness (A) :
- Mentions de presse, certifications, partenariats [Observable]
- Page À Propos avec vrai profil Michael KIHL [Observable]

Trustworthiness (T) :
- Disclosure affiliation visible ET claire [Observable — absent = problème]
- HTTPS, mentions légales, politique confidentialité [Observable]
- Avis clients sur pages de vente [Observable]

FORMAT :
Tableau : url | signal_EEAT | type | présence_actuelle | faiblesse | amélioration | impact | priorité
Templates à produire (copiables dans les gabarits WordPress) :
- Bloc "méthode de test" (pour articles de test plugins)
- Bloc "transparence affiliation" (pour articles affiliés)
- Bloc "pour qui / pas pour qui" (pour comparatifs)
```

---

#### Agent 09 — SEO Business Conversion Analyst

**Fiche :** `tasks/09-conversion-seo.md`
**Skill :** `money-pages-framework`
**Entrées :** `01_URL_INVENTORY` pages money + `05_CLUSTERS_MAP` + `08_EEAT`
**Sortie :** onglet `09_CONVERSION_SEO`
**Gate :** ≥3 parcours de conversion définis

```
Lis d'abord : tasks/09-conversion-seo.md

RÔLE : Consultant CRO + SEO spécialisé médias de niche WordPress monétisés
SITE : schoolsWP.com

INPUTS :
[01_URL_INVENTORY — pages role_business : vente|affilie|lead|newsletter]
[05_CLUSTERS_MAP — structure clusters et piliers]
[08_EEAT — pages auditées avec signaux confiance]

PARCOURS À CARTOGRAPHIER :
1. Visiteur article SEO → lead newsletter → client formation
2. Visiteur article LMS → page affiliation → clic affilié
3. Visiteur article info → page de vente → formulaire contact

PROBLÈMES COURANTS À DÉTECTER :
- Articles informationnels sans lien vers money page du même cluster [Observable : vérifier les liens]
- Homepage avec logique "blog" uniquement (pas de CTA vers piliers business) [Observable]
- CTA générique "newsletter" sur pages où un CTA spécifique convertirait mieux [Observable]
- Pages affiliées sans social proof visible [Observable]

ACTIONS :
1. Identifier les 5-10 money pages prioritaires à optimiser
2. Vérifier les ponts article info → money page pour chaque cluster P1
3. Évaluer la qualité et la pertinence des CTA actuels
4. Proposer les optimisations SEO qui améliorent aussi le business

FORMAT :
Tableau : url | intention | objectif_business | CTA_actuel | faiblesse | optimisation | priorité
Top 10 optimisations SEO à impact business direct
Top 5 parcours de conversion à créer ou renforcer
Définition des money pages prioritaires
```

---

#### Agent 10 — SEO Roadmap Director

**Fiche :** `tasks/10-roadmap-finale.md`
**Skill :** `authority-domination-roadmap`
**Référence :** `reports/quick-wins.md` (statuts existants) + `roadmap/roadmap-30-60-90.md`
**Entrées :** tous les onglets `02_` à `09_` + `10_Backlog`
**Sortie :** `10_QUICK_WINS` + `00_MASTER_ROADMAP` + Doc Roadmap
**Gate :** backlog consolidé, roadmap rédigée

```
Lis d'abord : tasks/10-roadmap-finale.md
Lis aussi : reports/quick-wins.md (pour le statut des QW existants)
Lis aussi : roadmap/roadmap-30-60-90.md (base existante à enrichir)

RÔLE : Directeur SEO stratégique chargé de transformer l'audit en roadmap d'exécution
SITE : schoolsWP.com

INPUTS :
[Toutes les sorties des agents 01 à 09]
[reports/quick-wins.md — statuts actuels]

ACTIONS :
1. Consolider sans doublons (dédupliquer les actions similaires entre agents)
2. Pour chaque action : Impact SEO (H/M/L) | Impact Business (H/M/L) | Effort (XS/S/M/L)
3. Score priorité : (Impact SEO + Impact Business) / Effort
4. ≤15 actions en P1 — filtrer strictement
5. Horizons : 30j (quick wins P1 effort XS/S) | 60j (P2 effort M) | 90j (stratégique)
6. Quick wins déjà réalisés (depuis reports/quick-wins.md) → exclure, noter comme "done"

TYPES D'ACTIONS OBLIGATOIRES À INCLURE :
- Décision finale sur multilingue (noindex ou engagement total)
- Transformation pages /category/ en piliers éditorialisés
- Passe maillage interne sur 20 articles les plus trafiqués
- Money pages à optimiser agressivement (top 5)
- Titre/meta à réécrire (top 5 CTR faibles GSC)

FORMAT :
Tableau : action | catégorie | impact_SEO | impact_business | effort | priorité | horizon | outil | responsable | etat
Plan 30j | Plan 60j | Plan 90j
Section "Quick wins à lancer cette semaine" (5 actions actionnables immédiatement)
Section "À valider avec outils SEO" (Screaming Frog, Ahrefs, GSC Coverage)
```

---

### Agents support (transversaux)

---

#### Agent S1 — Scorer Impact/Effort/Priorité

**Rôle :** Normaliser et scorer les recommandations de tous les agents
**Quand :** Après chaque agent principal, avant d'écrire dans Sheets
**Sortie :** Lignes `00_MASTER_ROADMAP` mises à jour

```
RÔLE : Scoreur SEO — normalisation impact/effort/priorité

INPUTS :
[Recommandations brutes de l'agent précédent]

ACTIONS :
1. Pour chaque recommandation :
   - Impact SEO : H (gain positions/trafic fort) | M | L
   - Impact Business : H (revenus/leads directs) | M | L
   - Effort : XS (< 1h) | S (< 1j) | M (< 1 semaine) | L (> 1 semaine)
   - Priorité : P1 | P2 | P3
   - Horizon : 30j | 60j | 90j
2. Éliminer les doublons avec le backlog existant
3. Marquer le type de preuve : Observable | Hypothèse | Bonne pratique

FORMAT :
Tableau normalisé prêt pour `00_MASTER_ROADMAP`
```

---

#### Agent S2 — DocWriter Sheets/Docs

**Rôle :** Écrire les sorties dans Google Sheets et Google Docs
**Quand :** Après chaque agent principal scoré
**Skills :** `n8n-workflow-patterns` (pour l'automatisation)

```
RÔLE : Rédacteur documentaire — Google Sheets et Google Docs

INPUTS :
[Tableau normalisé par Agent S1]
[ID Google Sheet cockpit]
[Dossier Google Docs "SEO schoolsWP - Exécution"]

ACTIONS :
1. Écrire dans l'onglet Sheets correspondant (Append Rows ou Update)
2. Créer/mettre à jour le Google Doc synthèse de la tâche
   Structure Doc : Objectif → Constat → Preuves → Diagnostic → Recommandations → Actions → À valider
3. Mettre à jour `00_MASTER_ROADMAP` avec le statut de la tâche
4. Si n8n disponible : générer le payload JSON pour le nœud Google Sheets

FORMAT :
Confirmation d'écriture
Chemin du Doc créé
Payload n8n (si demandé)
```

---

#### Agent S3 — QA Validator

**Rôle :** Vérifier la qualité de chaque sortie avant de passer à la tâche suivante
**Quand :** Avant chaque gate inter-tâches

```
RÔLE : Contrôleur qualité workflow SEO

INPUTS :
[Sortie brute de l'agent principal]
[Gate condition de la tâche]

VÉRIFICATIONS :
1. La gate condition est-elle satisfaite ? (ex : ≥80% URLs classifiées pour T1)
2. Chaque recommandation a un type de preuve explicite (Observable/Hypothèse/Bonne pratique) ?
3. Aucune donnée inventée ?
4. Format de sortie conforme (tableau + résumé + actions suivantes) ?
5. Blocages / données manquantes listés avec instruction de récupération ?

SI ÉCHEC : Lister précisément ce qui manque → renvoyer à l'agent pour complétion
SI SUCCÈS : Valider le passage à la tâche suivante

FORMAT :
Statut : VALIDÉ | INCOMPLET
Si INCOMPLET : liste précise des éléments manquants
Si VALIDÉ : confirmation + next agent à lancer
```

---

## PHASE 3 — Livrables obligatoires

À produire à la fin du workflow :

1. **Diagramme Mermaid** global — `diagrams/workflow-overview.mmd` (mettre à jour)
2. **Tableau impact/effort/priorité** global — `reports/impact-effort-matrix.md`
3. **Roadmap 30/60/90j** — `roadmap/roadmap-30-60-90.md` (enrichir avec données réelles)
4. **Quick wins** — `reports/quick-wins.md` (mettre à jour les statuts + ajouter nouveaux)
5. **Google Sheets 11 onglets** — voir structure dans `templates/sheets-schema.md`
6. **Google Docs 10 synthèses** — voir gabarits dans `templates/docs-template.md`
7. **Exemple n8n JSON** — `n8n/seo-workflow.json` (mettre à jour si changements)

---

## PHASE 4 — Contrôle qualité final

Avant de terminer, vérifier :

- [ ] Chaque agent a une responsabilité claire et non dupliquée
- [ ] Chaque recommandation porte son type de preuve (Observable/Hypothèse/Bonne pratique)
- [ ] Les quick wins sont actionnables sans outil externe supplémentaire
- [ ] La roadmap est cohérente (pas de dépendance cyclique)
- [ ] Les données manquantes sont listées avec instruction de récupération
- [ ] Le workflow peut être compris sans relire tout le contexte global

---

## Google Sheets — Structure cockpit

| Onglet                 | Tâche    | Colonnes clés                                                                                 |
| ---------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `00_MASTER_ROADMAP`    | Pilotage | id, tâche, agent, statut, priorité, impact_SEO, impact_business, effort, horizon, outil, date |
| `01_URL_INVENTORY`     | T1       | url, type_page, cluster, langue, role_SEO, role_business, priorité, observation               |
| `02_INDEXATION_AUDIT`  | T2       | url_or_pattern, risque, cause, action, decision, impact, effort, priorité                     |
| `03_GSC_ANALYSIS`      | T3       | url, requête, impressions, clics, CTR, position, diagnostic, action, priorité                 |
| `04_COMPETITOR_GAP`    | T4       | concurrent, cluster, mot_cle, schoolswp_présent, niveau_gap, opportunité, priorité            |
| `05_CLUSTERS_MAP`      | T5       | cluster, pilier_url, satellites, maturité, cannibal_risk, manques, action                     |
| `06_INTERNAL_LINKING`  | T6       | source, cible, ancre, raison_SEO, raison_business, priorité                                   |
| `07_INTERNATIONAL_SEO` | T7       | url_fr, url_en, url_de, hreflang_ok, parité, risque, action                                   |
| `08_EEAT`              | T8       | url, signal_EEAT, présence, faiblesse, amélioration, impact, priorité                         |
| `09_CONVERSION_SEO`    | T9       | url, intention, CTA_actuel, faiblesse, optimisation, priorité                                 |
| `10_QUICK_WINS`        | T10      | action, catégorie, impact, effort, responsable, deadline, statut                              |

Référence complète des schémas : `templates/sheets-schema.md`

---

## Ordre d'exécution

| Phase                | Agents       | Logique                           |
| -------------------- | ------------ | --------------------------------- |
| Phase 1 — Voir clair | 01 → 02 → 03 | Collecte observables + données    |
| Phase 2 — Comprendre | 04 → 05 → 06 | Concurrence + clusters + maillage |
| Phase 3 — Renforcer  | 07 → 08 → 09 | Technique + autorité + conversion |
| Phase 4 — Décider    | 10           | Roadmap finale                    |
| Support (continu)    | S1 → S2 → S3 | Après chaque agent principal      |

---

## Démarrage rapide

- **"Lance le workflow SEO depuis T1"** → Phase 0 workspace audit → collecter inputs → démarrer Agent 01
- **"Lance Agent 03 avec cet export GSC"** → Agent 03 directement
- **"Reprends depuis T5"** → charger `01_URL_INVENTORY` + `03_GSC_ANALYSIS` + `04_COMPETITOR_GAP` → Agent 05
- **"Valide T2"** → Agent S3 sur la sortie T2
- **"Score et documente T3"** → Agents S1 puis S2 sur la sortie T3
- **"Où en est le workflow ?"** → lire `00_MASTER_ROADMAP`

**En cas d'input manquant :** créer le placeholder, noter `[BLOQUANT : input manquant — instruction : ...]`, passer à la suite.
