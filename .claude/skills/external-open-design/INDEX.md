# INDEX — external-open-design

3 skills HTML générateurs cherry-picked de `nexu-io/open-design` (Apache 2.0). **Invocation manuelle uniquement** — frontmatter modifié pour éviter les triggers génériques (voir `NOTICE.md`).

Chaque skill produit du HTML standalone qui s'appuie sur un `DESIGN.md` injecté en contexte (voir `external-design-systems/` pour la bibliothèque de 73 design systems).

## Les 3 skills

| Skill | Sortie | Usage schoolsWP type |
|---|---|---|
| `open-design-email-marketing` | HTML email centré 600-680px, masthead/hero/lockup/CTA/specs grid/footer | Newsletter featured ~1-2/mois (annonce lancement formation, partenariat plugin majeur, édition spéciale) |
| `open-design-pricing-page` | HTML page pricing single screen, 2/3/4 tiers + comparison table + FAQ | Page tarifs formation TutorLMS premium, bundle FluentCart, abonnement membership |
| `open-design-docs-page` | HTML doc 3 colonnes (left nav + body + right TOC) | Mockup doc API plugin custom, page d'aide produit standalone, démo doc technique brief client |

## Routing — quand utiliser quel skill

### Tu veux un email...

| Cas | Skill / outil |
|---|---|
| Email FluentCRM quotidien plain text | Rédaction directe sans skill |
| Séquence affiliation découverte plugin | `plugin-email-sequence` |
| Email welcome capture lead-magnet | `lead-magnet-schoolswp` |
| Recyclage email reçu vers article | `email-to-content` |
| Nurturing générique anglais | `external-antigravity/email-sequence` |
| **Newsletter featured visuelle premium** | **`open-design-email-marketing`** |

### Tu veux une page de prix / offre...

| Cas | Skill / outil |
|---|---|
| Page de vente longue avec story/proof/objections/garantie | `mini-offre-page-de-vente` |
| Page affiliation tiers comparatif plugin | `landing-page-factory` |
| Landing capture lead-magnet | `lead-magnet-schoolswp` |
| Prototypage rapide visuel exploratoire | `aidesigner` (T0) |
| Production HTML brand-strict finale | `external-cc-design` (T1) |
| **Page pricing tiers + comparison + FAQ** | **`open-design-pricing-page`** |

### Tu veux une page docs...

| Cas | Skill / outil |
|---|---|
| Doc TutorLMS publiée sur schoolswp.com | WordPress + thème Kadence directement |
| Runbook markdown interne | `docs/runbooks-operationnels.md` plain markdown |
| Article tutoriel SEO long | `schoolswp-article-workflow` |
| Landing produit avec sections marketing | `open-design-pricing-page` ou `cc-design` |
| **Mockup visuel doc technique standalone** | **`open-design-docs-page`** |

## Workflow d'invocation

### Pattern recommandé : skill + DESIGN.md de référence

Pour avoir un rendu cohérent avec une marque connue, charger un DESIGN.md de `external-design-systems/` en contexte avant d'invoquer le skill OD :

```
Charge .claude/skills/external-design-systems/notion/DESIGN.md
puis invoque open-design-pricing-page pour la page tarifs formation TutorLMS
(3 tiers : Starter 47€ / Pro 97€ / Premium 197€).
```

### Pattern alternatif : skill + brand schoolsWP

Si tu veux que le rendu colle au brand schoolsWP (et non à une marque de référence), charge `content/docs/BRAND_RULES.md` en contexte au lieu d'un DESIGN.md tiers. Le skill OD requiert un DESIGN.md mais accepte n'importe quelle source de tokens.

## Hors scope (rejets documentés)

Les 28 autres skills d'Open Design n'ont pas été importés. Voir `NOTICE.md` pour le détail des rejets et des raisons.

Si un cas d'usage futur justifie un nouvel import (par ex. besoin réel de `social-carousel`, `team-okrs`, `eng-runbook`), suivre le même pattern d'évaluation comparative + frontmatter modifié + lock entry.
