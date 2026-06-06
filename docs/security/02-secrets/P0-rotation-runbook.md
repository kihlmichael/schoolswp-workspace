# P0 Rotation Runbook - Action immediate

> Date : 2026-05-12. Estimation totale : **60 minutes**.
> A faire AVANT l etape 5 du briefing (backup), sinon le snapshot capture des secrets perimes.
> Coche au fur et a mesure et reviens me dire OK quand tout est fait, on enchaine sur Etape 5.

---

## Pre-requis

- Ouvre 1Password (pour stocker les nouvelles valeurs au fur et a mesure)
- Garde Claude Code ouvert dans une autre fenetre (pour les updates `.env` apres rotation)

---

## 1. jwt n8n-mcp `.mcp.json` (...fCmA) - 15 min

**Localisation** : `.mcp.json` -> `mcpServers.n8n-mcp.env.N8N_API_KEY` (en clair, pas via ${VAR}).

**Etapes** :

- [ ] Ouvre https://schoolswp-n8n.wp1.host/settings/api
- [ ] Identifie la cle qui finit par `...fCmA` dans la liste
- [ ] Clique sur Revoke ou Delete sur cette cle
- [ ] Cree une nouvelle cle, nom : "Claude Code MCP - schoolsWP"
- [ ] Copie la nouvelle valeur dans 1Password vault "schoolsWP-apis" sous "n8n_api_key"
- [ ] Edite `.mcp.json` : remplace la valeur en clair par `${N8N_API_KEY}`
- [ ] Edite `.claude/settings.local.json` (top-level env block) : `"N8N_API_KEY": "<new value>"`
- [ ] Redemarre Claude Code (ou recharge la session pour que le MCP n8n-mcp pick la nouvelle valeur)
- [ ] Verifie : appelle `mcp__n8n-mcp__n8n_health_check` pour confirmer connectivite

---

## 2. Cle Gemini #1 (...yW1E) - 5 min

**Localisation** : Git history schoolswp, fichier `.nano-banana-config.json` (commit a4cbc571).

**Etapes** :

- [ ] Ouvre https://aistudio.google.com/apikey
- [ ] Identifie la cle finissant par `...yW1E` dans la liste
- [ ] Clique sur les 3 dots > Delete API key
- [ ] Cree une nouvelle cle, nom : "nano-banana schoolsWP"
- [ ] Copie la nouvelle valeur dans 1Password vault "schoolsWP-apis" sous "gemini_nanobanana"
- [ ] Si tu utilises encore cette cle quelque part : mettre a jour `.nano-banana-config.json` local (sans rewrite history Git)
- [ ] Note : la valeur historique reste dans Git mais est invalide cote provider = neutralisee

---

## 3. Cle Gemini #2 (...RUX0) - 10 min

**Localisation** : Git history schoolswp, 3 fichiers :
- `data/setup_gemini_credential.py`
- `tools/scripts/nas-photo-renamer.py`
- `tools/scripts/photo-vacances-organizer.py`

**Etapes** :

- [ ] Toujours sur https://aistudio.google.com/apikey
- [ ] Identifie la cle finissant par `...RUX0` (probable nom : "Gemini Production" ou "schoolswp-credential")
- [ ] Delete
- [ ] Cree une nouvelle cle, nom : "Gemini schoolsWP scripts"
- [ ] Stocke dans 1Password sous "gemini_scripts"
- [ ] Verifie si les 3 scripts Python ci-dessus sont encore utilises (probable archived/legacy) :
    - Si oui : update via `.env` + variable `GEMINI_API_KEY`
    - Si non : aucune action de plus, la cle revoked est neutralisee

---

## 4. jwt n8n geo-architect-bulk-fill (...rcGY) - 15 min

**Localisation** : Workflow n8n actif, ID `3JE0YzrhoiusJZ6T` ("Webhook > Google Sheets: GEO Architect Bulk Fill"), hardcode dans node Code.

**Etapes** (auto-fixable via MCP n8n-mcp) :

- [ ] Demande-moi : "Rotate jwt rcGY dans workflow 3JE0YzrhoiusJZ6T"
- [ ] Je :
    1. Appelle `n8n_get_workflow` pour extraire la valeur exacte
    2. Cree une credential typee `httpHeaderAuth` via `n8n_manage_credentials({action: 'create'})`
    3. Remplace le secret par la reference credential via `n8n_update_partial_workflow`
