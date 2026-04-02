# Lecon 3.2 — Migration : exporter vers n'importe quel hebergeur

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 3 — De la demo au site en production
- **Lecon** : 2/7
- **Duree cible** : 10 min
- **Objectif pedagogique** : Savoir exporter un site ZipWP et l'importer chez un hebergeur tiers (o2switch, Infomaniak, OVH), en evitant les problemes courants de migration.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Tu as decide d'exporter ton site ZipWP vers ton propre hebergeur. Bonne decision si tu veux le controle total. Maintenant, il faut que la migration se passe sans accroc — pas de page blanche, pas d'images manquantes, pas de formulaires casses.

Dans cette lecon, je te montre le processus complet, etape par etape. Du clic sur "Migrate" dans ZipWP jusqu'a la verification finale sur ton hebergeur.

---

[SECTION 1 — Preparer l'export cote ZipWP]

Avant de lancer quoi que ce soit, verifie trois choses sur ton site ZipWP.

Premierement : ton contenu est finalise. Textes relus, images remplacees, formulaire teste. Migrer un site en chantier, c'est migrer des problemes.

Deuxiemement : tes plugins sont a jour. Une migration avec des plugins obsoletes peut creer des conflits sur le nouveau serveur.

Troisiemement : note la version PHP de ton site ZipWP. Tu devras configurer la meme version — ou superieure — chez ton hebergeur.

Une fois tout ca en ordre, va dans ton dashboard ZipWP. Selectionne le site a migrer. Clique sur "Migrate". ZipWP utilise un plugin de migration integre qui va creer un package complet de ton site — base de donnees, fichiers, plugins, theme, medias. Tout est inclus.

Le package se telecharge sous forme d'archive. Garde-le precieusement.

---

[SECTION 2 — Preparer l'hebergeur cible]

Pendant que ton package se telecharge, prepare le terrain cote hebergeur.

Chez o2switch : connecte-toi a ton espace client, va dans cPanel, et installe un WordPress vierge via Softaculous. Note l'URL, le login admin, et le mot de passe. Configure PHP 8.1 ou superieur dans le selecteur PHP.

Chez Infomaniak : meme principe. Console d'administration, installe WordPress, configure PHP.

Chez OVH : attention aux offres Starter qui limitent PHP et la taille des uploads. Verifie que ton offre permet au moins 256 Mo d'upload et PHP 8.1+.

L'etape cle : augmente les limites PHP sur le nouveau serveur. Dans le php.ini ou via cPanel, configure : upload_max_filesize a 512M, post_max_size a 512M, max_execution_time a 300, memory_limit a 256M. Sans ca, l'import peut echouer si ton package est volumineux.

---

[SECTION 3 — Importer le package]

Connecte-toi a l'admin WordPress de ton nouveau site vierge. Installe le plugin de migration — le meme que celui utilise par ZipWP pour creer le package.

Va dans l'outil d'import du plugin. Selectionne ton archive. Lance l'import.

Le processus prend entre 2 et 10 minutes selon la taille du site et la vitesse du serveur. Ne ferme pas l'onglet. Ne rafraichis pas la page. Laisse-le travailler.

Quand c'est termine, le plugin te demande de te reconnecter. Utilise les identifiants de ton site ZipWP — pas ceux du WordPress vierge. L'import a ecrase la base de donnees, donc ce sont les credentials ZipWP qui sont actifs maintenant.

---

[SECTION 4 — Verification post-migration]

C'est l'etape que tout le monde saute — et c'est la que les problemes apparaissent deux semaines plus tard.

Verifie systematiquement :

Les pages — ouvre chaque page et verifie que le contenu s'affiche correctement. Les blocs Spectra doivent etre intacts.

Les images — parcoure le site et verifie qu'aucune image n'est cassee. Si tu vois des images manquantes, verifie la mediatheque WordPress.

Les formulaires — envoie un message test via le formulaire de contact. Verifie que tu recois l'email.

Les liens — clique sur les liens du menu, les boutons, les liens internes. Tout doit pointer au bon endroit.

Le responsive — teste sur mobile. Ouvre les DevTools de ton navigateur, passe en vue mobile, et parcoure les pages principales.

La vitesse — lance un test PageSpeed. Si le score est significativement plus bas que sur ZipWP, c'est un probleme de configuration serveur — cache, compression, version PHP.

---

[SECTION 5 — Problemes courants et solutions]

Probleme numero 1 : le package est trop volumineux pour l'import. Solution : augmente les limites PHP comme explique en section 2. Si ca ne suffit pas, utilise l'import via FTP — upload l'archive directement dans le dossier du plugin sur le serveur.

Probleme numero 2 : timeout serveur pendant l'import. Solution : augmente max_execution_time a 600. Chez certains hebergeurs mutualises, contacte le support pour qu'ils augmentent la limite temporairement.

Probleme numero 3 : les permaliens sont casses apres l'import. Solution : va dans Reglages → Permaliens dans l'admin WordPress, et clique sur "Enregistrer" sans rien changer. Ca regenere le fichier .htaccess.

Probleme numero 4 : les images ne s'affichent pas. Solution : verifie que les URLs dans la base de donnees pointent vers le bon domaine. Un search-and-replace dans la base de donnees peut etre necessaire — le plugin de migration le fait normalement automatiquement.

Conseil final : teste toujours le site apres migration — liens, formulaires, images. Pas dans une semaine. Maintenant.

---

[OUTRO]

Ta migration est terminee. Ton site ZipWP tourne maintenant sur ton propre hebergeur, avec le controle total.

Prochaine etape : connecter ton nom de domaine. DNS, SSL, configuration — on voit tout ca dans la lecon suivante.

---

## Notes de production

### Captures d'ecran suggerees

1. **Dashboard ZipWP** — Bouton "Migrate" dans les options du site
2. **cPanel o2switch** — Installation WordPress via Softaculous
3. **Config PHP** — Ecran de configuration des limites PHP (upload_max_filesize, etc.)
4. **Plugin migration** — Interface d'import avec la barre de progression
5. **Verification** — Checklist visuelle : pages, images, formulaires, liens, mobile, vitesse
6. **Erreur courante** — Message de timeout et la solution

### Transitions

- Intro → Section 1 : zoom sur le dashboard ZipWP
- Section 1 → Section 2 : transition vers logo hebergeur (o2switch)
- Section 2 → Section 3 : animation fleche "export → import"
- Section 3 → Section 4 : split screen site ZipWP / site migre
- Section 4 → Section 5 : fond rouge "problemes courants"
- Section 5 → Outro : retour avatar, ton rassurant

### Notes HeyGen / ElevenLabs

- Ton methodique et patient — migration = stress pour beaucoup de debutants
- Section 3 : insister sur "ne fermez pas l'onglet" — rythme lent, appuye
- Section 4 : rythme checklist, chaque point bien separe
- Section 5 : ton pragmatique, solutions directes
