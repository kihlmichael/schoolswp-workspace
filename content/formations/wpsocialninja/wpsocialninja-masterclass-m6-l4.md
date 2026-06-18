# Leçon 6.4 - Fluent Forms : collecter des avis via formulaire

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 6 - Intégrations et fonctions avancées
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Mettre en place une chaîne complète de collecte d'avis avec Fluent Forms : activer le module, construire le formulaire, mapper les champs vers WP Social Ninja, créer un template d'affichage, et savoir activer la modération avant publication.
- **Prérequis** : Module 3 vu (Business Reviews), WP Social Ninja Pro actif, plugin Fluent Forms installé.

---

## Script narration

**[INTRO - face camera]**

Jusqu'ici, on a affiché des avis venus de plateformes externes : Google, Facebook, Yelp. Mais tu peux aussi collecter tes propres avis, directement sur ton site, via un formulaire. C'est tout l'intérêt de l'intégration avec Fluent Forms.

Le principe : ton visiteur remplit un formulaire avec une note en étoiles et un commentaire. WP Social Ninja récupère automatiquement ces soumissions et les affiche comme des avis. Dans cette leçon, on monte la chaîne complète, du formulaire à l'affichage, et on voit comment modérer les avis avant qu'ils n'apparaissent. C'est parti.

Un point à savoir avant de commencer : afficher des avis collectés via Fluent Forms est une fonctionnalité premium. Il te faut WP Social Ninja Pro et le plugin Fluent Forms installé.

---

**[SECTION 1 - Activer le module dans Fluent Forms]**

**[ECRAN - Fluent Forms → Integrations]**

Première étape : activer la connexion côté Fluent Forms. Depuis ton tableau de bord WordPress, tu vas dans Fluent Forms, puis Integrations.

Tu cherches WP Social Ninja dans la liste, ou tu descends pour le trouver, et tu cliques sur le bouton pour activer le module. Ce geste connecte Fluent Forms et WP Social Ninja, et leur permet de partager des données. C'est le branchement de base, à faire une seule fois.

---

