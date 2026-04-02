# Script video — Module 6, Lecon 3 : Surveys et sondages

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 6 — Quiz, surveys et analytics
**Lecon** : 3/6 — Surveys et sondages
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast builder sondage, slide types de champs
**Objectif** : Creer des sondages de collecte de donnees avec les bons types de champs

---

**[INTRO — face camera]**

Les sondages sont l'outil le plus sous-estime de FluentForms. Un quiz divertit. Un formulaire de contact collecte. Mais un sondage t'apporte de l'intelligence — il te dit ce que tes clients pensent, veulent, et attendent.

On va construire un sondage de satisfaction post-achat avec les bons champs pour obtenir des donnees exploitables.

**[SECTION 1 — slide "Champs utiles pour les sondages"]**

FluentForms propose plusieurs types de champs specifiquement adaptes aux sondages.

Net Promoter Score (NPS). La question classique : "Sur une echelle de 0 a 10, recommanderais-tu notre service a un ami ?" Un seul champ, une metrique universelle. 0-6 : detracteurs. 7-8 : passifs. 9-10 : promoteurs.

Rating. Des etoiles ou des smileys. "Comment evalues-tu la qualite du support ?" De 1 a 5 etoiles.

Likert Scale. Une matrice avec des affirmations et des niveaux d'accord. "Le contenu etait pertinent" → Pas du tout d'accord / Pas d'accord / Neutre / D'accord / Tout a fait d'accord. Ideal pour evaluer plusieurs criteres d'un coup.

Textarea. Reponse libre. "Qu'est-ce qu'on pourrait ameliorer ?" Les reponses ouvertes donnent les insights les plus riches — mais elles sont plus difficiles a analyser a grande echelle.

Slider. Une echelle visuelle. "A quel point es-tu satisfait ?" Le curseur va de 0 a 100. Plus intuitif qu'un champ numerique.

**[SECTION 2 — screencast "Construire le sondage"]**

Cree un nouveau formulaire. "Sondage Satisfaction Post-Achat".

Structure en 4 sections.

Section 1 — Identification (optionnel). Email du client. Tu peux pre-remplir ce champ si tu envoies le sondage via FluentCRM avec un lien personnalise.

Section 2 — Satisfaction globale. Champ NPS : "Sur une echelle de 0 a 10, recommanderais-tu schoolsWP a un ami ?". Champ Rating : "Comment evalues-tu ton experience globale ?" — 5 etoiles.

Section 3 — Details. Likert Scale avec 4 affirmations :
- "Le contenu de la formation etait clair"
- "Le support a repondu rapidement"
- "Le rapport qualite-prix est bon"
- "Je me sens plus competent apres la formation"

Echelle : Pas du tout d'accord / Pas d'accord / Neutre / D'accord / Tout a fait d'accord.

Section 4 — Reponses ouvertes. Textarea : "Qu'est-ce qui t'a le plus plu ?". Textarea : "Qu'est-ce qu'on pourrait ameliorer ?". Textarea : "Un commentaire supplementaire ?" (optionnel).

**[SECTION 3 — screencast "Anonymiser les reponses"]**

Certains sondages fonctionnent mieux en anonyme. Le client est plus honnete s'il sait que sa reponse n'est pas liee a son nom.

Pour anonymiser : retire le champ Email ou rends-le optionnel. Dans les settings de notification, n'inclus pas d'identifiants dans le recap.

Mais attention : si tu anonymises, tu perds la capacite de relier les reponses aux contacts FluentCRM. C'est un compromis. Pour un sondage de satisfaction, je recommande de garder l'email — la valeur du feedback lie a un client identifie est superieure au gain marginal d'anonymat.

Si tu veux quand meme proposer l'option, ajoute une checkbox : "Rester anonyme". Et configure une condition : si cochee, le champ Email est masque.

**[SECTION 4 — screencast "Exporter les resultats"]**

Les reponses s'accumulent dans FluentForms, Entries. Tu peux les consulter une par une.

Pour une analyse globale, exporte en CSV. FluentForms, Entries, Export. Choisis le formulaire, la periode, et exporte.

Le fichier CSV s'ouvre dans Excel ou Google Sheets. Tu peux calculer les moyennes, les medianes, les distributions. Le NPS moyen, le nombre de promoteurs vs detracteurs, les tendances sur les Likert.

Pour un reporting plus visuel, importe le CSV dans un outil comme Google Data Studio ou meme un simple tableau croise dynamique dans Google Sheets.

**[SECTION 5 — screencast "Envoyer le sondage via FluentCRM"]**

Le sondage ne sert a rien si personne ne le remplit. L'envoi par email via FluentCRM est la methode la plus efficace.

Cree un email dans FluentCRM. Objet : "Ton avis compte — 2 minutes pour nous aider". Corps : message court expliquant pourquoi tu demandes un retour + lien vers le formulaire de sondage.

Envoie-le a la liste "clients" ou aux contacts avec le tag "bought-formation-X".

Timing : envoie le sondage 7 a 14 jours apres l'achat. Pas le lendemain — le client n'a pas encore eu le temps d'utiliser le produit. Pas 3 mois apres — il a oublie.

Taux de reponse attendu : 10-25% sur une base de clients existants. Si tu es en dessous de 10%, ameliore l'objet de l'email ou ajoute une incitation (coupon de reduction pour le prochain achat).

**[OUTRO — face camera]**

Tu as un sondage structure qui collecte des donnees exploitables. Dans la prochaine lecon, on regarde le Reports Dashboard de FluentForms Pro — un tableau de bord analytique qui te montre la performance de tous tes formulaires.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Champs sondage : NPS, Rating, Likert Scale, Textarea, Slider
- Structure : identification → satisfaction globale → details → reponses ouvertes
- Export CSV pour analyse dans Google Sheets
- Envoi via FluentCRM : 7-14 jours post-achat, taux reponse 10-25%
- Anonymisation optionnelle (compromis donnees vs honnetete)
- Cas pratique : sondage satisfaction post-achat

**Mots cles SEO** : sondage FluentForms, survey WordPress, NPS formulaire WordPress, sondage satisfaction WordPress

---

**Notes de production** :
- Face camera : intro (valeur des sondages) + outro (transition reports)
- Screencast : construction sondage + export CSV (~5 min)
- Slides : 1 slide (types de champs sondage)
- Ton : methodique — structure claire pour des donnees exploitables
