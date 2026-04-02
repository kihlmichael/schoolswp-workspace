# Lecon 8.7 — Cas pratique : funnel formation freemium schoolsWP

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 8 — Ecosysteme et automatisation
- **Duree cible** : 12 min (~1500 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Construire le funnel freemium complet utilise par schoolsWP — de la landing page opt-in gratuite jusqu'a la vente de la Masterclass, en passant par FluentCRM et TutorLMS. Comprendre le modele freemium comme systeme d'acquisition.

---

## Script narration

**[INTRO — face camera]**

Dans cette lecon, on construit ensemble le modele exact que schoolsWP utilise pour toutes ses formations. C'est un modele freemium : le client decouvre gratuitement, puis achete le premium quand il est pret. Et chaque etape est automatisee.

Ce n'est pas une theorie — c'est le systeme en production. Tu vas voir comment chaque brique s'assemble : CartFlows pour le funnel, FluentCRM pour les emails, TutorLMS pour la formation, et OttoKit pour le liant.

---

**[SECTION 1 — Vue d'ensemble du modele freemium]**

**[ECRAN — schema complet du parcours freemium]**

Le modele freemium schoolsWP se decompose en deux funnels connectes par une sequence email.

Funnel 1 — Acquisition gratuite :
Landing page de presentation du cours gratuit → Opt-in (prenom + email) → Thank You avec acces immediat au cours gratuit TutorLMS.

Phase intermediaire — Nurturing email :
Sequence FluentCRM automatique : J+3, J+7, J+14. Chaque email apporte de la valeur et teaser la Masterclass payante.

Funnel 2 — Vente Masterclass :
Landing page de vente → Checkout + order bump → Upsell → Thank You avec acces au cours premium TutorLMS.

Le client entre gratuitement, consomme du contenu de qualite, recoit des emails qui construisent la confiance, puis decide d'acheter quand il est pret. Pas de pression. Pas de vente forcee. Un parcours progressif.

---

**[SECTION 2 — Funnel 1 : la landing page opt-in]**

**[ECRAN — editeur Gutenberg + Kadence Blocks, landing page]**

On commence par le funnel d'acquisition. Cree un nouveau flow dans CartFlows avec deux steps : une Landing Page et une Thank You.

La Landing Page est ta page d'opt-in. Tu la construis avec Gutenberg et Kadence Blocks. Voici la structure :

Hero section : titre accrocheur + sous-titre + formulaire. Exemple : "Apprends a creer ton premier funnel de vente WordPress — Formation gratuite en 5 lecons." Le formulaire : juste prenom et email. Pas de carte bancaire. Pas de compte a creer.

Section benefices : 3 a 4 bullet points sur ce que le client va apprendre. "Creer ta premiere landing page", "Configurer un checkout qui convertit", "Comprendre les metriques de ton funnel."

Section curriculum : les 5 lecons du cours gratuit listees avec une icone "gratuit" a cote de chacune. Le client voit exactement ce qu'il obtient.

Le formulaire d'opt-in est un bloc FluentCRM Forms (ou Fluent Forms) integre dans la page. A la soumission, le contact est cree dans FluentCRM avec le tag "lead-formation-gratuite".

---

**[SECTION 3 — Thank You + acces TutorLMS]**

**[ECRAN — Thank You page avec lien vers le cours]**

Apres l'opt-in, le client arrive sur la Thank You page. Ici, deux choses doivent se passer :

Premierement, le client recoit son acces. La Thank You page affiche un gros bouton : "Acceder a ta formation gratuite maintenant" avec le lien vers le cours TutorLMS. Si le client n'a pas encore de compte WordPress, TutorLMS peut creer un compte automatiquement lors de l'inscription (via le plugin ou OttoKit).

Deuxiemement, dans les coulisses, OttoKit execute un workflow : le contact est inscrit au cours gratuit TutorLMS, le tag "inscrit-cours-gratuit" est applique dans FluentCRM, et la sequence email de nurturing demarre.

Le client ne voit rien de tout ca. Il voit juste : "Merci, clique ici pour commencer." Simple et efficace.

---

**[SECTION 4 — La sequence email FluentCRM]**

**[ECRAN — FluentCRM > Sequence > 4 emails]**

La sequence email est le pont entre le gratuit et le payant. Elle se declenche automatiquement quand le tag "inscrit-cours-gratuit" est applique.

Email 1 — J+0 (immediat) : "Bienvenue dans la formation ! Voici ton lien d'acces." C'est l'email de confirmation. Inclus le lien vers le cours et un conseil pour bien demarrer.

Email 2 — J+3 : "As-tu termine la lecon 2 ? Voici un bonus." Tu apportes de la valeur supplementaire — un tip, une ressource, un template. Et en PS : "Tu veux aller plus loin ? Decouvre la Masterclass complete."

Email 3 — J+7 : "Ce que la plupart des debutants ratent." Contenu educatif qui pointe vers une limite de la formation gratuite — une limite que la Masterclass payante resout. C'est du teasing naturel, pas de la vente agressive.

Email 4 — J+14 : "La Masterclass est disponible." Email de vente direct avec lien vers le funnel 2 (landing page de la Masterclass). Prix, benefices, temoignages. Un CTA clair.

Chaque email est court — 200 a 400 mots maximum. Le but n'est pas de vendre dans l'email, mais de ramener le client sur la page de vente.

---

**[SECTION 5 — Funnel 2 : vente de la Masterclass]**

**[ECRAN — flow CartFlows Masterclass avec 4 steps]**

Le deuxieme funnel est un flow CartFlows classique a 4 etapes : Landing → Checkout → Upsell → Thank You.

La Landing Page de vente : c'est ta page de persuasion complete. Headline, sous-titre, video de presentation, curriculum de la Masterclass, temoignages clients, garantie 30 jours, et le prix. Construite avec Kadence Blocks — pas besoin d'Elementor.

Le Checkout : le produit WooCommerce "CartFlows Masterclass" a 97 euros. Order bump : "Pack de templates de funnels prets a l'emploi — 17 euros." Le bump est a paiement unique, complementaire a la formation.

L'Upsell : "Accede a toutes les formations schoolsWP — 247 euros au lieu de 397 euros." C'est le all-access pass. Un clic, pas de formulaire supplementaire.

La Thank You : confirmation de commande + bouton "Commencer la Masterclass" qui redirige vers le dashboard TutorLMS. OttoKit inscrit automatiquement au cours premium, applique le tag "client-masterclass" dans FluentCRM, et retire le tag "lead-formation-gratuite".

---

**[SECTION 6 — Les metriques a suivre]**

**[ECRAN — tableau de KPIs du funnel freemium]**

Voici les metriques cles de ce modele :

- Taux d'opt-in (landing → email capture) : objectif 25-40%
- Taux de completion du cours gratuit : objectif 30-50%
- Taux d'ouverture de la sequence email : objectif 40-60%
- Taux de conversion gratuit → payant : objectif 3-8%
- AOV avec bump et upsell : objectif +30-50% du prix de base

Avec 1000 visiteurs sur la landing page gratuite, tu peux esperer : 300 opt-ins, 100 qui completent le cours, 10 a 25 qui achetent la Masterclass. A 97 euros + 30% de bump/upsell, ca fait 1260 a 3150 euros de CA. Sans un centime de pub si le trafic est organique.

---

**[OUTRO — face camera]**

Ce modele freemium, c'est la colonne vertebrale de schoolsWP. Il fonctionne pour les formations WordPress, mais aussi pour tout business de contenu : coaching, consulting, services. Le gratuit attire, le nurturing construit la confiance, le funnel convertit.

Dans la prochaine lecon, on change de contexte : un funnel e-commerce pour un produit physique.

---

## Notes de production

- **Visuels** : schema complet du parcours freemium (2 funnels + sequence), structure landing page opt-in, timeline sequence email, tableau KPIs
- **Captures d'ecran** : landing page opt-in Kadence, Thank You avec bouton TutorLMS, sequence FluentCRM, checkout Masterclass avec bump
- **Ton** : concret et transparent (on montre le vrai modele schoolsWP), pedagogique
- **Duree estimee** : ~12 min a debit normal
- **Transition** : enchaine sur L8.8 (Cas pratique funnel e-commerce)
