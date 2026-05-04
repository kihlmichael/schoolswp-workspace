---
name: external-design-systems
description: |
  Bibliothèque de 73 design systems brand-grade (Stripe, Notion, Linear, Cursor, Supabase, Anthropic, Apple, Vercel, Figma, Resend, Cal.com, Mistral, etc.) au format DESIGN.md. Chaque DESIGN.md fait 18-25 KB et couvre palette/typographie/layout/components/responsive avec une densité de doc designer.

  Skill d'invocation MANUELLE — ne pas auto-déclencher. Trois usages :

  1. Référence dans articles schoolsWP qui comparent ou citent un produit ("comment Stripe utilise sohne-var weight 300", "shadow system Linear vs Notion")
  2. Brief brand pour aidesigner / cc-design ("génère une landing dans le style Notion" → injecter notion/DESIGN.md en contexte)
  3. Modèle pour formaliser un futur DESIGN.md schoolsWP propre (la palette tokens + hiérarchie typo + shadow system n'existe pas encore en specs visuelles complètes dans BRAND_RULES.md)

  Triggers manuels : "design system X", "style Stripe/Notion/Linear", "DESIGN.md", "palette de référence". Ne pas confondre avec aidesigner (génération design) ni cc-design (production HTML brand-strict).
allowed-tools: Read, Grep, Glob
---

# External Design Systems Library

73 fichiers `DESIGN.md` issus de [`nexu-io/open-design`](https://github.com/nexu-io/open-design) (Apache 2.0), eux-mêmes forkés depuis [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) **avant** que celui-ci ne soit vidé de son contenu (chaque README pointe maintenant vers `getdesign.md`, produit fermé). C'est aujourd'hui le seul accès libre et complet à cette collection.

## Top 12 pour l'univers schoolsWP

| Marque | Pertinence pour schoolsWP |
|---|---|
| `stripe/` | Articles paiement (FluentCart, monétisation), références fintech |
| `notion/` | Articles productivité, workflows, comparaison écriture/structure |
| `linear-app/` | Style éditorial moderne, articles dev/produit |
| `cursor/` | Articles IDE / coding assistants, écosystème Claude Code |
| `supabase/` | Articles BaaS, stack n8n, comparatifs WP/headless |
| `anthropic` (`claude/`) | Articles Claude Code / agents / MCP |
| `vercel/` | Articles hébergement (même si schoolsWP est sur EasyHoster) |
| `figma/` | Articles design / collaboration |
| `cal/` (Cal.com) | Articles booking / coaching / rendez-vous |
| `resend/` | Articles email transactionnel / FluentSMTP comparatifs |
| `posthog/`, `sentry/` | Articles observabilité / analytics |
| `mistral-ai/`, `x-ai/`, `cohere/` | Articles IA / LLM comparatifs |

Voir `INDEX.md` pour le mapping complet et le routing par cas d'usage.

## Workflow d'invocation

### Cas 1 — citer dans un article

```
Lis .claude/skills/external-design-systems/stripe/DESIGN.md
puis cite la section "Typography Rules" dans l'article comparatif paiement.
```

Citation OK sous Apache 2.0 avec attribution (`Source : nexu-io/open-design, Apache 2.0`).

### Cas 2 — brief brand pour aidesigner / cc-design

```
Génère via cc-design une landing FluentCart dans l'esprit Notion :
charge .claude/skills/external-design-systems/notion/DESIGN.md
en contexte avant de produire l'HTML. Adapte palette + typo + shadow system,
ne réécris pas le contenu schoolsWP existant (BRAND_RULES.md prime).
```

Attention conflit brand : le brand schoolsWP doit toujours rester maître. Le DESIGN.md tiers est une **inspiration esthétique**, pas un override de marque.

### Cas 3 — modèle pour un DESIGN.md schoolsWP

`stripe/DESIGN.md` (700+ lignes, 17 niveaux de hiérarchie typo, palette en 8 catégories, shadow system blue-tinted) est un excellent template. Si tu décides de formaliser le brand schoolsWP en DESIGN.md complet, démarre depuis `stripe/`, `notion/` ou `linear-app/` et adapte.

## Règles de routing

- **NE PAS** se déclencher automatiquement sur les articles génériques. Invocation manuelle seulement.
- **NE PAS** servir de skill de création — c'est une **librairie de référence**. La création passe par `aidesigner` (T0 exploration) ou `cc-design` (T1 production brand-strict).
- **NE PAS** importer les tokens (palette, typo) directement dans le brand schoolsWP sans validation Michael — risque de drift de marque.

## Attribution

Voir `NOTICE.md` et `LICENSE` (Apache 2.0).
