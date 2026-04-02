# Script video — Module 6, Lecon 2 : Personality quiz

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 6 — Quiz, surveys et analytics
**Lecon** : 2/6 — Personality quiz
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast quiz builder mode personality, slide resultats
**Objectif** : Creer un quiz de personnalite avec profils et resultats personnalises

---

**[INTRO — face camera]**

Un quiz de personnalite, c'est different d'un quiz de connaissances. Il n'y a pas de bonne ou de mauvaise reponse. Chaque reponse oriente vers un profil — et chaque profil a un resultat different.

C'est un format viral. Les gens adorent decouvrir "quel type de X" ils sont. Et pour toi, c'est un outil de segmentation puissant.

**[SECTION 1 — slide "Le concept"]**

Le principe : chaque reponse attribue des points a une categorie. A la fin du quiz, la categorie avec le plus de points determine le profil du participant.

Notre cas pratique : "Quel type de site WordPress te correspond ?"

4 profils possibles :
- Blog / Createur de contenu
- E-commerce / Vendeur en ligne
- Formation / Formateur
- Portfolio / Freelance

Chaque question a 4 reponses, chacune associee a un profil.

**[SECTION 2 — screencast "Configurer le quiz"]**

Cree un nouveau formulaire. "Quiz — Quel site WordPress te correspond ?".

Active le Quiz Module dans les settings. Mais cette fois, au lieu du scoring classique, on va utiliser un systeme de categories.

La methode : chaque option de reponse donne des points dans une categorie specifique. On utilise les champs caches et le calcul pour tracker les scores par categorie.

Methode la plus simple dans FluentForms : cree 4 champs Hidden. Nomme-les "score-blog", "score-ecommerce", "score-formation", "score-portfolio". Valeur initiale : 0.

**[SECTION 3 — screencast "Les questions"]**

Question 1 : "Qu'est-ce qui te motive le plus en ligne ?" Options :
- "Partager mes idees et mon expertise" → +1 Blog
- "Vendre des produits" → +1 E-commerce
- "Transmettre un savoir" → +1 Formation
- "Montrer mon travail a des clients potentiels" → +1 Portfolio

Question 2 : "Comment veux-tu gagner de l'argent ?" Options :
- "Publicite et affiliation" → +1 Blog
- "Vente de produits physiques ou numeriques" → +1 E-commerce
- "Vente de cours en ligne" → +1 Formation
- "Prestation de services" → +1 Portfolio

Question 3 : "Quel outil t'attire le plus ?" Options :
- "Un editeur de contenu avec SEO" → +1 Blog
- "WooCommerce et des fiches produit" → +1 E-commerce
- "TutorLMS et des modules de cours" → +1 Formation
- "Des galeries et des temoignages clients" → +1 Portfolio

Continue avec 4 a 6 questions supplementaires. Plus il y a de questions, plus le resultat est precis. Mais au-dela de 10, le taux de completion chute.

Pour chaque question, utilise un champ Radio Button. Dans les settings avances, attribue la valeur numerique correspondante a chaque option.

**[SECTION 4 — screencast "Calculer le profil dominant"]**

A la fin du quiz, on compare les scores des 4 categories.

La methode la plus simple : utilise les confirmations conditionnelles.

Si score-blog >= score-ecommerce AND score-blog >= score-formation AND score-blog >= score-portfolio → affiche le resultat "Blog".

Repete pour chaque profil.

Chaque resultat a son propre message personnalise.

**[SECTION 5 — slide "Les 4 resultats"]**

Resultat Blog : "Tu es un createur de contenu ne. Un blog WordPress avec un bon SEO est ton terrain de jeu ideal. Commence par un theme oriente contenu et installe Rank Math."

Resultat E-commerce : "Tu es un vendeur en ligne. WooCommerce avec FluentCRM pour le suivi client est ta combinaison gagnante. Pense a CartFlows pour optimiser tes tunnels."

Resultat Formation : "Tu es un formateur. TutorLMS est fait pour toi. Cree ton premier cours et utilise FluentForms pour capturer tes futurs eleves."

Resultat Portfolio : "Tu es un freelance. Un site portfolio avec Kadence et des formulaires de prise de contact FluentForms va te generer des leads en continu."

Chaque resultat inclut un CTA adapte. Le blogueur recoit un lien vers ton guide SEO. Le vendeur vers ton guide WooCommerce. Le formateur vers ta formation TutorLMS. Le freelance vers ton guide freelance WordPress.

**[SECTION 6 — screencast "Segmentation FluentCRM"]**

Connecte les resultats a FluentCRM avec des feeds conditionnels.

Resultat Blog → tag "profile-blogger" + liste "leads-content"
Resultat E-commerce → tag "profile-ecommerce" + liste "leads-ecommerce"
Resultat Formation → tag "profile-formateur" + liste "leads-formation"
Resultat Portfolio → tag "profile-freelance" + liste "leads-portfolio"

Chaque profil entre dans une sequence email differente. Le blogueur recoit des contenus sur le SEO et le content marketing. Le vendeur recoit des contenus sur WooCommerce et la conversion. Personnalisation totale.

Le quiz ne collecte pas juste un email — il collecte un profil complet du visiteur.

**[OUTRO — face camera]**

Les personality quiz sont des machines a leads qualifies. Dans la prochaine lecon, on passe aux surveys et sondages — pour collecter des donnees structurees aupres de tes clients existants.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Personality quiz : pas de bonne reponse, chaque reponse oriente vers un profil
- 4 profils : Blog, E-commerce, Formation, Portfolio
- Scoring par categorie via champs caches ou calcul
- Confirmations conditionnelles pour afficher le bon resultat
- CTA adapte a chaque profil
- Segmentation FluentCRM : tag + liste par profil
- 5-10 questions max pour maintenir le taux de completion

**Mots cles SEO** : personality quiz WordPress, quiz personnalite FluentForms, quiz lead generation, quiz segmentation

---

**Notes de production** :
- Face camera : intro (format viral) + outro (transition surveys)
- Screencast : creation du quiz avec 3-4 questions et resultats (~5 min)
- Slides : 2 slides (concept + 4 resultats)
- Ton : fun et engage — le quiz doit donner envie d'etre pris
