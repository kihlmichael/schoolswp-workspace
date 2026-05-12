---
name: discord
description: |
  Pilote Discord via l'outil `discord` (bot token OpenClaw) : messages, réactions, stickers/emojis, sondages, threads, pins, recherche, création/modification/suppression de channels et catégories, permissions, infos membres/rôles, modération en DM ou channels.
  Utilise ce skill quand l'utilisateur dit : "envoie un message Discord sur le channel X", "réagis avec un emoji à ce message", "crée un sondage Discord", "modère ce channel", "récupère les permissions du serveur", ou demande une action concrète via le bot Discord.
  NE PAS utiliser pour : poster une notification automatique depuis n8n (utiliser un workflow n8n avec node Discord v2 webhook sendLegacy), publier un post de contenu communautaire planifié (utiliser `social-media-manager` ou l'agent `pulse`), ou tracer une routine claude.ai sur le webhook schoolsWP-Routines (voir `reference_discord_webhook_routines.md`).
metadata: {"openclaw":{"emoji":"🎮","requires":{"config":["channels.discord"]}}}
---

# Actions Discord

## Vue d'ensemble

Utilisez `discord` pour gérer les messages, réactions, threads, sondages et modération. Vous pouvez désactiver des groupes via `discord.actions.*` (activé par défaut, sauf roles/modération). L'outil utilise le bot token configuré pour OpenClaw.

## Informations à collecter

- Pour les réactions : `channelId`, `messageId`, et un `emoji`.
- Pour fetchMessage : `guildId`, `channelId`, `messageId`, ou un `messageLink` comme `https://discord.com/channels/<guildId>/<channelId>/<messageId>`.
- Pour stickers/sondages/sendMessage : une cible `to` (`channel:<id>` ou `user:<id>`). Texte `content` optionnel.
- Les sondages nécessitent aussi une `question` plus 2–10 `answers`.
- Pour les médias : `mediaUrl` avec `file:///chemin` pour fichiers locaux ou `https://...` pour distants.
- Pour upload d'emoji : `guildId`, `name`, `mediaUrl`, `roleIds` optionnel (limite 256KB, PNG/JPG/GIF).
- Pour upload de sticker : `guildId`, `name`, `description`, `tags`, `mediaUrl` (limite 512KB, PNG/APNG/Lottie JSON).

Les lignes de contexte de message incluent les champs `discord message id` et `channel` que vous pouvez réutiliser directement.

**Note :** `sendMessage` utilise le format `to: "channel:<id>"`, pas `channelId`. Les autres actions comme `react`, `readMessages`, `editMessage` utilisent `channelId` directement.
**Note :** `fetchMessage` accepte les IDs de message ou les liens complets comme `https://discord.com/channels/<guildId>/<channelId>/<messageId>`.

## Actions

### Réagir à un message

```json
{
  "action": "react",
  "channelId": "123",
  "messageId": "456",
  "emoji": "✅"
}
```

### Lister les réactions + utilisateurs

```json
{
  "action": "reactions",
  "channelId": "123",
  "messageId": "456",
  "limit": 100
}
```

### Envoyer un sticker

```json
{
  "action": "sticker",
  "to": "channel:123",
  "stickerIds": ["9876543210"],
  "content": "Bien joué !"
}
```

- Jusqu'à 3 IDs de sticker par message.
- `to` peut être `user:<id>` pour les DMs.

### Upload d'un emoji personnalisé

```json
{
  "action": "emojiUpload",
  "guildId": "999",
  "name": "party_blob",
  "mediaUrl": "file:///tmp/party.png",
  "roleIds": ["222"]
}
```

- Les images d'emoji doivent être PNG/JPG/GIF et <= 256KB.
- `roleIds` est optionnel ; omettre pour rendre l'emoji disponible à tous.

### Upload d'un sticker

```json
{
  "action": "stickerUpload",
  "guildId": "999",
  "name": "openclaw_wave",
  "description": "OpenClaw qui fait coucou",
  "tags": "👋",
  "mediaUrl": "file:///tmp/wave.png"
}
```

- Les stickers nécessitent `name`, `description`, et `tags`.
- Les uploads doivent être PNG/APNG/Lottie JSON et <= 512KB.

### Créer un sondage

```json
{
  "action": "poll",
  "to": "channel:123",
  "question": "Déjeuner ?",
  "answers": ["Pizza", "Sushi", "Salade"],
  "allowMultiselect": false,
  "durationHours": 24,
  "content": "Votez maintenant"
}
```

- `durationHours` par défaut 24 ; max 32 jours (768 heures).

### Vérifier les permissions du bot pour un channel

```json
{
  "action": "permissions",
  "channelId": "123"
}
```

## Idées à essayer

- Réagir avec ✅/⚠️ pour marquer les mises à jour de statut.
- Poster un sondage rapide pour les décisions de release ou horaires de réunion.
- Envoyer des stickers de célébration après des déploiements réussis.
- Upload de nouveaux emojis/stickers pour les moments de release.
- Lancer des sondages hebdomadaires "vérification des priorités" dans les channels d'équipe.
- DM des stickers comme accusés de réception quand une demande utilisateur est terminée.

## Contrôle des actions

Utilisez `discord.actions.*` pour désactiver des groupes d'actions :
- `reactions` (react + liste réactions + emojiList)
- `stickers`, `polls`, `permissions`, `messages`, `threads`, `pins`, `search`
- `emojiUploads`, `stickerUploads`
- `memberInfo`, `roleInfo`, `channelInfo`, `voiceStatus`, `events`
- `roles` (ajout/suppression de rôle, défaut `false`)
- `channels` (création/édition/suppression/déplacement de channel/catégorie, défaut `false`)
- `moderation` (timeout/kick/ban, défaut `false`)

### Lire les messages récents

```json
{
  "action": "readMessages",
  "channelId": "123",
  "limit": 20
}
```

### Récupérer un message unique

```json
{
  "action": "fetchMessage",
  "guildId": "999",
  "channelId": "123",
  "messageId": "456"
}
```

```json
{
  "action": "fetchMessage",
  "messageLink": "https://discord.com/channels/999/123/456"
}
```

### Envoyer/modifier/supprimer un message

```json
{
  "action": "sendMessage",
  "to": "channel:123",
  "content": "Bonjour depuis OpenClaw"
}
```

**Avec pièce jointe média :**

```json
{
  "action": "sendMessage",
  "to": "channel:123",
  "content": "Écoutez cet audio !",
  "mediaUrl": "file:///tmp/audio.mp3"
}
```

- `to` utilise le format `channel:<id>` ou `user:<id>` pour les DMs (pas `channelId` !)
- `mediaUrl` supporte les fichiers locaux (`file:///chemin/vers/fichier`) et URLs distantes (`https://...`)
- `replyTo` optionnel avec un ID de message pour répondre à un message spécifique

```json
{
  "action": "editMessage",
  "channelId": "123",
  "messageId": "456",
  "content": "Typo corrigée"
}
```

```json
{
  "action": "deleteMessage",
  "channelId": "123",
  "messageId": "456"
}
```

### Threads

```json
{
  "action": "threadCreate",
  "channelId": "123",
  "name": "Triage des bugs",
  "messageId": "456"
}
```

```json
{
  "action": "threadList",
  "guildId": "999"
}
```

```json
{
  "action": "threadReply",
  "channelId": "777",
  "content": "Réponse dans le thread"
}
```

### Pins

```json
{
  "action": "pinMessage",
  "channelId": "123",
  "messageId": "456"
}
```

```json
{
  "action": "listPins",
  "channelId": "123"
}
```

### Rechercher des messages

```json
{
  "action": "searchMessages",
  "guildId": "999",
  "content": "notes de release",
  "channelIds": ["123", "456"],
  "limit": 10
}
```

### Info membre + rôle

```json
{
  "action": "memberInfo",
  "guildId": "999",
  "userId": "111"
}
```

```json
{
  "action": "roleInfo",
  "guildId": "999"
}
```

### Lister les emojis personnalisés disponibles

```json
{
  "action": "emojiList",
  "guildId": "999"
}
```

### Changements de rôle (désactivé par défaut)

```json
{
  "action": "roleAdd",
  "guildId": "999",
  "userId": "111",
  "roleId": "222"
}
```

### Info channel

```json
{
  "action": "channelInfo",
  "channelId": "123"
}
```

```json
{
  "action": "channelList",
  "guildId": "999"
}
```

### Gestion des channels (désactivé par défaut)

Créer, modifier, supprimer et déplacer des channels et catégories. Activer via `discord.actions.channels: true`.

**Créer un channel texte :**

```json
{
  "action": "channelCreate",
  "guildId": "999",
  "name": "discussion-generale",
  "type": 0,
  "parentId": "888",
  "topic": "Discussion générale"
}
```

- `type` : entier type de channel Discord (0 = texte, 2 = vocal, 4 = catégorie ; autres valeurs supportées)
- `parentId` : ID de catégorie pour nicher dessous (optionnel)
- `topic`, `position`, `nsfw` : optionnels

**Créer une catégorie :**

```json
{
  "action": "categoryCreate",
  "guildId": "999",
  "name": "Projets"
}
```

**Modifier un channel :**

```json
{
  "action": "channelEdit",
  "channelId": "123",
  "name": "nouveau-nom",
  "topic": "Sujet mis à jour"
}
```

- Supporte `name`, `topic`, `position`, `parentId` (null pour retirer de la catégorie), `nsfw`, `rateLimitPerUser`

**Déplacer un channel :**

```json
{
  "action": "channelMove",
  "guildId": "999",
  "channelId": "123",
  "parentId": "888",
  "position": 2
}
```

- `parentId` : catégorie cible (null pour déplacer au niveau racine)

**Supprimer un channel :**

```json
{
  "action": "channelDelete",
  "channelId": "123"
}
```

**Modifier/supprimer une catégorie :**

```json
{
  "action": "categoryEdit",
  "categoryId": "888",
  "name": "Catégorie Renommée"
}
```

```json
{
  "action": "categoryDelete",
  "categoryId": "888"
}
```

### Statut vocal

```json
{
  "action": "voiceStatus",
  "guildId": "999",
  "userId": "111"
}
```

### Événements programmés

```json
{
  "action": "eventList",
  "guildId": "999"
}
```

### Modération (désactivé par défaut)

```json
{
  "action": "timeout",
  "guildId": "999",
  "userId": "111",
  "durationMinutes": 10
}
```

## Guide de style d'écriture Discord

**Restez conversationnel !** Discord est une plateforme de chat, pas de documentation.

### À faire
- Messages courts et percutants (1-3 phrases idéal)
- Plusieurs réponses rapides > un mur de texte
- Utiliser les emoji pour le ton/l'emphase 🦞
- Style décontracté en minuscules acceptable
- Découper l'info en morceaux digestes
- S'adapter à l'énergie de la conversation

### À éviter
- Pas de tableaux markdown (Discord les affiche en texte brut `| texte |`)
- Pas de `## Headers` pour le chat décontracté (utiliser **gras** ou MAJUSCULES pour l'emphase)
- Éviter les essais multi-paragraphes
- Ne pas sur-expliquer les choses simples
- Sauter le "Je serais ravi de vous aider !" superflu

### Formatage qui fonctionne
- **gras** pour l'emphase
- `code` pour les termes techniques
- Listes pour les éléments multiples
- > citations pour référencer
- Entourer les liens multiples de `<>` pour supprimer les previews

### Exemples de transformation

❌ Mauvais :
```
Je serais ravi de vous aider ! Voici un aperçu complet des stratégies de versioning disponibles :

## Versioning Sémantique
Semver utilise le format MAJOR.MINOR.PATCH où...

## Versioning Calendaire
CalVer utilise des versions basées sur la date comme...
```

✅ Bon :
```
options de versioning : semver (1.2.3), calver (2026.01.04), ou yolo (`latest` pour toujours). qu'est-ce qui correspond à ta cadence de release ?
```
