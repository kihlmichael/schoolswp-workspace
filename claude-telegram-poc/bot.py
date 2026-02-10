#!/usr/bin/env python3
"""
Telegram Bot ↔ Claude Code CLI (Proof of Concept)

Bot Telegram qui permet de piloter Claude Code en mode headless.
Sécurisé par allowlist d'user IDs.

Usage:
    python bot.py

Configuration:
    Créer un fichier .env avec TELEGRAM_BOT_TOKEN et ALLOWED_USERS
    Voir .env.example pour le template
"""

import subprocess
import json
import os
import sys
import html
import logging
from pathlib import Path
from datetime import datetime

# Charger les variables d'environnement depuis .env
from dotenv import load_dotenv
load_dotenv()

import mistune
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ============================================
# Configuration
# ============================================

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USERS = [int(x.strip()) for x in os.getenv("ALLOWED_USERS", "").split(",") if x.strip()]
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
CLAUDE_TIMEOUT = int(os.getenv("CLAUDE_TIMEOUT", "120"))
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

# Chemin vers Claude CLI (Windows: npm global)
CLAUDE_CMD = os.getenv("CLAUDE_CMD", None)
if not CLAUDE_CMD:
    # Chercher claude dans les emplacements courants
    possible_paths = [
        "claude",  # Dans le PATH
        os.path.expandvars(r"%APPDATA%\npm\claude.cmd"),  # Windows npm global
        os.path.expanduser("~/.npm-global/bin/claude"),  # Linux/Mac npm global
        "/usr/local/bin/claude",  # Mac Homebrew
    ]
    for path in possible_paths:
        expanded = os.path.expandvars(path)
        if os.path.exists(expanded):
            CLAUDE_CMD = expanded
            break
    if not CLAUDE_CMD:
        CLAUDE_CMD = "claude"  # Fallback

# Fichier de sessions (stocké dans le dossier du script)
SESSION_FILE = Path(__file__).parent / ".telegram-claude-sessions.json"

# ============================================
# Logging
# ============================================

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# ============================================
# Gestion des sessions
# ============================================

