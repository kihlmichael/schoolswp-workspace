# Guide de diagnostic — Bridge Telegram-Claude ne repond pas

**Symptome** : le terminal affiche `[BRIDGE] Demarre. En attente de messages...` mais aucune reponse n'arrive dans Telegram.

---

## Etape 1 — Verifier l'affichage complet au demarrage

La sortie normale est **en deux lignes** :
```
[BRIDGE] Demarre. En attente de messages...
[BRIDGE] Chat ID autorise : 123456789
```

Si la deuxieme ligne manque ou affiche `undefined`, ton `.env` n'est pas lu. Verifie que le fichier est dans le **meme dossier** que `bridge.js`, sans espaces autour du `=`, sans guillemets.

---

## Etape 2 — Tester l'API Telegram directement

```bash
curl "https://api.telegram.org/bot<TON_TOKEN>/getUpdates"
```

- `401` → token invalide, regenerer via `@BotFather`
- tableau vide → envoie un message au bot, puis relance
- messages presents → note `message.chat.id` et compare a `ALLOWED_CHAT_ID` dans `.env`

---

## Etape 3 — Le Chat ID (cause la plus frequente)

Le filtre dans `bridge.js` ligne 95 est strict : si le Chat ID ne correspond pas exactement, les messages sont ignores **silencieusement**. Tu verras `[BLOCK] Message ignore de XXXXX` dans le terminal si c'est ca.

Recupere ton vrai Chat ID depuis `getUpdates`, corrige `.env`, relance le bridge.

---

## Etape 4 — Tester `/ping` en premier

Envoie `/ping` depuis Telegram. Resultat attendu : `Bridge actif.` Si ca repond, le bridge fonctionne — le probleme vient de Claude Code.

---

## Etape 5 — Tester Claude Code independamment

```bash
claude -p "Dis bonjour en une phrase" --max-turns 1
```

Si `claude: command not found` : le PATH de Node.js ne trouve pas le CLI. Utilise le chemin absolu dans `bridge.js` :
```js
const claudePath = '/chemin/complet/vers/claude'; // which claude
const cmd = `${claudePath} -p "${escaped}" --max-turns 1 2>&1`;
```

---

## Etape 6 — Ajouter un log debug temporaire

Dans `bridge.js`, juste apres `const updates = await getUpdates();` :

```js
console.log(`[DEBUG] ${updates.length} update(s) recus`);
```

- `0 update(s)` en boucle alors que tu as envoye un message → probleme API/token
- `1 update(s)` mais rien ensuite → message filtre ou erreur silencieuse dans `runClaude`

---

## Checklist rapide

| Symptome terminal | Cause | Correction |
|---|---|---|
| Pas de ligne "Chat ID autorise" | `.env` mal lu | Verifier chemin et format |
| `[BLOCK] Message ignore de XXXXX` | Chat ID incorrect | Corriger `ALLOWED_CHAT_ID` |
| Rien du tout | Message pas recu par l'API | Tester via curl |
| `[MSG]` visible, pas de reponse | `runClaude` echoue | Tester `claude -p` directement |
| `[ERREUR Claude Code]` | `claude` pas dans le PATH | Chemin absolu |
| `/ping` OK, questions non | Timeout 2 min | Simplifier le prompt |
| Messages en double | Deux instances | `ps aux | grep bridge.js` |