- [ ] Tu valides en regardant le workflow dans https://schoolswp-n8n.wp1.host/workflow/3JE0YzrhoiusJZ6T
- [ ] Tu revoke l ancien jwt cote provider (si jwt n8n natif : Settings > API Keys ; si jwt custom : la source du token)

**Variantes** : meme operation pour le jwt dans workflow `BStRQkYKRv6VcRsf` (LinkedIn Post V4) et `iXR2tvSfd5L9zE2t` (Workflows Backup). Ils sont distincts, tous les 3 sont a fixer.

---

## 5. jwt settings.json (...91q4) - 10 min

**Localisation** : Git history schoolswp, fichier `settings.json` (root), commit 080ef6a9 (2026-03-05 "commitWP"). Le commit b5beaa32 (2026-03-14 "security hardening - untrack ccpa.config.json") a probablement retire le fichier du tracking, mais le jwt reste dans l historique.

**Etapes** :

- [ ] Verifie si `settings.json` (root) existe encore aujourd hui :
    - Ouvre PowerShell : `Test-Path "d:/VS Code/CLAUDE CODE/projects/schoolswp/settings.json"`
    - Si Yes : ouvre le fichier, identifie le jwt, suis son origine (commentaire, nom de variable adjacente).
    - Si No : le fichier a deja ete supprime. Le jwt est inerte cote disque mais reste dans Git history.
- [ ] Si tu identifies le service proprietaire : revoke cote provider.
- [ ] Si non identifiable : risque accepte, documente dans le dashboard final (etape 15).

---

## 6. Telegram bot token archive (...cfEY) - 5 min

**Localisation** : `apps/_archive/telegram-bot-legacy/.env` -> probable `TELEGRAM_BOT_TOKEN`.

**Etapes** :

- [ ] Ouvre Telegram, va sur @BotFather
- [ ] Tape `/mybots`
- [ ] Identifie le bot qui correspond au token `...cfEY` (regarde la liste de tes bots, tu en as 9 documentes)
- [ ] Selectionne le bot > API Token > Revoke current token
- [ ] (Si tu utilises encore ce bot, regenere et stocke dans 1Password. Sinon revoke suffit)
- [ ] Pour purger le fichier : confirmation a l etape de cleanup, on le supprimera via Explorer

---

## Validation finale

Une fois tous les 6 cocher OK :

- [ ] **Verifie qu aucun workflow n8n actif ne casse** : passe sur https://schoolswp-n8n.wp1.host et regarde les 27 actifs (statut). Si un tourne en erreur depuis < 1h, c est qu il utilisait un secret rotate.
- [ ] **Verifie que les agents Python locaux tournent** : un coup de `brain.bat --help` pour confirmer que les agents loadent toujours .env correctement.
- [ ] **Reviens me dire "OK rotation P0 done"** et on enchaine sur l etape 5 (backup non-negociable).

---

## En cas de probleme

- **Le MCP n8n-mcp ne se reconnecte pas apres rotation** : verifie que `.claude/settings.local.json` a bien la nouvelle valeur dans `env.N8N_API_KEY`. Force restart Claude Code.
- **Un workflow n8n casse** : tu peux toujours revoke la rotation cote n8n (recree une cle avec l ancienne valeur si tu l as gardee), mais c est mieux de fixer le workflow correctement.
- **Tu ne trouves pas la cle "...yW1E" dans Google AI Studio** : possible qu elle ait deja ete revoquee ou jamais utilisee. Skip.
- **Tu n identifies pas le bot Telegram cfEY** : ouvre `apps/_archive/telegram-bot-legacy/.env` avec Notepad (pas Claude), copie les 4 derniers chars, croise avec ta liste BotFather.

---

## Note sur l historique Git

Tu vas peut-etre te demander : "Et pourquoi ne pas reecrire l historique pour purger les secrets ?"

Reponse : `git filter-repo` ou `git filter-branch` change tous les hashes commits depuis le secret. Sur un repo de 157 commits avec 5+ machines connectees (PC dev + xCloud apps + sauvegardes WPvivid/Umbrella + Backblaze), ca crée plus de chaos que ca n en resoud. La **rotation cote provider rend les secrets historiques inertes** sans toucher au repo.

Si jamais le repo devient public un jour, **alors** considere `git filter-repo` 24h avant la mise en public, en gerant le sync de tous les remotes/sauvegardes.
