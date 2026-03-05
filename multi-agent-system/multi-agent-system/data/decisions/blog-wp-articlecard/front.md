# Analyse Frontend — ArticleCard WordPress REST v2

## Contexte
Page blog WordPress avec composant React `ArticleCard`, endpoint WP REST API v2, SEO schema.org Article.

---

## Décisions architecturales rappelées (mémoire longue)
1. **Typage WPPost** : inclure `_embedded` (wp:featuredmedia + author) — évite les N+1 requêtes
2. **Sanitisation obligatoire** : `title.rendered` et `excerpt.rendered` sont du HTML — DOMPurify requis
3. **Pattern stretched-link** : un seul `<a>` par carte pour l'accessibilité
4. **React.memo** : liste de cards = re-renders coûteux
5. **CLS image** : `aspect-ratio` CSS + `loading="lazy"` impératif

---

## Recommandations détaillées

### R1 — Typer WPPost avec _embedded et sanitiser avec DOMPurify
```ts
interface WPFeaturedMedia {
  source_url: string;
  alt_text: string;
  media_details: { width: number; height: number };
}

interface WPPost {
  id: number;
  slug: string;
  link: string;
  date: string; // ISO 8601
  title: { rendered: string };
  excerpt: { rendered: string };
  _embedded?: {
    'wp:featuredmedia'?: [WPFeaturedMedia];
    author?: [{ name: string; avatar_urls: Record<string, string> }];
  };
}
```
→ Fetch avec `?_embed` sur l'endpoint `/wp-json/wp/v2/posts`

### R2 — Composant ArticleCard performant
```tsx
import React, { memo } from 'react';
import DOMPurify from 'dompurify';

const ArticleCard = memo(({ post }: { post: WPPost }) => {
  const media = post._embedded?.['wp:featuredmedia']?.[0];
  const author = post._embedded?.author?.[0];
  const cleanTitle = DOMPurify.sanitize(post.title.rendered, { ALLOWED_TAGS: [] });
  const cleanExcerpt = DOMPurify.sanitize(post.excerpt.rendered, { ALLOWED_TAGS: ['p', 'strong', 'em'] });

  return (
    <article aria-labelledby={`title-${post.id}`}>
      {media && (
        <div className="card__media">
          <img
            src={media.source_url}
            alt={media.alt_text || cleanTitle}
            width={media.media_details.width}
            height={media.media_details.height}
            loading="lazy"
            decoding="async"
          />
        </div>
      )}
      <div className="card__body">
        <h2 id={`title-${post.id}`} className="card__title">
          <a href={post.link} className="card__link stretched-link">
            {cleanTitle}
          </a>
        </h2>
        <time dateTime={post.date}>
          {new Intl.DateTimeFormat('fr-FR', { dateStyle: 'long' }).format(new Date(post.date))}
        </time>
        {author && <span className="card__author">{author.name}</span>}
        <div
          className="card__excerpt"
          dangerouslySetInnerHTML={{ __html: cleanExcerpt }}
        />
      </div>
    </article>
  );
});
```

### R3 — CSS anti-CLS
```css
.card__media {
  aspect-ratio: 16 / 9;        /* réserve l'espace AVANT chargement image */
  overflow: hidden;
  background-color: #f0f0f0;   /* placeholder couleur */
}

.card__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Stretched-link pattern */
.card {
  position: relative;
}

.stretched-link::after {
  content: '';
  position: absolute;
  inset: 0;
}
```

### R4 — Skeleton loading
```tsx
const ArticleCardSkeleton = () => (
  <article aria-busy="true" aria-label="Chargement de l'article">
    <div className="card__media skeleton" />
    <div className="card__body">
      <div className="skeleton skeleton--title" />
      <div className="skeleton skeleton--text" />
      <div className="skeleton skeleton--text" style={{ width: '70%' }} />
    </div>
  </article>
);
```

### R5 — Dépendances hors scope frontend
- **Endpoint REST WP v2** : `/wp-json/wp/v2/posts?_embed&per_page=10` → dépend du backend WP
- **SEO schema.org** : le JSON-LD `Article` doit être injecté côté serveur (SSR/SSG) ou via Helmet — dépend de la stratégie SEO

---

## Warnings

### W1 — XSS via dangerouslySetInnerHTML
`excerpt.rendered` et `title.rendered` contiennent du HTML généré par WP. Sans DOMPurify, injection XSS directe. Ne jamais utiliser sans sanitisation même si la source est "de confiance".

### W2 — CLS images si width/height manquants dans _embedded
`media_details` peut être absent si le media est externe ou si le plugin WP ne l'expose pas. Prévoir un fallback `aspect-ratio: 16/9` CSS obligatoire.

### W3 — Performance N+1 sans ?_embed
Sans le paramètre `?_embed`, WP REST retourne des ID uniquement pour l'image et l'auteur. Chaque card déclencherait une requête supplémentaire → dégradation sévère des LCP/TTI sur les listes.

---

## Dépendances identifiées
- `back_api_schema` : structure exacte de l'endpoint `/wp-json/wp/v2/posts`, champs custom ACF éventuels
- `seo_schema_article` : stratégie d'injection du JSON-LD schema.org Article (SSR, Helmet, plugin WP)
