# Leçon 7.3 - Créer 4 templates "Specific Videos" (1 par thème) et curer les IDs

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 7 - Cas pratique schoolsWP : la page Vidéos
- **Durée cible** : 10 min (~1400 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Créer quatre templates YouTube de type Specific Videos, récupérer et coller les identifiants des vidéos pour chaque thème, régler le layout Grid et les options d'affichage, puis dupliquer pour aller plus vite.
- **Prérequis** : Leçon 7.2 vue (clé API connectée et API v3 activée).

---

## Script narration

**[INTRO - face camera]**

La clé est branchée, le moteur tourne. On entre maintenant dans le cœur du cas pratique : la curation. On va créer quatre templates, un par thème, et dans chacun on choisira nos vidéos à la main grâce au type Specific Videos.

Je te montre d'abord comment trouver l'identifiant d'une vidéo YouTube, puis on construit le premier template de A à Z. Une fois que tu auras compris le premier, les trois autres se feront en deux minutes grâce à la duplication. C'est parti.

---

**[SECTION 1 - L'identifiant d'une vidéo, le carburant de Specific Videos]**

**[ECRAN - URL YouTube avec le segment après v= surligné]**

Avant de toucher au plugin, comprenons ce qu'on va lui donner à manger. Le type Specific Videos fonctionne par identifiant de vidéo. L'identifiant, c'est la suite de caractères qui suit v égale dans l'URL YouTube.

Exemple concret de notre cas : pour le tuto Vider le cache WordPress avec Divi, l'URL contient v égale, puis l'identifiant 6CwIiZNzimQ. C'est uniquement cette partie qu'on copie, pas l'URL entière, et surtout pas ce qu'il y a après une éventuelle esperluette comme et égale, qui sert juste à indiquer un moment de la vidéo.

Bonne nouvelle : pour ce cas pratique, les quatre listes d'identifiants sont déjà préparées, regroupées par thème. Tu n'as plus qu'à les coller. On va les voir thème par thème.

---

**[SECTION 2 - Créer le premier template : WordPress et Divi]**

**[ECRAN - WP Social Ninja → Templates → Create New Template → YouTube]**

On crée le premier template. Tu vas dans WP Social Ninja, puis Templates, et tu cliques sur Create New Template, créer un nouveau template. Tu choisis la plateforme YouTube.

Tu arrives dans l'éditeur de template, organisé en trois onglets : General pour le contenu, Style pour le visuel, Connection pour la connexion. On reste sur General.

**[ECRAN - onglet General, section Source, dropdown Feed Type → Specific Videos]**

Première chose, la section Source. Dans le menu Feed Type, tu sélectionnes Specific Videos, les vidéos choisies. Un champ Video ID apparaît juste en dessous. C'est ici qu'on colle nos identifiants.

**[ECRAN - champ Video ID rempli avec les 5 IDs séparés par virgule, bouton Fetch Videos]**

Pour le thème WordPress et Divi, on a cinq vidéos. Tu colles les cinq identifiants dans le champ, séparés par une virgule, sans espace inutile : 6CwIiZNzimQ, PznWFDqB8uo, UUWXx5Fryic, TH8cR0OPXUA, 5d6Q4o underscore T1OQ. Ensuite tu cliques sur le bouton Fetch Videos, récupérer les vidéos. WP Social Ninja interroge YouTube et affiche les cinq vignettes dans l'aperçu. Si une vidéo manque, c'est qu'un identifiant est mal copié, vérifie celui-là.

---

**[SECTION 3 - Régler le layout Grid et les options d'affichage]**

**[ECRAN - section Template, Layout Type → Grid, Number of Columns]**

On descend dans la section Template, le réglage visuel de structure. Dans Layout Type, tu choisis Grid, la grille. C'est la disposition de notre maquette, et c'est inclus dans la version gratuite.

Juste en dessous, Number of Columns te laisse fixer le nombre de colonnes pour ordinateur, tablette et mobile. Pour coller à la maquette, mets quatre colonnes sur desktop, deux sur tablette, une sur mobile. On affinera le rendu responsive au Module suivant, mais ce réglage de base suffit déjà. Tu peux aussi ajuster Columns Gap, l'espace entre les vignettes.

**[ECRAN - section Video, toggles Display Title / Play Icon / Duration, Play Mode → Popup]**

Toujours dans General, la section Video contrôle ce qui s'affiche sur chaque vignette. Active Display Title pour le titre, Display Play Icon pour le bouton de lecture, et Display Duration pour la durée. Pour Play Mode, le mode de lecture, choisis Popup : la vidéo s'ouvre dans une fenêtre superposée sur ton site, c'est le réglage recommandé pour garder le visiteur chez toi.

Petit rappel : les compteurs de likes et de commentaires sont réservés à la version Pro. Pour notre page, on n'en a pas besoin, on reste en gratuit.

---

**[SECTION 4 - Filtres et ordre des vidéos]**

**[ECRAN - section Filters, Posts Order, Number of Videos to Display]**

Dans la section Filters, deux réglages utiles. Posts Order, l'ordre des vidéos : tu as Newest pour les plus récentes d'abord, Oldest pour les plus anciennes, ou Random pour mélanger. Pour une bibliothèque de tutos, je te conseille Newest, le plus récent en tête.

Number of Videos to Display fixe combien de vignettes s'affichent au chargement. Comme notre premier thème compte exactement cinq vidéos, mets cinq, tout s'affiche d'un coup, pas besoin de pagination.

Bon à savoir : il existe aussi un champ Hide Specific Videos, pour masquer une vidéo précise par son identifiant. On ne s'en sert pas ici puisqu'on a choisi nos vidéos une par une, mais retiens qu'il existe.

Une fois tout réglé, tu nommes le template, par exemple Vidéos WordPress et Divi, et tu cliques sur Save. Ton premier template est prêt.

---

**[SECTION 5 - Dupliquer pour les trois thèmes restants]**

**[ECRAN - Templates, survol d'un template → option Duplicate]**

Maintenant, le raccourci. Plutôt que tout refaire trois fois, on duplique. Sur la page Templates, tu survoles ton template WordPress et Divi : trois options apparaissent, Edit, Duplicate et Delete. Tu cliques sur Duplicate. WP Social Ninja crée une copie qui garde déjà tous tes réglages de layout et d'affichage.

**[ECRAN - édition de la copie, champ Video ID remplacé par la liste WooCommerce]**

Tu ouvres la copie, tu vas dans la section Source, et tu remplaces les identifiants par ceux du nouveau thème. Tu n'as plus à toucher au layout, il est déjà bon.

**[ECRAN - slide récap des 4 thèmes et de leurs IDs]**

Voici les trois listes restantes. WooCommerce, sept vidéos : hRo5khs3eLw, K2kkrJTiUOc, pLXmhv411Wc, XRbie2H2K7s, 5o1M4Bl6M3g, FlLVtITJGiQ, cy37XlZhTso. Pour ce template, comme il y a sept vidéos, pense à passer Number of Videos to Display à sept.

Plugins WordPress, quatre vidéos : toyKsSY91UI, 9TLtjcKIurc, nmdukyy0fdg, b06x6zKWpa4.

SEO et web, quatre vidéos : NbnSSa4Wlwg, m0tz1NTdLUw, Djtk3R2 tiret 4Yg, CzYuQpXGe94.

À chaque fois : tu dupliques, tu remplaces les identifiants, tu cliques sur Fetch Videos pour vérifier l'aperçu, tu ajustes le nombre de vidéos affichées, tu renommes, tu sauvegardes. Au bout du compte, tu as quatre templates, un par thème, tous prêts.

---

**[OUTRO - face camera]**

Tes quatre templates Specific Videos sont créés et curés. Chacun connaît exactement les vidéos qu'il doit montrer. Et grâce à la duplication, les trois derniers t'ont pris quelques minutes au lieu de tout reconstruire. Dans la prochaine leçon, on récupère les quatre shortcodes et on assemble la vraie page sur schoolswp.com, avec la mise en forme Kadence par-dessus. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- URL YouTube avec le segment après `v=` surligné en vert, en montrant qu'on coupe avant une éventuelle esperluette `&` (section 1)
- Templates → Create New Template → choix plateforme YouTube (section 2)
- Onglet General → Source → Feed Type → Specific Videos, apparition du champ Video ID (section 2)
- Champ Video ID rempli avec les 5 IDs WordPress et Divi + clic Fetch Videos + aperçu des 5 vignettes (section 2)
- Section Template : Layout Type → Grid, Number of Columns 4/2/1 (section 3)
- Section Video : toggles Title / Play Icon / Duration, Play Mode → Popup (section 3)
- Section Filters : Posts Order → Newest, Number of Videos to Display (section 4)
- Survol d'un template → option Duplicate, puis édition de la copie (section 5)
- Slide récap des 4 thèmes avec leurs listes d'IDs, thème courant surligné (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 5 : alternance screencast (clics réels) et slides récap d'IDs
- Section 2 : ralentir sur le collage des IDs séparés par virgule, c'est la manip clé
- Section 5 : insister sur le gain de temps de la duplication, ton rassurant
- Outro : face camera, CTA visuel vers la leçon 7.4

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - L'identifiant vidéo | 1:30 |
| Section 2 - Premier template | 2:30 |
| Section 3 - Layout Grid et affichage | 2:00 |
| Section 4 - Filtres et ordre | 1:30 |
| Section 5 - Dupliquer x3 | 1:45 |
| Outro | 0:15 |
| **Total** | **~10:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__youtube-feed-types.md` (Specific Videos, IDs multiples séparés par virgule)
- Doc : `sources/docs/guide__social-feeds__youtube-feed-template-general-settings.md` (Source, Template, Filters, Video)
- Doc : `sources/docs/guide__integrations__shortcode-usage.md` (Duplicate template)
- Maquette : `content/inspirations/youtube-hub-mockup.html` (4 thèmes + IDs + durées)
- Renvoi formation : leçon 2.2 (type Specific Videos)
