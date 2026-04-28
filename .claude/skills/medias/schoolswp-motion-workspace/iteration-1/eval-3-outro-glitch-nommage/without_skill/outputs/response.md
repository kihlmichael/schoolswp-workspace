# Outro Final V3 New -- Glitch + Neon Particles

## Fichiers crees/modifies

### 1. `outro-final-v3-new.tsx` (nouveau)

Chemin dans le projet : `src/compositions/outro-final-v3-new.tsx`

Composition Remotion de 5 secondes (150 frames a 30fps) avec :

**Effet Glitch sur le logo schoolsWP.com :**

- Aberration chromatique RGB (3 couches du logo decalees avec hue-rotate)
- Deplacements aleatoires X/Y, skew et scale sur le logo
- Barres de glitch horizontales colorees (slices) en mode `screen`
- Intensite variable : pic fort au debut (frames 20-55), stabilisation progressive, micro-burst a frame 110
- Screen shake global lie a l'intensite du glitch
- Bruit/static overlay avec seed variable par frame
- Scanlines CRT en arriere-plan
- Background flicker vert lors des pics de glitch

**Particules neon explosives :**

- 80 particules (vague 1) + 40 particules (vague 2, decalee) = 120 particules
- 6 couleurs neon : vert brand, rose accent, cyan, jaune, orange, lavande
- Explosion radiale depuis le centre (960, 540)
- Deceleration progressive, formes variees (cercles, carres, losanges)
- Glow neon via `boxShadow` sur chaque particule
- Rotation individuelle par particule
- Fade-in/fade-out par particule selon sa duree de vie

**Autres elements :**

- Glow neon derriere le logo (gradient vert + rose, breathing)
- Ligne verte accent animee (eased)
- URL "schoolsWP.com" en reveal lettre par lettre (spring) avec micro-glow neon aleatoire sur certains caracteres
- Vignette sombre aux bords
- Fade out global sur les 10 dernieres frames

### 2. `Root.tsx` (modifie)

- Import de `OutroFinalV3New` depuis `./compositions/outro-final-v3-new`
- Ajout d'une `<Composition>` avec id `OutroFinalV3New`, 5 secondes, 1920x1080

## Timeline de l'animation (5s / 150 frames)

| Phase | Frames  | Description                                                  |
| ----- | ------- | ------------------------------------------------------------ |
| 1     | 0-30    | Particules neon explosent depuis le centre                   |
| 2     | 20-60   | Logo apparait avec glitch intense (RGB split, shake, slices) |
| 3     | 60-100  | Glitch se stabilise, logo tient                              |
| 4     | 80-120  | Ligne verte + URL apparaissent lettre par lettre             |
| 5     | 120-150 | Hold + micro-burst glitch a 110 + fade out                   |

## Notes techniques

- Utilise `random()` de Remotion pour un rendu deterministe (pas de Math.random)
- Utilise `spring()` pour l'entree du logo et le reveal des caracteres
- Utilise `interpolate()` avec clamp pour toutes les animations
- Respecte le theme existant (`THEME.bgDark`, `THEME.primary`, `THEME.accent`, etc.)
- Logo : `logos/nom-white.svg` (fichier existant dans `public/logos/`)
- Nommage "schoolsWP.com" respecte (WP majuscule)
