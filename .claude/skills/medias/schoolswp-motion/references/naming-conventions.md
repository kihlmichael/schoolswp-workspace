# Conventions de nommage — video-marketing schoolsWP

## Assets

Format : `[type]-[usage]-[variant].[ext]`

### Exemples

| Fichier                      | Type  | Usage     | Variant       |
| ---------------------------- | ----- | --------- | ------------- |
| `logo-schoolswp-white.svg`   | logo  | schoolswp | white         |
| `logo-schoolswp-black.svg`   | logo  | schoolswp | black         |
| `music-outro-ambient-v1.mp3` | music | outro     | ambient-v1    |
| `sfx-pulse-soft-v1.wav`      | sfx   | pulse     | soft-v1       |
| `img-hero-background-v1.png` | img   | hero      | background-v1 |

### Types d'assets

| Type    | Dossier          | Description             |
| ------- | ---------------- | ----------------------- |
| `logo`  | `public/logos/`  | Logos de marque         |
| `music` | `public/audio/`  | Musiques de fond        |
| `sfx`   | `public/audio/`  | Effets sonores          |
| `img`   | `public/images/` | Images et illustrations |
| `font`  | `public/fonts/`  | Polices personnalisees  |

> **Etat actuel** : les logos existants utilisent le format `nom-white.svg` / `nom-black.svg`.
> La convention cible est `logo-schoolswp-white.svg`. La migration sera faite
> progressivement — ne pas renommer les fichiers existants sans plan explicite.

## Compositions

Format : `[BlocFonction][Variante].tsx`

### Blocs fonctionnels

| Prefixe          | Usage                             | Exemple                                         |
| ---------------- | --------------------------------- | ----------------------------------------------- |
| `Brand`          | Elements de marque (intro, outro) | `BrandIntro.tsx`, `BrandOutroA.tsx`             |
| `Scene` + numero | Scenes narratives                 | `Scene2Presentation.tsx`, `Scene4Solutions.tsx` |
| `Module`         | Openers de module de formation    | `ModuleOpener.tsx`                              |
| `Bumper`         | Transitions courtes               | `BumperTransition.tsx`                          |

### Regles

- PascalCase obligatoire
- Le nom du fichier = le nom de l'export = l'id de composition dans Root.tsx
- Les variantes s'ajoutent en suffixe : `BrandOutroC.tsx`, `BrandOutroCPro.tsx`
- Pas de suffixes vagues : `Test`, `New`, `Final`, `V2` dans les noms de fichiers

## Exports video

Format : `schoolsWP-[type]-[concept]-v[version].mp4`

### Exemples

| Fichier                               | Type  | Concept      | Version |
| ------------------------------------- | ----- | ------------ | ------- |
| `schoolsWP-brand-intro-v1.mp4`        | brand | intro        | 1       |
| `schoolsWP-brand-outro-c-v1.mp4`      | brand | outro-c      | 1       |
| `schoolsWP-brand-outro-c-pro-v2.mp4`  | brand | outro-c-pro  | 2       |
| `schoolsWP-scene-presentation-v1.mp4` | scene | presentation | 1       |

### Regles

- Toujours commencer par `schoolsWP-`
- Toujours terminer par `-v[numero]`
- Incrementer la version a chaque export significatif
- Pas de noms flous : `final-ok.mp4`, `test-2.mp4`, `new-version.mp4`

### Emplacement

| Dossier         | Contenu                              |
| --------------- | ------------------------------------ |
| `out/previews/` | Rendus de test / validation en cours |
| `out/finals/`   | Versions validees pretes a l'emploi  |
| `out/archive/`  | Anciennes versions conservees        |

> **Etat actuel** : les exports existants sont dans `out/` directement
> (ex: `brand-intro.mp4`). La migration vers la structure cible
> `out/previews/` / `out/finals/` / `out/archive/` sera faite progressivement.
