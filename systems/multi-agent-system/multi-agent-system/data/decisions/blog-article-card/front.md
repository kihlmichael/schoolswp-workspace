# Analyse Frontend — ArticleCard Blog WordPress

## Contexte
- Composant React ArticleCard pour page blog WordPress
- Consommation endpoint REST WP v2
- SEO schema.org Article (hors scope front, signalé en depends_on)

## Périmètre Frontend analysé
- Architecture composant ArticleCard (React 18+, TypeScript)
- Typage des données WP REST API v2
- Performance (LCP, CLS, FID/INP)
- Accessibilité & UX

---

## Recommandations détaillées

### 1. Typer strictement la réponse WP REST API v2
```typescript
interface WPPost {
  id: number;
  date: string;
  slug: string;
  link: string;
  title: { rendered: string };
  excerpt: { rendered: string; protected: boolean };
  content: { rendered: string; protected: boolean };
  featured_media: number;
  _embedded?: {
    'wp:featuredmedia'?: Array<{
      source_url: string;
      alt_text: string;
      media_details: { width: number; height: number };
    }>;
    author?: Array<{ name: string; avatar_urls: Record<string, string> }>;
  };
}
```

### 2. Composant ArticleCard avec skeleton loading
- Utiliser `React.Suspense` + skeleton pour éviter le CLS
- `aspect-ratio: 16/9` sur le conteneur image pour réserver l'espace

### 3. Image optimisée avec next/image ou img natif + sizes
- Passer `sizes` responsive pour éviter le LCP dégradé
- Toujours fournir `alt` depuis `_embedded['wp:featuredmedia'][0].alt_text`

### 4. Sanitisation du HTML WordPress
- `excerpt.rendered` et `title.rendered` contiennent du HTML — utiliser `DOMPurify`

### 5. Accessibilité carte article
- La carte entière doit être cliquable mais avec un seul `<a>` dans le DOM (pattern "stretched link")
- `aria-label` sur le lien pour les lecteurs d'écran

---

## Warnings
- CLS si image sans dimensions réservées
- XSS si rendu direct de `excerpt.rendered` sans sanitisation
- Dépendance SEO schema.org hors scope

## Dépendances externes
- back_api_schema (endpoint WP REST v2 + _embed support)
- seo_schema_article (JSON-LD Article côté backend ou Next.js Head)
