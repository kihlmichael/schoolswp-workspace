---
name: slack
description: Utiliser pour contrôler Slack via l'outil slack - réagir aux messages, épingler/désépingler des éléments, envoyer/modifier/supprimer des messages dans les channels ou DMs Slack.
metadata: {"openclaw":{"emoji":"💬","requires":{"config":["channels.slack"]}}}
---

# Actions Slack

## Vue d'ensemble

Utilisez `slack` pour réagir, gérer les pins, envoyer/modifier/supprimer des messages, et récupérer les infos membres. L'outil utilise le bot token configuré pour OpenClaw.

## Informations à collecter

- `channelId` et `messageId` (timestamp de message Slack, ex. `1712023032.1234`).
- Pour les réactions, un `emoji` (Unicode ou `:name:`).
- Pour l'envoi de messages, une cible `to` (`channel:<id>` ou `user:<id>`) et `content`.

Les lignes de contexte de message incluent les champs `slack message id` et `channel` que vous pouvez réutiliser directement.

## Actions

### Groupes d'actions

| Groupe d'action | Défaut | Notes |
| --- | --- | --- |
| reactions | activé | Réagir + lister réactions |
| messages | activé | Lire/envoyer/modifier/supprimer |
| pins | activé | Épingler/désépingler/lister |
| memberInfo | activé | Info membre |
| emojiList | activé | Liste des emojis personnalisés |

### Réagir à un message

```json
{
  "action": "react",
  "channelId": "C123",
  "messageId": "1712023032.1234",
  "emoji": "✅"
}
```

### Lister les réactions

```json
{
  "action": "reactions",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### Envoyer un message

```json
{
  "action": "sendMessage",
  "to": "channel:C123",
  "content": "Bonjour depuis OpenClaw"
}
```

### Modifier un message

```json
{
  "action": "editMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234",
  "content": "Texte mis à jour"
}
```

### Supprimer un message

```json
{
  "action": "deleteMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### Lire les messages récents

```json
{
  "action": "readMessages",
  "channelId": "C123",
  "limit": 20
}
```

### Épingler un message

```json
{
  "action": "pinMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### Désépingler un message

```json
{
  "action": "unpinMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### Lister les éléments épinglés

```json
{
  "action": "listPins",
  "channelId": "C123"
}
```

### Info membre

```json
{
  "action": "memberInfo",
  "userId": "U123"
}
```

### Liste des emojis

```json
{
  "action": "emojiList"
}
```

## Idées à essayer

- Réagir avec ✅ pour marquer les tâches terminées.
- Épingler les décisions clés ou les mises à jour de statut hebdomadaires.
