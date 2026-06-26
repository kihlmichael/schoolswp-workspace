# Nouveauté FluentCart - v1.5 : les variations avancées passent en version gratuite

- Date de veille : 2026-06-25
- Plugin : FluentCart (WPManageNinja)
- Versions concernées : 1.5.0 (2026-06-23) et 1.5.1 (2026-06-24)
- Version sur laquelle le cours était calé : 1.3.28 (donc 2 versions mineures de retard)
- Sources : vidéo WPTuts (24/06/2026), changelog WordPress.org, docs.fluentcart.com

## En une phrase

Depuis FluentCart 1.5.0, les variations avancées (couleur x taille, avec prix, SKU et stock par combinaison) sont disponibles dans la version **gratuite**. C'est précisément la brique qui manquait pour positionner FluentCart en alternative crédible à WooCommerce, et elle n'est plus derrière le paywall.

## Ce qui est nouveau (changelog officiel)

### 1.5.0 - 23 juin 2026

- Variations avancées avec génération automatique de toutes les combinaisons et attributs réutilisables.
- Attribute Manager : tri par glisser-déposer, synchronisation entre onglets.
- 8 jeux d'attributs intégrés : Couleur, Taille, Matière, Stockage, Mémoire, Poids, Style, Motif.
- Workflow d'enregistrement par étapes avec barre de sauvegarde persistante.
- Liens de paiement accessibles aux invités via "smart codes" (checkout direct, sans compte).
- Améliorations de performance sur la gestion des variations et le responsive mobile.

### 1.5.1 - 24 juin 2026

- UI/UX des variations avancées améliorée.
- Interface de gestion des stocks améliorée.
- Corrections de sécurité suite aux recommandations de l'équipe Plugin de WordPress.

## Le workflow montré dans le tuto (WPTuts, Paul C., 24/06/2026)

1. La liste des produits affiche désormais le type de chaque produit : produit simple, variations simples, variations avancées.
2. Le plus propre est de créer un produit neuf en mode variations avancées. Convertir un produit à variations simples déclenche un avertissement : tu perds les variations simples et tu dois taper "proceed" pour confirmer.
3. Tu choisis un attribut (ex : couleur) parmi les 8 jeux prédéfinis, puis tes valeurs (rouge, bleu, vert). Tu peux ajouter tes propres valeurs.
4. Tu ajoutes un second attribut (ex : taille : small, medium, large, extra large). FluentCart calcule automatiquement toutes les combinaisons (3 couleurs x 4 tailles = 12 variantes).
5. Par variante : prix, prix comparatif (barré), code SKU (saisi ou auto-généré), image (médiathèque ou upload), stock.
6. Menu trois points par variante : dupliquer, ou créer un lien de checkout direct (partage réseaux sociaux, paiement sans compte).
7. Côté client : sélecteur couleur puis taille, prix mis à jour en temps réel, SKU et stock qui suivent la combinaison.

## Point de vigilance (limite connue au 24/06/2026)

Dans le panneau de variante, certains champs ressemblent à des champs éditables mais ne le sont pas encore :

- Les compteurs disponible / en attente / livré sont calculés à partir des commandes (non éditables par design : normal).
- Le titre et le code SKU de la variante ne sont pas encore modifiables à cet endroit. Le présentateur en a parlé à Jewel (développeur WPManageNinja), qui s'est montré réceptif et a indiqué que c'était à l'étude pour une prochaine release.

À revérifier à chaque montée de version : si titre/SKU deviennent éditables, mettre à jour la leçon.

## Impact sur le cours schoolsWP

- Le cours était calé sur 1.3.28 : il faut le repasser sur 1.5.1 (bannière de version + captures à refaire).
- Ajout d'une leçon 01.07 dédiée aux variations avancées dans le module LAUNCH (`scripts-launch.md`).
- Angle marketing renforcé : "alternative gratuite à WooCommerce" devient démontrable, preuve à l'appui (variations gratuites).
- À garder en radar pour une prochaine MAJ du cours : éditabilité titre/SKU des variantes, et le support MCP/IA de FluentCart (annoncé dans la vidéo, sujet d'une future vidéo dédiée, à documenter quand elle sortira).

## Sources

- Vidéo : "Advanced Product Variations in Minutes (FluentCart Free Version)" - WPTuts (Paul C.) - https://www.youtube.com/watch?v=hNzbY6i_MRQ (publiée le 24/06/2026, 9:27)
- Changelog WordPress.org : https://wordpress.org/plugins/fluent-cart/ (v1.5.1, 7000+ installations actives, testé jusqu'à WP 7.0)
- Documentation officielle : https://docs.fluentcart.com/ (changelog : https://docs.fluentcart.com/guide/changelog)
- Documentation développeur / API : https://dev.fluentcart.com/ (REST API : https://dev.fluentcart.com/restapi/)
- GitHub officiel : https://github.com/fluent-cart/fluent-cart (org WPManageNinja : https://github.com/WPManageNinja)
- Communauté : https://community.wpmanageninja.com/portal (espace fluent-cart)
