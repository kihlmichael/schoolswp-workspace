// bridge.js — Telegram → Claude Code CLI bridge (polling)
// Copier dans ~/claude-telegram-bridge/ et lancer avec : node bridge.js

const fetch = require('node-fetch');
const { execSync } = require('child_process');
const fs = require('fs');

// --- CONFIGURATION ---
// Charge .env manuellement (zero dependance)
const envFile = fs.readFileSync('.env', 'utf-8');
envFile.split('\n').forEach(line => {
  const [key, ...val] = line.split('=');
  if (key && !key.startsWith('#')) {
    process.env[key.trim()] = val.join('=').trim();
  }
});

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const ALLOWED_ID = process.env.ALLOWED_CHAT_ID;
const API = `https://api.telegram.org/bot${TOKEN}`;
const POLL_INTERVAL = 3000; // 3 secondes
const MAX_MSG_LENGTH = 4000; // Limite Telegram = 4096

let offset = 0;

// --- FONCTIONS ---

async function getUpdates() {
  try {
    const res = await fetch(
      `${API}/getUpdates?offset=${offset}&timeout=30`
    );
    const data = await res.json();
    return data.ok ? data.result : [];
  } catch (err) {
    console.error('[ERREUR] getUpdates:', err.message);
    return [];
  }
}

async function sendMessage(chatId, text) {
  const chunks = [];
  for (let i = 0; i < text.length; i += MAX_MSG_LENGTH) {
    chunks.push(text.substring(i, i + MAX_MSG_LENGTH));
  }
  for (const chunk of chunks) {
    try {
      await fetch(`${API}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: chatId,
          text: chunk,
        }),
      });
    } catch (err) {
      console.error('[ERREUR] sendMessage:', err.message);
    }
  }
}

function runClaude(prompt) {
  try {
    const escaped = prompt.replace(/"/g, '\\"');
    const cmd = `claude -p "${escaped}" --max-turns 1 2>&1`;
    const output = execSync(cmd, {
      timeout: 120000, // 2 minutes max
      encoding: 'utf-8',
      cwd: process.env.CLAUDE_CWD || process.env.HOME,
    });
    return output.trim() || '(Reponse vide)';
  } catch (err) {
    return `[ERREUR Claude Code] ${err.message}`;
  }
}

// --- BOUCLE PRINCIPALE ---

async function main() {
  console.log('[BRIDGE] Demarre. En attente de messages...');
  console.log(`[BRIDGE] Chat ID autorise : ${ALLOWED_ID}`);

  while (true) {
    const updates = await getUpdates();

    for (const update of updates) {
      offset = update.update_id + 1;
      const msg = update.message;
      if (!msg || !msg.text) continue;

      const chatId = String(msg.chat.id);
      const text = msg.text;

      // Securite : ignore les messages non autorises
      if (chatId !== ALLOWED_ID) {
        console.log(`[BLOCK] Message ignore de ${chatId}`);
        continue;
      }

      console.log(`[MSG] ${text.substring(0, 80)}...`);

      // Commandes speciales
      if (text === '/ping') {
        await sendMessage(chatId, 'Bridge actif.');
        continue;
      }
      if (text === '/status') {
        const info = [
          'Status du bridge :',
          `Uptime : ${process.uptime().toFixed(0)}s`,
          `Offset : ${offset}`,
          `Node : ${process.version}`,
        ].join('\n');
        await sendMessage(chatId, info);
        continue;
      }

      // Envoi a Claude Code
      await sendMessage(chatId, 'Traitement en cours...');
      const response = runClaude(text);
      await sendMessage(chatId, response);
    }

    // Pause entre les polls
    await new Promise(r => setTimeout(r, POLL_INTERVAL));
  }
}

main().catch(console.error);
