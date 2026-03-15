# Plan : Vidéo intro YouTube schoolsWP avec Remotion (85s)

## Contexte

Le script YouTube intro est prêt dans `docs/youtube-intro-schoolswp.md` (85s, 20 plans avec timecodes). Le projet `video-marketing/` fournit des composants réutilisables (AnimatedText, CTAButton) et un thème brand kit complet. On crée un **nouveau projet `youtube-intro/`** car la nature est différente : template d'overlays motion graphics destiné à être composité sur du footage réel (facecam + captures écran), pas une vidéo autonome.

## Approche

Projet Remotion autonome `youtube-intro/`. Deux compositions :
1. **YouTubeIntroFull** (85s) — version longue
2. **YouTubeIntroOverlays** (85s) — uniquement les overlays (fond transparent) pour compositing

Les plans facecam/capture/b-roll sont rendus avec un fond coloré + label indiquant le type de plan (repère visuel pour le montage). Les overlays animés (textes écran, lower thirds, titres plein écran, CTA, sous-titres) sont les vrais éléments motion graphics.

## Structure du projet

```
youtube-intro/
├── public/
│   └── logo-schoolswp.svg          (copié depuis brand-reveal)
├── src/
│   ├── index.ts                     registerRoot
│   ├── Root.tsx                     2 Compositions (Full + Overlays)
│   ├── YouTubeIntro.tsx             Composant principal (séquencement 20 plans)
│   ├── theme.ts                     Réutilise la même palette que video-marketing
│   ├── texts.ts                     Contenu textuel (sous-titres + textes écran)
│   ├── timeline.ts                  Tableau des 20 plans avec timecodes/types/durées
│   ├── components/
│   │   ├── AnimatedText.tsx         Copié de video-marketing (identique)
│   │   ├── LowerThird.tsx           Bandeau nom + titre (slide-in gauche)
│   │   ├── FullScreenTitle.tsx      Titre plein écran (pattern interrupts)
│   │   ├── OverlayBadge.tsx         Badge overlay (①SEO, ②Performance, ③Automatisation)
│   │   ├── SubtitleBar.tsx          Sous-titre animé (fond semi-transparent)
│   │   ├── SubscribeButton.tsx      Bouton Subscribe YouTube animé
│   │   ├── CTAButton.tsx            Copié de video-marketing
│   │   └── ShotIndicator.tsx        Indicateur type de plan (facecam/capture/b-roll)
│   └── scenes/
│       ├── Shot01Hook.tsx           0:00–0:02 Facecam serré
│       ├── Shot02Proof.tsx          0:02–0:05 Capture PageSpeed
│       ├── Shot03Intro.tsx          0:05–0:09 Facecam + lower third
│       ├── Shot04Audience.tsx       0:09–0:15 Facecam + highlights profils
│       ├── Shot05PatternInt1.tsx    0:15–0:18 Titre plein écran "3 leviers"
│       ├── Shot06SEO.tsx            0:18–0:26 Facecam + badge ①SEO
│       ├── Shot07Perf.tsx           0:26–0:33 Capture + badge ②Performance
│       ├── Shot08Auto.tsx           0:33–0:41 Facecam + badge ③Automatisation
│       ├── Shot09PatternInt2.tsx    0:41–0:45 B-roll + titre "Moins de technique"
│       ├── Shot10Formats.tsx        0:45–0:50 Facecam plan large
│       ├── Shot11Tuto.tsx           0:50–0:55 Capture + overlay "Tutoriels"
│       ├── Shot12Comparatif.tsx     0:55–0:59 Capture + overlay "Tests·Comparatifs"
│       ├── Shot13Affirm.tsx         0:59–1:02 Facecam serré
│       ├── Shot14PatternInt3.tsx    1:02–1:05 Titre plein écran "Testé sur le terrain"
│       ├── Shot15Credibility.tsx    1:05–1:12 Facecam
│       ├── Shot16Method.tsx         1:12–1:17 B-roll + 3 mots animés
│       ├── Shot17Anchor.tsx         1:17–1:20 Facecam
│       ├── Shot18Subscribe.tsx      1:18–1:23 Facecam + bouton Subscribe overlay
│       ├── Shot19Newsletter.tsx     1:23–1:26 Facecam + overlay "Newsletter"
│       └── Shot20EndScreen.tsx      1:26–1:28 End screen logo + tagline
├── package.json
└── tsconfig.json
```