def load_sessions() -> dict:
    """Charge les sessions depuis le fichier JSON."""
    if SESSION_FILE.exists():
        try:
            return json.loads(SESSION_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            logger.warning("Fichier de sessions corrompu, réinitialisation")
            return {}
    return {}

def save_sessions(sessions: dict):
    """Sauvegarde les sessions dans le fichier JSON."""
    SESSION_FILE.write_text(json.dumps(sessions, indent=2), encoding="utf-8")

# ============================================
# Rendu Markdown → HTML Telegram
# ============================================

class TelegramRenderer(mistune.HTMLRenderer):
    """Convertisseur Markdown vers HTML compatible Telegram."""

    def heading(self, text, level, **attrs):
        return f"<b>{text}</b>\n\n"

    def paragraph(self, text):
        return f"{text}\n\n"

    def list(self, text, ordered, **attrs):
        return text + "\n"

    def list_item(self, text, **attrs):
        return f"• {text}\n"

    def block_code(self, code, info=None):
        escaped = html.escape(code.strip())
        return f"<pre>{escaped}</pre>\n\n"

    def codespan(self, text):
        return f"<code>{html.escape(text)}</code>"

    def emphasis(self, text):
        return f"<i>{text}</i>"

    def strong(self, text):
        return f"<b>{text}</b>"

    def strikethrough(self, text):
        return f"<s>{text}</s>"

    def link(self, text, url, title=None):
        return f'<a href="{html.escape(url)}">{text}</a>'

    def image(self, text, url, title=None):
        return f'[Image: {text}]'

    def block_quote(self, text):
        return f"<blockquote>{text}</blockquote>\n"

    def thematic_break(self):
        return "\n---\n\n"

    def linebreak(self):
        return "\n"

    def table(self, text):
        return f"<pre>{text}</pre>\n\n"

    def table_head(self, text):
        return text + "─" * 20 + "\n"

    def table_body(self, text):
        return text

    def table_row(self, text):
        return text + "\n"

    def table_cell(self, text, align=None, head=False):
        if head:
            return f"<b>{text}</b> │ "
        return f"{text} │ "


# Parser Markdown avec support GFM
md = mistune.create_markdown(
    renderer=TelegramRenderer(escape=False),
    plugins=['strikethrough', 'table', 'task_lists', 'url']
)

def markdown_to_telegram_html(text: str) -> str:
    """Convertit le Markdown en HTML compatible Telegram."""
    result = md(text)
    return result.strip()

# ============================================
# Vérification de sécurité
# ============================================

def check_authorization(user_id: int, username: str = None) -> bool:
    """Vérifie si l'utilisateur est autorisé."""
    logger.debug(f"Auth check: user_id={user_id} (type={type(user_id)}) vs ALLOWED={ALLOWED_USERS}")

    if not ALLOWED_USERS:
        logger.warning("ALLOWED_USERS vide - TOUT LE MONDE peut utiliser le bot!")
        return True

    if user_id in ALLOWED_USERS:
        logger.debug(f"Utilisateur {user_id} autorise")
        return True

    # Log les tentatives non autorisées
    logger.warning(f"Acces refuse: user_id={user_id} username={username} (allowed: {ALLOWED_USERS})")
    return False

# ============================================
# Handlers Telegram
# ============================================

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour /start"""
    user = update.effective_user
    if not check_authorization(user.id, user.username):
        await update.message.reply_text("❌ Accès non autorisé.")
        return

    await update.message.reply_text(
        f"👋 Bienvenue {user.first_name}!\n\n"
        "Je suis connecté à Claude Code.\n"
        "Envoyez-moi un message pour commencer.\n\n"
        "<b>Commandes:</b>\n"
        "/new - Nouvelle session\n"
        "/status - État de la session\n"
        "/health - Vérifier que le bot fonctionne\n"
        "/help - Aide",
        parse_mode="HTML"
    )

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour /help"""
    user = update.effective_user
    if not check_authorization(user.id, user.username):
        await update.message.reply_text("❌ Accès non autorisé.")
        return

    await update.message.reply_text(
        "<b>🤖 Bot Claude Code</b>\n\n"
        "<b>Commandes:</b>\n"
        "• /start - Démarrer le bot\n"
        "• /new - Effacer la session et repartir à zéro\n"
        "• /status - Voir l'état de votre session\n"
        "• /health - Vérifier que le bot fonctionne\n"
        "• /help - Cette aide\n\n"
        "<b>Usage:</b>\n"
        "Envoyez simplement un message pour interagir avec Claude Code.\n"
        "La session est maintenue entre les messages.\n\n"
        "<b>Sécurité:</b>\n"
        f"Mode dry-run: {'Oui' if DRY_RUN else 'Non'}\n"
        f"Utilisateurs autorisés: {len(ALLOWED_USERS)}",
        parse_mode="HTML"
    )

async def cmd_health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour /health - Vérification de santé"""
    user = update.effective_user

    # Vérifier Claude CLI
    try:
        result = subprocess.run(
            [CLAUDE_CMD, "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            shell=(sys.platform == "win32")  # Nécessaire pour .cmd sur Windows
        )
        claude_ok = result.returncode == 0
        claude_version = result.stdout.strip() if claude_ok else "N/A"
    except Exception as e:
        claude_ok = False
        claude_version = f"{str(e)} (path: {CLAUDE_CMD})"

    status_emoji = "+" if claude_ok else "X"
    is_authorized = user.id in ALLOWED_USERS if ALLOWED_USERS else True
    auth_status = "Autorise" if is_authorized else "Non autorise"

    await update.message.reply_text(
        f"<b>Health Check</b>\n\n"
        f"Bot: OK - En ligne\n"
        f"Claude CLI: {status_emoji} {claude_version}\n"
        f"Claude path: <code>{CLAUDE_CMD}</code>\n"
        f"Votre user_id: <code>{user.id}</code>\n"
        f"Allowed users: <code>{ALLOWED_USERS}</code>\n"
        f"Votre acces: {auth_status}\n"
        f"Mode dry-run: {'Actif' if DRY_RUN else 'Inactif'}\n"
        f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        parse_mode="HTML"
    )

async def cmd_ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour /ping - Alias de /health"""
    await cmd_health(update, context)

async def cmd_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour /new - Nouvelle session"""
    user = update.effective_user
    if not check_authorization(user.id, user.username):
        await update.message.reply_text("❌ Accès non autorisé.")
        return

    sessions = load_sessions()
    if str(user.id) in sessions:
        del sessions[str(user.id)]
        save_sessions(sessions)
        logger.info(f"Session effacée pour user_id={user.id}")

    await update.message.reply_text("Session effacee. Le prochain message demarrera une nouvelle conversation.")

async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour /status - État de la session"""
    user = update.effective_user
    if not check_authorization(user.id, user.username):
        await update.message.reply_text("❌ Accès non autorisé.")
        return

    sessions = load_sessions()
    has_session = str(user.id) in sessions
    session_id = sessions.get(str(user.id), "N/A")

    await update.message.reply_text(
        f"<b>📊 État de la session</b>\n\n"
        f"User ID: <code>{user.id}</code>\n"
        f"Username: @{user.username or 'N/A'}\n"
        f"Session active: {'✅ Oui' if has_session else '❌ Non'}\n"
        f"Session ID: <code>{session_id[:20]}...</code>" if has_session else "",
        parse_mode="HTML"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler pour les messages texte"""
    user = update.effective_user
    if not check_authorization(user.id, user.username):
        await update.message.reply_text("❌ Accès non autorisé.")
        return

    message = update.message.text
    logger.info(f"Message de {user.id} (@{user.username}): {message[:50]}...")

    # Mode dry-run pour les tests
    if DRY_RUN:
        await update.message.reply_text(
            f"🧪 <b>Mode Dry-Run</b>\n\n"
            f"Message reçu: <code>{html.escape(message[:100])}</code>\n\n"
            f"Claude ne sera pas appelé en mode dry-run.",
            parse_mode="HTML"
        )
        return

    sessions = load_sessions()

    # Construire la commande Claude
    cmd = [
        CLAUDE_CMD, "-p", message,
        "--output-format", "json",
        "--allowedTools", "Read,Write,Edit,Bash,Glob,Grep,WebFetch,WebSearch"
    ]

    # Reprendre la session existante
    if str(user.id) in sessions:
        cmd.extend(["--resume", sessions[str(user.id)]])
        logger.debug(f"Reprise de session: {sessions[str(user.id)][:20]}...")

    # Indicateur de frappe
    await update.message.chat.send_action("typing")

    # Appeler Claude Code
    try:
        result = subprocess.run(
            cmd if sys.platform != "win32" else " ".join(f'"{c}"' if " " in c else c for c in cmd),
            capture_output=True,
            text=True,
            timeout=CLAUDE_TIMEOUT,
            shell=(sys.platform == "win32")  # Nécessaire pour .cmd sur Windows
        )

        data = json.loads(result.stdout)
        response = data.get("result", "Pas de réponse")

        # Sauvegarder la session
        if data.get("session_id"):
            sessions[str(user.id)] = data["session_id"]
            save_sessions(sessions)
            logger.debug(f"Session sauvegardée: {data['session_id'][:20]}...")

    except subprocess.TimeoutExpired:
        logger.error(f"Timeout après {CLAUDE_TIMEOUT}s")
        response = f"⏱️ Timeout: Claude n'a pas répondu en {CLAUDE_TIMEOUT}s"
    except json.JSONDecodeError:
        logger.error(f"Erreur JSON: {result.stdout[:200]}")
        response = result.stdout or result.stderr or "❌ Erreur lors de l'appel à Claude"
    except Exception as e:
        logger.exception("Erreur inattendue")
        response = f"❌ Erreur: {str(e)}"

    # Convertir Markdown → HTML Telegram
    response = markdown_to_telegram_html(response)

    # Limite Telegram: 4096 caractères
    if len(response) > 4000:
        response = response[:4000] + "\n\n... (tronqué)"

    await update.message.reply_text(response, parse_mode="HTML")

# ============================================
# Main
# ============================================

def main():
    """Point d'entrée principal."""

    # Vérifications
    if not BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN non defini!")
        logger.error("Creez un fichier .env avec votre token (voir .env.example)")
        sys.exit(1)

    if not ALLOWED_USERS:
        logger.warning("ALLOWED_USERS non defini!")
        logger.warning("Le bot acceptera TOUS les utilisateurs.")
        logger.warning("Definissez ALLOWED_USERS dans .env pour restreindre l'acces.")

    # Afficher la config
    logger.info("=" * 50)
    logger.info("Demarrage du bot Telegram Claude Code")
    logger.info("=" * 50)
    logger.info(f"Claude CLI: {CLAUDE_CMD}")
    logger.info(f"Mode dry-run: {DRY_RUN}")
    logger.info(f"Timeout Claude: {CLAUDE_TIMEOUT}s")
    logger.info(f"Utilisateurs autorises: {ALLOWED_USERS or 'TOUS'}")
    logger.info(f"Fichier sessions: {SESSION_FILE}")
    logger.info("=" * 50)

    # Créer l'application
    app = Application.builder().token(BOT_TOKEN).build()

    # Ajouter les handlers
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("health", cmd_health))
    app.add_handler(CommandHandler("ping", cmd_ping))
    app.add_handler(CommandHandler("new", cmd_new))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot pret. Envoyez des messages sur Telegram.")
    logger.info("Arreter avec Ctrl+C")

    # Démarrer le polling (pas de webhook = pas d'exposition réseau)
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
