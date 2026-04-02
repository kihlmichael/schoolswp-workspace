# Lecon 2.4 — Lead capture : formulaire opt-in integre

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 2 — Pages de vente et landing pages
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir creer un step Optin dans CartFlows pour capturer des emails avant le checkout, configurer le formulaire, connecter FluentCRM, et designer la page avec Gutenberg + Kadence Blocks.

---

## Script narration

**[INTRO — face camera]**

Tous les funnels ne commencent pas par un checkout. Parfois, tu veux d'abord capturer un email — avant de proposer quoi que ce soit a l'achat. C'est exactement ce que fait le step Optin dans CartFlows.

Dans cette lecon, tu vas apprendre a creer une page opt-in integree a ton funnel, a configurer le formulaire, a connecter tes contacts a FluentCRM, et a designer le tout avec Kadence Blocks. Et je te montre pourquoi l'opt-in est le seul funnel ou tu n'as pas besoin de produit WooCommerce.

---

**[SECTION 1 — Qu'est-ce qu'un step Optin dans CartFlows]**

**[ECRAN — schema funnel : Optin → Thank You / Checkout]**

Un step Optin, c'est une page avec un formulaire email que tu places avant le checkout — ou meme sans checkout du tout. L'objectif est simple : recuperer le prenom et l'email de ton visiteur.

Contrairement a un step Checkout qui necessite un produit WooCommerce, le step Optin fonctionne de maniere autonome. Tu n'as besoin d'aucun produit, d'aucun panier, d'aucune passerelle de paiement. C'est une page de capture pure.

CartFlows gere le step Optin comme n'importe quelle autre etape de ton flow. Le visiteur arrive sur la page, remplit le formulaire, clique sur le bouton, et il est redirige vers l'etape suivante — une page de remerciement, un checkout, ou une autre page de ton choix.

---

**[SECTION 2 — Quand utiliser un step Optin]**

**[ECRAN — slide "4 cas d'usage de l'opt-in"]**

Voici les quatre situations ou le step Optin est le bon choix.

**Lead magnets.** Tu proposes un guide PDF, une checklist, un template gratuit. Le visiteur donne son email en echange. C'est le cas d'usage classique, et le plus efficace pour construire ta liste.

**Inscriptions webinars ou lives.** Tu organises un evenement en ligne. La page opt-in sert de page d'inscription. Apres le formulaire, tu rediriges vers une page de confirmation avec la date et le lien d'acces.

**Listes d'attente.** Tu prepares un lancement — formation, plugin, service. Le step Optin te permet de collecter les emails des personnes interessees avant meme que le produit existe.

**Pre-lancement.** Tu veux tester l'interet pour une offre avant de la creer. La page opt-in avec un teaser suffit pour mesurer la demande reelle.

Le point commun : dans ces quatre cas, tu n'as pas de produit a vendre immediatement. Tu construis ta liste d'abord, tu monetises ensuite.

---

**[SECTION 3 — Creer un step Optin]**

**[ECRAN — CartFlows → Flows → ton flow → Add New Step]**

Pour ajouter un step Optin, va dans CartFlows, ouvre ton flow, et clique sur "Add New Step". Dans le menu de selection du type, choisis "Optin".

CartFlows te propose des templates Optin — tu peux en importer un ou partir d'une page vierge. Si tu pars d'un template, verifie qu'il est compatible Gutenberg.

Une fois le step cree, il apparait dans ton flow comme n'importe quelle autre etape. Tu peux le placer en premiere position — ce qui est le cas le plus courant — ou apres un autre step selon la logique de ton funnel.

Clique sur "Edit" pour ouvrir l'editeur de page. C'est la que tu vas construire ta page opt-in avec Gutenberg et Kadence Blocks.

---

**[SECTION 4 — Configurer le formulaire]**

**[ECRAN — editeur du step Optin, reglages CartFlows]**

Dans les reglages du step Optin — onglet "Optin" dans la sidebar CartFlows — tu configures le formulaire.

**Les champs.** Au minimum, tu as besoin de deux champs : prenom et email. CartFlows te permet d'ajouter d'autres champs, mais resiste a la tentation. Chaque champ supplementaire reduit ton taux de conversion. Deux champs, c'est le standard. Si tu vends en B2B et que tu as besoin du nom de l'entreprise, ajoute-le — sinon, reste a deux.

**Le bouton CTA.** Personnalise le texte du bouton. Oublie le generique "Envoyer" ou "Submit". Utilise une formulation orientee benefice : "Recevoir mon guide", "Reserver ma place", "Acceder a la checklist". Le bouton doit dire ce que le visiteur obtient, pas ce qu'il fait.

**La redirection.** Apres soumission, le visiteur est redirige vers l'etape suivante de ton flow. Si ton flow n'a pas d'etape apres l'opt-in, configure une page thank you. CartFlows gere cette redirection automatiquement — tu n'as rien a coder.

---

**[SECTION 5 — Ou vont les emails]**

**[ECRAN — CartFlows → Optin settings → integration email]**

C'est la question cle : quand quelqu'un remplit ton formulaire, ou atterrit son email ?

**FluentCRM — recommande.** Si tu utilises FluentCRM (et tu devrais), configure l'integration directement dans les reglages du step Optin. CartFlows peut envoyer le contact vers une liste FluentCRM specifique et declencher un tag ou une automation. C'est la solution la plus propre : tout reste dans WordPress, pas de service externe, pas de limite d'envoi liee a un plan SaaS.

