# schoolsWP Project Sub-Agents — Index complet

<!-- AUTO:HEADER:START -->
**Total** : 38 sub-agents | **Mis à jour** : 2026-06-28
<!-- AUTO:HEADER:END -->

**Structure** : un fichier `.md` par agent dans `.claude/agents/`, frontmatter YAML (`name`, `description`, `model`, `tools`)

> Sub-agents Claude Code dispatchables via le tool Agent (parallélisables, contexte isolé). Différents de :
> - la fleet `schoolswp-agents/` (4 instances autonomes en process séparé, leurs propres `CLAUDE.md` + `soul.md` + mémoire)
> - les agents Python (`core/agents-py/`, 28 scripts CLI héritant de `BaseContentAgent`)
>
> Pour les règles de conflit qui doivent rester chargées en contexte, voir [CLAUDE.md](../../CLAUDE.md) (section Project Sub-Agents).

---

## Routing Priority — quel agent pour quelle demande

Tables d'arbitrage anti-collision. Les règles fines de conflit sont en bas (section « Règles de conflit »).

### Stratégie / pilotage marketing

| Input utilisateur | Agent à dispatcher |
|---|---|
| Diagnostic marketing global, choix des canaux prioritaires, arbitrage « quel agent lancer », revue COMEX, décision GO/FIX/WAIT/STOP sur un chantier marketing | `directeur-marketing-ia` |

> **Posture** : manager stratégique, pas exécutant. Repo-first par défaut, données live uniquement sur validation humaine, aucune autopublication, aucun déclenchement d'agent en autonomie. Livrable = Note de COMEX marketing (diagnostic + décisions + file de dispatch) dans `output/`.

### Production éditoriale schoolsWP

| Input utilisateur | Agent à dispatcher |
|---|---|
| Rédaction article, newsletter, brief éditorial, tutoriel, guide | `studio` |
| Cocon sémantique, brief SEO, keyword analysis, maillage interne | `radar` |
| Post LinkedIn, Bluesky, Pinterest text, YouTube description/titre, recyclage social | `pulse` |
| FluentCRM, OttoKit, n8n, Fluent Forms, sales funnels, webhooks | `flow` |
| Adaptation EN → FR d'un framework ou doc stratégique | `framework-adapter-fr` |
| Post Reddit FR/EN, commentaire thread, shortlist subs | `reddit` |
| Brief thruuu `.docx` → article schoolsWP publiable (pipeline complet orchestré, statut `REVIEW_REQUIRED`) | `thruuu-article-orchestrator` |

### YouTube OS (pipeline vidéo schoolsWP)

| Input utilisateur | Agent à dispatcher |
|---|---|
| « Je veux faire une vidéo sur X » (orchestration complète) | `youtube-os-orchestrator` |
| Idées vidéo priorisées (P1/P2/P3) à partir d'un sujet/plugin/opportunité | `youtube-strategy-scout` |
| Script complet 9 sections (hook → CTA) + notes tournage + B-roll | `youtube-script-writer` |
| Titres x5, description, chapitres, tags, hashtags, commentaire épinglé | `youtube-seo-packager` |
| Brief miniature (3 variantes A/B/C) + composition + prompt image | `youtube-thumbnail-director` |
| Vidéo longue → Shorts + sous-titres FR/EN/DE + posts LinkedIn | `youtube-clipper` |
| Checklist publication, blocage tant que statut ≠ `APPROVED` | `youtube-publisher-scheduler` |
| Données YouTube → une action prioritaire + test suivant | `youtube-analytics-learner` |
| Audit livrable avant validation (clarté, ton, crédibilité, risques) | `youtube-quality-auditor` |

> **Règle fondatrice YouTube OS** : statut par défaut `REVIEW_REQUIRED`, aucune publication publique sans validation humaine explicite. Livrables dans `content/youtube/`, traces de pipeline dans `runs/youtube-os/`.

### Réseaux sociaux organiques (experts plateforme)

| Input utilisateur | Agent à dispatcher |
|---|---|
| Tweets, threads X, bio/profil X, stratégie reply/quote | `x-expert` |
| Posts Threads, fils conversationnels, articulation cross-post Instagram | `threads-expert` |
| Reels, carrousels, Stories, captions, hashtags/SEO IG, bio/highlights, link-in-bio | `instagram-expert` |
| Posts de Page Facebook, stratégie de Groupes, événements, portée organique | `facebook-expert` |
| Scripts/hooks TikTok, formats natifs, sons, séries, captions + texte à l'écran | `tiktok-expert` |
| Veille et scoring des trends TikTok (sons, hashtags, formats, challenges) | `tiktok-trends-watch` |

