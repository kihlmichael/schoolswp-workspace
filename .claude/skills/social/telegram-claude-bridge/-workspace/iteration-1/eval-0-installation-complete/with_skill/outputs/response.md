# Guide complet — Piloter Claude Code depuis Telegram (Windows)

## Architecture

```
Telephone (Telegram) --> API Telegram (getUpdates) <-- Bridge Node.js (polling) --> claude -p (CLI)
```

Le bridge tourne sur ta machine en polling. Zero port expose, zero serveur externe.

## Prerequis

| Element | Version | Verification |
|---|---|---|
| Node.js | v18+ | `node --version` |
| npm | v9+ | `npm --version` |
| Claude Code CLI | Derniere | `claude --version` |

Test prealable :
```bash
claude -p "Dis bonjour" --max-turns 1
```

## Etape 1 — Creer le bot via @BotFather

1. Ouvrir Telegram, chercher **@BotFather**
2. Envoyer `/newbot`
3. Choisir un nom affiche (ex: `schoolsWP Claude`)
4. Choisir un username unique (ex: `schoolswp_claude_bot`)
5. Copier le token (format: `123456789:ABCdefGHI...`)

Ne jamais partager ce token.

## Etape 2 — Recuperer le Chat ID

1. Envoyer un message au bot
2. Ouvrir dans le navigateur : `https://api.telegram.org/bot<TON_TOKEN>/getUpdates`
3. Reperer `message.chat.id` (nombre comme `123456789`)

## Etape 3 — Creer le dossier projet

```powershell
mkdir $HOME\claude-telegram-bridge
cd $HOME\claude-telegram-bridge
npm init -y
npm install node-fetch@2
```

Note Windows : `node-fetch@2` car la v2 fonctionne en CommonJS (`require`).

## Etape 4 — Creer le fichier .env

```
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
ALLOWED_CHAT_ID=123456789
```

Attention Windows : pas d'espaces autour du `=`, pas de guillemets.

## Etape 5 — Copier le script bridge.js

Depuis PowerShell :
```powershell
Copy-Item "d:\VS Code\CLAUDE CODE\.claude\skills\telegram-claude-bridge\scripts\bridge.js" "$HOME\claude-telegram-bridge\bridge.js"
```

Le script gere : polling toutes les 3 secondes, filtrage par Chat ID, decoupe des messages longs (>4000 chars), commandes `/ping` et `/status`, timeout 2 min sur Claude Code.

## Etape 6 — Lancer le bridge

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

| Test | Action | Resultat attendu |
|---|---|---|
| Ping | `/ping` dans Telegram | "Bridge actif." |
| Status | `/status` | Uptime, offset, version Node |
| Question libre | "Quelle heure est-il ?" | Reponse de Claude |
| Securite | Message depuis un autre compte | Ignore dans les logs |

## Erreurs frequentes (Windows)

| Symptome | Correction |
|---|---|
| `claude: command not found` | Verifier avec `where.exe claude`. Ajouter au PATH si besoin. |
| Bridge ne recoit rien | Envoyer `/start` au bot, puis relancer |
| 401 Unauthorized | Verifier le token dans `.env` |
| Reponse tronquee | Deja gere par le script (chunks de 4000 chars) |

## Securite

- Filtrage par Chat ID (seul ton compte utilise le bot)
- Secrets dans `.env` (pas de token en dur)
- Polling (machine non exposee)
- Timeout sur Claude (pas de process zombie)
- Ajouter `.env` dans `.gitignore`

## Lancement automatique

**Option recommandee — pm2 :**
```bash
npm install -g pm2
pm2 start bridge.js --name claude-bridge
pm2 startup
pm2 save
```

**Alternative Windows — Tache planifiee :**
Creer une tache via `schtasks` ou le planificateur de taches pour lancer `node bridge.js` au demarrage.

## Feuille de route

- **Phase 1** (semaine 1-2) : logger fichier, pm2, commande `/help`
- **Phase 2** (semaine 3-4) : commandes predefinies (`/seo`, `/article`), contexte conversation
- **Phase 3** (mois 2+) : cwd pointe sur schoolsWP, integration MCP, templates de prompts
