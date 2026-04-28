# Telegram → Claude Code Bridge sur Windows

Ce guide explique comment envoyer des messages depuis Telegram sur ton telephone et les faire executer par Claude Code sur ta machine Windows.

---

## Vue d'ensemble

L'architecture repose sur trois composants :

```
[Ton telephone Telegram] → [Bot Telegram] → [Script Python sur Windows] → [Claude Code CLI]
```

Le script Python tourne en arriere-plan sur ta machine, ecoute les messages entrants du bot, et les transmet a Claude Code via la CLI.

---

## Prerequis

- Windows 10/11
- Claude Code installe (`claude` disponible dans le terminal)
- Python 3.9+ installe (`python --version`)
- Un compte Telegram
- Acces a BotFather sur Telegram

---

## Etape 1 — Creer le bot Telegram

1. Ouvre Telegram, cherche `@BotFather`
2. Envoie `/newbot`
3. Choisis un nom (ex: `MonClaudeBot`) et un username (ex: `mon_claude_bot`)
4. BotFather te donne un **token API** de la forme `123456789:ABCdef...` — copie-le

---

## Etape 2 — Recuperer ton Chat ID

1. Envoie n'importe quel message a ton nouveau bot
2. Ouvre dans un navigateur : `https://api.telegram.org/bot<TON_TOKEN>/getUpdates`
3. Dans la reponse JSON, trouve `"chat":{"id":XXXXXXXXX}` — note ce nombre, c'est ton **Chat ID**

C'est ce Chat ID qui permettra de filtrer les messages (seul toi peux declencher des commandes).

---

## Etape 3 — Installer la dependance Python

```bash
pip install python-telegram-bot
```

---

## Etape 4 — Creer le script bridge

Cree un fichier `telegram_claude_bridge.py` :

```python
import subprocess
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# --- Configuration ---
TELEGRAM_TOKEN = "TON_TOKEN_ICI"
ALLOWED_CHAT_ID = TON_CHAT_ID_ICI  # Entier, pas de guillemets
WORKING_DIR = r"D:\VS Code\CLAUDE CODE\projects\schoolswp"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    if chat_id != ALLOWED_CHAT_ID:
        logger.warning(f"Message ignore — chat_id non autorise : {chat_id}")
        return

    message = update.message.text
    logger.info(f"Commande recue : {message}")

    await update.message.reply_text(f"Execution en cours...\n`{message}`", parse_mode="Markdown")

    try:
        result = subprocess.run(
            ["claude", "-p", message, "--output-format", "text"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=WORKING_DIR,
            encoding="utf-8"
        )

        output = result.stdout.strip() or result.stderr.strip() or "(pas de sortie)"

        if len(output) > 4000:
            output = output[:4000] + "\n\n...(tronque)"

        await update.message.reply_text(output)

    except subprocess.TimeoutExpired:
        await update.message.reply_text("Timeout — la commande a pris plus de 5 minutes.")
    except Exception as e:
        await update.message.reply_text(f"Erreur : {str(e)}")


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bridge Telegram → Claude Code demarre")
    app.run_polling()


if __name__ == "__main__":
    main()
```

---

## Etape 5 — Configurer le script

Remplace :
- `TON_TOKEN_ICI` → le token recupere a l'etape 1
- `TON_CHAT_ID_ICI` → ton Chat ID recupere a l'etape 2
- `WORKING_DIR` → le dossier depuis lequel Claude Code doit s'executer

---

## Etape 6 — Tester manuellement

```bash
python telegram_claude_bridge.py
```

Depuis Telegram, envoie un message a ton bot : `liste les fichiers dans le dossier courant`

Tu devrais recevoir la reponse de Claude Code dans Telegram.

---

## Etape 7 — Lancer automatiquement au demarrage Windows (optionnel)

### Option A — Planificateur de taches Windows

1. Ouvre **Planificateur de taches** (Task Scheduler)
2. Cree une tache de base, declencheur : **Au demarrage**
3. Programme : `pythonw.exe`
4. Arguments : chemin complet vers le script

### Option B — Fichier .bat dans le dossier Demarrage

```bat
@echo off
start /B pythonw "C:\Users\TonNom\claude-bridge\telegram_claude_bridge.py"
```

Place ce `.bat` dans :
```
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\
```

---

## Securite

- **Ne partage jamais ton token Telegram** — il donne le controle total du bot
- Le filtre `ALLOWED_CHAT_ID` est essentiel : sans lui, n'importe qui peut executer des commandes sur ta machine
- Claude Code s'execute avec les permissions de ton compte Windows
- Envisage d'ajouter un prefixe de commande pour eviter les executions accidentelles

---

## Depannage

| Probleme | Cause probable | Solution |
|---|---|---|
| Le bot ne repond pas | Token incorrect | Verifie le token dans BotFather |
| "claude: command not found" | CLI pas dans le PATH | Utilise le chemin complet vers `claude` |
| Timeout systematique | Commande trop longue | Augmente le `timeout` dans `subprocess.run` |
| Encodage casse | Probleme Windows | Ajoute `encoding="utf-8"` |
| Script plante au demarrage | Dependance manquante | Relance `pip install python-telegram-bot` |
