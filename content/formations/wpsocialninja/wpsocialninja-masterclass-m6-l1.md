# Leçon 6.1 - Shortcodes : la mécanique universelle d'affichage

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 6 - Intégrations et fonctions avancées
- **Durée cible** : 6 min (~840 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Comprendre ce qu'est un shortcode WP Social Ninja, savoir le trouver et le copier depuis la page Templates, et l'insérer sur n'importe quelle page ou article via le bloc Shortcode de WordPress.
- **Prérequis** : Module 2 ou 3 terminé (au moins un template feed ou avis créé et sauvegardé).

---

## Script narration

**[INTRO - face camera]**

Tu as passé du temps à régler ton feed YouTube ou ton mur d'avis : la source, le layout, les couleurs. Maintenant, il faut l'afficher sur ton site. Et c'est là qu'intervient le shortcode.

Le shortcode, c'est la mécanique universelle d'affichage de WP Social Ninja. Une seule ligne de code que tu poses où tu veux : une page, un article, une barre latérale. C'est la méthode qui marche partout, peu importe ton thème ou ton constructeur de page. Dans cette leçon, on voit ce que c'est, où le trouver, et comment le poser proprement. C'est parti.

---

**[SECTION 1 - Ce qu'est un shortcode]**

**[FACE CAMERA]**

Commençons par le concept, parce qu'il est simple.

Un shortcode, c'est une courte ligne de code que WordPress sait interpréter. WP Social Ninja en génère un automatiquement pour chaque template que tu crées. Tu n'as rien à écrire toi-même.

Quand tu colles cette ligne sur une page, elle dit à WordPress : "affiche mon feed ici, à cet endroit précis". Au moment où le visiteur charge la page, WordPress remplace cette ligne par ton feed complet, entièrement stylé, exactement comme tu l'as conçu dans le plugin.

Voilà à quoi ça ressemble : ouvre crochet, w p underscore social underscore ninja, un identifiant, la plateforme, ferme crochet. Par exemple `[wp_social_ninja id="100" platform="youtube"]`. Le numéro change selon ton template, la plateforme aussi. Tu n'as pas à le taper : tu vas le copier.

---

**[SECTION 2 - Trouver et copier ton shortcode]**

**[ECRAN - WP Social Ninja → Templates]**

Tous tes shortcodes sont rangés au même endroit. Depuis ton tableau de bord WordPress, tu vas dans WP Social Ninja, puis Templates.

Tu vois la liste de tous les templates que tu as créés : ton template YouTube, ton template Instagram, ton mur d'avis, et ainsi de suite. Pour chacun, il y a une colonne appelée ShortCode.

**[ECRAN - colonne ShortCode, clic pour copier]**

Tu repères la ligne du template que tu veux afficher. Dans la colonne ShortCode, tu vois son code unique, celui qui lui est propre. Tu cliques directement dessus, et il est copié dans ton presse-papiers. C'est fait. Pas de copier-coller manuel à la souris, un simple clic suffit.

Petit réflexe à prendre : note bien que chaque template a son propre identifiant. Si tu as trois feeds différents, tu auras trois shortcodes différents. Ne les mélange pas.

---

**[SECTION 3 - Poser le shortcode sur une page ou un article]**

**[ECRAN - éditeur de blocs WordPress, ajout d'un bloc Shortcode]**

Maintenant qu'il est copié, on le pose. La méthode la plus courante, c'est de l'ajouter directement dans une page ou un article.

Tu ouvres la page que tu veux modifier, ou tu en crées une nouvelle. Dans l'éditeur de blocs WordPress, tu cliques sur l'icône plus pour ajouter un nouveau bloc. Tu tapes "Shortcode", tu sélectionnes le bloc Shortcode.

**[ECRAN - collage du shortcode dans le bloc, puis Publier]**

Tu colles ta ligne dans le bloc. Puis tu cliques sur Publier, ou Mettre à jour si la page existait déjà.

Et c'est terminé. Quand tu visualises la page en ligne, WordPress a remplacé cette unique ligne par ton template WP Social Ninja complet et stylé. Le feed se mettra à jour tout seul à chaque nouveau contenu, sans que tu retouches la page.

---

**[SECTION 4 - La page Templates, ton hub de gestion]**

**[ECRAN - survol d'un template, menu Edit / Duplicate / Delete]**

Un dernier point utile : cette page All Templates n'est pas qu'une liste de shortcodes. C'est aussi ton centre de gestion.

Quand tu survoles un template, tu vois apparaître trois options. Edit, pour modifier un template existant. Duplicate, pour créer une copie instantanée : parfait quand tu veux un feed similaire sans repartir de zéro. Et Delete, pour supprimer un template dont tu n'as plus besoin.

**[FACE CAMERA]**

Garde ce réflexe en tête : le shortcode est la voie qui fonctionne dans tous les cas. Que tu sois sur Gutenberg avec Kadence, comme sur un site schoolsWP, ou sur n'importe quel autre constructeur, le bloc Shortcode affichera toujours ton feed. Les constructeurs de page comme Elementor ou Beaver, qu'on verra ensuite, ne sont qu'un confort supplémentaire. Le shortcode, lui, reste ta base.

---

**[OUTRO - face camera]**

Tu sais maintenant ce qu'est un shortcode, où le trouver dans la page Templates, et comment le poser sur n'importe quelle page avec le bloc Shortcode. C'est la mécanique d'affichage que tu vas réutiliser tout au long de la formation, et notamment dans le cas pratique du Module 7. Dans la prochaine leçon, on voit comment afficher tes templates directement dans Elementor, sans passer par le bloc Shortcode. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Exemple visuel de shortcode `[wp_social_ninja id="100" platform="youtube"]` affiché en gros, surligné (section 1)
- Page WP Social Ninja → Templates avec la colonne ShortCode bien visible (section 2)
- Clic sur le shortcode dans la liste + petit toast "copié" (section 2)
- Éditeur de blocs WordPress : ajout du bloc Shortcode, collage, bouton Publier (section 3)
- Survol d'un template avec le menu Edit / Duplicate / Delete (section 4)
- Page finale en ligne avec le feed rendu, pour montrer le résultat (section 3)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : rester face camera ou slide simple, c'est du concept (pas de screencast)
- Sections 2 et 3 : screencast réel, clics dans l'interface, du copie au collage
- Section 4 : screencast court sur le survol, puis retour face camera pour le réflexe shortcode universel
- Outro : face camera, CTA visuel vers la leçon 6.2

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Ce qu'est un shortcode | 1:15 |
| Section 2 - Trouver et copier | 1:15 |
| Section 3 - Poser sur une page | 1:45 |
| Section 4 - Hub de gestion | 1:00 |
| Outro | 0:15 |
| **Total** | **~6:00** |

### Sources

- Doc : `sources/docs/guide__integrations__shortcode-usage.md`
- Doc : `sources/docs/guide__getting-started__templates-overview.md` (gestion des templates : Edit / Duplicate / Delete)
- Doc : `sources/docs/guide__integrations__integrations-overview.md` (le shortcode comme méthode de base avant les page builders)
