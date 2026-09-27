# apps/hyperframes — Projet HyperFrames schoolsWP

Projet de rendu vidéo HTML vers MP4 via HyperFrames (Apache 2.0, HeyGen). Voir github.com/heygen-com/hyperframes.

## Video Production System v1.1

Pour tout média parlé qui subit un montage, lire d'abord :

`apps/hyperframes/execution-layer/README.md`

Règle v1.1 :
- l'original reste intact ;
- le montage est décrit par un EDL canonique ;
- après une coupe, tout timing aval utilise le transcript retimé ;
- sourceStart/sourceEnd conservent la provenance originale ;
- les erreurs de parole ambiguës restent review-gated ;
- aucune composition HyperFrames ne doit utiliser des timestamps devenus obsolètes.

Le Control Plane schoolsWP reste prioritaire : Evidence Ledger, Brand Kit, Real UI First, Human Gates, publication et boucle LEARNED ne sont pas remplacés par l'Execution Layer.

## Positionnement dans le stack vidéo schoolsWP

- apps/video-marketing/ (Remotion, React) pour vidéos structurées, multi-scènes, cours formation TutorLMS
- apps/hyperframes/ (ici, HTML + CSS + GSAP) pour intros courtes, overlays sociaux, recyclage article vers vidéo 30-60s, shader transitions
- apps/hyperframes/execution-layer/ pour montage temporel, provenance et QA reproductible

En cas de doute sur le moteur visuel, défaut = Remotion (deja en prod, governance theme.ts et texts.ts).
En cas de média parlé édité, l'Execution Layer v1.1 s'applique quel que soit le moteur de rendu final.

## Skills installees

Emplacement : .claude/skills/external-hyperframes/ (skills externes HyperFrames existants).

- hyperframes : creer et editer compositions HTML
- hyperframes-cli : commandes CLI (init, lint, preview, render, tts)
- hyperframes-registry : installer blocks et components via registry
- website-to-hyperframes : capturer URL vers video
- gsap : animations GSAP
- hyperframes-media : preprocess assets (Kokoro TTS, Whisper, u2net background removal).
- remotion-to-hyperframes : porter une composition Remotion existante vers HyperFrames, uniquement sur demande explicite.

Skills canoniques schoolsWP v1.1 :

- execution-layer/skills/canonical/animate
- execution-layer/skills/canonical/swp-cut-silences
- execution-layer/skills/canonical/swp-cut-mistakes
- execution-layer/skills/canonical/swp-video-preflight

Synchronisation locale Claude/Codex :

    cd apps/hyperframes/execution-layer
    npm run skills:sync
    npm run skills:check

## Commandes (a lancer depuis apps/hyperframes/)

- npx hyperframes preview : preview browser live reload
- npx hyperframes render : rendu MP4 vers renders/
- npx hyperframes lint : valider compositions
- npx hyperframes lint --verbose : include info-level
- npx hyperframes add nom-bloc : ajouter bloc du catalogue
- npx hyperframes docs topic : doc locale

Execution Layer :

    cd execution-layer
    npm test
    npm run preflight
    npm run smoke

## Structure

- index.html : composition principale (root timeline)
- execution-layer/ : Video Production System v1.1 P0
- compositions/ : sous-compositions
- compositions/components/ : snippets reutilisables
- assets/ : medias
- recyclage/<slug-article>/ : projets historiques/compatibles
- renders/<slug-article>/ : sorties MP4
- hyperframes.json : config projet

## Convention outputs

Toute commande npx hyperframes render doit ecrire dans renders/<slug-article>/<filename>.mp4.
Pour une intro generique : renders/intros/<filename>.mp4.

## Regles cles

1. Tout element temporise doit avoir data-start, data-duration, data-track-index.
2. Element avec timing doit avoir class="clip".
3. Timelines paused, enregistres sur window.__timelines[composition-id].
4. Videos en muted plus audio separe pour le son.
5. Sous-compositions via data-composition-src="compositions/file.html".
6. Logique deterministe uniquement, pas de Date.now(), Math.random(), fetch reseau.
7. Un montage média invalide les anciens timings : utiliser transcript.json + edit-decisions.json v1.1.
8. UI_CAPTURE exige une vraie capture vérifiée ; ne pas inventer une interface WordPress.
9. Un PASS technique ne remplace jamais une validation humaine schoolsWP.

## Linting apres edition

Lancer npx hyperframes lint apres toute modification d un .html. Corriger toutes les erreurs avant de considerer la tache finie.

## Prerequis

- Node.js >= 22
- FFmpeg

## Doc

- Local : npx hyperframes docs topic
- Full : hyperframes.heygen.com/introduction
- Index machine-readable : hyperframes.heygen.com/llms.txt
