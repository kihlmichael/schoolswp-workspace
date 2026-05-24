---
name: wp-site-audit-30pts
description: |
  Audit WordPress complet noté sur 30 points (5 catégories × 6 points : Sécurité, Performance, SEO, Contenu, Technique) avec données réelles tirées en parallèle de WP Umbrella, DataForSEO Lighthouse, Google Search Console et DataForSEO on-page. Produit un score chiffré par catégorie, un score total, et un top 3 d'actions prioritaires avec impact estimé.
  Déclenche dès que l'utilisateur demande : "audite ce site WordPress", "audit complet de mon site", "score sécurité / performance / SEO de mon WP", "audit 30 points", "diagnostic WordPress", "scan complet du site", "donne-moi un état des lieux du site", "audit santé site WP", "fais l'audit de schoolswp.com" (ou de tout autre URL WordPress). Privilégier ce skill plutôt qu'une checklist générique : l'objectif est de tirer des métriques réelles, pas de réciter des bonnes pratiques.
  NE PAS utiliser pour : audit de code WordPress (utiliser wp-project-triage), audit SEO seul d'un article publié (utiliser le système content/audits/<slug>/<date>/), audit perf seul (utiliser wp-performance), génération d'un rapport client commercial (cet audit est interne, factuel, sans dressing).
last_reviewed: 2026-05-24
review_interval_days: 180
---

# WordPress Site Audit — 30 points

## Objectif

Auditer un site WordPress complet en 5 catégories, noter chaque catégorie sur 6 points (total /30), et restituer un top 3 d'actions priorisées par impact estimé. L'audit doit s'appuyer sur des **données réelles tirées en parallèle**, pas sur des suppositions.

## Entrées requises

- URL du site (ex : `https://schoolswp.com/`).
- Site connecté à WP Umbrella (sinon le bloc Sécurité/Technique sera partiel — le signaler).
- Site vérifié dans GSC du compte connecté (sinon le bloc SEO/CTR sera partiel — le signaler).

## Sortie obligatoire

Un rapport Markdown structuré contenant, dans cet ordre :

1. En-tête avec date d'audit + sources de données utilisées.
2. Une section par catégorie avec **tableau de checks** (check, verdict, détail) + **score X/6** + **justification de la perte**.
3. Bloc **SCORE TOTAL : XX / 30** avec récap des 5 notes.
4. **TOP 3 ACTIONS PRIORITAIRES** : impact estimé chiffré, étapes concrètes, temps + risque par action.

Voir le template complet en bas de ce fichier.

## Procédure

### Étape 1 — Tirer les données en parallèle (un seul tour de tool calls)

Lancer **dans le même message** :

