# Schema Markup — schoolsWP Marketing

Implémentation des données structurées (schema.org) pour améliorer la visibilité dans les résultats Google.

## Triggers

- "schema", "schema.org"
- "données structurées", "structured data"
- "rich snippets", "rich results"
- "FAQ schema", "review schema"

## Pourquoi le schema markup

### Bénéfices SEO

```
✅ Rich snippets dans les SERP (étoiles, FAQ, prix)
✅ Meilleure compréhension du contenu par Google
✅ Éligibilité aux fonctionnalités spéciales
✅ CTR amélioré (jusqu'à +30%)
✅ Position 0 / Featured snippets
```

### Types de rich results

| Type | Affichage | Impact CTR |
|------|-----------|------------|
| FAQ | Questions dépliables | +15-25% |
| Review | Étoiles jaunes | +10-20% |
| HowTo | Étapes numérotées | +10-15% |
| Product | Prix, dispo, avis | +20-30% |
| Article | Date, auteur, image | +5-10% |
| Course | Infos formation | +15-20% |
| Breadcrumb | Fil d'Ariane | +5-10% |

## Schemas prioritaires schoolsWP

### 1. Organization (site-wide)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "schoolsWP",
  "url": "https://schoolswp.com",
  "logo": "https://schoolswp.com/logo.png",
  "description": "Formation et ressources WordPress pour entrepreneurs et créateurs",
  "founder": {
    "@type": "Person",
    "name": "Michaël KIHL"
  },
  "sameAs": [
    "https://www.linkedin.com/company/schoolswp",
    "https://www.youtube.com/@schoolswp",
    "https://twitter.com/schoolswp"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "contact@schoolswp.com"
  }
}
```

### 2. Article (blog posts)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Comment optimiser les Core Web Vitals sur WordPress",
  "description": "Guide complet pour améliorer LCP, INP et CLS sur votre site WordPress",
  "image": "https://schoolswp.com/images/cwv-guide.jpg",
  "author": {
    "@type": "Person",
    "name": "Michaël KIHL",
    "url": "https://schoolswp.com/about"
  },
  "publisher": {
    "@type": "Organization",
    "name": "schoolsWP",
    "logo": {
      "@type": "ImageObject",
      "url": "https://schoolswp.com/logo.png"
    }
  },
  "datePublished": "2025-01-15",
  "dateModified": "2025-02-01"
}
```

### 3. Course (formations)

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Formation Performance WordPress",
  "description": "Apprends à optimiser ton site WordPress pour un temps de chargement < 2 secondes",
  "provider": {
    "@type": "Organization",
    "name": "schoolsWP",
    "sameAs": "https://schoolswp.com"
  },
  "offers": {
    "@type": "Offer",
    "price": "397",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "validFrom": "2025-01-01"
  },
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online",
    "courseWorkload": "PT12H"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "127"
  }
}
```

### 4. FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Combien de temps faut-il pour optimiser WordPress ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Avec notre méthode, vous pouvez obtenir des résultats significatifs en 1 weekend. La formation complète se fait en 12-15 heures à votre rythme."
      }
    },
    {
      "@type": "Question",
      "name": "La formation est-elle adaptée aux débutants ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui, chaque module part des bases. Vous avez uniquement besoin d'un site WordPress installé. 73% de nos étudiants n'avaient jamais optimisé leur site avant."
      }
    }
  ]
}
```

