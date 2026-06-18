# Leçon 2.3 - YouTube : layouts, skins, réglages et filtres de curation

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 2 - Social Feeds
- **Durée cible** : 9 min (~1260 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Configurer l'apparence d'un feed YouTube (layout grille ou carrousel, skins) et maîtriser les filtres de curation pour ne montrer que les bonnes vidéos, dans le bon ordre.
- **Prérequis** : Leçon 2.2 terminée (chaîne YouTube connectée, type de feed choisi).

---

## Script narration

**[INTRO - face camera]**

Dans la leçon précédente, tu as connecté ta chaîne et choisi ton type de feed. Maintenant, on s'occupe de l'apparence et du tri. Parce qu'un feed YouTube qui affiche toutes tes vidéos en vrac, ce n'est pas une vitrine, c'est un fourre-tout.

Dans cette leçon, on voit la disposition (grille ou carrousel), les skins prêts à l'emploi, les réglages d'affichage de chaque vidéo, et surtout les filtres de curation qui te donnent la main sur ce qui apparaît. On finit par les réglages globaux de performance. C'est parti.

---

**[SECTION 1 - Layout : grille ou carrousel]**

**[ECRAN - éditeur de template YouTube, onglet General → section Template]**

Tout se passe dans l'onglet General de ton template, section Template. C'est elle qui définit la structure visuelle.

Premier réglage : le Layout Type. Sur YouTube, tu as deux dispositions. La grille, ou Grid : un quadrillage propre, multi-colonnes, où toutes les vignettes ont la même hauteur. C'est net, symétrique, parfait pour une page de vidéos. Et le carrousel, ou Carousel : un slider horizontal dans lequel le visiteur fait défiler les vidéos. Idéal quand tu veux gagner de la place, par exemple sur une page d'accueil.

Juste en dessous, tu règles le nombre de colonnes séparément pour le bureau, la tablette et le mobile. Par exemple trois colonnes sur ordinateur, deux sur tablette, une sur mobile. Et le Columns Gap fixe l'espace en pixels entre chaque vidéo.

**[ECRAN - panneau Carousel Settings qui apparaît quand Layout = Carousel]**

Si tu choisis le carrousel, un panneau Carousel Settings apparaît. Tu y trouves l'autoplay pour faire défiler automatiquement, la vitesse de défilement en millisecondes, le nombre d'éléments visibles à la fois, le nombre d'éléments qui défilent à chaque glissement, et le type de navigation : flèches, points, les deux, ou aucun. Pour un site sobre, je te conseille les flèches sans autoplay agressif.

---

**[SECTION 2 - Les skins : Vega, Sirius, Polaris, Rigel]**

**[ECRAN - dropdown Template, défilement des skins]**

Toujours dans la section Template, le réglage Template, c'est le skin. Ce sont des habillages visuels prêts à l'emploi, avec des noms d'étoiles : Vega, Sirius, Polaris, Rigel.

Chaque skin change le style des cartes, des polices et de la disposition des éléments. Le mieux, c'est de cliquer de l'un à l'autre et de regarder l'aperçu en direct. Tu choisis celui qui colle le plus à ton site, et tu ajusteras les détails dans l'onglet Style ensuite.

Mon conseil : pars d'un skin proche de ton rendu cible, ça t'évitera de tout reconstruire à la main.

---

**[SECTION 3 - Les filtres de curation]**

**[ECRAN - onglet General → section Filters]**

On arrive au cœur du contrôle : la section Filters. C'est elle qui décide quelles vidéos apparaissent et dans quel ordre.

Premier réglage : Number of Videos to Display, le nombre de vidéos affichées au chargement. Attention, c'est différent du Total Feed vu en leçon 2.2, qui est le nombre de vidéos récupérées depuis YouTube. Ici, c'est ce qui s'affiche d'emblée.

Ensuite, Posts Order, l'ordre. Tu as Newest pour les plus récentes d'abord, Oldest pour les plus anciennes, et Random pour un ordre aléatoire à chaque chargement.

**[ECRAN - champs Show Posts / Hide Posts / Hide Specific Videos]**

Puis viennent les vrais outils de curation. Show Posts Containing These Words : tu n'affiches que les vidéos dont le titre ou la description contient certains mots ou hashtags. Pratique pour isoler une thématique. Son miroir, Hide Posts Containing These Words : tu exclus les vidéos qui contiennent certains mots. Parfait pour écarter du hors-sujet.

Et le plus précis : Hide Specific Videos. Tu colles les identifiants des vidéos que tu ne veux pas voir, et elles disparaissent du feed. Contrôle au cas par cas.

Avec ces trois leviers, tu transformes un flux brut en sélection éditoriale. C'est exactement ce qui sépare une vitrine soignée d'un mur de vidéos en vrac.

---

**[SECTION 4 - Affichage de chaque vidéo et lecture]**

**[ECRAN - onglet General → section Video]**

Section Video maintenant : elle contrôle l'apparence de chaque vidéo et la façon dont elle se lit.

Le réglage clé, c'est le Play Mode. Popup ouvre la vidéo dans une fenêtre superposée sur ton site, c'est le défaut recommandé, le visiteur reste chez toi. In-line lit la vidéo directement dans le feed. YouTube Player renvoie le visiteur sur YouTube. Le mode Gallery, lui, est réservé à la version Pro.

Ensuite, une série d'interrupteurs te laissent afficher ou masquer : le titre, l'icône de lecture, la durée, la date, le compteur de vues, la description, et le nom de la chaîne. Tu peux aussi limiter le nombre de mots du titre pour garder une mise en page nette, et ajouter un bouton d'appel à l'action Watch Now sous chaque vidéo.

Une précision honnête : les compteurs de likes et de commentaires sont réservés à la version Pro. Sur la version gratuite, tu affiches déjà les vues, le titre et la durée, ce qui suffit largement pour une vitrine propre.

---

**[SECTION 5 - Header, bouton d'abonnement et pagination]**

**[ECRAN - sections Header, Subscribe Button, Pagination]**

Trois sections complémentaires pour finir le template.

Le Header, c'est la bannière en haut du feed : tu peux y afficher la bannière de la chaîne, le logo, le nom, le nombre d'abonnés, le nombre de vidéos, et un bouton Subscribe. Tu peux tout masquer d'un coup si tu veux un feed minimaliste.

Le Subscribe Button ajoute un bouton d'abonnement que tu places en haut, en bas, ou aux deux, avec un texte personnalisable comme "Abonne-toi sur YouTube".

Enfin, la Pagination : elle gère ce qui se passe en bas du feed. None affiche un nombre fixe de vidéos sans plus. Load More ajoute un bouton "voir plus". Prev Next permet d'aller à la page suivante. Concrètement, si tu affiches huit vidéos au départ et que tu charges quatre vidéos de plus à chaque clic, le visiteur explore sans surcharger la page au démarrage.

---

**[SECTION 6 - Réglages globaux : cache et images]**

**[ECRAN - WP Social Ninja → Settings → Feed Platforms → YouTube Settings]**

Un dernier endroit à connaître, et il ne se trouve pas dans le template. Va dans WP Social Ninja, Settings, onglet Feed Platforms, puis YouTube Settings. Ce sont les réglages globaux qui s'appliquent à tous tes feeds YouTube.

Check New Feeds Every fixe la fréquence à laquelle le plugin vérifie les nouvelles vidéos, par exemple toutes les six heures ou une fois par jour. Un intervalle plus long allège le chargement de ton site.

Clear Cache vide le cache immédiatement : c'est le réflexe quand un feed ne montre pas tes nouvelles vidéos. Optimize Image accélère le chargement, mais attention, comme l'indique le réglage, les vidéos ne se lisent alors plus directement dans le feed. Et Reset Local Images force le plugin à recharger toutes les vignettes.

**[FACE CAMERA]**

Le réflexe à garder : si une vidéo récente n'apparaît pas, ce n'est presque jamais un bug. C'est le cache. Un clic sur Clear Cache, et c'est réglé.

---

**[OUTRO - face camera]**

Tu sais maintenant donner une vraie apparence à ton feed YouTube : layout, skin, affichage des vidéos, et surtout les filtres pour curer ta sélection. Dans la prochaine leçon, on change de plateforme et on attaque Facebook : connexion, token, layouts, et les feeds spécifiques comme les albums et les events. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Section Template avec Layout Type (Grid / Carousel) et réglages de colonnes (section 1)
- Panneau Carousel Settings qui apparaît en mode carrousel (section 1)
- Dropdown Template montrant les skins Vega, Sirius, Polaris, Rigel avec aperçu (section 2)
- Section Filters complète, avec Show / Hide / Hide Specific Videos surlignés (section 3)
- Section Video avec le dropdown Play Mode déployé (section 4)
- Sections Header, Subscribe Button et Pagination (section 5)
- Settings → Feed Platforms → YouTube Settings, bouton Clear Cache mis en évidence en vert schoolsWP (section 6)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 5 : screencast dans l'éditeur de template, slides Kadence pour les récaps
- Section 3 : ralentir, c'est le cœur pédagogique de la leçon (curation)
- Section 6 : sortir de l'éditeur, montrer le chemin Settings → Feed Platforms
- Outro : face camera, CTA visuel vers la leçon 2.4

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Layout | 1:30 |
| Section 2 - Skins | 0:45 |
| Section 3 - Filtres de curation | 2:00 |
| Section 4 - Affichage vidéo | 1:30 |
| Section 5 - Header / abonnement / pagination | 1:30 |
| Section 6 - Réglages globaux | 1:00 |
| Outro | 0:15 |
| **Total** | **~9:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__youtube-feed-template-general-settings.md`
- Doc : `sources/docs/guide__social-feeds__youtube-settings.md`
- Doc (style header/title/item box) : `sources/docs/guide__social-feeds__style-connection-settings.md`
- Vidéos officielles : #1 (Give your YouTube Feed a Niche Look), #2 (Customize Your YouTube Feed)
