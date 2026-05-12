---
name: telegram-claude
description: |
  Référence opérationnelle de l'orchestrateur Telegram <-> Claude pour schoolsWP : serveur Express (`agents/telegram-claude/server.js`) qui route 4 bots Telegram (Studio creation contenu, Radar veille/recherche, Flow automatisation OttoKit/FluentCRM/n8n, Pulse analytics) vers l'API Anthropic avec system prompts dedies. Couvre l'ajout d'un nouveau bot, la modification d'un agent existant, le debug de webhook, la gestion de l'historique de conversation, l'enregistrement des webhooks via ngrok.
  Utilise ce skill quand l'utilisateur dit : "modifier l'agent Studio/Radar/Flow/Pulse", "ajouter un agent Telegram", "nouveau bot Telegram schoolsWP", "debug webhook telegram", "register-webhooks", "system prompt agent telegram", "BOT_TOKENS server.js", "ngrok telegram", ou demande de toucher au code de `agents/telegram-claude/`.
  NE PAS utiliser pour : configurer le canal Telegram personnel de Michael (utiliser `telegram:configure` + `telegram:access`), gerer les bots Telegram non-Claude de l'ecosysteme (welcome bot, notif bot — voir `reference_bots_messaging_sheet.md`), créer une automation n8n qui poste sur Telegram (utiliser `flow` agent), ou rediger du contenu pour Telegram (utiliser le skill plateforme adapte).
---

# SKILL : Telegram -> Claude Orchestrateur schoolsWP

## Quand utiliser ce skill
- Modifier un agent Telegram (Studio, Radar, Flow, Pulse)
- Ajouter un nouvel agent
- Déboguer un webhook
- Gérer l'historique de conversation

## Structure
agents/telegram-claude/
├── server.js              <- Serveur Express + logique agents
├── register-webhooks.js   <- Enregistrement webhooks Telegram
├── package.json
└── .env.example

## Commandes utiles
```bash
# Installation
cd agents/telegram-claude && npm install

# Dev local
npm run dev

# Exposer via ngrok
ngrok http 3000

# Enregistrer les webhooks
node register-webhooks.js https://TA_URL
```

## Agents actifs
| Agent | Route | Rôle |
|---|---|---|
| Studio | /webhook/studio | Création de contenu schoolsWP |
| Radar | /webhook/radar | Veille et recherche |
| Flow | /webhook/flow | Automatisation OttoKit / FluentCRM / n8n |
| Pulse | /webhook/pulse | Analytics et reporting |

## Ajouter un agent
1. Ajouter token dans .env
2. Ajouter dans BOT_TOKENS dans server.js
3. Ajouter system prompt dans SYSTEM_PROMPTS
4. Ajouter route app.post(...)
5. Relancer register-webhooks.js

## Variables d'environnement requises
- ANTHROPIC_API_KEY
- TELEGRAM_TOKEN_STUDIO
- TELEGRAM_TOKEN_RADAR
- TELEGRAM_TOKEN_FLOW
- TELEGRAM_TOKEN_PULSE
- PORT (défaut 3000)
