# Scripts vidéo - F1 Module 0 : Comprendre, vendre sans WooCommerce

**Formation** : Vendre sans WooCommerce (SureCart) - méthode CAISSE (parcours F1)
**Module** : M0 - Comprendre (Gratuit, lead magnet)
**Leçons** : 5 vidéos + 1 quiz + 1 fiche PDF
**Durée totale** : ~20 min
**Type** : Vidéo HeyGen + voix ElevenLabs
**Date** : 2026-06-04
**Sources** : `_sources/docs-kb/` (understanding-ecommerce-fees, stripe-application-fee, getting-started, surecart-product-types, surecart-glossary) + positionnement schoolsWP

> Rôle de ce module : c'est le lead magnet gratuit. Il doit être utile en lui-même (on donne de la vraie valeur, pas un teaser) et donner envie de suivre la méthode complète. Ton honnête, zéro survente.

---

### Leçon 0.1 : Le vrai coût de WooCommerce

**Durée** : ~4 min (~600 mots)
**Objectif pédagogique** : Comprendre que le coût de WooCommerce n'est pas son prix (il est gratuit) mais sa charge cachée, et poser la question : ai-je vraiment besoin de tout ça pour vendre mes offres ?
**Écran** : Face caméra intro/outro, slides pour la pile d'extensions.

---

**[INTRO - face caméra]**

Tu as un site WordPress, tu veux vendre quelque chose dessus, et tout le monde te répond la même chose : installe WooCommerce. C'est le standard, c'est gratuit, c'est ce que tout le monde utilise. Et c'est vrai. Mais avant de te lancer, je veux te poser une question honnête : est-ce que tu as vraiment besoin de WooCommerce pour ce que tu veux vendre ?

Dans cette première leçon, on regarde le vrai coût de WooCommerce. Pas son prix, parce qu'il est gratuit. Son coût caché.

**[SECTION 1 - Gratuit ne veut pas dire sans coût]**

**[ÉCRAN - slide "WooCommerce : la pile d'extensions"]**

WooCommerce tout seul, c'est un moteur de boutique de base. Le souci, c'est qu'on reste rarement sur WooCommerce tout seul.

Tu veux des abonnements ? C'est une extension payante. Tu veux un tunnel de paiement optimisé ? Une autre extension. La relance de panier abandonné ? Encore une. La gestion fine de la TVA, les upsells, les codes promo avancés ? Tu empiles.

Au bout de quelques semaines, tu te retrouves avec WooCommerce plus six, huit, parfois dix extensions. Chacune a son abonnement, ses mises à jour, ses réglages, et son risque de conflit avec les autres. Le jour où l'une se met à jour et casse une autre, c'est toi qui passes la soirée à débugger.

**[SECTION 2 - Le poids et la performance]**

**[ÉCRAN - slide "Le poids sur ton site"]**

Deuxième coût : le poids. WooCommerce charge ses ressources sur l'ensemble de ton site, pas seulement sur tes pages de vente. Même tes articles de blog traînent le poids de la boutique. Sur un petit hébergement, ça se sent sur la vitesse, et la vitesse, c'est du SEO et des ventes.

Plus tu empiles d'extensions, plus tu alourdis la base de données et le temps de chargement. Pour une grosse boutique avec des milliers de références, ce poids est justifié. Pour vendre trois prestations, un ebook et un abonnement, c'est souvent surdimensionné.

**[SECTION 3 - La charge mentale de la maintenance]**

**[ÉCRAN - slide "Le coût en temps"]**

Troisième coût, le plus sous-estimé : ton temps. Chaque extension, c'est une mise à jour à surveiller, une compatibilité à vérifier, un réglage à comprendre. Tu n'es pas développeur, tu es créateur, freelance ou formateur. Chaque heure passée à maintenir ta boutique est une heure que tu ne passes pas à créer ou à vendre.

**[OUTRO - face caméra]**

Soyons clairs : WooCommerce est un excellent outil, et pour certains projets c'est le bon choix. On verra exactement lesquels dans la leçon 4. Mais pour beaucoup de créateurs qui veulent juste encaisser proprement quelques offres, il existe une voie plus légère. C'est SureCart, et c'est ce qu'on découvre dans la prochaine leçon.

---

**Points clés** :

- Le coût de WooCommerce n'est pas son prix, c'est sa charge cachée (extensions, poids, maintenance).
- On reste rarement sur WooCommerce seul : on empile des extensions payantes.
- WooCommerce reste pertinent pour les gros catalogues (vu en leçon 0.4).

