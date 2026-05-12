---
parent: masteriyo-arbitrage-2026-05-06.md
type: draft-schema
purpose: Ajouter un schema Review au @graph JSON-LD de /masteriyo-lms-avis/
date_drafted: 2026-05-07
---

# Schema Review à ajouter pour /masteriyo-lms-avis/

## Diagnostic

- HTML actuel : @graph Rank Math contient Place, EducationalOrganization+Organization, WebSite, ImageObject, BreadcrumbList, WebPage, Person, BlogPosting
- PAS de Review ni Product, donc pas de rich snippet possible
- Note 4,8/5 mentionnée dans le contenu visible mais ABSENTE du schema
- GSC URL inspect 2026-05-07 confirme : rich_results detected_types = Breadcrumbs uniquement

C'est la cause directe de l'absence de rich snippet étoilé sur la SERP.

## Snippet Review à insérer dans le @graph

```json
{
  "@type": "Review",
  "@id": "https://schoolswp.com/masteriyo-lms-avis/#review",
  "itemReviewed": {
    "@type": "SoftwareApplication",
    "@id": "https://schoolswp.com/masteriyo-lms-avis/#masteriyo",
    "name": "Masteriyo LMS",
    "applicationCategory": "BusinessApplication",
    "applicationSubCategory": "LMS",
    "operatingSystem": "WordPress",
    "url": "https://masteriyo.com",
    "description": "Plugin LMS WordPress avec interface React JS, paiement intégré Stripe/PayPal, content drip Pro, compatible Yoast/Rank Math.",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "EUR",
      "availability": "https://schema.org/InStock",
      "description": "Version gratuite disponible. Plans premium Starter et Growth."
    }
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "4.5",
    "bestRating": "5",
    "worstRating": "1"
  },
  "author": {
    "@id": "https://schoolswp.com/#person"
  },
  "datePublished": "2026-01-12",
  "publisher": {
    "@id": "https://schoolswp.com/#organization"
  },
  "reviewBody": "Masteriyo LMS est un plugin WordPress LMS solide et léger, basé sur React JS, avec une interface intuitive et un paiement intégré sans WooCommerce. Recommandé pour les créateurs débutants ou les projets single-course. Pour les besoins avancés (subscriptions natives, course bundles, marketplace multi-formateurs), je préfère Tutor LMS 3.0+ sur schoolsWP."
}
```

## Note importante sur la valeur de rating

La note 4,8/5 actuelle dans l'article correspond à la moyenne WordPress.org (143 avis vérifiés). Ce n'est PAS la note personnelle de Michael, c'est la note communautaire.

Pour le schema Review, il faut MA note personnelle (Michael KIHL en tant qu'auteur), pas la moyenne wp.org. Je recommande 4,5/5 (alignée avec le ton de la refonte : Masteriyo reste solide pour son audience, juste pas assez complet pour les besoins schoolsWP).

Si tu préfères afficher la moyenne wp.org en plus, il faut un schema AggregateRating séparé (pas Review), avec attribution explicite à la source wp.org. Pour ne pas confondre Google et risquer une pénalité, un seul des deux à la fois est plus safe.

## Méthode de push recommandée

### Option A - Manuel via Rank Math Schema Generator (préféré)

1. Ouvrir l'article /masteriyo-lms-avis/ dans Gutenberg
2. Sidebar Rank Math, onglet Schema, bouton Add Schema, choisir Review
3. Coller les valeurs ci-dessus dans le formulaire Schema Generator
4. Save puis publier
5. Vérifier via GSC URL inspect (re-test live URL) que le schema Review est détecté
6. Soumettre une demande d'indexation pour accélérer

### Option B - Automatisé via mu-plugin (si on industrialise)

Le mu-plugin schoolswp-person-schema.php (cf. mémoire project_person_schema_enrichment.md) enrichit déjà le schema Person. On peut ajouter une fonction qui injecte un schema Review sur tous les articles d'avis schoolsWP basée sur les postmeta rank_math_schema_Review. Tool à créer si on souhaite industrialiser sur les 7+ articles d'avis listés plus bas.

**Recommandation** : Option A en premier (cas masteriyo seul). Option B si on souhaite traiter tous les avis d'un coup.

## Validation post-deploy

1. GSC URL inspect sur https://schoolswp.com/masteriyo-lms-avis/ après publication, attendre que rich_results.detected_types inclue Review ou Product
2. Test Rich Results : https://search.google.com/test/rich-results
3. Schema Markup Validator : https://validator.schema.org/
4. Re-crawl forcé via Request indexing dans GSC après validation

Délai d'apparition typique du rich snippet : 1 à 3 semaines post-validation.

## Articles potentiellement concernés par le même bug

À vérifier sur les autres articles d'avis schoolsWP. Il est probable que le bug soit systémique car aucun schema Review n'a été configuré dans Rank Math au moment de la rédaction des articles d'avis.

- /fluentcrm-avis/
- /fluentboards-avis/
- /fluentforms-avis/
- /kadence-avis/
- /rank-math-avis/
- /wp-rocket-avis/
- /flyingpress-avis/

Si confirmé, mission séparée audit-schema-review-tous-articles-avis à planifier. Impact estimé : récupération potentielle de rich snippets sur l'ensemble du portfolio avis schoolsWP, gain CTR significatif.
