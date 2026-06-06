# Leçon 7.5 - SEO et finitions : schema, performance, responsive, publication

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 7 - Cas pratique schoolsWP : la page Vidéos
- **Durée cible** : 8 min (~1120 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Finaliser la page Vidéos : régler les réglages globaux de performance YouTube, vérifier le responsive, soigner le référencement de la page, et publier proprement.
- **Prérequis** : Leçon 7.4 vue (page assemblée avec les 4 sections).

---

## Script narration

**[INTRO - face camera]**

Ta page fonctionne, les quatre grilles s'affichent. On pourrait publier tout de suite, mais on ne va pas le faire. Les finitions, c'est ce qui sépare une page qui marche d'une page qui performe.

Dans cette dernière leçon, on règle quatre choses : la performance avec le cache, le responsive sur mobile, le référencement de la page, et enfin la publication. Je te dis aussi un mot honnête sur le schema vidéo, pour ne pas te vendre du rêve. C'est parti.

---

**[SECTION 1 - Performance : le cache global YouTube]**

**[ECRAN - WP Social Ninja → Settings → Feed Platforms → YouTube Settings]**

On commence par la performance, parce qu'afficher vingt vignettes ne doit pas ralentir ta page. WP Social Ninja met les feeds en cache, c'est-à-dire qu'il garde une copie locale au lieu d'interroger YouTube à chaque visite.

Tu trouves ces réglages dans WP Social Ninja, puis Settings, onglet Feed Platforms, puis YouTube Settings. Ce sont des réglages globaux, ils valent pour tous tes feeds YouTube d'un coup.

**[ECRAN - réglage Check New Feeds Every]**

Premier réglage : Check New Feeds Every, la fréquence de vérification. Il décide à quelle cadence le plugin va voir si tu as publié de nouvelles vidéos : six heures, un jour, une semaine. Pour une page de tutos, tu ne publies pas dix fois par jour, donc un intervalle long comme un jour est parfait. Plus l'intervalle est long, plus ta page charge vite.

**[ECRAN - bouton Clear Cache]**

Juste à côté, le bouton Clear Cache, vider le cache. Garde-le en tête : si un jour tes vignettes ne se mettent pas à jour ou affichent une ancienne version, ce bouton force le plugin à récupérer le contenu frais de YouTube immédiatement.

---

**[SECTION 2 - Performance : l'optimisation des images]**

**[ECRAN - toggle Optimize Image dans YouTube Settings]**

Toujours dans YouTube Settings, il y a un réglage Optimize Image, optimiser l'image. Activé, il allège le chargement de la page. Mais attention au compromis, et c'est important : la doc le dit clairement, si tu actives cette option, les vidéos ne se lancent plus directement dans le feed.

Pour notre page, on a choisi le mode de lecture Popup à la leçon précédente, donc la vidéo s'ouvre dans une fenêtre superposée, pas en place. Selon ce que tu veux privilégier, vitesse ou lecture en place, tu décides. Mon conseil pour une bibliothèque de tutos : teste avec, regarde le rendu, et garde-le si la lecture en popup reste fluide. Il y a aussi un bouton Reset Local Images si tes miniatures n'apparaissent pas correctement.

---

**[SECTION 3 - Responsive : vérifier le rendu mobile]**

**[ECRAN - onglet Style d'un template, icônes Desktop / Tablet / Mobile]**

Le responsive, c'est-à-dire l'adaptation à la taille de l'écran. Une partie est déjà gérée par les colonnes qu'on a réglées à la leçon 3 : quatre sur desktop, deux sur tablette, une sur mobile.

Pour aller plus loin, ouvre l'onglet Style d'un template. En haut du panneau, tu as trois icônes : Desktop, Tablet et Mobile. Quand tu cliques sur Mobile par exemple, les ajustements de style que tu fais ne s'appliquent qu'à cette taille d'écran. Tu peux ainsi réduire une taille de police ou un espacement uniquement sur mobile.

**[FACE CAMERA]**

Le vrai test, c'est de regarder ta page sur ton propre téléphone, en conditions réelles. Vérifie que les vignettes ne sont pas écrasées, que les titres restent lisibles, et que le bouton de lecture est facile à toucher. Une page Vidéos se consulte beaucoup sur mobile, ne néglige pas ce passage.

---

**[SECTION 4 - SEO de la page et le mot honnête sur le schema vidéo]**

**[ECRAN - réglages SEO de la page : titre, meta description, slug /videos/]**

Parlons référencement. Le premier levier, c'est ta page elle-même. Soigne le titre SEO et la meta description dans ton plugin de référencement, garde le slug propre en barre videos barre, et profite des titres H2 par thème qu'on a posés : ils disent clairement à Google de quoi parle chaque section.

**[FACE CAMERA]**

Maintenant, le point honnête sur le schema. WP Social Ninja propose un Schema Snippet, des données structurées pour Google. Mais lis bien la doc : cette fonction est faite pour les avis clients, pas pour les feeds vidéo. Elle a besoin d'un en-tête business et de notes pour produire son schema, ce qui n'a aucun sens pour une page de tutos.

Donc, sois clair là-dessus : pour ta page Vidéos, n'active pas ce Schema Snippet, il n'est pas conçu pour ça. Si un jour tu veux un vrai schema VideoObject pour tes vidéos, ça passe par un plugin SEO dédié à la vidéo, pas par WP Social Ninja. Je préfère te le dire que te laisser cliquer un réglage inutile.

---

**[SECTION 5 - Publier et vérifier]**

**[ECRAN - bouton Publish de la page, puis page en ligne sur schoolswp.com/videos/]**

On publie. Tu cliques sur Publish, et ta page Vidéos est en ligne. Mais on ne s'arrête pas au clic : on va la voir en vrai.

Ouvre l'adresse barre videos barre et déroule. Vérifie quatre choses. Un : les quatre sections sont là, dans le bon ordre, avec le bon thème. Deux : chaque grille affiche le bon nombre de vidéos, cinq, sept, quatre et quatre. Trois : un clic sur une vignette lance bien la vidéo. Quatre : la page reste rapide et propre sur mobile.

Si une vidéo manque, retour au template concerné pour vérifier son identifiant. Si rien ne se met à jour, le bouton Clear Cache qu'on a vu. Tu as maintenant une page Vidéos complète, à jour automatiquement, et entièrement sous ton contrôle.

---

**[OUTRO - face camera]**

Et voilà, le cas pratique est bouclé, et la masterclass aussi. Tu es parti d'une chaîne YouTube et d'une maquette, et tu as construit une page Vidéos réelle : clé API, quatre templates Specific Videos, quatre shortcodes, mise en page Kadence, performance et publication. Tu sais refaire tout ça pour ta propre chaîne.

Tu maîtrises désormais WP Social Ninja de bout en bout, des feeds aux avis, du chat aux notifications, jusqu'à un projet concret livré. Bravo pour le parcours, et à toi de jouer sur ton site.

---

## Notes de production

### Captures d'écran suggérées

- WP Social Ninja → Settings → Feed Platforms → YouTube Settings, vue d'ensemble du panneau (section 1)
- Réglage Check New Feeds Every (dropdown) + bouton Clear Cache (section 1)
- Toggle Optimize Image avec un encart rappelant le compromis lecture directe (section 2)
- Onglet Style d'un template, icônes Desktop / Tablet / Mobile en haut du panneau (section 3)
- Page Vidéos affichée sur un mockup de téléphone, scroll mobile (section 3)
- Réglages SEO de la page (titre, meta description, slug /videos/) (section 4)
- Encart "Schema Snippet = avis, pas vidéo" avec croix rouge sur le toggle (section 4)
- Clic Publish + page en ligne sur schoolswp.com/videos/, lancement d'une vidéo en popup (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 3 : screencast réglages + test mobile
- Section 2 : insister visuellement sur le compromis Optimize Image
- Section 4 : retour face camera pour le mot honnête sur le schema, ton direct, pas de survente
- Section 5 : screencast publication puis page live
- Outro : face camera, clôture de la masterclass, ton chaleureux

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:30 |
| Section 1 - Cache global | 1:30 |
| Section 2 - Optimisation images | 1:15 |
| Section 3 - Responsive | 1:30 |
| Section 4 - SEO et schema | 1:45 |
| Section 5 - Publier et vérifier | 1:15 |
| Outro | 0:15 |
| **Total** | **~8:00** |

### Sources

- Doc : `sources/docs/guide__social-feeds__youtube-settings.md` (Check New Feeds Every, Clear Cache, Optimize Image, Reset Local Images)
- Doc : `sources/docs/guide__customization-design__website-styling-for-feeds-and-reviews.md` (responsive Desktop/Tablet/Mobile)
- Doc : `sources/docs/guide__business-reviews__configure-schema.md` (Schema Snippet réservé aux reviews, pas aux feeds)
- Maquette : `content/inspirations/youtube-hub-mockup.html` (slug /videos/, comptes 5/7/4/4)
