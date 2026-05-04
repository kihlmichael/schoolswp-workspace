# INDEX — external-design-systems

73 design systems brand-grade, classés par affinité avec l'univers schoolsWP. Chaque entrée pointe vers `<brand>/DESIGN.md` (palette + typographie + layout + components + responsive).

> Skill d'invocation **manuelle uniquement**. Voir `SKILL.md` pour le protocole et `NOTICE.md` pour l'attribution Apache 2.0.

## Tier S — Forte affinité schoolsWP (12)

À connaître par cœur. Citables dans articles, exploitables comme brief brand.

| Marque | Pertinence | Articles types |
|---|---|---|
| [`stripe/`](stripe/DESIGN.md) | Fintech / paiement | FluentCart, monétisation, comparatifs paiement |
| [`notion/`](notion/DESIGN.md) | Productivité / écriture | Workflows, écosystème CRM/LMS |
| [`linear-app/`](linear-app/DESIGN.md) | Issue tracker éditorial | Projet, dev, productivité moderne |
| [`cursor/`](cursor/DESIGN.md) | IDE / coding | Claude Code, agents, IDE assistants |
| [`supabase/`](supabase/DESIGN.md) | BaaS | Stack n8n, comparatifs WP/headless |
| [`claude/`](claude/DESIGN.md) | Anthropic | Claude Code, agents, MCP, IA |
| [`vercel/`](vercel/DESIGN.md) | Hosting frontend | Hébergement, déploiement, comparatifs |
| [`figma/`](figma/DESIGN.md) | Design collaboratif | Branding, design articles |
| [`cal/`](cal/DESIGN.md) | Booking / scheduling | Coaching, rendez-vous, automatisation |
| [`resend/`](resend/DESIGN.md) | Email transactionnel | FluentSMTP, comparatifs email API |
| [`posthog/`](posthog/DESIGN.md) | Product analytics | SEO, data, comportement utilisateur |
| [`sentry/`](sentry/DESIGN.md) | Monitoring | Observabilité, erreurs, qualité |

## Tier A — Pertinence indirecte (14)

Références ponctuelles dans articles thématiques.

| Marque | Catégorie | Cas d'usage |
|---|---|---|
| [`mintlify/`](mintlify/DESIGN.md) | Docs as code | Articles documentation produit |
| [`framer/`](framer/DESIGN.md) | Site builder animé | Comparatifs no-code/WP |
| [`webflow/`](webflow/DESIGN.md) | No-code | Comparatif vs WordPress |
| [`lovable/`](lovable/DESIGN.md) | AI app builder | Tendances IA / app builders |
| [`intercom/`](intercom/DESIGN.md) | Support / chat | FluentSupport comparatifs |
| [`superhuman/`](superhuman/DESIGN.md) | Email productivity | Articles workflow email |
| [`wise/`](wise/DESIGN.md) | Fintech | Alternatives paiement |
| [`revolut/`](revolut/DESIGN.md) | Fintech | Alternatives paiement |
| [`airtable/`](airtable/DESIGN.md) | DB no-code | Workflows, comparatifs Notion |
| [`miro/`](miro/DESIGN.md) | Whiteboard | Collaboration, frameworks visuels |
| [`sanity/`](sanity/DESIGN.md) | Headless CMS | Comparatifs vs WP |
| [`mongodb/`](mongodb/DESIGN.md) | DB documentaire | Stack technique |
| [`clickhouse/`](clickhouse/DESIGN.md) | DB analytics | Performance, observabilité |
| [`composio/`](composio/DESIGN.md) | Agents / MCP | Connecteurs IA, automation |

## Tier B — IA / LLM / Tech (16)

Articles IA, comparatifs modèles, tooling tech.

| Marque | Domaine |
|---|---|
| [`mistral-ai/`](mistral-ai/DESIGN.md) | LLM européen |
| [`x-ai/`](x-ai/DESIGN.md) | Grok / xAI |
| [`cohere/`](cohere/DESIGN.md) | LLM enterprise |
| [`together-ai/`](together-ai/DESIGN.md) | Inference platform |
| [`replicate/`](replicate/DESIGN.md) | Model hosting |
| [`runwayml/`](runwayml/DESIGN.md) | Gen video / créatif |
| [`elevenlabs/`](elevenlabs/DESIGN.md) | TTS (utilisé en HyperFrames) |
| [`minimax/`](minimax/DESIGN.md) | LLM Chine |
| [`nvidia/`](nvidia/DESIGN.md) | Hardware AI |
| [`ollama/`](ollama/DESIGN.md) | Local LLM |
| [`hashicorp/`](hashicorp/DESIGN.md) | Infra / DevOps |
| [`opencode-ai/`](opencode-ai/DESIGN.md) | Coding agent open-source |
| [`voltagent/`](voltagent/DESIGN.md) | Repo source upstream |
| [`raycast/`](raycast/DESIGN.md) | Productivity launcher |
| [`expo/`](expo/DESIGN.md) | React Native |
| [`warp/`](warp/DESIGN.md) | Terminal moderne |

