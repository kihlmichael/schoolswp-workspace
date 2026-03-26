# Scripts video — Module 8 : eCommerce & Monetisation

**Formation** : Maitriser TutorLMS
**Module** : M8 — eCommerce & Monetisation (Premium)
**Lecons** : 15 videos + 1 quiz
**Duree totale** : ~85 min
**Date** : 2026-03-23

---

### Lecon 8.1 — Vue d'ensemble eCommerce natif

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast du panneau Monetization
**Source** : Video #32 + doc native-ecommerce/overview

---

**[INTRO — face camera]**

Si tu vends des cours en ligne, tu as besoin d'un systeme de paiement. Avant la version 3, TutorLMS dependait de WooCommerce pour ca. Depuis la v3, tout est integre nativement. Plus besoin de plugin externe, plus de configuration complexe. Dans cette lecon, je te montre ce que le eCommerce natif propose et comment l'activer.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Monetization]

Pour activer le eCommerce natif, va dans Tutor LMS, puis Settings, puis Monetization. Dans le menu deroulant "eCommerce Engine", selectionne "Native". Enregistre. C'est fait.

**[ECRAN — screencast panneau Monetization]**

[Vue d'ensemble des sous-menus qui apparaissent]

Une fois active, de nouvelles sections apparaissent sous Monetization :
- Payment Methods — pour configurer tes passerelles de paiement
- Coupons — pour creer des codes de reduction
- Tax — pour gerer la TVA et les taxes
- Orders — pour suivre les commandes
- Checkout — pour parametrer la page de paiement

**[ECRAN — screencast liste des passerelles]**

[Montre la page Payment Methods avec les passerelles disponibles]

TutorLMS supporte dix passerelles de paiement :
- Stripe et PayPal — les deux principales, celles que je recommande
- Paddle, Razorpay, Mollie, Klarna, Alipay, Paystack, 2Checkout, Authorize.net
- Plus la possibilite d'ajouter un paiement manuel — virement bancaire, cheque, ce que tu veux

Chaque passerelle s'installe en un clic depuis cette page. On les verra en detail dans les prochaines lecons.

**[ECRAN — screencast section Pricing d'un cours]**

[Ouvre le Course Builder, section Pricing]

Cote cours, la section Pricing du Course Builder te permet de definir :
- Un prix unique pour un achat ponctuel
- Un abonnement avec facturation recurrente
- Ou les deux — l'eleve choisit

Tu peux aussi marquer un cours comme gratuit. On verra les abonnements et memberships dans la lecon 8.4.

**[TRANSITION — face camera]**

La recommandation schoolsWP : pour un site qui vend en Europe, configure Stripe en passerelle principale et PayPal en complement. C'est la combinaison qui couvre le plus de cas. On commence par Stripe dans la prochaine lecon.

---

**Points cles** :
- eCommerce natif active dans Settings > Monetization > eCommerce Engine > Native
- 10 passerelles integrees + paiement manuel
- Sections : Payment Methods, Coupons, Tax, Orders, Checkout
- Cours configurable en gratuit, achat unique, abonnement ou les deux
- Recommandation : Stripe + PayPal pour l'Europe

**Mots cles SEO** : TutorLMS eCommerce natif, vendre cours TutorLMS, monetisation LMS WordPress, TutorLMS v3 paiement

---

### Lecon 8.2 — Configuration Stripe

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Stripe Dashboard + TutorLMS
**Source** : Video #33 + doc payment-gateways/stripe

---

**[INTRO — face camera]**

Stripe est la passerelle de paiement numero un pour vendre des cours en ligne en Europe. Cartes bancaires, Apple Pay, Google Pay — tout passe par Stripe. Dans cette lecon, on configure Stripe dans TutorLMS de A a Z, mode test inclus.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods]

Premiere etape : installer Stripe. Va dans Settings, Monetization, Payment Methods. Clique sur "Add new gateway", selectionne Stripe dans la liste, puis clique sur Install. Active-le avec le toggle, puis clique sur l'icone de configuration.

**[ECRAN — screencast champs de configuration Stripe]**

[Montre les champs : Environment, Publishable Key, Secret Key, Webhook Secret]

Tu as quatre champs a remplir :

1. Environment — choisis "Test" pour commencer. Tu passeras en "Live" quand tout sera valide.
2. Publishable Key — ta cle publique
3. Secret Key — ta cle secrete
4. Webhook Secret — la cle du webhook

On va chercher ces trois cles dans le dashboard Stripe.

**[ECRAN — screencast Stripe Dashboard]**

[Navigation vers Developers > API keys]

Connecte-toi a ton compte Stripe. Va dans Developers, puis API keys. Tu y trouves deux cles :
- La Publishable key — elle commence par "pk_test" en mode test ou "pk_live" en production
- La Secret key — elle commence par "sk_test" ou "sk_live"

Copie chacune et colle-la dans le champ correspondant de TutorLMS.

**[ECRAN — screencast Stripe Webhooks]**

[Navigation vers Developers > Webhooks > Add destination]

Maintenant le webhook. C'est ce qui permet a Stripe de notifier TutorLMS quand un paiement est effectue, echoue ou annule.

Dans Stripe, va dans Developers, puis Webhooks, puis "Add an endpoint". Dans le champ URL, colle l'URL webhook que TutorLMS t'affiche dans ses reglages.

Ensuite, selectionne les trois evenements obligatoires :
- payment_intent.payment_failed
- charge.updated
- payment_intent.canceled

Valide. Stripe genere un Webhook Secret — copie-le et colle-le dans le dernier champ de TutorLMS.

**[ECRAN — screencast TutorLMS — Save]**

[Montre le bouton Save Changes]

Enregistre les reglages dans TutorLMS. Stripe est maintenant connecte.

**[ECRAN — screencast test d'achat]**

[Montre un achat test sur le front-end]

Avant de passer en production, teste un achat. En mode test Stripe, utilise la carte 4242 4242 4242 4242, n'importe quelle date future, n'importe quel CVC. Tu devrais voir la commande apparaitre dans TutorLMS et dans Stripe.

**[TRANSITION — face camera]**

Quand tes tests sont concluants, repasse l'environnement sur "Live", remplace les cles test par les cles de production, et met a jour le webhook. Stripe est pret. Prochaine lecon : PayPal.

---

**Points cles** :
- Installation : Settings > Monetization > Payment Methods > Add new gateway > Stripe
- 3 cles a configurer : Publishable Key, Secret Key, Webhook Secret
- Webhook : 3 evenements obligatoires (payment_intent.payment_failed, charge.updated, payment_intent.canceled)
- Toujours tester en mode Test avant de passer en Live
- Carte test : 4242 4242 4242 4242
- Cles test : prefixe pk_test / sk_test — cles live : pk_live / sk_live

**Mots cles SEO** : TutorLMS Stripe, configurer Stripe LMS WordPress, paiement Stripe TutorLMS, webhook Stripe TutorLMS

---

### Lecon 8.3 — Configuration PayPal

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast PayPal Developer + TutorLMS
**Source** : Video #34 + doc payment-gateways/paypal

---

**[INTRO — face camera]**

PayPal reste incontournable. Beaucoup d'eleves preferent payer avec leur compte PayPal plutot que de saisir une carte bancaire. C'est pour ca que je recommande de l'ajouter en complement de Stripe. Voyons comment le configurer dans TutorLMS.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods]

Bonne nouvelle : PayPal est deja dans la liste des passerelles disponibles — pas besoin de l'installer. Active-le avec le toggle, puis clique sur l'icone de configuration.

**[ECRAN — screencast champs PayPal dans TutorLMS]**

[Montre les champs : Environment, Client ID, Client Secret, Merchant Email, Webhook ID]

Tu as cinq champs :
1. Environment — Test (Sandbox) ou Live
2. Client ID
3. Client Secret Key
4. Merchant Email — l'adresse email de ton compte PayPal
5. Webhook ID

On commence en mode Sandbox pour tester.

**[ECRAN — screencast PayPal Developer]**

[Navigation vers developer.paypal.com > Apps & Credentials]

Va sur developer.paypal.com. Connecte-toi, puis va dans Apps & Credentials. Assure-toi d'etre en mode Sandbox. Clique sur "Create App", donne-lui un nom — par exemple "TutorLMS" — et valide.

Une fois l'app creee, tu vois le Client ID et le Client Secret. Copie-les dans TutorLMS.

**[ECRAN — screencast PayPal Webhooks]**

[Navigation vers la section Webhooks de l'app]

Pour le webhook, dans les reglages de ton app PayPal, va dans la section Webhooks et ajoute un nouveau webhook. Colle l'URL webhook de TutorLMS. Selectionne les deux evenements :
- Checkout order approved
- Payment capture completed

Valide. PayPal te donne un Webhook ID — copie-le et colle-le dans TutorLMS.

**[ECRAN — screencast TutorLMS — Save]**

N'oublie pas d'ajouter l'adresse email de ton compte PayPal dans le champ Merchant Email. Enregistre.

**[ECRAN — screencast test]**

[Montre un achat test via PayPal Sandbox]

Teste un achat en Sandbox. PayPal te fournit des comptes test dans le Developer Dashboard pour simuler un achat sans vrai paiement.

**[TRANSITION — face camera]**

Quand c'est valide, passe en Live, remets les cles de production et le Webhook ID live. Verifie que PayPal est bien disponible dans ton pays et ta devise. Tu as maintenant deux passerelles actives : Stripe et PayPal. Pour la plupart des sites, c'est suffisant.

---

**Points cles** :
- PayPal deja pre-installe dans TutorLMS — juste a activer
- 5 champs : Environment, Client ID, Client Secret, Merchant Email, Webhook ID
- App a creer sur developer.paypal.com > Apps & Credentials
- Webhook : 2 evenements (Checkout order approved, Payment capture completed)
- Comptes Sandbox fournis par PayPal pour les tests
- Verifier la disponibilite dans ton pays/devise

**Mots cles SEO** : TutorLMS PayPal, configurer PayPal LMS WordPress, paiement PayPal TutorLMS, PayPal sandbox TutorLMS

---

### Lecon 8.4 — Abonnements & Memberships

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Subscriptions + Memberships
**Source** : Video #35 + doc subscriptions, memberships

---

**[INTRO — face camera]**

Vendre un cours a l'unite, c'est bien. Proposer un abonnement mensuel ou une membership qui donne acces a tous tes cours, c'est un revenu recurrent. TutorLMS gere les deux nativement depuis la v3.5. Voyons comment ca marche.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS Pro > Addons]

Premiere etape : activer l'addon Subscriptions. Va dans Tutor LMS Pro, puis Addons. Cherche "Subscriptions" et active-le. C'est cet addon qui debloque a la fois les abonnements par cours et les memberships globales.

**PARTIE 1 — Abonnements par cours**

**[ECRAN — screencast Course Builder > Pricing]**

[Ouvre un cours, section Pricing]

Pour ajouter un abonnement a un cours, ouvre le Course Builder et va dans la section Pricing. Passe le cours en "Paid" si ce n'est pas deja fait. Tu vois maintenant le bouton "Add Subscription".

**[ECRAN — screencast creation abonnement]**

[Clique sur Add Subscription, montre les champs]

Clique dessus. Tu configures :
- Le nom du plan — par exemple "Acces mensuel"
- Le prix recurrent
- L'intervalle de facturation — jour, semaine, mois ou annee
- Le nombre de cycles — un nombre fixe ou "Until Cancelled" pour un abonnement continu
- Des frais d'inscription optionnels — un montant additionnel a la premiere facturation
- Un prix barre pour les promotions
- Le statut "Featured" pour mettre en avant un plan

**[ECRAN — screencast options d'achat]**

[Montre les options : Subscription only, One-time only, Both]

Tu peux proposer trois modes :
- Abonnement uniquement — l'eleve paie tant qu'il veut acceder
- Achat unique — paiement une fois, acces a vie
- Les deux — l'eleve choisit

Mon conseil : propose les deux. Ca laisse le choix et ca convient a tous les profils.

**PARTIE 2 — Memberships**

**[ECRAN — screencast Settings > Subscriptions]**

[Navigation vers Tutor LMS Pro > Settings > Subscriptions]

Les memberships, c'est un niveau au-dessus. Au lieu de gerer des abonnements cours par cours, tu crees un plan qui donne acces a plusieurs cours ou a tout ton catalogue.

Va dans Tutor LMS Pro, Settings, Subscriptions. Clique sur "New Membership Plan".

**[ECRAN — screencast creation membership]**

[Montre les champs du formulaire]

Tu retrouves les memes champs que pour un abonnement — nom, prix, intervalle, cycles — plus deux options specifiques :

Premiere option : le type d'acces. "Full Site Membership" donne acces a tous les cours du site. "Category-wise Membership" restreint l'acces a certaines categories — par exemple "Tous les cours WordPress" ou "Tous les cours Marketing".

Deuxieme option : la periode d'essai. Tu peux offrir un essai gratuit ou a prix reduit avant la premiere facturation. Et avec l'option "Skip Payment for Free Trials", l'eleve n'a meme pas besoin d'entrer sa carte bancaire pour commencer.

**[ECRAN — screencast shortcode]**

[Montre le shortcode tutor_membership_pricing sur une page]

Pour afficher tes plans sur une page, utilise le shortcode `[tutor_membership_pricing]`. Ca genere un tableau de prix propre avec tes differents plans.

**[ECRAN — screencast option Membership-only]**

Si tu veux aller plus loin, dans Settings > Subscriptions, active "Membership-only site". Ca desactive l'achat de cours individuels — tout passe par la membership. Utile si tu as un catalogue fourni et que tu veux simplifier ton offre.

**[TRANSITION — face camera]**

Abonnements par cours pour commencer, membership globale quand ton catalogue grandit. C'est une strategie progressive. Dans la prochaine lecon, on voit comment booster tes ventes avec les coupons de reduction.

---

**Points cles** :
- Addon Subscriptions a activer dans Tutor LMS Pro > Addons
- Abonnement par cours : configurable dans le Course Builder > Pricing
- Intervalles : jour, semaine, mois, annee — cycles fixes ou illimites
- Membership : Full Site ou Category-wise, avec essai gratuit possible
- Shortcode `[tutor_membership_pricing]` pour afficher les plans
- Mode "Membership-only site" pour desactiver les achats individuels
- Requiert TutorLMS v3.5+ et le eCommerce natif

**Mots cles SEO** : TutorLMS abonnement, membership TutorLMS, revenu recurrent LMS WordPress, subscription TutorLMS

---

### Lecon 8.5 — Coupons de reduction

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Coupons
**Source** : doc native-ecommerce/coupons

---

**[INTRO — face camera]**

Les coupons de reduction, c'est un levier de vente classique. Lancement, Black Friday, parrainage — tu as toujours besoin d'un code promo a un moment ou un autre. TutorLMS integre un systeme de coupons complet dans son eCommerce natif. Voyons comment creer et gerer tes codes.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Coupons]

Prerequis : le eCommerce natif doit etre active. Ensuite, va dans Tutor LMS, puis l'onglet Coupons. Clique sur "Create Coupon".

**[ECRAN — screencast formulaire de creation]**

[Montre les champs du formulaire coupon]

Premier bloc : les informations de base. Tu definis un titre interne — pour toi, pas visible par l'eleve — et un code coupon. Tu peux le taper manuellement ou laisser TutorLMS en generer un automatiquement.

**[ECRAN — screencast type de reduction]**

[Montre les options Percentage / Fixed]

Deuxieme bloc : le type de reduction. Deux choix :
- Pourcentage — par exemple 20% de reduction
- Montant fixe — par exemple 10 euros de reduction

**[ECRAN — screencast portee du coupon]**

[Montre les options All Courses, All Bundles, Specific...]

Troisieme bloc : la portee. Tu choisis sur quoi le coupon s'applique :
- Tous les cours
- Tous les bundles
- Les deux
- Ou des cours specifiques, des bundles specifiques, ou une categorie specifique

Ca te permet de creer des promos ciblees — par exemple un coupon valable uniquement sur les cours WordPress.

**[ECRAN — screencast limites d'utilisation]**

[Montre les champs de restriction]

Quatrieme bloc : les restrictions. Tu definis :
- Le nombre total d'utilisations du coupon — par exemple 100 utilisations maximum
- Le nombre d'utilisations par client — par exemple 1 par personne
- Un montant minimum d'achat
- Un nombre minimum d'articles dans le panier

**[ECRAN — screencast dates de validite]**

[Montre les champs Start/End date]

Cinquieme bloc : la periode de validite. Date et heure de debut, date et heure de fin. Si tu ne mets pas de date de fin, le coupon reste actif indefiniment.

**[ECRAN — screencast type Code vs Automatique]**

[Montre l'option coupon automatique]

Et un detail important : le type de coupon. "Code-based" — l'eleve doit saisir le code au checkout. "Automatic" — la reduction s'applique automatiquement, sans code. Pratique pour les promos sitewide.

**[ECRAN — screencast Settings > Checkout]**

Derniere chose : dans Settings > Checkout, verifie que l'option "Enable Coupon Code" est activee. Sans ca, le champ de saisie du code n'apparait pas sur la page de paiement.

**[TRANSITION — face camera]**

Les coupons sont prets. Pense a definir des dates de validite et des limites d'utilisation pour eviter les mauvaises surprises. Prochaine lecon : la configuration des taxes.

---

**Points cles** :
- Coupons dans Tutor LMS > Coupons (eCommerce natif requis)
- Deux types : Code-based (saisie manuelle) ou Automatic (applique seul)
- Reduction en pourcentage ou en montant fixe
- Portee : tous les cours, bundles, categories, ou selection specifique
- Restrictions : nombre d'utilisations total/par client, montant minimum
- Validite : dates debut/fin configurables
- Activer "Enable Coupon Code" dans Settings > Checkout

**Mots cles SEO** : TutorLMS coupons, code promo LMS WordPress, reduction cours TutorLMS, coupon TutorLMS

---

### Lecon 8.6 — Configuration taxes

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Tax settings
**Source** : doc native-ecommerce/tax

---

**[INTRO — face camera]**

La TVA, c'est pas la partie la plus excitante, mais c'est obligatoire. Si tu vends des cours en ligne depuis la France ou l'Europe, tu dois collecter et declarer la TVA. TutorLMS te permet de configurer les taxes directement dans son eCommerce natif. Voyons ca.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Taxes]

Va dans Tutor LMS, Settings, Monetization. La section "Taxes" apparait quand le eCommerce natif est active.

**[ECRAN — screencast ajout region fiscale]**

[Clique sur "Add tax region"]

Clique sur "Add tax region" pour creer ta premiere zone fiscale. Tu selectionnes un pays — par exemple France — et tu definis le taux de TVA. Pour la France, c'est 20% sur les formations en ligne.

Tu peux appliquer un taux unique a tout le pays, ou definir des taux differents par region ou province. Utile si tu vends dans des pays avec des taux variables selon les etats — comme les USA ou le Canada.

**[ECRAN — screencast reglages globaux]**

[Montre les trois options globales]

Ensuite, trois reglages globaux importants :

Premier reglage : "Tax Already Included in Prices". Active-le si tes prix affichent deja la TVA incluse — ce qui est la norme en France pour le B2C. L'eleve voit le prix final, pas de surprise au checkout.

Deuxieme reglage : "Tax Calculated at Checkout". La taxe s'affiche uniquement au moment du paiement. Utile pour le B2B ou les marches ou les prix sont affiches HT.

Troisieme reglage : "Display Prices Inclusive of Tax". Quand c'est active, les prix affiches sur le site incluent la taxe partout — page cours, catalogue, checkout.

**[ECRAN — screencast reglage par cours]**

[Montre l'option dans le Course Builder]

Bonus : tu peux aussi gerer la taxe cours par cours. Dans le Course Builder, section Pricing, des options apparaissent pour activer ou desactiver la taxe sur les achats ponctuels et sur les abonnements. Ces options n'apparaissent que quand le cours a un prix defini.

**[TRANSITION — face camera]**

Pour un site francais, la configuration typique, c'est : une region France a 20%, prix TTC affiches. Adapte selon ton pays. Si tu utilises Paddle comme passerelle, note que Paddle gere ses propres calculs de taxes — les reglages TutorLMS ne s'appliquent pas. Dans la prochaine lecon, on parle de la gestion des commandes.

---

**Points cles** :
- Taxes dans Settings > Monetization > Taxes (eCommerce natif requis)
- Ajout de regions fiscales par pays, avec taux personnalisable par region
- France : 20% TVA sur les formations en ligne
- 3 modes : taxes incluses dans le prix, calculees au checkout, affichees TTC
- Configuration possible cours par cours dans le Course Builder
- Exception Paddle : gere ses propres taxes

**Mots cles SEO** : TutorLMS TVA, taxes LMS WordPress, configurer TVA formation en ligne, TutorLMS taxe France

---

### Lecon 8.7 — Gestion des commandes

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Orders
**Source** : doc native-ecommerce/orders

---

**[INTRO — face camera]**

Chaque vente genere une commande. Suivi des paiements, remboursements, problemes de transaction — tout se passe dans le gestionnaire de commandes de TutorLMS. Voyons comment l'utiliser au quotidien.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Orders]

Va dans Tutor LMS, puis Orders. Tu retrouves la liste de toutes les commandes avec :
- Le numero de commande
- Le nom de l'eleve
- Le cours achete
- Le montant
- La date
- Le statut

**[ECRAN — screencast filtres et statuts]**

[Montre les filtres disponibles]

Les statuts possibles :
- Completed — paiement recu et valide
- Pending — en attente de confirmation du paiement
- Cancelled — annulee
- Refunded — remboursee

Tu peux filtrer par statut pour retrouver rapidement les commandes qui posent probleme. Les commandes en "Pending" sont celles a surveiller — ca signifie que la passerelle de paiement n'a pas confirme la transaction.

**[ECRAN — screencast detail d'une commande]**

[Clique sur une commande pour voir le detail]

En cliquant sur une commande, tu vois le detail complet : informations de l'eleve, methode de paiement utilisee, coupon applique le cas echeant, montant HT, taxe, total.

**[ECRAN — screencast commande bloquee]**

[Montre une commande en Pending]

Si une commande reste en "Pending", deux causes possibles. Premiere : la passerelle de paiement n'a pas envoye la confirmation — verifie que ton webhook est correctement configure. Deuxieme : le paiement a echoue cote banque — l'eleve doit reessayer.

Dans les deux cas, ne valide jamais manuellement une commande sans avoir verifie le paiement dans le dashboard de ta passerelle — Stripe ou PayPal.

**[ECRAN — screencast remboursement]**

[Montre le processus de remboursement]

Pour un remboursement, le processus depend de ta passerelle. En general, tu lances le remboursement depuis le dashboard Stripe ou PayPal, et le statut se met a jour automatiquement dans TutorLMS via le webhook. L'eleve perd l'acces au cours apres remboursement.

**[TRANSITION — face camera]**

Le gestionnaire de commandes est ton tableau de bord financier dans TutorLMS. Consulte-le regulierement, surtout les premiers jours apres un lancement. Dans la prochaine lecon, on optimise l'experience d'achat avec la configuration du checkout.

---

**Points cles** :
- Commandes dans Tutor LMS > Orders
- 4 statuts : Completed, Pending, Cancelled, Refunded
- Commandes Pending : verifier le webhook ou le paiement cote passerelle
- Ne jamais valider manuellement sans verification dans Stripe/PayPal
- Remboursements : lancer depuis la passerelle, statut mis a jour via webhook
- Detail commande : eleve, methode, coupon, montant, taxe

**Mots cles SEO** : TutorLMS commandes, gestion commandes LMS WordPress, remboursement TutorLMS, suivi ventes TutorLMS

---

### Lecon 8.8 — Configuration checkout

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Checkout settings
**Source** : doc native-ecommerce/checkout

---

**[INTRO — face camera]**

Le checkout, c'est la derniere etape avant le paiement. C'est la ou tu perds des ventes si l'experience est mauvaise. TutorLMS propose trois reglages cles pour optimiser cette page. Voyons-les.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Checkout]

Va dans Settings, Monetization, puis Checkout. Trois options t'attendent.

**[ECRAN — screencast option Coupon Code]**

[Montre le toggle Enable Coupon Code]

Premiere option : "Enable Coupon Code". Active-la si tu utilises des coupons — on les a configures dans la lecon 8.5. Si tu ne proposes pas de coupons, desactive-la pour ne pas afficher un champ vide qui fait douter l'eleve ("est-ce que je rate une promo ?").

**[ECRAN — screencast option Buy Now]**

[Montre le toggle Buy Now]

Deuxieme option : "Buy Now". Quand c'est active, le bouton "Add to Cart" sur la page du cours est remplace par un bouton "Buy Now". L'eleve va directement au paiement sans passer par un panier. Moins d'etapes, moins d'abandon. Je recommande de l'activer si tu vends des cours a l'unite.

**[ECRAN — screencast option Guest Checkout]**

[Montre le toggle Guest Checkout]

Troisieme option : "Guest Checkout". L'eleve peut acheter sans creer de compte au prealable. TutorLMS cree le compte automatiquement avec les informations de facturation et envoie un email de reinitialisation de mot de passe. L'eleve definit son mot de passe, et il a acces a son cours.

C'est un bon compromis : tu reduis la friction a l'achat sans perdre la creation de compte.

Quand le Guest Checkout est actif, un bouton de connexion apparait aussi sur la page checkout pour les clients existants.

**[TRANSITION — face camera]**

Ma recommandation : active "Buy Now" et "Guest Checkout" pour maximiser tes conversions. Desactive le champ coupon si tu n'en utilises pas. Simple et efficace. Prochaine lecon : Paddle, une passerelle alternative qui gere la TVA a ta place.

---

**Points cles** :
- Checkout dans Settings > Monetization > Checkout
- 3 options : Enable Coupon Code, Buy Now, Guest Checkout
- Buy Now : supprime le panier, achat direct — reduit l'abandon
- Guest Checkout : achat sans compte, creation automatique + email mot de passe
- Desactiver le champ coupon si pas de promos (evite le doute)
- Recommandation : Buy Now + Guest Checkout actifs

**Mots cles SEO** : TutorLMS checkout, page paiement LMS WordPress, optimiser checkout TutorLMS, guest checkout TutorLMS

---

### Lecon 8.9 — Paddle

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Paddle Dashboard + TutorLMS
**Source** : doc payment-gateways/paddle

---

**[INTRO — face camera]**

Paddle, c'est different des autres passerelles. Paddle agit comme "Merchant of Record" — ca veut dire que c'est Paddle qui vend ton cours a ta place, gere la TVA, les factures et la conformite fiscale dans chaque pays. Si tu vends a l'international et que tu ne veux pas te prendre la tete avec la TVA par pays, Paddle est une option serieuse.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods > Add new gateway > Paddle]

Installation classique : Settings, Monetization, Payment Methods, Add new gateway, selectionne Paddle, Install, active le toggle.

**[ECRAN — screencast champs de configuration]**

[Montre les champs : Environment, API Key, Client-side Token, Webhook Secret]

Trois cles a recuperer dans ton dashboard Paddle :

1. API Key — dans Developer Tools > Authentication. Genere une nouvelle cle avec les permissions adequates.
2. Client-side Token — genere separement, utilise pour les transactions front-end.
3. Webhook Secret — configure dans Developer Tools > Notifications.

**[ECRAN — screencast Paddle Webhooks]**

[Navigation vers Developer Tools > Notifications > Create webhook]

Pour le webhook, dans Paddle, va dans Developer Tools, Notifications, et cree un nouveau webhook. L'URL a utiliser :

`https://tondomaine.com/wp-json/tutor/v1/ecommerce-webhook?payment_method=paddle`

Selectionne trois evenements :
- Transaction.completed
- Adjustment.created
- Adjustment.updated

Copie le Secret genere et colle-le dans TutorLMS.

**[ECRAN — screencast approbation domaine]**

[Montre Checkout > Website Approval dans Paddle]

Etape supplementaire avec Paddle : tu dois faire approuver ton domaine. Dans Paddle, va dans Checkout, Website Approval, et soumets ton domaine — juste le domaine, sans https://. Configure aussi ton URL comme lien de paiement par defaut dans les reglages Checkout.

**[TRANSITION — face camera]**

Point important : quand tu utilises Paddle, les reglages de taxes de TutorLMS ne s'appliquent pas. C'est Paddle qui gere tout le calcul fiscal. Pratique, mais tu perds le controle sur l'affichage des prix. A toi de voir si ca correspond a ton modele.

---

**Points cles** :
- Paddle = Merchant of Record : gere TVA, factures, conformite fiscale
- 3 cles : API Key, Client-side Token, Webhook Secret
- Webhook : 3 evenements (Transaction.completed, Adjustment.created, Adjustment.updated)
- Approbation du domaine obligatoire dans Paddle
- Les taxes TutorLMS ne s'appliquent pas avec Paddle
- Les clients TVA peuvent saisir leur numero de TVA au checkout Paddle

**Mots cles SEO** : TutorLMS Paddle, Paddle LMS WordPress, Merchant of Record LMS, TVA automatique formation en ligne

---

### Lecon 8.10 — Razorpay

**Duree** : 3 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Razorpay Dashboard + TutorLMS
**Source** : doc payment-gateways/razorpay

---

**[INTRO — face camera]**

Razorpay, c'est la passerelle de reference en Inde. Si ton audience est indienne ou si tu veux accepter UPI, net banking ou les portefeuilles numeriques indiens, c'est la passerelle qu'il te faut. Configuration rapide.

**[ECRAN — screencast TutorLMS admin]**

[Installation Razorpay : Add new gateway > Razorpay > Install]

Meme processus : Settings, Monetization, Payment Methods, Add new gateway, Razorpay, Install, active le toggle.

**[ECRAN — screencast champs de configuration]**

[Montre les champs : Environment, Key ID, Key Secret, Webhook Secret]

Trois informations a recuperer dans ton dashboard Razorpay, section Account & Settings, puis API Keys :
- Key ID
- Key Secret

Clique sur "Generate Test Key" pour les cles de test. Tu peux telecharger les deux cles en CSV.

**[ECRAN — screencast Razorpay Webhooks]**

[Navigation vers Account & Settings > Webhooks]

Pour le webhook, dans Razorpay, va dans Account & Settings, Webhooks, "Add New Webhook". L'URL :

`https://tondomaine.com/wp-json/tutor/v1/ecommerce-webhook?payment_method=razorpay`

Selectionne deux evenements :
- Payment Failed
- Payment Captured

Definis un Webhook Secret — attention, tu dois saisir le meme secret manuellement dans TutorLMS. Ce n'est pas genere automatiquement comme avec Stripe.

Enregistre des deux cotes et c'est operationnel.

**[TRANSITION — face camera]**

Razorpay est specifique au marche indien. Si tu ne vises pas cette audience, passe a la lecon suivante. Sinon, c'est une passerelle fiable avec un bon support des methodes de paiement locales.

---

**Points cles** :
- Razorpay : reference en Inde (UPI, net banking, wallets)
- 3 cles : Key ID, Key Secret, Webhook Secret
- Webhook : 2 evenements (Payment Failed, Payment Captured)
- Webhook Secret a definir manuellement (identique des deux cotes)
- Verifier la disponibilite dans ton pays/devise avant configuration

**Mots cles SEO** : TutorLMS Razorpay, paiement Inde LMS WordPress, Razorpay formation en ligne

---

### Lecon 8.11 — Mollie / Klarna / Alipay

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS pour chaque passerelle
**Source** : doc payment-gateways/mollie, klarna, alipay

---

**[INTRO — face camera]**

Trois passerelles dans une seule lecon : Mollie, Klarna et Alipay. Chacune couvre un marche specifique. Mollie pour les Pays-Bas et l'Europe du Nord, Klarna pour le paiement fractionne en Scandinavie et en Allemagne, Alipay pour la Chine. Voyons la configuration de chacune.

**PARTIE 1 — Mollie**

**[ECRAN — screencast TutorLMS]**

[Installation Mollie : Add new gateway > Mollie > Install]

Mollie est la passerelle la plus simple a configurer. Installation classique, puis un seul champ a remplir : ta cle API.

Pour la trouver, dans ton compte Mollie, va dans Organization, puis More, Developers, API Keys. Copie la cle Live ou Test selon ton besoin. Colle-la dans TutorLMS, choisis l'environnement, enregistre. C'est tout.

Mollie supporte iDEAL, Bancontact, SOFORT, les cartes bancaires et d'autres methodes europeennes. C'est un bon choix si ton audience est au Benelux ou en Europe du Nord.

**PARTIE 2 — Klarna**

**[ECRAN — screencast TutorLMS]**

[Installation Klarna : Add new gateway > Klarna > Install]

Klarna permet le paiement en plusieurs fois — "Pay Later" ou "Slice it". Populaire en Suede, Allemagne, Pays-Bas.

Deux champs a remplir : Username et Password. Tu les generes dans le Klarna Merchant Portal, section Settings, Klarna API Keys. Clique sur "Generate new Klarna API key" et telecharge les identifiants. Important : tu dois les telecharger pour fermer la fenetre — ils ne s'affichent qu'une fois.

Colle-les dans TutorLMS, choisis l'environnement, enregistre.

**PARTIE 3 — Alipay**

**[ECRAN — screencast TutorLMS]**

[Installation Alipay : Add new gateway > Alipay > Install]

Alipay, c'est le portefeuille numerique dominant en Chine. Si tu as des eleves chinois, c'est incontournable. La configuration suit le meme schema : installation, cles API depuis ton compte Alipay, configuration dans TutorLMS.

**[TRANSITION — face camera]**

Ces trois passerelles sont complementaires aux principales. Ajoute-les uniquement si ton audience le justifie. Pour la plupart des sites francophones, Stripe et PayPal suffisent. Mollie peut etre un ajout pertinent si tu vises le Benelux.

---

**Points cles** :
- Mollie : 1 cle API, supporte iDEAL/Bancontact/SOFORT — ideal pour le Benelux
- Klarna : Username + Password, paiement fractionne — Scandinavie/Allemagne
- Alipay : portefeuille numerique — marche chinois
- Les trois suivent le meme schema d'installation dans TutorLMS
- A activer uniquement si ton audience est sur ces marches
- Toutes necessitent Tutor LMS Pro

**Mots cles SEO** : TutorLMS Mollie, TutorLMS Klarna, TutorLMS Alipay, passerelle paiement Europe LMS

---

### Lecon 8.12 — Paystack / 2Checkout / Authorize.net

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS pour chaque passerelle
**Source** : doc payment-gateways/paystack, 2checkout, authorize-net

---

**[INTRO — face camera]**

Trois autres passerelles secondaires : Paystack pour l'Afrique, 2Checkout pour la couverture mondiale, Authorize.net pour les Etats-Unis. Meme format que la lecon precedente — on va a l'essentiel.

**PARTIE 1 — Paystack**

**[ECRAN — screencast TutorLMS]**

[Installation Paystack : Add new gateway > Paystack > Install]

Paystack est la passerelle de reference en Afrique — Nigeria, Ghana, Afrique du Sud, Kenya. Installation classique, un seul champ principal : ta Secret Key.

Dans ton dashboard Paystack, va dans Settings, API Keys & Webhooks. Copie ta Secret Key et colle-la dans TutorLMS.

Pour le webhook, ajoute cette URL dans Paystack :

`https://tondomaine.com/wp-json/tutor/v1/ecommerce-webhook?payment_method=paystack`

Choisis l'environnement Test ou Live, enregistre.

**PARTIE 2 — 2Checkout**

**[ECRAN — screencast TutorLMS]**

[Installation 2Checkout : Add new gateway > 2Checkout > Install]

2Checkout — aussi connu sous le nom Verifone — couvre plus de 200 pays. C'est une alternative si tu veux une couverture geographique maximale avec une seule passerelle. Configuration : cles API depuis ton compte 2Checkout, meme schema.

**PARTIE 3 — Authorize.net**

**[ECRAN — screencast TutorLMS]**

[Installation Authorize.net : Add new gateway > Authorize.net > Install]

Authorize.net, c'est le veteran des passerelles aux Etats-Unis. Si ton audience est americaine et que tu as deja un compte Authorize.net, la configuration suit le meme processus : cles API, environnement, webhook.

**[TRANSITION — face camera]**

Comme pour la lecon precedente : ces passerelles sont la pour des besoins specifiques. Paystack si tu vises l'Afrique, 2Checkout pour une couverture mondiale, Authorize.net pour le marche americain. Ne les ajoute pas "au cas ou" — chaque passerelle active est un point de maintenance supplementaire.

---

**Points cles** :
- Paystack : Secret Key + webhook — reference en Afrique
- 2Checkout (Verifone) : couverture 200+ pays
- Authorize.net : marche americain
- Webhook Paystack : URL format /wp-json/tutor/v1/ecommerce-webhook?payment_method=paystack
- N'activer que les passerelles dont ton audience a besoin
- Toutes necessitent Tutor LMS Pro

**Mots cles SEO** : TutorLMS Paystack, TutorLMS 2Checkout, TutorLMS Authorize.net, passerelle paiement Afrique LMS

---

### Lecon 8.13 — Paiement manuel

**Duree** : 3 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Manual Payment
**Source** : doc payment-gateways/manual-payment

---

**[INTRO — face camera]**

Tous tes eleves n'ont pas une carte bancaire ou un compte PayPal. Le paiement manuel, c'est la solution pour accepter les virements bancaires, les cheques, ou n'importe quelle methode hors ligne. Tu recois le paiement, tu valides manuellement la commande. Voyons comment ca marche.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > Payment Methods > Add manual payment]

Va dans Settings, Monetization, Payment Methods. Cette fois, clique sur "Add manual payment" au lieu de "Add new gateway".

**[ECRAN — screencast formulaire de configuration]**

[Montre les champs : Title, Icon, Payment Instructions]

Trois champs a remplir :

1. Title — le nom de ta methode de paiement. Par exemple "Virement bancaire" ou "Cheque". C'est ce que l'eleve verra au checkout.

2. Icon — optionnel. Tu peux uploader une icone pour rendre la methode plus visuelle.

3. Payment Instructions — les instructions de paiement. C'est le champ le plus important. Detaille precisement ce que l'eleve doit faire : a quel IBAN envoyer le virement, quelle reference indiquer, quel est le delai de traitement. Sois precis — plus tes instructions sont claires, moins tu auras de questions.

**[ECRAN — screencast exemple d'instructions]**

[Montre un exemple d'instructions redigees]

Exemple pour un virement bancaire :
"Effectue un virement sur le compte suivant :
IBAN : FR76 XXXX XXXX XXXX
BIC : XXXXXXXX
Reference : ton numero de commande
Delai : ton acces sera active sous 48h apres reception du virement."

**[ECRAN — screencast gestion commande manuelle]**

[Montre une commande en Pending dans Orders]

Quand un eleve choisit le paiement manuel, sa commande apparait en "Pending" dans le gestionnaire de commandes. A toi de verifier la reception du paiement sur ton compte bancaire, puis de valider manuellement la commande pour donner acces au cours.

**[TRANSITION — face camera]**

Le paiement manuel demande un suivi humain — ce n'est pas automatise. Utilise-le comme complement, pas comme methode principale. Prochaine lecon : comment migrer de WooCommerce vers le eCommerce natif.

---

**Points cles** :
- Paiement manuel dans Payment Methods > Add manual payment
- 3 champs : Title, Icon (optionnel), Payment Instructions
- Instructions claires = moins de questions (IBAN, reference, delai)
- Commandes en Pending jusqu'a validation manuelle
- Methode complementaire, pas principale — necessite un suivi humain
- Tu peux creer plusieurs methodes manuelles (virement, cheque, especes...)

**Mots cles SEO** : TutorLMS paiement manuel, virement bancaire LMS WordPress, paiement hors ligne TutorLMS

---

### Lecon 8.14 — Migration WooCommerce vers natif

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Migration Tool
**Source** : doc migration/woocommerce-migration

---

**[INTRO — face camera]**

Si tu utilisais WooCommerce avec TutorLMS avant la v3, tu as probablement des commandes, des coupons et peut-etre des abonnements dans WooCommerce. TutorLMS fournit un outil de migration pour tout transferer vers le eCommerce natif. Mais attention : c'est une operation sensible. Voyons comment la faire proprement.

**[ECRAN — slide "Avant de migrer"]**

Avant toute chose : fais une sauvegarde complete de ta base de donnees. C'est non negociable. Si quelque chose se passe mal pendant la migration, tu dois pouvoir revenir en arriere. Utilise un plugin de backup comme UpdraftPlus ou fais un export MySQL.

**[ECRAN — screencast prerequis]**

[Montre les plugins necessaires]

Les prerequis :
- TutorLMS et Tutor LMS Pro installes et actifs
- L'outil de migration TutorLMS installe
- WooCommerce toujours actif — ne le desactive pas avant la migration
- Si tu as des abonnements : WooCommerce Subscriptions doit aussi etre actif

**[ECRAN — screencast activation eCommerce natif]**

[Navigation vers Settings > Monetization > eCommerce Engine > Native]

Premiere etape : active le eCommerce natif dans Settings, Monetization, eCommerce Engine, selectionne "Native". Enregistre.

**[ECRAN — screencast outil de migration]**

[Navigation vers Tutor LMS Pro > Tools > WooCommerce Migration]

Deuxieme etape : va dans Tutor LMS Pro, Tools, onglet WooCommerce Migration. Tu as deux options.

**[ECRAN — screencast migration automatique]**

[Montre le bouton "Migrate Now"]

Option 1 : Migration automatique. Clique sur "Migrate Now". TutorLMS transfere tout en une fois — commandes, coupons et abonnements. C'est la methode la plus rapide si tu veux tout migrer.

**[ECRAN — screencast migration personnalisee]**

[Montre les checkboxes de selection]

Option 2 : Migration personnalisee. Tu coches ce que tu veux migrer — commandes, coupons, abonnements — independamment. Utile si tu veux migrer par etapes ou si tu n'as pas besoin de tout transferer.

**[ECRAN — screencast resultats de migration]**

[Montre l'ecran de resultats]

Apres la migration, trois resultats possibles :
- Succes — tout est transfere sans erreur
- Termine avec erreurs — la migration est faite mais certains elements ont echoue
- Echec — rien n'a ete transfere, souvent a cause d'un timeout serveur ou d'un conflit de plugin

TutorLMS garde un historique des migrations avec le detail : type de donnees, nombre d'elements, date.

**[ECRAN — screencast verification]**

[Montre la verification dans Orders et Coupons]

Apres migration, verifie :
- Les commandes dans Tutor LMS > Orders — compare le nombre avec WooCommerce
- Les coupons dans Tutor LMS > Coupons
- Les abonnements dans Tutor LMS > Subscriptions
- Les acces des eleves — connecte-toi avec un compte test pour verifier

**[TRANSITION — face camera]**

Une fois la migration validee et testee, tu peux desactiver WooCommerce. Mais garde-le en reserve quelques semaines au cas ou tu decouvres un probleme. Et rappelle-toi : la sauvegarde de base de donnees, c'est ton filet de securite. Ne lance jamais une migration sans.

---

**Points cles** :
- Sauvegarde de la base de donnees obligatoire avant migration
- Prerequis : TutorLMS Pro + outil migration + WooCommerce encore actif
- Activer le eCommerce natif avant de lancer la migration
- 2 modes : automatique (tout d'un coup) ou personnalisee (par type de donnees)
- 3 types migres : commandes, coupons, abonnements
- Verifier les donnees apres migration avant de desactiver WooCommerce
- Historique des migrations disponible dans l'outil

**Mots cles SEO** : migration WooCommerce TutorLMS, TutorLMS eCommerce natif migration, quitter WooCommerce LMS, TutorLMS v3 migration

---

### Lecon 8.15 — Gift Course

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS Gift Course
**Source** : doc gift-course

---

**[INTRO — face camera]**

Offrir un cours en cadeau — c'est une fonctionnalite que peu de LMS proposent, et pourtant c'est un levier de vente puissant. Noel, anniversaires, cadeaux d'entreprise... TutorLMS integre ca nativement. Voyons comment l'activer et comment ca fonctionne pour l'acheteur et le destinataire.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Course]

Pour activer le gifting, va dans Tutor LMS, Settings, Course. Active l'option "Enable Course Gifting". Enregistre. Un bouton "Gift this Course" apparait maintenant sur toutes les pages de cours.

**[ECRAN — screencast front-end — acheteur]**

[Montre le bouton "Gift this Course" sur une page cours]

Cote acheteur : sur la page du cours, un bouton "Gift this Course" apparait a cote du bouton d'achat classique. En cliquant, l'acheteur remplit :
- Le nom du destinataire
- Son adresse email
- Une date et heure de livraison — optionnel, pour programmer l'envoi
- Un message personnel — optionnel aussi

Ca fonctionne pour les cours individuels et les bundles. Ensuite, l'acheteur passe au checkout normalement et paie.

**[ECRAN — screencast front-end — destinataire]**

[Montre l'email recu et le dashboard eleve]

Cote destinataire : il recoit un email avec le cadeau. Si le destinataire n'a pas de compte sur ton site, TutorLMS en cree un automatiquement et envoie un email de reinitialisation de mot de passe.

Une fois connecte, le cours offert apparait dans une section dediee du dashboard. Le destinataire clique sur "Reveal Gift" pour debloquer l'inscription. Le cours passe alors dans sa section "My Courses" classique.

**[ECRAN — screencast politique de remboursement]**

[Montre l'info remboursement]

Point important sur les remboursements : l'acheteur peut demander un remboursement uniquement avant que le destinataire ait revele le cadeau. Une fois que le destinataire a clique sur "Reveal Gift", le remboursement n'est plus possible.

**[ECRAN — screencast personnalisation emails]**

[Navigation vers Settings > Email]

Tu peux personnaliser les emails de cadeau dans Settings > Email. Deux templates sont modifiables : la confirmation d'achat pour l'acheteur et la notification de livraison pour le destinataire. Ca necessite l'addon Email active.

**[TRANSITION — face camera]**

Le gifting, c'est une source de revenus complementaire qui ne demande aucun effort de maintenance. Active-le et laisse-le travailler. C'est la derniere lecon de contenu de ce module. On termine avec le quiz.

---

**Points cles** :
- Activation : Settings > Course > Enable Course Gifting
- Bouton "Gift this Course" sur toutes les pages cours
- Acheteur : nom, email, date programmee, message personnel
- Fonctionne pour cours individuels et bundles
- Destinataire : compte cree automatiquement si necessaire, "Reveal Gift" pour s'inscrire
- Remboursement possible uniquement avant que le cadeau soit revele
- Emails personnalisables dans Settings > Email (addon Email requis)

**Mots cles SEO** : TutorLMS gift course, offrir cours en ligne cadeau, TutorLMS cadeau formation, gift course LMS WordPress

---

### Lecon 8.16 — Quiz Module 8

**Duree** : ~5 min (10 questions)
**Type** : Quiz TutorLMS
**Seuil de reussite** : 70%

---

**Question 1**
Ou active-t-on le eCommerce natif de TutorLMS ?

- A) Tutor LMS > Addons > eCommerce
- B) Settings > Monetization > eCommerce Engine > Native ✓
- C) Settings > General > Payments
- D) WooCommerce > Settings > TutorLMS

**Explication** : Le eCommerce natif s'active dans Settings > Monetization en selectionnant "Native" comme eCommerce Engine.

---

**Question 2**
Quels sont les trois evenements webhook obligatoires pour Stripe dans TutorLMS ?

- A) payment.success, payment.failed, payment.refund
- B) charge.succeeded, charge.failed, charge.refunded
- C) payment_intent.payment_failed, charge.updated, payment_intent.canceled ✓
- D) invoice.paid, invoice.payment_failed, customer.subscription.deleted

**Explication** : Les trois evenements requis sont payment_intent.payment_failed, charge.updated et payment_intent.canceled.

---

**Question 3**
Quelle est la difference entre un abonnement par cours et une membership ?

- A) L'abonnement est gratuit, la membership est payante
- B) L'abonnement concerne un seul cours, la membership donne acces a plusieurs cours ou tout le catalogue ✓
- C) L'abonnement est mensuel, la membership est annuelle
- D) Il n'y a pas de difference

**Explication** : L'abonnement se configure cours par cours. La membership donne acces a une categorie de cours ou a tout le site.

---

**Question 4**
Quel est l'avantage principal de Paddle par rapport aux autres passerelles ?

- A) Paddle est gratuit
- B) Paddle supporte plus de devises
- C) Paddle agit comme Merchant of Record et gere la TVA automatiquement ✓
- D) Paddle est plus rapide

