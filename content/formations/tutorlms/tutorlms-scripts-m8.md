# Scripts vidéo - Module 8 : eCommerce & Monétisation

**Formation** : Maîtriser TutorLMS
**Module** : M8 - eCommerce & Monétisation (Premium)
**Leçons** : 15 vidéos + 1 quiz
**Durée totale** : ~85 min
**Date** : 2026-03-23

---

### Leçon 8.1 : Vue d'ensemble eCommerce natif

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast du panneau Monetization
**Source** : Vidéo #32 + doc native-ecommerce/overview

---

**[INTRO - face caméra]**

Si tu vends des cours en ligne, tu as besoin d'un système de paiement. Avant la version 3, TutorLMS dépendait de WooCommerce pour ça. Depuis la v3, tout est intégré nativement. Plus besoin de plugin externe, plus de configuration complexe. Dans cette leçon, je te montre ce que le eCommerce natif propose et comment l'activer.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Monetization]

Pour activer le eCommerce natif, va dans Tutor LMS, puis Settings, puis Monetization. Dans le menu déroulant "eCommerce Engine", sélectionne "Native". Enregistre. C'est fait.

**[ÉCRAN - screencast panneau Monetization]**

[Vue d'ensemble des sous-menus qui apparaissent]

Une fois activé, de nouvelles sections apparaissent sous Monetization :
- Payment Methods - pour configurer tes passerelles de paiement
- Coupons - pour créer des codes de réduction
- Tax - pour gérer la TVA et les taxes
- Orders - pour suivre les commandes
- Checkout - pour paramétrer la page de paiement

**[ÉCRAN - screencast liste des passerelles]**

[Montre la page Payment Methods avec les passerelles disponibles]

TutorLMS supporte dix passerelles de paiement :
- Stripe et PayPal - les deux principales, celles que je recommande
- Paddle, Razorpay, Mollie, Klarna, Alipay, Paystack, 2Checkout, Authorize.net
- Plus la possibilité d'ajouter un paiement manuel - virement bancaire, chèque, ce que tu veux

Chaque passerelle s'installe en un clic depuis cette page. On les verra en détail dans les prochaines leçons.

**[ÉCRAN - screencast section Pricing d'un cours]**

[Ouvre le Course Builder, section Pricing]

Côté cours, la section Pricing du Course Builder te permet de définir :
- Un prix unique pour un achat ponctuel
- Un abonnement avec facturation récurrente
- Ou les deux - l'élève choisit

Tu peux aussi marquer un cours comme gratuit. On verra les abonnements et memberships dans la leçon 8.4.

**[TRANSITION - face caméra]**

La recommandation schoolsWP : pour un site qui vend en Europe, configure Stripe en passerelle principale et PayPal en complément. C'est la combinaison qui couvre le plus de cas. On commence par Stripe dans la prochaine leçon.

---

**Points clés** :
- eCommerce natif activé dans Settings > Monetization > eCommerce Engine > Native
- 10 passerelles intégrées + paiement manuel
- Sections : Payment Methods, Coupons, Tax, Orders, Checkout
- Cours configurable en gratuit, achat unique, abonnement ou les deux
- Recommandation : Stripe + PayPal pour l'Europe

**Mots clés SEO** : TutorLMS eCommerce natif, vendre cours TutorLMS, monétisation LMS WordPress, TutorLMS v3 paiement

---

### Leçon 8.2 : Configuration Stripe

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Stripe Dashboard + TutorLMS
**Source** : Vidéo #33 + doc payment-gateways/stripe

---

**[INTRO - face caméra]**

Stripe est la passerelle de paiement numéro un pour vendre des cours en ligne en Europe. Cartes bancaires, Apple Pay, Google Pay - tout passe par Stripe. Dans cette leçon, on configure Stripe dans TutorLMS de A à Z, mode test inclus.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods]

Première étape : installer Stripe. Va dans Settings, Monetization, Payment Methods. Clique sur "Add new gateway", sélectionne Stripe dans la liste, puis clique sur Install. Active-le avec le toggle, puis clique sur l'icône de configuration.

**[ÉCRAN - screencast champs de configuration Stripe]**

[Montre les champs : Environment, Publishable Key, Secret Key, Webhook Secret]

Tu as quatre champs à remplir :

1. Environment - choisis "Test" pour commencer. Tu passeras en "Live" quand tout sera validé.
2. Publishable Key - ta clé publique
3. Secret Key - ta clé secrète
4. Webhook Secret - la clé du webhook

On va chercher ces trois clés dans le dashboard Stripe.

**[ÉCRAN - screencast Stripe Dashboard]**

[Navigation vers Developers > API keys]

Connecte-toi à ton compte Stripe. Va dans Developers, puis API keys. Tu y trouves deux clés :
- La Publishable key - elle commence par "pk_test" en mode test ou "pk_live" en production
- La Secret key - elle commence par "sk_test" ou "sk_live"

Copie chacune et colle-la dans le champ correspondant de TutorLMS.

**[ÉCRAN - screencast Stripe Webhooks]**

[Navigation vers Developers > Webhooks > Add destination]

Maintenant le webhook. C'est ce qui permet à Stripe de notifier TutorLMS quand un paiement est effectué, échoué ou annulé.

Dans Stripe, va dans Developers, puis Webhooks, puis "Add an endpoint". Dans le champ URL, colle l'URL webhook que TutorLMS t'affiche dans ses réglages.

Ensuite, sélectionne les trois événements obligatoires :
- payment_intent.payment_failed
- charge.updated
- payment_intent.canceled

Valide. Stripe génère un Webhook Secret - copie-le et colle-le dans le dernier champ de TutorLMS.

**[ÉCRAN - screencast TutorLMS - Save]**

[Montre le bouton Save Changes]

Enregistre les réglages dans TutorLMS. Stripe est maintenant connecté.

**[ÉCRAN - screencast test d'achat]**

[Montre un achat test sur le front-end]

Avant de passer en production, teste un achat. En mode test Stripe, utilise la carte 4242 4242 4242 4242, n'importe quelle date future, n'importe quel CVC. Tu devrais voir la commande apparaître dans TutorLMS et dans Stripe.

**[TRANSITION - face caméra]**

Quand tes tests sont concluants, repasse l'environnement sur "Live", remplace les clés test par les clés de production, et mets à jour le webhook. Stripe est prêt. Prochaine leçon : PayPal.

---

**Points clés** :
- Installation : Settings > Monetization > Payment Methods > Add new gateway > Stripe
- 3 clés à configurer : Publishable Key, Secret Key, Webhook Secret
- Webhook : 3 événements obligatoires (payment_intent.payment_failed, charge.updated, payment_intent.canceled)
- Toujours tester en mode Test avant de passer en Live
- Carte test : 4242 4242 4242 4242
- Clés test : préfixe pk_test / sk_test - clés live : pk_live / sk_live

**Mots clés SEO** : TutorLMS Stripe, configurer Stripe LMS WordPress, paiement Stripe TutorLMS, webhook Stripe TutorLMS

---

### Leçon 8.3 : Configuration PayPal

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast PayPal Developer + TutorLMS
**Source** : Vidéo #34 + doc payment-gateways/paypal

---

**[INTRO - face caméra]**

PayPal reste incontournable. Beaucoup d'élèves préfèrent payer avec leur compte PayPal plutôt que de saisir une carte bancaire. C'est pour ça que je recommande de l'ajouter en complément de Stripe. Voyons comment le configurer dans TutorLMS.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods]

Bonne nouvelle : PayPal est déjà dans la liste des passerelles disponibles - pas besoin de l'installer. Active-le avec le toggle, puis clique sur l'icône de configuration.

**[ÉCRAN - screencast champs PayPal dans TutorLMS]**

[Montre les champs : Environment, Client ID, Client Secret, Merchant Email, Webhook ID]

Tu as cinq champs :
1. Environment - Test (Sandbox) ou Live
2. Client ID
3. Client Secret Key
4. Merchant Email - l'adresse email de ton compte PayPal
5. Webhook ID

On commence en mode Sandbox pour tester.

**[ÉCRAN - screencast PayPal Developer]**

[Navigation vers developer.paypal.com > Apps & Credentials]

Va sur developer.paypal.com. Connecte-toi, puis va dans Apps & Credentials. Assure-toi d'être en mode Sandbox. Clique sur "Create App", donne-lui un nom - par exemple "TutorLMS" - et valide.

Une fois l'app créée, tu vois le Client ID et le Client Secret. Copie-les dans TutorLMS.

**[ÉCRAN - screencast PayPal Webhooks]**

[Navigation vers la section Webhooks de l'app]

Pour le webhook, dans les réglages de ton app PayPal, va dans la section Webhooks et ajoute un nouveau webhook. Colle l'URL webhook de TutorLMS. Sélectionne les deux événements :
- Checkout order approved
- Payment capture completed

Valide. PayPal te donne un Webhook ID - copie-le et colle-le dans TutorLMS.

**[ÉCRAN - screencast TutorLMS - Save]**

N'oublie pas d'ajouter l'adresse email de ton compte PayPal dans le champ Merchant Email. Enregistre.

**[ÉCRAN - screencast test]**

[Montre un achat test via PayPal Sandbox]

Teste un achat en Sandbox. PayPal te fournit des comptes test dans le Developer Dashboard pour simuler un achat sans vrai paiement.

**[TRANSITION - face caméra]**

Quand c'est validé, passe en Live, remets les clés de production et le Webhook ID live. Vérifie que PayPal est bien disponible dans ton pays et ta devise. Tu as maintenant deux passerelles actives : Stripe et PayPal. Pour la plupart des sites, c'est suffisant.

---

**Points clés** :
- PayPal déjà pré-installé dans TutorLMS - juste à activer
- 5 champs : Environment, Client ID, Client Secret, Merchant Email, Webhook ID
- App à créer sur developer.paypal.com > Apps & Credentials
- Webhook : 2 événements (Checkout order approved, Payment capture completed)
- Comptes Sandbox fournis par PayPal pour les tests
- Vérifier la disponibilité dans ton pays/devise

**Mots clés SEO** : TutorLMS PayPal, configurer PayPal LMS WordPress, paiement PayPal TutorLMS, PayPal sandbox TutorLMS

---

### Leçon 8.4 : Abonnements & Memberships

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Subscriptions + Memberships
**Source** : Vidéo #35 + doc subscriptions, memberships

---

**[INTRO - face caméra]**

Vendre un cours à l'unité, c'est bien. Proposer un abonnement mensuel ou une membership qui donne accès à tous tes cours, c'est un revenu récurrent. TutorLMS gère les deux nativement depuis la v3.5. Voyons comment ça marche.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS Pro > Addons]

Première étape : activer l'addon Subscriptions. Va dans Tutor LMS Pro, puis Addons. Cherche "Subscriptions" et active-le. C'est cet addon qui débloque à la fois les abonnements par cours et les memberships globales.

**PARTIE 1 - Abonnements par cours**

**[ÉCRAN - screencast Course Builder > Pricing]**

[Ouvre un cours, section Pricing]

Pour ajouter un abonnement à un cours, ouvre le Course Builder et va dans la section Pricing. Passe le cours en "Paid" si ce n'est pas déjà fait. Tu vois maintenant le bouton "Add Subscription".

**[ÉCRAN - screencast création abonnement]**

[Clique sur Add Subscription, montre les champs]

Clique dessus. Tu configures :
- Le nom du plan - par exemple "Accès mensuel"
- Le prix récurrent
- L'intervalle de facturation - jour, semaine, mois ou année
- Le nombre de cycles - un nombre fixe ou "Until Cancelled" pour un abonnement continu
- Des frais d'inscription optionnels - un montant additionnel à la première facturation
- Un prix barré pour les promotions
- Le statut "Featured" pour mettre en avant un plan

**[ÉCRAN - screencast options d'achat]**

[Montre les options : Subscription only, One-time only, Both]

Tu peux proposer trois modes :
- Abonnement uniquement - l'élève paie tant qu'il veut accéder
- Achat unique - paiement une fois, accès à vie
- Les deux - l'élève choisit

Mon conseil : propose les deux. Ça laisse le choix et ça convient à tous les profils.

**PARTIE 2 - Memberships**

**[ÉCRAN - screencast Settings > Subscriptions]**

[Navigation vers Tutor LMS Pro > Settings > Subscriptions]

Les memberships, c'est un niveau au-dessus. Au lieu de gérer des abonnements cours par cours, tu crées un plan qui donne accès à plusieurs cours ou à tout ton catalogue.

Va dans Tutor LMS Pro, Settings, Subscriptions. Clique sur "New Membership Plan".

**[ÉCRAN - screencast création membership]**

[Montre les champs du formulaire]

Tu retrouves les mêmes champs que pour un abonnement - nom, prix, intervalle, cycles - plus deux options spécifiques :

Première option : le type d'accès. "Full Site Membership" donne accès à tous les cours du site. "Category-wise Membership" restreint l'accès à certaines catégories - par exemple "Tous les cours WordPress" ou "Tous les cours Marketing".

Deuxième option : la période d'essai. Tu peux offrir un essai gratuit ou à prix réduit avant la première facturation. Et avec l'option "Skip Payment for Free Trials", l'élève n'a même pas besoin d'entrer sa carte bancaire pour commencer.

**[ÉCRAN - screencast shortcode]**

[Montre le shortcode tutor_membership_pricing sur une page]

Pour afficher tes plans sur une page, utilise le shortcode `[tutor_membership_pricing]`. Ça génère un tableau de prix propre avec tes différents plans.

**[ÉCRAN - screencast option Membership-only]**

Si tu veux aller plus loin, dans Settings > Subscriptions, active "Membership-only site". Ça désactive l'achat de cours individuels - tout passe par la membership. Utile si tu as un catalogue fourni et que tu veux simplifier ton offre.

**[TRANSITION - face caméra]**

Abonnements par cours pour commencer, membership globale quand ton catalogue grandit. C'est une stratégie progressive. Dans la prochaine leçon, on voit comment booster tes ventes avec les coupons de réduction.

---

**Points clés** :
- Addon Subscriptions à activer dans Tutor LMS Pro > Addons
- Abonnement par cours : configurable dans le Course Builder > Pricing
- Intervalles : jour, semaine, mois, année - cycles fixes ou illimités
- Membership : Full Site ou Category-wise, avec essai gratuit possible
- Shortcode `[tutor_membership_pricing]` pour afficher les plans
- Mode "Membership-only site" pour désactiver les achats individuels
- Requiert TutorLMS v3.5+ et le eCommerce natif

**Mots clés SEO** : TutorLMS abonnement, membership TutorLMS, revenu récurrent LMS WordPress, subscription TutorLMS

---

### Leçon 8.5 : Coupons de réduction

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Coupons
**Source** : doc native-ecommerce/coupons

---

**[INTRO - face caméra]**

Les coupons de réduction, c'est un levier de vente classique. Lancement, Black Friday, parrainage - tu as toujours besoin d'un code promo à un moment ou un autre. TutorLMS intègre un système de coupons complet dans son eCommerce natif. Voyons comment créer et gérer tes codes.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Coupons]

Prérequis : le eCommerce natif doit être activé. Ensuite, va dans Tutor LMS, puis l'onglet Coupons. Clique sur "Create Coupon".

**[ÉCRAN - screencast formulaire de création]**

[Montre les champs du formulaire coupon]

Premier bloc : les informations de base. Tu définis un titre interne - pour toi, pas visible par l'élève - et un code coupon. Tu peux le taper manuellement ou laisser TutorLMS en générer un automatiquement.

**[ÉCRAN - screencast type de réduction]**

[Montre les options Percentage / Fixed]

Deuxième bloc : le type de réduction. Deux choix :
- Pourcentage - par exemple 20% de réduction
- Montant fixe - par exemple 10 euros de réduction

**[ÉCRAN - screencast portée du coupon]**

[Montre les options All Courses, All Bundles, Specific...]

Troisième bloc : la portée. Tu choisis sur quoi le coupon s'applique :
- Tous les cours
- Tous les bundles
- Les deux
- Ou des cours spécifiques, des bundles spécifiques, ou une catégorie spécifique

Ça te permet de créer des promos ciblées - par exemple un coupon valable uniquement sur les cours WordPress.

**[ÉCRAN - screencast limites d'utilisation]**

[Montre les champs de restriction]

Quatrième bloc : les restrictions. Tu définis :
- Le nombre total d'utilisations du coupon - par exemple 100 utilisations maximum
- Le nombre d'utilisations par client - par exemple 1 par personne
- Un montant minimum d'achat
- Un nombre minimum d'articles dans le panier

**[ÉCRAN - screencast dates de validité]**

[Montre les champs Start/End date]

Cinquième bloc : la période de validité. Date et heure de début, date et heure de fin. Si tu ne mets pas de date de fin, le coupon reste actif indéfiniment.

**[ÉCRAN - screencast type Code vs Automatique]**

[Montre l'option coupon automatique]

Et un détail important : le type de coupon. "Code-based" - l'élève doit saisir le code au checkout. "Automatic" - la réduction s'applique automatiquement, sans code. Pratique pour les promos sitewide.

**[ÉCRAN - screencast Settings > Checkout]**

Dernière chose : dans Settings > Checkout, vérifie que l'option "Enable Coupon Code" est activée. Sans ça, le champ de saisie du code n'apparaît pas sur la page de paiement.

**[TRANSITION - face caméra]**

Les coupons sont prêts. Pense à définir des dates de validité et des limites d'utilisation pour éviter les mauvaises surprises. Prochaine leçon : la configuration des taxes.

---

**Points clés** :
- Coupons dans Tutor LMS > Coupons (eCommerce natif requis)
- Deux types : Code-based (saisie manuelle) ou Automatic (appliqué seul)
- Réduction en pourcentage ou en montant fixe
- Portée : tous les cours, bundles, catégories, ou sélection spécifique
- Restrictions : nombre d'utilisations total/par client, montant minimum
- Validité : dates début/fin configurables
- Activer "Enable Coupon Code" dans Settings > Checkout

**Mots clés SEO** : TutorLMS coupons, code promo LMS WordPress, réduction cours TutorLMS, coupon TutorLMS

---

### Leçon 8.6 : Configuration taxes

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Tax settings
**Source** : doc native-ecommerce/tax

---

**[INTRO - face caméra]**

La TVA, c'est pas la partie la plus excitante, mais c'est obligatoire. Si tu vends des cours en ligne depuis la France ou l'Europe, tu dois collecter et déclarer la TVA. TutorLMS te permet de configurer les taxes directement dans son eCommerce natif. Voyons ça.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Taxes]

Va dans Tutor LMS, Settings, Monetization. La section "Taxes" apparaît quand le eCommerce natif est activé.

**[ÉCRAN - screencast ajout région fiscale]**

[Clique sur "Add tax region"]

Clique sur "Add tax region" pour créer ta première zone fiscale. Tu sélectionnes un pays - par exemple France - et tu définis le taux de TVA. Pour la France, c'est 20% sur les formations en ligne.

Tu peux appliquer un taux unique à tout le pays, ou définir des taux différents par région ou province. Utile si tu vends dans des pays avec des taux variables selon les états - comme les USA ou le Canada.

**[ÉCRAN - screencast réglages globaux]**

[Montre les trois options globales]

Ensuite, trois réglages globaux importants :

Premier réglage : "Tax Already Included in Prices". Active-le si tes prix affichent déjà la TVA incluse - ce qui est la norme en France pour le B2C. L'élève voit le prix final, pas de surprise au checkout.

Deuxième réglage : "Tax Calculated at Checkout". La taxe s'affiche uniquement au moment du paiement. Utile pour le B2B ou les marchés où les prix sont affichés HT.

Troisième réglage : "Display Prices Inclusive of Tax". Quand c'est activé, les prix affichés sur le site incluent la taxe partout - page cours, catalogue, checkout.

**[ÉCRAN - screencast réglage par cours]**

[Montre l'option dans le Course Builder]

Bonus : tu peux aussi gérer la taxe cours par cours. Dans le Course Builder, section Pricing, des options apparaissent pour activer ou désactiver la taxe sur les achats ponctuels et sur les abonnements. Ces options n'apparaissent que quand le cours a un prix défini.

**[TRANSITION - face caméra]**

Pour un site français, la configuration typique, c'est : une région France à 20%, prix TTC affichés. Adapte selon ton pays. Si tu utilises Paddle comme passerelle, note que Paddle gère ses propres calculs de taxes - les réglages TutorLMS ne s'appliquent pas. Dans la prochaine leçon, on parle de la gestion des commandes.

---

**Points clés** :
- Taxes dans Settings > Monetization > Taxes (eCommerce natif requis)
- Ajout de régions fiscales par pays, avec taux personnalisable par région
- France : 20% TVA sur les formations en ligne
- 3 modes : taxes incluses dans le prix, calculées au checkout, affichées TTC
- Configuration possible cours par cours dans le Course Builder
- Exception Paddle : gère ses propres taxes

**Mots clés SEO** : TutorLMS TVA, taxes LMS WordPress, configurer TVA formation en ligne, TutorLMS taxe France

---

### Leçon 8.7 : Gestion des commandes

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Orders
**Source** : doc native-ecommerce/orders

---

**[INTRO - face caméra]**

Chaque vente génère une commande. Suivi des paiements, remboursements, problèmes de transaction - tout se passe dans le gestionnaire de commandes de TutorLMS. Voyons comment l'utiliser au quotidien.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Orders]

Va dans Tutor LMS, puis Orders. Tu retrouves la liste de toutes les commandes avec :
- Le numéro de commande
- Le nom de l'élève
- Le cours acheté
- Le montant
- La date
- Le statut

**[ÉCRAN - screencast filtres et statuts]**

[Montre les filtres disponibles]

Les statuts possibles :
- Completed - paiement reçu et validé
- Pending - en attente de confirmation du paiement
- Cancelled - annulée
- Refunded - remboursée

Tu peux filtrer par statut pour retrouver rapidement les commandes qui posent problème. Les commandes en "Pending" sont celles à surveiller - ça signifie que la passerelle de paiement n'a pas confirmé la transaction.

**[ÉCRAN - screencast détail d'une commande]**

[Clique sur une commande pour voir le détail]

En cliquant sur une commande, tu vois le détail complet : informations de l'élève, méthode de paiement utilisée, coupon appliqué le cas échéant, montant HT, taxe, total.

**[ÉCRAN - screencast commande bloquée]**

[Montre une commande en Pending]

Si une commande reste en "Pending", deux causes possibles. Première : la passerelle de paiement n'a pas envoyé la confirmation - vérifie que ton webhook est correctement configuré. Deuxième : le paiement a échoué côté banque - l'élève doit réessayer.

Dans les deux cas, ne valide jamais manuellement une commande sans avoir vérifié le paiement dans le dashboard de ta passerelle - Stripe ou PayPal.

**[ÉCRAN - screencast remboursement]**

[Montre le processus de remboursement]

Pour un remboursement, le processus dépend de ta passerelle. En général, tu lances le remboursement depuis le dashboard Stripe ou PayPal, et le statut se met à jour automatiquement dans TutorLMS via le webhook. L'élève perd l'accès au cours après remboursement.

**[TRANSITION - face caméra]**

Le gestionnaire de commandes est ton tableau de bord financier dans TutorLMS. Consulte-le régulièrement, surtout les premiers jours après un lancement. Dans la prochaine leçon, on optimise l'expérience d'achat avec la configuration du checkout.

---

**Points clés** :
- Commandes dans Tutor LMS > Orders
- 4 statuts : Completed, Pending, Cancelled, Refunded
- Commandes Pending : vérifier le webhook ou le paiement côté passerelle
- Ne jamais valider manuellement sans vérification dans Stripe/PayPal
- Remboursements : lancer depuis la passerelle, statut mis à jour via webhook
- Détail commande : élève, méthode, coupon, montant, taxe

**Mots clés SEO** : TutorLMS commandes, gestion commandes LMS WordPress, remboursement TutorLMS, suivi ventes TutorLMS

---

### Leçon 8.8 : Configuration checkout

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Checkout settings
**Source** : doc native-ecommerce/checkout

---

**[INTRO - face caméra]**

Le checkout, c'est la dernière étape avant le paiement. C'est là où tu perds des ventes si l'expérience est mauvaise. TutorLMS propose trois réglages clés pour optimiser cette page. Voyons-les.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Checkout]

Va dans Settings, Monetization, puis Checkout. Trois options t'attendent.

**[ÉCRAN - screencast option Coupon Code]**

[Montre le toggle Enable Coupon Code]

Première option : "Enable Coupon Code". Active-la si tu utilises des coupons - on les a configurés dans la leçon 8.5. Si tu ne proposes pas de coupons, désactive-la pour ne pas afficher un champ vide qui fait douter l'élève ("est-ce que je rate une promo ?").

**[ÉCRAN - screencast option Buy Now]**

[Montre le toggle Buy Now]

Deuxième option : "Buy Now". Quand c'est activé, le bouton "Add to Cart" sur la page du cours est remplacé par un bouton "Buy Now". L'élève va directement au paiement sans passer par un panier. Moins d'étapes, moins d'abandon. Je recommande de l'activer si tu vends des cours à l'unité.

**[ÉCRAN - screencast option Guest Checkout]**

[Montre le toggle Guest Checkout]

Troisième option : "Guest Checkout". L'élève peut acheter sans créer de compte au préalable. TutorLMS crée le compte automatiquement avec les informations de facturation et envoie un email de réinitialisation de mot de passe. L'élève définit son mot de passe, et il a accès à son cours.

C'est un bon compromis : tu réduis la friction à l'achat sans perdre la création de compte.

Quand le Guest Checkout est actif, un bouton de connexion apparaît aussi sur la page checkout pour les clients existants.

**[TRANSITION - face caméra]**

Ma recommandation : active "Buy Now" et "Guest Checkout" pour maximiser tes conversions. Désactive le champ coupon si tu n'en utilises pas. Simple et efficace. Prochaine leçon : Paddle, une passerelle alternative qui gère la TVA à ta place.

---

**Points clés** :
- Checkout dans Settings > Monetization > Checkout
- 3 options : Enable Coupon Code, Buy Now, Guest Checkout
- Buy Now : supprime le panier, achat direct - réduit l'abandon
- Guest Checkout : achat sans compte, création automatique + email mot de passe
- Désactiver le champ coupon si pas de promos (évite le doute)
- Recommandation : Buy Now + Guest Checkout actifs

**Mots clés SEO** : TutorLMS checkout, page paiement LMS WordPress, optimiser checkout TutorLMS, guest checkout TutorLMS

---

### Leçon 8.9 : Paddle

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Paddle Dashboard + TutorLMS
**Source** : doc payment-gateways/paddle

---

**[INTRO - face caméra]**

Paddle, c'est différent des autres passerelles. Paddle agit comme "Merchant of Record" - ça veut dire que c'est Paddle qui vend ton cours à ta place, gère la TVA, les factures et la conformité fiscale dans chaque pays. Si tu vends à l'international et que tu ne veux pas te prendre la tête avec la TVA par pays, Paddle est une option sérieuse.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods > Add new gateway > Paddle]

Installation classique : Settings, Monetization, Payment Methods, Add new gateway, sélectionne Paddle, Install, active le toggle.

**[ÉCRAN - screencast champs de configuration]**

[Montre les champs : Environment, API Key, Client-side Token, Webhook Secret]

Trois clés à récupérer dans ton dashboard Paddle :

1. API Key - dans Developer Tools > Authentication. Génère une nouvelle clé avec les permissions adéquates.
2. Client-side Token - généré séparément, utilisé pour les transactions front-end.
3. Webhook Secret - configuré dans Developer Tools > Notifications.

**[ÉCRAN - screencast Paddle Webhooks]**

[Navigation vers Developer Tools > Notifications > Create webhook]

Pour le webhook, dans Paddle, va dans Developer Tools, Notifications, et crée un nouveau webhook. L'URL à utiliser :

`https://tondomaine.com/wp-json/tutor/v1/ecommerce-webhook?payment_method=paddle`

Sélectionne trois événements :
- Transaction.completed
- Adjustment.created
- Adjustment.updated

Copie le Secret généré et colle-le dans TutorLMS.

**[ÉCRAN - screencast approbation domaine]**

[Montre Checkout > Website Approval dans Paddle]

Étape supplémentaire avec Paddle : tu dois faire approuver ton domaine. Dans Paddle, va dans Checkout, Website Approval, et soumets ton domaine - juste le domaine, sans https://. Configure aussi ton URL comme lien de paiement par défaut dans les réglages Checkout.

**[TRANSITION - face caméra]**

Point important : quand tu utilises Paddle, les réglages de taxes de TutorLMS ne s'appliquent pas. C'est Paddle qui gère tout le calcul fiscal. Pratique, mais tu perds le contrôle sur l'affichage des prix. À toi de voir si ça correspond à ton modèle.

---

**Points clés** :
- Paddle = Merchant of Record : gère TVA, factures, conformité fiscale
- 3 clés : API Key, Client-side Token, Webhook Secret
- Webhook : 3 événements (Transaction.completed, Adjustment.created, Adjustment.updated)
- Approbation du domaine obligatoire dans Paddle
- Les taxes TutorLMS ne s'appliquent pas avec Paddle
- Les clients TVA peuvent saisir leur numéro de TVA au checkout Paddle

**Mots clés SEO** : TutorLMS Paddle, Paddle LMS WordPress, Merchant of Record LMS, TVA automatique formation en ligne

---

### Leçon 8.10 : Razorpay

**Durée** : 3 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Razorpay Dashboard + TutorLMS
**Source** : doc payment-gateways/razorpay

---

**[INTRO - face caméra]**

Razorpay, c'est la passerelle de référence en Inde. Si ton audience est indienne ou si tu veux accepter UPI, net banking ou les portefeuilles numériques indiens, c'est la passerelle qu'il te faut. Configuration rapide.

**[ÉCRAN - screencast TutorLMS admin]**

[Installation Razorpay : Add new gateway > Razorpay > Install]

Même processus : Settings, Monetization, Payment Methods, Add new gateway, Razorpay, Install, active le toggle.

**[ÉCRAN - screencast champs de configuration]**

[Montre les champs : Environment, Key ID, Key Secret, Webhook Secret]

Trois informations à récupérer dans ton dashboard Razorpay, section Account & Settings, puis API Keys :
- Key ID
- Key Secret

Clique sur "Generate Test Key" pour les clés de test. Tu peux télécharger les deux clés en CSV.

**[ÉCRAN - screencast Razorpay Webhooks]**

[Navigation vers Account & Settings > Webhooks]

Pour le webhook, dans Razorpay, va dans Account & Settings, Webhooks, "Add New Webhook". L'URL :

`https://tondomaine.com/wp-json/tutor/v1/ecommerce-webhook?payment_method=razorpay`

Sélectionne deux événements :
- Payment Failed
- Payment Captured

Définis un Webhook Secret - attention, tu dois saisir le même secret manuellement dans TutorLMS. Ce n'est pas généré automatiquement comme avec Stripe.

Enregistre des deux côtés et c'est opérationnel.

**[TRANSITION - face caméra]**

Razorpay est spécifique au marché indien. Si tu ne vises pas cette audience, passe à la leçon suivante. Sinon, c'est une passerelle fiable avec un bon support des méthodes de paiement locales.

---

**Points clés** :
- Razorpay : référence en Inde (UPI, net banking, wallets)
- 3 clés : Key ID, Key Secret, Webhook Secret
- Webhook : 2 événements (Payment Failed, Payment Captured)
- Webhook Secret à définir manuellement (identique des deux côtés)
- Vérifier la disponibilité dans ton pays/devise avant configuration

**Mots clés SEO** : TutorLMS Razorpay, paiement Inde LMS WordPress, Razorpay formation en ligne

---

### Leçon 8.11 : Mollie / Klarna / Alipay

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS pour chaque passerelle
**Source** : doc payment-gateways/mollie, klarna, alipay

---

**[INTRO - face caméra]**

Trois passerelles dans une seule leçon : Mollie, Klarna et Alipay. Chacune couvre un marché spécifique. Mollie pour les Pays-Bas et l'Europe du Nord, Klarna pour le paiement fractionné en Scandinavie et en Allemagne, Alipay pour la Chine. Voyons la configuration de chacune.

**PARTIE 1 - Mollie**

**[ÉCRAN - screencast TutorLMS]**

[Installation Mollie : Add new gateway > Mollie > Install]

Mollie est la passerelle la plus simple à configurer. Installation classique, puis un seul champ à remplir : ta clé API.

Pour la trouver, dans ton compte Mollie, va dans Organization, puis More, Developers, API Keys. Copie la clé Live ou Test selon ton besoin. Colle-la dans TutorLMS, choisis l'environnement, enregistre. C'est tout.

Mollie supporte iDEAL, Bancontact, SOFORT, les cartes bancaires et d'autres méthodes européennes. C'est un bon choix si ton audience est au Benelux ou en Europe du Nord.

**PARTIE 2 - Klarna**

**[ÉCRAN - screencast TutorLMS]**

[Installation Klarna : Add new gateway > Klarna > Install]

Klarna permet le paiement en plusieurs fois - "Pay Later" ou "Slice it". Populaire en Suède, Allemagne, Pays-Bas.

Deux champs à remplir : Username et Password. Tu les génères dans le Klarna Merchant Portal, section Settings, Klarna API Keys. Clique sur "Generate new Klarna API key" et télécharge les identifiants. Important : tu dois les télécharger pour fermer la fenêtre - ils ne s'affichent qu'une fois.

Colle-les dans TutorLMS, choisis l'environnement, enregistre.

**PARTIE 3 - Alipay**

**[ÉCRAN - screencast TutorLMS]**

[Installation Alipay : Add new gateway > Alipay > Install]

Alipay, c'est le portefeuille numérique dominant en Chine. Si tu as des élèves chinois, c'est incontournable. La configuration suit le même schéma : installation, clés API depuis ton compte Alipay, configuration dans TutorLMS.

**[TRANSITION - face caméra]**

Ces trois passerelles sont complémentaires aux principales. Ajoute-les uniquement si ton audience le justifie. Pour la plupart des sites francophones, Stripe et PayPal suffisent. Mollie peut être un ajout pertinent si tu vises le Benelux.

---

**Points clés** :
- Mollie : 1 clé API, supporte iDEAL/Bancontact/SOFORT - idéal pour le Benelux
- Klarna : Username + Password, paiement fractionné - Scandinavie/Allemagne
- Alipay : portefeuille numérique - marché chinois
- Les trois suivent le même schéma d'installation dans TutorLMS
- À activer uniquement si ton audience est sur ces marchés
- Toutes nécessitent Tutor LMS Pro

**Mots clés SEO** : TutorLMS Mollie, TutorLMS Klarna, TutorLMS Alipay, passerelle paiement Europe LMS

---

### Leçon 8.12 : Paystack / 2Checkout / Authorize.net

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS pour chaque passerelle
**Source** : doc payment-gateways/paystack, 2checkout, authorize-net

---

**[INTRO - face caméra]**

Trois autres passerelles secondaires : Paystack pour l'Afrique, 2Checkout pour la couverture mondiale, Authorize.net pour les États-Unis. Même format que la leçon précédente - on va à l'essentiel.

**PARTIE 1 - Paystack**

**[ÉCRAN - screencast TutorLMS]**

[Installation Paystack : Add new gateway > Paystack > Install]

Paystack est la passerelle de référence en Afrique - Nigeria, Ghana, Afrique du Sud, Kenya. Installation classique, un seul champ principal : ta Secret Key.

Dans ton dashboard Paystack, va dans Settings, API Keys & Webhooks. Copie ta Secret Key et colle-la dans TutorLMS.

Pour le webhook, ajoute cette URL dans Paystack :

`https://tondomaine.com/wp-json/tutor/v1/ecommerce-webhook?payment_method=paystack`

Choisis l'environnement Test ou Live, enregistre.

**PARTIE 2 - 2Checkout**

**[ÉCRAN - screencast TutorLMS]**

[Installation 2Checkout : Add new gateway > 2Checkout > Install]

2Checkout - aussi connu sous le nom Verifone - couvre plus de 200 pays. C'est une alternative si tu veux une couverture géographique maximale avec une seule passerelle. Configuration : clés API depuis ton compte 2Checkout, même schéma.

**PARTIE 3 - Authorize.net**

**[ÉCRAN - screencast TutorLMS]**

[Installation Authorize.net : Add new gateway > Authorize.net > Install]

Authorize.net, c'est le vétéran des passerelles aux États-Unis. Si ton audience est américaine et que tu as déjà un compte Authorize.net, la configuration suit le même processus : clés API, environnement, webhook.

**[TRANSITION - face caméra]**

Comme pour la leçon précédente : ces passerelles sont là pour des besoins spécifiques. Paystack si tu vises l'Afrique, 2Checkout pour une couverture mondiale, Authorize.net pour le marché américain. Ne les ajoute pas "au cas où" - chaque passerelle active est un point de maintenance supplémentaire.

---

**Points clés** :
- Paystack : Secret Key + webhook - référence en Afrique
- 2Checkout (Verifone) : couverture 200+ pays
- Authorize.net : marché américain
- Webhook Paystack : URL format /wp-json/tutor/v1/ecommerce-webhook?payment_method=paystack
- N'activer que les passerelles dont ton audience a besoin
- Toutes nécessitent Tutor LMS Pro

**Mots clés SEO** : TutorLMS Paystack, TutorLMS 2Checkout, TutorLMS Authorize.net, passerelle paiement Afrique LMS

---

### Leçon 8.13 : Paiement manuel

**Durée** : 3 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Manual Payment
**Source** : doc payment-gateways/manual-payment

---

**[INTRO - face caméra]**

Tous tes élèves n'ont pas une carte bancaire ou un compte PayPal. Le paiement manuel, c'est la solution pour accepter les virements bancaires, les chèques, ou n'importe quelle méthode hors ligne. Tu reçois le paiement, tu valides manuellement la commande. Voyons comment ça marche.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods > Add manual payment]

Va dans Settings, Monetization, Payment Methods. Cette fois, clique sur "Add manual payment" au lieu de "Add new gateway".

**[ÉCRAN - screencast formulaire de configuration]**

[Montre les champs : Title, Icon, Payment Instructions]

Trois champs à remplir :

1. Title - le nom de ta méthode de paiement. Par exemple "Virement bancaire" ou "Chèque". C'est ce que l'élève verra au checkout.

2. Icon - optionnel. Tu peux uploader une icône pour rendre la méthode plus visuelle.

3. Payment Instructions - les instructions de paiement. C'est le champ le plus important. Détaille précisément ce que l'élève doit faire : à quel IBAN envoyer le virement, quelle référence indiquer, quel est le délai de traitement. Sois précis - plus tes instructions sont claires, moins tu auras de questions.

**[ÉCRAN - screencast exemple d'instructions]**

[Montre un exemple d'instructions rédigées]

Exemple pour un virement bancaire :
"Effectue un virement sur le compte suivant :
IBAN : FR76 XXXX XXXX XXXX
BIC : XXXXXXXX
Référence : ton numéro de commande
Délai : ton accès sera activé sous 48h après réception du virement."

**[ÉCRAN - screencast gestion commande manuelle]**

[Montre une commande en Pending dans Orders]

Quand un élève choisit le paiement manuel, sa commande apparaît en "Pending" dans le gestionnaire de commandes. À toi de vérifier la réception du paiement sur ton compte bancaire, puis de valider manuellement la commande pour donner accès au cours.

**[TRANSITION - face caméra]**

Le paiement manuel demande un suivi humain - ce n'est pas automatisé. Utilise-le comme complément, pas comme méthode principale. Prochaine leçon : comment migrer de WooCommerce vers le eCommerce natif.

---

**Points clés** :
- Paiement manuel dans Payment Methods > Add manual payment
- 3 champs : Title, Icon (optionnel), Payment Instructions
- Instructions claires = moins de questions (IBAN, référence, délai)
- Commandes en Pending jusqu'à validation manuelle
- Méthode complémentaire, pas principale - nécessite un suivi humain
- Tu peux créer plusieurs méthodes manuelles (virement, chèque, espèces...)

**Mots clés SEO** : TutorLMS paiement manuel, virement bancaire LMS WordPress, paiement hors ligne TutorLMS

---

### Leçon 8.14 : Migration WooCommerce vers natif

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Migration Tool
**Source** : doc migration/woocommerce-migration

---

**[INTRO - face caméra]**

Si tu utilisais WooCommerce avec TutorLMS avant la v3, tu as probablement des commandes, des coupons et peut-être des abonnements dans WooCommerce. TutorLMS fournit un outil de migration pour tout transférer vers le eCommerce natif. Mais attention : c'est une opération sensible. Voyons comment la faire proprement.

**[ÉCRAN - slide "Avant de migrer"]**

Avant toute chose : fais une sauvegarde complète de ta base de données. C'est non négociable. Si quelque chose se passe mal pendant la migration, tu dois pouvoir revenir en arrière. Utilise un plugin de backup comme UpdraftPlus ou fais un export MySQL.

**[ÉCRAN - screencast prérequis]**

[Montre les plugins nécessaires]

Les prérequis :
- TutorLMS et Tutor LMS Pro installés et actifs
- L'outil de migration TutorLMS installé
- WooCommerce toujours actif - ne le désactive pas avant la migration
- Si tu as des abonnements : WooCommerce Subscriptions doit aussi être actif

**[ÉCRAN - screencast activation eCommerce natif]**

[Navigation vers Settings > Monetization > eCommerce Engine > Native]

Première étape : active le eCommerce natif dans Settings, Monetization, eCommerce Engine, sélectionne "Native". Enregistre.

**[ÉCRAN - screencast outil de migration]**

[Navigation vers Tutor LMS Pro > Tools > WooCommerce Migration]

Deuxième étape : va dans Tutor LMS Pro, Tools, onglet WooCommerce Migration. Tu as deux options.

**[ÉCRAN - screencast migration automatique]**

[Montre le bouton "Migrate Now"]

Option 1 : Migration automatique. Clique sur "Migrate Now". TutorLMS transfère tout en une fois - commandes, coupons et abonnements. C'est la méthode la plus rapide si tu veux tout migrer.

**[ÉCRAN - screencast migration personnalisée]**

[Montre les checkboxes de sélection]

Option 2 : Migration personnalisée. Tu coches ce que tu veux migrer - commandes, coupons, abonnements - indépendamment. Utile si tu veux migrer par étapes ou si tu n'as pas besoin de tout transférer.

**[ÉCRAN - screencast résultats de migration]**

[Montre l'écran de résultats]

Après la migration, trois résultats possibles :
- Succès - tout est transféré sans erreur
- Terminé avec erreurs - la migration est faite mais certains éléments ont échoué
- Échec - rien n'a été transféré, souvent à cause d'un timeout serveur ou d'un conflit de plugin

TutorLMS garde un historique des migrations avec le détail : type de données, nombre d'éléments, date.

**[ÉCRAN - screencast vérification]**

[Montre la vérification dans Orders et Coupons]

Après migration, vérifie :
- Les commandes dans Tutor LMS > Orders - compare le nombre avec WooCommerce
- Les coupons dans Tutor LMS > Coupons
- Les abonnements dans Tutor LMS > Subscriptions
- Les accès des élèves - connecte-toi avec un compte test pour vérifier

**[TRANSITION - face caméra]**

Une fois la migration validée et testée, tu peux désactiver WooCommerce. Mais garde-le en réserve quelques semaines au cas où tu découvres un problème. Et rappelle-toi : la sauvegarde de base de données, c'est ton filet de sécurité. Ne lance jamais une migration sans.

---

**Points clés** :
- Sauvegarde de la base de données obligatoire avant migration
- Prérequis : TutorLMS Pro + outil migration + WooCommerce encore actif
- Activer le eCommerce natif avant de lancer la migration
- 2 modes : automatique (tout d'un coup) ou personnalisée (par type de données)
- 3 types migrés : commandes, coupons, abonnements
- Vérifier les données après migration avant de désactiver WooCommerce
- Historique des migrations disponible dans l'outil

**Mots clés SEO** : migration WooCommerce TutorLMS, TutorLMS eCommerce natif migration, quitter WooCommerce LMS, TutorLMS v3 migration

---

### Leçon 8.15 : Gift Course

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Gift Course
**Source** : doc gift-course

---

**[INTRO - face caméra]**

Offrir un cours en cadeau - c'est une fonctionnalité que peu de LMS proposent, et pourtant c'est un levier de vente puissant. Noël, anniversaires, cadeaux d'entreprise... TutorLMS intègre ça nativement. Voyons comment l'activer et comment ça fonctionne pour l'acheteur et le destinataire.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Course]

Pour activer le gifting, va dans Tutor LMS, Settings, Course. Active l'option "Enable Course Gifting". Enregistre. Un bouton "Gift this Course" apparaît maintenant sur toutes les pages de cours.

**[ÉCRAN - screencast front-end - acheteur]**

[Montre le bouton "Gift this Course" sur une page cours]

Côté acheteur : sur la page du cours, un bouton "Gift this Course" apparaît à côté du bouton d'achat classique. En cliquant, l'acheteur remplit :
- Le nom du destinataire
- Son adresse email
- Une date et heure de livraison - optionnel, pour programmer l'envoi
- Un message personnel - optionnel aussi

Ça fonctionne pour les cours individuels et les bundles. Ensuite, l'acheteur passe au checkout normalement et paie.

**[ÉCRAN - screencast front-end - destinataire]**

[Montre l'email reçu et le dashboard élève]

Côté destinataire : il reçoit un email avec le cadeau. Si le destinataire n'a pas de compte sur ton site, TutorLMS en crée un automatiquement et envoie un email de réinitialisation de mot de passe.

Une fois connecté, le cours offert apparaît dans une section dédiée du dashboard. Le destinataire clique sur "Reveal Gift" pour débloquer l'inscription. Le cours passe alors dans sa section "My Courses" classique.

**[ÉCRAN - screencast politique de remboursement]**

[Montre l'info remboursement]

Point important sur les remboursements : l'acheteur peut demander un remboursement uniquement avant que le destinataire ait révélé le cadeau. Une fois que le destinataire a cliqué sur "Reveal Gift", le remboursement n'est plus possible.

**[ÉCRAN - screencast personnalisation emails]**

[Navigation vers Settings > Email]

Tu peux personnaliser les emails de cadeau dans Settings > Email. Deux templates sont modifiables : la confirmation d'achat pour l'acheteur et la notification de livraison pour le destinataire. Ça nécessite l'addon Email activé.

**[TRANSITION - face caméra]**

Le gifting, c'est une source de revenus complémentaire qui ne demande aucun effort de maintenance. Active-le et laisse-le travailler. C'est la dernière leçon de contenu de ce module. On termine avec le quiz.

---

**Points clés** :
- Activation : Settings > Course > Enable Course Gifting
- Bouton "Gift this Course" sur toutes les pages cours
- Acheteur : nom, email, date programmée, message personnel
- Fonctionne pour cours individuels et bundles
- Destinataire : compte créé automatiquement si nécessaire, "Reveal Gift" pour s'inscrire
- Remboursement possible uniquement avant que le cadeau soit révélé
- Emails personnalisables dans Settings > Email (addon Email requis)

**Mots clés SEO** : TutorLMS gift course, offrir cours en ligne cadeau, TutorLMS cadeau formation, gift course LMS WordPress

---

### Leçon 8.16 : Quiz Module 8

**Durée** : ~5 min (10 questions)
**Type** : Quiz TutorLMS
**Seuil de réussite** : 70%

---

**Question 1**
Où active-t-on le eCommerce natif de TutorLMS ?

- A) Tutor LMS > Addons > eCommerce
- B) Settings > Monetization > eCommerce Engine > Native ✓
- C) Settings > General > Payments
- D) WooCommerce > Settings > TutorLMS

**Explication** : Le eCommerce natif s'active dans Settings > Monetization en sélectionnant "Native" comme eCommerce Engine.

---

**Question 2**
Quels sont les trois événements webhook obligatoires pour Stripe dans TutorLMS ?

- A) payment.success, payment.failed, payment.refund
- B) charge.succeeded, charge.failed, charge.refunded
- C) payment_intent.payment_failed, charge.updated, payment_intent.canceled ✓
- D) invoice.paid, invoice.payment_failed, customer.subscription.deleted

**Explication** : Les trois événements requis sont payment_intent.payment_failed, charge.updated et payment_intent.canceled.

---

**Question 3**
Quelle est la différence entre un abonnement par cours et une membership ?

- A) L'abonnement est gratuit, la membership est payante
- B) L'abonnement concerne un seul cours, la membership donne accès à plusieurs cours ou tout le catalogue ✓
- C) L'abonnement est mensuel, la membership est annuelle
- D) Il n'y a pas de différence

**Explication** : L'abonnement se configure cours par cours. La membership donne accès à une catégorie de cours ou à tout le site.

---

**Question 4**
Quel est l'avantage principal de Paddle par rapport aux autres passerelles ?

- A) Paddle est gratuit
- B) Paddle supporte plus de devises
- C) Paddle agit comme Merchant of Record et gère la TVA automatiquement ✓
- D) Paddle est plus rapide

