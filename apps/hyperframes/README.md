# HyperFrames — schoolsWP

Projet de rendu video HTML vers MP4 pour schoolsWP. Moteur : HyperFrames (HeyGen, Apache 2.0).

## Video Production System v1.1

Le dossier `execution-layer/` contient le socle P0 du **schoolsWP Video Production System v1.1 — HyperFrames Execution Layer**.

Pour les vidéos avec parole, cette couche devient la référence pour :
- transcript canonique mot-à-mot ;
- Edit Decision Ledger (EDL) ;
- retiming après montage ;
- cut-silences ;
- revue des erreurs/retakes ;
- Footage Ledger et SHA256 ;
- preflight et tests.

Elle ne remplace pas les règles schoolsWP de preuve, de marque, de validation humaine ou de publication.

Les projets existants sous `recyclage/` restent compatibles et ne sont pas migrés automatiquement.

## Quickstart

Depuis ce dossier (apps/hyperframes/) :

1. Preview live : npx hyperframes preview
2. Rendu MP4 : npx hyperframes render
3. Lint : npx hyperframes lint

Depuis `apps/hyperframes/execution-layer/` :

    npm test
    npm run preflight

Le premier npx telecharge le package hyperframes a la volee (Node >= 22 + FFmpeg requis, tous deux presents).

## Positionnement

Complementaire de apps/video-marketing/ (Remotion). Voir CLAUDE.md pour la regle de routing.

- Remotion : videos structurees, multi-scenes, cours formation
- HyperFrames : intros courtes, overlays sociaux, article vers video 30-60s, shader transitions
- Execution Layer v1.1 : montage temporel, provenance et QA avant composition/rendu

Defaut = Remotion si les deux moteurs peuvent faire le job. Le choix du moteur ne change pas l'obligation d'utiliser la timeline canonique v1.1 lorsqu'un média parlé a été édité.

## Structure

- index.html : composition test minimale (titre anime avec GSAP)
- hyperframes.json : config projet
- execution-layer/ : contrats temporels, scripts, validateurs et fixtures v1.1
- compositions/ : sous-compositions
- assets/ : medias sources
- renders/ : sorties MP4 (gitignored)

## Skills Claude Code

Les skills HyperFrames externes existants restent disponibles dans .claude/skills/external-hyperframes/.

Les skills v1.1 propres à schoolsWP sont canoniques dans :
`execution-layer/skills/canonical/`.

Ils peuvent être synchronisés vers Claude Code et Codex avec :

    cd apps/hyperframes/execution-layer
    npm run skills:sync

## Doc

- Site : hyperframes.heygen.com
- Repo : github.com/heygen-com/hyperframes
- Catalog : hyperframes.heygen.com/catalog
