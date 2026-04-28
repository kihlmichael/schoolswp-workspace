# Process de production video schoolsWP

> Ce document decrit le workflow complet de production, de l'idee au livrable final.

## Les 8 etapes

### 1. Cadrage creatif

Avant de coder, definir :

- objectif de la video
- duree cible
- ambiance et niveau d'energie
- couleur dominante
- texte affiche
- destination finale (YouTube, LinkedIn, site, etc.)
- presence ou non d'audio

Sortie attendue : brief court dans `docs/brand-video-brief.md`

### 2. Preparation des inputs

Verifier chaque input :

- bon logo (bonne version couleur)
- dimensions correctes
- audio valide si present
- typo conforme
- casse exacte des textes (schoolsWP, pas schoolswp)

Controle obligatoire pour chaque logo :

- couleur reelle du SVG (pas juste le nom du fichier)
- lisibilite sur fond clair
- lisibilite sur fond sombre
- ecriture correcte de schoolsWP

### 3. Creation de composition

Creer une composition dediee dans `src/compositions/`.

Regles :

- 1 composition = 1 intention claire
- extraire les elements reutilisables dans `src/components/`
- centraliser les constantes dans `theme.ts`
- declarer proprement dans `Root.tsx`

Chaque composition doit definir : `id`, `durationInFrames`, `fps`, `width`, `height`

### 4. Animation

Construire une animation :

- sobre et premium
- lisible et coherente
- pensee en frames
- chaque mouvement a une intention

### 5. Preview / rendu test

Objectif : valider avant export final

- rythme
- lisibilite
- placement des elements
- duree
- transitions
- coherence brand

Dossier : `out/previews/`

### 6. QA

Faire une QA systematique avant validation (voir checklist ci-dessous).

### 7. Export final

Exporter la version validee dans `out/finals/`.

Regles :

- incrementer la version
- archiver les anciennes versions importantes
- noter le rendu dans `docs/render-log.md`

### 8. Archivage

Conserver :

- fichier final
- brief
- log
- assets utiles

Deplacer les versions obsoletes dans `out/archive/`

---

## Checklist QA obligatoire

### Branding

- [ ] schoolsWP bien ecrit partout (WP majuscules)
- [ ] Logo correct (bonne variante, bonne couleur)
- [ ] Couleurs conformes a theme.ts
- [ ] Ton visuel schoolsWP respecte (calme, premium, clair)
- [ ] URL schoolsWP.com ecrite correctement

### Technique

- [ ] Dimensions correctes (1920x1080)
- [ ] FPS correct (30 via THEME.fps)
- [ ] Duree correcte
- [ ] Aucun element coupe ou debordant
- [ ] Aucun asset manquant
- [ ] Aucun texte tronque
- [ ] Aucune erreur de structure evidente
- [ ] Imports corrects
- [ ] Composition enregistree dans Root.tsx

### Motion

- [ ] Animation fluide (pas de saccade)
- [ ] Hierarchie visuelle claire
- [ ] Temps de lecture suffisant pour chaque texte
- [ ] Fin propre (pas de coupure brutale)
- [ ] Pas d'effet cheap ou de surcharge
- [ ] Springs coherentes avec les conventions du projet

### Son (si audio present)

- [ ] Niveau coherent
- [ ] Pas de saturation
- [ ] Synchro correcte si SFX
- [ ] Fin audio propre

### Export

- [ ] Nom de fichier propre (convention respectee)
- [ ] Bon emplacement de sortie
- [ ] Version incrementee
- [ ] Log de rendu mis a jour si necessaire

---

## Format de render-log

Quand un rendu significatif est genere, documenter dans `docs/render-log.md` :

```markdown
## schoolsWP-brand-outro-c-pro-v2

- Date : 2026-03-30
- Composition : BrandOutroCPro
- Duree : 5s
- Format : 1920x1080 MP4
- Changements : [description des modifications]
- Statut : [preview | valide | archive]
```

---

## Statuts de production

| Statut         | Signification                               |
| -------------- | ------------------------------------------- |
| **Confirme**   | Verifie par lecture de fichier ou execution |
| **A verifier** | Suppose mais non controle                   |
| **Recommande** | Suggestion basee sur les conventions        |
| **Bloquant**   | Empeche de continuer sans resolution        |