**Explication** : Paddle agit comme Merchant of Record - il gère la collecte de TVA, les factures et la conformité fiscale dans chaque pays.

---

**Question 5**
Que fait l'option "Buy Now" dans les réglages Checkout ?

- A) Elle ajoute un compteur d'urgence
- B) Elle remplace le bouton "Add to Cart" par un bouton d'achat direct, sans passer par le panier ✓
- C) Elle envoie un email de relance automatique
- D) Elle active le paiement en un clic

**Explication** : "Buy Now" supprime l'étape du panier - l'élève va directement au paiement, ce qui réduit l'abandon.

---

**Question 6**
Quels types de coupons existent dans TutorLMS ?

- A) Pourcentage uniquement
- B) Montant fixe uniquement
- C) Code-based et Automatic, avec réduction en pourcentage ou montant fixe ✓
- D) Code-based uniquement, en pourcentage

**Explication** : TutorLMS propose des coupons Code-based (saisie manuelle) ou Automatic (appliqués automatiquement), avec réduction en pourcentage ou en montant fixe.

---

**Question 7**
Que faut-il faire AVANT de lancer une migration WooCommerce vers le eCommerce natif ?

- A) Désactiver WooCommerce
- B) Sauvegarder la base de données et garder WooCommerce actif ✓
- C) Supprimer tous les produits WooCommerce
- D) Mettre le site en maintenance

