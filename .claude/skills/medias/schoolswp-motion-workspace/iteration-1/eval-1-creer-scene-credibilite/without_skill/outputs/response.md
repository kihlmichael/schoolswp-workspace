# Scene 6 -- Credibilite : implementation

## Fichiers crees / modifies

### 1. `src/compositions/Scene6Credibility.tsx` (NOUVEAU)

Composition Remotion de 600 frames (20 secondes @ 30fps) structuree en 5 phases :

| Phase | Frames  | Duree  | Contenu                                                                                                                                                |
| ----- | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | 0-60    | 0-2s   | Fond sombre, avatar fondateur (cercle vert + initiales MK), nom "Michael KIHL" et titre "Fondateur & expert WordPress education" avec spring + fade-in |
| 2     | 60-180  | 2-6s   | 3 badges en stagger avec spring punch : "2021 / Depuis", "100+ / Contenus publies", "5 / Etapes -- la methode schoolsWP"                               |
| 3     | 180-360 | 6-12s  | Titre "L'ecosysteme schoolsWP" + ligne verte + 4 piliers en stagger (Blog, Newsletter, YouTube, Academy) avec icones dans des carres arrondis          |
| 4     | 360-540 | 12-18s | Hold / respiration -- tous les elements visibles                                                                                                       |
| 5     | 540-600 | 18-20s | Fade-out global                                                                                                                                        |

Elements visuels :

- Fond `THEME.bgDark` (#12111F) pour contraste
- Avatar fondateur : cercle vert avec initiales "MK" (pas de photo requise)
- Badges : valeur en `THEME.primary` (#00D400) + label en `THEME.textLight`
- Ligne verte animee entre badges et ecosysteme
- Glow radial subtil derriere l'avatar
- Piliers ecosysteme : icones emoji dans des carres `THEME.greenSubtle`
- Toutes les donnees viennent de `TEXTS.credibility` (deja present dans `texts.ts`)

Animations :

- `spring()` avec `THEME.springSmooth` pour le fondateur
- `spring()` avec `THEME.springPunch` pour les badges (plus percutant)
- `spring()` avec `THEME.springSmooth` pour les piliers ecosysteme
- Fade-in/out standard via `interpolate`

### 2. `src/Root.tsx` (MODIFIE)

Ajout de :

- Import `Scene6Credibility`
- Nouvelle `<Composition>` avec `id="Scene6Credibility"`, duree `THEME.scene6.duration` (600 frames = 20s)

## Fichiers NON modifies (deja corrects)

- **`src/theme.ts`** : `scene6: { start: 4050, duration: 600 }` existait deja (20s a 30fps)
- **`src/texts.ts`** : `TEXTS.credibility` existait deja avec fondateur, badges et ecosystemItems

## Position dans la timeline globale

La scene s'insere en position 6 dans la sequence video :

1. Hook (20s)
2. Presentation (25s)
3. Problemes (35s)
4. **Solutions (35s)**
5. Benefices (20s)
6. **Credibilite (20s)** <-- cette scene
7. CTA (15s)

Note : dans le theme, la scene 6 est deja prevue apres la scene 5 (Benefices). Pour l'integrer dans la composition finale `VideoMarketing`, il faudra utiliser `<Sequence>` dans une composition parent qui enchaine les 7 scenes. La composition `Scene6Credibility` est ici enregistree comme composition standalone previewable dans le Remotion Studio.
