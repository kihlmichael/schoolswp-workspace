# Blotato API Reference

Reference technique pour le skill social-media-manager. Base URL : `https://backend.blotato.com/v2`

Auth : header `blotato-api-key: <KEY>` sur chaque requete. La cle est dans `.env` (`BLOTATO_API_KEY`).

Rate limit global : 30 req/min (publish, visuals, upload). 60 req/min (get status).

---

## Table des matieres

- [Comptes connectes](#comptes-connectes)
- [Sous-comptes (Pages)](#sous-comptes-pages)
- [Publier un post](#publier-un-post)
- [Statut de publication](#statut-de-publication)
- [Upload media](#upload-media)
- [Creer un visuel](#creer-un-visuel)
- [Statut du visuel](#statut-du-visuel)
- [Templates visuels](#templates-visuels)
- [IDs par plateforme](#ids-par-plateforme)

---

## Comptes connectes

```
GET /users/me/accounts
GET /users/me/accounts?platform=linkedin
```

Reponse :
```json
{
  "items": [
    { "id": "98432", "platform": "twitter", "fullname": "...", "username": "..." }
  ]
}
```

Utilise `items[].id` comme `accountId` dans les requetes de publication.

---

## Sous-comptes (Pages)

Necessaire pour Facebook (obligatoire) et LinkedIn (si Company Page).

```
GET /users/me/accounts/:accountId/subaccounts
```

Reponse :
```json
{
  "items": [
    { "id": "123456789", "accountId": "98433", "name": "My Business Page" }
  ]
}
```

Utilise `items[].id` comme `target.pageId`.

---

## Publier un post

```
POST /posts
```

### Structure complete

```json
{
  "post": {
    "accountId": "ACCOUNT_ID",
    "content": {
      "text": "Le texte du post",
      "mediaUrls": ["https://..."],
      "platform": "linkedin",
      "additionalPosts": []
    },
    "target": {
      "targetType": "linkedin"
    }
  },
  "scheduledTime": "2026-04-10T09:00:00+02:00",
  "useNextFreeSlot": false
}
```

### Regles critiques

- `content.platform` et `target.targetType` doivent etre identiques
- `scheduledTime` et `useNextFreeSlot` sont au **niveau racine** (pas dans `post`)
- Sans `scheduledTime` ni `useNextFreeSlot` : publication immediate
- `mediaUrls` : tableau vide `[]` pour text-only, URLs publiques directes sinon
- `additionalPosts` : threads (Twitter, Bluesky, Threads uniquement)

### Champs target par plateforme

| Plateforme | targetType | Requis | Optionnel |
|---|---|---|---|
| Twitter | `twitter` | — | — |
| LinkedIn | `linkedin` | — | `pageId` (Company Page) |
| Facebook | `facebook` | `pageId` | `mediaType`, `link` |
| Instagram | `instagram` | — | `mediaType` (`reel`/`story`), `altText`, `collaborators`, `coverImageUrl` |

### Reponse

```json
{ "postSubmissionId": "uuid-here" }
```

---

## Statut de publication

```
GET /posts/:postSubmissionId
```

| Statut | Action |
|---|---|
| `in-progress` | Continuer le polling (toutes les 2s) |
| `published` | Termine. `publicUrl` disponible |
| `failed` | Arret. `errorMessage` disponible |

Reponse succes :
```json
{
  "postSubmissionId": "...",
  "status": "published",
  "publicUrl": "https://x.com/user/status/123456"
}
```

---

## Upload media

### Option 1 : URL publique directe (recommande)

Passer l'URL directement dans `mediaUrls` — pas besoin d'upload prealable.

### Option 2 : Upload via URL

```
POST /media
```
```json
{ "url": "https://example.com/image.jpg" }
```
Reponse : `{ "url": "https://database.blotato.com/..." }`

### Option 3 : Upload fichier local (presigned)

```
POST /media/uploads
```
```json
{ "filename": "photo.jpg" }
```
Reponse :
```json
{
  "presignedUrl": "https://...",
  "publicUrl": "https://..."
}
```
Puis `PUT presignedUrl` avec le fichier. Max 1 GB.

---

## Creer un visuel

```
POST /videos/from-templates
```

```json
{
  "templateId": "TEMPLATE_ID",
  "inputs": {},
  "prompt": "Description en langage naturel du visuel souhaite",
  "render": true
}
```

- `prompt` : l'IA remplit les inputs automatiquement (recommande)
- `inputs` manuels prennent priorite sur le prompt IA
- Combinaison possible : prompt + overrides manuels

Reponse : `{ "item": { "id": "VIDEO_ID", "status": "queueing" } }`

---

## Statut du visuel

```
GET /videos/creations/:id
```

Statuts (dans l'ordre) : `queueing` -> `generating-script` -> `script-ready` -> `generating-media` -> `media-ready` -> `exporting` -> `done` | `creation-from-template-failed`

Polling : toutes les 5 secondes.

Reponse `done` :
```json
{
  "item": {
    "id": "...",
    "status": "done",
    "mediaUrl": "https://...video.mp4",
    "imageUrls": ["https://...slide1.jpg", "https://...slide2.jpg"]
  }
}
```

- `mediaUrl` : pour les videos
- `imageUrls` : pour les carousels/slideshows
- Utiliser ces URLs dans `mediaUrls` lors de la publication

---

## Templates visuels

```
GET /videos/templates?fields=id,name,description,inputs
GET /videos/templates?search=carousel
GET /videos/templates?id=SPECIFIC_ID
```

Types courants : Image Slideshow, Quote Card, Tweet Card, Tutorial Carousel, AI Story Video, Combine Clips.

Types d'inputs : `text`, `number`, `boolean`, `enum`, `image`, `video`, `color`, `array`, `object`.

---

## IDs par plateforme

| Plateforme | Besoin | Comment obtenir |
|---|---|---|
| Twitter, Instagram, Bluesky | `accountId` seulement | `GET /users/me/accounts?platform=X` |
| LinkedIn (profil) | `accountId` seulement | `GET /users/me/accounts?platform=linkedin` |
| LinkedIn (Company Page) | `accountId` + `pageId` | + `GET /users/me/accounts/:id/subaccounts` |
| Facebook | `accountId` + `pageId` (obligatoire) | + `GET /users/me/accounts/:id/subaccounts` |
| Pinterest | `accountId` + `boardId` | boardId via Blotato UI uniquement |
