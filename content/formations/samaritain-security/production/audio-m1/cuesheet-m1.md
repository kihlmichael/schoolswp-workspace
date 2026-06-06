# M1 — Samaritain Security : cuesheet montage

Source audio : 10 MP3 ElevenLabs (voix clone Michaël), dossier `audio-m1/`.
Durée totale mesurée : **4:05.76** (cible script doc : 4:45.00, drift total : -39.24s).

| # | Scène | Capture | Cible script | Durée MP3 réelle | Démarre à | Drift |
|---|-------|---------|--------------|------------------|-----------|-------|
| S01 | `M1-S01-hook.mp3` | face cam (pas de capture) | 0:00.00–0:15.00 (15s) | 18.11s | 0:00.00 | +3.11s |
| S02 | `M1-S02-desactiver.mp3` | screencast live : page Extensions WP | 0:15.00–0:40.00 (25s) | 23.64s | 0:18.11 | -1.36s |
| S03 | `M1-S03-televerser.mp3` | screencast live : Extensions > Ajouter > Téléverser ZIP | 0:40.00–1:10.00 (30s) | 24.61s | 0:41.75 | -5.39s |
| S04 | `M1-S04-licence.mp3` | Cap 19 (écran licence vide) puis Cap 3 (Licence Active) | 1:10.00–1:50.00 (40s) | 27.12s | 1:06.36 | -12.88s |
| S05 | `M1-S05-nouvelle-url.mp3` | Cap 4 zoom URL connexion - SLUG À FLOUTER | 1:50.00–2:30.00 (40s) | 36.36s | 1:33.48 | -3.64s |
| S06 | `M1-S06-preuve-404.mp3` | Cap 17 (page 404 'Oups') | 2:30.00–2:55.00 (25s) | 26.61s | 2:09.85 | +1.61s |
| S07 | `M1-S07-nouvelle-url-ok.mp3` | Cap 18 (login sur slug perso) - SLUG À FLOUTER | 2:55.00–3:15.00 (20s) | 14.86s | 2:36.46 | -5.14s |
| S08 | `M1-S08-url-secours.mp3` | Zoom Cap 3 (récap licence, 'Clé de récupération') | 3:15.00–3:50.00 (35s) | 27.59s | 2:51.32 | -7.41s |
| S09 | `M1-S09-dashboard.mp3` | Cap 2 (tableau de bord, score 96/100) | 3:50.00–4:30.00 (40s) | 29.16s | 3:18.90 | -10.84s |
| S10 | `M1-S10-outro.mp3` | face cam (pas de capture) | 4:30.00–4:45.00 (15s) | 17.69s | 3:48.07 | +2.69s |

## Lecture du drift

- Drift positif (+) : la voix-off est plus lente que la cible script. Allonge le plan capture ou mets une pause naturelle.
- Drift négatif (-) : la voix-off est plus rapide. Le plan capture peut être raccourci, ou ajoute un fondu enchaîné.
- Drift cumulé global = écart entre la durée vidéo totale et les 4:45 cibles. À répartir sur les face cam (S01, S10) si tu veux retomber pile.

## Slugs à flouter dans le montage

- S05 (`M1-S05-nouvelle-url.mp3` + capture 4) — l'URL personnalisée affichée par Samaritain.
- S07 (`M1-S07-nouvelle-url-ok.mp3` + capture 18) — la même URL dans la barre d'adresse Chrome.

Mêmes coordonnées que l'IP floutée pour rester cohérent (Gaussian blur, padding 4px).
