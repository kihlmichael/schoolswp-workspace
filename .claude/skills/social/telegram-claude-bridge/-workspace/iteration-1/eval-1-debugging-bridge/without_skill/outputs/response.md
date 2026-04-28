# Guide de diagnostic — Bridge Telegram-Claude silencieux

**Symptome** : `[BRIDGE] Demarre` s'affiche, mais aucun message ne produit de reponse.

---

## Etape 1 — Verifier que Telegram envoie bien les messages au bridge

**Mode polling** — teste directement via curl :

```bash
curl https://api.telegram.org/bot<TON_TOKEN>/getUpdates
```

Envoie un message depuis ton telephone, puis relance cette commande. Si `result` est vide : soit le bridge consomme les updates sans logger, soit un autre processus tourne en parallele.

**Mode webhook** — verifie l'etat :

```bash
curl https://api.telegram.org/bot<TON_TOKEN>/getWebhookInfo
```

Le champ `last_error_message` indique si Telegram a tente de livrer et echoue.

---

## Etape 2 — Verifier le token bot

```bash
curl https://api.telegram.org/bot<TON_TOKEN>/getMe
```

Si `ok: false` → token invalide ou revoque. Regenere via @BotFather avec `/token`.

---

## Etape 3 — Ajouter des logs aux trois points critiques

```python
# 1. Reception
print("[BRIDGE] Message recu :", update.message.text)

# 2. Avant Claude
print("[BRIDGE] Appel Claude...")

# 3. Avant renvoi Telegram
print("[BRIDGE] Envoi reponse, chat_id :", chat_id)
```

Si les logs s'arretent au point 1 : le handler n'est pas enregistre. Au point 2 : l'appel Claude echoue. Au point 3 : le renvoi Telegram echoue (mauvais chat_id).

---

## Etape 4 — Chercher les try/except muets (cause la plus frequente)

```python
# Mauvais — avale l'erreur silencieusement
try:
    response = await client.messages.create(...)
except Exception:
    pass

# Corriger en :
except Exception as e:
    print("[BRIDGE] ERREUR :", e)
```

---

## Etape 5 — Verifier les variables d'environnement

```python
import os
print("TELEGRAM_TOKEN :", bool(os.getenv("TELEGRAM_TOKEN")))
print("ANTHROPIC_API_KEY :", bool(os.getenv("ANTHROPIC_API_KEY")))
```

Un `.env` non charge au bon endroit est une cause classique de silence total.

---

## Etape 6 — Verifier le filtrage chat_id

Beaucoup de bridges ont une allowlist. Si ton chat_id n'y est pas, le message est ignore sans log.

```python
ALLOWED_CHAT_IDS = [123456]
if update.message.chat_id not in ALLOWED_CHAT_IDS:
    return  # ignore en silence
```

Trouve ton chat_id reel dans la sortie de `getUpdates` (champ `message.chat.id`).

---

## Etape 7 — Verifier les conflits de processus

Deux instances du bridge = la seconde ne recoit plus rien (la premiere a consomme les updates).

```bash
ps aux | grep bridge   # Linux/macOS
tasklist | findstr python  # Windows
```

---

## Etape 8 — Tester l'API Anthropic directement

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-4-6","max_tokens":50,"messages":[{"role":"user","content":"ping"}]}'
```

401 = cle invalide. 529 = surcharge. Silence dans le bridge = erreur catchee quelque part.

---

## Checklist rapide

| Verification | Action |
|---|---|
| Token valide | `curl .../getMe` |
| Updates recus | `curl .../getUpdates` apres envoi |
| Handler enregistre | Log dans la fonction handler |
| Try/except muets | Grep `except:` et `except Exception:` dans le code |
| Variables d'env | Log au demarrage |
| Processus unique | `ps aux` ou `tasklist` |
| Filtrage chat_id | Lire le code source |
| API Anthropic OK | Test curl direct |

**Ordre de priorite** : commence par `getUpdates` direct, puis ajoute un log dans le handler, puis cherche les blocs except muets — ces trois etapes resolvent 90% des cas.
