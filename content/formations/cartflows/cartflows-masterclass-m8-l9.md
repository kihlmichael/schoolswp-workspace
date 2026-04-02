# Lecon 8.9 — Cas pratique : funnel service/prestation freelance

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 8 — Ecosysteme et automatisation
- **Duree cible** : 10 min (~1300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Construire un funnel CartFlows adapte a un freelance vendant des prestations de service. Gerer les specificites : pas de produit physique, paiement par acompte, onboarding client, et upsell de maintenance.

---

## Script narration

**[INTRO — face camera]**

Un freelance qui vend des services — audit SEO, creation de site, consulting, design — a les memes besoins qu'un e-commercant : une page qui convertit, un checkout qui rassure, et un post-achat qui professionnalise la relation.

Mais les specificites sont differentes. Tu ne livres pas un produit physique. Tu ne vends pas forcement un prix fixe. Et l'etape apres l'achat n'est pas une livraison — c'est un onboarding. Voyons comment adapter CartFlows a ce contexte.

---

**[SECTION 1 — Le produit : une prestation de service]**

**[ECRAN — exemple de prestation : audit SEO]**

Prenons un exemple concret : tu es freelance SEO et tu vends un audit SEO complet a 497 euros. Le client arrive sur ta page, il comprend ce qu'il va obtenir (un rapport detaille + recommandations + appel de restitution), et il paie.

Dans WooCommerce, tu crees un produit "Simple" (pas une subscription) a 497 euros. C'est un produit virtuel — pas de livraison. Tu coches "Virtuel" dans les options du produit pour desactiver les champs d'adresse au checkout.

Alternative : si tu preferes encaisser un acompte plutot que le montant total, cree un produit "Acompte Audit SEO" a 197 euros (40% du total). Le solde sera facture apres la prestation, en dehors du funnel (par facture classique ou via un deuxieme lien de paiement).

---

**[SECTION 2 — La landing page du freelance]**

**[ECRAN — landing page prestation audit SEO]**

La landing page d'un freelance a une structure differente d'une page produit classique. Tu ne vends pas un objet — tu vends ton expertise et le resultat que le client va obtenir.

Structure recommandee :

Section 1 — Le probleme. "Ton site ne genere pas de trafic organique ? Tu publies du contenu mais personne ne le trouve ?" Tu identifies la douleur du client.

Section 2 — La solution. "Mon audit SEO complet analyse 47 points cles de ton site et te livre un plan d'action prioritise." Tu presentes ta prestation comme la solution.

Section 3 — Ce qui est inclus. Liste detaillee : audit technique, analyse de contenu, etude de mots-cles, rapport PDF de 30 pages, appel de restitution 1h. Le client sait exactement ce qu'il achete.

Section 4 — Preuves sociales. Temoignages de clients precedents, logos d'entreprises, resultats chiffres ("Augmentation de 180% du trafic organique en 6 mois pour le client X").

Section 5 — Prix et CTA. "Audit SEO complet — 497 euros. Resultats livres sous 10 jours ouvrables." Bouton : "Reserver mon audit."

---

**[SECTION 3 — Le checkout adapte aux services]**

**[ECRAN — checkout CartFlows simplifie pour service]**

Le checkout pour un service est plus simple que pour un produit physique. Pas d'adresse de livraison, pas de choix de transporteur. Tu veux juste le nom, l'email, et les informations de paiement.

Dans CartFlows, active le layout deux colonnes. A gauche : le formulaire (nom, email, telephone). A droite : le recapitulatif de la prestation avec les details.

Ajoute un champ personnalise si necessaire : "URL de ton site web" — pour que tu puisses commencer l'audit des la commande recue. CartFlows permet d'ajouter des champs custom au checkout.

Et le bump. Le bump parfait pour un freelance qui vend un audit : "Ajoute un rapport PDF detaille de tes concurrents (3 concurrents analyses) — 47 euros." C'est un complement logique. Le client achete un audit de son site — l'analyse concurrentielle est la suite naturelle.

Autre option de bump : "Ajoute un appel supplementaire de suivi a 30 jours — 37 euros." Le client recoit l'audit, met en oeuvre les recommandations, et dans 30 jours tu fais un point sur les progres.

---

**[SECTION 4 — Upsell : pack maintenance ou consulting long terme]**

**[ECRAN — page upsell pack maintenance]**

Apres le paiement de l'audit, le upsell s'affiche. Et pour un freelance, le upsell le plus naturel c'est la continuite de la relation.

"Tu viens de reserver ton audit SEO. Pour une mise en oeuvre accompagnee, decouvre le pack maintenance 3 mois — 297 euros/mois." Le pack comprend : implementation des recommandations de l'audit, suivi mensuel des positions, optimisation continue, un appel mensuel de 30 minutes.

C'est un one-click upsell. Le client n'a pas a ressaisir ses informations. Un bouton : "Oui, je veux etre accompagne." Un lien : "Non merci, l'audit seul me suffit."

Taux d'acceptation estime : 5 a 10%. Sur un upsell a 297 euros/mois x 3 mois = 891 euros, meme 5% d'acceptation augmente significativement ton revenu moyen.

Si le client refuse, pas de downsell agressif. Un simple : "OK. Si tu changes d'avis, tu pourras souscrire au pack maintenance depuis ton espace client."

---

**[SECTION 5 — Thank You et onboarding]**

**[ECRAN — Thank You page avec questionnaire integre]**

C'est la que le funnel freelance se distingue le plus. La Thank You page n'est pas juste une confirmation — c'est le debut de l'onboarding.

Apres le paiement, le client voit : "Merci pour ta confiance ! Pour preparer au mieux ton audit, remplis ce questionnaire." Et tu integres un lien vers un formulaire — Fluent Forms, Typeform, ou Google Forms.

Le questionnaire d'onboarding demande :
- L'URL du site a auditer
- Les objectifs principaux (plus de trafic, plus de conversions, meilleur positionnement)
- Les mots-cles cibles
- L'acces Google Search Console et Analytics (optionnel mais recommande)
- La date souhaitee pour l'appel de restitution

Ce questionnaire fait deux choses : il professionnalise immediatement la relation (le client se dit "cette personne est organisee"), et il te donne les informations pour commencer a travailler sans email d'aller-retour.

Dans les coulisses, OttoKit peut automatiser : creer une tache dans ton outil de gestion de projet, envoyer une notification Slack "Nouvel audit commande par [nom]", et appliquer le tag "client-audit-seo" dans FluentCRM.

---

**[SECTION 6 — Specificites freelance a retenir]**

**[ECRAN — checklist specificites freelance]**

Quelques points cles pour adapter CartFlows au contexte freelance :

Pas de produit physique : coche "Virtuel" dans WooCommerce pour supprimer les champs de livraison.

Paiement par acompte : si tu ne veux pas encaisser la totalite, cree un produit "Acompte" au montant souhaite. Mentionne clairement dans la description : "Acompte de 40% — le solde de 300 euros sera facture a la livraison."

L'onboarding est ton produit : pour un freelance, la premiere impression apres l'achat est critique. Un questionnaire bien construit, un email de bienvenue professionnel, et un calendrier de booking pour l'appel — ca transforme un simple achat en debut de relation de confiance.

Upsell = continuite : le meilleur upsell pour un freelance n'est pas un produit supplementaire — c'est la version longue de la relation. Audit → accompagnement. Site one-shot → maintenance. Consulting ponctuel → retainer mensuel.

---

**[OUTRO — face camera]**

Le funnel freelance avec CartFlows, c'est ta vitrine de vente + ton systeme d'onboarding en un seul parcours. Le client decouvre, achete, et commence a travailler avec toi — le tout automatise.

Dans la derniere lecon de ce module, on compare CartFlows et FunnelKit pour t'aider a faire le bon choix.

---

## Notes de production

- **Visuels** : landing page prestation SEO, checkout simplifie sans livraison, page upsell maintenance, Thank You avec questionnaire
- **Captures d'ecran** : produit WooCommerce virtuel, champ custom URL au checkout, bump rapport concurrentiel, formulaire onboarding
- **Ton** : pratique et adapte au freelance, focus sur la professionnalisation
- **Duree estimee** : ~10 min a debit normal
- **Transition** : enchaine sur L8.10 (CartFlows vs FunnelKit)
