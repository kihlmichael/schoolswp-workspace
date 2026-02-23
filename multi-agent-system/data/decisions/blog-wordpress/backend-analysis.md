# Backend Analysis — Page Blog WordPress (ArticleCard + WP REST v2 + schema.org)

## Contexte & Décisions antérieures appliquées
- BFF FastAPI avec JWT middleware (routes publiques GET exemptées)
- Cache Redis composite : `wp:posts:{page}:{per_page}:{category}:{lang}` TTL 300s / article 600s / media+author 3600s
- Invalidation webhook HMAC-SHA256 sur `publish_post` / `save_post`
- Normalisation payload WP + fetch parallèle asyncio.gather media+author
- schema.org Article pré-construit côté BFF

---

## Endpoint BFF — GET /api/v1/posts (listing ArticleCard)

### Champs WP REST v2 requis (via `_fields`)
```
id, slug, title.rendered, excerpt.rendered,
date, modified, author, featured_media,
categories, tags, link, yoast_head_json (si plugin Yoast actif)
```

### Payload normalisé retourné au frontend
```json
{
  "id": 42,
  "slug": "mon-article",
  "title": "Titre de l'article",
  "excerpt": "<p>Extrait sanitizé...</p>",
  "published_at": "2024-01-15T10:30:00Z",
  "modified_at": "2024-01-16T08:00:00Z",
  "author": { "id": 3, "name": "Jane Doe", "avatar_url": "..." },
  "thumbnail": { "url": "...", "alt": "...", "width": 800, "height": 450 },
  "categories": [{ "id": 5, "name": "Tech", "slug": "tech" }],
  "read_time_minutes": 4,
  "schema_org": { /* Article JSON-LD pré-construit */ }
}
```

### Calcul read_time (BFF)
```python
import re
words = len(re.findall(r'\w+', strip_html(content_rendered)))
read_time = max(1, round(words / 200))  # 200 mots/min
```

---

## Endpoint BFF — GET /api/v1/posts/{slug}

### Pipeline complet
1. Check Redis `wp:post:{slug}` → HIT : retour immédiat
2. MISS : GET /wp/v2/posts?slug={slug}&_fields=...
3. asyncio.gather(fetch_media(featured_media_id), fetch_author(author_id))
4. HTML sanitize (bleach/nh3) sur content.rendered + excerpt.rendered
5. Construire schema.org Article
6. SET Redis `wp:post:{slug}` TTL 600s
7. Retourner payload normalisé

### Sanitization HTML (sécurité XSS)
```python
import nh3
ALLOWED_TAGS = {"p","h2","h3","h4","ul","ol","li","strong","em","a","img","blockquote","code","pre"}
ALLOWED_ATTRS = {"a": {"href", "title", "rel"}, "img": {"src", "alt", "width", "height"}}
clean_content = nh3.clean(raw_html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)
```

---

## schema.org Article — Construction BFF

```python
def build_schema_org_article(post: NormalizedPost, site_url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post.title[:110],  # max 110 chars spec Google
        "description": strip_html(post.excerpt)[:160],
        "image": {
            "@type": "ImageObject",
            "url": post.thumbnail.url,
            "width": post.thumbnail.width,
            "height": post.thumbnail.height
        },
        "datePublished": post.published_at.isoformat(),
        "dateModified": post.modified_at.isoformat(),
        "author": {
            "@type": "Person",
            "name": post.author.name,
            "url": f"{site_url}/author/{post.author.slug}"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Mon Site",
            "logo": {
                "@type": "ImageObject",
                "url": f"{site_url}/logo.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{site_url}/blog/{post.slug}"
        }
    }
```
> ⚠️ headline tronqué à 110 chars — exigence Google Rich Results

---

## Stratégie Cache Redis — Récapitulatif

| Ressource         | Clé Redis                                      | TTL    | Invalidation         |
|-------------------|------------------------------------------------|--------|----------------------|
| Listing posts     | `wp:posts:{page}:{per_page}:{category}:{lang}` | 300s   | Webhook publish_post |
| Article individuel| `wp:post:{slug}`                               | 600s   | Webhook save_post    |
| Auteur            | `wp:author:{id}`                               | 3600s  | Manuel / TTL         |
| Media/thumbnail   | `wp:media:{id}`                                | 3600s  | Manuel / TTL         |
| JWT blacklist     | `jwt:blacklist:{jti}`                          | = exp  | Révocation immédiate |

---

## Sécurité

### CORS
```python
origins = ["https://monsite.com", "https://www.monsite.com"]
# JAMAIS "*" en production avec credentials
```

### Rate Limiting (Redis sliding window)
- GET /api/v1/posts : 100 req/min/IP
- GET /api/v1/posts/{slug} : 60 req/min/IP
- POST webhook invalidation : 10 req/min + vérif HMAC obligatoire

### Webhook HMAC-SHA256
```python
import hmac, hashlib
def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```

---

## Dépendances externes identifiées
- **Frontend** : props attendues par ArticleCard (structure payload normalisé ci-dessus)
- **SEO** : injection du schema.org JSON-LD dans `<head>` (responsabilité frontend/SSR)
- **WP Plugin** : Yoast SEO optionnel (si présent, utiliser `yoast_head_json` comme fallback)
