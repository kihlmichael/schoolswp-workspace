# Exemple d'extrait d'analyse — Workflow "Telegram YouTube Bot"

Cet extrait montre le format attendu pour les sections cles de l'analyse.
Ce n'est pas un workflow reel — c'est un exemple pedagogique.

---

## 1. Resume executif

- **Ce que fait l'automatisation** : Un bot Telegram recoit un lien YouTube, extrait les metadonnees de la video via l'API YouTube Data v3, genere une description optimisee SEO via OpenAI GPT-4, puis formate un post pret a publier pour une communaute Skool.
- **Point d'entree** : Telegram Trigger (event: message)
- **Resultat final** : Message Telegram contenant (1) description video et (2) post Skool formate
- **Services externes** : Telegram Bot API, YouTube Data API v3, OpenAI API
- **Parcours complet** : Message Telegram → extraction URL → appel YouTube API → generation IA → formatage → reponse Telegram

## 3. Cartographie du pipeline (extrait)

#### Etape 1 — Reception du message Telegram

- **Source** : noeud `Telegram Trigger` (confirme dans le JSON)
- **Entree** : message utilisateur contenant un lien YouTube
- **Traitement** : detection de l'event `message`, extraction du texte
- **Sortie** : `{{ $json.message.text }}`, `{{ $json.message.chat.id }}`
- **Dependances** : credential `telegramApi` (confirme)
- **Preuve** : confirme
- **Notes** : filtre sur `message` uniquement, pas `callback_query`

#### Etape 2 — Extraction de l'ID YouTube

- **Source** : noeud `Extract Video ID` (type: Set)
- **Entree** : `{{ $json.message.text }}`
- **Traitement** : regex extraction via expression n8n `={{ $json.message.text.match(/(?:v=|youtu\.be\/)([a-zA-Z0-9_-]{11})/)?.[1] }}`
- **Sortie** : champ `videoId`
- **Dependances** : aucune
- **Preuve** : confirme — expression trouvee dans le noeud Set
- **Notes** : pas de fallback si le lien est invalide (risque identifie)

## 4. Analyse noeud par noeud (extrait)

#### Workflow : "YouTube Description Generator"

**Trigger** : Telegram Trigger (event: message)

| # | Noeud | Type | Role | Expressions cles | Variables produites | Variables consommees | Preuve |
|---|-------|------|------|------------------|--------------------|--------------------|--------|
| 1 | Telegram Trigger | n8n-nodes-base.telegramTrigger | Recevoir messages | — | message.text, message.chat.id | — | confirme |
| 2 | Extract Video ID | n8n-nodes-base.set | Extraire ID YouTube | `={{ $json.message.text.match(...)  }}` | videoId | message.text | confirme |
| 3 | YouTube Get Video | n8n-nodes-base.httpRequest | Recuperer metadonnees | — | snippet.title, snippet.description | videoId | confirme |
| 4 | Generate Description | @n8n/n8n-nodes-langchain.openAi | Generer description SEO | — | generated_description | snippet.* | confirme |
| 5 | Format Skool Post | n8n-nodes-base.set | Formatter le post Skool | template concatenation | skool_post | generated_description, snippet.title | probable |
| 6 | Send Response | n8n-nodes-base.telegram | Envoyer reponse | — | — | chat.id, generated_description, skool_post | confirme |

**Prompts extraits** :

```
Tu es un expert YouTube SEO. A partir des metadonnees suivantes, genere une description
optimisee pour YouTube qui inclut :
- Un hook accrocheur en premiere ligne
- Les points cles de la video
- Des timestamps si possibles (sinon, les omettre)
- 5-8 hashtags pertinents
- Un appel a l'action

Metadonnees :
Titre : {{ $json.snippet.title }}
Description originale : {{ $json.snippet.description }}
Chaine : {{ $json.snippet.channelTitle }}
```

## 5. Dependances externes (extrait)

| Service | Usage exact | Auth | Donnees envoyees | Donnees recues | Variable .env | Preuve |
|---------|------------|------|-----------------|---------------|--------------|--------|
| Telegram Bot API | Trigger + Send message | Bot Token | message text, chat_id | message_id, update_id | `TELEGRAM_BOT_TOKEN` | confirme |
| YouTube Data API v3 | GET video snippet | API Key (query param) | videoId | title, description, channelTitle, tags | `YOUTUBE_API_KEY` | confirme |
| OpenAI API | Chat completion GPT-4 | Bearer token | system+user prompt | generated text | `OPENAI_API_KEY` | confirme |
| Skool API | — | — | — | — | — | introuvable — aucun appel API Skool detecte, le post est formate localement |

## 8. Ambiguites (extrait)

#### Importants

| Element | Pourquoi c'est ambigu | Ce qui manque | Impact | Action requise |
|---------|----------------------|--------------|--------|---------------|
| Format exact du post Skool | Le noeud "Format Skool Post" utilise une concatenation de champs mais le template complet n'est pas visible (expression trop longue, tronquee dans l'export) | Relire le JSON brut du noeud pour extraire l'expression complete | Le post genere pourrait ne pas matcher le format attendu | Verifier manuellement dans le JSON, champ `parameters.values[0].string` |
| Gestion des liens invalides | Aucun noeud IF apres "Extract Video ID" pour verifier que `videoId` n'est pas null | Un noeud de validation | Le workflow crash silencieusement si on envoie un texte sans lien YouTube | Ajouter un IF avec fallback message d'erreur |

#### Mineurs

| Element | Pourquoi c'est ambigu | Ce qui manque | Impact | Action requise |
|---------|----------------------|--------------|--------|---------------|
| Timezone du workflow | Non specifiee dans le JSON | Configuration n8n serveur | Faible — pas de logique temporelle | Aucune action immediate |
