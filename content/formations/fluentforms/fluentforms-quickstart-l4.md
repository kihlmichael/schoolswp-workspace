# Script video - Lecon 4 : Creer un formulaire de capture d'email

**Formation** : FluentForms Quick Start
**Code** : FRM-011
**Lecon** : 4/5 - Creer un formulaire de capture d'email
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera pour intro/conclusion, screencast complet de la creation et du placement
**Objectif** : Creer un formulaire de capture email minimaliste, connecter a FluentCRM, placer strategiquement

---

**[INTRO - face camera]**

Le formulaire de contact, c'est fait. Maintenant on passe au formulaire qui genere des resultats : la capture d'email.

Un formulaire de contact attend que le visiteur ait une question. Un formulaire de capture d'email va chercher le visiteur - il lui propose quelque chose en echange de son adresse. C'est le formulaire qui construit ta liste.

**[SECTION 1 - Creer le formulaire]**

**[ECRAN - screencast FluentForms → Nouveau formulaire → Formulaire vierge]**

Cette fois, on part de zero. Clique sur Nouveau formulaire, puis Formulaire vierge. Donne-lui un nom : "Capture email - Newsletter".

On va ajouter deux champs. Pas trois, pas cinq. Deux.

Moins de champs, c'est plus d'inscriptions. Chaque champ supplementaire reduit ton taux de conversion. Pour une capture d'email, prenom et email - c'est tout ce dont tu as besoin.

**[ECRAN - screencast ajout des champs]**

Premier champ : glisse un champ "Name" depuis la liste. Clique dessus. Dans les options, selectionne "First Name Only" - on veut juste le prenom, pas le nom de famille. Le label : "Ton prenom". Coche "Obligatoire".

Pourquoi le prenom ? Parce qu'il te permet de personnaliser tes emails. "Salut {prenom}" convertit mieux que "Salut". C'est un champ qui pese presque rien en friction mais qui ajoute de la valeur a tes sequences email.

Deuxieme champ : glisse un champ "Email". Label : "Ton email". Coche "Obligatoire". FluentForms valide automatiquement le format.

Dernier element : le bouton d'envoi. Clique dessus pour changer le texte. Remplace "Submit" par quelque chose de concret : "Je m'inscris", "Recevoir les conseils", ou "Acces gratuit". Evite les textes generiques - le bouton doit dire ce que la personne obtient.

Ton formulaire fait deux champs et un bouton. C'est minimaliste, et c'est exactement ce qu'il faut.

**[SECTION 2 - Connecter a FluentCRM]**

