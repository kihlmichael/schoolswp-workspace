# Lecon 2.5 — Images et medias : remplacer les visuels IA

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 2 — Personnalisation avancee
- **Lecon** : 5/8
- **Duree cible** : 6 min
- **Objectif pedagogique** : Comprendre pourquoi remplacer les images stock, ou trouver de bons visuels, et comment les optimiser avant upload.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Les images generees par ZipWP sont correctes. Elles sont dans le bon univers, elles ont un style professionnel, elles remplissent l'espace. Mais elles sont generiques. Et un site avec des photos generiques, ca se voit — et ca ne convertit pas.

Dans cette lecon, on parle de comment remplacer ces visuels et les optimiser pour la performance et le SEO.

---

[SECTION 1 — Pourquoi remplacer les images stock]

Deux raisons principales.

L'authenticite. Tes visiteurs veulent voir TON activite, TON equipe, TON environnement de travail. Une photo de banque d'images montrant des gens souriants dans un bureau generique ne cree aucune connexion emotionnelle. TES photos — meme prises avec un smartphone — sont 10 fois plus credibles.

La differenciation. Les images stock sont utilisees par des milliers de sites. Si un visiteur reconnait une photo qu'il a vue ailleurs, ta credibilite chute. Tes propres visuels rendent ton site unique par definition.

Ca ne veut pas dire que toutes les images stock sont a bannir. Pour des illustrations conceptuelles — un fond de section, une image decorative — les images stock conviennent. Mais pour tout ce qui montre ton activite — toi, tes produits, tes locaux, tes resultats — utilise tes propres photos.

---

[SECTION 2 — Sources d'images]

Tes propres photos — c'est l'ideal. Prends des photos de qualite correcte avec ton smartphone. Lumiere naturelle, arriere-plan propre, sujet net. Pour un investissement minimal, tu peux aussi faire appel a un photographe local pour une seance de 2 heures — ca te donne assez de visuels pour tout le site.

Unsplash — integre directement dans WordPress et dans Spectra. Des photos haute qualite, libres de droits, gratuites. La selection est enorme. Utilise la recherche par mots-cles en anglais pour de meilleurs resultats.

Pexels — meme principe qu'Unsplash, avec un catalogue different. Utile quand tu ne trouves pas ce que tu cherches sur Unsplash.

Pixabay — troisieme option, catalogue plus large mais qualite plus variable.

A eviter : les images avec watermark, les images protegees par copyright, les images generees par IA qui ressemblent a des photos (doigts etranges, texte incoherent). Si tu utilises des images libres de droits, verifie toujours la licence — certaines interdisent l'usage commercial.

---

[SECTION 3 — Optimisation avant upload]

Uploader des images non optimisees, c'est le moyen le plus rapide de plomber la vitesse de ton site. Et un site lent perd des visiteurs et du SEO.

Format. Utilise le WebP. C'est le format recommande par Google — il est plus leger que le JPEG a qualite egale. La plupart des outils de conversion le proposent. Si ton hebergeur ne supporte pas WebP, reste en JPEG pour les photos et PNG pour les visuels avec transparence.

Dimensions. Redimensionne tes images AVANT de les uploader. Une image hero n'a pas besoin de faire 4000 pixels de large — 1920 pixels suffisent. Une image dans une colonne de 400 pixels n'a pas besoin de faire 2000 pixels. Adapte la taille a l'usage.

Compression. Utilise un outil de compression : Imagify (plugin WordPress), ShortPixel (plugin WordPress), ou TinyPNG (en ligne, gratuit). Vise une reduction de 60 a 80% du poids sans perte visible de qualite. Une image hero devrait peser entre 80 et 200 Ko, pas 2 Mo.

Lazy loading. WordPress active le lazy loading par defaut depuis la version 5.5. Ca veut dire que les images en bas de page ne se chargent que quand le visiteur scroll vers elles. Verifie que l'attribut `loading="lazy"` est present sur tes images — Spectra le gere automatiquement.

---

[SECTION 4 — Alt text SEO]

Chaque image doit avoir un texte alternatif — le "alt text". C'est obligatoire pour l'accessibilite (les lecteurs d'ecran), et c'est un signal SEO.

Le alt text doit decrire l'image en langage naturel, avec ton mot-cle si c'est pertinent. Exemples :

- Mauvais : "IMG_4521.jpg" ou "image" ou vide
- Correct : "photo" ou "bureau"
- Bon : "Seance de coaching sportif individuel a Lyon dans une salle de fitness"

Ne bourre pas le alt text de mots-cles. Une description naturelle de 5 a 15 mots suffit. Google sait faire la difference entre un alt text utile et du keyword stuffing.

Dans WordPress, tu edites le alt text depuis la bibliotheque de medias ou directement dans les reglages du bloc image.

---

[OUTRO]

Les images font 50% de l'impression visuelle de ton site. Remplace les photos stock par tes visuels, optimise le format et le poids, et soigne les alt texts. C'est un investissement de quelques heures qui transforme completement la perception de ton site.

Dans la prochaine lecon, on decouvre l'AI Assistant integre a ZipWP — un outil d'ecriture IA qui t'aide a ameliorer tes textes directement dans l'editeur WordPress.

---

## Notes de production

### Captures d'ecran suggerees

1. **Image stock vs reelle** — Comparaison cote a cote (meme site, images differentes)
2. **Unsplash dans WordPress** — Interface de recherche integree
3. **TinyPNG** — Avant/apres compression (taille du fichier)
4. **Dimensions** — Illustration des tailles recommandees par usage
5. **Alt text** — Champ alt text dans les reglages d'une image WordPress
6. **PageSpeed** — Impact des images sur le score (avant/apres optimisation)

### Transitions

- Intro → Section 1 : zoom sur une image stock generique dans un site ZipWP
- Section 1 → Section 2 : transition vers les sources d'images
- Section 3 : screencasts de compression et conversion
- Section 4 : edition du alt text dans WordPress
- Outro : retour avatar, teaser AI Assistant

### Notes HeyGen / ElevenLabs

- Lecon courte — rythme soutenu mais pas presse
- Section 1 : ton convaincu — "ca se voit et ca ne convertit pas"
- Section 3 : ton technique mais accessible, pas de jargon inutile
- "TES photos sont 10 fois plus credibles" : articuler, c'est le message cle
