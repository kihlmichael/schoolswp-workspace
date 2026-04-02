# Lecon 5.8 — One-page website : portfolio, coming soon, evenement

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 5 — Sites business avec ZipWP
- **Lecon** : 8/8
- **Duree cible** : 8 min
- **Objectif pedagogique** : Creer un site one-page avec ZipWP pour des cas specifiques — portfolio freelance, page coming soon, page evenement, CV en ligne — avec navigation par ancres et design adapte.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Parfois, tu n'as pas besoin d'un site complet. Pas 5 pages, pas 10, juste une. Un portfolio freelance, une page coming soon pour un lancement, une page evenement, un CV en ligne. Un site one-page, clair et efficace.

Et ZipWP est parfait pour ca. Tu generes, tu ajustes, tu publies. En moins d'une heure, ton one-page est en ligne. On voit quand c'est le bon format et comment le construire.

---

[SECTION 1 — Quand un one-page suffit]

Un one-page n'est pas un site au rabais. C'est le bon format pour un objectif precis.

Portfolio freelance : tu es designer, photographe, developpeur. Tu veux montrer tes realisations et permettre aux prospects de te contacter. Pas besoin de pages separees — tout tient sur une page fluide.

Page coming soon : tu lances un produit, un service, une formation. Le site n'est pas pret mais tu veux commencer a capter des emails. Un titre, un visuel, un formulaire d'inscription, et un compte a rebours. C'est tout.

Page evenement : tu organises un webinaire, un workshop, une conference. Les informations (date, lieu, programme, intervenants) et un bouton d'inscription. Une seule page, zero navigation complexe.

CV en ligne : tu cherches un emploi ou tu veux renforcer ta presence en ligne. Ton parcours, tes competences, tes projets, et un bouton de contact. Plus percutant qu'un PDF.

Le point commun : un seul objectif, une seule action attendue du visiteur. Pas de dispersion.

---

[SECTION 2 — Generer avec ZipWP]

Le prompt fait la difference. Quand tu generes un one-page, dis-le explicitement a ZipWP.

Exemple pour un portfolio : "Site one-page pour un graphiste freelance specialise en identite visuelle. Sections : hero avec mon nom et ma specialite, portfolio avec 6 projets recents, services (logo, charte graphique, packaging), temoignages clients, et formulaire de contact. Design minimal et moderne."

Exemple pour une coming soon : "Page coming soon pour le lancement d'une application de gestion de projet. Un titre accrocheur, une description en une phrase, un visuel du produit, un formulaire d'inscription email pour etre notifie au lancement, et un compte a rebours vers la date de lancement."

ZipWP va generer un site multi-pages par defaut. Pas de souci — tu vas fusionner tout le contenu sur une seule page. Garde la page d'accueil, supprime les autres du menu, et deplace le contenu pertinent des autres pages vers ta page unique.

---

[SECTION 3 — Navigation par ancres]

Sur un one-page, le menu ne pointe pas vers d'autres pages mais vers des sections de la meme page. C'est la navigation par ancres.

Comment ca marche : chaque section de ta page a un identifiant unique (un "ID HTML"). Le menu contient des liens qui pointent vers ces identifiants. Quand le visiteur clique sur "Portfolio" dans le menu, la page scrolle automatiquement jusqu'a la section portfolio.

Configuration dans Spectra : selectionne le bloc conteneur de chaque section. Dans les reglages avances, ajoute un "HTML Anchor" — par exemple "portfolio", "services", "contact".

Configuration du menu : va dans Apparence → Menus. Ajoute des "Liens personnalises". L'URL est simplement "#portfolio", "#services", "#contact". Le texte est le nom visible dans le menu. Enregistre.

Resultat : le visiteur clique sur un element du menu, la page scrolle en douceur jusqu'a la bonne section. Pas de chargement de page, pas de temps d'attente. C'est fluide et professionnel.

---

[SECTION 4 — Design specifique pour le one-page]

Un one-page a ses propres regles de design.

