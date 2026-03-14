# Analyse Backend — Page Blog WordPress + REST WP v2

## Contexte
- Stack : WordPress comme headless CMS, React frontend, endpoint REST WP v2
- Périmètre backend : endpoint, auth, cache, sécurité, modèle de données

## Endpoints REST WP v2 identifiés

### GET /wp/v2/posts
```
GET /wp/v2/posts
  ?_fields=id,slug,title,excerpt,date,modified,author,featured_media,categories,tags,yoast_head_json
  &per_page=12
  &page=1
  &status=publish
  &orderby=date
  &order=desc
```

### GET /wp/v2/posts/:id (article unique)
```
GET /wp/v2/posts/{id}
  ?_fields=id,slug,title,content,excerpt,date,modified,author,featured_media,categories,tags,yoast_head_json
```

### Endpoints auxiliaires nécessaires
- GET /wp/v2/media/{id}         → image featured (src, alt, sizes)
- GET /wp/v2/users/{id}         → auteur (name, avatar_urls)
- GET /wp/v2/categories          → labels catégories
- GET /wp/v2/tags                → labels tags

## Stratégie Cache Redis

| Endpoint          | TTL    | Clé de cache                          | Invalidation         |
|-------------------|--------|---------------------------------------|----------------------|
| /wp/v2/posts      | 300s   | `blog:posts:page:{n}:per:{pp}`        | Hook WP save_post    |
| /wp/v2/posts/{id} | 600s   | `blog:post:{id}`                      | Hook WP save_post    |
| /wp/v2/media/{id} | 3600s  | `blog:media:{id}`                     | Rare, TTL suffisant  |
| /wp/v2/users/{id} | 3600s  | `blog:author:{id}`                    | Rare, TTL suffisant  |

## Sécurité & Auth

- Lecture seule : pas de JWT requis pour posts published
- CORS : restreindre `Access-Control-Allow-Origin` au domaine frontend uniquement
- Rate limiting : 100 req/min par IP sur le proxy/BFF
- Headers WP à supprimer côté proxy : X-WP-Nonce, Link (expose pagination interne)
- Application password WP si accès aux drafts nécessaire (scope à définir)

## Modèle de données ArticleCard (payload normalisé)

```typescript
interface ArticleCardDTO {
  id: number;
  slug: string;
  title: string;           // rendered (HTML décodé)
  excerpt: string;         // rendered, strip_tags côté BFF
  publishedAt: string;     // ISO 8601
  modifiedAt: string;      // ISO 8601
  author: {
    id: number;
    name: string;
    avatarUrl: string;     // 96px
  };
  featuredImage: {
    src: string;
    srcset: string;
    alt: string;
    width: number;
    height: number;
  };
  categories: { id: number; name: string; slug: string }[];
  readingTimeMin: number;  // calculé : content.length / 200
}
```

## Schema.org Article (données sources BFF)

Champs nécessaires depuis WP pour schema.org Article :
- headline      → title.rendered
- datePublished → date (ISO)
- dateModified  → modified (ISO)
- author.name   → user.name
- image         → featured_media (src + dimensions)
- description   → excerpt.rendered (strip_tags)
- url           → link (champ WP)

## Risques identifiés

1. N+1 queries : chaque post nécessite 3 appels (media, author, catégories) → résoudre avec BFF aggregator
2. WP sans cache natif : ajouter plugin WP REST Cache ou Redis Object Cache côté WP
3. Payload verbeux si _fields oublié : monitorer taille réponse
