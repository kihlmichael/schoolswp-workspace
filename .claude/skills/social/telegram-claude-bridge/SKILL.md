---
name: telegram-claude-bridge
description: |
  Tutoriel pas-a-pas pour construire un bridge Node.js entre Telegram et Claude Code CLI. Utilise
  ce skill des qu'un utilisateur veut piloter Claude Code a distance depuis Telegram ou un telephone
  — que ce soit créer un bot BotFather, récupérer un Chat ID, ecrire un script de polling qui appelle
  `claude -p`, ou configurer un relais bot-vers-CLI local. Couvre aussi le lancement automatique (pm2),
  la sécurité (filtrage Chat ID), et les commandes predefinies. Ce skill concerne la CONSTRUCTION d'une
  infrastructure de pont, PAS l'utilisation du plugin MCP Telegram existant. Ne pas utiliser pour les
  noeuds Telegram n8n, les erreurs MCP Telegram, les bots de groupe generiques, le monitoring par
  alertes Telegram, ou les appels API Anthropic directs.
---

# Telegram-Claude-Bridge

Bridge local Node.js qui relie un bot Telegram a Claude Code CLI. L'utilisateur envoie un message
depuis son telephone, le script recupere le message en polling, le passe a `claude -p`, et renvoie
la reponse dans Telegram. Zero serveur externe, zero webhook, zero port expose.

## Architecture

```
Telephone (Telegram) --> API Telegram (getUpdates) <-- Bridge Node.js (polling) --> Claude Code CLI
```

4 briques :

| Brique | Role | Localisation |
|---|---|---|
| Bot Telegram | Interface de commande mobile | Cloud Telegram (gratuit) |
| API Telegram (getUpdates) | File d'attente de messages | Cloud Telegram |
| Bridge Node.js | Recupere les messages, lance Claude, renvoie la reponse | Machine locale |
| Claude Code CLI | Execute les taches IA | Machine locale |

Avantages : pas de serveur a payer, pas de webhook a exposer, fonctionne derriere NAT/VPN,
controle total, arret simple (couper le script).

## Prerequis

### Machine locale

| Element | Version min | Verification |
|---|---|---|
| Node.js | v18+ | `node --version` |
| npm | v9+ | `npm --version` |
| Claude Code CLI | Derniere | `claude --version` |
| Connexion internet | Stable | `ping api.telegram.org` |

### Comptes et tokens

| Element | Comment l'obtenir |
|---|---|
| Compte Telegram | App Telegram sur telephone |
| Bot Token | Cree via @BotFather (gratuit) |
| Chat ID personnel | Via @userinfobot ou API du bot |
| Cle API Anthropic | Deja configuree dans Claude Code |

Temps estime : ~25 minutes pour un MVP fonctionnel.

## Installation pas a pas

### Etape 1 — Creer le bot Telegram

1. Ouvrir Telegram, chercher **@BotFather**
2. Envoyer `/newbot`
3. Choisir un nom affiche (ex: `schoolsWP Claude`)
4. Choisir un username unique (ex: `schoolswp_claude_bot`)
5. Copier le token fourni (format: `123456789:ABCdefGHI...`)

Ne jamais partager ce token.

### Etape 2 — Recuperer le Chat ID

1. Envoyer un message quelconque au nouveau bot
2. Ouvrir dans un navigateur : `https://api.telegram.org/bot<TON_TOKEN>/getUpdates`
3. Reperer `message.chat.id` dans la reponse JSON (nombre comme `123456789`)
4. Le noter

### Etape 3 — Creer le dossier projet

```bash
mkdir ~/claude-telegram-bridge
cd ~/claude-telegram-bridge
npm init -y
npm install node-fetch@2
```

node-fetch@2 car la v2 fonctionne en CommonJS (`require`). La v3 exige ESM.

### Etape 4 — Creer le fichier .env

```bash
# ~/claude-telegram-bridge/.env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
ALLOWED_CHAT_ID=123456789
```

Ajouter `.env` dans `.gitignore` si le projet est versionne.

### Etape 5 — Copier le script bridge

Copier le fichier `scripts/bridge.js` fourni avec ce skill dans le dossier projet,
ou le generer avec la commande :

```bash
cp <chemin-du-skill>/scripts/bridge.js ~/claude-telegram-bridge/bridge.js
```

