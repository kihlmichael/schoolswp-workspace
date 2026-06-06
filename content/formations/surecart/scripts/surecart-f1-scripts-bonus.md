# Scripts vidéo - F1 Bonus : cas pratiques et la suite

**Formation** : Vendre sans WooCommerce (SureCart) - méthode CAISSE (parcours F1)
**Module** : Bonus - cas pratiques et la suite (payant, section finale)
**Leçons** : 5 vidéos (B.1 à B.5), durée variable
**Durée totale** : ~28 min
**Type** : Vidéo HeyGen + voix ElevenLabs
**Date** : 2026-06-04
**Sources** : récapitulatif des modules M1 à M8 pour B.1 et B.2 ; `_sources/docs-kb/` (initial-troubleshooting, fix-surecart-store-disconnected, caching) pour B.3 ; architecture des 3 parcours pour B.5. B.4 est un gabarit vivant, à alimenter avec les vraies questions des élèves.

> Rôle de cette section : ancrer la méthode dans deux cas concrets de bout en bout, donner un réflexe de dépannage, ouvrir un espace de questions vivant, et orienter vers la suite. B.1 et B.2 ne présentent aucune nouvelle fonction : ce sont des montages complets qui réutilisent les modules. B.3 ajoute la méthode de débogage. B.4 est volontairement un cadre à compléter après le lancement.

---

### Leçon B.1 : Cas pratique, vendre une prestation de service de A à Z

**Durée** : ~8 min (~1000 mots)
**Objectif pédagogique** : Monter une offre de prestation complète en enchaînant les acquis : produit service, prix, frais de mise en place, checkout, CGV, email, test.
**Écran** : Screencast complet d'un montage de prestation, en renvoyant à chaque module.

---

**[INTRO - face caméra]**

On passe de la théorie au montage complet. Imaginons que tu vends un accompagnement, disons un audit de site à 300 euros. On va le construire de A à Z, en réutilisant tout ce que tu as appris. Pas de nouvelle fonction : juste l'enchaînement, pour que tu voies comment les modules s'emboîtent dans la vraie vie.

