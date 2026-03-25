---
name: openai-whisper
description: Transcription audio locale avec le CLI Whisper (pas de clé API nécessaire).
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
