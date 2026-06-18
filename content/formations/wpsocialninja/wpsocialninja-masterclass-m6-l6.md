# Leçon 6.6 - Import/Export et réglages de performance

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 6 - Intégrations et fonctions avancées
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Exporter et importer ses contenus WP Social Ninja entre deux sites, comprendre la limite des avis non exportables, optimiser la performance via le format WebP, gérer le RGPD, et savoir déléguer l'accès via les Managers.
- **Prérequis** : Modules 2 et 3 vus (au moins quelques templates et avis créés).

---

## Script narration

**[INTRO - face camera]**

Pour clôturer ce module, on s'occupe de trois sujets pratiques mais souvent négligés : transférer tes contenus d'un site à un autre, garder ton site rapide malgré les images des feeds, et déléguer l'accès au plugin sans donner les pleines clés.

Ces réglages ne sont pas glamours, mais ce sont eux qui font la différence entre un site bien tenu et un site qui rame ou qui se gère mal à plusieurs. Dans cette leçon, on voit l'import et l'export, les réglages de performance, le RGPD, et la gestion des accès. C'est parti.

---

**[SECTION 1 - Exporter tes contenus]**

**[ECRAN - WP Social Ninja → Tools → Export]**

Commençons par l'export. Tu vas dans la section Tools de WP Social Ninja, dans la barre latérale gauche de WordPress. Tu y trouves les options Export et Import.

Tu choisis d'abord le type de données à exporter dans le menu déroulant. Tu as le choix entre : les Reviews, les Testimonials, les templates de feeds et d'avis, les templates de popups de notification, et les chat widgets. Après avoir choisi le type, tu sélectionnes le template précis à exporter.

Note bien le format de sortie, parce qu'il change selon le contenu. Les Reviews et les Testimonials sortent en CSV. Les templates de feeds et d'avis, les templates de popups et les chat widgets sortent en JSON.

---

**[SECTION 2 - La limite à connaître sur les avis]**

**[FACE CAMERA]**

Et là, attention, c'est le point que tout le monde découvre à ses dépens.

Quand tu exportes un template de feed ou d'avis, seuls les réglages du template partent. Les avis eux-mêmes ne sont pas exportés, parce qu'ils ne pourront pas s'afficher sur l'autre site.

Pourquoi ? Parce que l'autre site n'a pas l'autorisation nécessaire pour afficher des avis venus de la plateforme. Toutes les plateformes n'exigent pas cette autorisation, mais certaines oui, comme Facebook, Instagram, Tripadvisor ou Yelp. Sur le nouveau site, tu devras donc reconnecter la plateforme pour récupérer les avis.

Le réflexe à retenir : l'export sert à transférer tes designs et tes réglages, pas à dupliquer un mur d'avis tout fait. Garde cette nuance en tête avant de migrer.

---

**[SECTION 3 - Importer sur le nouveau site]**

**[ECRAN - WP Social Ninja → Tools → Import]**

L'import est le miroir de l'export. Tu cliques sur l'option Import dans la barre latérale. Tu choisis le type de données à importer dans le menu déroulant. Tu cliques sur Choose File pour sélectionner le fichier depuis ton ordinateur, puis sur le bouton Import pour l'envoyer.

Même règle de format : les Reviews et Testimonials s'importent en CSV, les templates et chat widgets en JSON. Pour t'aider, WP Social Ninja fournit un fichier CSV de démonstration qui te montre la structure attendue. Si tu prépares un fichier d'avis à la main, c'est ce modèle que tu suis pour ne pas te tromper de colonnes.

---

**[SECTION 4 - Les réglages de performance]**

**[ECRAN - WP Social Ninja → Settings → Advanced Settings]**

Passons à la performance. Tout se joue dans WP Social Ninja, Settings, Advanced Settings. C'est le centre de contrôle de ton plugin.

Premier réglage clé : Optimize Image Format Type. Quand le plugin récupère une image, par exemple une photo Instagram ou un avatar de Google review, il en crée une copie optimisée sur ton propre serveur. Tu choisis ici le format de ces copies.

La recommandation est claire : choisis le format WebP. C'est un format moderne créé par Google, qui offre le meilleur équilibre entre qualité d'image et poids réduit. Des fichiers plus légers, c'est un site qui charge plus vite pour tes visiteurs. C'est un réglage à activer une fois, et qui travaille pour toi ensuite.

