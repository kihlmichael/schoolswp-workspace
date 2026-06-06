# Scripts vidéo - F2 Module 1 : Fondations express

**Formation** : Créateurs - numérique, abonnements, paywall (SureCart) - méthode PREMIUM (parcours F2)
**Module** : M1 - Fondations express (payant, 1er module de la méthode)
**Leçons** : 4 vidéos + 1 quiz + 1 checklist fondations
**Durée totale** : ~25 min
**Type** : Vidéo HeyGen + voix ElevenLabs
**Date** : 2026-06-05
**Sources** : `_sources/docs-kb/` (installing-surecart, getting-started, add-surecart-api, connect-stripe, connect-paypal, add-checkout-form, how-to-make-test-payments, clear-test-data) + `_sources/youtube-transcripts/` (02-how-to-create-checkout-forms)

> Rôle de ce module : poser le minimum technique pour encaisser, vite. C'est l'express : on installe, on connecte un processeur, on monte une première page de paiement, on valide par un paiement test. La maîtrise complète de la caisse (méthode robuste via wp-config.php, Apple Pay, branding clair et sombre, traduction, cache, factures, taxes) est dans le parcours F1 Vendre sans WooCommerce : on la cite, on ne la refait pas. Ici, l'élève veut monétiser son contenu, pas devenir expert de la caisse.

---

### Leçon 1.1 : Installer SureCart et connecter ton compte

**Durée** : ~6 min (~850 mots)
**Objectif pédagogique** : Installer le plugin, rattacher la boutique à un compte (étape critique), et connecter le plugin à la plateforme avec le jeton API, par la méthode standard.
**Écran** : Screencast installation, assistant, bandeau Complete Setup, screencast Connection.

---

**[INTRO - face caméra]**

On pose les fondations, et on va à l'essentiel. Trois choses dans cette leçon : installer le plugin, rattacher ta boutique à ton compte, et relier le plugin à la plateforme. Si tu veux la version complète, avec toutes les options et la méthode la plus robuste, elle est dans le parcours Vendre sans WooCommerce. Ici, on fait le strict nécessaire pour avancer vite.

**[SECTION 1 - Installer le plugin]**

**[ÉCRAN - screencast : Extensions, Ajouter, recherche SureCart]**

Dans ton tableau de bord WordPress, va dans Extensions, puis Ajouter une extension. Cherche SureCart, clique sur Installer, puis sur Activer. C'est la même manipulation que pour n'importe quelle extension. Une fois activé, un menu SureCart apparaît dans la barre latérale. C'est ton poste de pilotage.

**[SECTION 2 - L'assistant et l'étape à ne pas zapper]**