> **Posture commune** : organique uniquement (les Ads = futurs agents dédiés), repo-first, zéro MCP, ne publient jamais, ne programment jamais, ne récupèrent aucune donnée live sans validation. Décisions GO/FIX/WAIT/STOP. Livrables dans `output/`. `instagram-expert` délègue le rendu image à `tools/html-to-png` + la config metricool-carousel ; `tiktok-expert` délègue la production vidéo (`youtube-clipper` + stack HeyGen/montage/ElevenLabs) et la veille des trends à `tiktok-trends-watch`.

### SEO / techniques

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit technique SEO, schema, Core Web Vitals, sitemap/robots, meta tags | `seo-specialist` |

### Pinterest

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit compte Pinterest, Ads, scaling horizontal, creatives IA, SEO Pinterest, retargeting | `pinterest-expert` |

### Design / UI

| Input utilisateur | Agent à dispatcher |
|---|---|
| Frontend, landing page, dashboard, marketing page via MCP aidesigner | `aidesigner-frontend` |

### SEO local / Google Business Profile

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit fiche GBP, catégories, description, services, posts, photos, Q&A, stratégie et réponses aux avis, cohérence NAP, citations locales, optimisation local pack, UTM | `google-business-expert` |

> **Posture** : expert GBP + SEO local, opérationnel mais prudent. Repo-first, zéro MCP, ne publie jamais, ne répond jamais directement à un avis, ne modifie jamais une fiche, ne récupère aucune donnée live sans validation. Livrable = Note Google Business (9 sections, décision GO/FIX/WAIT/STOP) dans `output/`.

### Acquisition payante / Paid Media

| Input utilisateur | Agent à dispatcher |
|---|---|
| Audit Google Ads Search, plans d'acquisition SEA, landing ads, mots-clés, tracking, QS, décisions | `ads-operator` |
| Meta Ads (Facebook + Instagram) : structure, audiences, créas, pixel/CAPI, budget, ROAS, décisions | `meta-ads-operator` |
| TikTok Ads : Spark Ads, audiences, créas natives, pixel/Events API, budget, rotation créa, décisions | `tiktok-ads-operator` |

> **Posture commune** : opérateurs d'acquisition payante (pattern `ads-operator`), repo-first, ne publient ni ne modifient aucune campagne, aucun accès live autonome. Format de réponse Situation/Diagnostic/Priorités/Action plan/Devil's advocate/Decision/Next test. Vocabulaire de décision : GO / FIX THEN GO / PAUSE / STOP / WAIT_MORE_DATA. Michael exécute manuellement.

### Publication externe (hors schoolsWP)

| Input utilisateur | Agent à dispatcher |
|---|---|
| Article via Skoatch API + push draft WordPress sur michaelkihl.fr (ou autre site WP non-schoolsWP) | `skoatch-publisher` |

### Code review / qualité (read-only)

| Input utilisateur | Agent à dispatcher |
|---|---|
| Review de code après implémentation, avant merge d'une PR, audit d'un diff (5 axes) | `code-reviewer` |
| Détection décision architecturale → ADR pattern Nygard | `adr-writer` |
| Review adversariale d'un plan d'implémentation (5 dimensions) | `plan-challenger` |
| LLM-as-Judge qualité avant commit/action | `output-evaluator` |
| Détection silent failures, swallowed errors, fallbacks dangereux | `silent-failure-hunter` |

### Harness / infra

| Input utilisateur | Agent à dispatcher |
|---|---|
| Tuning harness Claude Code (reliability, cost, throughput) | `harness-optimizer` |

### Hors schoolsWP (projets personnels)

| Input utilisateur | Agent à dispatcher |
|---|---|
| AI influencer / OFM (identity design, photo prompt batches Alexya) | `ofm-bot` |

---

## Tables détaillées par groupe

<!-- AUTO:TABLES:START -->

### Stratégie / COMEX (orchestration)

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `directeur-marketing-ia` | opus | Read, Write, Edit, Glob, Grep | Use this agent as the marketing director / COMEX of schoolsWP : strategic pilot, not a content executor. |

