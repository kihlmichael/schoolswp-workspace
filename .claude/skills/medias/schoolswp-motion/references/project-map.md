# Project Map — video-marketing schoolsWP

> Racine : `D:\VS Code\CLAUDE CODE\projects\schoolswp\apps\video-marketing\`

## Structure cible

```
video-marketing/
├── src/
│   ├── index.ts              # Point d'entree — registerRoot()
│   ├── Root.tsx               # Registre des compositions Remotion
│   ├── theme.ts               # Constantes : couleurs, typos, springs, timeline
│   ├── texts.ts               # Contenu textuel de toutes les scenes
│   ├── compositions/          # Compositions Remotion (1 fichier = 1 video)
│   ├── components/            # Composants reutilisables (AnimatedText, etc.)
│   ├── hooks/                 # Hooks custom Remotion
│   └── lib/                   # Utilitaires et helpers
│
├── public/
│   ├── logos/                 # Assets logo (SVG + PNG, white + black)
│   ├── audio/                 # Musiques et SFX
│   ├── images/                # Images et illustrations
│   └── fonts/                 # Polices personnalisees (reserve — Google Fonts utilise)
│
├── scripts/
│   ├── render-all.sh          # Script de render batch
│   ├── render-one.sh          # Render d'une composition specifique
│   └── qa-checklist.md        # Checklist QA imprimable
│
├── out/
│   ├── previews/              # Rendus de test / validation
│   ├── finals/                # Versions validees
│   └── archive/               # Anciennes versions
│
├── docs/
│   ├── brand-video-brief.md   # Brief creatif par video
│   ├── naming-convention.md   # Conventions de nommage
│   └── render-log.md          # Journal des rendus
│
├── package.json
└── tsconfig.json
```

> **Etat actuel** : certains dossiers de la structure cible n'existent pas encore
> (`hooks/`, `lib/`, `docs/`, `out/previews/`, `out/finals/`, `out/archive/`,
> `scripts/render-one.sh`, `scripts/qa-checklist.md`).
> Les creer au besoin, progressivement — pas de migration massive sans plan.

## Compositions existantes

### Enregistrees dans Root.tsx

| ID             | Fichier                           | Duree     | Description                                   |
| -------------- | --------------------------------- | --------- | --------------------------------------------- |
| BrandIntro     | `compositions/BrandIntro.tsx`     | 5s (150f) | Logo reveal + tagline animee                  |
| BrandOutroA    | `compositions/BrandOutroA.tsx`    | 5s (150f) | Ligne fluide → logo → slogan                  |
| BrandOutroB    | `compositions/BrandOutroB.tsx`    | 6s (180f) | Particules convergentes → logo                |
| BrandOutroC    | `compositions/BrandOutroC.tsx`    | 5s (150f) | Pulse rings → logo → URL                      |
| BrandOutroCPro | `compositions/BrandOutroCPro.tsx` | 5s (150f) | Grille + particules + texte lettre par lettre |

### Fichiers de composition non enregistres

| Fichier                               | Duree prevue | Description                   |
| ------------------------------------- | ------------ | ----------------------------- |
| `compositions/Scene2Presentation.tsx` | 25s          | Presentation logo + mots-cles |
| `compositions/Scene4Solutions.tsx`    | 35s          | 5 blocs solutions stagger     |
| `compositions/Scene7CTA.tsx`          | 15s          | Call-to-action vert           |

> Ces scenes font partie de la video narrative complete (VideoMarketing)
> qui est dans le sous-dossier legacy `video-marketing/`.

## Composants reutilisables

Situes dans `video-marketing/src/components/` (sous-dossier legacy) :

| Composant       | Role                             | Props cles                                   |
| --------------- | -------------------------------- | -------------------------------------------- |
| `AnimatedText`  | Texte spring + slide-up + accent | text, accentPhrase, fontSize, delay, heading |
| `SolutionBlock` | Bloc avec barre verte + stagger  | title, desc, index                           |
| `CTAButton`     | Bouton CTA avec pulse            | text, delay                                  |
| `ProblemCard`   | Carte probleme                   | (scene 3)                                    |
| `BeforeAfter`   | Comparaison avant/apres          | (scene 5)                                    |
| `TimelineBadge` | Badge credibilite                | (scene 6)                                    |

> **A terme** : migrer les composants utilises vers `src/components/` (racine)
> pour qu'ils soient accessibles sans passer par le sous-dossier legacy.

## Fichiers source de verite

| Fichier        | Role                               | Quand le lire                              |
| -------------- | ---------------------------------- | ------------------------------------------ |
| `src/theme.ts` | Couleurs, typos, springs, timeline | Toujours, en debut de session              |
| `src/texts.ts` | Tout le contenu textuel            | Quand on touche au texte ou cree une scene |
| `src/Root.tsx` | Compositions enregistrees          | Quand on cree/supprime une composition     |

## Assets actuels

### Logos (`public/logos/`)

| Fichier         | Format | Fond   | Taille |
| --------------- | ------ | ------ | ------ |
| `nom-white.svg` | SVG    | Sombre | 5.0K   |
| `nom-white.png` | PNG    | Sombre | 11K    |
| `nom-black.svg` | SVG    | Clair  | 5.0K   |
| `nom-black.png` | PNG    | Clair  | 11K    |

### Dossiers reserves (vides)

- `public/fonts/` — Google Fonts utilise via `@remotion/google-fonts`
- `public/images/` — reserve
- `public/audio/` — reserve

## Exports existants (`out/`)

| Fichier                 | Composition source |
| ----------------------- | ------------------ |
| `brand-intro.mp4`       | BrandIntro         |
| `brand-outro-a.mp4`     | BrandOutroA        |
| `brand-outro-b.mp4`     | BrandOutroB        |
| `brand-outro-c.mp4`     | BrandOutroC        |
| `brand-outro-c-pro.mp4` | BrandOutroCPro     |

> Convention cible : `schoolsWP-brand-intro-v1.mp4`
> (voir `references/naming-conventions.md`)

## Dependances

| Package                  | Version | Role                        |
| ------------------------ | ------- | --------------------------- |
| `remotion`               | ^4.0.0  | Framework video React       |
| `@remotion/cli`          | ^4.0.0  | CLI render/studio           |
| `@remotion/google-fonts` | ^4.0.0  | Nunito Sans + Roboto        |
| `@remotion/transitions`  | ^4.0.0  | Transitions entre sequences |
| `react`                  | ^18.3.0 | UI composants               |
| `typescript`             | ^5.5.0  | Typage                      |

## Commandes

| Commande                                 | Action                                          |
| ---------------------------------------- | ----------------------------------------------- |
| `npm run studio`                         | Lance le studio Remotion (preview live)         |
| `npm run render`                         | Render VideoMarketing → out/video-marketing.mp4 |
| `npx remotion render <ID> out/<nom>.mp4` | Render une composition specifique               |
| `bash scripts/render-all.sh`             | Render batch                                    |
