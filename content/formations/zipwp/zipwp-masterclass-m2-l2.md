# Lecon 2.2 - Spectra : maitriser le page builder block de BSF

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 2 - Personnalisation avancee
- **Lecon** : 2/8
- **Duree cible** : 10 min
- **Objectif pedagogique** : Comprendre le fonctionnement de Spectra comme extension de Gutenberg, maitriser les blocs essentiels et le systeme d'imbrication.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Astra gere l'enveloppe de ton site - header, footer, couleurs, typographie. Spectra gere le contenu de chaque page - les sections, les blocs, les mises en page. C'est le duo Astra + Spectra qui donne a ZipWP sa puissance.

Mais Spectra n'est pas un page builder comme les autres. Ce n'est pas Elementor, ce n'est pas Divi. C'est une extension de Gutenberg - l'editeur natif de WordPress. Ca veut dire que tu travailles avec les blocs WordPress standard, plus des blocs avances ajoutes par Spectra. Et c'est un avantage : moins de code, moins de poids, meilleure compatibilite.

---

[SECTION 1 - Spectra et Gutenberg : quelle relation ?]

Gutenberg, c'est l'editeur de blocs integre a WordPress depuis la version 5.0. Tu ajoutes du contenu en empilant des blocs - paragraphe, image, titre, liste. C'est simple mais limite.

Spectra vient se greffer sur Gutenberg et ajoute une trentaine de blocs avances. Le principe : tu restes dans l'editeur natif, mais tu as beaucoup plus de possibilites. Pas de plugin lourd, pas de builder separe, pas de shortcodes.

Pour faire un parallele que tu connais peut-etre : Spectra est a Gutenberg ce que Kadence Blocks est au theme Kadence. Un booster de blocs qui reste dans l'ecosysteme natif.

Quand tu ouvres une page generee par ZipWP dans l'editeur WordPress, tu vois des blocs Spectra partout - des conteneurs, des titres avances, des images avec overlay, des boutons stylises. Tout ca est editable directement dans Gutenberg.

---

[SECTION 2 - Les blocs essentiels de Spectra]

Voici les 10 blocs que tu utiliseras le plus souvent. Tu les retrouves dans l'insereur de blocs, categorie "Spectra".

Le Container. C'est le bloc fondamental. Tout commence par un container. Il definit une zone avec sa largeur, son padding, sa couleur de fond, ses bordures. Tu imbriques les autres blocs a l'interieur. Pense au container comme a une boite dans laquelle tu ranges tes elements.

L'Advanced Heading. Un titre avec des options de style avancees - taille, couleur, espacement, police, separateur decoratif. Beaucoup plus flexible que le bloc titre standard de WordPress.

L'Image. Le bloc image Spectra ajoute des overlays, des animations au survol, des coins arrondis, des ombres. Plus riche que le bloc image natif.

Le Button. Des boutons avec gradient, icone, animation. Tu peux creer des groupes de boutons - un principal et un secondaire cote a cote.

L'Icon List. Une liste avec des icones au lieu de puces classiques. Parfait pour les listes de services, de fonctionnalites, ou d'avantages.

Les Tabs. Des onglets pour organiser du contenu dans un espace compact. Utile pour les pages services avec plusieurs offres.

L'Accordion. Des sections qui s'ouvrent et se ferment au clic. Ideal pour les FAQ.

Le Countdown. Un compte a rebours avec date et heure. Utile pour les lancements, les promotions, les evenements.

Les Testimonials. Un carrousel de temoignages clients avec photo, nom, texte. Genere automatiquement par ZipWP si tu as mentionne des avis dans ton prompt.

Le Star Rating. Des etoiles de notation - a combiner avec les temoignages pour renforcer la credibilite.

---

[SECTION 3 - Le systeme de blocs imbriques]

Le concept cle de Spectra, c'est l'imbrication. Tu ne poses pas des blocs les uns sous les autres - tu les imbriques les uns dans les autres.

Un Container contient d'autres containers. Un container parent peut contenir 2 containers enfants cote a cote - ca cree 2 colonnes. Chaque colonne contient ses propres blocs - titre, texte, image, bouton.

C'est le meme principe que les div HTML imbriquees, mais en visual. Et c'est ce qui te donne une flexibilite totale sur la mise en page.

Exemple concret : tu veux une section "Nos services" avec 3 colonnes. Tu crees un Container parent (pleine largeur). A l'interieur, tu ajoutes 3 Containers enfants (chacun prend un tiers). Dans chaque container enfant, tu mets une icone, un titre, un paragraphe, et un bouton. Resultat : 3 colonnes de services, alignees, responsives.

Le piege frequent : perdre le fil de l'imbrication. Utilise la vue "List View" (l'icone en haut a gauche de l'editeur) pour voir l'arborescence de tous les blocs. Ca t'evite de selectionner le mauvais container.

---

[SECTION 4 - Les controles responsive]

Chaque bloc Spectra a des controles responsives - des reglages specifiques par appareil.

En haut de l'editeur, tu vois les icones desktop, tablette, mobile. Quand tu cliques sur tablette ou mobile, les reglages du bloc que tu selectionnes s'adaptent. Tu peux definir une taille de police differente sur mobile, un padding different sur tablette, ou meme masquer un bloc entier sur un appareil.

Par exemple, un titre en 48 pixels sur desktop peut etre trop gros sur mobile. Tu passes en vue mobile et tu le reduis a 28 pixels. Les deux valeurs coexistent - desktop garde 48, mobile utilise 28.

Spectra gere ca proprement - pas de hack CSS, pas de media queries manuelles. Tout est dans l'interface.

On verra les optimisations responsive en detail dans la lecon 2.7. Pour l'instant, retiens que chaque reglage peut etre ajuste par appareil.

---

[OUTRO]

Tu connais maintenant Spectra - sa relation avec Gutenberg, ses 10 blocs essentiels, le systeme d'imbrication, et les controles responsive. C'est l'outil avec lequel tu vas passer le plus de temps quand tu personnalises un site genere par ZipWP.

Dans la prochaine lecon, on explore la Patterns Library - des sections pre-construites que tu inseres en un clic et que tu personnalises ensuite. C'est le raccourci pour creer des pages riches sans tout construire bloc par bloc.

---

## Notes de production

### Captures d'ecran suggerees

1. **Editeur Gutenberg** - Vue avec les blocs Spectra dans une page generee
2. **Insereur de blocs** - Categorie Spectra avec la liste des blocs
3. **Container imbrique** - Vue List View montrant l'arborescence parent/enfant
4. **10 blocs** - Montage rapide des 10 blocs en action (1-2 secondes chacun)
5. **Responsive toggle** - Icones desktop/tablette/mobile dans l'editeur
6. **Comparaison Spectra vs natif** - Meme contenu avec blocs natifs vs blocs Spectra

### Transitions

- Intro → Section 1 : ouverture de l'editeur WordPress sur une page generee
- Section 2 : defilement rapide des 10 blocs (type montage)
- Section 3 : zoom sur List View avec l'arborescence
- Section 4 : bascule desktop → mobile dans l'editeur
- Outro : retour avatar, teaser Patterns Library

### Notes HeyGen / ElevenLabs

- Ton pedagogique mais dynamique - beaucoup de contenu a couvrir
- Articuler les noms des blocs : "Container", "Advanced Heading", "Accordion"
- Section 3 (imbrication) : ralentir, concept important
- Analogie "Spectra est a Gutenberg ce que Kadence Blocks est a Kadence" : bien articuler