## Timeline (frames @ 30fps, 20 plans)

| Shot | TC | Frames | Durée | Type | Overlay principal |
|------|----|--------|-------|------|-------------------|
| 01 | 0:00 | 0–60 | 2s | Facecam | Sous-titre |
| 02 | 0:02 | 60–150 | 3s | Capture | "Site lent = visiteurs perdus" |
| 03 | 0:05 | 150–270 | 4s | Facecam | Lower third "Michaël KIHL · schoolsWP" |
| 04 | 0:09 | 270–450 | 6s | Facecam | Highlights profils (jaune) |
| 05 | 0:15 | 450–540 | 3s | **Titre plein écran** | "3 leviers concrets" |
| 06 | 0:18 | 540–780 | 8s | Facecam+insert | Badge "① SEO" |
| 07 | 0:26 | 780–990 | 7s | Capture | Badge "② Performance" |
| 08 | 0:33 | 990–1230 | 8s | Facecam | Badge "③ Automatisation" |
| 09 | 0:41 | 1230–1350 | 4s | **B-roll** | "Moins de technique. Plus de résultats." |
| 10 | 0:45 | 1350–1500 | 5s | Facecam large | Sous-titre |
| 11 | 0:50 | 1500–1650 | 5s | Capture | "Tutoriels étape par étape" |
| 12 | 0:55 | 1650–1770 | 4s | Capture | "Tests · Comparatifs" |
| 13 | 0:59 | 1770–1860 | 3s | Facecam | Sous-titre |
| 14 | 1:02 | 1860–1950 | 3s | **Titre plein écran** | "Testé sur le terrain" |
| 15 | 1:05 | 1950–2160 | 7s | Facecam | Sous-titre |
| 16 | 1:12 | 2160–2310 | 5s | B-roll/capture | "WordPress · SEO · Automatisation" (1 par 1) |
| 17 | 1:17 | 2310–2400 | 3s | Facecam | Sous-titre |
| 18 | 1:20 | 2400–2550 | 5s | Facecam+overlay | Bouton Subscribe animé |
| 19 | 1:25 | 2550–2640 | 3s | Facecam | "Newsletter → description" |
| 20 | 1:28 | 2640–2700 | 2s | **End screen** | Logo + tagline |
| **Total** | | **2700** | **90s** | | |

## Composants à créer (nouveaux)

### LowerThird
- Slide-in depuis la gauche (spring)
- Barre verte `#00D400` à gauche, fond semi-transparent sombre
- Nom en Nunito Sans bold, titre en Roboto regular
- Auto-disparition après ~3s

### FullScreenTitle
- Fond configurable (clair ou vert)
- Texte centré, Nunito Sans bold, grande taille
- Fade-in + scale spring, hold, fade-out

### OverlayBadge
- Numéro encerclé (①②③) + label
- Fond semi-transparent, coin supérieur gauche
- Slide-in depuis la gauche

### SubtitleBar
- Fond semi-transparent sombre, centré en bas
- Texte blanc Roboto, 2 lignes max
- Fade-in/out par segment

### SubscribeButton
- Style bouton YouTube rouge + cloche
- Apparition scale spring + pulse

### ShotIndicator
- Petit label en haut à droite (DEV uniquement)
- Indique "FACECAM", "CAPTURE", "B-ROLL" avec couleur

## Composants réutilisés depuis video-marketing

- `AnimatedText.tsx` — copié tel quel
- `CTAButton.tsx` — copié tel quel
- `theme.ts` — même palette, ajustements timeline

## Dépendances (identiques à video-marketing)

```json
{
  "remotion": "^4.0.0",
  "@remotion/cli": "^4.0.0",
  "@remotion/google-fonts": "^4.0.0",
  "@remotion/transitions": "^4.0.0",
  "react": "^18.3.0",
  "react-dom": "^18.3.0",
  "typescript": "^5.5.0",
  "@types/react": "^18.3.0"
}
```

## Vérification

1. `cd youtube-intro && npm install`
2. `npx tsc --noEmit` → zéro erreur
3. `npm run studio` → prévisualiser les deux compositions dans Remotion Studio
4. Vérifier : timing des 20 shots, animations des overlays, transitions fluides
5. `npm run render` → générer `out/youtube-intro-full.mp4`