### 5. HowTo (tutoriels)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Comment activer le cache LiteSpeed sur WordPress",
  "description": "Guide étape par étape pour configurer LiteSpeed Cache",
  "totalTime": "PT10M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "EUR",
    "value": "0"
  },
  "step": [
    {
      "@type": "HowToStep",
      "name": "Installer le plugin",
      "text": "Allez dans Extensions > Ajouter et recherchez 'LiteSpeed Cache'",
      "image": "https://schoolswp.com/images/step1.jpg"
    },
    {
      "@type": "HowToStep",
      "name": "Activer le cache",
      "text": "Dans LiteSpeed Cache > Cache, activez 'Enable Cache'",
      "image": "https://schoolswp.com/images/step2.jpg"
    }
  ]
}
```

### 6. Review / AggregateRating

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Formation Performance WordPress",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "bestRating": "5",
    "worstRating": "1",
    "ratingCount": "127"
  },
  "review": [
    {
      "@type": "Review",
      "author": {
        "@type": "Person",
        "name": "Marie D."
      },
      "datePublished": "2025-01-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5"
      },
      "reviewBody": "Mon score PageSpeed est passé de 34 à 91 en 2 heures."
    }
  ]
}
```

### 7. BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Accueil",
      "item": "https://schoolswp.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Formations",
      "item": "https://schoolswp.com/formations"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Performance WordPress",
      "item": "https://schoolswp.com/formations/performance-wordpress"
    }
  ]
}
```

## Implémentation WordPress

### Option 1 : Plugin (recommandé)

```
YOAST SEO PREMIUM
- Schema automatique pour articles, pages
- FAQ blocks avec schema intégré
- Configuration organisation

RANK MATH
- Schema automatique
- Templates personnalisables
- HowTo block intégré

SCHEMA PRO
- Tous types de schema
- Interface visuelle
- Conditions d'affichage
```

### Option 2 : Code custom

```php
// Dans functions.php ou plugin custom

add_action( 'wp_head', 'schoolswp_schema_organization' );
function schoolswp_schema_organization() {
  if ( is_front_page() ) {
    $schema = [
      '@context' => 'https://schema.org',
      '@type'    => 'Organization',
      'name'     => 'schoolsWP',
      'url'      => home_url(),
      // ... reste du schema
    ];

    printf(
      '<script type="application/ld+json">%s</script>',
      wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE )
    );
  }
}
```

### Option 3 : Gutenberg blocks

```
BLOCS FAQ AVEC SCHEMA INTÉGRÉ
- Yoast FAQ Block
- Rank Math FAQ Block
- Ultimate Blocks

BLOCS HOWTO
- Yoast How-To Block
- Schema & Structured Data for WP
```

## Validation

### Outils de test

```
1. RICH RESULTS TEST (Google)
   https://search.google.com/test/rich-results
   → Vérifie éligibilité rich results

2. SCHEMA MARKUP VALIDATOR
   https://validator.schema.org/
   → Validation syntaxe schema.org

3. GOOGLE SEARCH CONSOLE
   Améliorations > [Type de résultat]
   → Erreurs en production
```

### Erreurs courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| "Missing field" | Champ requis absent | Ajouter le champ |
| "Invalid value" | Format incorrect | Vérifier le type attendu |
| "Page not indexable" | noindex sur la page | Retirer noindex |
| "Structured data mismatch" | Schema ≠ contenu visible | Aligner les deux |

## Checklist implémentation

### Par type de page

```
HOMEPAGE
□ Organization
□ WebSite (avec SearchAction si pertinent)

ARTICLES DE BLOG
□ Article
□ BreadcrumbList
□ FAQPage (si FAQ présente)
□ HowTo (si tutoriel)

PAGES DE FORMATION
□ Course
□ AggregateRating (si avis)
□ FAQPage
□ BreadcrumbList

PAGES PRODUITS (WooCommerce)
□ Product
□ Offer
□ AggregateRating
□ Review

TOUTES LES PAGES
□ BreadcrumbList
```

### Validation finale

```
□ Schema présent sur chaque type de page
□ Validé dans Rich Results Test
□ Pas d'erreurs dans Search Console
□ Données cohérentes avec le contenu visible
□ Images référencées accessibles
□ URLs absolues (pas relatives)
□ JSON-LD valide (pas d'erreurs syntaxe)
```

## Ressources

- [seo-audit.md](seo-audit.md) — Audit SEO complet
- [Schema.org](https://schema.org) — Documentation officielle
- [Google Rich Results](https://developers.google.com/search/docs/appearance/structured-data)