## Tier C — Consumer / lifestyle / niche (28)

Références iconiques mais affinité directe schoolsWP faible. Pratique pour articles éditoriaux ou inspiration cosmétique.

**Consumer & retail**
- [`airbnb/`](airbnb/DESIGN.md) [`uber/`](uber/DESIGN.md) [`pinterest/`](pinterest/DESIGN.md) [`spotify/`](spotify/DESIGN.md) [`meta/`](meta/DESIGN.md)
- [`shopify/`](shopify/DESIGN.md) [`nike/`](nike/DESIGN.md) [`starbucks/`](starbucks/DESIGN.md) [`mastercard/`](mastercard/DESIGN.md) [`apple/`](apple/DESIGN.md)
- [`xiaohongshu/`](xiaohongshu/DESIGN.md)

**Crypto / fintech extrême**
- [`coinbase/`](coinbase/DESIGN.md) [`kraken/`](kraken/DESIGN.md) [`binance/`](binance/DESIGN.md)

**Automotive & telco**
- [`bmw/`](bmw/DESIGN.md) [`bugatti/`](bugatti/DESIGN.md) [`ferrari/`](ferrari/DESIGN.md) [`lamborghini/`](lamborghini/DESIGN.md)
- [`renault/`](renault/DESIGN.md) [`tesla/`](tesla/DESIGN.md) [`vodafone/`](vodafone/DESIGN.md)

**Media / gaming / aerospace**
- [`playstation/`](playstation/DESIGN.md) [`theverge/`](theverge/DESIGN.md) [`wired/`](wired/DESIGN.md)
- [`spacex/`](spacex/DESIGN.md) [`ibm/`](ibm/DESIGN.md)

**Templates neutres**
- [`default/`](default/DESIGN.md) — système de fallback générique
- [`warm-editorial/`](warm-editorial/DESIGN.md) — style éditorial chaud (newsletter premium)
- [`zapier/`](zapier/DESIGN.md) [`clay/`](clay/DESIGN.md)

## Routing par cas d'usage schoolsWP

| Cas d'usage | DESIGN.md à charger en priorité |
|---|---|
| Article paiement / FluentCart | `stripe`, `wise`, `revolut` |
| Article CRM / FluentCRM | `notion`, `intercom`, `superhuman` |
| Article LMS / formation TutorLMS | `notion`, `linear-app`, `cursor` |
| Article SEO / analytics | `posthog`, `sentry`, `clickhouse` |
| Article automation / n8n / agents | `composio`, `claude`, `cursor`, `vercel` |
| Article IA / comparatif LLM | `claude`, `mistral-ai`, `cohere`, `ollama` |
| Article hébergement / WP comparatif | `vercel`, `sanity`, `webflow`, `framer` |
| Article design / branding | `figma`, `framer`, `miro` |
| Article docs / runbooks | `mintlify`, `linear-app`, `notion` |
| Landing FluentCart pricing | `stripe`, `cal`, `notion` |
| Landing formation premium | `notion`, `linear-app`, `cursor` |
| Newsletter premium / éditorial | `apple`, `theverge`, `wired`, `warm-editorial` |
| Article TTS / vidéo / HyperFrames | `elevenlabs`, `runwayml` |

## Pièges / règles de conflit

- **Ne pas auto-trigger** sur les articles génériques. Toujours invocation manuelle.
- **Brand schoolsWP > brand tiers** : un DESIGN.md tiers est une **inspiration esthétique**, jamais un override de marque. `content/docs/BRAND_RULES.md` reste maître.
- **Pas de skill de création** : c'est une **librairie de référence**. Création = `aidesigner` (T0 exploration) ou `cc-design` (T1 production brand-strict).
- **Citation OK** sous Apache 2.0 avec attribution dans l'article (`Source : nexu-io/open-design, Apache 2.0`).
- **Trademarks** : les noms de marque restent propriété de leurs ayants droit (voir `NOTICE.md`).
