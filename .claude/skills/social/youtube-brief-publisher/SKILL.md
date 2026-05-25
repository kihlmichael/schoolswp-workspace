---
name: youtube-brief-publisher
description: |
  Pipeline complet YouTube : transcription d'audio via ElevenLabs (Scribe v2), rédaction de scripts originaux schoolsWP via Claude 3.5 Sonnet sous contraintes brand strict, génération SEO via Claude 3.5 Haiku et auto-publication YouTube via Google Sheets/Drive et Blotato (W209/W209a).
  Utilise ce skill quand l'utilisateur dit : "génère un brief depuis cette vidéo YouTube", "rédige un script schoolsWP à partir de ce lien", "publie ma vidéo YouTube finale", "active la routine de publication", ou pour paramétrer/intégrer le bot Telegram YT.
---

# YouTube Brief & Publisher - Pipeline schoolsWP

Ce Skill implémente le double pipeline de production de contenu vidéo schoolsWP à partir d'une vidéo YouTube concurrent/inspirante :
1. **Pipeline de Brief (W209)** : Transcription audio (ElevenLabs Scribe v2), réécriture originale au "JE" sous contraintes strictes `BRAND_RULES` (Claude 3.5 Sonnet), package SEO structuré (Claude 3.5 Haiku), écriture dans Google Sheets, notification Telegram de l'utilisateur et log Discord de l'équipe.
2. **Pipeline d'Auto-Publication (W209a)** : Scrutation périodique de Google Sheets (toutes les 30 min), téléchargement de la vidéo produite sur Google Drive, publication YouTube via Blotato en mode non répertorié ("unlisted") et alertes Discord.

---

## 1. Prérequis & Fichier d'Environnement

Créez ou complétez le fichier `.env` à la racine du projet schoolsWP avec les clés d'API requises :

```env
# 1. TELEGRAM BOT
TELEGRAM_BOT_TOKEN=__TOKEN_BOT_TELEGRAM__
TELEGRAM_ADMIN_CHAT_ID=__CHAT_ID_ADMIN_TELEGRAM__

# 2. GOOGLE APPLICATION CREDENTIALS
GOOGLE_APPLICATION_CREDENTIALS_JSON=__CONTENU_JSON_SERVICE_ACCOUNT__
GOOGLE_SHEETS_SPREADSHEET_ID=1WQgRPLFctLUcMauI1AdRniGB5rFpWrc8mZjumtecVMU

# 3. ELEVENLABS API (TRANSCRIPTION)
ELEVENLABS_API_KEY=__CLE_API_ELEVENLABS__

# 4. ANTHROPIC API (INTELLIGENCE ARTIFICIELLE)
ANTHROPIC_API_KEY=__CLE_API_ANTHROPIC__

# 5. DISCORD WEBHOOK (ALERTING)
DISCORD_WEBHOOK_SEO=__URL_WEBHOOK_DISCORD__

# 6. BLOTATO API (YOUTUBE AUTO-PUBLISH)
BLOTATO_API_KEY=__CLE_API_BLOTATO__
BLOTATO_ACCOUNT_ID=__ACCOUNT_ID_BLOTATO__
```

---

## 2. Structure et Organisation

Les composants du Skill sont organisés ainsi :
* `prompts/write_brief_sonnet.txt` : Prompt système Sonnet pour la rédaction originale (au "JE", tutoiement direct, respect de la règle 31 de non-paraphrase).
* `prompts/write_seo_haiku.txt` : Prompt système Haiku forçant la génération stricte de JSON structuré pour les métadonnées SEO.
* `config/settings.json` : Paramètres d'onglets Sheets, de langue de sortie et de visibilité YouTube par défaut.
* `scripts/transcribe_elevenlabs.py` : Module de téléchargement d'audio léger (`yt-dlp`) et de transcription (`ElevenLabs Scribe v2`).
* `scripts/sheets_client.py` : Client d'API Google Sheets (écritures et lectures).
* `scripts/drive_client.py` : Client d'API Google Drive (téléchargement du MP4 de production).
* `scripts/blotato_client.py` : Client d'API de publication Blotato / YouTube.

---

## 3. Guide d'Utilisation

### A. Générer un Brief & SEO à partir d'un lien YouTube (W209)
Pour lancer manuellement l'orchestrateur de brief sur un lien YouTube :

```bash
.venv/Scripts/python .claude/skills/social/youtube-brief-publisher/scripts/run_pipeline.py "https://www.youtube.com/watch?v=A8vGpt9Qx_o
brief schoolsWP : angle / cible / promesse" "TELEGRAM_CHAT_ID"
```