**Explication** : Une sauvegarde complète de la base de données est obligatoire, et WooCommerce doit rester actif pendant la migration.

---

**Question 8**
Pour un site vendant des formations en France, quel taux de TVA configurer ?

- A) 5.5%
- B) 10%
- C) 20% ✓
- D) 0% - les formations en ligne sont exonérées

**Explication** : En France, les formations en ligne sont soumises au taux normal de TVA à 20%.

---

**Question 9**
Quand un cours est offert en cadeau, à quel moment le remboursement devient-il impossible ?

- A) Dès que l'achat est effectué
- B) Après 24 heures
- C) Quand le destinataire clique sur "Reveal Gift" ✓
- D) Quand le destinataire termine le cours

**Explication** : Le remboursement est possible tant que le destinataire n'a pas révélé le cadeau. Après le "Reveal Gift", l'inscription est effective et le remboursement n'est plus disponible.

---

**Question 10**
Quelle combinaison de passerelles schoolsWP recommande-t-il pour un site européen ?

- A) PayPal uniquement
- B) Stripe + Paddle
- C) Stripe en principal + PayPal en complément ✓
- D) Mollie + Klarna

**Explication** : La recommandation schoolsWP est Stripe comme passerelle principale (cartes, Apple Pay, Google Pay) et PayPal en complément pour les élèves qui préfèrent payer via leur compte PayPal.

---

**Fin du Module 8 - eCommerce & Monétisation**

Résumé du module :
- Le eCommerce natif TutorLMS (v3+) remplace WooCommerce pour la majorité des cas
- Stripe + PayPal = combinaison recommandée pour l'Europe
- 10 passerelles intégrées + paiement manuel pour couvrir tous les marchés
- Abonnements par cours + memberships globales pour le revenu récurrent
- Coupons, taxes, checkout et commandes gérés nativement
- Migration WooCommerce disponible avec outil dédié
- Gift Course pour les ventes additionnelles

Durée totale estimée du module : ~85 minutes