**Explication** : Paddle agit comme Merchant of Record — il gere la collecte de TVA, les factures et la conformite fiscale dans chaque pays.

---

**Question 5**
Que fait l'option "Buy Now" dans les reglages Checkout ?

- A) Elle ajoute un compteur d'urgence
- B) Elle remplace le bouton "Add to Cart" par un bouton d'achat direct, sans passer par le panier ✓
- C) Elle envoie un email de relance automatique
- D) Elle active le paiement en un clic

**Explication** : "Buy Now" supprime l'etape du panier — l'eleve va directement au paiement, ce qui reduit l'abandon.

---

**Question 6**
Quels types de coupons existent dans TutorLMS ?

- A) Pourcentage uniquement
- B) Montant fixe uniquement
- C) Code-based et Automatic, avec reduction en pourcentage ou montant fixe ✓
- D) Code-based uniquement, en pourcentage

**Explication** : TutorLMS propose des coupons Code-based (saisie manuelle) ou Automatic (appliques automatiquement), avec reduction en pourcentage ou en montant fixe.

---

**Question 7**
Que faut-il faire AVANT de lancer une migration WooCommerce vers le eCommerce natif ?

- A) Desactiver WooCommerce
- B) Sauvegarder la base de donnees et garder WooCommerce actif ✓
- C) Supprimer tous les produits WooCommerce
- D) Mettre le site en maintenance

