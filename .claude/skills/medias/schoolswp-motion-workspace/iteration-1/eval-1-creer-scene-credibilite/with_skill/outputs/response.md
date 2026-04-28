# Scene 6 Credibilite -- Rapport complet

## Diagnostic

### Ce qui existe deja

- **Confirme** : `theme.ts` contient deja le slot `scene6: { start: 4050, duration: 600 }` (20 secondes a 30 fps = 600 frames). Aucune modification de theme.ts necessaire.
- **Confirme** : `texts.ts` contient deja la section `credibility` avec :
  - `founder: "Michael KIHL"`
  - `founderTitle: "Fondateur & expert WordPress education"`
  - `badges` : 3 badges (Depuis 2021, 100+ Contenus publies, 5 Etapes)
  - `ecosystemItems: ["Blog", "Newsletter", "YouTube", "Academy"]`
- **Confirme** : Le composant `TimelineBadge` existe dans le legacy (`video-marketing/src/components/TimelineBadge.tsx`) et gere l'animation scale + fade-in avec stagger par index. Reutilisable directement.
- **Confirme** : Le composant `AnimatedText` existe et gere slide-up + fade-in avec accentPhrase optionnel.
- **Confirme** : `Root.tsx` ne contient pas de Scene6Credibility -- il faut l'enregistrer.
- **Confirme** : Aucun fichier `Scene6Credibility.tsx` n'existe dans `src/compositions/`.
- **Confirme** : Les logos sont dans `public/logos/` (nom-black.svg, nom-black.png, nom-white.svg, nom-white.png). Scene 6 utilise un fond clair (`bgLight`) donc le logo noir serait le bon choix si un logo etait affiche, mais la scene n'en a pas besoin selon le brief.

### Ce qui peut etre reutilise

- `AnimatedText` -- pour le nom du fondateur, le titre, le label ecosysteme
- `TimelineBadge` -- pour les 3 badges (Depuis 2021, 100+, 5 etapes)
- `springSmooth`, `springPunch`, `springGentle` -- springs existantes
- Tous les tokens THEME (couleurs, typographies, stagger, fadeIn)

### Ce qui manque

- Le champ `ecosystemTitle` n'existait pas dans `texts.ts`. **Ajoute** pour centraliser le texte "L'ecosysteme schoolsWP" au lieu de le hardcoder.
- Le fichier `Scene6Credibility.tsx` -- a creer.
- L'enregistrement dans `Root.tsx` -- a ajouter.

### Risques eventuels

- **A verifier** : Les composants `AnimatedText` et `TimelineBadge` sont dans le sous-dossier legacy (`video-marketing/src/components/`). L'import `../components/AnimatedText` suppose que les composants sont dans `src/components/`. Les scenes existantes (Scene2, Scene4, Scene7) utilisent le meme chemin d'import, ce qui signifie soit les composants existent aussi dans `src/components/` (non visible sur le filesystem) soit il y a un alias ou une resolution de module. Le code produit suit exactement le meme pattern d'import que les scenes existantes.
- **A verifier** : Le rendu visuel final (hierarchie, lisibilite, equilibre des espacements) ne peut etre valide qu'en preview dans le studio Remotion.

---

## Plan d'action

1. **Ajouter `ecosystemTitle`** dans `texts.ts` pour centraliser le texte du label ecosysteme
2. **Creer `Scene6Credibility.tsx`** dans `src/compositions/` avec :
   - Fond clair (`THEME.bgLight`)
   - Section haute : nom fondateur (H2) + titre (Body) via `AnimatedText`
   - Ligne d'accent verte horizontale (expansion depuis le centre via `springSmooth`)
   - Section milieu : 3 badges via `TimelineBadge` en ligne, stagger progressif
   - Section basse : label ecosysteme avec accentPhrase "schoolsWP" + 4 items en pills
   - Fade-in scene (0-30 frames), fade-out scene (540-600 frames)
3. **Enregistrer la composition** dans `Root.tsx` avec `durationInFrames={THEME.fps * 20}` (600 frames)
4. **theme.ts** : aucune modification (scene6 deja definie, tous les tokens existent)

---

## Fichiers impactes

### Crees

| Fichier                                  | Role                                            |
| ---------------------------------------- | ----------------------------------------------- |
| `src/compositions/Scene6Credibility.tsx` | Composition scene credibilite (20s, 600 frames) |

### Modifies

| Fichier        | Modification                                                  |
| -------------- | ------------------------------------------------------------- |
| `src/Root.tsx` | Import + `<Composition>` pour Scene6Credibility               |
| `src/texts.ts` | Ajout du champ `ecosystemTitle` dans la section `credibility` |

### Laisses intacts

