# apps/hyperframes — Projet HyperFrames schoolsWP

Projet de rendu vidéo HTML vers MP4 via HyperFrames (Apache 2.0, HeyGen). Voir github.com/heygen-com/hyperframes.

## Positionnement dans le stack vidéo schoolsWP

- apps/video-marketing/ (Remotion, React) pour vidéos structurées, multi-scènes, cours formation TutorLMS
- apps/hyperframes/ (ici, HTML + CSS + GSAP) pour intros courtes, overlays sociaux, recyclage article vers vidéo 30-60s, shader transitions

En cas de doute, défaut = Remotion (deja en prod, governance theme.ts et texts.ts).

## Skills installees

Emplacement : .claude/skills/external-hyperframes/ (5 skills)

- hyperframes : creer et editer compositions HTML
- hyperframes-cli : commandes CLI (init, lint, preview, render, tts)
- hyperframes-registry : installer blocks et components via registry
- website-to-hyperframes : capturer URL vers video
- gsap : animations GSAP

Invoquer via slash commands (apres reload session) : /hyperframes, /hyperframes-cli, /hyperframes-registry, /website-to-hyperframes, /gsap.

## Commandes (a lancer depuis apps/hyperframes/)

- npx hyperframes preview : preview browser live reload
- npx hyperframes render : rendu MP4 vers renders/
- npx hyperframes lint : valider compositions
- npx hyperframes lint --verbose : include info-level
- npx hyperframes add nom-bloc : ajouter bloc du catalogue
- npx hyperframes docs topic : doc locale (topics : data-attributes, gsap, compositions, rendering, examples, troubleshooting)

## Structure

- index.html : composition principale (root timeline)
- compositions/ : sous-compositions (referencees via data-composition-src)
- compositions/components/ : snippets reutilisables
- assets/ : medias (videos, images, audio)
- recyclage/<slug-article>/ : sources des compositions par article (16x9 master + variants 1x1/9x16/2x3 + build_variants.py + narrate.py)
- renders/<slug-article>/ : sorties MP4 par article (gitignored). Miroir de recyclage/<slug>/
- renders/intros/ : sorties MP4 des intros generiques schoolsWP (non rattachees a un article)
- hyperframes.json : config projet (registry + paths)

## Convention outputs

Toute commande npx hyperframes render doit ecrire dans renders/<slug-article>/<filename>.mp4 (jamais a la racine de renders/). Pour une intro generique : renders/intros/<filename>.mp4. Le slug doit matcher le dossier source dans recyclage/.

## Regles cles

1. Tout element temporise doit avoir data-start, data-duration, data-track-index
2. Element avec timing doit avoir class="clip" (controle visibilite framework)
3. Timelines paused, enregistres sur window.__timelines[composition-id]
4. Videos en muted plus audio separe pour le son
5. Sous-compositions via data-composition-src="compositions/file.html"
6. Logique deterministe uniquement, pas de Date.now(), Math.random(), fetch reseau

## Linting apres edition

Lancer npx hyperframes lint apres toute modification d un .html. Corriger toutes les erreurs avant de considerer la tache finie.

## Prerequis

- Node.js >= 22 (installe : v24.14.1)
- FFmpeg (installe via winget Gyan.FFmpeg)

## Doc

- Local : npx hyperframes docs topic
- Full : hyperframes.heygen.com/introduction
- Index machine-readable : hyperframes.heygen.com/llms.txt
