# Module 3 — Lecon 5 : Reglages Advanced
> Duree estimee : 3 min | Type : Adapte du transcript video #08

## Script de narration

[INTRO]

Les reglages avances de Tutor LMS regroupent des options plus techniques : editeur de cours, pages d'inscription, restrictions d'acces, mode maintenance. On passe tout en revue pour que tu saches exactement quoi activer et quoi laisser tranquille.

[CONTENU]

Direction Tutor LMS, Reglages, onglet Advanced.

[CAPTURE ECRAN : Menu Settings > Advanced]

Premiere option : l'editeur Gutenberg pour la creation de cours. En l'activant, tu remplaces l'editeur Tutor par l'editeur de blocs WordPress dans le constructeur de cours back-end. Si tu es a l'aise avec Gutenberg, ca te donne plus de flexibilite pour structurer tes contenus.

[CAPTURE ECRAN : Toggle editeur Gutenberg]

Ensuite, tu peux masquer les produits de cours sur la page boutique WooCommerce. Par defaut, les produits lies a tes formations apparaissent sur ta page Shop au meme titre que tes autres produits WooCommerce. En activant cette option, tu caches uniquement les produits Tutor LMS — tes autres produits restent visibles.

[CAPTURE ECRAN : Toggle "Hide Course Products" et comparaison de la page Shop avec/sans]

Les trois options suivantes concernent les pages liees. Tu peux selectionner quelle page WordPress sert de page d'archive des cours, de page d'inscription instructeur, et de page d'inscription eleve. Choisis les pages correspondantes dans les menus deroulants.

[CAPTURE ECRAN : Trois menus deroulants pour les pages d'archive, inscription instructeur et inscription eleve]

Le permalien de base des lecons te permet de modifier le slug utilise dans les URLs de tes lecons. Par defaut, c'est "lessons". Change-le uniquement si tu as une raison specifique — par exemple pour avoir des URLs en francais.

[CAPTURE ECRAN : Champ permalien de base avec valeur par defaut]

Tu peux renseigner une cle API YouTube. Cette cle, que tu obtiens depuis la Google Developer Console, te permet de connecter des diffusions en direct YouTube a tes cours Tutor LMS. Si tu ne fais pas de live, passe cette option.

[CAPTURE ECRAN : Champ API Key YouTube]

L'option de completion de profil est pratique. En l'activant, tes eleves et instructeurs verront une notification leur demandant de completer leur profil s'ils ne l'ont pas fait. Ca t'aide a avoir des profils remplis sur ta plateforme.

[CAPTURE ECRAN : Toggle Profile Completion et apercu de la notification front-end]

Le modele de connexion Tutor remplace la page de connexion WordPress par defaut par celle de Tutor LMS. Si tu veux eviter que tes utilisateurs voient l'interface d'administration WordPress a la connexion, active cette option.

[CAPTURE ECRAN : Toggle Tutor Login et comparaison page de connexion WP vs Tutor]

Option importante : restreindre l'acces au back-office WordPress pour les instructeurs. En activant ce toggle, les instructeurs ne voient plus la barre d'administration et ne peuvent plus acceder a wp-admin. Fortement recommande si tu travailles avec des instructeurs externes — ils n'ont pas besoin de voir le back-office.

[CAPTURE ECRAN : Toggle restriction acces wp-admin]

L'option de suppression des donnees est sensible. En l'activant, toutes les donnees de Tutor LMS seront effacees si tu desinstalles le plugin. Laisse-la desactivee sauf si tu sais exactement ce que tu fais.

[CAPTURE ECRAN : Toggle "Erase upon uninstallation" avec avertissement visuel]

Et enfin, le mode maintenance. En l'activant, ton site affiche un message personnalise a tes visiteurs pour les informer que le site est temporairement indisponible. Toi, en tant qu'admin, tu gardes l'acces au back-office. Utile quand tu fais des modifications importantes sur ta plateforme.

[CAPTURE ECRAN : Toggle mode maintenance et apercu du message front-end]

[RECAP]

Les reglages avances, c'est le couteau suisse de Tutor LMS : editeur, pages, acces, maintenance. Deux options a retenir absolument : restreindre l'acces wp-admin pour les instructeurs, et laisser desactivee la suppression des donnees. Dans la prochaine lecon, on configure les emails.

## Notes de production
- Captures ecran necessaires : chaque toggle, comparaison page Shop avec/sans produits cours, comparaison page connexion WP vs Tutor, notification de completion de profil, message mode maintenance
- Points d'attention : insister sur la restriction wp-admin (securite) et sur le danger du toggle de suppression des donnees
