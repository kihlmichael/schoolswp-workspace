# Script video - Module 6, Lecon 1 : Quiz builder avec scoring

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 6 - Quiz, surveys et analytics
**Lecon** : 1/6 - Quiz builder avec scoring
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast quiz builder, slide recapitulatif
**Objectif** : Creer un quiz avec scoring automatique, resultats et redirection conditionnelle

---

**[INTRO - face camera]**

Les quiz sont des aimants a engagement. Un quiz bien fait genere plus de soumissions qu'un formulaire classique - les gens adorent se tester. Et cote business, un quiz te donne des donnees de qualification que aucun formulaire classique ne peut capturer.

FluentForms Pro inclut un quiz builder natif. On va creer ensemble un quiz "Teste tes connaissances WordPress" avec scoring automatique.

**[SECTION 1 - screencast "Creer le quiz"]**

Cree un nouveau formulaire. "Quiz - Teste tes connaissances WordPress".

Dans les settings du formulaire, active le mode Quiz. FluentForms, Form Settings, Quiz Settings. Active "Enable Quiz Module". C'est la que tu configures le comportement global du quiz.

Options disponibles : afficher le score a la fin, afficher les bonnes reponses, randomiser l'ordre des questions, limiter le temps.

Pour notre quiz, on active l'affichage du score et des bonnes reponses. On desactive la limite de temps - c'est un quiz educatif, pas un examen.

**[SECTION 2 - screencast "Ajouter les questions"]**

On va creer 10 questions. Chaque question vaut 10 points. Score total : 100.

Question 1 - Choix unique. "Quel est le page builder par defaut de WordPress ?" Options : Elementor, Gutenberg (correct), Divi, Beaver Builder. Points : 10.

Question 2 - Choix unique. "Quel plugin SEO est recommande pour WordPress ?" Options : Yoast SEO, Rank Math (correct), All in One SEO, SEOPress. Points : 10.

Pour chaque question, tu selectionnes le type de champ. Radio Button pour le choix unique. Checkbox pour le choix multiple. Dropdown si tu preferes un menu deroulant.

Dans les settings du champ, tu coches la reponse correcte et tu attribues les points. FluentForms calcule le score automatiquement.

Question 3 - Vrai/Faux. "WordPress est un CMS open source." Vrai (correct) / Faux. Points : 10.

Continue avec 7 autres questions sur les themes, les plugins, la securite, les performances - adapte au niveau de ton audience.

**[SECTION 3 - screencast "Choix multiple avec scoring partiel"]**

Pour les questions a choix multiple, tu peux attribuer des points partiels.

Question 5 - Choix multiple. "Quels sont des plugins de cache WordPress ? (plusieurs reponses possibles)". Options : WP Rocket (correct), Contact Form 7, LiteSpeed Cache (correct), WP Super Cache (correct), Advanced Custom Fields. Points : 10 au total.

Configuration : chaque bonne reponse cochee donne des points. Chaque mauvaise reponse cochee en retire. Ou tu peux exiger toutes les bonnes reponses pour obtenir les points - a toi de choisir le mode.

**[SECTION 4 - screencast "Affichage des resultats"]**

Quand le participant soumet le quiz, FluentForms affiche les resultats.

Dans les Confirmation Settings, tu peux personnaliser le message selon le score.

Score 80-100 : "Bravo, tu maitrises WordPress. Tu es pret pour les sujets avances." Redirige vers ta formation avancee.

Score 50-79 : "Pas mal, tu as de bonnes bases. Quelques lacunes a combler." Redirige vers ton guide gratuit.

Score 0-49 : "Tu debutes, et c'est parfait. On va t'accompagner." Redirige vers ta formation debutant.

Configure ces messages avec les confirmations conditionnelles. IF score >= 80 THEN message A. IF score >= 50 AND score < 80 THEN message B. Sinon message C.

Chaque message peut inclure un CTA different. Le quiz qualifie le visiteur ET le dirige vers la ressource adaptee a son niveau.

**[SECTION 5 - screencast "Connecter le quiz a FluentCRM"]**

Le quiz devient un outil de segmentation quand tu le connectes a FluentCRM.

Cree des feeds conditionnels :
- Si score >= 80 → tag "level-advanced"
- Si score >= 50 et < 80 → tag "level-intermediate"
- Si score < 50 → tag "level-beginner"

Chaque participant recoit un tag selon son resultat. Tu peux ensuite envoyer des sequences email adaptees au niveau.

Les debutants recoivent des emails avec des bases WordPress. Les avances recoivent des contenus sur l'optimisation et la performance. Meme quiz, trois parcours differents.

**[SECTION 6 - slide "Pourquoi les quiz convertissent"]**

Quelques chiffres.

Un quiz genere en moyenne 2x plus de soumissions qu'un formulaire d'opt-in classique. Le taux de completion d'un quiz de 5-10 questions est de 70-85%. Et la perception de valeur est plus elevee - le participant recoit un resultat personnalise, pas juste un PDF.

Utilise les quiz comme lead magnet. "Teste tes connaissances WordPress" est plus attractif que "Telecharge notre guide WordPress". Le quiz engage, le guide informe. Les deux se completent.

**[OUTRO - face camera]**

Tu as un quiz fonctionnel avec scoring, resultats conditionnels et segmentation CRM. Dans la prochaine lecon, on explore une autre approche : les personality quiz - pas de bonne ou mauvaise reponse, mais un profil personnalise.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Quiz Module a activer dans les settings du formulaire (Pro)
- Types de questions : choix unique, choix multiple, vrai/faux
- Score automatique : points par question, total calcule
- Resultats conditionnels : message different selon le score
- Connexion FluentCRM : tags par niveau (beginner/intermediate/advanced)
- Quiz = lead magnet performant (2x plus de soumissions)
- Cas pratique : "Teste tes connaissances WordPress" - 10 questions, score /100

**Mots cles SEO** : FluentForms quiz, quiz WordPress, quiz scoring formulaire, FluentForms quiz builder

---

**Notes de production** :
- Face camera : intro (pitch engagement quiz) + outro (transition personality quiz)
- Screencast : creation complete du quiz avec 3-4 questions montrees (~7 min)
- Slides : 1 slide (pourquoi les quiz convertissent)
- Ton : dynamique - les quiz c'est fun, le ton doit le refleter
