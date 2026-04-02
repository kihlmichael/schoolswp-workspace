# Script video — Module 4, Lecon 1 : Passerelles de paiement

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 — Paiements
**Lecon** : 1/7 — Passerelles de paiement
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast Payment Settings, slides comparatif passerelles
**Objectif** : Comprendre les 4 passerelles disponibles et configurer Stripe correctement

---

**[INTRO — face camera]**

FluentForms ne fait pas que collecter des donnees — il encaisse des paiements. Directement dans WordPress, sans WooCommerce, sans plugin supplementaire.

Aujourd'hui on passe en revue les quatre passerelles disponibles, et on configure ensemble celle que je te recommande.

**[SECTION 1 — slide "4 passerelles disponibles"]**

FluentForms supporte quatre passerelles de paiement.

Stripe. C'est la reference. Cartes bancaires, Apple Pay, Google Pay. API solide, dashboard clair, frais transparents. C'est celle que j'utilise et que je recommande pour la plupart des cas.

PayPal. Le classique. Certains clients preferent payer via leur compte PayPal. Si tu vends a l'international, avoir PayPal en option est pertinent.

Razorpay. Populaire en Inde et en Asie du Sud. Si ton audience est la-bas, c'est la passerelle locale de reference.

Mollie. Populaire en Europe, notamment aux Pays-Bas, en Belgique et en Allemagne. Elle supporte iDEAL, Bancontact, SOFORT — des methodes de paiement locales que Stripe ne gere pas toujours nativement.

Pour un site francophone, Stripe est le choix par defaut. Tu peux ajouter PayPal ou Mollie en complement si tes clients le demandent.

**[SECTION 2 — screencast "Configuration dans FluentForms"]**

On passe a la configuration. Direction FluentForms, Settings, Payment Settings.

Premier onglet : General. Ici tu choisis ta devise — euros pour nous. Tu definis le format d'affichage du prix. Et tu actives les passerelles que tu veux utiliser.

Clique sur l'onglet Stripe. Tu as deux champs : la cle publique et la cle secrete. Il faut les recuperer dans ton dashboard Stripe.

Connecte-toi a stripe.com, va dans Developers, API Keys. Tu as deux modes : Test et Live. Commence toujours par le mode Test. Copie la cle publique (pk_test), colle-la dans FluentForms. Copie la cle secrete (sk_test), colle-la aussi.

Active le toggle "Enable Stripe". Sauvegarde.

C'est fait. Stripe est connecte en mode test.

**[SECTION 3 — slide "Free vs Pro pour les paiements"]**

Point important a connaitre.

En version gratuite, Stripe fonctionne. Mais FluentForms ajoute 1.9% de frais de transaction en plus des frais Stripe habituels. Sur un produit a 100 euros, ca fait 1.90 euro de plus a chaque vente.

En version Pro, ces frais supplementaires disparaissent. Tu ne paies que les frais Stripe standards — environ 1.4% + 0.25 euro en Europe.

Si tu fais quelques ventes par mois, la version gratuite suffit. Si tu vends regulierement, le passage en Pro se rembourse vite rien qu'avec l'economie sur les frais.

**[SECTION 4 — screencast "Mode Test"]**

Pour tester tes formulaires de paiement, utilise toujours le mode Test de Stripe d'abord.

Le numero de carte de test universel : 4242 4242 4242 4242. Date d'expiration : n'importe quelle date future. CVC : n'importe quels 3 chiffres.

Avec cette carte, tu peux soumettre des paiements de test sans qu'aucun argent ne circule. Tu recois les webhooks, tu vois les transactions dans le dashboard Stripe — tout est identique a la production, sauf que c'est fictif.

Quand tout fonctionne en test, remplace les cles test par les cles live. Et c'est en production.

**[SECTION 5 — slide "Quelle passerelle choisir"]**

En resume, voici ma recommandation.

Stripe en passerelle principale. C'est la plus complete, la plus fiable, la mieux integree avec FluentForms.

PayPal en option secondaire si tu vends a l'international ou si tes clients le demandent.

Mollie si tu as une audience forte en Benelux ou en Allemagne et que tu veux proposer des moyens de paiement locaux.

Razorpay uniquement si ton marche principal est l'Inde.

Tu peux activer plusieurs passerelles en meme temps. Le client choisira au moment du paiement.

**[OUTRO — face camera]**

Les passerelles sont configurees. Dans la prochaine lecon, on construit notre premier formulaire de paiement concret — un produit simple vendu directement via FluentForms, sans aucun plugin e-commerce.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- 4 passerelles : Stripe (recommande), PayPal, Razorpay, Mollie
- Config : FluentForms → Settings → Payment Settings → cles API
- Free : Stripe avec 1.9% de frais supplementaires
- Pro : Stripe sans frais supplementaires
- Toujours tester en mode Test avant de passer en Live
- Carte test : 4242 4242 4242 4242

**Mots cles SEO** : FluentForms paiement, FluentForms Stripe, passerelle paiement WordPress formulaire, FluentForms PayPal

---

**Notes de production** :
- Face camera : intro + outro
- Slides : 3 slides (passerelles, free vs pro, recommandation)
- Screencast : Payment Settings + dashboard Stripe (cles API + mode test)
- Ton : pratique, direct — pas de survente des passerelles
