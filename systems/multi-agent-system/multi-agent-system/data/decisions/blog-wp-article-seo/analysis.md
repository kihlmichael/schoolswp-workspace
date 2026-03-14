# SEO Analysis — Blog WordPress ArticleCard + REST WP v2

## Contexte
- Composant : React `ArticleCard`
- Source de données : WP REST API v2 (`/wp-json/wp/v2/posts`)
- Objectif SEO : Schema.org Article complet, meta tags, Core Web Vitals

---

## 1. META TAGS PATTERNS

### Meta Title
```
{post.title.rendered} | {site_name}
```
- Max **60 caractères**
- Mot-clé principal en tête du titre
- `site_name` = constante d'environnement ou endpoint `/wp-json/wp/v2/settings`

### Meta Description
```
strip_html(post.excerpt.rendered).slice(0, 155)
// Fallback si excerpt vide :
strip_html(post.content.rendered).slice(0, 155)
```
- Jamais généré dynamiquement depuis le composant React (SSR/SSG requis)
- Éviter les caractères spéciaux non encodés

### Canonical URL
```
post.link  // fourni nativement par WP REST API v2
```
- Toujours injecter `<link rel="canonical">` pour éviter duplicate content paginated

### Open Graph (obligatoire pour partage social)
```
og:title   = post.title.rendered
og:description = strip_html(post.excerpt.rendered).slice(0, 200)
og:image   = post._embedded['wp:featuredmedia'][0].source_url
og:image:width  = post._embedded['wp:featuredmedia'][0].media_details.width
og:image:height = post._embedded['wp:featuredmedia'][0].media_details.height
og:type    = "article"
og:url     = post.link
article:published_time = post.date_gmt (ISO 8601)
article:modified_time  = post.modified_gmt (ISO 8601)
article:author = post._embedded.author[0].link
```

### Twitter Card
```
twitter:card = "summary_large_image"
twitter:title = post.title.rendered
twitter:description = strip_html(post.excerpt.rendered).slice(0, 200)
twitter:image = post._embedded['wp:featuredmedia'][0].source_url
```

---

## 2. SCHEMA.ORG — BlogPosting (sous-type de Article)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{post.title.rendered}",
  "description": "{strip_html(post.excerpt.rendered).slice(0, 160)}",
  "url": "{post.link}",
  "datePublished": "{post.date_gmt}",
  "dateModified": "{post.modified_gmt}",
  "author": {
    "@type": "Person",
    "name": "{post._embedded.author[0].name}",
    "url": "{post._embedded.author[0].link}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{site_name}",
    "logo": {
      "@type": "ImageObject",
      "url": "{site_logo_url}",
      "width": 600,
      "height": 60
    }
  },
  "image": {
    "@type": "ImageObject",
    "url": "{post._embedded['wp:featuredmedia'][0].source_url}",
    "width": "{post._embedded['wp:featuredmedia'][0].media_details.width}",
    "height": "{post._embedded['wp:featuredmedia'][0].media_details.height}"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{post.link}"
  },
  "wordCount": "{word_count(post.content.rendered)}",
  "inLanguage": "fr-FR",
  "keywords": "{post.tags -> mapped to tag names via _embedded['wp:term']}"
}
```

> ⚠️ Requiert `?_embed` dans l'endpoint WP REST pour récupérer author, featuredmedia, wp:term en une seule requête.

---

## 3. CORE WEB VITALS — Points d'impact SEO

### LCP (Largest Contentful Paint) — CRITIQUE
- L'image featured (`wp:featuredmedia`) est quasi-systématiquement l'élément LCP sur une ArticleCard
- **Action** : ajouter `fetchpriority="high"` + `loading="eager"` sur l'image above-the-fold
- **Action** : fournir `width` et `height` depuis `media_details` pour éviter le layout shift
- Cible : LCP < 2.5s

### CLS (Cumulative Layout Shift) — IMPORTANT
- Réserver l'espace image AVANT le chargement avec ratio CSS (`aspect-ratio` ou padding-top hack)
- Skeleton loader React doit avoir les mêmes dimensions que le contenu final
- Cible : CLS < 0.1

### INP (Interaction to Next Paint) — MODÉRÉ
- Pas d'impact direct sur ArticleCard statique
- Vigilance si pagination ou infinite scroll React déclenche re-renders massifs

---

## 4. ENDPOINT WP REST v2 — Paramètres SEO-critiques

```
GET /wp-json/wp/v2/posts?_embed&per_page=10&orderby=date&order=desc
```

Champs exploitables pour SEO :
| Champ API | Usage SEO |
|---|---|
| `title.rendered` | meta title, headline schema |
| `excerpt.rendered` | meta description, description schema |
| `date_gmt` | datePublished schema, article:published_time OG |
| `modified_gmt` | dateModified schema, article:modified_time OG |
| `link` | canonical, og:url, url schema |
| `_embedded.author[0]` | author schema Person |
| `_embedded['wp:featuredmedia'][0]` | og:image, image schema, LCP element |
| `_embedded['wp:term']` | keywords schema |
| `slug` | URL SEO-friendly (vérifier structure permalink WP) |

---

## 5. DÉPENDANCES IDENTIFIÉES

- `front_image_strategy` : stratégie de resize/srcset pour featured image (WebP, dimensions, CDN)
- `back_url_structure` : pattern permalink WordPress (`/%postname%/` recommandé vs `?p=123`)
- `front_rendering_strategy` : SSR ou SSG obligatoire — les meta tags injectés par React côté client ne sont pas lus par les crawlers Google sans rendu serveur