---

**[SECTION 5 - RGPD, données et gestion des accès]**

**[ECRAN - Advanced Settings, toggle GDPR et bouton Delete all Platform Data]**

Toujours dans Advanced Settings, deux outils importants.

Le toggle GDPR, ton interrupteur de confidentialité. Quand tu l'actives, le plugin enregistre d'abord les images localement, sur ton serveur, au lieu de les charger directement depuis Facebook, Google ou Instagram. Résultat : le navigateur de ton visiteur n'a plus besoin de contacter ces sites externes pour afficher une image, ce qui évite de partager automatiquement des données comme son adresse IP avec ces plateformes. C'est utile pour respecter le RGPD.

Juste en dessous, le bouton Delete all Platform Data. À manier avec une extrême prudence : c'est un reset total, permanent, impossible à annuler. Il efface tous tes comptes connectés, tous tes feeds et avis en cache, et toutes les images optimisées. À n'utiliser que sur conseil du support ou avant de désinstaller définitivement le plugin.

**[ECRAN - WP Social Ninja → Settings → Manager]**

Dernier sujet : déléguer l'accès. Par défaut, seul l'administrateur voit le plugin. Mais tu peux confier des tâches précises à un collaborateur grâce à l'onglet Manager, dans Settings.

Tu cliques sur New Manager, tu saisis l'email de la personne. Point important : cet email doit déjà correspondre à un compte utilisateur existant sur ton site, par exemple un Éditeur ou un Auteur. Ensuite, tu coches uniquement les permissions que tu veux accorder, par exemple Manage Templates mais pas Manage Settings. Tu confirmes, et la personne pourra créer des templates sans toucher à tes réglages globaux ni à tes connexions.

**[FACE CAMERA]**

Avec ça, tu boucles le module : tu sais transférer tes contenus, garder ton site léger, respecter la confidentialité, et travailler à plusieurs proprement.

---

**[OUTRO - face camera]**

Tu sais maintenant exporter et importer tes contenus, avec la nuance importante sur les avis non transférables, optimiser tes images en WebP, gérer le RGPD, et déléguer l'accès via les Managers. Ce module sur les intégrations et les fonctions avancées est terminé. Dans le Module 7, place au cas pratique : on construit une vraie page Vidéos sur un site schoolsWP, en réutilisant tout ce que tu as appris. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- WP Social Ninja → Tools : options Export et Import, menu déroulant des types de données (sections 1 et 3)
- Slide récap des formats : CSV pour Reviews/Testimonials, JSON pour templates/popups/chat widgets (sections 1 et 3)
- Encadré visuel "Les avis ne s'exportent pas avec le template" + logos Facebook/Instagram/Tripadvisor/Yelp (section 2)
- Import : Choose File + bouton Import + mention du CSV de démo (section 3)
- Advanced Settings : Optimize Image Format Type avec WebP recommandé (section 4)
- Advanced Settings : toggle GDPR et bouton Delete all Platform Data avec avertissement rouge (section 5)
- Settings → Manager : New Manager, champ email, cases de permissions (section 5)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 et 3 : screencast réel dans Tools, montrer le menu déroulant et les formats
- Section 2 : face camera ou slide d'avertissement, c'est le piège conceptuel du module
- Section 4 : screencast Advanced Settings, insister sur WebP comme gain de vitesse
- Section 5 : screencast, ralentir et cadrer en rouge le bouton Delete all Platform Data (action irréversible), puis Manager, puis retour face camera pour la conclusion du module
- Outro : face camera, CTA visuel vers le Module 7 (cas pratique page Vidéos)

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Exporter | 1:00 |
| Section 2 - Limite sur les avis | 1:00 |
| Section 3 - Importer | 1:00 |
| Section 4 - Performance WebP | 1:15 |
| Section 5 - RGPD, data, Managers | 1:55 |
| Outro | 0:15 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__import-export-migration__export-import-custom-reviews.md`
- Doc : `sources/docs/guide__management-settings__advanced-settings.md` (WebP, GDPR, Delete all Platform Data)
- Doc : `sources/docs/guide__management-settings__manager.md` (délégation d'accès et permissions)
