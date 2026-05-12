# Mission en cours — schoolsWP OS

**Date** : 2026-05-11
**Priorité #1** : Pilier FluentCRM automations (débloque le lead magnet welcome en 404)

---

## Tâche active

### Article pilier : FluentCRM, les 4 automations indispensables

**Slug cible** : `/fluentcrm-automations-indispensables/` (à publier sur schoolswp.com)

**Pilier** : CRM
**Intent** : informationnelle / décisionnelle (terrain freelance WP, pas tutoriel YouTuber)
**Objectif business** : apurer la dette SEO + débloquer la séquence welcome

**Pourquoi maintenant** : 4 assets schoolsWP linkent déjà ce slug et pointent en 404 :

- Email 3 séquence welcome FluentCRM (template id 2866642)
- Landing page `/template-welcome-fluentcrm/` (page id 2867562)
- Page de remerciement `/merci-template-welcome-fluentcrm/` (page id 2866761)
- PDF lead magnet v3 (CTA email 3)

**Brief minimum à couvrir** :

- 4 automations jugées indispensables après 3 ans d'usage client :
  1. Welcome
  2. Abandon panier / re-engagement
  3. Post-achat / anniversaire d'inscription
  4. Segmentation avancée
- Angle terrain freelance WordPress
- Screenshots config FluentCRM réels
- Blocs Benchmark + Goals
- Tags / listes utilisés
- Exemples de délais et conditions concrets
- Lien partenaire : `schoolswp.com/fluentcrm` (sans `/go/`)

**Prochaines étapes** :

- [ ] Brief SEO + outline via `thruuu-writer` ou `schoolswp-article-workflow`
- [ ] V1 article (cible ~2 500 mots, ton terrain solo "je")
- [ ] Captures écran FluentCRM réelles (compte Pro schoolswp.com)
- [ ] Audit 4 axes (SEO + IA + Conversion + Autorité)
- [ ] V3 finale + Publish Score ≥ 85
- [ ] Publication via Novamira MCP (gros contenu : pattern b64 chunks)
- [ ] Mise à jour Email 3 séquence welcome (template 2866642) avec lien live
- [ ] Mise à jour landing + thank-you + PDF v3
- [ ] Update mémoire `project_fluentcrm_automations_pillar.md` (transformer en référence au pillar publié)

---

## Chantiers ouverts (à reprendre après pilier FluentCRM)

### Formation FluentBoards : Task 0.5 puis 0.6

- Bundle FluentCart 2673000 Draft, prix 67 € early bird à activer (compare-at 97 €)
- Inner product `acces-cours-fluentboards` et order bump `pack-workflows-n8n-avances-fluentboards` à créer côté Michael
- IDs à récupérer puis mappage bundle confirmé
- Task 0.6 : automation FluentCRM enroll TutorLMS course 2670141 (action native ou fallback HTTP REST)
- Spec : `docs/superpowers/specs/2026-04-21-formation-fluentboards-design.md`

### Article FluentCRM money page (hérité)

- `content/articles/crm-fluentcrm/final.md` : corriger mix accents / sans accents
- Publication sur schoolswp.com (slug à confirmer : `/fluentcrm/` ou `/fluentcrm-avis/`)
- Créer lien affilié FluentCRM réel via cloak `schoolswp.com/fluentcrm`
- Lead magnet "Listes & Tags FluentCRM"
- Satellite 1 du cluster : FluentSMTP + Amazon SES

### Pipeline recyclage article vers vidéo HF

- Workflow n8n 8k07aXZWaMJK2pNg (LinkedIn Carousel Intros)
- Kling 3.0 pro i2v, 90 credits par intro
- 1 master 16:9 + `build_variants.py` pour 3 formats
- Narration ElevenLabs Charlie

### michaelkihl.fr + Skoatch

- Tool `tools/skoatch/` installé 2026-05-11, 2594 credits dispo
- site_id=503 michaelkihl.fr OK, schoolswp.com INTERDIT (BRAND_RULES incompatibles)
- Pipeline éditorial à définir pour michaelkihl.fr

---

## Backlog

- [ ] Retrofit images anciens articles (pré-2026-04-20) avec métadata SEO + hygiène URL
- [ ] Audit pilier LMS (`pillar_authority --all`)
- [ ] Cluster CRM complet (8 satellites planifiés dans `crm-fluentcrm/cluster.md`)
- [ ] Plan ROI éditorial Q2 2026
- [ ] YouTube intro Remotion 85s (`plans/youtube-intro-remotion.md`)
- [ ] Article pilier "5 meilleurs plugins de cache" (avant de lier H2 Alternatives des avis cache)
- [ ] Knowledge graph mise à jour

---

## Complété récemment (sprint avril-mai 2026)

- [x] W209 ingestion YouTube competitor vers brief schoolsWP + W209a auto-publish + Discord notify fix
- [x] W206 W207 W208 W208a veille concurrentielle 3 axes (plugins + éditoriaux + locale Grand Est)
- [x] Install HeyGen MCP + register higgsfield dans le template
- [x] Fluent ecosystem MCP servers via launcher pattern
- [x] AI summary buttons mu-plugin v2.1 (5 pills LLM sur 357 articles FR/EN/DE)
- [x] Hyperframes : recycle FluentCart Gratuit vs Pro + FP vs WP Rocket + brand intro
- [x] WP Umbrella plugin v0.1.3 connecté + skills sites/health
- [x] Push `.user.ini` schoolswp.com (timeouts Easy Content Linker)
- [x] Tool Skoatch + skill dev/skoatch-api
- [x] Tool wp-media-upload pipeline + Discord avatar generator + Gutenberg v4 builder
- [x] Reddit sub-agent FR/EN
- [x] Import design-systems lib (73 DESIGN.md) + 3 skills open-design (frontmatter `od:`)
- [x] Import defuddle depuis kepano/obsidian-skills
- [x] Hook anti-leak secrets `${VAR}` dans `.mcp.json` args/headers
- [x] Interdiction em-dash + en-dash étendue aux règles projet
