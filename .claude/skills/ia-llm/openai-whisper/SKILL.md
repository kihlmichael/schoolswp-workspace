---
name: openai-whisper
description: |
  Transcription audio locale avec le CLI Whisper open source (pas de clé API). Gère --model (turbo par défaut, medium/large pour précision), --task translate, formats de sortie txt/srt/vtt/json. Modèles téléchargés automatiquement dans ~/.cache/whisper.
  Utilise ce skill quand l'utilisateur dit : "Whisper local", "CLI Whisper", "transcription offline", "transcrit sans clé API", "translate audio en anglais", ou traite un volume audio sans budget API.
  NE PAS utiliser pour : transcription cloud rapide via API (utiliser `openai-whisper-api`), transcription temps réel streaming (utiliser `gemini-live-api-dev`), ou récupérer les sous-titres d'une vidéo YouTube (utiliser `dataforseo` subtitles).
homepage: https://openai.com/research/whisper
metadata: {"openclaw":{"emoji":"🎙️","requires":{"bins":["whisper"]},"install":[{"id":"brew","kind":"brew","formula":"openai-whisper","bins":["whisper"],"label":"Installer OpenAI Whisper (brew)"}]}}
---

# Whisper (CLI)

Utilisez `whisper` pour transcrire de l'audio localement.

## Démarrage rapide

- `whisper /chemin/audio.mp3 --model medium --output_format txt --output_dir .`
- `whisper /chemin/audio.m4a --task translate --output_format srt`

## Notes

- Les modèles se téléchargent dans `~/.cache/whisper` au premier lancement.
- `--model` est par défaut `turbo` sur cette installation.
- Utiliser des modèles plus petits pour la vitesse, plus grands pour la précision.
