# Lecon 5.5 - Site avec CRM : ZipWP + FluentCRM

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 5 - Sites business avec ZipWP
- **Lecon** : 5/8
- **Duree cible** : 10 min
- **Objectif pedagogique** : Installer FluentCRM sur un site ZipWP, configurer la capture d'emails, creer une sequence de bienvenue automatique, et segmenter les contacts par source.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Un site sans capture d'email, c'est un robinet ouvert. Les visiteurs passent, regardent, et ne reviennent jamais. Tu perds 95% de ton trafic - des gens qui etaient interesses mais qui n'ont aucune raison de revenir.

FluentCRM resout ce probleme. C'est un CRM complet, installe directement dans WordPress, qui capture les emails, segmente tes contacts, et envoie des sequences automatiques. Et sur un site ZipWP, l'integration est native. On installe et on configure tout aujourd'hui.

---

[SECTION 1 - Installer FluentCRM]

FluentCRM s'installe comme n'importe quel plugin WordPress. Extensions → Ajouter → "FluentCRM" → Installer → Activer.

L'assistant de bienvenue te guide. Configure les bases : le nom de l'expediteur (ton nom ou celui de ton entreprise), l'email d'expedition (utilise une adresse sur ton propre domaine - contact@tonsite.fr - jamais un Gmail), et le logo qui apparaitra dans tes emails.

FluentCRM utilise le systeme d'envoi de WordPress par defaut. Pour un envoi fiable, connecte un service SMTP - FluentSMTP (du meme editeur, gratuit) ou un service comme Amazon SES, SendGrid, ou Mailgun. Sans SMTP, tes emails risquent d'atterrir dans les spams.

La version gratuite de FluentCRM permet la gestion de contacts, les tags, les listes, et les emails manuels. La version Pro ajoute les sequences automatiques, les segments dynamiques, les rapports avances, et les integrations e-commerce.

---

