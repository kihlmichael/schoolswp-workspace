# Analyse Frontend — ArticleCard WordPress REST API

## Contexte
- Composant React `ArticleCard` consommant l'endpoint WP REST API v2 (`/wp-json/wp/v2/posts`)
- SEO schema.org Article géré côté frontend (JSON-LD)
- Environnement : React 18+, TypeScript strict

---

## Recommandations

### 1. Typage strict de la réponse WP REST v2
```typescript
interface WPPost {
  id: number;
  date: string; // ISO 8601
  slug: string;
  link: string;
  title: { rendered: string };
  excerpt: { rendered: string; protected: boolean };
  content: { rendered: string; protected: boolean };
  featured_media: number;
  _embedded?: {
    "wp:featuredmedia"?: Array<{
      source_url: string;
      alt_text: string;
      media_details: { width: number; height: number };
    }>;
    author?: Array<{ name: string; avatar_urls: Record<string, string> }>;
  };
}
```
Utiliser `_embed=true` sur l'appel REST pour fusionner media + author en 1 requête.

### 2. Composant ArticleCard mémoïsé avec skeleton
```tsx
const ArticleCard = React.memo<{ post: WPPost; priority?: boolean }>(
  ({ post, priority = false }) => {
    const media = post._embedded?.["wp:featuredmedia"]?.[0];
    const author = post._embedded?.author?.[0];

    return (
      <article className="article-card" aria-label={post.title.rendered}>
        <div className="article-card__media-wrapper">
          {media ? (
            <img
              src={media.source_url}
              alt={media.alt_text || post.title.rendered}
              width={media.media_details.width}
              height={media.media_details.height}
              loading={priority ? "eager" : "lazy"}
              decoding="async"
              fetchpriority={priority ? "high" : "auto"}
            />
          ) : (
            <div className="article-card__media-placeholder" aria-hidden="true" />
          )}
        </div>
        <div className="article-card__body">
          <h2
            className="article-card__title"
            dangerouslySetInnerHTML={{ __html: post.title.rendered }}
          />
          <p
            className="article-card__excerpt"
            dangerouslySetInnerHTML={{ __html: post.excerpt.rendered }}
          />
          {author && (
            <footer className="article-card__meta">
              <span>{author.name}</span>
              <time dateTime={post.date}>
                {new Date(post.date).toLocaleDateString("fr-FR")}
              </time>
            </footer>
          )}
        </div>
      </article>
    );
  }
);
ArticleCard.displayName = "ArticleCard";
```

### 3. CSS anti-CLS — aspect-ratio fixé
```css
.article-card__media-wrapper {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background-color: #f0f0f0; /* placeholder visible pendant le chargement */
}

.article-card__media-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.2s ease;
}
```

### 4. Skeleton loader (état de chargement)
```tsx
const ArticleCardSkeleton = () => (
  <div className="article-card article-card--skeleton" aria-hidden="true">
    <div className="article-card__media-wrapper skeleton-block" />
    <div className="article-card__body">
      <div className="skeleton-line skeleton-line--title" />
      <div className="skeleton-line" />
      <div className="skeleton-line skeleton-line--short" />
    </div>
  </div>
);
```

### 5. JSON-LD schema.org Article injecté via React Portal/Helmet
```tsx
const ArticleJsonLd = ({ post }: { post: WPPost }) => {
  const media = post._embedded?.["wp:featuredmedia"]?.[0];
  const author = post._embedded?.author?.[0];

  const schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: post.title.rendered.replace(/<[^>]+>/g, ""),
    datePublished: post.date,
    dateModified: post.modified ?? post.date,
    image: media?.source_url,
    author: author
      ? { "@type": "Person", name: author.name }
      : undefined,
    url: post.link,
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
};
```

---

## Warnings

- `dangerouslySetInnerHTML` sur title/excerpt : risque XSS si WP est compromis — assainir avec DOMPurify côté client ou garantir la confiance du contenu WP
- La prop `modified` n'est pas dans le type WPPost de base, vérifier que l'endpoint retourne bien ce champ (nécessite `context=edit` ou champ custom)
- CORS doit être configuré côté WP pour autoriser les appels depuis le domaine React

---

## Dépendances identifiées
- `back_api_schema` : endpoint `/wp-json/wp/v2/posts?_embed=true&per_page=X` — confirmer les champs exposés et la pagination (headers `X-WP-Total`, `X-WP-TotalPages`)
- `seo_schema_org` : le champ `dateModified` (`post.modified`) doit être exposé par l'API — vérifier avec l'équipe backend WP
