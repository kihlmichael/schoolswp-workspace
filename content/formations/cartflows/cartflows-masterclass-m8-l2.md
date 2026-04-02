# Lecon 8.2 — CartFlows + OttoKit : automatiser les actions post-achat

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 8 — Ecosysteme et automatisation
- **Duree cible** : 10 min (~1300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Utiliser OttoKit pour automatiser des actions post-achat au-dela de l'email. Configurer des workflows qui connectent CartFlows a TutorLMS, FluentCRM, Slack et d'autres services.

---

## Script narration

**[INTRO — face camera]**

Dans la lecon precedente, on a connecte CartFlows a FluentCRM pour gerer les emails et la segmentation. Mais l'email n'est qu'une partie de l'equation. Quand un client achete, tu veux peut-etre aussi l'inscrire a un cours, prevenir ton equipe, mettre a jour un tableur, ou envoyer un webhook vers un outil externe.

C'est exactement ce que fait OttoKit. Et vu que CartFlows et OttoKit sont developpes par le meme editeur — Brainstorm Force — l'integration est native et profonde.

---

**[SECTION 1 — OttoKit : automatisation WordPress cloud]**

**[ECRAN — dashboard OttoKit]**

OttoKit, anciennement SureTriggers, c'est une plateforme d'automatisation cloud qui se connecte directement a ton WordPress. Tu installes le plugin OttoKit, tu relies ton site a ton compte OttoKit, et tu crees des workflows visuels avec des declencheurs et des actions.

La difference avec n8n ou Make, c'est que OttoKit comprend nativement les plugins WordPress. Il ne passe pas par une API generique — il parle directement a WooCommerce, FluentCRM, TutorLMS, et bien sur CartFlows. Les champs, les produits, les tags : tout est disponible dans l'interface sans configuration manuelle.

Le plan gratuit offre deja 5 workflows actifs. Pour un site e-commerce avec CartFlows, c'est suffisant pour demarrer.

---

**[SECTION 2 — Le trigger : commande WooCommerce completee]**

**[ECRAN — OttoKit > Nouveau workflow > choix du trigger]**

On commence par creer un nouveau workflow dans OttoKit. Le declencheur principal pour CartFlows, c'est "WooCommerce — Order Completed". A chaque commande validee dans ton funnel, ce trigger se declenche.

Tu peux filtrer par produit. Si tu veux que le workflow ne s'active que pour un produit specifique — par exemple ta formation premium — tu ajoutes un filtre : "Product Name contains Formation Premium". Comme ca, les achats d'autres produits ne declenchent pas ce workflow.

Le trigger capture toutes les donnees de la commande : email du client, nom, montant, produits achetes, coupon utilise. Ces donnees sont disponibles comme variables dans toutes les actions suivantes.

---

**[SECTION 3 — Les actions post-achat essentielles]**

**[ECRAN — OttoKit > editeur de workflow avec actions chainées]**

Voici les actions que tu vas chainer apres le trigger. Je te montre les plus courantes pour un funnel CartFlows.

Action 1 — Inscrire a un cours TutorLMS. Choisis l'action "TutorLMS — Enroll User in Course". Selectionne le cours dans le menu deroulant. L'email de la commande est utilise pour identifier l'utilisateur. Si le compte WordPress n'existe pas encore, OttoKit peut le creer automatiquement.

Action 2 — Appliquer un tag FluentCRM. Action "FluentCRM — Add Tag to Contact". Tu selectionnes le tag. Si le contact n'existe pas dans FluentCRM, il est cree. Cette action est complementaire a l'integration directe FluentCRM/WooCommerce — ici tu peux ajouter des tags plus specifiques selon le workflow.

Action 3 — Envoyer un email personnalise. Pas via FluentCRM cette fois, mais directement via OttoKit. Utile pour un email transactionnel immediat qui ne fait pas partie d'une sequence : "Bienvenue, voici ton acces."

Action 4 — Notifier sur Slack ou par webhook. Action "Slack — Send Message" vers un canal #ventes. Le message : "Nouvelle vente : [nom] a achete [produit] pour [montant] euros." Ton equipe est informee en temps reel.

Action 5 — Creer une tache. Si tu utilises un outil de gestion de projet connecte a OttoKit, tu peux creer automatiquement une tache "Preparer l'onboarding pour [nom]."

---

**[SECTION 4 — Workflow complet : achat formation]**

**[ECRAN — workflow OttoKit complet avec 5 actions]**

Assemblons le tout dans un workflow complet. Voici ce qui se passe quand quelqu'un achete ta formation via un funnel CartFlows :

Trigger : WooCommerce Order Completed (produit = Formation CartFlows Premium).

Etape 1 : TutorLMS — inscrire au cours "CartFlows Masterclass". Etape 2 : FluentCRM — appliquer le tag "client-masterclass-cartflows". Etape 3 : OttoKit Email — envoyer "Bienvenue, voici ton acces au cours" avec le lien direct vers TutorLMS. Etape 4 : Slack — notification dans #ventes avec le nom et le montant. Etape 5 : Delai 1 heure, puis FluentCRM — demarrer la sequence "Onboarding Masterclass".

Cinq actions automatiques, zero intervention manuelle. Le client achete, il recoit son acces, ton CRM est a jour, ton equipe est prevenue, et l'onboarding demarre.

---

**[SECTION 5 — Integration native CartFlows et OttoKit]**

**[ECRAN — OttoKit triggers specifiques CartFlows]**

Comme CartFlows et OttoKit viennent du meme editeur, Brainstorm Force, tu as acces a des triggers specifiques CartFlows dans OttoKit. Pas seulement "commande WooCommerce" — mais aussi "CartFlows — Offer Accepted" pour les upsells, "CartFlows — Bump Accepted" pour les order bumps.

Ca te permet de creer des workflows differents selon le comportement dans le funnel :
- Le client accepte l'upsell → workflow specifique avec tag "client-vip" + notification prioritaire
- Le client refuse l'upsell → workflow alternatif avec tag "a-relancer" + sequence email de relance
- Le client prend le bump → tag "interesse-par-bonus" pour le cibler sur les prochaines offres

Cette granularite n'est pas possible avec une simple integration WooCommerce. C'est la valeur ajoutee de l'ecosysteme Brainstorm Force.

---

**[SECTION 6 — Bonnes pratiques et limites]**

**[ECRAN — checklist bonnes pratiques]**

Quelques conseils avant de multiplier les workflows :

Commence simple. Un workflow par produit principal. Ne cree pas 20 workflows des le premier jour — tu vas te perdre dans les declencheurs et les doublons.

Teste chaque workflow avec une commande test. Passe une commande toi-meme et verifie que chaque action s'execute correctement. Regarde les logs dans OttoKit pour confirmer.

Attention aux doublons avec FluentCRM. Si tu as deja configure l'integration directe WooCommerce/FluentCRM pour les tags, ne duplique pas les memes tags dans OttoKit. Choisis un seul chemin pour chaque action.

Le plan gratuit a des limites. 5 workflows, executions limitees. Si tu as beaucoup de produits et de scenarios, tu auras besoin du plan Pro. Mais pour un funnel simple avec 2-3 produits, le gratuit suffit.

---

**[OUTRO — face camera]**

OttoKit transforme chaque vente CartFlows en une chaine d'actions automatiques. Email, inscription cours, notification, tagging — tout se fait sans que tu leves le petit doigt.

Dans la prochaine lecon, on se concentre sur la connexion CartFlows + TutorLMS pour vendre des formations via funnel — et on verra comment structurer le parcours de A a Z.

---

## Notes de production

- **Visuels** : dashboard OttoKit, editeur de workflow visuel, schema workflow complet 5 actions
- **Captures d'ecran** : OttoKit trigger WooCommerce, actions TutorLMS/FluentCRM/Slack, logs d'execution
- **Ton** : technique et pratique, focus sur le workflow concret
- **Duree estimee** : ~10 min a debit normal
- **Transition** : enchaine sur L8.3 (CartFlows + TutorLMS)