**Mots clés SEO** : alternative WooCommerce, WooCommerce trop lourd, vendre sur WordPress sans WooCommerce, coût WooCommerce

---

### Leçon 0.2 : SureCart en 5 minutes, plateforme et plugin

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Comprendre l'architecture de SureCart (un plugin WordPress relié à une plateforme managée) et pourquoi ce modèle garde ton site léger.
**Écran** : Schéma plugin/plateforme, screencast rapide du menu SureCart.

---

**[INTRO - face caméra]**

Avant d'installer quoi que ce soit, tu dois comprendre comment SureCart est construit. Parce que c'est exactement cette architecture qui explique pourquoi il reste léger là où d'autres alourdissent ton site. Cinq minutes, et tu auras le modèle en tête.

**[SECTION 1 - SureCart, c'est deux choses]**

**[ÉCRAN - schéma : à gauche "Plugin WordPress", à droite "Plateforme SureCart", une flèche entre les deux]**

SureCart, ce n'est pas juste un plugin. C'est deux morceaux qui travaillent ensemble.

D'un côté, le plugin WordPress. C'est ce que tu installes sur ton site. Il gère tout ce que tes visiteurs voient et touchent : tes fiches produit, ton formulaire de paiement, ton panier, l'espace client. Tout ça en blocs natifs WordPress, dans l'éditeur que tu connais déjà.

De l'autre côté, la plateforme SureCart. C'est l'infrastructure qui tourne en dehors de ton site. Elle héberge les données de ta boutique : tes produits, tes commandes, tes clients. Elle gère la logique : les prix, le stock, le traitement des commandes.

**[SECTION 2 - Pourquoi ce découpage change tout]**

**[ÉCRAN - slide "Le travail lourd part ailleurs"]**

Voilà l'intérêt. Le travail lourd, le stockage et le traitement, ne pèse pas sur ton site WordPress. Il est déporté sur la plateforme.

Concrètement, ta base de données WordPress ne gonfle pas à chaque commande comme elle le ferait autrement. Ton site reste rapide, même quand ta boutique tourne. Tu profites d'une boutique complète sans transformer ton WordPress en usine.

Les deux morceaux se parlent grâce à une clé, ce qu'on appelle un jeton API. Tu la mets en place une fois au moment de la connexion, et tu n'y touches plus. On le fera ensemble dans le module 1.

**[SECTION 3 - Le vocabulaire que tu vas croiser]**

**[ÉCRAN - slide glossaire animé, un terme à la fois]**

Pour ne pas être perdu, voici cinq mots que tu vas croiser tout le temps.

Le formulaire de paiement, ou checkout : la page où ton client entre ses informations et paie. C'est le cœur de ta vente.

L'instant checkout : une page dédiée à un seul produit, où le client va droit au paiement sans parcourir toute la boutique.

Le panier flottant : le petit panier qui apparaît sur le côté quand on ajoute un article.

L'espace client, ou customer portal : l'endroit où ton client retrouve ses commandes, ses abonnements, ses factures, et met à jour ses informations tout seul.

Le processeur de paiement : le service qui encaisse réellement l'argent. Stripe et PayPal sont les plus courants. SureCart n'encaisse pas à leur place, il s'y connecte.

**[SECTION 4 - Tour rapide du menu]**

**[ÉCRAN - screencast du menu SureCart dans WordPress]**

Une fois le plugin installé, un menu SureCart apparaît dans la barre latérale de WordPress. Tu y retrouves tes produits, tes commandes, tes clients, tes coupons, tes formulaires, et tes réglages. Tout est au même endroit, dans WordPress. Pas besoin de jongler entre dix interfaces.

**[OUTRO - face caméra]**

Retiens ça : SureCart, c'est un plugin léger sur ton site, relié à une plateforme qui fait le gros du travail ailleurs. C'est ce modèle qui te donne une vraie boutique sans alourdir ton WordPress. Maintenant, parlons d'argent, parce que c'est la première question que tout le monde se pose : combien ça coûte vraiment ? Prochaine leçon.

---

**Points clés** :

- SureCart = un plugin WordPress (vitrine, checkout, panier, espace client) + une plateforme managée (données, logique, traitement).
- Le travail lourd est déporté sur la plateforme : ton site reste léger.
- La connexion se fait via un jeton API, configuré une fois.
- Vocabulaire de base : checkout, instant checkout, panier flottant, espace client, processeur de paiement.

**Mots clés SEO** : qu'est-ce que SureCart, SureCart c'est quoi, SureCart plateforme plugin, SureCart WordPress fonctionnement

---

### Leçon 0.3 : Les frais réels, ce que tu paies vraiment

**Durée** : ~4 min (~700 mots)
**Objectif pédagogique** : Distinguer clairement les trois types de frais (processeur, plan SureCart, frais d'abonnement Stripe relabellisé) pour décider en connaissance de cause, sans fausse promesse.
**Écran** : Slides avec tableaux de frais, exemple chiffré.

---

**[INTRO - face caméra]**

C'est la question qui revient toujours : combien SureCart va me prendre sur mes ventes ? Je vais être direct et honnête avec toi, parce que sur ce sujet il y a beaucoup de confusion. Il y a trois choses différentes que les gens mélangent. On les sépare une par une.

**[SECTION 1 - Les frais du processeur de paiement]**

**[ÉCRAN - slide "Frais processeur : Stripe et PayPal"]**

Premier type de frais : ceux du processeur de paiement. C'est Stripe ou PayPal qui les prélève, pas SureCart.

Stripe, c'est en gros 2,9 % plus 30 centimes par transaction réussie. PayPal, c'est environ 3,49 % plus un montant fixe. Ces frais sont standards dans tout l'e-commerce. Tu les paierais avec n'importe quel outil, WooCommerce inclus. Sur ces frais-là, SureCart ne prend rien.

**[SECTION 2 - Le plan SureCart]**

**[ÉCRAN - slide "Plan Launch gratuit vs Pro"]**

Deuxième type de frais : le plan SureCart lui-même.

SureCart a un plan gratuit, appelé Launch. Tu as accès à toutes les fonctionnalités et au support. En échange, ce plan ajoute une commission de 1,9 % par transaction. C'est honnête de le dire : sur le plan gratuit, il y a bien une commission SureCart.

Pour comparer, d'autres outils WordPress prélèvent plus : autour de 2 à 3 % selon les solutions, souvent sans te donner accès à toutes leurs fonctions. SureCart, lui, te donne tout dès le gratuit.

Et surtout : dès que tu passes sur un plan Pro, payé en abonnement, cette commission de 1,9 % disparaît. Plus de pourcentage prélevé par SureCart, tu payes un montant fixe et c'est tout.

**[ÉCRAN - slide "Le calcul simple"]**

Le calcul est simple. Tant que tu testes et que tu vends peu, le plan gratuit avec ses 1,9 % te coûte presque rien. Le jour où tu vends assez pour que 1,9 % de ton chiffre dépasse le prix de l'abonnement Pro, tu passes Pro et tu économises. On posera ce calcul précisément dans la formation.

**[SECTION 3 - La fameuse "SureCart Application Fee"]**

**[ÉCRAN - slide "Application Fee : ce n'est pas un frais en plus"]**

Troisième point, et c'est celui qui inquiète à tort. Si tu vends des abonnements avec Stripe, tu verras parfois une ligne nommée "SureCart Application Fee" sur tes transactions.

Ce n'est pas un frais supplémentaire. Quand tu vends de l'abonnement avec Stripe, il y a toujours un petit frais lié à la gestion du récurrent. Avec la plupart des outils, ce frais part chez Stripe. Avec SureCart, ce même frais apparaît sous le nom SureCart, parce que c'est SureCart qui gère ton système d'abonnements. Le montant total que tu paies est le même. Seule l'étiquette change.

**[OUTRO - face caméra]**

Donc, pour résumer honnêtement : les frais Stripe ou PayPal, tu les paies partout. La commission SureCart de 1,9 % existe sur le plan gratuit et disparaît en Pro. Et l'Application Fee n'est pas un coût en plus. Pas de promesse magique de ma part : juste les chiffres. Dans la leçon suivante, on voit si SureCart est le bon choix pour toi, et dans quels cas WooCommerce reste plus pertinent.

---

**Points clés** :

- Frais processeur (Stripe ~2,9 % + 30¢, PayPal ~3,49 % + fixe) : prélevés par le processeur, pas par SureCart. Payés avec tout outil.
- Plan gratuit Launch : toutes les fonctions + 1,9 % de commission. Plan Pro : commission supprimée, abonnement fixe.
- "SureCart Application Fee" sur les abonnements Stripe : pas un frais en plus, juste le frais d'abonnement Stripe relabellisé.

**Mots clés SEO** : frais SureCart, commission SureCart, SureCart prix, SureCart application fee, SureCart gratuit ou payant

---

### Leçon 0.4 : Pour qui SureCart, et quand WooCommerce reste pertinent

**Durée** : ~4 min (~650 mots)
**Objectif pédagogique** : Situer SureCart par ses cas d'usage (types de produits) et donner un cadre de décision honnête vis-à-vis de WooCommerce.
**Écran** : Slides types de produits, slide de décision.

---

**[INTRO - face caméra]**

SureCart n'est pas fait pour tout le monde, et c'est très bien comme ça. Dans cette leçon, je te donne un cadre de décision clair : pour qui SureCart est le bon outil, et dans quels cas WooCommerce reste le meilleur choix. Pas de parti pris, juste de quoi trancher.

**[SECTION 1 - Tout ce que SureCart sait vendre]**

**[ÉCRAN - slide "6 types de produits", apparition une par une]**

D'abord, SureCart est plus polyvalent qu'on ne le croit. Il gère six types de produits.

Les produits numériques, parfaits pour les cours en ligne et les accès. Les téléchargements, pour les ebooks, PDF, fichiers audio ou vidéo. Les produits physiques, avec stock et variations. Les abonnements, pour les revenus récurrents. Les produits sous licence, pour vendre un logiciel, un thème ou un plugin. Et les produits d'affiliation, liés à la plateforme d'affiliation.

Autrement dit, que tu vendes une prestation, un ebook, un abonnement ou un objet, SureCart sait le faire.

**[SECTION 2 - Pour qui SureCart est le bon choix]**

**[ÉCRAN - slide "SureCart est fait pour toi si..."]**

SureCart est le bon outil si tu te reconnais ici.

Tu vends un nombre raisonnable d'offres : des prestations, des produits numériques, des abonnements, quelques produits physiques. Tu veux que ton site reste léger et rapide. Tu veux un paiement moderne, des abonnements et des leviers de panier intégrés, sans empiler cinq extensions. Et tu préfères passer ton temps à créer et vendre plutôt qu'à maintenir une usine.

Si c'est toi, tu es exactement la cible de cette formation.

**[SECTION 3 - Quand WooCommerce reste plus pertinent]**

**[ÉCRAN - slide "Reste sur WooCommerce si..."]**

Et soyons justes, WooCommerce reste le meilleur choix dans plusieurs cas.

Tu as un très gros catalogue, des milliers de références à gérer. Tu as besoin d'une fonction de niche très spécifique qui n'existe que dans l'écosystème d'extensions WooCommerce. Tu fais du multi-vendeur, une vraie place de marché. Ou tu as déjà une boutique WooCommerce solide qui tourne bien : dans ce cas, ne change pas pour changer.

WooCommerce est puissant et mature. Le but ici n'est pas de le remplacer partout, mais de te montrer qu'il existe une voie plus légère quand tu n'as pas besoin de toute cette puissance.

**[SECTION 4 - Les trois parcours]**

**[ÉCRAN - slide "3 parcours SureCart"]**

Un mot sur cette formation. Elle fait partie d'une série de trois parcours. Celui-ci, vendre sans WooCommerce, c'est le socle : encaisser proprement tes offres. Il existe aussi un parcours dédié aux créateurs, pour le numérique, les abonnements et le contenu premium, et un parcours boutique, pour le physique avec stock et expédition. Tu commences par le bon endroit ici.

**[OUTRO - face caméra]**

Tu as maintenant le cadre pour décider. Si SureCart correspond à ce que tu veux vendre, on passe à la dernière leçon de ce module gratuit : un tour du tableau de bord, pour que tu visualises où on va mettre les mains.

---

**Points clés** :

- SureCart gère 6 types de produits : numérique, téléchargement, physique, abonnement, licence, affiliation.
- Bon choix si : peu d'offres, site léger souhaité, paiement moderne et abonnements intégrés sans empiler.
- WooCommerce reste pertinent : très gros catalogue, niche d'extension spécifique, multi-vendeur, boutique existante qui tourne.
- Ce parcours (F1) est le socle ; parcours Créateurs et Boutique en complément.

**Mots clés SEO** : SureCart pour qui, SureCart ou WooCommerce, que vendre avec SureCart, types de produits SureCart

---

### Leçon 0.5 : Tour du tableau de bord et ce que tu vas savoir faire

**Durée** : ~3 min (~500 mots)
**Objectif pédagogique** : Donner une vision concrète de l'interface et de l'assistant de configuration, rappeler la promesse de la formation, et orienter vers la suite (CTA doux).
**Écran** : Screencast de l'assistant de configuration et du dashboard.

---

**[INTRO - face caméra]**

Pour finir ce module gratuit, je te fais un tour rapide de là où tout se passe. Pas d'installation ici, juste de quoi visualiser l'interface pour ne pas être perdu quand on entrera dans le concret.

**[SECTION 1 - L'assistant de configuration]**

**[ÉCRAN - screencast de l'assistant SureCart]**

À la première activation, SureCart lance un assistant de configuration. Il te demande quatre choses simples : ta couleur de marque, ta devise, si tu veux partir de zéro ou avec des produits de démonstration, et une adresse email pour les notifications. Tu cliques, c'est posé en deux minutes.

**[ÉCRAN - zoom sur le bandeau "Complete Setup"]**

Attention à une étape à ne pas zapper. Après l'assistant, tu dois rattacher ta boutique à un compte SureCart, en cliquant sur "Complete Setup" dans le bandeau. C'est ce qui revendique ta boutique. Une boutique non rattachée peut être supprimée. On le fera proprement dans le module 1.

**[SECTION 2 - Le tableau de bord]**

**[ÉCRAN - screencast du menu SureCart]**

Côté tableau de bord, tout vit dans le menu SureCart de WordPress. Tu y trouves tes produits, tes commandes, tes clients, tes coupons, tes formulaires de paiement, et tes réglages, où tu connectes Stripe ou PayPal, tes emails, l'expédition et les taxes. Un seul endroit, dans une interface que tu connais déjà.

**[SECTION 3 - Ce que tu vas savoir faire]**

**[ÉCRAN - slide "À la fin de la formation"]**

Voilà où on va. À la fin de la méthode complète, tu sauras installer et connecter SureCart, créer tes offres, publier une page de paiement qui convertit, encaisser proprement avec factures et taxes, vendre en abonnement, augmenter ton panier avec les order bumps et les paniers abandonnés, et lancer. Une vraie boutique, en live.

**[OUTRO - face caméra]**

Tu viens de terminer le module gratuit. Tu sais maintenant pourquoi SureCart existe, comment il est construit, ce qu'il coûte vraiment, et s'il est fait pour toi. Récupère la fiche "SureCart ou WooCommerce" que je t'ai préparée, elle résume tout ça sur une page.

Si tu veux passer du pourquoi au comment, la méthode complète t'attend dans le module 1 : on installe, on connecte, et on encaisse ta première vente. On se retrouve là-bas.

---

**Points clés** :

- Assistant de configuration : couleur, devise, départ de zéro ou démo, email de notification.
- Étape à ne pas zapper : rattacher la boutique via "Complete Setup" (une boutique non rattachée peut être supprimée).
- Tableau de bord : produits, commandes, clients, coupons, formulaires, réglages, le tout dans WordPress.
- CTA : récupérer la fiche PDF + transition vers le module 1 payant.

**Mots clés SEO** : tableau de bord SureCart, assistant configuration SureCart, démarrer avec SureCart, interface SureCart

---

## Notes de production (module)

### Captures et écrans à préparer

- Slide "pile d'extensions WooCommerce" (0.1)
- Schéma plugin / plateforme avec flèche jeton API (0.2)
- Screencast menu SureCart dans WordPress (0.2 et 0.5)
- Slides frais : tableau Stripe/PayPal, slide Launch vs Pro, slide Application Fee (0.3)
- Slide 6 types de produits, animation une par une (0.4)
- Slide décision "SureCart pour toi si / reste sur WooCommerce si" (0.4)
- Screencast assistant de configuration + zoom bandeau Complete Setup (0.5)

### Ton et transitions

- Intro/outro de chaque leçon : face caméra, fond neutre schoolsWP.
- Sections : alternance screencast / slides Kadence aux couleurs de marque.
- Leçon 0.3 (frais) : ton posé et honnête, pas de survente. C'est la leçon qui crée la confiance.
- Outro 0.5 : seule transition commerciale du module (fiche PDF + module 1). Rester soft.

### Livrables du module

- Fiche PDF 1 page "SureCart ou WooCommerce : comment choisir" (générée via le pipeline PDF schoolsWP).
- Quiz 5 questions (modèle plateforme/plugin, frais, types de produits, cas WooCommerce, étape Complete Setup).

### Garde-fous voix schoolsWP

- Tutoiement, singulier solo, jamais d'em-dash.
- WooCommerce traité avec respect (cadre "pour qui", pas de dénigrement).
- Aucune promesse absolue sur les frais ni sur la fiabilité.

### Correction à reporter dans le plan

- Le plan F1 (leçon 0.3) disait "pas de commission SureCart" : c'est vrai en Pro, mais le plan gratuit Launch ajoute 1,9 %. Script corrigé en conséquence. À aligner dans `formation-outline.md` si tu valides cette formulation.