**[SECTION 1 - Créer l'offre de service]**

**[ÉCRAN - screencast : produit service, sans expédition]**

On commence comme au module 2. SureCart, Products, Add New. Je nomme le produit Audit de site, je rédige une description concrète : ce qui est inclus, ce que le client reçoit, la durée, le livrable. Comme c'est un service, je ne touche ni au stock ni à l'expédition. J'ajoute un prix en paiement unique, 300 euros.

**[ÉCRAN - screencast : option frais de mise en place ou échéancier]**

Si mon audit demande du travail dès le départ, je peux, comme au module 5, ajouter des frais de mise en place, ou proposer un paiement échelonné pour une prestation plus chère. Pour cet exemple, je reste sur un paiement unique simple.

**[SECTION 2 - La page de paiement]**

**[ÉCRAN - screencast : formulaire ou Instant Checkout]**

Deux options, vues au module 3. Soit je crée un formulaire de paiement dédié, soigné en deux colonnes avec une description et un avis client à gauche. Soit, plus rapide, j'active l'Instant Checkout sur le produit pour avoir un lien direct. Pour une prestation vendue par email ou en visio, l'Instant Checkout est souvent parfait.

**[ÉCRAN - screencast : champ personnalisé + CGV]**

J'en profite pour ajouter un champ personnalisé, comme au module 3 : l'URL du site à auditer, pour avoir l'info dès la commande. Et j'ajoute la case des conditions générales de vente, obligatoire, liée à ma page CGV.

**[SECTION 3 - L'après-commande]**

**[ÉCRAN - screencast : email de confirmation personnalisé]**

Je personnalise l'email de confirmation, comme au module 7, pour qu'il soit chaleureux et qu'il annonce la suite : sous quel délai je reviens vers le client, ce qu'il doit me transmettre. Pour une prestation, ce premier email cadre la relation.

**[ÉCRAN - screencast : facture si besoin]**

Et si mon client est une entreprise qui veut une facture en amont, je peux lui en créer une facture payable, comme au module 4, plutôt qu'un lien de paiement classique.

**[SECTION 4 - Tester et ouvrir]**

**[ÉCRAN - screencast : paiement test puis live]**

Avant de l'envoyer à un vrai client, je teste, comme aux modules 1 et 4 : achat test en navigation privée, vérification de l'email reçu, du champ URL bien enregistré dans la commande. Je nettoie les données de test, je désactive le mode test, et je partage mon lien. Ma prestation est en vente, proprement.

**[ÉCRAN - slide "Le montage complet"]**

Tu vois le principe : un produit service, un prix, un checkout avec une info utile et les CGV, un email qui cadre, un test, et go. Chaque brique vient d'un module. Tu n'as rien appris de neuf ici, tu as juste assemblé.

**[OUTRO - face caméra]**

Voilà une prestation vendue de bout en bout. Passons à un autre grand classique, au fonctionnement très différent : le produit numérique, l'ebook ou le template, qui se livre tout seul. Prochaine leçon.

---

**Points clés** :

- Service = produit en paiement unique, sans stock ni expédition, description concrète (M2).
- Option frais de mise en place ou échéancier pour une prestation lourde ou chère (M5).
- Page de paiement via formulaire soigné ou Instant Checkout (M3), champ personnalisé utile (ex. URL du site) + CGV (M3).
- Email de confirmation qui cadre la relation (M7) ; facture payable si client entreprise (M4).
- Tester, nettoyer, désactiver le mode test, partager (M1, M4). Aucun acquis nouveau : pur assemblage.

**Mots clés SEO** : vendre une prestation SureCart, vendre un service WordPress, cas pratique SureCart, audit en ligne SureCart, freelance SureCart

---

### Leçon B.2 : Cas pratique, vendre un ebook ou un template numérique

**Durée** : ~8 min (~1000 mots)
**Objectif pédagogique** : Monter un produit numérique livré automatiquement, avec un levier de panier et une option lead magnet.
**Écran** : Screencast complet d'un montage de produit numérique.

---

**[INTRO - face caméra]**

Deuxième cas pratique, à l'opposé du service : un produit numérique. Disons un ebook à 19 euros, ou un pack de templates. Sa force, c'est qu'il se crée une fois et se livre tout seul, à l'infini. On le monte de A à Z, toujours en réutilisant tes acquis.

**[SECTION 1 - Le produit et son fichier]**

**[ÉCRAN - screencast : produit numérique, Downloads, Secure Storage]**

SureCart, Products, Add New. Je nomme l'ebook, je soigne la description et j'ajoute une belle image de couverture, comme au module 2. Point clé : dans la section Downloads, j'attache mon fichier en stockage sécurisé, pour qu'il soit protégé. J'ajoute un prix en paiement unique, 19 euros.

**[ÉCRAN - slide "Livraison automatique"]**

Et c'est là toute la beauté du numérique, vue au module 2 : après l'achat, le client reçoit l'accès dans son espace et par email, automatiquement. Je n'envoie rien à la main. Une vente la nuit se livre toute seule.

**[SECTION 2 - La page de paiement et un levier]**

**[ÉCRAN - screencast : Instant Checkout]**

J'active l'Instant Checkout, comme au module 3, pour un lien direct partageable sur mes réseaux et dans mes emails. C'est idéal pour un produit unique à prix accessible.

**[ÉCRAN - screencast : order bump]**

Et comme mon produit est peu cher, j'ajoute un levier de panier du module 6 : un order bump. Par exemple, au moment de payer l'ebook, je propose un pack de templates complémentaire à prix réduit. Le client coche, et mon panier moyen grimpe. Si je suis sur un plan Pro, c'est un réflexe à avoir sur les petits prix.

**[SECTION 3 - La page de remerciement]**

**[ÉCRAN - screencast : thank you page]**

Je crée une page de remerciement personnalisée, comme au module 3, qui rassure et indique comment accéder au fichier. Pour un produit numérique, ce moment compte : le client veut savoir tout de suite où est son achat.

**[SECTION 4 - L'angle lead magnet]**

**[ÉCRAN - screencast : produit gratuit lié]**

Astuce qui boucle avec le module 2 : je peux proposer un extrait gratuit, par exemple le premier chapitre de l'ebook, en produit à zéro euro. Le formulaire devient une capture de lead, je récupère l'email, et ma séquence envoie ensuite vers l'ebook complet. Le gratuit nourrit le payant.

**[ÉCRAN - screencast : test]**

Et bien sûr, je teste avant d'ouvrir : achat test, vérification que le fichier se télécharge bien depuis l'espace client et l'email, nettoyage, désactivation du mode test. Mon ebook est en vente, et il se vendra pendant que je dors.

**[OUTRO - face caméra]**

Deux cas, deux logiques : la prestation que tu livres toi-même, et le numérique qui se livre seul. Avec ces deux montages, tu as un modèle pour à peu près tout ce que tu voudras vendre. Maintenant, parlons de ce qui arrive quand quelque chose coince : le dépannage. Prochaine leçon.

---

**Points clés** :

- Produit numérique : fichier attaché en stockage sécurisé (M2), prix unique. Livraison automatique (espace client + email).
- Instant Checkout pour un lien direct partageable (M3).
- Order bump sur un petit prix pour monter le panier (M6, plan Pro).
- Page de remerciement qui indique l'accès au fichier (M3).
- Angle lead magnet : extrait gratuit en produit à zéro euro pour capter l'email (M2), la séquence pousse vers le payant.
- Tester la livraison du fichier avant d'ouvrir.

**Mots clés SEO** : vendre un ebook SureCart, vendre un template numérique, produit téléchargeable WordPress, livraison automatique SureCart, cas pratique numérique SureCart

---

### Leçon B.3 : Éviter et résoudre les soucis courants

**Durée** : ~6 min (~850 mots)
**Objectif pédagogique** : Donner une méthode de dépannage systématique pour les problèmes courants : cache, conflits de plugins, store déconnecté, paiement.
**Écran** : Slide méthode pas à pas, screencast des points clés (Clear Account Cache, reconnexion, resync webhooks).

---

**[INTRO - face caméra]**

Un jour, quelque chose coincera : un affichage bizarre, un paiement qui plante, une boutique qui se dit déconnectée. Pas de panique. La plupart de ces soucis se règlent en quelques minutes avec une bonne méthode. Je te donne le réflexe de dépannage, dans l'ordre, qui résout la grande majorité des cas.

**[SECTION 1 - La règle d'or]**

**[ÉCRAN - slide "Un changement à la fois"]**

Avant tout, la règle d'or : tu changes une chose à la fois, et tu vérifies si le problème persiste après chaque étape. C'est comme ça qu'on isole la cause. Si tu changes cinq réglages d'un coup, tu ne sauras jamais lequel a réglé, ou cassé, quoi. Fais des modifications minimales.

**[SECTION 2 - Les premiers gestes]**

**[ÉCRAN - slide "Les réflexes de base"]**

On commence par le simple, qui résout déjà beaucoup. Vérifie que SureCart est à jour. Vide les caches, et là il y en a trois : le cache de ton navigateur, le cache de ton site via ton plugin de cache, et le cache du compte SureCart.

**[ÉCRAN - screencast : Settings, Clear Account Cache]**

Ce dernier est dans SureCart, Settings, bouton Clear Account Cache en haut à droite. Beaucoup d'affichages bizarres disparaissent juste avec ça. Essaie aussi un autre navigateur ou un autre appareil, pour écarter un souci local.

**[SECTION 3 - Cache et conflits]**

**[ÉCRAN - slide "Cache et plugins"]**

Si le souci touche tes pages SureCart, reviens sur le cache du module 1 : exclus les pages de paiement, panier, connexion et espace client de ton cache. C'est la cause numéro un des bugs de checkout.

**[ÉCRAN - slide "Désactiver un par un"]**

Si ça persiste, cherche un conflit. Désactive tes autres plugins un par un, en testant à chaque fois. Fais pareil avec ton thème si besoin. Quand le problème disparaît, tu as trouvé le coupable. Vérifie aussi que tes pages essentielles, Boutique, Paiement, Espace client, Panier, n'ont pas été supprimées ou mises à la corbeille par erreur, et restaure-les si besoin.

**[SECTION 4 - Le store déconnecté]**

**[ÉCRAN - slide "Boutique déconnectée"]**

Le cas classique : ta boutique affiche déconnectée. Le plus souvent, c'est un plugin de sécurité qui régénère les clés internes de WordPress, les salts, ce qui invalide ton jeton API stocké en base. La parade définitive, on l'a vue au module 1 : tu inscris ton jeton directement dans le fichier wp-config.php, avec la ligne define, au-dessus de la ligne That's all, stop editing. Là, il survit aux régénérations. En attendant, tu peux simplement recoller ton jeton dans Settings, Connection.

**[SECTION 5 - Les soucis de paiement]**

**[ÉCRAN - slide "Paiement qui coince"]**

Pour un problème de paiement, va sur ton tableau de bord SureCart, Settings, Payments, et rafraîchis ou reconnecte ton processeur. Vérifie que tu as connecté le bon compte et la bonne boutique. Et pour des soucis plus techniques liés aux webhooks, il existe un bouton Resync Webhooks dans Settings, Connection, Advanced Options. Si tu en arrives là sans succès, le support SureCart prend le relais : ces gestes simples règlent déjà environ 80 % des cas.

**[OUTRO - face caméra]**

Tu as maintenant un réflexe de dépannage. Pas besoin de paniquer ni d'écrire au support au premier souci : la méthode résout l'essentiel. La prochaine leçon est un peu spéciale : c'est ton espace de questions, qui va grandir avec le temps.

---

**Points clés** :

- Règle d'or : un changement à la fois, modifications minimales, vérifier après chaque étape.
- Réflexes de base : mettre SureCart à jour, vider les 3 caches (navigateur, site, compte SureCart via Clear Account Cache), tester un autre navigateur.
- Cache : exclure paiement, panier, connexion, espace client (M1). Conflits : désactiver plugins et thème un par un. Vérifier les pages essentielles non supprimées.
- Boutique déconnectée : souvent un plugin de sécurité (salts) ; parade = jeton dans wp-config.php (M1) ; dépannage rapide = recoller le jeton.
- Paiement : rafraîchir/reconnecter le processeur, vérifier le bon compte et la bonne boutique ; Resync Webhooks pour les soucis techniques. Ces gestes règlent environ 80 % des cas.

**Mots clés SEO** : dépannage SureCart, SureCart déconnecté, bug checkout SureCart, problème paiement SureCart, résoudre problème SureCart

---

### Leçon B.4 : Questions et réponses

**Durée** : variable (gabarit évolutif, ~2 min au départ)
**Objectif pédagogique** : Ouvrir un espace de questions vivant, alimenté par les vraies questions des élèves, avec un socle de réponses de départ.
**Écran** : Face caméra + slides de réponses, à enrichir au fil du temps.

---

**[INTRO - face caméra]**

Cette leçon est différente des autres. C'est ton espace de questions et réponses, et il va grandir. À chaque fois que des élèves posent une question récurrente, j'ajoute une réponse ici. Donc reviens-y de temps en temps, il s'enrichit. Pour démarrer, je réponds aux questions qui reviennent le plus souvent.

**[SECTION 1 - Le socle de départ]**

**[ÉCRAN - slide "SureCart est-il gratuit ?"]**

SureCart est-il gratuit ? Oui, il existe un plan gratuit, Launch, avec toutes les fonctions et une commission de 1,9 % par transaction. Dès que tu passes en Pro, payé en abonnement, cette commission disparaît. Les frais Stripe ou PayPal, eux, s'appliquent partout, quel que soit l'outil. On l'a détaillé au module 0.

**[ÉCRAN - slide "Mes données sont-elles bloquées ?"]**

Suis-je enfermé chez SureCart ? Non. Tes données sont exportables, et tu peux migrer d'un site WordPress à un autre en gardant ta connexion, surtout si ton jeton est dans le wp-config.php. Le modèle headless rend même les migrations plus simples.

**[ÉCRAN - slide "Order bumps et plan"]**

Pourquoi je ne vois pas les order bumps ou les upsells ? Ces leviers du module 6 sont sur les plans Pro et Business. Sur le plan gratuit, tu ne les verras pas. C'est normal, ce n'est pas un bug.

**[ÉCRAN - slide "Apple Pay invisible"]**

Apple Pay ne s'affiche pas, pourquoi ? Trois causes habituelles, vues au module 1 : tu n'es pas sur Safari, ton domaine n'est pas validé exactement comme il s'affiche dans Stripe, ou Apple Pay n'est pas disponible dans ton pays.

**[ÉCRAN - slide "TVA et fiscalité"]**

Comment gérer ma TVA ? SureCart te donne les outils, vus au module 4, mais pas le conseil. Pour ta situation précise, ton comptable est la bonne personne. Je ne le dirai jamais assez.

**[SECTION 2 - Comment poser tes questions]**

**[ÉCRAN - slide "Pose ta question"]**

Si ta question n'est pas ici, pose-la dans l'espace prévu de la formation. Les questions les plus fréquentes deviendront de nouvelles réponses dans cette leçon. C'est toi qui fais grandir cette section.

**[OUTRO - face caméra]**

Reviens ici régulièrement, il s'étoffe. Pour la dernière leçon, on regarde la suite : où aller quand tu auras dépassé le cadre de ce parcours.

---

**Points clés** :

- Leçon vivante, à enrichir avec les vraies questions des élèves (gabarit évolutif).
- Socle de départ : plan gratuit + 1,9 % vs Pro sans commission (M0) ; données exportables, pas d'enfermement ; order bumps/upsells réservés aux plans Pro/Business (M6) ; Apple Pay (Safari, domaine exact, pays) (M1) ; TVA = outils oui, conseil = comptable (M4).
- Inviter les élèves à poser leurs questions dans l'espace de la formation.

**Mots clés SEO** : FAQ SureCart, questions SureCart, SureCart gratuit ou payant, problème Apple Pay SureCart, migrer vers SureCart

---

### Leçon B.5 : Et après, les parcours Créateurs et Boutique

**Durée** : ~4 min (~600 mots)
**Objectif pédagogique** : Orienter l'élève vers la suite selon son besoin, en restant honnête sur le fait qu'il n'a peut-être besoin de rien de plus.
**Écran** : Slide des 3 parcours, face caméra.

---

**[INTRO - face caméra]**

Tu as terminé le socle : vendre sans WooCommerce, encaisser proprement, lancer. Pour beaucoup d'entre vous, c'est tout ce qu'il faut, et c'est très bien comme ça. Mais selon ce que tu vends, tu pourrais avoir envie d'aller plus loin. Je te montre les deux directions possibles.

**[SECTION 1 - D'abord, tu n'as peut-être besoin de rien]**

**[ÉCRAN - slide "Le socle suffit souvent"]**

Soyons honnêtes : si tu vends quelques offres, des prestations, des produits numériques, un abonnement, ce parcours couvre ton besoin. N'ajoute pas de complexité pour le plaisir. Une boutique simple qui tourne et qui vend vaut mieux que des fonctions que tu n'utilises pas. Va d'abord vendre avec ce que tu as appris.

**[SECTION 2 - Si tu vends du contenu premium : parcours Créateurs]**

**[ÉCRAN - slide "Parcours Créateurs"]**

Première direction. Si tu veux vendre du contenu premium, monter un espace membre, protéger un accès, vendre des licences logicielles, ou pousser ta rétention d'abonnés avec des outils comme le Subscription Saver, les montées de gamme automatiques ou le dunning, c'est le terrain du parcours Créateurs. C'est la suite logique si ton activité tourne autour du numérique, des abonnements et du contenu protégé.

**[SECTION 3 - Si tu vends du physique : parcours Boutique]**

**[ÉCRAN - slide "Parcours Boutique"]**

Deuxième direction. Si tu vends des produits physiques avec un vrai catalogue, des variations nombreuses, de la gestion de stock, des zones et tarifs d'expédition, du suivi de colis, ou des règles de taxes avancées, c'est le terrain du parcours Boutique. C'est là qu'on traite la logistique que ce parcours a volontairement laissée de côté.

**[SECTION 4 - Choisir selon ton activité]**

**[ÉCRAN - slide "3 parcours, un socle commun"]**

Retiens la logique d'ensemble. Ce parcours, vendre sans WooCommerce, est le socle commun : encaisser proprement. Le parcours Créateurs ajoute le numérique avancé et la rétention. Le parcours Boutique ajoute le physique et la logistique. Tu choisis selon ce que tu vends, pas par envie de tout collectionner.

**[OUTRO - face caméra]**

Et voilà, tu es au bout de ce parcours. Tu sais vendre sur WordPress sans WooCommerce, avec une caisse légère, propre et maîtrisée. Tu as une boutique, des offres, de quoi encaisser, fidéliser et lancer. La suite t'appartient. Le plus important, ce n'est pas la prochaine formation, c'est ta prochaine vente. Alors vas-y. Merci d'avoir suivi cette méthode, et à bientôt.

---

**Points clés** :

- Le socle F1 suffit pour beaucoup : ne pas ajouter de complexité inutile, aller vendre d'abord.
- Parcours Créateurs : contenu premium, espace membre, accès protégé, licences, rétention avancée (Subscription Saver, montées de gamme, dunning).
- Parcours Boutique : catalogue et variations avancées, stock, expédition, suivi de colis, taxes avancées.
- Logique : F1 socle (encaisser), Créateurs (numérique avancé), Boutique (physique). Choisir selon l'activité.

**Mots clés SEO** : parcours SureCart, formation SureCart créateurs, formation SureCart boutique, aller plus loin SureCart, vendre numérique physique WordPress

---

## Notes de production (section)

### Captures et écrans à préparer

- Screencast montage complet d'une prestation (produit service, prix, Instant Checkout, champ URL, CGV, email) (B.1)
- Screencast montage complet d'un produit numérique (Downloads secure storage, Instant Checkout, order bump, thank you page, extrait gratuit) (B.2)
- Slides méthode de dépannage + screencast Clear Account Cache, reconnexion processeur, Resync Webhooks (B.3)
- Slides de réponses Q&A (à enrichir dans le temps) (B.4)
- Slide des 3 parcours + slide "le socle suffit souvent" (B.5)

### Ton et transitions

- Intro/outro face caméra, fond neutre schoolsWP.
- B.1 et B.2 : montrer l'assemblage, renvoyer explicitement aux modules ("comme au module X"). Pas de nouveauté.
- B.3 : ton rassurant, méthode dans l'ordre, insister sur "un changement à la fois".
- B.4 : assumer le format vivant ; tourner les réponses de socle de façon intemporelle pour qu'elles vieillissent bien.
- B.5 : honnêteté avant tout ("tu n'as peut-être besoin de rien"), clôture chaleureuse du parcours.

### Livrables et statut

- Pas de nouveau livrable obligatoire ; B.1 et B.2 peuvent fournir deux fiches "montage type" (service / numérique).
- B.4 : prévoir un mécanisme de mise à jour (ajouter une réponse à chaque question récurrente d'élève).
- Quiz : optionnel sur le Bonus ; le quiz final de validation est en M8.

### Garde-fous voix schoolsWP

- Tutoiement, singulier solo, jamais d'em-dash ni d'en-dash.
- WooCommerce et la complexité traités sans dénigrement : on cadre les cas, on ne dévalorise pas.
- Disclaimer fiscal maintenu (B.4).
- Aucune promesse de résultat ; "ta prochaine vente" plutôt que "tu vas gagner X".
- B.5 : ne pas pousser à l'achat des autres parcours par réflexe ; orienter selon le besoin réel.

### Cohérence avec le plan et les modules précédents

- B.1 et B.2 sont des synthèses pures de M1 à M8 (produit, prix, checkout, CGV, email, test, order bump, lead magnet).
- B.3 ajoute la méthode de dépannage et renvoie au cache du M1 et au jeton wp-config.php du M1.
- B.5 reprend l'architecture des 3 parcours et le hors-périmètre F1 (numérique avancé vers Créateurs, physique vers Boutique).
- Clôt définitivement le parcours F1 ; ouvre proprement vers F2 et F3 sans forcer.
