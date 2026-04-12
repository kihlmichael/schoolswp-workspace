# WordPress REST API — Intégration n8n schoolsWP

Guide pratique pour brancher WordPress dans les workflows n8n.

---

## Setup WordPress

### Créer l'utilisateur API

1. WordPress Admin → Utilisateurs → Ajouter
2. Nom : `seo-agent`
3. Rôle : **Éditeur** (suffisant pour créer/modifier des brouillons)
4. Profil → Application Passwords → générer un mot de passe

### Configurer la credential n8n

- Type : **Basic Auth**
- Username : `seo-agent`
- Password : le mot de passe d'application généré (avec espaces ou sans, les deux marchent)

---

## Endpoints utilisés

### GET — Récupérer un post par slug

```
Method : GET
URL    : https://schoolswp.com/wp-json/wp/v2/posts?slug={{$json.slug}}
Auth   : Basic Auth (seo-agent)
```

Retourne un tableau. Accéder au premier élément :

```javascript
// Dans un Code node après le GET
const post = Array.isArray(items[0].json) ? items[0].json[0] : items[0].json;
const wp_id = post?.id || "";
const title = post?.title?.rendered || "";
const content = post?.content?.rendered || "";
```

### POST — Créer un brouillon

```
Method : POST
URL    : https://schoolswp.com/wp-json/wp/v2/posts
Auth   : Basic Auth (seo-agent)
Headers : Content-Type: application/json

Body JSON :
{
  "title"   : "={{ $json.draft_title }}",
  "status"  : "draft",
  "content" : "={{ $json.draft_content }}"
}
```

Retourne le post créé. Récupérer l'URL admin pour le Google Sheet :

```
={{ 'https://schoolswp.com/wp-admin/post.php?post=' + $json.id + '&action=edit' }}
```

### POST — Mettre à jour un post existant

```
Method : POST
URL    : https://schoolswp.com/wp-json/wp/v2/posts/{{ $json.wp_id }}
Auth   : Basic Auth (seo-agent)

Body JSON :
{
  "title"   : "={{ $json.new_title }}",
  "content" : "={{ $json.new_content }}"
}
```

### POST — Publier un brouillon existant

```
Body JSON :
{
  "status" : "publish"
}
```

---

## Expressions n8n utiles

### Construire l'URL admin après création

```
={{ 'https://schoolswp.com/wp-admin/post.php?post=' + $json.id + '&action=edit' }}
```

### Récupérer le slug depuis une URL

```javascript
// Code node
const url = item.json.url || "";
const clean = url.replace(/^https?:\/\/[^/]+/, "").replace(/^\/|\/$/g, "");
const parts = clean.split("/");
item.json.slug = parts[parts.length - 1] || "";
```

### Nettoyer le HTML d'un post récupéré

```javascript
// Code node — nettoyer le content.rendered
const content = post?.content?.rendered || "";
const clean = content
  .replace(/<[^>]*>/g, " ")
  .replace(/\s+/g, " ")
  .trim()
  .slice(0, 12000);
```

---

## Codes d'erreur courants

| Code | Cause probable                                  | Solution                              |
| ---- | ----------------------------------------------- | ------------------------------------- |
| 401  | Bad credentials (username ou password faux)     | Vérifier l'Application Password       |
| 403  | Droits insuffisants (rôle trop bas)             | Passer le rôle à Éditeur              |
| 404  | Mauvais endpoint (ex: /pages au lieu de /posts) | Vérifier le type de contenu WP        |
| 400  | Body JSON mal formé ou champ inconnu            | Vérifier les guillemets et la syntaxe |

---

## Flux complet — Patch SEO (Workflow 02)

```
Read seo_pages (P1, status=detected)
  → Extract slug (Code)
  → GET WP post by slug (httpRequest)
  → Clean HTML (Code)
  → OpenAI résumé
  → OpenAI patch SEO (JSON: patch_title, patch_meta, faq)
  → Parse JSON (Code)
  → OpenAI draft HTML
  → POST /wp-json/wp/v2/posts  [status=draft]
  → Update seo_pages (draft_url + status=drafted)
```

### Mapping Google Sheets après POST

Dans le node Update seo_pages, les champs à écrire :

```
draft_url       : ={{ 'https://schoolswp.com/wp-admin/post.php?post=' + $json.id + '&action=edit' }}
patch_title     : ={{ $('Parse JSON').item.json.patch_title }}
patch_meta      : ={{ $('Parse JSON').item.json.patch_meta }}
status          : drafted
```

---

## Flux complet — Nouvel article (Workflow 04)

```
Read topic_ideas (status=selected)
  → OpenAI brief SEO (JSON: angle, promise, h2_h3, faq, cta)
  → Parse JSON (Code)
  → OpenAI draft HTML complet
  → POST /wp-json/wp/v2/posts  [status=draft]
  → Update topic_ideas (draft_url + status=drafted)
```

### Body POST à copier dans n8n

```json
{
  "title": "={{ $json.working_title }}",
  "status": "draft",
  "content": "={{ $json.text }}"
}
```

Note : `$json.text` est la sortie du node OpenAI v1.8 (champ `message.content` ou `text` selon le Parse node en amont).

---

## Block minimal à copier dans n8n

**Credential** : type "HTTP Basic Auth", nom `WordPress schoolsWP`, user `seo-agent`, password = Application Password WP.

**Node HTTP Request — Create WordPress Draft**

```
Method            : POST
URL               : https://schoolswp.com/wp-json/wp/v2/posts
Authentication    : Basic Auth → WordPress schoolsWP
Send Body         : true
Body Content Type : JSON
Specify Body      : Using JSON
```

Body JSON :

```json
{
  "title": "={{$json.draft_title}}",
  "status": "draft",
  "content": "={{$json.draft_content}}"
}
```

> Si le draft apparaît vide dans WordPress : vérifier que `draft_content` est bien généré par le node précédent et que les expressions commencent par `={{...}}`.

**Test minimal (body fixe, sans variables) :**

```json
{
  "title": "Test draft schoolsWP",
  "status": "draft",
  "content": "<p>Test simple depuis n8n.</p>"
}
```

Si ça passe → auth OK → tu peux passer aux variables dynamiques.

---

## Node suivant — Set Admin URL

```
draft_wp_id  : ={{$json.id}}
draft_url    : =https://schoolswp.com/wp-admin/post.php?post={{$json.id}}&action=edit
draft_status : ={{$json.status}}
```

---

## Node GET — Lire un article par slug

```
Name   : Get WordPress Post By Slug
Method : GET
URL    : =https://schoolswp.com/wp-json/wp/v2/posts?slug={{$json.slug}}
Auth   : Basic Auth → WordPress schoolsWP
```

Pour une page (pas un article) : remplacer `/posts` par `/pages`.

---

## Erreurs fréquentes

| Code       | Cause                                           | Fix                               |
| ---------- | ----------------------------------------------- | --------------------------------- |
| 401        | Mauvais identifiant ou Application Password     | Vérifier la credential Basic Auth |
| 403        | Compte WP sans droits suffisants                | Passer le rôle à Éditeur          |
| Draft vide | `draft_content` non généré ou expression cassée | Vérifier le node Set précédent    |
