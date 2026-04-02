# Script video — Module 4, Lecon 4 : Tarification conditionnelle

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 — Paiements
**Lecon** : 4/7 — Tarification conditionnelle
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast builder avec conditions de prix, slide recapitulatif
**Objectif** : Creer un formulaire ou le prix s'ajuste en temps reel selon les options selectionnees

---

**[INTRO — face camera]**

Jusqu'ici, on a vu des prix fixes. Un produit, un prix. Mais dans la realite, beaucoup de prestations ont un prix variable. Un site vitrine ne coute pas le meme prix qu'un site e-commerce. Un coaching individuel ne coute pas le meme prix qu'un coaching de groupe.

FluentForms Pro permet de faire varier le prix en temps reel selon les choix du visiteur. C'est exactement ce qu'on va construire.

**[SECTION 1 — screencast "Le cas pratique"]**

On va creer un formulaire de devis pour une prestation freelance en creation de site WordPress.

Trois offres :
- Site vitrine : 500 euros
- Site e-commerce : 1200 euros
- Site e-commerce + SEO : 1800 euros

Et des options supplementaires :
- Redaction de contenu : +300 euros
- Formation WordPress (2h) : +200 euros
- Maintenance 12 mois : +50 euros par mois (600 euros)

Le prix total s'affiche en temps reel pendant que le client coche ses options.

**[SECTION 2 — screencast "Construire les champs"]**

Cree un nouveau formulaire. "Devis Creation Site WordPress".

Ajoute Name et Email. Puis un champ Radio Button pour le type de site. Label : "Type de site". Options :
- Site vitrine — 500 euros
- Site e-commerce — 1200 euros
- Site e-commerce + SEO — 1800 euros

Maintenant, au lieu d'un Radio classique, utilise un champ Payment Item de type "Multiple Choice". C'est la ou la magie opere. Chaque option a un prix associe.

Configure les trois options avec leurs prix respectifs. Le champ sait que c'est un montant, pas juste du texte.

**[SECTION 3 — screencast "Ajouter les options supplementaires"]**

Pour les options, ajoute un champ Checkbox Payment Item. Type : "Checkbox Selection". Chaque case cochee ajoute son montant au total.

Options :
- Redaction de contenu : 300.00
- Formation WordPress 2h : 200.00
- Maintenance 12 mois : 600.00

Le client peut cocher zero, une, ou toutes les options. Le total se met a jour en temps reel.

**[SECTION 4 — screencast "Le calcul dynamique"]**

Ajoute un champ Payment Summary en dessous. Ce champ affiche automatiquement :
- L'option principale selectionnee et son prix
- Les options supplementaires cochees et leurs prix
- Le total

Le client voit exactement ce qu'il va payer. Pas de surprise.

Si tu veux aller plus loin, tu peux ajouter un champ Numeric avec une formule de calcul. Par exemple, afficher le prix HT et le prix TTC (HT x 1.20). Mais pour la plupart des cas, le Payment Summary suffit.

**[SECTION 5 — screencast "Logique conditionnelle avancee"]**

On peut aller encore plus loin avec la logique conditionnelle.

Exemple : si le client choisit "Site e-commerce + SEO", tu affiches un champ supplementaire "Nombre de pages a optimiser" avec un select : 5 pages (inclus), 10 pages (+400 euros), 20 pages (+800 euros).

Configure la condition : Show this field IF "Type de site" IS "Site e-commerce + SEO".

Le champ apparait uniquement quand l'option correspondante est selectionnee. Et son prix s'ajoute au total.

C'est comme ca que tu construis des formulaires de devis complexes qui restent simples pour le client. Il ne voit que les options pertinentes pour son choix.

**[SECTION 6 — screencast "Finaliser et tester"]**

Ajoute le champ Stripe Card Element et le bouton de soumission.

Pour le label du bouton, utilise quelque chose de dynamique si possible, ou un texte generique comme "Valider et payer". Le Payment Summary juste au-dessus rappelle le total.

Teste le formulaire. Selectionne "Site e-commerce" — 1200 euros. Coche "Redaction de contenu" — le total passe a 1500 euros. Coche "Formation" — 1700 euros. Le prix bouge en temps reel devant tes yeux.

C'est cette reactivite qui donne confiance au client. Il controle son budget.

**[SECTION 7 — slide "Cas d'utilisation"]**

La tarification conditionnelle fonctionne pour beaucoup de situations.

Prestataire de services : devis en ligne avec options. Restaurant : commande a emporter avec supplements. Evenementiel : inscription avec choix de formule (standard, VIP, premium). Formation : choix entre presentiel et distanciel avec tarifs differents.

A chaque fois, le meme principe : des champs de paiement avec des prix, des conditions qui les affichent ou les masquent, et un total qui se calcule en temps reel.

**[OUTRO — face camera]**

Tu as un formulaire de devis interactif ou le prix s'adapte aux choix du client. C'est un outil de vente puissant. Dans la prochaine lecon, on voit comment limiter les quantites disponibles — gestion d'inventaire directement dans FluentForms.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Payment Item type "Multiple Choice" : chaque option a un prix
- Checkbox Payment Item : options additionnelles qui s'ajoutent au total
- Payment Summary : recapitulatif en temps reel
- Logique conditionnelle : afficher des options selon les choix precedents
- Le prix total se met a jour dynamiquement
- Cas pratique : devis creation site (500/1200/1800 euros + options)

**Mots cles SEO** : FluentForms tarification conditionnelle, formulaire devis WordPress, prix dynamique formulaire, FluentForms payment conditions

---

**Notes de production** :
- Face camera : intro (probleme prix variable) + outro (transition inventaire)
- Screencast : construction complete du formulaire devis (~7 min)
- Slide : 1 slide cas d'utilisation
- Ton : pas a pas, montrer la reactivite du prix en temps reel — c'est le wow moment