**[SECTION 2 - Construire le formulaire d'avis]**

**[ECRAN - Fluent Forms, création ou édition d'un formulaire]**

Maintenant, on construit le formulaire qui va recueillir les avis. Tu retournes dans Fluent Forms. Tu peux créer un nouveau formulaire ou en modifier un existant.

L'important, c'est que ton formulaire contienne les bons champs. Il te faut au minimum un champ Name pour le nom, un champ Email Address, un champ Text pour le commentaire, et un champ Ratings pour la note en étoiles.

Bonne nouvelle : le champ Ratings de Social Ninja est désormais disponible directement dans Fluent Forms. Tu n'as donc pas besoin de bricoler une note maison, le champ étoiles est prêt à l'emploi.

---

**[SECTION 3 - Configurer l'intégration sur le formulaire]**

**[ECRAN - Settings & Integrations → Configure Integration]**

Activer le module globalement ne suffit pas : tu dois dire à ce formulaire précis d'envoyer ses données à WP Social Ninja.

Dans l'éditeur de ton formulaire, tu vas dans l'onglet Settings and Integrations. Dans le menu de gauche, tu choisis Configure Integration. Tu cliques sur le bouton Add New Integration, et tu sélectionnes WPSocial Ninja Integration dans la liste déroulante.

---

**[SECTION 4 - Mapper les champs : l'étape clé]**

**[ECRAN - panneau de mapping des champs]**

Un nouveau panneau de configuration apparaît. C'est l'étape la plus importante, alors prends ton temps. Tu dois mapper tes champs, c'est-à-dire dire à WP Social Ninja quel champ du formulaire correspond à quoi.

D'abord, Name : tu donnes un nom interne à cette intégration, par exemple "Formulaire avis clients". C'est juste pour t'y retrouver. Ensuite, Integration Source : tu choisis Fluent Forms dans la liste.

Viennent les champs obligatoires, ceux à ne pas rater. Ratings, la note : tu sélectionnes le shortcode des étoiles de Social Ninja, c'est l'option inputs wpsr rating elem dans la liste. Reviewer Name, le nom de l'auteur : tu choisis le champ où l'utilisateur saisit son nom. Et Comment, le texte de l'avis : tu sélectionnes le shortcode inputs input text.

**[ECRAN - champs optionnels du mapping]**

Ensuite, des champs optionnels, que tu remplis si ton formulaire les propose. Reviewer Email, l'adresse, généralement pas affichée publiquement mais utile pour tes archives. Reviewer Image, si ton formulaire a un champ d'upload pour une photo. Reviewer URL, pour un lien vers le site ou le réseau de l'auteur. ReviewTitle, pour un titre d'avis. Et Category, pour ranger automatiquement les avis par catégorie.

Un réglage utile au passage : Conditional Logic. En l'activant, tu peux poser une règle, par exemple n'envoyer à WP Social Ninja que les avis notés quatre étoiles ou plus. Pratique pour filtrer en amont.

Quand tout est mappé, tu cliques sur Save Feed. Puis sur Save Form. Tu peux ensuite copier le shortcode du formulaire et le coller sur une page.

---

**[SECTION 5 - Créer le template d'affichage et modérer]**

**[ECRAN - WP Social Ninja → Templates → Add Review Template]**

Le formulaire collecte les avis, mais il faut maintenant un template pour les afficher. Tu vas dans WP Social Ninja, puis Templates, Add New Template, et tu choisis Add Review Template.

Dans l'éditeur de template, tu vas dans General, puis Platforms. Tu sélectionnes Fluent Forms dans la liste des plateformes. Tu stylises ton template, layout et couleurs, et tu cliques sur Save. Désormais, tout avis soumis via ton formulaire est automatiquement récupéré et affiché par ce template.

**[ECRAN - Settings → Reviews Platform → Fluent Form Settings, modération]**

Dernier point, et il est important : la modération. Par défaut, les avis peuvent apparaître instantanément. Si tu veux valider chaque avis avant qu'il ne soit public, tu vas dans WP Social Ninja, Settings, Reviews Platform, puis Fluent Form Settings. Tu actives l'option qui impose une approbation manuelle des avis et témoignages, et tu sauvegardes.

À partir de là, chaque nouvelle soumission arrive dans l'onglet Reviews de WP Social Ninja, où tu approuves ou rejettes avant publication.

**[FACE CAMERA]**

Concrètement, tu poses deux éléments sur ton site. Le shortcode du formulaire, sur une page "Laisser un avis". Et le shortcode du template d'affichage, sur ta page de témoignages. Deux shortcodes, exactement la mécanique de la leçon 6.1.

---

**[OUTRO - face camera]**

Tu sais maintenant collecter tes propres avis via Fluent Forms, du module à l'affichage, et tu maîtrises la modération pour garder la main sur ce qui est publié. Dans la prochaine leçon, on regarde l'IA intégrée à WP Social Ninja, avec OpenAI et OpenRouter, et à quoi elle sert vraiment sur tes avis. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Fluent Forms → Integrations, toggle WP Social Ninja activé (section 1)
- Éditeur de formulaire Fluent Forms avec les champs Name, Email, Text, Ratings (section 2)
- Settings & Integrations → Configure Integration → Add New Integration → WPSocial Ninja Integration (section 3)
- Panneau de mapping : Ratings, Reviewer Name, Comment surlignés comme obligatoires (section 4)
- Vue des shortcodes à mapper (inputs.wpsr_rating_elem, inputs.input_text) (section 4)
- Conditional Logic : règle "4 étoiles ou plus" (section 4)
- WP Social Ninja → Templates → Add Review Template → General → Platforms → Fluent Forms (section 5)
- Settings → Reviews Platform → Fluent Form Settings : toggle d'approbation manuelle (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP, mentionner Pro requis sans appuyer
- Sections 1 à 4 : screencast réel, alterner Fluent Forms et le panneau de mapping
- Section 4 : ralentir nettement sur les trois champs obligatoires (Ratings, Reviewer Name, Comment), c'est le point de friction
- Section 5 : screencast WP Social Ninja, insister sur la modération avant publication, puis retour face camera sur les "deux shortcodes"
- Outro : face camera, CTA visuel vers la leçon 6.5

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:40 |
| Section 1 - Activer le module | 0:45 |
| Section 2 - Construire le formulaire | 1:00 |
| Section 3 - Configurer l'intégration | 1:00 |
| Section 4 - Mapper les champs | 2:00 |
| Section 5 - Template et modération | 1:20 |
| Outro | 0:15 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__business-reviews__fluent-forms-review.md`
- Doc : `sources/docs/guide__integrations__shortcode-usage.md` (affichage du formulaire et du template via shortcode)
- Vidéo officielle : #47 (Integrate Fluent Forms with WP Social Ninja)