[SECTION 2 - Formulaire d'inscription email]

Tu as deux options pour capturer des emails sur ton site ZipWP.

Option 1 - SureForms : tu crees un formulaire minimaliste avec deux champs - prenom et email. Ajoute-le en bas de tes articles, sur ta page d'accueil, ou dans la sidebar. Dans SureForms, configure l'action apres soumission : "Ajouter a FluentCRM" avec un tag specifique (par exemple "inscription-site").

Option 2 - le widget FluentCRM : FluentCRM Pro inclut un formulaire d'inscription natif. Va dans FluentCRM → Forms → Create Form. Choisis un modele, personnalise les champs et le design. Tu obtiens un shortcode a inserer ou tu veux dans ton site.

Les deux options fonctionnent. SureForms est plus flexible visuellement (tu as acces a tous les blocs Spectra pour le design). Le widget FluentCRM est plus rapide a configurer et gere automatiquement le double opt-in.

L'emplacement ideal : un formulaire dans le hero de la page d'accueil avec un lead magnet ("Telecharge le guide gratuit"), un formulaire en bas de chaque article de blog, et un formulaire sur la page Contact.

---

[SECTION 3 - Sequence de bienvenue automatique]

Quand quelqu'un s'inscrit, il ne faut pas le laisser dans le silence. Une sequence de bienvenue, c'est 3 a 5 emails envoyes automatiquement dans les jours qui suivent l'inscription.

Cree une sequence : FluentCRM → Email Sequences → Create New. Nomme-la "Bienvenue".

Email 1 - Jour 0 (immediat) : "Bienvenue ! Voici ton guide." Tu livres le lead magnet promis. Tu te presentes en 3 phrases. Tu dis ce que la personne va recevoir dans les prochains jours.

Email 2 - Jour 2 : "Mon histoire" ou "Pourquoi j'ai cree [ton business]". Tu construis la relation. Tu partages ton parcours et tes valeurs. Pas de vente.

Email 3 - Jour 4 : "La plus grosse erreur que je vois." Tu apportes de la valeur concrete. Un conseil actionnable lie a ta thematique. Tu commences a positionner ton expertise.

Email 4 - Jour 7 : "Voici comment je peux t'aider." Tu presentes tes offres - formation, service, produit. C'est le premier email de vente. Il arrive apres que tu as deja apporte de la valeur.

Email 5 - Jour 10 : "Une question pour toi." Tu demandes du feedback. "Quel est ton plus gros defi en [thematique] ?" Ca engage la conversation et te donne des insights precieux.

Configure le declencheur : dans FluentCRM → Automations → Create. Declencheur : "Contact added to list" ou "Tag applied". Action : "Start Email Sequence" → selectionne ta sequence de bienvenue.

---

[SECTION 4 - Tags et segmentation par source]

Les tags, c'est ce qui transforme une liste d'emails en un CRM intelligent.

Le principe : chaque contact recoit des tags qui decrivent d'ou il vient, ce qu'il a fait, et ce qui l'interesse. Tu peux ensuite envoyer des emails cibles a chaque segment.

Tags par source d'acquisition : "inscription-site" pour ceux qui s'inscrivent via le formulaire du site. "inscription-blog" pour ceux qui viennent d'un article. "inscription-landing" pour ceux qui viennent d'une landing page specifique.

Pour tagger automatiquement, configure-le dans SureForms ou dans l'automation FluentCRM. Chaque formulaire applique un tag different - comme ca tu sais toujours d'ou vient le contact.

---

[SECTION 5 - Connecter avec WooCommerce ou SureCart]

FluentCRM s'integre nativement avec WooCommerce et SureCart. Quand un visiteur achete, FluentCRM le tague automatiquement.

Avec WooCommerce : va dans FluentCRM → Settings → Integrations → WooCommerce. Active l'integration. Tu peux configurer des regles : "Quand un client achete le produit X, applique le tag Y." Par exemple : achat de la formation → tag "client-formation" + retrait du tag "prospect".

Avec SureCart : meme logique. Active l'integration SureCart dans FluentCRM. Configure les tags automatiques par produit.

Ca te permet de differencier tes emails. Un prospect recoit des emails de nurturing et de vente. Un client recoit des emails de suivi, de formation, et d'upsell. Tu ne parles pas de la meme facon a quelqu'un qui n'a pas encore achete et a quelqu'un qui est deja client.

Le conseil schoolsWP : un site sans capture d'email, c'est un robinet ouvert - les visiteurs passent et ne reviennent jamais. FluentCRM ferme ce robinet.

---

[OUTRO]

FluentCRM est installe sur ton site ZipWP. Les formulaires capturent les emails. La sequence de bienvenue se declenche automatiquement. Les tags segmentent tes contacts par source et par comportement.

Tu as maintenant un site qui ne se contente pas de recevoir du trafic - il le convertit en relation durable.

Dans la prochaine lecon, on ajoute la derniere brique : l'automatisation avec OttoKit. Des workflows qui connectent formulaires, achats et emails sans intervention manuelle.

---

## Notes de production

### Captures d'ecran suggerees

1. **FluentCRM Dashboard** - Vue d'ensemble avec contacts et tags
2. **Formulaire SureForms** - Formulaire email minimaliste integre dans une page Spectra
3. **Sequence emails** - Editeur de sequence avec les 5 emails programmes
4. **Automation builder** - Declencheur "inscription" → action "sequence bienvenue"
5. **Tags WooCommerce** - Integration FluentCRM × WooCommerce avec tags automatiques

### Transitions

- Intro → Section 1 : installation FluentCRM depuis le dashboard WP
- Section 1 → Section 2 : creation du formulaire d'inscription
- Section 2 → Section 3 : editeur de sequence email
- Section 3 → Section 4 : gestion des tags et segments
- Section 4 → Section 5 : integration e-commerce
- Section 5 → Outro : vue du CRM avec contacts segmentes

### Notes HeyGen / ElevenLabs

- Ton persuasif sur l'intro - faire ressentir l'urgence de capturer les emails
- Section 3 (sequence) : rythme pose, detailler chaque email avec son objectif
- Section 4 (tags) : ton technique mais accessible, bien expliquer la logique de segmentation
- Insister sur la metaphore du "robinet ouvert" - c'est le message cle