**WooCommerce.** Par defaut, CartFlows cree un contact WooCommerce. C'est suffisant si tu veux juste stocker l'email, mais ca ne te donne aucun outil d'email marketing. Tu devras quand meme connecter un outil derriere.

**Mailchimp, ConvertKit, et autres.** CartFlows Pro supporte les integrations avec les services email externes. Si tu utilises deja Mailchimp ou ConvertKit, tu peux connecter le formulaire directement. Mais pour un setup WordPress complet, FluentCRM reste le choix le plus coherent — tu gardes le controle total sur tes donnees.

Mon conseil : connecte toujours ton formulaire opt-in a FluentCRM avec un tag specifique au lead magnet. Ca te permet de segmenter ta liste des le premier contact.

---

**[SECTION 6 — Designer la page avec Gutenberg + Kadence Blocks]**

**[ECRAN — editeur Gutenberg, construction de la page opt-in]**

Ta page opt-in doit etre simple et focalisee. Pas de menu de navigation, pas de sidebar, pas de footer avec 20 liens. Un seul objectif : le visiteur remplit le formulaire.

Voici la structure qui fonctionne, bloc par bloc avec Kadence.

**Hero section.** Bloc Kadence Row Layout en pleine largeur. Un titre H1 clair qui annonce le benefice ("Le guide complet pour choisir ton LMS WordPress"). Un sous-titre d'une ou deux lignes qui precise ce que le visiteur va recevoir. Une image ou un mockup du lead magnet a droite.

**Formulaire.** Place le formulaire CartFlows juste en dessous du hero, ou dans la colonne droite du hero si tu utilises un layout deux colonnes. Le formulaire doit etre visible sans scroller sur desktop.

**Preuve sociale.** En dessous du formulaire, ajoute un bloc Kadence Testimonials ou une ligne de texte simple : "Rejoint par 500+ createurs WordPress" ou des logos de sites. Si tu n'as pas encore de preuve sociale, ajoute une phrase de rassurance : "Gratuit, sans spam, desabonnement en un clic".

**Rien d'autre.** Pas de section "A propos", pas de blog, pas de liens sortants. La page opt-in est une impasse volontaire : le visiteur remplit le formulaire ou il part. C'est le principe.

Pour le template de page, utilise le template "Canvas" de Kadence — il supprime le header et le footer du theme, ce qui te donne une page completement autonome.

---

**[SECTION 7 — Connecter l'opt-in au reste du funnel]**

**[ECRAN — vue flow CartFlows avec les steps enchaines]**

Apres l'opt-in, que se passe-t-il ? Deux scenarios principaux.

**Scenario 1 : Opt-in → Thank You.** Le visiteur donne son email, il arrive sur une page de remerciement qui confirme l'envoi du lead magnet. C'est le flow le plus simple, ideal pour les guides et checklists. Tu peux ajouter un CTA secondaire sur la page thank you — vers un article, une offre, ou ton site.

**Scenario 2 : Opt-in → Checkout.** Le visiteur donne son email, puis il arrive sur une page de vente ou un checkout pour un produit payant. C'est le flow "tripwire" : tu offres quelque chose de gratuit, puis tu proposes immediatement une offre a petit prix. CartFlows gere cette transition nativement — les deux steps sont dans le meme flow.

Dans les deux cas, le lien entre les steps est automatique. Tu n'as pas a configurer de redirection manuelle. L'ordre des steps dans ton flow definit le parcours du visiteur.

---

**[OUTRO — face camera]**

L'opt-in est le seul funnel ou tu n'as pas besoin de produit WooCommerce. C'est la porte d'entree ideale pour construire ta liste, tester une idee, ou preparer un lancement. Deux champs, un CTA clair, une page sans distraction — c'est tout ce qu'il faut.

Connecte toujours ton formulaire a FluentCRM des le depart. Meme si tu n'as pas encore de sequence email, les contacts seront la quand tu seras pret.

Dans la prochaine lecon, on parle du checkout custom — comment personnaliser la page de paiement pour qu'elle convertisse mieux que le checkout WooCommerce par defaut.

---

## Notes de production

### Captures d'ecran suggerees

- Schema funnel Optin → Thank You / Checkout (section 1)
- Slide "4 cas d'usage" — icones lead magnet / webinar / liste d'attente / pre-lancement (section 2)
- CartFlows → Add New Step → selection type "Optin" (section 3)
- Reglages Optin : champs formulaire + bouton CTA (section 4)
- Reglages integration email : FluentCRM / WooCommerce / Mailchimp (section 5)
- Editeur Gutenberg : construction page opt-in avec hero + formulaire + preuve sociale (section 6)
- Vue flow CartFlows : enchainement Optin → Thank You et Optin → Checkout (section 7)

### Transitions

- Intro : face camera, fond neutre schoolsWP
- Sections 1, 2 : slides explicatives
- Sections 3, 4, 5 : screencast CartFlows
- Section 6 : screencast Gutenberg + Kadence
- Section 7 : screencast CartFlows flow builder
- Outro : face camera, CTA vers lecon suivante

### Duree estimee par section

| Section | Duree |
| --- | --- |
| Intro | 0:30 |
| Section 1 — Step Optin | 0:50 |
| Section 2 — Cas d'usage | 1:00 |
| Section 3 — Creer le step | 0:50 |
| Section 4 — Configurer le formulaire | 1:15 |
| Section 5 — Ou vont les emails | 1:15 |
| Section 6 — Designer la page | 1:30 |
| Section 7 — Connecter au funnel | 0:50 |
| Outro | 0:20 |
| **Total** | **~8:20** |
