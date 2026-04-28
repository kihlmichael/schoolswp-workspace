# Brand Kit schoolsWP — Reference rapide

> Source de verite : `src/theme.ts`. En cas de divergence, theme.ts fait autorite.

## Couleurs

| Token            | Hex                    | Usage                                   |
| ---------------- | ---------------------- | --------------------------------------- |
| `primary`        | #00D400                | Vert neon — accents, CTA, lignes, glows |
| `primaryDark`    | #00A100                | Vert fonce — hover, variantes           |
| `accent`         | #E668D4                | Magenta — accent secondaire rare        |
| `bgLight`        | #FAFBFD                | Fond clair — scenes de contenu          |
| `bgSubtle`       | #F4F6FB                | Fond gris-bleu leger                    |
| `bgDark`         | #12111F                | Fond sombre — intros/outros brand       |
| `bgDarkAlt`      | #212121                | Fond sombre alternatif                  |
| `textPrimary`    | #212121                | Texte principal fond clair              |
| `textSecondary`  | #57556D                | Texte secondaire                        |
| `textLight`      | #8F8DA5                | Texte leger                             |
| `textWhite`      | #FAFBFD                | Texte sur fond sombre                   |
| `gridColor`      | rgba(255,255,255,0.04) | Grille sur fond sombre                  |
| `gridColorLight` | rgba(0,0,0,0.035)      | Grille sur fond clair                   |
| `red`            | #B82105                | Rouge — problemes, alertes              |
| `redSubtle`      | rgba(184,33,5,0.12)    | Rouge transparent                       |
| `greenSubtle`    | rgba(0,212,0,0.12)     | Vert transparent                        |

## Typographies

| Role     | Police      | Token THEME   |
| -------- | ----------- | ------------- |
| Headings | Nunito Sans | `headingFont` |
| Body     | Roboto      | `bodyFont`    |

### Echelle de tailles

| Token             | Taille | Usage                     |
| ----------------- | ------ | ------------------------- |
| `fontSizeHero`    | 64px   | Titres principaux, hooks  |
| `fontSizeH2`      | 48px   | Sous-titres de scene      |
| `fontSizeH3`      | 36px   | Titres de blocs           |
| `fontSizeBody`    | 28px   | Texte courant             |
| `fontSizeCaption` | 22px   | Legendes, URLs            |
| `fontSizeSmall`   | 18px   | Mentions legales, credits |

Line height : 1.4

## Spring Configs

| Config         | Damping | Mass | Stiffness | Usage                                  |
| -------------- | ------- | ---- | --------- | -------------------------------------- |
| `springSmooth` | 200     | 1    | 80        | Logos, elements brand, entrees fluides |
| `springPunch`  | 120     | 0.8  | 150       | CTA, textes importants, impact         |
| `springGentle` | 200     | 1.2  | 60        | Sous-titres, transitions douces        |

## Timing (frames @ 30fps)

| Constante          | Valeur    | Equivalent |
| ------------------ | --------- | ---------- |
| `fadeInDuration`   | 20 frames | 0.67s      |
| `staggerDelay`     | 15 frames | 0.50s      |
| `transitionFrames` | 30 frames | 1.00s      |

## Timeline narrative

| Scene                  | Start | Duration | Secondes | Contenu                    |
| ---------------------- | ----- | -------- | -------- | -------------------------- |
| Scene 1 (Hook)         | 0     | 600      | 0-20s    | Accroche emotionnelle      |
| Scene 2 (Presentation) | 600   | 750      | 20-45s   | Logo + tagline + mots-cles |
| Scene 3 (Problemes)    | 1350  | 1050     | 45-80s   | 5 pain points              |
| Scene 4 (Solutions)    | 2400  | 1050     | 80-115s  | 5 solutions schoolsWP      |
| Scene 5 (Benefices)    | 3450  | 600      | 115-135s | Avant/Apres                |
| Scene 6 (Credibilite)  | 4050  | 600      | 135-155s | Fondateur + badges         |
| Scene 7 (CTA)          | 4650  | 450      | 155-170s | Appel a l'action           |

Total : 5100 frames = 2min50 @ 30fps

## Logos disponibles

| Fichier                      | Format | Fond   |
| ---------------------------- | ------ | ------ |
| `public/logos/nom-white.svg` | SVG    | Sombre |
| `public/logos/nom-white.png` | PNG    | Sombre |
| `public/logos/nom-black.svg` | SVG    | Clair  |
| `public/logos/nom-black.png` | PNG    | Clair  |

## Specifications video

- Resolution : 1920x1080
- FPS : 30
- Format : MP4
- Sortie : `out/`
