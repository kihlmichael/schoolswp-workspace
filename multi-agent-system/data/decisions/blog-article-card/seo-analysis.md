# SEO Analysis — ArticleCard WordPress Blog

## Contexte
- Composant : React `ArticleCard`
- Source : WP REST API v2 (`/wp-json/wp/v2/posts`)
- Schema cible : `schema.org/BlogPosting`

---

## Meta Tags Patterns

### Meta Title
```
{post.title.rendered} | {site_name}
```
- Max 60 caractères
- Mot-clé principal en tête (= titre du post)
- `site_name` récupéré via `/wp-json/wp/v2/settings` (champ `title`)

### Meta Description
```
strip_html(post.excerpt.rendered).slice(0, 155)
// fallback si excerpt vide :
strip_html(post.content.rendered).slice(0, 155)
```
- Strip HTML obligatoire (`excerpt.rendered` retourne du HTML WP)
- 155 chars = limite safe desktop Google
- Aucune meta description vide tolérée (dégrade CTR)

---

## Schema.org — BlogPosting (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{post.title.rendered}",
  "description": "{excerpt strippé, 155 chars}",
  "datePublished": "{post.date_gmt}Z",
  "dateModified": "{post.modified_gmt}Z",
  "author": {
    "@type": "Person",
    "name": "{post._embedded['wp:term'][0].name}",
    "url": "{post._embedded.author[0].link}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{site_name}",
    "logo": {
      "@type": "ImageObject",
      "url": "{site_logo_url}"
    }
  },
  "image": {
    "@type": "ImageObject",
    "url": "{post._embedded['wp:featuredmedia'][0].source_url}",
    "width": 1200,
    "height": 630
  },
  "url": "{post.link}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{post.link}"
  }
}
```
> ⚠️ Requiert `?_embed` sur l'endpoint pour exposer `author` et `wp:featuredmedia`

---

## Core Web Vitals — Points d'impact ArticleCard

| Métrique | Impact | Action |
|----------|--------|--------|
| **LCP** | Featured image = LCP candidate | `fetchpriority="high"` + `loading="eager"` sur la 1ère card visible |
| **CLS** | Dimensions image non définies | Toujours spécifier `width` & `height` sur `<img>` (ratio 16:9 ou 4:3) |
| **INP** | Click sur card = navigation | Éviter `onClick` JS pur → préférer `<a href>` natif pour interactivité immédiate |

---

## Open Graph / Twitter Card

```html
<meta property="og:type" content="article" />
<meta property="og:title" content="{post.title.rendered}" />
<meta property="og:description" content="{excerpt strippé}" />
<meta property="og:image" content="{featuredmedia.source_url}" />
<meta property="og:url" content="{post.link}" />
<meta property="article:published_time" content="{post.date_gmt}Z" />
<meta property="article:modified_time" content="{post.modified_gmt}Z" />
<meta name="twitter:card" content="summary_large_image" />
```

---

## Dépendances identifiées
- `front_image_strategy` : dimensions et formats (WebP, AVIF) de `featuredmedia`
- `back_url_structure` : pattern de slugs WP (`post.link`) pour canonical
- `back_embed_params` : confirmation que `?_embed` est activé sur l'endpoint REST
