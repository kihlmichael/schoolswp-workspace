---
name: remotion
description: |
  Construit des vidéos programmatiques avec Remotion (React) : compositions, animations frame-by-frame, gestion audio/vidéo/images, transitions, séquences. Sortie pour `apps/video-marketing/` (cours TutorLMS, vidéos multi-scènes structurelles).
  Utilise ce skill quand l'utilisateur dit : "Remotion", "vidéo React", "composition vidéo programmatique", "animation frame-by-frame", "rendu vidéo schoolsWP", ou pour toute vidéo structurelle multi-scènes dans `apps/video-marketing/`.
  NE PAS utiliser pour : intros courtes ≤30s ou overlays sociaux (utiliser `external-hyperframes/`), vidéos AI avec avatar (utiliser `external-heygen/`), ou cas avancés FFmpeg/captions/3D/voiceover (voir `remotion-best-practices`).
---

# Remotion - Video programmatique React

Remotion permet de creer des videos en React, rendues frame-by-frame. Toute la doc officielle : https://www.remotion.dev/docs/

## Structure projet

Le fichier racine est `src/Root.tsx` :

```tsx
import { Composition } from "remotion";
import { MyComp } from "./MyComp";

export const Root: React.FC = () => {
  return (
    <Composition
      id="MyComp"
      component={MyComp}
      durationInFrames={120}
      width={1920}
      height={1080}
      fps={30}
      defaultProps={{}}
    />
  );
};
```

**Valeurs par defaut** : 1920x1080, 30fps, id="MyComp".
`defaultProps` doit correspondre aux props du composant.

## Hooks essentiels

- `useCurrentFrame()` : frame courante (commence a 0)
- `useVideoConfig()` : `{fps, durationInFrames, height, width}`

```tsx
const frame = useCurrentFrame();
const { fps, durationInFrames, height, width } = useVideoConfig();
```

## Composants media

### Video

```tsx
import { OffthreadVideo } from "remotion";
<OffthreadVideo
  src="https://example.com/video.mp4"
  style={{ width: "100%" }}
/>;
```

Props : `startFrom` (trim debut), `endAt` (limite duree), `volume` (0-1).

### Image

```tsx
import { Img } from "remotion";
<Img src="https://example.com/image.png" style={{ width: "100%" }} />;
```

### GIF anime

```tsx
import { Gif } from "@remotion/gif";
<Gif src="https://example.com/animation.gif" style={{ width: "100%" }} />;
```

Necessite le package `@remotion/gif`.

### Audio

```tsx
import { Audio } from "remotion";
<Audio src="https://example.com/audio.mp3" />;
```

Props : `startFrom`, `endAt`, `volume` (0-1).

### Assets locaux

Utiliser `staticFile()` pour les fichiers dans `public/` :

```tsx
import { Audio, staticFile } from "remotion";
<Audio src={staticFile("audio.mp3")} />;
```

## Layout et sequencement

### AbsoluteFill (superposition)

```tsx
import { AbsoluteFill } from "remotion";
<AbsoluteFill>
  <AbsoluteFill>
    <div>Arriere-plan</div>
  </AbsoluteFill>
  <AbsoluteFill>
    <div>Premier plan</div>
  </AbsoluteFill>
</AbsoluteFill>;
```

### Sequence (apparition differee)

```tsx
import { Sequence } from "remotion";
<Sequence from={10} durationInFrames={20}>
  <div>Apparait apres 10 frames</div>
</Sequence>;
```

- `from` : frame d'apparition (negatif = coupe le debut)
- `durationInFrames` : duree d'affichage
- `useCurrentFrame()` dans un enfant repart a 0 depuis le debut de la Sequence

### Series (elements sequentiels)

```tsx
import { Series } from "remotion";
<Series>
  <Series.Sequence durationInFrames={20}>
    <div>Premiere partie</div>
  </Series.Sequence>
  <Series.Sequence durationInFrames={30}>
    <div>Deuxieme partie</div>
  </Series.Sequence>
  <Series.Sequence durationInFrames={30} offset={-8}>
    <div>Troisieme partie (decalee de -8 frames)</div>
  </Series.Sequence>
</Series>;
```

`offset` decale le debut par rapport a la fin du precedent.

### TransitionSeries (transitions entre elements)

```tsx
import {
  linearTiming,
  springTiming,
  TransitionSeries,
} from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { wipe } from "@remotion/transitions/wipe";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <Fill color="blue" />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    timing={springTiming({ config: { damping: 200 } })}
    presentation={fade()}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <Fill color="black" />
  </TransitionSeries.Sequence>
</TransitionSeries>;
```

L'ordre est important : `Transition` doit etre entre deux `Sequence`.

## Animation

### interpolate()

```tsx
import { interpolate } from "remotion";

const value = interpolate(frame, [0, 100], [0, 1], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```

Toujours ajouter `extrapolateLeft: 'clamp'` et `extrapolateRight: 'clamp'` par defaut.

### spring()

```tsx
import { spring } from "remotion";

const value = spring({
  fps,
  frame,
  config: { damping: 200 },
});
```

### random() (deterministe)

```tsx
import { random } from "remotion";
const value = random("my-seed"); // 0-1, deterministe
```

`Math.random()` est INTERDIT. Toujours utiliser `random()` avec une seed statique.

## Regles fondamentales

1. **Determinisme** : le code React DOIT etre deterministe (meme input = meme output)
2. **Pas d'interactivite** : pas de onClick, onHover, useState pour l'interactivite
3. **Pas d'effets** : eviter useEffect, les calculs doivent etre purs base sur la frame
4. **Animations par frame** : utiliser `interpolate()` ou `spring()` avec `useCurrentFrame()`
5. **Pas de Math.random()** : utiliser `random('seed')` de remotion
6. **Composants purs** : pas de side effects ni de data fetching

## Remotion vs React classique

| Aspect            | Remotion                       | React classique         |
| ----------------- | ------------------------------ | ----------------------- |
| State             | `useCurrentFrame()`            | `useState()`            |
| Animation         | `interpolate()` / `spring()`   | CSS transitions / libs  |
| Input utilisateur | Aucun (props a la composition) | onClick, onChange, etc. |
| Effets            | Aucun (calculs purs)           | `useEffect()`           |
| Rendu             | Frame-by-frame                 | Event-driven            |
