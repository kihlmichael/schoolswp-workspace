---
name: openai-whisper-api
description: |
  Transcription audio via l'API OpenAI /v1/audio/transcriptions (whisper-1) en curl. Gère --language, --prompt (noms d'intervenants), --json, sortie .txt par défaut. Nécessite OPENAI_API_KEY.
  Utilise ce skill quand l'utilisateur dit : "transcription Whisper API", "OpenAI audio transcriptions", "transcrit ce mp3/m4a en cloud", "Whisper en curl", ou veut une transcription rapide sans installer le CLI Whisper local.
  NE PAS utiliser pour : transcription locale sans clé API (utiliser openai-whisper), transcription d'une vidéo YouTube (utiliser dataforseo subtitles ou external-video-use), ou transcription temps réel streaming (utiliser gemini-live-api-dev).
homepage: https://platform.openai.com/docs/guides/speech-to-text
metadata: {"openclaw":{"emoji":"☁️","requires":{"bins":["curl"],"env":["OPENAI_API_KEY"]},"primaryEnv":"OPENAI_API_KEY"}}
last_reviewed: 2026-04-23
review_interval_days: 60
---

# OpenAI Whisper API (curl)

Transcrire un fichier audio via l'endpoint `/v1/audio/transcriptions` d'OpenAI.

## Démarrage rapide

```bash
{baseDir}/scripts/transcribe.sh /chemin/vers/audio.m4a
```

Défauts :
- Modèle : `whisper-1`
- Sortie : `<input>.txt`

## Options utiles

```bash
{baseDir}/scripts/transcribe.sh /chemin/vers/audio.ogg --model whisper-1 --out /tmp/transcript.txt
{baseDir}/scripts/transcribe.sh /chemin/vers/audio.m4a --language fr
{baseDir}/scripts/transcribe.sh /chemin/vers/audio.m4a --prompt "Noms des intervenants : Pierre, Daniel"
{baseDir}/scripts/transcribe.sh /chemin/vers/audio.m4a --json --out /tmp/transcript.json
```

## Clé API

Définir `OPENAI_API_KEY`, ou la configurer dans `~/.openclaw/openclaw.json` :

```json5
{
  skills: {
    "openai-whisper-api": {
      apiKey: "VOTRE_CLE_OPENAI_ICI"
    }
  }
}
```