| Fichier                                | Raison                                                     |
| -------------------------------------- | ---------------------------------------------------------- |
| `src/theme.ts`                         | `scene6` deja defini, aucune nouvelle constante necessaire |
| `src/compositions/Scene4Solutions.tsx` | Scene precedente, non impactee                             |
| `src/compositions/Scene7CTA.tsx`       | Scene suivante, non impactee                               |
| Tous les composants existants          | Reutilises tels quels                                      |

---

## Commandes executees

Aucune commande de build ou de rendu executee. Les fichiers ont ete ecrits dans le dossier outputs uniquement.

---

## Resultat

### Composition creee : Scene6Credibility

- **Duree** : 20 secondes (600 frames @ 30fps)
- **Fond** : `THEME.bgLight` (#FAFBFD)
- **Structure narrative** :
  - **0-2s** : Entree du nom "Michael KIHL" (H2, heading, springPunch via AnimatedText)
  - **0.7s** : Entree du titre fondateur (Body, springPunch via AnimatedText)
  - **0-3s** : Ligne d'accent verte qui s'etend horizontalement (springSmooth, 120px)
  - **0-8s** : 3 badges en stagger (40 frames entre chaque, springPunch via TimelineBadge)
    - "2021 / Depuis"
    - "100+ / Contenus publies"
    - "5 / Etapes -- la methode schoolsWP"
  - **9s** : Label "L'ecosysteme schoolsWP" avec "schoolsWP" en vert accent
  - **10-12s** : 4 pills ecosysteme en stagger (15 frames entre chaque, springGentle)
    - Blog, Newsletter, YouTube, Academy
    - Fond subtle (`THEME.bgSubtle`), bordure discrete
  - **18-20s** : Fade-out progressif

### Patterns d'animation respectes

- **Entree texte** : slide-up (40px) + fade-in via AnimatedText
- **Entree badges** : scale (0.8 -> 1) + fade-in via TimelineBadge / springPunch
- **Accent line** : expansion horizontale depuis le centre via springSmooth
- **Stagger** : delai incremental pour badges (40f) et items ecosysteme (15f)
- **Pulse subtil** : Math.sin() pour respiration douce sur la section ecosysteme

---

## QA

### Branding

- [x] **schoolsWP** bien ecrit partout (WP majuscules) -- dans texts.ts et via accentPhrase
- [x] **Michael KIHL** ecrit correctement (KIHL en majuscules)
- [x] Couleurs conformes a theme.ts -- aucune couleur hardcodee
- [x] Ton visuel schoolsWP respecte (calme, premium, clair)
- [x] Aucun logo utilise (non requis par le brief)

### Technique

- [x] Dimensions correctes (1920x1080) via Composition
- [x] FPS correct (`THEME.fps`) -- jamais hardcode
- [x] Duree correcte (600 frames = 20s via `THEME.fps * 20`)
- [x] Imports coherents avec les scenes existantes (Scene2, Scene4, Scene7)
- [x] Composition enregistree dans Root.tsx
- [x] Textes centralises dans texts.ts -- aucun texte hardcode
- [x] Constantes centralisees dans theme.ts

### Motion

- [x] Hierarchie visuelle claire : fondateur (H2) > badges (stagger) > ecosysteme (H3 + pills)
- [x] Springs coherentes (springSmooth pour accent, springPunch pour badges, springGentle pour items)
- [x] Fade-in/out scene propres (30 frames entree, 60 frames sortie)
- [x] Temps de lecture suffisant (10s fondateur+badges, 10s ecosysteme)
- [x] Pas d'effet cheap ou de surcharge
- [ ] **A verifier** : equilibre visuel des espacements (necessite preview studio)
- [ ] **A verifier** : lisibilite reelle de tous les textes a 1920x1080

### Export

- [x] Nom de fichier propre (`Scene6Credibility.tsx`)
- [x] Convention PascalCase respectee

---

## Modification texts.ts

Un seul champ ajoute a la section `credibility` :

```typescript
ecosystemTitle: "L'ecosysteme schoolsWP",
```

Cela evite de hardcoder le texte dans la composition et respecte la regle absolue du projet : tout texte affiche va dans `texts.ts`.

---

## Suite recommandee

**Prochaine etape prioritaire** : Lancer `npm run studio` et previsualiser la composition Scene6Credibility dans le studio Remotion pour valider :

1. L'equilibre visuel global (espacements, hierarchie)
2. Le timing percu (est-ce que chaque element reste assez longtemps a l'ecran ?)
3. La transition fluide avec Scene 5 (Benefices) et Scene 7 (CTA)
4. La lisibilite sur ecran reel

Si la preview est satisfaisante, integrer Scene6Credibility dans la composition narrative complete (VideoMarketing) en la placant en Sequence apres Scene 5 (Benefices) a la frame 4050 (conforme a `THEME.scene6.start`).
