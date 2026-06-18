---
title: SureCart - Quiz Module 7 : Après la vente
version: 1.0
last_updated: 2026-06-05
---

# Quiz - Module 7 : Après la vente

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin de Module 7, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 8).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

À quoi sert la page **Dashboard** créée automatiquement par SureCart, et comment ton client y accède-t-il facilement depuis ta navigation ?

- [ ] Elle sert uniquement à afficher les téléchargements ; le client y accède via un lien dans les emails de commande
- [x] C'est l'espace self-service du client (commandes, abonnements, téléchargements, moyens de paiement) ; pour le rendre accessible depuis la navigation, tu l'ajoutes au menu via Apparence, Menus
- [ ] Elle remplace la page de remerciement après l'achat ; le client y est redirigé automatiquement sans rien configurer
- [ ] C'est une page d'administration réservée au propriétaire de la boutique

**Explication** : SureCart crée automatiquement une page Dashboard avec trois blocs : abonnements, commandes, téléchargements. Le client peut s'y gérer seul (coordonnées, mot de passe, factures) sans t'écrire. Pour qu'il la trouve facilement, tu l'ajoutes à ton menu dans Apparence, Menus. Trois chemins d'accès existent aussi : le bouton sur la page de remerciement, le bouton dans l'email de commande, et la définition du mot de passe au premier accès.

---

## Question 2

**Type** : Choix unique (Single Choice)

Tu veux personnaliser l'objet et le corps de l'email de confirmation de commande envoyé à tes acheteurs. Quelle est la bonne séquence ?

- [ ] SureCart, Settings, Notifications, modifier le texte directement dans WordPress, enregistrer
- [ ] app.surecart.com, Email, Customer Emails, modifier le sujet et le corps, utiliser les variables Liquid, Preview, enregistrer
- [x] SureCart, Settings, Notifications, cliquer sur Edit à côté de l'email, être redirigé vers la plateforme (Email, Customer Emails), modifier sujet et corps, utiliser Preview et Send Test, enregistrer
- [ ] Réglages WordPress, Email, chercher SureCart dans la liste des modèles, modifier

**Explication** : Les emails clients se gèrent en deux temps. Dans WordPress, SureCart, Settings, Notifications, tu actives ou désactives chaque email. Pour en modifier le contenu, tu cliques sur Edit : cela t'emmène sur la plateforme SureCart (app.surecart.com), dans Email, Customer Emails. Là tu modifies le sujet et le corps avec les variables Liquid, tu fais un Preview pour voir le rendu, tu t'envoies un test, et tu enregistres. Le bouton Revert to Default te permet de revenir au modèle d'origine si besoin.

---

## Question 3

**Type** : Vrai / Faux (True/False)

SureCart est headless : les données clients vivent dans le cloud SureCart, pas dans ta base WordPress. Cela signifie qu'une intégration comme l'inscription automatique à un cours fonctionne sans que le client soit un utilisateur WordPress.

- [ ] Vrai
- [x] Faux

**Explication** : Parce que SureCart est headless, les données clients vivent dans le cloud - c'est ce qui garde ton site léger. Mais les intégrations (donner accès à un cours, alimenter un CRM) nécessitent que le client existe comme utilisateur WordPress avec un rôle. À l'achat, cet utilisateur est créé automatiquement. Si tu as importé des clients depuis un autre outil, tu dois les synchroniser manuellement via Settings, Advanced, Syncing, Sync Customers.

---

## Question 4

**Type** : Choix unique (Single Choice)

Pour commencer à mesurer tes ventes dans Google Analytics sans manipulation technique compliquée, quelle est la voie recommandée dans ce module ?

- [ ] Google Tag Manager avec un déclencheur sur l'événement d'achat SureCart et une balise GA4
- [ ] Copier-coller manuellement le code de suivi GA4 dans le fichier functions.php de ton thème
- [x] Installer l'extension officielle Google Site Kit : elle suit automatiquement l'ajout au panier et l'achat, et affiche tes statistiques dans l'administration WordPress
- [ ] Utiliser les webhooks SureCart pour envoyer chaque événement vers Google Analytics en temps réel

**Explication** : La voie simple pour la grande majorité des créateurs est Google Site Kit, l'extension officielle. Elle s'installe comme n'importe quel plugin, suit automatiquement les événements clés (ajout au panier, achat) et affiche tes stats GA dans ton admin WordPress, sans manipulation technique. Google Tag Manager est la voie avancée, utile si tu fais de la publicité ou si tu veux suivre des événements plus fins (vue produit, début de checkout) - mais c'est à ajouter seulement quand tu en as vraiment besoin.

---

## Question 5

**Type** : Choix multiple (Multiple Choice)

Dans les réglages d'affiliation de SureCart, tu dois choisir un **type d'attribution**. Quelles affirmations sont correctes ? (plusieurs bonnes réponses)

- [x] L'attribution détermine quel affilié touche la commission quand un visiteur a cliqué sur plusieurs liens d'affiliés différents avant d'acheter
- [ ] L'attribution premier clic et dernier clic donnent toujours le même résultat si l'acheteur n'a cliqué que sur un seul lien
- [x] La durée du cookie (ex. 30 jours) définit combien de temps après le clic d'un affilié une vente lui est encore attribuée
- [x] Les paiements aux affiliés ne sont pas automatiques : SureCart prépare la liste dans Payouts, mais tu règles tes affiliés toi-même en dehors de la plateforme
- [ ] Les achats effectués en mode test de SureCart sont comptabilisés dans les statistiques d'affiliation pour permettre de valider l'installation

**Explication** : L'attribution (premier ou dernier clic) s'applique quand un acheteur a cliqué sur plusieurs liens d'affiliés différents - l'affirmation sur "même résultat avec un seul lien" est donc vraie mais hors sujet comme réponse à cocher. La durée du cookie (30 jours est un standard courant) définit la fenêtre d'attribution après le clic. Les paiements sont manuels : c'est une limite honnête à connaître avant de s'engager envers des affiliés. Et les achats en mode test ne sont pas comptabilisés - uniquement les vraies ventes.

---