**Explication** : Une sauvegarde complete de la base de donnees est obligatoire, et WooCommerce doit rester actif pendant la migration.

---

**Question 8**
Pour un site vendant des formations en France, quel taux de TVA configurer ?

- A) 5.5%
- B) 10%
- C) 20% ✓
- D) 0% — les formations en ligne sont exonerees

**Explication** : En France, les formations en ligne sont soumises au taux normal de TVA a 20%.

---

**Question 9**
Quand un cours est offert en cadeau, a quel moment le remboursement devient-il impossible ?

- A) Des que l'achat est effectue
- B) Apres 24 heures
- C) Quand le destinataire clique sur "Reveal Gift" ✓
- D) Quand le destinataire termine le cours

**Explication** : Le remboursement est possible tant que le destinataire n'a pas revele le cadeau. Apres le "Reveal Gift", l'inscription est effective et le remboursement n'est plus disponible.

---

**Question 10**
Quelle combinaison de passerelles schoolsWP recommande-t-il pour un site europeen ?

- A) PayPal uniquement
- B) Stripe + Paddle
- C) Stripe en principal + PayPal en complement ✓
- D) Mollie + Klarna

**Explication** : La recommandation schoolsWP est Stripe comme passerelle principale (cartes, Apple Pay, Google Pay) et PayPal en complement pour les eleves qui preferent payer via leur compte PayPal.

---

**Fin du Module 8 — eCommerce & Monetisation**

Resume du module :
- Le eCommerce natif TutorLMS (v3+) remplace WooCommerce pour la majorite des cas
- Stripe + PayPal = combinaison recommandee pour l'Europe
- 10 passerelles integrees + paiement manuel pour couvrir tous les marches
- Abonnements par cours + memberships globales pour le revenu recurrent
- Coupons, taxes, checkout et commandes geres nativement
- Migration WooCommerce disponible avec outil dedie
- Gift Course pour les ventes additionnelles

Duree totale estimee du module : ~85 minutes
