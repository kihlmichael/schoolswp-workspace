# Lecon 2.7 — Responsive : optimiser pour mobile et tablette

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 2 — Personnalisation avancee
- **Lecon** : 7/8
- **Duree cible** : 8 min
- **Objectif pedagogique** : Verifier et optimiser le rendu mobile/tablette d'un site genere — ajustements par appareil, erreurs courantes, tests reels.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

60 a 75% du trafic web vient du mobile. Si ton site n'est pas impeccable sur un smartphone, tu perds la majorite de tes visiteurs avant meme qu'ils aient lu ta premiere phrase.

La bonne nouvelle : les sites generes par ZipWP sont responsives par defaut — Astra et Spectra gerent les adaptations de base. La mauvaise nouvelle : tes personnalisations peuvent casser le rendu mobile. Et il y a des erreurs que l'IA ne detecte pas.

---

[SECTION 1 — La preview responsive dans Spectra]

L'editeur WordPress integre une preview responsive. En bas a gauche de l'ecran (ou dans la barre superieure selon ta version), tu trouves les icones desktop, tablette et mobile.

Clique sur tablette : la zone d'edition se reduit a une largeur de tablette (~768 pixels). Clique sur mobile : elle se reduit a une largeur de smartphone (~375 pixels). Tu vois immediatement comment ta page s'affiche sur chaque appareil.

Mais attention : cette preview est une approximation. Elle ne reproduit pas exactement le comportement d'un vrai navigateur mobile — les polices, les espacements et les interactions tactiles peuvent etre legerement differents. Utilise-la comme outil de travail, pas comme validation finale.

---

[SECTION 2 — Ajustements par appareil]

Chaque bloc Spectra a des reglages specifiques par appareil. Quand tu selectionnes un bloc et que tu es en vue mobile, les reglages du panneau lateral s'appliquent uniquement au mobile.

Les ajustements les plus frequents.

Taille de police. Un titre de 48 pixels sur desktop est trop gros sur mobile. Passe en vue mobile et reduis-le a 28-32 pixels. Le corps de texte peut rester a 16 pixels — c'est lisible sur les deux appareils.

Padding et marges. Les espacements genereux qui fonctionnent sur desktop creent des vides enormes sur mobile. Reduis le padding vertical des sections — passe de 80 pixels a 40 pixels par exemple. Reduis les marges laterales aussi.

Nombre de colonnes. 3 colonnes cote a cote sur desktop deviennent illisibles sur mobile. Configure le container pour empiler les colonnes verticalement sur mobile — c'est souvent le comportement par defaut avec Spectra, mais verifie.

Masquer des elements. Certains elements n'ont pas de sens sur mobile — une grande image decorative, un tableau complexe, un compteur anime. Spectra permet de masquer un bloc sur un appareil specifique dans les reglages de visibilite (Display conditions).

---

[SECTION 3 — Les 5 erreurs mobiles courantes]

Erreur 1 : des titres trop longs. Un titre de 12 mots sur une seule ligne en desktop se retrouve sur 3 lignes en mobile. Raccourcis tes titres ou utilise une taille differente sur mobile.

Erreur 2 : des images trop lourdes. Meme avec le lazy loading, une image de 2 Mo prend du temps a charger sur une connexion 4G. Compresse tes images — on l'a vu dans la lecon precedente. Vise moins de 200 Ko par image.

Erreur 3 : des boutons trop petits. Sur mobile, un bouton doit etre assez grand pour etre clique avec le pouce. Minimum 44x44 pixels — c'est la recommandation de Google. Augmente le padding des boutons sur mobile si necessaire.

Erreur 4 : du padding excessif. Des sections avec 100 pixels de marge en haut et en bas sur desktop creent des pages interminables sur mobile. Reduis les espacements de 40 a 50% sur mobile.

Erreur 5 : des formulaires penibles. Un formulaire avec 8 champs sur une seule colonne, c'est decourageant sur mobile. Reduis le nombre de champs au strict minimum — nom, email, message. Et verifie que les champs sont assez grands pour taper facilement.

---

[SECTION 4 — Tester sur un vrai telephone]

La preview responsive de l'editeur n'est pas suffisante. Tu dois tester sur un vrai appareil.

Methode 1 : ouvre ton site sur ton smartphone. Navigue sur chaque page. Clique sur les boutons. Remplis le formulaire. Scroll du haut en bas. Tu detecteras des problemes invisibles dans la preview — des textes qui debordent, des boutons mal places, des images qui se chevauchent.

Methode 2 : utilise les DevTools de Chrome. Clic droit → "Inspecter" → icone mobile (en haut a gauche des DevTools). Tu peux simuler differents appareils — iPhone, Samsung, iPad — avec leurs dimensions exactes.

Methode 3 : demande a 2-3 personnes d'ouvrir ton site sur leurs telephones et de te faire un retour. Des yeux frais detectent des problemes que tu ne vois plus.

Verifie ces points sur mobile : le menu est-il accessible (hamburger menu) ? Les images se chargent-elles rapidement ? Les boutons sont-ils cliquables ? Le formulaire est-il utilisable ? Le texte est-il lisible sans zoomer ?

---

[OUTRO]

Un site qui n'est pas optimise pour le mobile en 2026, c'est un site qui perd la majorite de son audience. Prends le temps de verifier et d'ajuster le rendu mobile — tailles de police, espacements, colonnes, boutons, formulaires.

Derniere lecon du module : la performance. On va mesurer la vitesse de ton site, comprendre les Core Web Vitals, et appliquer les optimisations qui font la difference pour le SEO et la conversion.

---

## Notes de production

### Captures d'ecran suggerees

1. **Preview responsive** — Editeur WordPress en mode mobile avec la page visible
2. **Reglages par appareil** — Panneau lateral avec icones desktop/tablette/mobile sur un champ
3. **Avant/apres mobile** — Section avec 3 colonnes desktop vs empilee sur mobile
4. **5 erreurs** — Montage des 5 erreurs avec exemples visuels
5. **Chrome DevTools** — Simulateur d'appareil avec le site ouvert
6. **Test reel** — Photo d'un smartphone montrant le site

### Transitions

- Intro → Section 1 : bascule desktop → mobile dans l'editeur
- Section 2 : demonstrations d'ajustements en temps reel
- Section 3 : montage rapide des 5 erreurs
- Section 4 : transition vers Chrome DevTools puis photo smartphone
- Outro : retour avatar, teaser performance

### Notes HeyGen / ElevenLabs

- Ton serieux mais pratique — le mobile n'est pas optionnel
- "60 a 75% du trafic vient du mobile" : articuler, chiffre cle
- Section 3 : rythme dynamique, erreur par erreur
- Section 4 : ton encourageant — "prends 15 minutes pour tester"
