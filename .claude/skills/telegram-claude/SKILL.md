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
