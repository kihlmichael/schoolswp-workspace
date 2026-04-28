# Architecture : commandes predefinies Telegram pour schoolsWP

## Principe de routage

Le dispatcher detecte si le message commence par `/`, extrait la commande et les arguments, puis mappe vers un handler dedie :

```
Message → Dispatcher → Command Router → Prompt Builder → Anthropic API → sendMessage
```

## Structure de fichiers

```
telegram-bot/
├── dispatcher.js         # Detection /cmd et routage
├── commands/
│   ├── index.js          # Registry { seo, article, check }
│   ├── seo.js
│   ├── article.js
│   └── check.js
├── lib/
│   ├── claude.js         # Wrapper callClaude()
│   └── wp-api.js         # Appels WP REST API (pour /check)
```

## Mapping commande → prompt

| Commande | Args | Prompt envoye |
|---|---|---|
| `/seo` | vide | Audit general schoolswp.fr |
| `/seo lms wordpress` | mot-cle | Analyse intention + structure + 3 actions |
| `/seo https://...` | URL | Audit on-page cible |
| `/article fluentcrm avis` | sujet | H1 + plan + premier H2 + metadonnees SEO |
| `/check` | vide | Ping WP API + n8n en parallele |
| `/check api` | composant | Ping WordPress REST uniquement |

## Code cle — dispatcher.js

```javascript
async function dispatch(bot, msg) {
  const match = msg.text?.match(/^\/(\w+)(?:@\w+)?(?:\s+(.*))?$/s);
  if (match) {
    const cmd = match[1].toLowerCase();
    const args = (match[2] || '').trim();
    const handler = commands[cmd];
    if (handler) {
      await bot.sendMessage(msg.chat.id, `Traitement de /${cmd}...`);
      const result = await handler(args, { chatId: msg.chat.id });
      await sendLong(bot, msg.chat.id, result);
    }
  }
}
```

## Prompts systeme par commande

**`/seo`** : "Expert SEO WordPress specialise formation en ligne. Audit en 5 points, score /10, priorite HAUTE/MOYENNE/BASSE."

**`/article`** : "Redacteur schoolsWP, audience createurs de formation. Genere : H1 + intro + plan H2/H3 + premier H2 developpe + metadonnees (title 60 car, meta 155 car, slug)."

**`/check`** : Pas de Claude — ping direct WP REST API + n8n `/healthz`, puis resume par Claude si les donnees sont complexes.

## Pattern avance : appel direct agent Python

Si le bot tourne sur le meme serveur que les agents schoolsWP :

```javascript
const { execFile } = require('child_process');
const python = 'd:/VS Code/CLAUDE CODE/projects/schoolswp/.venv/Scripts/python';

async function runAgent(module, args) {
  const { stdout } = await execFileAsync(python, ['-m', module, ...args]);
  return stdout;
}

// Dans /seo :
return runAgent('agents.seo_auditor.cli', ['--keyword', args]);
```

Cela reutilise exactement les 28 agents Python existants plutot que de dupliquer la logique.