Scroll fluide : dans les reglages Astra (Personnaliser → Performance ou via un snippet CSS), active le smooth scroll. Le defilement entre les sections devient doux au lieu de sauter brutalement. Un detail qui change la perception de qualite.

Sections pleine largeur : chaque section doit occuper toute la largeur de l'ecran. Utilise le bloc "Container" de Spectra en mode "Full Width". Alterne les couleurs de fond entre les sections — blanc, gris clair, couleur de marque — pour creer une separation visuelle nette.

Hauteur des sections : chaque section principale devrait avoir une hauteur minimale — pas necessairement plein ecran, mais suffisamment pour que le contenu respire. Evite les sections ecrasees avec trop de texte. Un one-page, ca se lit en scrollant, pas en plissant les yeux.

Animations au scroll : Spectra propose des animations d'entree pour les blocs — apparition en fondu, glissement depuis la gauche ou la droite. Utilise-les avec parcimonie — une animation par section, pas sur chaque element. L'objectif est de guider l'oeil, pas de donner le tournis.

---

[SECTION 5 — Publier rapidement]

L'avantage du one-page : tu peux le mettre en ligne en moins d'une heure.

Si c'est un coming soon, connecte ton formulaire a FluentCRM ou a un service comme Mailchimp pour commencer a capturer des emails avant meme que ton site complet soit pret.

Si c'est un portfolio, verifie le rendu sur mobile. Ouvre l'apercu responsive dans l'editeur Gutenberg. Les images doivent se redimensionner proprement, le texte doit rester lisible, et le formulaire de contact doit etre utilisable au pouce.

Si c'est un evenement, ajoute le schema markup "Event" pour que Google affiche la date et le lieu directement dans les resultats de recherche. SureRank ou Rank Math gerent ca.

Le one-page est ideal pour tester une idee rapidement. Tu ne sais pas si ta formation va trouver son public ? Cree un coming soon, capture des emails, et mesure l'interet avant d'investir 50 heures dans la creation du cours. C'est du validation produit a cout zero.

---

[OUTRO]

Un one-page avec ZipWP, c'est rapide a creer, efficace a lire, et parfait pour un objectif precis. Portfolio, coming soon, evenement, CV — chaque cas a sa structure, mais le principe reste le meme : une page, un objectif, zero distraction.

C'est la derniere lecon du module 5. Tu as maintenant 8 types de sites business dans ta boite a outils : site vitrine, e-commerce, formation, funnels, CRM, automatisation, landing page, et one-page.

Dans le module 6, on prend du recul. L'ecosysteme complet de Brainstorm Force, les comparatifs honnetes avec la concurrence, et comment transformer ZipWP en business rentable.

---

## Notes de production

### Captures d'ecran suggerees

1. **Prompt one-page** — Champ ZipWP avec le prompt portfolio
2. **Navigation ancres** — Menu avec liens #portfolio, #services, #contact
3. **HTML Anchor** — Reglages du bloc Spectra avec l'identifiant de section
4. **Design sections** — Vue pleine page avec sections alternees et animations
5. **Vue mobile** — Rendu responsive du one-page sur smartphone

### Transitions

- Intro → Section 1 : exemples visuels de one-pages (portfolio, coming soon, evenement)
- Section 1 → Section 2 : ouverture ZipWP, saisie du prompt
- Section 2 → Section 3 : configuration du menu avec ancres
- Section 3 → Section 4 : edition du design, animations, sections pleine largeur
- Section 4 → Section 5 : publication et test mobile
- Section 5 → Outro : recap visuel des 8 types de sites du module 5

### Notes HeyGen / ElevenLabs

- Ton decontracte et efficace — le one-page est un format rapide, le ton doit le refleter
- Section 3 (ancres) : rythme technique mais clair, montrer la manipulation
- Section 4 (design) : visuellement riche, montrer les animations a l'ecran
- Conclure le module avec energie — on passe au niveau superieur dans le module 6