### Contenu éditorial schoolsWP

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `flow` | sonnet | Read, Write, Edit, Bash, Glob, Grep | Use this agent for CRM, email marketing, and automation tasks on schoolsWP. |
| `framework-adapter-fr` | sonnet | Glob, Grep, ListMcpResourcesTool, Read, ReadMcpResourceTool, WebFetch, WebSearch, Edit, NotebookEdit, Write, Bash | Use this agent when the user needs to adapt, translate, or rewrite an English-language framework, methodology, or strategic document into natural, high-quality French. |
| `pulse` | haiku | Read, Write, Edit, Glob, Grep | Use this agent for social media content and community tasks for schoolsWP. |
| `radar` | sonnet | Read, Write, Edit, Glob, Grep | Use this agent for SEO and GEO tasks related to schoolsWP. |
| `reddit` | sonnet | Read, Write, Edit, Glob, Grep | Use this agent for Reddit content and strategy tasks for schoolsWP. |
| `studio` | opus | Read, Write, Edit, Bash, Glob, Grep | Use this agent when the user asks to write, draft, or create content for schoolsWP. |
| `thruuu-article-orchestrator` | opus | Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch | Use this agent to orchestrate the full pipeline that turns a thruuu content brief (.docx) into a publish-ready schoolsWP article, in an isolated context. |

### YouTube OS

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `youtube-analytics-learner` | opus | (par défaut) | Analyse les performances YouTube schoolsWP et transforme les données en décisions éditoriales concrètes. |
| `youtube-clipper` | opus | (par défaut) | Découpe les vidéos longues schoolsWP en extraits courts, Shorts, sous-titres FR/EN/DE, posts LinkedIn et checklists de publication. |
| `youtube-os-orchestrator` | opus | (par défaut) | Pilote le YouTube OS schoolsWP. À utiliser pour transformer une idée, un article, une vidéo longue ou une opportunité en pipeline YouTube complet. |
| `youtube-publisher-scheduler` | opus | (par défaut) | Prépare la publication YouTube schoolsWP, vérifie les éléments de mise en ligne et bloque toute publication sans validation humaine. |
| `youtube-quality-auditor` | opus | (par défaut) | Audite les livrables YouTube schoolsWP avant validation humaine : clarté, crédibilité, ton, risques, affiliation et publication. |
| `youtube-script-writer` | opus | (par défaut) | Rédige des scripts YouTube schoolsWP clairs, pédagogiques et actionnables à partir d'une idée, d'un brief, d'un article ou d'un plugin. |
| `youtube-seo-packager` | opus | (par défaut) | Prépare le package SEO YouTube schoolsWP : titres, description, chapitres, tags, hashtags et commentaire épinglé. |
| `youtube-strategy-scout` | opus | (par défaut) | Trouve et priorise des idées de vidéos YouTube schoolsWP à partir d'un sujet, d'un article, d'un plugin, d'une question ou d'une opportunité SEO. |
| `youtube-thumbnail-director` | opus | (par défaut) | Crée des briefs de miniatures YouTube schoolsWP lisibles, sobres, premium utiles et cohérents avec l'identité visuelle. |

### Spécialistes domaine

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `aidesigner-frontend` | (défaut) | (par défaut) | Use this skill when the user wants to create or redesign a frontend, landing page, dashboard, marketing page, or other UI with AIDesigner. |
| `google-business-expert` | opus | Read, Write, Edit, Glob, Grep | Use this agent for Google Business Profile (GBP) + local SEO for schoolsWP / michaelkihl.fr. |
| `pinterest-expert` | opus | (par défaut) | Agent Pinterest expert base sur les enseignements de Luc Bermond (1606 unites, 215 videos). |
| `seo-specialist` | sonnet | Read, Grep, Glob, Bash, WebSearch, WebFetch | SEO specialist for technical SEO audits, on-page optimization, structured data, Core Web Vitals, and content/keyword mapping. |
| `skoatch-publisher` | sonnet | Read, Write, Edit, Bash, Glob, Grep | Use this agent when the user wants to generate articles via Skoatch API and push them as WordPress drafts on michaelkihl.fr or another connected non-schoolsWP site. |

### Réseaux sociaux (experts plateforme, organique)

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `facebook-expert` | opus | Read, Write, Edit, Glob, Grep | Use this agent for organic Facebook content and strategy for schoolsWP. |
| `instagram-expert` | opus | Read, Write, Edit, Glob, Grep | Use this agent for organic Instagram content and strategy for schoolsWP. |
| `threads-expert` | opus | Read, Write, Edit, Glob, Grep | Use this agent for organic Threads (Meta) content and strategy for schoolsWP. |
| `tiktok-expert` | opus | Read, Write, Edit, Glob, Grep | Use this agent for organic TikTok content and strategy for schoolsWP. |
| `tiktok-trends-watch` | opus | Read, Write, Edit, Glob, Grep | Use this agent for TikTok trends watch and analysis for schoolsWP. |
| `x-expert` | opus | Read, Write, Edit, Glob, Grep | Use this agent for organic X (Twitter) content and strategy for schoolsWP. |