**[ECRAN - screencast de l'integration FluentCRM]**

Si tu as FluentCRM installe sur ton site, cette etape est puissante. Tu vas connecter ton formulaire directement a ton CRM - chaque inscription cree automatiquement un contact avec les bons tags et la bonne liste.

Va dans l'onglet Reglages de ton formulaire, puis dans la section Marketing & CRM Integrations. Clique sur "Ajouter une nouvelle integration" et selectionne FluentCRM.

Configure le mapping. Le champ "Prenom" de ton formulaire correspond au champ "First Name" de FluentCRM. Le champ "Email" correspond a "Email". C'est automatique, verifie juste que c'est correct.

Ensuite, les options importantes.

Listes : selectionne la liste dans laquelle tu veux ajouter les nouveaux contacts. Par exemple "Newsletter" ou "Prospects". Si tu n'as pas encore de liste, cree-la dans FluentCRM avant.

Tags : ajoute un tag pour identifier la source. Par exemple "source:formulaire-newsletter" ou "source:quickstart". Ca te permet de segmenter tes contacts plus tard.

Statut : choisis "Subscribed" si tu veux que les contacts recoivent tes emails immediatement, ou "Pending" si tu veux un double opt-in. Pour la France et l'Europe, le double opt-in est recommande pour la conformite RGPD.

Double opt-in : si tu actives cette option, FluentCRM envoie un email de confirmation. Le contact doit cliquer sur le lien pour valider son inscription. C'est une etape supplementaire, mais ca garantit des adresses valides et un consentement clair.

**[ECRAN - slide "Sans FluentCRM"]**

Si tu n'as pas FluentCRM, pas de probleme. Toutes les soumissions sont enregistrees dans le dashboard FluentForms. Tu peux les exporter en CSV a tout moment. Tu peux aussi connecter FluentForms a Mailchimp, ConvertKit, ou MailerLite via les integrations natives.

Mais si tu construis ton ecosysteme sur WordPress, FluentCRM est le choix logique. Meme equipe, integration native, zero cout supplementaire en version gratuite. Je te le recommande.

**[SECTION 3 - Design inline vs vertical]**

**[ECRAN - screencast du builder → mise en page]**

Par defaut, FluentForms empile les champs verticalement - un champ par ligne. C'est bien pour un formulaire de contact avec plusieurs champs.

Pour un formulaire de capture d'email avec deux champs, le layout inline - horizontal - est souvent plus efficace. Les champs s'alignent sur une seule ligne : prenom, email, bouton. Ca prend moins de place et ca ressemble a un formulaire d'inscription, pas a un formulaire de contact.

Pour passer en inline, selectionne les deux champs et le bouton, et configure-les en colonnes. Dans FluentForms, tu peux utiliser le champ "Container" avec trois colonnes : une pour le prenom, une pour l'email, une pour le bouton.

Alternative : garde le layout vertical si tu integres le formulaire dans un widget sidebar ou un footer etroit. L'inline fonctionne mieux sur les pages larges.

**[SECTION 4 - Ou placer le formulaire]**

**[ECRAN - screencast de l'insertion dans differents emplacements]**

Un formulaire de capture d'email, ca ne se met pas seulement sur une page dediee. Voici les quatre meilleurs emplacements.

Premier emplacement : la sidebar. Si tu as un blog, place le formulaire dans un widget sidebar. Chaque visiteur qui lit un article le voit. Utilise un bloc "Shortcode" ou le widget FluentForms.

Deuxieme emplacement : le footer. En bas de chaque page, avant les mentions legales. C'est un emplacement classique qui capte les visiteurs qui scrollent jusqu'en bas - ils sont engages. Avec Kadence, tu peux ajouter le bloc FluentForms directement dans la section footer de ton theme.

Troisieme emplacement : une page dediee. Une landing page avec un titre accrocheur, un paragraphe qui explique ce que le visiteur recoit, et le formulaire. C'est la page que tu lies dans tes emails, tes reseaux sociaux, et tes call-to-action.

Quatrieme emplacement : en fin d'article. Apres la conclusion de chaque article de blog, ajoute le formulaire. Le visiteur vient de lire ton contenu, il est convaincu de ta valeur - c'est le moment de lui proposer d'aller plus loin.

Tu n'es pas oblige de choisir un seul emplacement. Place le meme formulaire a plusieurs endroits. FluentForms gere ca nativement avec le shortcode ou le bloc Gutenberg - tu reutilises le meme formulaire partout.

**[OUTRO - face camera]**

Ton formulaire de capture d'email est pret et connecte a FluentCRM. Place-le sur ton site - au minimum en sidebar et en fin d'article. Chaque formulaire bien place, c'est un contact de plus dans ta liste.

Derniere lecon : on personnalise le design des deux formulaires et on fait le point sur ce que tu peux faire ensuite.

---

**Points cles** :
- Formulaire minimaliste : prenom + email + bouton personnalise
- Moins de champs = plus d'inscriptions
- FluentCRM : mapping, listes, tags, double opt-in (recommande RGPD)
- Sans FluentCRM : export CSV ou integration Mailchimp/ConvertKit/MailerLite
- Layout inline (horizontal) pour les pages larges, vertical pour sidebar/footer
- 4 emplacements : sidebar, footer, page dediee, fin d'article

**Mots cles SEO** : capture email WordPress, formulaire inscription newsletter WordPress, FluentForms FluentCRM integration, formulaire lead capture WordPress

---

**Notes de production** :
- Face camera : intro (20 sec) + outro (15 sec)
- Screencast principal : creation (2 min), FluentCRM (2 min 30), design inline (1 min), placements (2 min)
- Slide : 1 slide (sans FluentCRM)
- Montrer le rendu final inline et vertical cote a cote
- Si FluentCRM n'est pas installe sur le site de demo, montrer l'ecran d'integration avec une capture annotee
