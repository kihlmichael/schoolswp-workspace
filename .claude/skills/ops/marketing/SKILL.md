---
name: marketing
description: Marketing skills for schoolsWP - CRO, copywriting, SEO, email sequences, pricing strategy, and analytics. Use when user asks about conversion optimization, landing pages, email marketing, SEO audit, pricing, or growth strategies. Applies proven frameworks while respecting schoolsWP brand voice.
user-invocable: true
triggers:
  - CRO
  - conversion optimization
  - landing page
  - copywriting
  - email sequence
  - drip campaign
  - SEO audit
  - pricing strategy
  - A/B test
  - analytics
  - marketing ideas
metadata:
  brand: schoolsWP
  version: 1.0.0
  based-on: coreyhaines31/marketingskills
---

# schoolsWP Marketing Skills

Collection de compétences marketing spécialisées pour schoolsWP, basée sur les frameworks de Conversion Factory adaptés à l'univers WordPress et au ton schoolsWP.

## Philosophie schoolsWP

Avant d'appliquer ces frameworks marketing, rappelle-toi les principes schoolsWP :

1. **Pédagogie avant vente** — On enseigne, on ne manipule pas
2. **Clarté technique** — Simplifier sans dumbing down
3. **Preuves concrètes** — Données, benchmarks, exemples réels
4. **Ton direct** — Pas de fluff, pas de promesses vides
5. **WordPress-first** — Toujours contextualiser pour l'écosystème WP

## Skills disponibles

### Conversion Optimization (CRO)

| Skill | Trigger | Description |
|-------|---------|-------------|
| [page-cro](references/conversion/page-cro.md) | "optimise cette page", "CRO" | Optimisation des pages marketing |
| [form-cro](references/conversion/form-cro.md) | "optimise ce formulaire" | Optimisation des formulaires |
| [signup-flow-cro](references/conversion/signup-flow-cro.md) | "tunnel d'inscription" | Optimisation des flows d'inscription |
| [ab-testing](references/conversion/ab-testing.md) | "A/B test", "split test" | Mise en place de tests A/B |

### Copywriting

| Skill | Trigger | Description |
|-------|---------|-------------|
| [copywriting](references/copywriting/copywriting.md) | "écris du copy", "landing page" | Rédaction marketing orientée conversion |
| [copy-editing](references/copywriting/copy-editing.md) | "améliore ce texte" | Révision et optimisation de copy existant |
| [email-sequence](references/copywriting/email-sequence.md) | "email sequence", "drip campaign" | Création de séquences email |

### SEO

| Skill | Trigger | Description |
|-------|---------|-------------|
| [seo-audit](references/seo/seo-audit.md) | "audit SEO", "pourquoi je ne ranke pas" | Audit technique et on-page |
| [programmatic-seo](references/seo/programmatic-seo.md) | "SEO programmatique" | Création de contenu SEO à grande échelle |
| [schema-markup](references/seo/schema-markup.md) | "schema.org", "données structurées" | Implémentation de structured data |

### Stratégie

| Skill | Trigger | Description |
|-------|---------|-------------|
| [pricing-strategy](references/strategy/pricing-strategy.md) | "prix", "tarification", "monétisation" | Stratégie de pricing et packaging |
| [launch-strategy](references/strategy/launch-strategy.md) | "lancement", "launch" | Planification de lancement produit |
| [marketing-psychology](references/strategy/marketing-psychology.md) | "psychologie", "persuasion" | Principes de persuasion éthique |

### Analytics

| Skill | Trigger | Description |
|-------|---------|-------------|
| [analytics-tracking](references/analytics/analytics-tracking.md) | "GA4", "tracking", "analytics" | Configuration et audit analytics |

## Utilisation

### Invocation directe

```
/schoolswp-marketing-skills page-cro [URL ou contenu de la page]
/schoolswp-marketing-skills email-sequence welcome [contexte]
/schoolswp-marketing-skills seo-audit [domaine]
```

### Invocation contextuelle

Claude détecte automatiquement l'intention :
- "Ma page de vente ne convertit pas" → `page-cro`
- "J'ai besoin d'une séquence de bienvenue" → `email-sequence`
- "Audite le SEO de schoolswp.com" → `seo-audit`

## Workflow type CRO

```
1. Audit initial (identifier les problèmes)
   └── page-cro | form-cro | signup-flow-cro

2. Optimisation copy (améliorer le messaging)
   └── copywriting | copy-editing

3. Test (valider les hypothèses)
   └── ab-testing

4. Mesure (tracker les résultats)
   └── analytics-tracking
```

## Adaptation schoolsWP

### Ton marketing schoolsWP

| À éviter | Préférer |
|----------|----------|
| "Révolutionnez votre site" | "Accélère ton WordPress de 40%" |
| "Solution magique" | "Méthode en 5 étapes" |
| "Devenez un expert" | "Apprends à optimiser toi-même" |
| "Offre limitée !!!" | "Formation disponible jusqu'au [date]" |
| Urgence artificielle | Valeur concrète et mesurable |

### Preuves schoolsWP

Toujours inclure dans le copy :
- **Données mesurables** : "Score PageSpeed de 95+", "Temps de chargement < 2s"
- **Résultats clients** : Screenshots, témoignages avec contexte
- **Expertise WordPress** : Références aux standards WP, Gutenberg, Core Web Vitals
- **Transparence** : Limites, cas où ça ne marche pas

### CTAs schoolsWP

| Générique | schoolsWP |
|-----------|-----------|
| "En savoir plus" | "Voir le guide complet" |
| "S'inscrire" | "Recevoir la checklist gratuite" |
| "Acheter" | "Démarrer la formation" |
| "Contacter" | "Poser ta question" |

## Intégration avec autres skills

- **05_Branding** : Vérifier la cohérence du copy avec le ton schoolsWP
- **04_WordPress** : Contexte technique pour les pages WP
- **06_Dev** : Implémentation technique (schema markup, analytics)

## Ressources

- [Marketing Skills Repository](https://github.com/coreyhaines31/marketingskills) — Source originale
- [Conversion Factory](https://conversionfactory.co/) — Méthodologie CRO
- Brand guidelines : [05_Branding/references/](../05_Branding/references/)

---

**schoolsWP Marketing** — Du marketing qui enseigne, pas qui manipule.
