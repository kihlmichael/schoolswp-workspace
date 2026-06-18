# Script video - Module 5, Lecon 3 : Listes et tags automatiques

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 5 - FluentForms + FluentCRM
**Lecon** : 3/7 - Listes et tags automatiques
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast FluentCRM + FluentForms, slides strategie
**Objectif** : Organiser listes et tags pour une segmentation propre et automatique

---

**[INTRO - face camera]**

Tu sais connecter FluentForms a FluentCRM. Maintenant, la question importante : comment organiser tes listes et tes tags pour ne pas te retrouver avec un bazar inutilisable dans six mois ?

On va mettre en place une convention de nommage claire et configurer chaque formulaire pour qu'il assigne automatiquement la bonne segmentation.

**[SECTION 1 - slide "Listes vs Tags - la difference"]**

Rappel rapide.

Une liste, c'est un conteneur large. Tu y mets des contacts qui ont un point commun global. Exemples : "Newsletter", "Clients", "Prospects", "Leads gratuits".

Un tag, c'est une etiquette precise. Tu le colles sur un contact pour qualifier un comportement, un interet ou une source specifique. Exemples : "interest-seo", "source-lead-magnet", "bought-formation-lms".

Un contact est dans une ou deux listes maximum. Mais il peut avoir des dizaines de tags.

Les listes servent a la gestion globale. Les tags servent a la segmentation fine et au ciblage.

**[SECTION 2 - slide "Convention de nommage"]**

Voici la convention que j'utilise sur schoolsWP et que je te recommande.

Pour les listes, utilise un format simple et descriptif :
- newsletter
- leads-seo
- leads-formation
- clients
- prospects-atelier

Pour les tags, utilise un prefixe qui indique la categorie :
- source-formulaire-contact
- source-lead-magnet-checklist
- source-webinar-seo
- interest-seo
- interest-lms
- interest-crm
- action-download-guide
- action-inscription-atelier
- status-prospect
- status-client
- bought-formation-lms
- bought-ebook-seo

Le prefixe te permet de filtrer rapidement. Dans FluentCRM, tu peux trier les tags par nom - les prefixes regroupent les tags par categorie.

**[SECTION 3 - screencast "Creer les listes dans FluentCRM"]**

Direction FluentCRM, Contacts, Lists. Cree les listes de base :
- newsletter - tous les abonnes newsletter
- leads-seo - contacts interesses par le SEO
- leads-formation - contacts interesses par les formations
- clients - contacts qui ont achete

Chaque liste a un titre et une description optionnelle. La description t'aide a te rappeler l'usage dans 6 mois.

**[SECTION 4 - screencast "Creer les tags dans FluentCRM"]**

FluentCRM, Contacts, Tags. Cree les tags de base :
- source-formulaire-contact
- source-newsletter
- source-lead-magnet-checklist-seo
- interest-seo
- interest-lms
- interest-automatisation

Tu n'as pas besoin de tout creer maintenant. Cree les tags au fur et a mesure que tu ajoutes des formulaires. Mais respecte toujours la convention de nommage.

**[SECTION 5 - screencast "Configurer chaque formulaire"]**

Maintenant, la regle d'or : chaque formulaire a sa propre combinaison liste + tags.

Formulaire de contact : liste "prospects" + tag "source-formulaire-contact".

Formulaire newsletter : liste "newsletter" + tag "source-newsletter".

Formulaire "Guide SEO gratuit" : liste "leads-seo" + tag "source-lead-magnet-checklist-seo" + tag "interest-seo".

Formulaire inscription atelier : liste "prospects-atelier" + tag "source-inscription-atelier" + tag "interest-formation".

Ouvre chaque formulaire, va dans Settings, Marketing & CRM, FluentCRM Feed, et configure la bonne combinaison.

En 30 secondes par formulaire, tu as une segmentation propre. Et chaque nouveau contact qui arrive est immediatement qualifie.

**[SECTION 6 - screencast "Verifier la segmentation"]**

Apres quelques semaines, va dans FluentCRM et regarde tes contacts.

Filtre par liste : combien de contacts dans "leads-seo" ? Combien dans "newsletter" ?

Filtre par tag : combien ont le tag "interest-lms" ? Combien ont "source-lead-magnet-checklist-seo" ?

Tu peux combiner les filtres. Montre-moi tous les contacts qui sont dans la liste "leads-seo" ET qui ont le tag "source-lead-magnet-checklist-seo" ET qui n'ont PAS le tag "status-client". Ce sont tes prospects SEO les plus qualifies qui n'ont pas encore achete.

C'est la puissance de la segmentation. Un formulaire collecte. Le CRM organise. Et toi, tu cibles.

**[SECTION 7 - slide "Cas pratique complet"]**

Cas pratique : formulaire "Guide SEO gratuit".

Le visiteur arrive sur ta page, voit le formulaire d'opt-in. Prenom + email. Il soumet.

FluentForms enregistre la soumission. Le feed FluentCRM s'execute :
- Contact cree dans FluentCRM
- Liste : "leads-seo"
- Tags : "source-lead-magnet-checklist-seo", "interest-seo"

Le contact est maintenant segmente. Tu sais d'ou il vient (lead magnet), ce qui l'interesse (SEO), et ou il en est (lead, pas encore client).

Et ca, c'est la base pour la prochaine etape - les tags dynamiques qui changent selon les reponses du formulaire. On voit ca dans la lecon suivante.

**[OUTRO - face camera]**

Tes listes et tags sont organises. Chaque formulaire alimente FluentCRM avec une segmentation propre. Dans la prochaine lecon, on va encore plus loin : les tags dynamiques - le tag change selon ce que le visiteur a repondu dans le formulaire.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Listes : conteneurs larges (newsletter, leads-seo, clients)
- Tags : etiquettes precises avec prefixes (source-, interest-, action-, status-, bought-)
- Convention de nommage : kebab-case avec prefixe categorisant
- Chaque formulaire = combinaison unique liste + tags
- Verifier la segmentation avec les filtres FluentCRM
- Cas pratique : "Guide SEO gratuit" → liste leads-seo + tags source + interest

**Mots cles SEO** : FluentCRM listes tags, segmentation CRM WordPress, organiser contacts FluentCRM, FluentForms segmentation automatique

---

**Notes de production** :
- Face camera : intro (le risque du bazar) + outro (transition tags dynamiques)
- Screencast : creation listes/tags + config formulaires (~6 min)
- Slides : 3 slides (listes vs tags, convention nommage, cas pratique)
- Ton : structure, methodique - poser les bases proprement