### Acquisition payante / Paid Media

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `ads-operator` | opus | Read, Grep, Glob, Bash | Opérateur SEA schoolsWP / michaelkihl.fr. À utiliser pour audits Google Ads Search, plans d'acquisition, landing ads, budget, mots-clés, négatifs, tracking, Quality Score, conversions hors-ligne, et d… |
| `meta-ads-operator` | opus | Read, Grep, Glob, Bash | Opérateur Meta Ads (Facebook + Instagram) schoolsWP / michaelkihl.fr. |
| `tiktok-ads-operator` | opus | Read, Grep, Glob, Bash | Opérateur TikTok Ads schoolsWP / michaelkihl.fr. À utiliser pour audits de comptes TikTok Ads, plans d'acquisition payante, Spark Ads (boost de contenu organique), structure de campagnes, audiences, c… |

### Code review / qualité — read-only

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `adr-writer` | opus | Read, Grep, Glob | Architecture Decision Record generator agent — read-only. Detects architectural decisions in code changes, classifies criticality, and generates ADRs in the pattern-oriented ADR format by Michael Nyga… |
| `code-reviewer` | sonnet | Read, Grep, Glob, Bash | Senior code reviewer, read-only. Evaluates a diff across 5 axes (correctness, readability, architecture, security, performance) and returns categorized findings with an APPROVE or REQUEST CHANGES verd… |
| `output-evaluator` | haiku | Read, Grep, Glob | Evaluate Claude Code outputs for quality before commit/action (LLM-as-a-Judge pattern) |
| `plan-challenger` | opus | Read, Grep, Glob | Adversarial plan review agent — read-only. Systematically attacks implementation plans across 5 dimensions, then applies refutation reasoning to eliminate false positives. Never modifies code. |
| `silent-failure-hunter` | sonnet | Read, Grep, Glob, Bash | Review code for silent failures, swallowed errors, bad fallbacks, and missing error propagation. |

### Harness / infra

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `harness-optimizer` | sonnet | Read, Grep, Glob, Bash, Edit | Analyze and improve the local agent harness configuration for reliability, cost, and throughput. |

### Hors schoolsWP (projets personnels)

| Agent | Modèle | Outils | Description |
| --- | --- | --- | --- |
| `ofm-bot` | opus | Read, Write, Edit, Glob, Grep | Use this agent for AI influencer / OFM content production tasks (identity design, photo prompt batches for Alexya engine). |

<!-- AUTO:TABLES:END -->

---

## Règles de conflit (anti-collision)

> Ces règles **doivent rester chargées en contexte** (donc dupliquées dans `CLAUDE.md`) car elles évitent les mauvais dispatches en cours de session.

