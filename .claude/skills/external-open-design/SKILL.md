---
name: external-open-design
description: |
  Bibliothèque de 3 skills HTML générateurs cherry-picked depuis nexu-io/open-design (Apache 2.0) le 2026-04-30 :

  - `open-design-email-marketing` (sous-skill) — HTML email visuel premium centré 600-680px pour newsletter featured schoolsWP (~1-2/mois max). Annonces lancement formation, partenariat plugin majeur.
  - `open-design-pricing-page` (sous-skill) — page pricing single-screen 2/3/4 tiers + comparison table + FAQ. Pour offres propres formation TutorLMS premium, bundle FluentCart.
  - `open-design-docs-page` (sous-skill) — doc 3 colonnes (left nav + body + right TOC) pour mockup doc API plugin custom, page d'aide standalone, démo doc technique.

  Skills d'invocation MANUELLE — frontmatter modifié pour éviter conflit avec skills schoolsWP existants (lead-magnet-schoolswp, plugin-email-sequence, mini-offre-page-de-vente, schoolswp-article-workflow). Voir INDEX.md pour le routing complet par cas d'usage et NOTICE.md pour l'attribution Apache 2.0.

  Pattern d'invocation : charger un DESIGN.md depuis external-design-systems/<brand>/DESIGN.md (ou content/docs/BRAND_RULES.md pour brand schoolsWP) puis invoquer le sous-skill par référence chemin. Triggers manuels stricts : "newsletter premium" / "email lancement formation" (email-marketing), "pricing 3 tiers" / "tarifs formation tutorlms" (pricing-page), "mockup doc technique" / "page docs standalone" (docs-page).
allowed-tools: Read, Write, Edit, Glob, Grep
---

# External Open-Design Skills (Vague 2)

3 skills HTML générateurs cherry-picked du repo [`nexu-io/open-design`](https://github.com/nexu-io/open-design) (commit `9b57c22c`, Apache 2.0). Companion library de `external-design-systems/` (73 DESIGN.md, Vague 1).

## Workflow d'invocation

### Cas standard — utiliser un design system tiers comme brand

```
Charge .claude/skills/external-design-systems/notion/DESIGN.md
puis lis .claude/skills/external-open-design/pricing-page/SKILL.md
et applique le workflow pour : page tarifs formation TutorLMS
(3 tiers : Starter 47€ / Pro 97€ / Premium 197€).
```

### Cas brand schoolsWP — utiliser BRAND_RULES.md comme tokens

```
Charge content/docs/BRAND_RULES.md comme DESIGN.md de référence
puis lis .claude/skills/external-open-design/email-marketing/SKILL.md
et applique le workflow pour : newsletter featured de lancement
de la formation FluentBoards (date sortie : 15 mai 2026).
```

## Routing rapide

| Demande typique | Skill / fichier à lire |
|---|---|
| "Newsletter premium mensuelle" | `email-marketing/SKILL.md` |
| "Page pricing formation 3 tiers" | `pricing-page/SKILL.md` |
| "Mockup doc API plugin custom" | `docs-page/SKILL.md` |
| "Email FluentCRM quotidien" | Rédaction directe sans skill |
| "Séquence affiliation plugin" | `plugin-email-sequence` (skill schoolsWP existant) |
| "Page de vente longue avec story+proof" | `mini-offre-page-de-vente` (skill schoolsWP existant) |
| "Article SEO long" | `schoolswp-article-workflow` (skill schoolsWP existant) |

Voir `INDEX.md` pour les 3 tables de conflit complètes (email / pricing / docs).

## Garde-fous

- **Ne pas auto-trigger** — frontmatter sous-skills déjà serré, mais rester vigilant sur "email" / "pricing" / "docs" génériques.
- **Brand schoolsWP > brand tiers** — un DESIGN.md tiers est une inspiration esthétique pour le HTML produit, pas un override du brand schoolsWP. Pour livraison finale brand-strict, passer par `external-cc-design` avec le DESIGN.md schoolsWP.
- **Apache 2.0** — frontmatter modifié, contenu workflow verbatim. Voir `NOTICE.md` pour le détail des modifications.
