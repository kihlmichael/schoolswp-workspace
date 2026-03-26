# Analyse Backend — Page Blog WordPress avec ArticleCard + WP REST v2

## Contexte
- Composant React `ArticleCard` côté frontend (hors scope)
- Endpoint WordPress REST API v2 à exposer via BFF
- SEO schema.org Article (généré côté backend, transmis au frontend)

---

## Architecture retenue : BFF FastAPI (pattern confirmé)

### Pattern décisionnel persisté
- BFF FastAPI normalise les données WP REST v2 brutes
- Fetch parallèle `asyncio.gather` pour media + author + post
- HTML sanitization obligatoire (XSS)
- Schema.org Article pré-construit et transmis au frontend

---

## Endpoints WP REST v2 ciblés

### 1. Listing d'articles
```
GET /wp/v2/posts
  ?_fields=id,slug,title,excerpt,date,modified,author,featured_media,categories,tags,_links
  &per_page=12
  &page={page}
  &status=publish
  &orderby=date
  &order=desc
```

### 2. Article unique
```
GET /wp/v2/posts/{id}?_fields=id,slug,title,content,excerpt,date,modified,author,featured_media,categories,tags,yoast_head_json
GET /wp/v2/users/{author_id}?_fields=id,name,description,avatar_urls,link
GET /wp/v2/media/{featured_media_id}?_fields=id,source_url,alt_text,media_details
```

---

## Modèle de données normalisé (sortie BFF)

```python
class ArticleCardDTO(BaseModel):
    id: int
    slug: str
    title: str                   # extrait de title.rendered + strip HTML
    excerpt: str                 # extrait de excerpt.rendered + strip HTML + truncate 160
    date_published: datetime     # ISO 8601
    date_modified: datetime      # ISO 8601
    author: AuthorDTO
    featured_image: ImageDTO | None
    categories: list[int]
    tags: list[int]
    read_time_minutes: int       # calculé depuis word_count
    schema_org: dict             # schema.org Article JSON-LD pré-construit

class AuthorDTO(BaseModel):
    id: int
    name: str
    avatar_url: str

class ImageDTO(BaseModel):
    url: str
    alt: str
    width: int
    height: int
```

---

## Stratégie de Cache Redis

| Route BFF         | TTL   | Invalidation                          |
|-------------------|-------|---------------------------------------|
| listing /articles | 300s  | webhook WP `publish_post` → flush     |
| article /articles/{slug} | 600s | webhook WP `save_post` → flush key |
| /authors/{id}     | 3600s | rare changement, flush manuel         |
| /media/{id}       | 3600s | rare changement, flush manuel         |

**Clé de cache** : `wp:article:{slug}`, `wp:listing:page:{n}:per:{limit}`

---

## Schema.org Article — Construction BFF

```python
def build_schema_org_article(post: dict, author: dict, image: dict | None) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": strip_html(post["title"]["rendered"])[:110],
        "description": strip_html(post["excerpt"]["rendered"])[:160],
        "datePublished": post["date_gmt"] + "Z",
        "dateModified": post["modified_gmt"] + "Z",
        "author": {
            "@type": "Person",
            "name": author["name"],
            "url": author["link"]
        },
        "publisher": {
            "@type": "Organization",
            "name": settings.SITE_NAME,
            "logo": {"@type": "ImageObject", "url": settings.SITE_LOGO_URL}
        },
        "image": {
            "@type": "ImageObject",
            "url": image["source_url"],
            "width": image["media_details"]["sizes"]["full"]["width"],
            "height": image["media_details"]["sizes"]["full"]["height"]
        } if image else None,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{settings.SITE_URL}/blog/{post['slug']}"
        }
    }
```

---

## Sécurité

- **CORS** : whitelist domaine frontend uniquement, pas de wildcard `*`
- **Rate limiting** : 60 req/min par IP sur les endpoints BFF publics (slowapi)
- **HTML Sanitization** : `bleach.clean()` sur `content.rendered` et `excerpt.rendered`
- **WP Application Passwords** : credentials WP en variables d'env, jamais hardcodés
- **Webhook secret** : HMAC-SHA256 sur payload d'invalidation cache WP → BFF

---

## Dépendances identifiées

- `front_component_props` : structure ArticleCardDTO doit être contractualisée avec frontend
- `seo_url_structure` : slug WP = URL canonique → à aligner avec le router frontend
