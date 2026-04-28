# Modifications BrandIntro -- couleurs fond et tagline

## Fichier modifie

`src/compositions/BrandIntro.tsx`

## Changements effectues

### 1. Fond de la scene : `#12111F` -> `#1a1a2e`

Ligne 50 -- la propriete `backgroundColor` de `AbsoluteFill` utilisait `THEME.bgDark` (`#12111F`).
Remplacee par la valeur en dur `"#1a1a2e"` pour un rendu plus premium (bleu nuit profond au lieu de noir-violet).

```diff
- backgroundColor: THEME.bgDark,
+ backgroundColor: "#1a1a2e",
```

### 2. Couleur du tagline : `#FAFBFD` -> `#6CB4EE`

Ligne 87 -- la propriete `color` du tagline utilisait `THEME.textWhite` (`#FAFBFD`).
Remplacee par `"#6CB4EE"` (bleu clair) pour un contraste doux sur le nouveau fond.

```diff
- color: THEME.textWhite,
+ color: "#6CB4EE",
```

## Remarque

Ces deux valeurs sont codees en dur dans le composant au lieu de passer par `THEME`. Si ces couleurs doivent etre reutilisees ailleurs, il serait preferable de les ajouter au fichier `theme.ts` (par exemple `bgPremium` et `textAccentLight`).
