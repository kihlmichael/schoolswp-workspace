# Leçon 1.5 - Réglages globaux et bibliothèque de templates

## Metadata

- **Formation** : WP Social Ninja Masterclass (premium)
- **Module** : 1 - Fondations et prise en main
- **Durée cible** : 7 min (~980 mots)
- **Type** : Vidéo HeyGen + voix ElevenLabs
- **Objectif pédagogique** : Régler les paramètres globaux qui s'appliquent à tout le plugin (performance, RGPD, gestionnaires) et savoir gérer ta bibliothèque de templates (créer, dupliquer, vider le cache, filtrer).
- **Prérequis** : Leçon 1.4 (interface connue, premier template créé via l'assistant).

---

## Script narration

**[INTRO - face camera]**

Avant de te lancer dans la création de feeds et d'avis, on prend le temps de poser deux fondations souvent négligées : les réglages globaux du plugin, et la gestion de ta bibliothèque de templates.

Les réglages globaux, ce sont des choix qui s'appliquent à tout WP Social Ninja d'un coup : performance, vie privée, accès des collaborateurs. Et la bibliothèque de templates, c'est l'endroit où tout ce que tu crées va vivre. Comprendre ces deux zones maintenant t'évitera des allers-retours plus tard. On commence par les réglages globaux.

---

**[SECTION 1 - Où se trouvent les réglages globaux]**

**[ECRAN - WP Social Ninja → Settings]**

Les réglages globaux vivent dans WP Social Ninja, puis Settings. C'est le centre de contrôle du plugin entier.

Tu y gères la clé de licence, les réglages qui s'appliquent à tout le plugin, la configuration des API de certaines plateformes comme l'API Google, et les réglages de cache, c'est-à-dire la fréquence de synchronisation automatique de tes contenus.

On va se concentrer sur les réglages qui comptent vraiment au démarrage, en commençant par la performance.

---

**[SECTION 2 - Performance et format d'image]**

**[ECRAN - Settings → Advanced Settings → Image Format]**

Premier réglage utile : le format d'image optimisé. Tu le trouves dans Advanced Settings.

Quand le plugin récupère une image, une photo Instagram ou l'avatar d'un avis Google, il peut la convertir et en enregistrer une copie optimisée sur ton propre serveur. La doc recommande le format WebP : c'est un format moderne créé par Google, qui offre le meilleur équilibre entre qualité d'image et poids de fichier réduit.

Concrètement : des images plus légères, donc un site qui se charge plus vite pour tes visiteurs. C'est un réglage à activer une fois, et tu n'y reviens plus.

---

**[SECTION 3 - RGPD et confidentialité]**

**[ECRAN - Settings → Advanced Settings → GDPR toggle]**

Deuxième réglage, important si tu es en Europe : le RGPD. C'est aussi dans Advanced Settings, sous la forme d'un interrupteur.

Quand tu l'actives, le plugin change de comportement pour mieux protéger tes visiteurs. Au lieu de charger les images directement depuis les plateformes externes comme Facebook, Google ou Instagram, il enregistre d'abord des copies de ces images localement, sur ton serveur.

Pourquoi c'est utile : le navigateur de ton visiteur n'a plus besoin de se connecter à ces sites externes juste pour afficher une image. Ça limite le partage automatique de données comme l'adresse IP avec des plateformes tierces. Si la conformité te concerne, active cet interrupteur.

**[FACE CAMERA]**

Toujours dans cette page, tu trouves un bouton de réinitialisation totale, Delete all Platform Data. Une mise en garde claire : cette action est définitive et ne peut pas être annulée. Elle efface tous tes comptes connectés, tous tes feeds et avis en cache, toutes les images optimisées. Tu ne l'utilises que sur instruction du support, ou si tu désinstalles définitivement le plugin. À connaître, mais à ne pas toucher au quotidien.

---

**[SECTION 4 - Donner accès à un collaborateur]**

**[ECRAN - Settings → Manager → New Manager]**

Troisième réglage : les gestionnaires, l'onglet Manager dans Settings.

Par défaut, seul l'administrateur du site voit et utilise WP Social Ninja. Mais tu peux donner des permissions précises à un collaborateur, sans lui ouvrir tout ton site. Par exemple, autoriser un éditeur à créer des templates de feeds, mais pas à modifier les réglages globaux ni à connecter de nouveaux comptes.

Tu cliques sur New Manager, tu entres l'email de la personne. Point important : cet email doit déjà correspondre à un utilisateur existant de ton WordPress. Tu coches ensuite les permissions que tu veux accorder, par exemple Manage Templates uniquement, et tu confirmes. Tu peux modifier ou retirer ces accès à tout moment via le menu trois points.

---

**[SECTION 5 - La bibliothèque de templates]**

**[ECRAN - WP Social Ninja → Templates]**

On passe à la bibliothèque de templates. Tu y accèdes via WP Social Ninja, puis Templates. C'est là que vit tout ce que tu crées, rangé par onglets : Social Feeds, Business Reviews, Chat Widgets, Notification Popup et Testimonials.

Pour créer un nouveau template, tu cliques sur le bouton Create Template en haut à droite, ce qui ouvre l'éditeur avancé. Une fois enregistré, chaque template apparaît dans la liste avec sa colonne Shortcode : tu cliques dessus pour le copier, puis tu le colles sur n'importe quelle page ou article.

**[ECRAN - menu trois points sur un template]**

Chaque template a un menu trois points sur la droite, avec quatre actions. Edit, pour rouvrir l'éditeur. Duplicate, pour faire une copie identique, parfait pour tester une variante sans toucher à l'original. Clear Cache, pour vider les données stockées de ce template précis quand ton feed ne se met pas à jour comme prévu. Et Delete, pour le supprimer définitivement.

Si tu as beaucoup de templates, tu disposes en haut d'un filtre par plateforme, d'une barre de recherche, et d'actions groupées pour en supprimer plusieurs d'un coup.

---

**[OUTRO - face camera]**

Tu sais maintenant régler la performance, la confidentialité et les accès collaborateurs au niveau global, et gérer ta bibliothèque de templates de bout en bout. C'est la dernière brique de fondation avant d'attaquer la connexion des plateformes. Dans la prochaine leçon, on plonge dans la logique des connexions : clés API et tokens d'accès. On se retrouve juste après.

---

## Notes de production

### Captures d'écran suggérées

- Page Settings, vue d'ensemble des onglets globaux (section 1)
- Réglage Image Format avec WebP recommandé (section 2) - asset doc `advance-settings-1`
- Interrupteur GDPR dans Advanced Settings (section 3)
- Mise en garde visuelle sur le bouton Delete all Platform Data (section 3)
- Ajout d'un gestionnaire : New Manager, email, cases de permissions (section 4) - assets doc `managers-1`, `managers-2`
- Liste des templates avec colonne Shortcode (section 5) - asset doc `template`
- Menu trois points d'un template : Edit, Duplicate, Clear Cache, Delete (section 5) - asset doc `manage-existing-template`

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1 à 5 : screencast dans l'interface, slides ponctuelles pour les rappels
- Section 3 : retour face camera sur la mise en garde Delete all Platform Data, ton sérieux
- Section 5 : ralentir sur le clic de copie du shortcode, c'est le geste clé du plugin
- Outro : face camera, CTA visuel vers la leçon 1.6

### Durée estimée par section

| Section | Durée |
| --- | --- |
| Intro | 0:35 |
| Section 1 - Où sont les réglages globaux | 0:45 |
| Section 2 - Performance et format d'image | 1:10 |
| Section 3 - RGPD et confidentialité | 1:25 |
| Section 4 - Accès collaborateur | 1:10 |
| Section 5 - Bibliothèque de templates | 1:35 |
| Outro | 0:20 |
| **Total** | **~7:00** |

### Sources

- Doc : `sources/docs/guide__management-settings__advanced-settings.md`
- Doc : `sources/docs/guide__management-settings__manager.md`
- Doc : `sources/docs/guide__getting-started__templates-overview.md`
- Vidéo officielle : #56 (Configuring Global Settings)
