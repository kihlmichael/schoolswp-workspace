# HyperFrames — schoolsWP

Projet de rendu video HTML vers MP4 pour schoolsWP. Moteur : HyperFrames (HeyGen, Apache 2.0).

## Quickstart

Depuis ce dossier (apps/hyperframes/) :

1. Preview live : npx hyperframes preview
2. Rendu MP4 : npx hyperframes render
3. Lint : npx hyperframes lint

Le premier npx telecharge le package hyperframes a la volee (Node >= 22 + FFmpeg requis, tous deux presents).

## Positionnement

Complementaire de apps/video-marketing/ (Remotion). Voir CLAUDE.md pour la regle de routing.

- Remotion : videos structurees, multi-scenes, cours formation
- HyperFrames : intros courtes, overlays sociaux, article vers video 30-60s, shader transitions

Defaut = Remotion si les deux peuvent faire le job.

## Structure

- index.html : composition test minimale (titre anime avec GSAP)
- hyperframes.json : config projet
- compositions/ : sous-compositions
- assets/ : medias sources
- renders/ : sorties MP4 (gitignored)

## Skills Claude Code

5 skills installees dans .claude/skills/external-hyperframes/ : hyperframes, hyperframes-cli, hyperframes-registry, website-to-hyperframes, gsap.

Plus 3 skills LiveAvatar dans .claude/skills/external-liveavatar/ (pour quand la licence HeyGen sera prise).

## Doc

- Site : hyperframes.heygen.com
- Repo : github.com/heygen-com/hyperframes
- Catalog : hyperframes.heygen.com/catalog
