# Leçon 7.1 - Le projet : afficher ses tutos YouTube par thème sur son site

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 7 - Cas pratique schoolsWP : la page Vidéos
- **Durée cible** : 6 min (~840 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Comprendre le projet du module (une page Vidéos qui affiche les tutos YouTube triés par thème), la méthode retenue avec WP Social Ninja, et la liste des étapes à venir.
- **Prérequis** : Module 2 vu (feeds YouTube, type Specific Videos), notion de shortcode.

---

## Script narration

**[INTRO - face camera]**

On arrive au module final, et c'est le plus concret de toute la formation. Jusqu'ici tu as appris la mécanique de WP Social Ninja, plateforme par plateforme. Maintenant on construit quelque chose de réel, du début à la fin.

L'objectif : sur un vrai site WordPress, schoolswp.com, on va créer une page Vidéos qui affiche les tutoriels YouTube de la chaîne @michaelkihl, classés par thème. À la fin du module, tu auras une page propre, à jour, et tu sauras refaire exactement la même chose pour ta chaîne. On regarde d'abord à quoi ça ressemble, puis la méthode qu'on va suivre. C'est parti.

---

**[SECTION 1 - Le résultat qu'on vise]**

**[ECRAN - maquette de la page Vidéos schoolsWP]**

Voilà la cible. Une page avec un titre, une courte intro, et surtout quatre sections de vidéos, une par thème.

Premier thème : WordPress et Divi. Deuxième : WooCommerce. Troisième : les plugins WordPress. Quatrième : SEO et web. Chaque section a son titre, et en dessous une grille de vignettes YouTube. Une vignette, c'est la miniature de la vidéo, son titre, et un bouton de lecture. Quand un visiteur clique, la vidéo se lance.

Pourquoi trier par thème plutôt que tout afficher en vrac ? Parce que tes visiteurs ne cherchent pas un fil chronologique, ils cherchent un sujet. Quelqu'un qui veut apprendre WooCommerce doit trouver tes tutos WooCommerce regroupés au même endroit. C'est ça, l'idée de la page : transformer une chaîne YouTube en bibliothèque organisée sur ton propre site.

---

**[SECTION 2 - Pourquoi cette page sur ton site, et pas juste sur YouTube]**

**[FACE CAMERA]**

Tu vas me dire : mes vidéos sont déjà sur YouTube, pourquoi les remettre sur mon site ? Trois bonnes raisons.

D'abord, le visiteur reste chez toi. Au lieu de l'envoyer sur YouTube où il va se perdre dans les suggestions, il regarde ton contenu dans ton univers, avec ta marque autour.

Ensuite, tu gardes la main sur l'ordre et le tri. Sur YouTube, c'est l'algorithme qui décide. Sur ta page, c'est toi qui choisis quelles vidéos apparaissent et dans quelle section.

Enfin, le référencement. Une page Vidéos bien construite donne à Google une raison de plus de t'envoyer du trafic, et on verra en fin de module comment l'optimiser.

---

**[SECTION 3 - La méthode WP Social Ninja]**

**[ECRAN - slide "1 thème = 1 template" avec les 4 thèmes alignés]**

Maintenant, comment on fait ça techniquement. La règle est simple : un thème égale un template.

On va créer quatre templates YouTube dans WP Social Ninja. Un pour WordPress et Divi, un pour WooCommerce, un pour les plugins, un pour SEO et web. Chaque template est réglé sur le type de feed Specific Videos, celui qu'on a vu au Module 2. Souviens-toi, c'est le type qui te laisse choisir les vidéos une par une, par leur identifiant. C'est exactement ce qu'il nous faut pour curer chaque thème à la main.

Chaque template génère un shortcode, du style crochet wp underscore social underscore ninja, id égale un numéro, platform égale youtube, crochet. On posera ces quatre shortcodes l'un sous l'autre sur la page, et chacun affichera sa grille de vidéos. Quatre shortcodes, quatre sections, une page.

Le tout en version gratuite : le layout Grid, la grille qu'on voit dans la maquette, ne demande aucune licence Pro.

---

**[SECTION 4 - Le seul prérequis et le plan du module]**

**[ECRAN - slide "Plan du module 7"]**

Avant de construire, il y a un prérequis unique : la connexion de ta chaîne YouTube à WP Social Ninja. On l'a abordée au Module 2, et dans la prochaine leçon je te refais la création de la clé API YouTube Data v3 pas à pas, parce que c'est le point qui fait perdre du temps à tout le monde.

Voici le plan des cinq leçons. Leçon 2 : créer la clé API dans Google Cloud. Leçon 3 : créer les quatre templates Specific Videos et y coller les bons identifiants de vidéos. Leçon 4 : assembler la page avec les quatre shortcodes et la mettre en forme dans Kadence. Leçon 5 : les finitions, c'est-à-dire le schema, la performance, le responsive et la publication.

---

**[OUTRO - face camera]**

Tu as maintenant la vision d'ensemble : une page Vidéos triée en quatre thèmes, quatre templates Specific Videos, quatre shortcodes, le tout en gratuit. La seule clé à fabriquer avant de commencer, c'est la clé API YouTube. C'est précisément ce qu'on fait dans la prochaine leçon, écran par écran. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Maquette complète de la page Vidéos schoolsWP, scroll lent du haut vers les 4 sections (section 1)
- Zoom sur une vignette (miniature + titre + bouton play vert) pour montrer l'anatomie d'une carte (section 1)
- Slide "1 thème = 1 template" : les 4 thèmes alignés avec leur nombre de vidéos (5 / 7 / 4 / 4) (section 3)
- Slide d'un shortcode type `[wp_social_ninja id="X" platform="youtube"]` (section 3)
- Slide "Plan du module 7" : les 5 leçons listées, leçon courante surlignée en vert schoolsWP (section 4)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Section 1 : screencast de la maquette, mouvement de scroll posé
- Section 2 : retour face camera, ton direct, pas de slide
- Section 3 : slides Kadence, accent vert sur le mot Specific Videos
- Section 4 : slide plan, puis retour face camera pour l'outro

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Le résultat | 1:30 |
| Section 2 - Pourquoi sur ton site | 1:15 |
| Section 3 - La méthode | 1:30 |
| Section 4 - Prérequis et plan | 1:00 |
| Outro | 0:15 |
| **Total** | **~6:00** |

### Sources

- Maquette : `content/inspirations/youtube-hub-mockup.html`
- Doc : `sources/docs/guide__social-feeds__youtube-feed-types.md` (type Specific Videos)
- Doc : `sources/docs/guide__integrations__shortcode-usage.md`
- Renvoi formation : leçon 2.2 (connexion YouTube et 5 types de feed)