**[ÉCRAN - screencast de l'assistant + zoom bandeau vert Complete Setup]**

Passe sur le menu SureCart, clique sur Get Started, puis Create New Store. L'assistant te pose quatre questions simples : ta couleur de marque, ta devise, partir de zéro ou avec des produits de démonstration, et un email de notification. Mon conseil pour ce module : choisis les produits de démonstration. Ça te donne tout de suite de quoi t'entraîner, et tu les supprimeras plus tard.

Maintenant, l'étape critique, celle que beaucoup sautent. Après l'assistant, un bandeau vert affiche un bouton Complete Setup. Clique dessus. Tu crées ton compte SureCart ou tu te connectes, et tu valides ton email. C'est cette action qui rattache officiellement ta boutique à ton compte. Pourquoi c'est important : une boutique non rattachée est considérée comme abandonnée, et elle peut être supprimée. Tu ne veux pas construire ton activité sur une base qui peut disparaître. Donc tu le fais maintenant.

**[SECTION 3 - Connecter le plugin avec le jeton API]**

**[ÉCRAN - screencast app.surecart.com, menu API, Secret Token, puis Settings, Connection]**

Ton plugin et la plateforme doivent se parler. Le pont, c'est une clé, le jeton API. Rends-toi sur app point surecart point com, dans le menu API, onglet Secret Token. Ta clé s'affiche, elle commence par s-t-tiret. Copie-la. Un mot de prudence : ce jeton donne accès à ta boutique, traite-le comme un mot de passe, ne le colle jamais dans un message public.

Reviens sur WordPress, va dans SureCart, Settings, onglet Connection, colle ta clé dans le champ API Token et clique sur Save. Le statut passe à Connected. Pour la grande majorité des sites de créateurs, cette méthode suffit. Il existe une méthode plus solide, qui définit le jeton dans le fichier wp-config.php, utile si tu utilises un plugin de sécurité costaud qui déconnecte ta boutique. Je ne la détaille pas ici : elle est expliquée pas à pas dans le parcours F1. Si tu n'es pas concerné, la méthode par l'interface est parfaite.

**[OUTRO - face caméra]**

Plugin installé, boutique rattachée, plateforme connectée. Mais relier SureCart à la plateforme, ce n'est pas encore relier l'argent. Pour encaisser, il te faut un processeur de paiement. C'est la prochaine leçon.

---

**Points clés** :

- Installation classique : Extensions, Ajouter, SureCart, Installer, Activer.
- Étape critique : Complete Setup dans le bandeau vert pour rattacher la boutique à un compte. Une boutique non rattachée peut être supprimée.
- Jeton API : app.surecart.com, menu API, Secret Token (commence par st\_), à coller dans Settings, Connection. Statut Connected.
- La méthode robuste via wp-config.php existe : détaillée dans le parcours F1, non nécessaire pour démarrer.

**Mots clés SEO** : installer SureCart, connecter SureCart, jeton API SureCart, Complete Setup SureCart, configurer SureCart créateur

---

### Leçon 1.2 : Connecter Stripe et PayPal

**Durée** : ~6 min (~800 mots)
**Objectif pédagogique** : Connecter Stripe en mode live et en mode test, ajouter PayPal, et savoir quand s'arrêter là.
**Écran** : Screencast Payment Processors, onglets Stripe et PayPal.

---

**[INTRO - face caméra]**

Pour encaisser, il te faut un processeur de paiement. C'est lui qui prélève réellement l'argent. SureCart s'y connecte, il n'encaisse pas à sa place. On commence par Stripe, le plus répandu, qui gère la carte bancaire et Apple Pay, puis on ajoute PayPal.

**[SECTION 1 - Connecter Stripe en mode live]**

**[ÉCRAN - screencast : SureCart, Settings, Payment Processors, Stripe, Connect, Live Mode]**

Va dans SureCart, Settings, puis Payment Processors. Tu vois la liste des processeurs. Active Stripe : ça t'envoie sur la plateforme SureCart. Ouvre le menu Connect et choisis Live Mode, mode réel. Tu entres ton email Stripe, ton mot de passe, et le code de vérification reçu sur ton téléphone. Une fois connecté, reviens sur ta page WordPress et rafraîchis-la : une pastille verte apparaît, Stripe est connecté. Parfois Stripe met quelques minutes à apparaître sur ton checkout, c'est normal.

**[SECTION 2 - Le mode test de Stripe]**

**[ÉCRAN - screencast : Connect, Test Mode]**

Tu peux aussi connecter Stripe en mode test, pour vérifier tes paiements sans manipuler de vrai argent. Même chemin, mais tu choisis Test Mode dans le menu Connect. En test, tu n'as pas besoin d'informations réelles. On s'en servira dans la dernière leçon du module pour valider ton tunnel.

**[SECTION 3 - Ajouter PayPal]**

**[ÉCRAN - screencast : Payment Processors, PayPal, Connect, Live Mode + slide Not Approved]**

PayPal reste un réflexe d'achat pour une partie de tes clients. La logique est la même : Payment Processors, clique sur PayPal, onglet PayPal, Connect, Live Mode, connexion à ton compte. Après connexion, PayPal apparaît activé.

Un cas à connaître : si tu vois un avertissement Not Approved, non approuvé, ça veut dire que PayPal n'a pas encore validé ton compte pour encaisser. Ce n'est pas un bug de SureCart. Tu contactes le support de PayPal pour finaliser ton approbation. Le mode test existe aussi pour PayPal, même logique.

**[SECTION 4 - Quand s'arrêter là]**

**[ÉCRAN - slide "Ne pas empiler"]**

Deux précisions. Apple Pay passe par Stripe et se configure dans ton tableau de bord Stripe, avec une validation de domaine. Je ne la détaille pas ici, elle est dans le parcours F1, étape par étape. Et selon ton pays, d'autres processeurs existent, comme Mollie ou Razorpay.

Mon conseil de créateur : ne multiplie pas les processeurs pour le plaisir. Pour la plupart des créateurs francophones, Stripe seul, ou Stripe plus PayPal, suffit largement. Tu pourras toujours en ajouter plus tard si un besoin précis apparaît.

**[OUTRO - face caméra]**

Tu peux maintenant encaisser. Il te manque l'endroit où ton client va réellement payer : une page de paiement. On en monte une ensemble dans la prochaine leçon, en cinq minutes.

---

**Points clés** :

- Stripe : Settings, Payment Processors, Stripe, Connect, Live Mode. Pastille verte après rafraîchissement. Mode test disponible (Connect, Test Mode).
- PayPal : même logique. Avertissement Not Approved = compte PayPal pas encore validé, contacter PayPal.
- Apple Pay passe par Stripe (config domaine détaillée dans F1). Autres processeurs régionaux selon le pays.
- Ne pas empiler les processeurs : Stripe seul ou Stripe plus PayPal suffit pour la plupart des créateurs.

**Mots clés SEO** : connecter Stripe SureCart, SureCart PayPal, processeur de paiement SureCart, paiement carte WordPress, encaisser sur WordPress

---

### Leçon 1.3 : Une première page de paiement en 5 minutes

**Durée** : ~7 min (~900 mots)
**Objectif pédagogique** : Créer un formulaire de paiement à partir d'un modèle, y ajouter un produit, le personnaliser à l'essentiel, et récupérer son lien.
**Écran** : Screencast Forms, choix du template, ajout produit, éditeur de blocs, list view, preview.

---

**[INTRO - face caméra]**

Tu as de quoi encaisser, il te faut maintenant l'endroit où le client paie : le formulaire de paiement, ce qu'on appelle le checkout. Je vais te montrer comment en monter un en quelques minutes. Petit prérequis : il te faut au moins un produit. Pour cette démonstration, on utilise un des produits de démonstration installés tout à l'heure. La création de tes vraies offres numériques, c'est le module 2.

**[SECTION 1 - Où vivent tes formulaires]**

**[ÉCRAN - screencast : SureCart, Forms, Add New]**

Tous tes formulaires de paiement se trouvent dans SureCart, Forms. Clique sur Add New, ajouter. La première chose : donne un nom à ton formulaire. Ce nom est pour toi seul, tes clients ne le voient jamais. Il te sert à t'y retrouver quand tu en auras plusieurs.

**[SECTION 2 - Choisir un design de départ]**

**[ÉCRAN - screencast : les modèles de départ]**

SureCart te propose des points de départ. Le modèle par défaut contient un sélecteur de prix. Le modèle Simple ne l'a pas, c'est le plus épuré. Et un modèle en deux sections place le formulaire et un récapitulatif de commande côte à côte. Ce ne sont que des assemblages de composants que tu peux ajouter ou retirer ensuite. Pour démarrer simplement, choisis le modèle Simple, puis clique sur Next.

**[SECTION 3 - Ajouter ton produit]**

**[ÉCRAN - screencast : Add Product, sélection, Create]**

Maintenant, quel produit vendre sur ce formulaire. Clique sur Products, puis choisis ton produit de démonstration. Tu peux en ajouter plusieurs, mais pour ce premier formulaire, restons sur un seul. Clique sur Create. Le formulaire s'ouvre alors dans l'éditeur de blocs WordPress, celui que tu connais déjà.

**[SECTION 4 - Personnaliser l'essentiel]**

**[ÉCRAN - screencast : list view, composants, champ Name, option submit]**

Pour bien voir ce qui compose ton formulaire, clique sur l'icône de vue en liste, en haut à gauche. Tu vois alors tous les composants : le paiement express, l'email, les lignes de produit, le bouton de validation, et un champ de coupon.

Deux réglages utiles tout de suite. Premièrement, ajoute un champ pour le nom : clique sur le plus, choisis le composant Name, et remonte-le en haut du formulaire. Deuxièmement, clique sur le bouton de validation, et active l'option qui affiche le montant à payer directement dans le texte du bouton. C'est un détail qui rassure l'acheteur : il voit exactement ce qu'il va payer en cliquant. Place aussi les lignes de produit en haut, pour un formulaire plus clair. Clique sur Update.

**[SECTION 5 - Le mettre en ligne et récupérer le lien]**

**[ÉCRAN - screencast : preview + copier le shortcode]**

Ton formulaire est maintenant rattaché à une page, que tu peux prévisualiser pour voir le rendu côté client : nom, email, et le bouton de paiement. Si tu veux placer ce même formulaire sur une autre page, copie son shortcode depuis le formulaire, puis ajoute un bloc shortcode sur la page voulue et colle-le.

Tu peux aller beaucoup plus loin : passer en deux colonnes, déplacer les composants par glisser-déposer, ajouter des champs personnalisés ou les conditions générales. Tout ça, en visuel, sans code. Le détail de ces options de page de paiement est couvert dans le parcours F1. Pour démarrer, ce que tu viens de faire suffit largement.

**[OUTRO - face caméra]**

Tu as une page de paiement fonctionnelle. Avant de la partager à qui que ce soit, une règle d'or : on teste. Dans la dernière leçon du module, on passe une vraie commande de test, sans dépenser un centime, et on prépare le passage en live.

---

**Points clés** :

- Les formulaires de paiement vivent dans SureCart, Forms. Add New, puis un nom interne (invisible pour le client).
- Modèles de départ : Default (avec sélecteur de prix), Simple (épuré), deux sections (formulaire plus récapitulatif).
- Ajouter le produit, puis personnaliser dans l'éditeur de blocs : champ Name, montant affiché dans le bouton, lignes de produit en haut.
- Partage via la page du formulaire ou via le shortcode sur n'importe quelle page. Options avancées (deux colonnes, champs custom, CGV) détaillées dans F1.

**Mots clés SEO** : créer page de paiement SureCart, formulaire de paiement SureCart, checkout SureCart, vendre en ligne WordPress, lien de paiement SureCart

---

### Leçon 1.4 : Mode test et passage en live

**Durée** : ~6 min (~800 mots)
**Objectif pédagogique** : Activer le mode test, réussir un paiement test de bout en bout, nettoyer les données de test et passer en live proprement.
**Écran** : Screencast Test Mode, paiement test, Clear Test Data.

---

**[INTRO - face caméra]**

On arrive au moment de vérité : faire passer une vraie commande de test, sans dépenser un centime. C'est l'exercice qui valide tout ce qu'on a fait depuis le début du module. Si ton paiement test passe, tes fondations sont solides. Je te montre comment, puis comment nettoyer derrière toi avant d'ouvrir au public.

**[SECTION 1 - Le processeur de test intégré]**

**[ÉCRAN - slide "Le test processor de SureCart"]**

Bonne nouvelle d'abord : SureCart a son propre processeur de test, actif par défaut. Tu n'as même pas besoin de carte. Au paiement, une option de paiement de test apparaît, sans aucune information bancaire à saisir. C'est l'idéal pour vérifier ton tunnel. À garder en tête : ce processeur ne sert qu'à vérifier, il n'encaisse rien et n'a rien à faire sur une boutique ouverte au public.

**[SECTION 2 - Activer le mode test]**

**[ÉCRAN - screencast : produit, Instant Checkout, Test Mode ; formulaire, Custom Forms, Test]**

Le mode test s'active par produit ou par formulaire. Sur un produit, ouvre le menu Instant Checkout et active Test Mode, puis Save. Un badge Test Mode apparaît : aucun vrai paiement ne peut passer. Tu peux aussi activer le mode test au niveau d'un formulaire de paiement, dans la section Custom Forms, en choisissant Test puis Update.

Il existe aussi une option pour réserver les commandes de test aux administrateurs, afin que des visiteurs ne créent pas de fausses commandes. Elle est dans les réglages avancés, détaillée dans le parcours F1.

**[SECTION 3 - Passer ta commande de test]**

**[ÉCRAN - screencast : checkout, remplir, Purchase, modal Thank you]**

Maintenant, le test. Ouvre ta page de paiement, remplis le nom, et l'adresse si elle est demandée. Avec le processeur de test intégré, pas besoin d'informations bancaires. Si tu testes via Stripe en mode test, tu utilises une carte de test fournie par Stripe. Clique sur Purchase.

Ce que tu dois voir : une fenêtre de confirmation Thank you, un reçu de test qui part vers l'email utilisé, et ta commande qui apparaît dans l'espace client. Si tu vois tout ça, ton tunnel fonctionne de bout en bout. Si ça bloque, reprends trois points dans l'ordre : la connexion à la plateforme, le processeur connecté, et le cache. Le réglage fin du cache, qui est la cause numéro un des bugs de paiement, est traité en détail dans le parcours F1.

**[SECTION 4 - Nettoyer et passer en live]**

**[ÉCRAN - screencast : Settings, Advanced, Clear Test Data]**

Tes tests créent des commandes et des utilisateurs. Avant de passer en live, on nettoie. Va dans SureCart, Settings, onglet Advanced, et descends jusqu'à Clear Test Data. Tu cliques et tu confirmes en tapant le mot CONFIRM. Attention, cette action est irréversible : vérifie bien que tu n'effaces que des données de test, jamais de vraies commandes.

Et n'oublie pas de repasser tes produits et formulaires en mode normal en désactivant le Test Mode, sinon tu ne pourras pas encaisser pour de vrai.

**[OUTRO - face caméra]**

Et voilà : SureCart installé, un processeur connecté, une page de paiement en ligne, et un paiement test réussi. Tes fondations sont posées. Récupère la checklist fondations que je t'ai préparée. Maintenant, on entre dans ton vrai sujet de créateur : vendre des produits numériques. C'est le module 2, on se retrouve là-bas.

---

**Points clés** :

- Processeur de test intégré, actif par défaut, sans carte. À ne pas laisser sur une boutique publique.
- Mode test par produit (Instant Checkout, Test Mode, Save) ou par formulaire (Custom Forms, Test, Update). Badge visible.
- Paiement test réussi = modal Thank you, reçu, commande dans l'espace client. En cas de blocage : connexion, processeur, cache (cache détaillé dans F1).
- Nettoyer via Clear Test Data (taper CONFIRM, irréversible) et désactiver le Test Mode avant de passer en live.

**Mots clés SEO** : mode test SureCart, paiement test SureCart, passer en live SureCart, Clear Test Data, tester sa boutique WordPress

---

## Notes de production (module)

### Captures et écrans à préparer

- Screencast installation plugin (Extensions, Ajouter, SureCart) (1.1)
- Screencast assistant + zoom bandeau vert Complete Setup (1.1)
- Screencast app.surecart.com, API, Secret Token + Settings, Connection (jeton flouté) (1.1)
- Screencast Payment Processors, Stripe, Connect (Live et Test) (1.2)
- Screencast PayPal, Connect + slide Not Approved (1.2)
- Slide "ne pas empiler les processeurs" (1.2)
- Screencast Forms, Add New, choix du modèle (Simple) (1.3)
- Screencast Add Product, Create, éditeur de blocs, list view (1.3)
- Screencast option "montant dans le bouton", preview, copie du shortcode (1.3)
- Screencast Instant Checkout Test Mode + Custom Forms Test (1.4)
- Screencast paiement test (Purchase, modal Thank you) (1.4)
- Screencast Settings, Advanced, Clear Test Data (prompt CONFIRM) (1.4)

### Ton et transitions

- Intro/outro de chaque leçon : face caméra, fond neutre schoolsWP.
- Module express : à chaque fois qu'un sujet est approfondi ailleurs (wp-config, Apple Pay, cache, options de checkout), le dire en une phrase et renvoyer au parcours F1, sans le refaire. C'est le fil conducteur du module.
- Leçon 1.3 : c'est la leçon la plus concrète et la plus valorisante (la première page de paiement). Soigner le rythme du screencast.
- Leçon 1.4 : soigner le moment "modal Thank you" comme une petite victoire.

### Livrables du module

- Checklist fondations (plugin installé, boutique rattachée, jeton API connecté, Stripe connecté, PayPal connecté ou écarté, première page de paiement créée, mode test activé, paiement test réussi, données de test nettoyées, mode test désactivé avant le live).
- Quiz 5 questions (rattacher via Complete Setup, où récupérer le jeton API, connecter Stripe, monter un formulaire de paiement, mode test et Clear Test Data).

### Garde-fous voix schoolsWP

- Tutoiement, singulier solo, jamais d'em-dash ni d'en-dash.
- Aucune promesse absolue. Honnêteté sur les renvois : ce module est volontairement express, la profondeur est dans F1.
- Prudence sécurité : jeton API traité comme un mot de passe, floutté à l'écran.

### Cohérence avec le plan et M0

- M0 annonçait des "fondations express : installer et encaisser l'essentiel" : ce module tient la promesse, sans déborder sur le terrain de F1.
- Le vocabulaire de M0 (checkout, processeur de paiement, espace client) est réutilisé tel quel, sans le redéfinir.
- Le produit de démonstration sert de support à la leçon 1.3 ; la création des vraies offres numériques arrive au module 2.