- **`studio` vs YouTube OS** : `studio` rédige du contenu éditorial schoolsWP (article, newsletter, brief, script générique). Pour une vidéo YouTube complète avec pipeline (script → SEO → thumbnail → publication), passer par `youtube-os-orchestrator`. Pour un script vidéo isolé : `studio` reste OK.
- **`pulse` vs YouTube OS** : `pulse` produit la description / titre d'une vidéo YouTube ponctuelle. `youtube-seo-packager` produit le package SEO complet (5 titres, description, chapitres, tags, hashtags, commentaire épinglé) dans le cadre d'un pipeline.
- **`pulse` vs `pinterest-expert`** : `pulse` rédige le texte pin (titre + description). `pinterest-expert` audite / scale / pilote Ads / SEO Pinterest organique.
- **`flow` vs `pulse`** : `flow` = mécanique CRM/automation/n8n. `pulse` = copy social. La pipeline Pinterest technique (n8n + Placid + Tailwind) reste `flow`.
- **`pulse` vs experts réseaux (`x-expert` / `threads-expert` / `instagram-expert` / `facebook-expert`)** : `pulse` garde LinkedIn, Bluesky, texte Pinterest, descriptions YouTube et la coordination communautaire transverse (calendrier, Discord, Substack). X, Threads, Instagram et Facebook appartiennent désormais à leur expert dédié (stratégie + format + algo + contenu de la plateforme). Tous organiques : les Ads relèveront d'agents Ads séparés (Meta Ads, TikTok Ads). `instagram-expert` ne génère pas les visuels (délégués à `tools/html-to-png` + metricool-carousel).
- **`tiktok-expert` vs `youtube-clipper` vs `tiktok-trends-watch`** : `youtube-clipper` découpe une vidéo longue YouTube en Shorts/clips + sous-titres (production). `tiktok-expert` fait la stratégie + le contenu natif TikTok (et peut consommer ces clips) mais ne produit pas la vidéo lui-même. La veille et le scoring des trends TikTok appartiennent à `tiktok-trends-watch`, qui n'écrit aucun contenu et passe le relais à `tiktok-expert`. `tiktok-trends-watch` n'est pas le schoolsWP Plugin Radar (trends TikTok ≠ sorties de plugins).
- **Paid vs organique (`meta-ads-operator` / `tiktok-ads-operator` vs `facebook-expert` / `instagram-expert` / `tiktok-expert`)** : les agents Ads gèrent l'acquisition payante (budget, audiences, pixel, créas sponsorisées, décisions GO/FIX THEN GO/PAUSE/STOP/WAIT_MORE_DATA) ; les experts réseaux gèrent l'organique (contenu natif gratuit). `meta-ads-operator` = Facebook + Instagram Ads ; `tiktok-ads-operator` = TikTok Ads (les Spark Ads boostent un contenu organique validé par `tiktok-expert`). Aucun ne publie ni ne modifie de campagne : décision seulement, exécution manuelle par Michael.
- **`radar` vs `seo-specialist`** : `radar` = SEO éditorial schoolsWP (cocons, briefs, maillage). `seo-specialist` = SEO technique générique (schema, Core Web Vitals, sitemap, audit serveur).
- **`google-business-expert` vs `seo-specialist` / `radar` / `ads-operator`** : `google-business-expert` = SEO local + fiche Google Business Profile (catégories, avis, NAP, citations, local pack, posts GBP). `seo-specialist` reste le SEO technique on-site, `radar` le SEO éditorial, `ads-operator` l'acquisition payante Google Ads. Le local et la fiche GBP n'appartiennent qu'à `google-business-expert`. Il ne publie jamais et ne modifie jamais la fiche.
- **`skoatch-publisher` isolation** : **interdit sur schoolswp.com** (BRAND_RULES incompatibles). michaelkihl.fr uniquement, ou autre site WP non-schoolsWP sur demande explicite.
- **`ofm-bot` isolation** : aucun chevauchement avec schoolsWP (utiliser `studio` / `radar` / `pulse` / `flow`). Pas de génération d'image standalone (utiliser nano-banana directement).
- **Quartet `studio` / `radar` / `pulse` / `flow`** : mirror la fleet `schoolswp-agents/` (instances autonomes) mais en sub-agents projet dispatchables en parallèle dans la session courante.
- **`thruuu-article-orchestrator` vs `studio`** : l'orchestrateur traite uniquement un pipeline complet à partir d'un brief thruuu `.docx` (gap analysis → rédaction → humanisation → linking → QA editor-in-chief). `studio` reste le défaut pour tout contenu éditorial générique (newsletter, script, brief, article sans brief `.docx`). L'orchestrateur s'appuie sur le skill `thruuu-writer`, il ne le duplique pas. Il ne publie jamais : statut de sortie `REVIEW_REQUIRED`.

---

## Maintenance

Les zones marquées `<!-- AUTO:HEADER -->` (compteur + date) et `<!-- AUTO:TABLES -->` (tables détaillées par groupe) sont régénérées par le script [tools/scripts/agents-registry.py](../../tools/scripts/agents-registry.py) :

    .venv/Scripts/python tools/scripts/agents-registry.py            # rapport (lecture seule)
    .venv/Scripts/python tools/scripts/agents-registry.py --sync     # régénère INDEX.md
    .venv/Scripts/python tools/scripts/agents-registry.py --check    # exit 1 si désynchronisé (CI / pre-commit)

**Pour ajouter un agent** :

1. Créer `.claude/agents/<nom>.md` avec frontmatter (`name`, `description`, `model`, `tools`).
2. Ajouter `"<nom>": "<groupe>"` dans le dict `GROUPS` de `tools/scripts/agents-registry.py`.
3. Ajouter une entrée routing manuelle (section « Routing Priority » de cet INDEX) — pas auto-générée car c'est de la sémantique humaine.
4. Lancer `--sync` pour régénérer les tables détaillées et le compteur.

**Pour supprimer un agent** : retirer le fichier `.md`, l'entrée du dict `GROUPS`, le routing, puis `--sync`.

**Pour renommer** : `name:` dans le frontmatter fait foi pour le dispatch, pas le nom de fichier (exemple : `pinterest.md` expose `pinterest-expert`). Mettre à jour `GROUPS` et le routing en conséquence.

**Agent non classé** : si un `.md` existe mais n'est pas dans `GROUPS`, le script le range dans le groupe « Non classé » et alerte. À mapper explicitement.