Le script fait ~90 lignes et gere : polling, filtrage Chat ID, decoupe messages longs,
commandes `/ping` et `/status`, timeout 2 min sur Claude Code.

### Etape 6 — Lancer le bridge

```bash
cd ~/claude-telegram-bridge
node bridge.js
```

Sortie attendue :
```
[BRIDGE] Demarre. En attente de messages...
[BRIDGE] Chat ID autorise : 123456789
```

## Tests de validation

| Test | Commande / Action | Resultat attendu |
|---|---|---|
| Bridge demarre | `node bridge.js` | Message "Demarre" dans le terminal |
| Ping | `/ping` dans Telegram | "Bridge actif." |
| Status | `/status` dans Telegram | Uptime, offset, version Node |
| Claude repond | Question simple dans Telegram | Reponse IA |
| Securite | Message depuis un autre compte | Ignore dans les logs |
| Timeout | Requete tres longue | Erreur propre apres 2 min |

Test prealable CLI (sans Telegram) :
```bash
claude -p "Dis bonjour en une phrase" --max-turns 1
```

## Erreurs frequentes

| Symptome | Cause | Correction |
|---|---|---|
| Bridge ne recoit rien | Pas de message envoye au bot avant le lancement | Envoyer `/start`, relancer |
| 401 Unauthorized | Token invalide ou mal copie | Verifier `.env` (pas d'espace) |
| `claude: command not found` | CLI pas dans le PATH | `which claude`, ajouter au `.bashrc` |
| Reponse tronquee | Message > 4096 chars | Le script decoupe deja (verifier `MAX_MSG_LENGTH`) |
| Timeout 2 min | Requete trop lourde | Simplifier la demande ou augmenter le timeout |
| Bot repond en double | Deux instances tournent | `ps aux | grep bridge.js`, tuer les doublons |
| Erreur Markdown Telegram | Caracteres speciaux dans la reponse | Supprimer `parse_mode: 'Markdown'` |

## Securite

### Inclus dans le MVP

- Filtrage par Chat ID (seul le proprietaire peut utiliser le bot)
- Secrets dans `.env` (pas de token en dur)
- Polling (machine non exposee sur internet)
- Timeout sur Claude Code (pas de process zombie)

### Recommandations supplementaires

1. **Filtrer les prompts dangereux** : bloquer les mots-cles sensibles (`rm -rf`, `sudo`)
2. **Logger les requetes** : fichier log avec date + prompt + reponse
3. **Limiter le repertoire de travail** : fixer `cwd` sur un dossier specifique dans `runClaude()`
4. **Ne jamais versionner `.env`**

### Ce que le bridge ne fait PAS

- N'execute pas de commandes shell directement (tout passe par Claude Code)
- Ne stocke rien en base
- N'expose aucun port reseau
- Ne tourne que quand lance manuellement

## Feuille de route

### Phase 1 — Stabilisation (semaine 1-2)

| Action | Detail |
|---|---|
| Logger fichier | Chaque requete + reponse avec timestamp |
| Lancement auto | pm2 start bridge.js (ou systemd) |
| Markdown robuste | Desactiver `parse_mode` si caracteres problematiques |
| Commande `/help` | Lister les commandes disponibles |

### Phase 2 — Fonctionnalites avancees (semaine 3-4)

| Action | Detail |
|---|---|
| Contexte conversation | Garder les N derniers echanges en memoire |
| Commandes predefinies | `/seo`, `/article`, `/check` → prompts preconfigures |
| Envoi de fichiers | Recevoir un fichier via Telegram, le passer a Claude |
| Mode silencieux | `/mute` pour desactiver les confirmations |

### Phase 3 — Integration schoolsWP (mois 2+)

| Action | Detail |
|---|---|
| Repertoire schoolsWP | Pointer Claude sur le dossier projet |
| Integration MCP | Google Drive, Notion via MCP |
| Templates de prompts | `/prompt [nom]` → bibliotheque de prompts |
| Multi-sessions | Plusieurs sessions Claude Code en parallele |

### pm2 vs systemd

| Critere | pm2 | systemd |
|---|---|---|
| Installation | `npm install -g pm2` | Deja present sur Linux |
| Lancement | `pm2 start bridge.js` | `systemctl start claude-bridge` |
| Restart auto | `pm2 startup` + `pm2 save` | `Restart=on-failure` |
| Recommande | Oui (plus simple) | Si controle total voulu |