Le script va automatiquement :
1. Découper le message pour isoler l'URL YouTube (ligne 1) et votre brief (lignes 2+).
2. Ajouter une ligne d'ingestion initiale dans votre table Google Sheets (statut `received`).
3. Télécharger la piste audio de la vidéo source via `yt-dlp` et la transcrire via **ElevenLabs Scribe v2** en français.
4. Rédiger le script original au "JE" avec Claude 3.5 Sonnet.
5. Formater le package SEO JSON (Titre, Description et 15 tags) avec Claude 3.5 Haiku.
6. Mettre à jour la ligne Google Sheets (statut `ready`).
7. Vous envoyer un message de succès sur Telegram et alerter l'équipe sur Discord.

### B. Lancer la routine de publication automatique (W209a)
Pour scanner la feuille de suivi Google Sheets et publier sur YouTube les vidéos prêtes qui possèdent un lien Google Drive :

```bash
.venv/Scripts/python .claude/skills/social/youtube-brief-publisher/scripts/run_publisher.py
```

Le script va automatiquement :
1. Lire la feuille Google Sheets et filtrer toutes les lignes ayant le statut `"ready"`.
2. Pour chaque ligne, si le champ `url_video` est renseigné (lien de partage Google Drive de votre vidéo produite) :
   * Extraire l'ID du fichier Google Drive.
   * Télécharger la vidéo binaire MP4 de manière sécurisée en local temporaire.
   * Pousser le binaire de la vidéo sur YouTube via l'API Blotato en mode non répertorié (`unlisted`).
   * Mettre à jour le statut de la ligne Sheets à `"published"` et enregistrer le timestamp exact dans `published_at`.
   * Pousser un webhook de confirmation et de relecture sur Discord.
   * Nettoyer la vidéo temporaire locale.

---

## 4. Architecture de la base Google Sheets (12 colonnes)

Le fichier Google Sheets (ID `1WQgRPLFctLUcMauI1AdRniGB5rFpWrc8mZjumtecVMU`, onglet par défaut `"Untitled"`) comporte l'organisation stricte suivante :

| Colonne | En-tête | Rôle technique |
| :--- | :--- | :--- |
| A | `date` | Horodatage ISO de la demande reçue par Telegram. |
| B | `url` | URL YouTube de la vidéo concurrente source. |
| C | `brief_user` | Brief d'orientation saisi par l'humain. |
| D | `video_id` | ID vidéo unique extrait (sert de clé primaire). |
| E | `language` | `"francais"` par défaut. |
| F | `status` | Cycle de vie de la demande : `"received"` -> `"ready"` -> `"published"`. |
| G | `brief_schoolswp` | Le script de brief complet original rédigé par Claude 3.5 Sonnet. |
| H | `title_fr` | Le titre YouTube optimisé (max 60 caractères). |
| I | `description_fr` | La description SEO rédigée (2-3 paragraphes). |
| J | `tags_fr` | Les 15 tags optimisés en minuscules séparés par des virgules. |
| K | `url_video` | URL de partage Google Drive de votre vidéo finale (déposée manuellement). |
| L | `published_at` | Horodatage ISO de publication effective de la vidéo sur YouTube. |

---

## 5. Rapatriement et Intégration n8n

Les fichiers de sauvegardes des workflows d'origine sont stockés dans le projet et peuvent être réimportés dans votre instance n8n à tout moment :
* **Workflow W209** : [tR7J1fteY44eDdke__InTesting--Telegram---Sheets--YT-Source----Brief-schoolsWP--W209.json](../../../../docs/security/09-backup/n8n-snapshot-2026-05-12/tR7J1fteY44eDdke__InTesting--Telegram---Sheets--YT-Source----Brief-schoolsWP--W209.json)
* **Workflow W209a** : [kgeMDb9hIXwvOzLK__InTesting--Sheets---Blotato---YouTube--Auto-Publish--W209a.json](../../../../docs/security/09-backup/n8n-snapshot-2026-05-12/kgeMDb9hIXwvOzLK__InTesting--Sheets---Blotato---YouTube--Auto-Publish--W209a.json)

### Procédure de paramétrage post-import :
1. Dans l'interface de n8n, créez un nouveau workflow et cliquez sur **Import from file** en important l'un des JSON ci-dessus.
2. **Remappez les credentials** sur vos identifiants réels :
   * Telegram : Associez à votre bot dédié `@schoolswp_yt_bot`
   * Google Sheets : Connectez à votre Service Account `Google Sheets - schoolsWP v2`
   * Google Drive : Connectez à votre Service Account `Google Drive - schoolsWP v2`
   * Anthropic : Associez votre clé d'API Anthropic de production
   * Discord Webhook : Configurez l'URL ou le connecteur webhook Discord
3. Basculez le bouton **Active** en haut à droite à `True` pour rendre les déclencheurs opérationnels.
