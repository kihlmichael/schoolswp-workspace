# Analyse Backend — Blog WordPress ArticleCard

## Contexte
- Endpoint : WordPress REST API v2
- Composant : ArticleCard (React, scope frontend — ignoré)
- SEO : schema.org Article (dépendance signalée)

## Endpoints concernés

### Listing articles
`GET /wp/v2/posts?_fields=id,slug,title,excerpt,date,modified,featured_media,author,categories,tags,yoast_head_json&per_page=10&page=1`

### Article unique
`GET /wp/v2/posts/{id}?_fields=id,slug,title,content,excerpt,date,modified,featured_media,author,categories,tags,yoast_head_json`

### Media (image featured)
`GET /wp/v2/media/{media_id}?_fields=id,source_url,alt_text,media_details`

## Stratégie Cache Redis

| Ressource        | Clé Redis                          | TTL    | Invalidation          |
|------------------|------------------------------------|--------|-----------------------|
| Listing posts    | `wp:posts:page:{n}:per:{x}`        | 300s   | Hook `save_post` WP   |
| Post unique      | `wp:post:{id}`                     | 600s   | Hook `save_post` WP   |
| Media            | `wp:media:{id}`                    | 3600s  | Rarement modifié      |
| Authors          | `wp:author:{id}`                   | 1800s  | Hook `profile_update` |

Invalidation active via webhook WP → endpoint backend `/api/cache/invalidate` (auth HMAC-SHA256).

## Sécurité

- CORS : whitelist domaines frontend uniquement, bloquer `*`
- Rate limiting : 60 req/min par IP sur les endpoints publics (Redis token bucket)
- Auth WP Application Passwords pour endpoints privés (brouillons, previews)
- Headers recommandés : `Cache-Control: public, max-age=300, stale-while-revalidate=60`

## Modèle de données normalisé (sortie API BFF)

```json
{
  "id": 42,
  "slug": "mon-article",
  "title": "Mon Article de Blog",
  "excerpt": "Résumé court...",
  "content": "<p>HTML sanitized...</p>",
  "publishedAt": "2024-01-15T10:30:00Z",
  "modifiedAt": "2024-01-20T14:00:00Z",
  "author": {
    "id": 3,
    "name": "Jane Doe",
    "avatar": "https://..."
  },
  "featuredImage": {
    "url": "https://...",
    "alt": "Description image",
    "width": 1200,
    "height": 630
  },
  "categories": [{ "id": 5, "name": "Tech", "slug": "tech" }],
  "tags": [{ "id": 12, "name": "Python", "slug": "python" }],
  "seo": {
    "metaTitle": "...",
    "metaDescription": "...",
    "schemaOrg": { "@context": "...", "@type": "Article", "..." : "..." }
  }
}
```

## Pattern BFF recommandé (Python/FastAPI)

```python
@router.get("/articles/{slug}", response_model=ArticleOut)
async def get_article(slug: str, cache: Redis = Depends(get_redis)):
    cache_key = f"wp:post:slug:{slug}"
    if cached := await cache.get(cache_key):
        return ArticleOut.parse_raw(cached)
    
    # 1. Fetch WP post by slug
    post = await wp_client.get_post_by_slug(slug)
    # 2. Parallel fetch media + author
    media, author = await asyncio.gather(
        wp_client.get_media(post["featured_media"]),
        wp_client.get_author(post["author"])
    )
    # 3. Normalize + sanitize HTML content
    article = normalize_article(post, media, author)
    
    await cache.setex(cache_key, 600, article.json())
    return article
```

## Dépendances inter-services
- SEO / schema.org : généré côté backend dans le champ `seo.schemaOrg`, transmis au frontend
- Invalidation cache : webhook WordPress → backend (sécurisé HMAC)
