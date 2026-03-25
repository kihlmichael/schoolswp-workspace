# Module 1 — Lecon 4 : Reglages des permalinks
> Duree estimee : 2 min | Type : A creer

## Script de narration

[INTRO]
Si tu ne configures pas correctement tes permalinks, tu vas tomber sur des erreurs 404 partout dans Tutor LMS — pages de cours, pages etudiants, tableaux de bord. On regle ca en deux minutes.

[CONTENU]
Par defaut, WordPress utilise des URLs qui ressemblent a ca : monsite.com/?p=123. Ce format ne fonctionne pas avec Tutor LMS. Le plugin a besoin de permalinks en texte clair pour generer ses pages correctement.

Rends-toi dans Reglages, puis Permalinks dans ton tableau de bord WordPress.

[CAPTURE ECRAN : menu Reglages > Permalinks dans WordPress]

Tu vas voir plusieurs options de structure. Selectionne "Nom de l'article" — c'est l'option qui genere des URLs du type monsite.com/mon-premier-cours. C'est aussi la meilleure option pour le SEO.

[CAPTURE ECRAN : page de reglages Permalinks avec l'option "Nom de l'article" selectionnee]

Clique sur Enregistrer les modifications en bas de la page. Meme si l'option etait deja selectionnee, clique quand meme sur Enregistrer — ca force WordPress a regenerer les regles de reecriture d'URL, ce qui peut corriger certains problemes de 404.

[CAPTURE ECRAN : bouton "Enregistrer les modifications" en bas de la page Permalinks]

Maintenant, teste. Ouvre un nouvel onglet et rends-toi sur la page de ton tableau de bord etudiant ou sur une page de cours. Si tout s'affiche normalement, c'est bon.

[CAPTURE ECRAN : page de cours Tutor LMS qui s'affiche correctement]

Si tu tombes encore sur une erreur 404 apres avoir change les permalinks, voici trois choses a verifier :

Premierement, vide le cache de ton navigateur. Les anciennes URLs peuvent rester en memoire.

Deuxiemement, si tu utilises un plugin de cache comme WP Super Cache, W3 Total Cache ou LiteSpeed Cache, vide aussi le cache du plugin.

[CAPTURE ECRAN : option "Purger le cache" dans un plugin de cache]

Troisiemement, verifie que ton fichier .htaccess est accessible en ecriture. Sur certains hebergeurs, les permissions du fichier .htaccess sont verrouillees, ce qui empeche WordPress de mettre a jour les regles de reecriture. Contacte ton hebergeur si c'est le cas.

Un dernier conseil : ne change plus la structure des permalinks une fois que tu as commence a creer des cours et a inscrire des etudiants. Changer les permalinks en cours de route casse tous les liens existants — liens internes, liens partages par tes etudiants, signets...

[RECAP]
Retiens trois choses : selectionne "Nom de l'article" dans Reglages > Permalinks, clique sur Enregistrer meme si c'etait deja le bon choix, et vide tes caches si tu rencontres des 404. C'est un reglage qu'on fait une fois et qu'on ne touche plus.

## Notes de production
- Captures ecran necessaires : menu Reglages > Permalinks, options de structure avec "Nom de l'article" selectionnee, bouton Enregistrer, page de cours fonctionnelle, purge de cache plugin
- Points d'attention : insister sur le "cliquer Enregistrer meme si deja selectionne" (astuce frequente en support WordPress), ne pas oublier le conseil de ne pas changer les permalinks apres lancement