1. `umbrella:umbrella` skill puis `GET /projects?per_page=50` → identifier le project_id, hosting, downtime, plugins en retard.
2. `GET /projects/{id}/vulnerabilities` → CVE plugins/thèmes/core.
3. `GET /projects/{id}/broken-links?per_page=20` → backlog liens cassés (note la pagination totale, c'est révélateur).
4. `mcp__dataforseo__on_page_lighthouse` sur l'URL home → perf desktop, LCP, CLS, FCP, server response, unused JS/CSS.
5. `mcp__dataforseo__on_page_instant_pages` avec `enable_javascript: true` → title/H1/description, internal links count, scripts count, social tags, DOM size, content readability.
6. `mcp__gsc-mcp__list_properties` (si propriété pas confirmée) puis :
   - `mcp__gsc-mcp__get_performance_overview` (28 jours) → clicks, impressions, CTR, position.
   - `mcp__gsc-mcp__get_sitemaps` → état des sitemaps soumis, warnings, indexed_urls.
   - `mcp__gsc-mcp__inspect_url_enhanced` sur la home → indexing state, canonical Google vs user, rich_results.

Toutes ces calls n'ont pas de dépendance entre elles : **les batcher en un seul tour** est non-négociable pour la perf de l'audit.

### Étape 2 — Noter chaque catégorie

#### Sécurité (6 pts)

| Check | Source | Règle de notation |
|---|---|---|
| Plugins/thème/core à jour | WP Umbrella `plugins[].need_update` | -0.5 par plugin en retard (cap -1.5) |
| 0 vulnérabilité CVE | WP Umbrella vulnerabilities endpoint | -1.5 si ≥1 CVE non patchée |
| 2FA + page connexion masquée | Présence de SecuPress / Wordfence / iThemes / Sucuri dans `plugins[]` | -0.5 si aucun plugin sécu actif |
| HTTPS forcé | DataForSEO `is_https: true` + redirect HTTP→HTTPS | -1 si manquant |
| Fichiers sensibles protégés | Présence d'un plugin sécu | À documenter, pas pénalisable sans accès interne |
| XML-RPC désactivé si inutilisé | Présence d'un plugin sécu | À documenter |

#### Performance (6 pts)

| Métrique | Cible verte | Cible orange | Rouge |
|---|---|---|---|
| Lighthouse Desktop | ≥95 | 85-94 | <85 |
| Lighthouse Mobile (WP Umbrella `latest_performance_score_mobile`) | ≥90 | 70-89 | <70 |
| LCP | <2.5 s | 2.5-4 s | >4 s |
| CLS | <0.1 | 0.1-0.25 | >0.25 |
| Server response time | <600 ms | 600-1500 ms | >1500 ms |
| Unused JS + Unused CSS | <30 % chacun | 30-60 % | >60 % |
| Scripts count | <25 | 25-40 | >40 |
| Compression active | Brotli ou gzip | — | aucune = -1 |

Score = 6 - (nombre de seuils orange × 0.25) - (nombre de seuils rouges × 0.75), arrondi à 0.5 près.

#### SEO (6 pts)

| Check | Source | Règle |
|---|---|---|
| Title/H1/Meta uniques + longueurs OK | DataForSEO instant_pages `meta.title_length` (45-65), `description_length` (130-160), `htags.h1` (1 seul) | -0.5 par déviation |
| Maillage interne | `internal_links_count` (cible ≥30 sur home) + présence Link Whisper ou Easy Content Linker dans plugins | -0.5 si <20 |
| Sitemaps soumis et valides | GSC sitemaps endpoint | -0.25 par sitemap avec >50 warnings |
| Indexation home | GSC inspect `verdict: PASS` + `coverage_state: Submitted and indexed` | -1 si pas PASS |
| Canonical correct | GSC inspect `google_canonical == user_canonical` | -1 si divergent |
| Rich results | GSC inspect `rich_results` non null + Schema détecté | -1 si null sur home |
| CTR organique | GSC perf 28j `ctr` vs benchmark 2 % | -1 si <1 %, -0.5 si 1-2 % |

#### Contenu (6 pts)

| Check | Source | Règle |
|---|---|---|
| Fraîcheur | `article:modified_time` < 6 mois sur home | -0.5 si >12 mois |
| E-E-A-T visible | Auteur nommé dans H2/H3, photo, twitter:creator | -0.5 par signal absent |
| Pas de duplication | Canonical OK + audit hreflang si multilangue | -1 si suspicions |
| TL;DR / FAQ | Présence d'un H2 "FAQ" ou "Questions" ou "TL;DR" | -0.5 si absent |
| Qualité rédactionnelle | `description_to_content_consistency` > 0.7, `title_to_content_consistency` > 0.7 | -0.5 par seuil raté |
| Médias optimisés | `images_count` raisonnable + alt présent (og:image:alt) + WebP servi | -0.5 par signal absent |
| **Liens cassés** | WP Umbrella broken-links | Multiplier la première page (20) par la pagination totale pour estimer le backlog. -1 si >100 estimés, -2 si >500 |

#### Technique (6 pts)

| Check | Source | Règle |
|---|---|---|
| Version PHP supportée | WP Umbrella site details (PHP version) | -1 si <8.0, -2 si <7.4 |
| **PHP issues loggées** | WP Umbrella `count_php_issues` | -0.5 si >50, -1 si >150, -1.5 si >500 |
| BDD optimisée | WP Umbrella DB optimization (date dernière passe) | -0.5 si jamais |
| SSL/HTTPS valide | DataForSEO `is_https: true` + cert valide | -2 si invalide |
| Sauvegardes auto | WP Umbrella backup actif | -1 si absent |
| Monitoring uptime | WP Umbrella + date dernière downtime | -0.5 si downtime <30j |
| TTFB / latency | WP Umbrella `latest_ping` (<2000 ms idéal) | -0.5 si 2-5 s, -1 si >5 s |

### Étape 3 — Top 3 actions prioritaires

Sélectionner les 3 actions à plus fort levier en croisant **impact business** × **effort technique** × **risque**.

Pour chaque action, livrer :

- **Titre court orienté résultat** (ex : "Doubler le CTR organique via Schema enrichi").
- **Impact estimé chiffré** quand possible (ex : "passer de 358 à ~3 700 clics/mois si CTR 0,28 % → 3 %").
- **Étapes concrètes** numérotées (3-5 max).
- **Temps + risque** (ex : "1 jour, risque faible").

Privilégier systématiquement :

1. Les actions qui **débloquent des conversions** (liens cassés sur affiliés, produits ecommerce morts, CTA cassés).
2. Les actions à **gros multiplicateur SEO** (CTR sous 1 %, Schema absent, sitemap pollué de warnings).
3. Les actions qui **réduisent le risque opérationnel** (PHP issues nombreuses, plugins en retard avec CVE potentielles, TTFB qui dérive).

Ne **jamais** proposer comme top 3 : "mettre à jour WordPress" si tout est déjà à jour, "activer HTTPS" si déjà actif, "installer un plugin de cache" si FlyingPress/WP Rocket déjà présent. Les actions doivent être **dérivées des pertes de points constatées**, pas génériques.

## Vérification anti-faux positifs

**Avant de conclure qu'un lien est cassé, qu'un cloak est mort, ou qu'une page renvoie une erreur, il faut éliminer 5 catégories de faux positifs.** Beaucoup d'outils de monitoring (WP Umbrella inclus) signalent comme "broken" des URLs qui fonctionnent en réalité pour un humain. Conclure trop vite = corriger ce qui n'est pas cassé et casser ce qui marche.

### Les 5 patterns de faux positifs

1. **Anti-bot openresty / Cloudflare / Imunify360** : le serveur renvoie un challenge JavaScript ("Un instant…", "One moment…", "Just a moment…") avec HTTP 200 ou 415. curl/HEAD ne passe pas le challenge et échoue ou récupère la page d'attente. **Diagnostic** : grep le tag title du body. Si "Un instant" / "Loader" / "Just a moment" apparaît, c'est un faux positif côté checker : le contenu réel n'est pas visible. À tester avec un vrai navigateur.

2. **LinkedIn / X / Twitter / Reddit anti-scraping (HTTP 999, 403, 429)** : ces plateformes bloquent par défaut les user-agents non-navigateurs avec un code custom (LinkedIn = 999). Un cloak /linkedin qui redirige vers linkedin.com/in/xxx apparaît cassé dans WP Umbrella mais fonctionne parfaitement pour un humain. **Diagnostic** : si httpStatus = 999 ET destination = domaine social connu, faux positif quasi-systématique.

3. **HEAD requests bloqués** : certains serveurs (notamment derrière openresty/Cloudflare) répondent HTTP 415 sur HEAD mais 200 sur GET. **Diagnostic** : refaire la requête en GET (curl -sL -X GET) avec User-Agent navigateur complet avant de conclure.

4. **Soft-404** : la page répond HTTP 200 mais affiche un contenu "page non trouvée". **Diagnostic** : grep le tag title ET les mots-clés "404, not found, introuvable, page not found" dans le body. Une vraie 404 doit aussi renvoyer le bon code HTTP côté serveur ; un 200 avec body de 404 est un soft-404 à corriger.

5. **Timeout réseau ou rate-limit ponctuel** (checkError "This operation was aborted" ou "fetch failed") : peut être un vrai problème serveur, mais le plus souvent un coup de chaleur du checker. **Diagnostic** : recheck 24h plus tard avant de prononcer la mort de l'URL.

### Niveaux de confiance par source

Chaque source de données a une fiabilité différente. Pondérer les conclusions en conséquence :

| Source | Niveau de confiance | Détails |
|---|---|---|
| **WP Umbrella** | Élevé pour vulnérabilités CVE, PHP issues, plugins en retard. **Moyen** pour broken links (faux positifs sociaux + anti-bot fréquents). | Toujours croiser broken-links avec test navigateur avant action. |
| **Google Search Console** | Très élevé pour indexation, sitemaps, performance (clicks/impressions/CTR/position). Source de vérité Google. | Pas de faux positif structurel. Délai de fraîcheur 2-3 jours. |
| **DataForSEO Lighthouse / on-page** | Élevé pour métriques performance (LCP, CLS, TBT) et structure on-page (title, H1, canonical, internal links). | Lance sur infrastructure DFS, pas affecté par les anti-bot du site cible. |
| **curl / HEAD direct depuis cette session** | **Faible** pour les sites schoolsWP (challenge openresty + Imunify360 systématique). | Utiliser uniquement pour vérifier que le DNS résout et qu'il y a réponse, pas pour conclure sur le contenu. |
| **curl GET avec UA navigateur complet** | Moyen. Suffit pour 80 % des sites mais bloqué sur ceux derrière openresty/Imunify360/Cloudflare aggressive. | Si "Un instant" apparaît dans le title, escalader vers un vrai navigateur. |
| **Inspection HTML body (regex/grep)** | Variable. Suffit pour soft-404 et détection du challenge openresty. Insuffisant pour vérifier qu'un cloak redirige correctement (le contenu serveur ne montre pas la chaîne de redirect). | Excellent pour disqualifier (page de challenge détectée), insuffisant pour valider (réussite redirect non observable). |
| **Test navigateur humain** | Source de vérité finale pour les redirects, cloaks et liens externes vers plateformes anti-scraping. | À demander à l'utilisateur pour clôturer une décision sur un cloak ou un lien social. |

### Règle d'engagement

- Tant qu'**au moins 2 sources fiables** ne convergent pas sur "lien cassé", marquer le lien comme **À vérifier humainement** et non comme cassé.
- Un seul signal d'une source de confiance Faible (curl, HEAD) **ne suffit jamais** à déclarer un lien mort.
- Documenter explicitement dans le rapport d'audit la source qui a déclenché chaque action.

## Règle anti-boucle pour les cloaks

Un cloak (schoolswp.com/slug/ vers destination tierce) **ne doit jamais cibler une URL appartenant au même domaine que le slug source**, sinon il crée une boucle infinie de redirection (HTTP 30x permanent jusqu'à browser cap, erreur ERR_TOO_MANY_REDIRECTS).

### Cas concrets à refuser

- /o2switch vers https://schoolswp.com/o2switch/ → **BOUCLE** (le handler re-match le slug, redirige à nouveau, ad infinitum).
- /linkedin vers https://schoolswp.com/linkedin → **BOUCLE** (idem).
- /x vers https://x.com/... → **OK** (domaine externe).
- /feed-youtube vers https://www.youtube.com/... → **OK** (domaine externe).

### Vérifications automatiques avant push

Avant de proposer un nouveau cloak, exécuter mentalement (ou via grep) ces 3 checks sur la destination :

1. **Le host de la destination est-il différent du host du site source ?** Si égal, refus immédiat, marquer le slug en TODO.
2. **Le slug existe-t-il déjà comme page WP réelle (post, page, taxonomy term) ?** Si oui, conflit, le mu-plugin va intercepter et casser la page. Vérifier via WP-CLI (wp post list field=post_name) côté serveur ou via une URL de test.
3. **Le slug est-il un préfixe de langue Polylang** (fr, en, de) ? Si oui, le strip Polylang du handler va vider le path, refus.

### Quoi faire quand la destination est inconnue ou crée une boucle

- **Ne pas inventer** une destination de remplacement plausible (ex : page review interne). Le cloak doit pointer vers une vraie destination externe avec ref affilié ou profil social.
- **Marquer le slug en TODO explicite** dans le rapport, avec la mention "URL d'affiliation externe à fournir par l'utilisateur".
- **Laisser le mu-plugin sans le slug** plutôt que d'ajouter une cible bancale. Un slug absent = WP affiche sa 404 par défaut, c'est mieux qu'une boucle infinie qui plante le navigateur.

### Test post-déploiement obligatoire

Pour chaque cloak ajouté, vérifier dans un vrai navigateur :

- URL schoolswp.com/slug (sans slash final) → arrivée sur la destination tierce attendue.
- URL schoolswp.com/slug/ (avec slash final) → idem.
- Variante avec préfixe langue : schoolswp.com/en/slug → doit aussi arriver sur la destination (le handler strip le préfixe).
- Cas conflit : schoolswp.com/slug-suite ou schoolswp.com/slug/page → ne doit **pas** être catché (le handler exige slug = path complet d'un segment).

Si un seul de ces 4 tests échoue, le cloak est défaillant. Ne pas le déclarer en production.

## Template de sortie

```markdown
# Audit WordPress — {URL}

**Date** : {YYYY-MM-DD} | **Source données** : WP Umbrella (ID {x}), GSC, DataForSEO Lighthouse + on-page

## 1. SÉCURITÉ — X / 6

| Check | Verdict | Détail |
|---|---|---|
| ... | OK / PARTIEL / À FIXER | ... |

**Perte** : {justification en 1 ligne}.

## 2. PERFORMANCE — X / 6

| Métrique | Valeur | Verdict |
|---|---|---|
| ... | ... | Excellent / Bon / À améliorer |

**Perte** : {...}.

## 3. SEO — X / 6
{...}
**GSC 28 jours** : {clicks} clics / {impressions} impressions / CTR {x %} / position moy. {x}.

## 4. CONTENU — X / 6
{...}

## 5. TECHNIQUE — X / 6
{...}

---

## SCORE TOTAL : XX / 30

| Catégorie | Note |
|---|---|
| Sécurité | X/6 |
| Performance | X/6 |
| SEO | X/6 |
| Contenu | X/6 |
| Technique | X/6 |
| **Total** | **XX/30** |

---

## TOP 3 ACTIONS PRIORITAIRES

### 1. {Titre orienté résultat}
**Impact estimé** : {chiffré}.

**Action** :
- {étape 1}
- {étape 2}
- {étape 3}
- Temps : {X}. Risque : {faible / moyen / élevé}.

### 2. {...}

### 3. {...}
```

## Règles de style

- Tutoiement (cf. branding schoolsWP).
- **Pas d'em-dash** (U+2014) ni de demi-cadratin (U+2013). Utiliser le deux-points, le tiret simple ou le point.
- Ne pas inventer de métriques. Si une source est indisponible, écrire "À vérifier via {source}" et ne pas pénaliser.
- Pas de promesses absolues ("100 % sécurisé"). Toujours conditionner aux données observées à la date d'audit.
- Garder un ton factuel d'auditeur expérimenté, pas commercial.

## Cas limites

- **Site pas dans WP Umbrella** : passer les blocs Sécurité/Technique en mode partiel, l'écrire en tête de catégorie, et baser la notation uniquement sur ce qui est observable depuis l'extérieur (HTTPS, headers, presence de SecuPress via DataForSEO scripts list).
- **Site pas dans GSC** : passer le bloc SEO en mode partiel, calculer la note sur les seuls signaux on-page (title, H1, canonical, internal links, Schema détecté dans la page).
- **Site multilangue** : auditer la home dans la langue par défaut. Mentionner en bloc Contenu "auditer hreflang sur les 200+ pages" comme TODO si Polylang/WPML détecté.
- **Site staging ou pas en HTTPS** : refuser l'audit pour le bloc SEO/Technique et expliquer pourquoi.

## Exemple condensé (entrée → sortie)

**Entrée** : "audite schoolswp.com sur 30 points"

**Sortie** : voir le rapport d'audit produit le 2026-05-24 dans la conversation qui a initialement créé ce skill (22/30, top 3 = broken affiliate cloaks / CTR via Schema / 173 PHP issues + alléger home).

## Actions suivantes après audit

Une fois le rapport livré, proposer naturellement :

1. **Traiter le top 3** en commençant par l'action 1 (la plus à fort levier). Demander à l'utilisateur laquelle attaquer en premier.
2. **Sauvegarder l'audit** dans `content/audits/<domain>/<YYYY-MM-DD>/audit.md` si le site appartient à un compte tracké (schoolswp.com, michaelkihl.fr).
3. **Planifier la prochaine passe** (typiquement 90 jours pour les sites en cycle d'optimisation continue, 180 jours en cycle stable).
