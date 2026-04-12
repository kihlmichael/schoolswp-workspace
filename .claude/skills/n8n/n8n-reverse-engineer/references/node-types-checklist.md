# Checklist d'extraction par type de noeud n8n

Reference rapide : quoi extraire de chaque type de noeud rencontre dans un export JSON n8n.

---

## Triggers (declencheurs)

### Webhook
- URL du webhook (path)
- Methode HTTP (GET/POST)
- Auth configuree (headerAuth, basicAuth, none)
- Response mode (onReceived, lastNode)
- Schema du body attendu

### Telegram Trigger
- Event type (message, callback_query, edited_message)
- Filtres (chat type, commande specifique)
- Credential reference (nom)
- Champs produits : `message.text`, `message.chat.id`, `message.from`

### Schedule Trigger
- Cron expression ou intervalle
- Timezone

### Form Trigger
- Champs du formulaire
- Titre, description
- Mode de reponse

---

## Transformation de donnees

### Set / Edit Fields
- Champs crees ou modifies (nom + valeur)
- Expressions n8n dans les valeurs (`={{ $json.field }}`, `={{ $('node').item.json.field }}`)
- Mode : "Manual Mapping" vs "JSON"
- Champs supprimes (keep only set)

### Code (JavaScript/Python)
- Langage utilise
- Code source complet (copier textuellement)
- Variables d'entree (`$input.all()`, `$json`, `items`)
- Variables de sortie (structure du return)
- Dependances (require, import)
- Erreurs potentielles (try/catch, throw)

### Function / Function Item (legacy)
- Meme traitement que Code
- Noter que ces noeuds sont deprecies

### Merge
- Mode (append, combine, chooseBranch)
- Input 1 et Input 2 (quels noeuds alimentent)
- Join key si mode combine

### Split In Batches
- Taille du batch
- Options (reset, pause)

### Aggregate
- Champ(s) d'aggreation
- Operation (concatenate, merge, etc.)

---

## Logique conditionnelle

### IF
- Condition exacte (expression)
- Branche true → quel noeud
- Branche false → quel noeud
- Type de comparaison (string, number, boolean, dateTime)

### Switch
- Expression evaluee
- Cas (case values) et noeuds de destination
- Fallback / default

### Filter
- Condition de filtrage
- Comportement "all" vs "any"

---

## Appels externes

### HTTP Request
- URL (verifier si elle contient des expressions)
- Methode (GET, POST, PUT, DELETE, PATCH)
- Headers (statiques et dynamiques)
- Body type (json, form-data, raw)
- Body content (copier tel quel)
- Auth type (predefinedCredentialType, headerAuth, queryAuth, none)
- Credential reference
- Response format attendu
- Options (timeout, redirect, proxy, pagination)

### OpenAI / ChatOpenAI
- Modele utilise (gpt-4, gpt-3.5-turbo, etc.)
- System prompt (texte exact)
- User prompt (texte exact, avec expressions)
- Temperature, max_tokens, top_p
- Tools/functions si definis
- Response format (text, json_object)
- Credential reference

### Anthropic
- Modele
- System prompt
- User messages
- Max tokens
- Credential reference

---

## Integrations specifiques

### Telegram (Send Message)
- Chat ID source (expression ou valeur fixe)
- Texte du message (avec expressions)
- Parse mode (HTML, Markdown, MarkdownV2)
- Reply markup (inline keyboard, reply keyboard)
- Reply to message ID

### Google Sheets
- Operation (append, read, update, lookup)
- Spreadsheet ID
- Sheet name
- Range
- Columns / mapping
- Credential reference

### Google Drive
- Operation (upload, download, list, create folder)
- Folder ID
- File name
- MIME type

### YouTube
- Operation (get video details, search, list)
- Video ID source
- Champs extraits

### WordPress
- Operation (create post, update post, get)
- URL du site
- Champs mappes (title, content, status, categories, tags)
- Credential reference

---

## Controle de flux

### Wait
- Duree ou condition
- Resume type (webhook, timeout)

### Execute Workflow
- Workflow ID reference (noter — ce sub-workflow doit etre analyse aussi)
- Donnees passees en entree
- Mode (once, each item)

### Respond to Webhook
- Response body
- Response headers
- Status code

### Error Trigger
- Workflow source de l'erreur
- Donnees d'erreur disponibles

### No Op / Noop
- Simple passthrough — noter mais pas d'extraction

---

## Pour chaque noeud, toujours verifier

1. **Disabled?** — `"disabled": true` dans le JSON signifie que le noeud est inactif
2. **continueOnFail** — `true` signifie que les erreurs sont avalees (verifier s'il y a une branche d'erreur en aval)
3. **retryOnFail** — nombre de retries et delai
4. **notes** — champ `notes` ou `notesInFlow` (commentaires du createur)
5. **position** — peut aider a comprendre le flux visuel
6. **webhookId** — identifiant unique du webhook (pas le path)
7. **credentials** — toujours noter le nom reference, jamais la valeur
