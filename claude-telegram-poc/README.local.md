# Bot Telegram ↔ Claude Code (PoC Local)

Proof of Concept pour piloter Claude Code via Telegram.

## Architecture

```
Telegram App → Bot Telegram (polling) → bot.py → Claude Code CLI
                    ↑                        ↓
                    └────── Réponse ←────────┘
```

**Sécurité :**
- Mode polling (pas de webhook = pas d'exposition réseau entrante)
- Allowlist d'utilisateurs par user_id Telegram
- Pas de secrets en dur dans le code

---

## Prérequis

| Composant | Vérification |
|-----------|--------------|
| Python 3.10+ | `python --version` |
| Claude Code CLI | `claude --version` |
| Compte Telegram | App installée |

---

## Installation

### 1. Créer l'environnement virtuel

```bash
cd claude-telegram-poc

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configurer le fichier .env

```bash
# Copier le template
cp .env.example .env

# Éditer avec vos valeurs
notepad .env  # Windows
# ou
nano .env     # Linux/Mac
```

**Valeurs à remplir :**

| Variable | Description | Comment l'obtenir |
|----------|-------------|-------------------|
| `TELEGRAM_BOT_TOKEN` | Token du bot | @BotFather sur Telegram → /newbot |
| `ALLOWED_USERS` | Votre user ID | @userinfobot sur Telegram |

**Exemple de .env :**
```env
TELEGRAM_BOT_TOKEN=7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ALLOWED_USERS=123456789
LOG_LEVEL=INFO
```

---

## Lancement

### Mode développement

```bash
# Activer l'environnement
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Lancer le bot
python bot.py
```

### Mode dry-run (test sans appeler Claude)

```bash
# Dans .env, ajouter :
DRY_RUN=true

# Puis lancer normalement
python bot.py
```

### Arrêter le bot

Appuyez sur `Ctrl+C` dans le terminal.

---

## Commandes Telegram

| Commande | Description |
|----------|-------------|
| `/start` | Démarrer et voir le message d'accueil |
| `/health` | Vérifier que le bot et Claude fonctionnent |
| `/ping` | Alias de /health |
| `/status` | Voir l'état de votre session |
| `/new` | Effacer la session et repartir à zéro |
| `/help` | Afficher l'aide |

**Message texte** → Envoyé à Claude Code, réponse retournée.

---

## Diagnostic

### Le bot ne répond pas

1. Vérifier que le bot tourne (`python bot.py`)
2. Vérifier les logs dans le terminal
3. Tester `/health` sur Telegram

### "Accès non autorisé"

1. Vérifier `ALLOWED_USERS` dans `.env`
2. Obtenir votre user ID via @userinfobot
3. Redémarrer le bot après modification

### Timeout Claude

```env
# Augmenter le timeout dans .env
CLAUDE_TIMEOUT=180
```

### Voir plus de logs

```env
LOG_LEVEL=DEBUG
```

### Erreur "TELEGRAM_BOT_TOKEN non défini"

1. Vérifier que `.env` existe
2. Vérifier que le token est bien renseigné
3. Pas d'espaces autour du `=`

---

## Fichiers du projet

```
claude-telegram-poc/
├── bot.py              # Script principal
├── requirements.txt    # Dépendances Python
├── .env.example        # Template de configuration
├── .env                # Votre configuration (NE PAS COMMIT)
├── .gitignore          # Fichiers à ignorer
└── README.local.md     # Ce fichier
```

**Fichiers générés :**
- `.telegram-claude-sessions.json` - Sessions utilisateurs (local)

---

## Sécurité

### Ce que le bot peut faire

- Lire/écrire des fichiers (via Claude Code)
- Exécuter des commandes Bash (via Claude Code)
- Accéder au web (WebFetch, WebSearch)

### Protections en place

- ✅ Allowlist par user_id (seuls les IDs listés peuvent utiliser le bot)
- ✅ Mode polling (pas d'exposition réseau entrante)
- ✅ Logs des tentatives non autorisées
- ✅ Mode dry-run pour les tests

### Recommandations

1. **Ne jamais partager le token** du bot
2. **Restreindre ALLOWED_USERS** à vous seul en PoC
3. **Superviser les logs** lors des premiers tests
4. **Ne pas exposer** le bot sur un serveur public sans audit

---

## Dépannage avancé

### Tester Claude Code manuellement

```bash
claude -p "Dis bonjour" --output-format json
```

### Vérifier les sessions

```bash
cat .telegram-claude-sessions.json
```

### Effacer toutes les sessions

```bash
rm .telegram-claude-sessions.json
```

---

## Crédits

Basé sur [openclaw-prompts-and-skills](https://github.com/seedprod/openclaw-prompts-and-skills) par SeedProd.
