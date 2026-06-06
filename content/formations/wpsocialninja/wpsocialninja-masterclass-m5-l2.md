# Leçon 5.2 - Styling du popup, streams et badge

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 5 - Notifications
- **Durée cible** : 6 min (~840 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Affiner l'apparence du popup de notification avec l'onglet Style, comprendre la logique des streams pour faire défiler plusieurs sources d'avis, et savoir quand préférer la disposition en badge.
- **Prérequis** : Leçon 5.1 terminée (popup créé, source et timing configurés).

---

## Script narration

**[INTRO - face camera]**

Dans la leçon précédente, tu as monté ton popup de notification et réglé son timing. Là, on passe au visuel et à l'organisation.

Trois choses au programme : le styling, pour que la bulle colle à ta marque ; les streams, pour faire défiler plusieurs sources d'avis dans le même popup ; et le badge, une disposition différente qui regroupe tes avis de façon plus discrète. On reprend l'éditeur de popup là où on l'avait laissé.

---

**[SECTION 1 - L'onglet Style : coller à ta marque]**

**[ECRAN - éditeur de popup → onglet Style]**

On reste dans l'éditeur de ton popup, et on ouvre l'onglet Style. C'est lui qui contrôle tout le visuel : couleurs, polices et espacements. La logique est la même que pour n'importe quel template de feed, donc tu retrouves vite tes repères.

**[ECRAN - sections Title, Texte de l'avis, Item Box]**

Tu ajustes le texte d'abord : la couleur et la typographie du titre, puis du corps de l'avis. Tu choisis la taille, la graisse, la hauteur de ligne, pour rester lisible à petite échelle, parce qu'un popup est petit par nature.

Ensuite la boîte elle-même, l'Item Box. Tu règles la couleur de fond, le padding interne, et tu peux ajouter une bordure : style, épaisseur et couleur. C'est ce qui détache joliment la bulle du reste de la page.

**[FACE CAMERA]**

Mon réflexe schoolsWP : reprends tes couleurs de marque pour le fond et le titre, et garde un texte sobre. Un popup, ça doit attirer l'œil une seconde, pas crier. Et n'oublie pas Save après chaque réglage.

---

**[SECTION 2 - Les streams : faire défiler plusieurs sources]**

**[ECRAN - slide "Stream" : plusieurs avis qui s'enchaînent]**

Parlons des streams. Un stream, c'est simplement le flux d'avis qui défile dans ton popup, l'un après l'autre. Souviens-toi : dans la leçon précédente, tu as coché plusieurs sources dans la section Platforms. Le stream, c'est ce qui les enchaîne.

Concrètement, si tu as connecté tes témoignages manuels et tes avis Google, le popup peut alterner entre les deux. Le visiteur voit défiler un avis, puis un autre, puis un autre, et l'ensemble forme un flux continu de preuve sociale.

**[ECRAN - rappel des réglages Delay Between et Number of Reviews]**

Deux réglages pilotent ce défilement, et tu les connais déjà. Le Delay Between, vu en leçon 5.1, fixe le rythme entre deux avis du stream. Et le nombre d'avis chargés détermine la longueur de la boucle avant qu'elle ne recommence. Plus tu charges d'avis, plus le flux semble varié et vivant.

Pense aussi aux filtres : comme pour un feed, tu peux limiter le stream à tes meilleurs avis, par exemple uniquement les 5 étoiles, pour ne montrer que le haut du panier.

---

**[SECTION 3 - Le badge : une autre façon d'afficher]**

**[ECRAN - slide comparant "popup défilant" et "badge regroupé"]**

Dernière disposition : le badge. Au lieu de bulles qui apparaissent et disparaissent une à une, le badge regroupe tes avis dans un petit élément fixe, posé dans un coin de l'écran. Le visiteur peut cliquer pour ouvrir le lot d'avis.

C'est l'option plus discrète. Le popup défilant attire activement le regard, le badge attend qu'on s'y intéresse. Tu choisis selon le ton de ton site : preuve sociale insistante pour une page de vente, présence calme pour un site éditorial.

**[ECRAN - rappel Display 'Read all reviews' Button]**

Et ça rejoint un réglage vu en 5.1 : le bouton "Read all reviews". Activé, il transforme ton popup en porte d'entrée vers ta page d'avis complète. Badge plus bouton, tu obtiens un point de preuve sociale compact qui renvoie vers l'ensemble de tes témoignages.

---

**[OUTRO - face camera]**

Voilà le Module 5 bouclé. Tu sais créer un popup, choisir sa source et son timing, le styler à ta marque, faire défiler plusieurs sources en stream, et choisir entre l'affichage défilant et le badge plus discret. Tu as maintenant la preuve sociale en mouvement, en plus des feeds et des avis vus dans les modules précédents.

Dans le prochain module, on passe aux intégrations et aux fonctions avancées : shortcodes, page builders, et les petites mécaniques qui relient tout l'écosystème. On se retrouve là-bas.

---

## Notes de production

### Captures d'écran suggérées

- Éditeur de popup → onglet Style, vue d'ensemble (section 1)
- Zoom sur Item Box : couleur de fond, padding, bordure (section 1)
- Slide "Stream" animée : trois avis qui s'enchaînent dans une même bulle (section 2)
- Rappel visuel des réglages Delay Between et nombre d'avis (section 2)
- Slide comparative "popup défilant vs badge regroupé" côte à côte (section 3)
- Exemple de badge posé dans un coin, ouvert au clic (section 3)

### Transitions

- Intro : face camera, fond neutre schoolsWP, rappel rapide du popup de la leçon 5.1
- Section 1 : screencast dans l'onglet Style, puis retour face camera pour le conseil de marque
- Section 2 : slides Kadence pour illustrer le défilement, le concept de stream est plus visuel que cliquable
- Section 3 : slide comparative claire, c'est le point de décision (défilant vs badge)
- Outro : face camera, double CTA - fin de module et teaser Module 6

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:25 |
| Section 1 - Onglet Style | 2:00 |
| Section 2 - Streams | 1:45 |
| Section 3 - Badge | 1:30 |
| Outro | 0:20 |
| **Total** | **~6:00** |

### Sources

- Doc : `sources/docs/guide__advanced-features__notification-popup.md` (onglets Style et réglages, sources multiples)
- Doc : `sources/docs/guide__social-feeds__style-connection-settings.md` (logique de l'onglet Style : Title, Item Box, typographie, bordure)
- Vidéos officielles : #51 (Style Notification Pop-up Box), #29 (Notification Streams and Badge Layout)
