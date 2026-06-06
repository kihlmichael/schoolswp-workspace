# Lecon 5.6 - Site avec automatisation : ZipWP + OttoKit

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 5 - Sites business avec ZipWP
- **Lecon** : 6/8
- **Duree cible** : 10 min
- **Objectif pedagogique** : Configurer OttoKit (ex-SureTriggers) pour automatiser les actions cles d'un site ZipWP - formulaires, achats, inscriptions - sans ecrire une ligne de code.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Ton site ZipWP est en place. Tu as des formulaires, tu vends des produits, tu captures des emails. Maintenant, imagine que chaque action sur ton site declenche automatiquement la bonne reaction - un formulaire soumis envoie une notification Slack ET un email de confirmation. Un achat ajoute un tag FluentCRM ET inscrit l'acheteur a un cours TutorLMS. Tout ca sans que tu leves le petit doigt.

C'est exactement ce que fait OttoKit. Anciennement connu sous le nom de SureTriggers, OttoKit est l'outil d'automatisation cloud de Brainstorm Force. Et puisqu'il fait partie du meme ecosysteme que ZipWP, Astra, et Spectra, l'integration est native.

---

[SECTION 1 - OttoKit : ce que c'est et comment ca marche]

OttoKit fonctionne sur un principe de "trigger → action". Quelque chose se passe sur ton site (le trigger), et OttoKit execute une ou plusieurs actions en reponse.

La difference avec d'autres outils d'automatisation comme Zapier ou Make : OttoKit est integre directement a l'ecosysteme WordPress de Brainstorm Force. Il connait nativement SureForms, SureCart, Astra, Spectra, TutorLMS, FluentCRM. Pas besoin de cle API complexe ou de connecteur tiers - tout se connecte en quelques clics.

OttoKit est un service cloud. Ca veut dire que les automatisations tournent sur les serveurs d'OttoKit, pas sur ton WordPress. Ton site reste leger et rapide, meme avec 20 automatisations actives.

Installe le connecteur : Extensions → Ajouter → "OttoKit" → Installer → Activer. Connecte ton site a ton compte OttoKit (cree un compte sur ottokit.com si ce n'est pas deja fait). Une fois connecte, OttoKit detecte automatiquement les plugins installes sur ton site - SureForms, WooCommerce, FluentCRM, TutorLMS.

---

[SECTION 2 - Les triggers disponibles]

Voici les triggers les plus utiles pour un site ZipWP.

Nouveau formulaire soumis (SureForms) : quelqu'un remplit un formulaire sur ton site - contact, inscription, demande de devis. OttoKit detecte la soumission et declenche les actions.

Nouvel achat (WooCommerce ou SureCart) : un client achete un produit. OttoKit sait quel produit, quel montant, et qui est l'acheteur.

Nouvel inscrit (TutorLMS) : un apprenant s'inscrit a un cours. OttoKit capture l'evenement.

Nouveau contact (FluentCRM) : un email est ajoute a FluentCRM, avec ses tags et ses listes.

Page visitee (WordPress) : un visiteur accede a une page specifique - utile pour declencher des actions basees sur le comportement de navigation.

Nouvel utilisateur WordPress : quelqu'un cree un compte sur ton site.

Chaque trigger donne acces aux donnees de l'evenement - nom, email, produit achete, cours inscrit. Ces donnees sont utilisables dans les actions qui suivent.

---

[SECTION 3 - Les actions disponibles]

Cote actions, OttoKit peut :

Envoyer un email : un email personnalise avec les donnees du trigger. Pas un email FluentCRM - un email ponctuel envoye par OttoKit (utile pour les notifications rapides).

Ajouter un tag FluentCRM : tagger automatiquement un contact dans FluentCRM en fonction de ce qu'il a fait.

Creer une tache : ajouter une tache dans ton outil de gestion de projet (Trello, Asana, Notion).

Notifier Slack : envoyer un message dans un canal Slack - ideal pour etre prevenu en temps reel d'un achat ou d'une inscription.

Webhook : envoyer les donnees vers n'importe quel service externe via HTTP. C'est le connecteur universel - si un service a une API, OttoKit peut communiquer avec.

Inscrire a un cours TutorLMS : ajouter automatiquement un utilisateur a un cours specifique.

Ajouter a une liste FluentCRM : inscrire le contact dans une liste de diffusion specifique.

---

[SECTION 4 - Cas concrets]

Passons a la pratique avec deux automatisations que tu peux configurer en 10 minutes.

Cas 1 - Formulaire contact → Notification Slack + email auto-reponse. Trigger : "New form submission" (SureForms, formulaire de contact). Action 1 : envoyer un message Slack dans le canal #demandes - "Nouvelle demande de [nom] : [message]". Action 2 : envoyer un email au visiteur - "Merci pour ta demande. Je reviens vers toi sous 24h."

Configure ca dans OttoKit : cree un nouveau workflow, selectionne le trigger SureForms, choisis ton formulaire, ajoute les deux actions en sequence. Teste avec un formulaire reel - soumets une demande test et verifie que le Slack et l'email partent.

Cas 2 - Nouvel achat → Tag FluentCRM + inscription cours TutorLMS. Trigger : "New order completed" (WooCommerce). Condition : le produit achete est la "Formation Photo". Action 1 : ajouter le tag "client-formation-photo" dans FluentCRM. Action 2 : inscrire l'utilisateur au cours "Formation Photo" dans TutorLMS. Action 3 : envoyer un email de bienvenue avec les instructions d'acces.

Ce deuxieme cas est puissant : l'achat declenche automatiquement l'acces au cours et le suivi CRM. Zero intervention manuelle. Le client paye, il recoit ses acces, et tu es notifie. Tout est automatique.

---

[SECTION 5 - Bonnes pratiques]

Quelques regles pour que tes automatisations restent fiables.

Teste toujours avant de publier. Chaque workflow OttoKit a un mode test - utilise-le. Un email qui part vers le mauvais destinataire, ca peut etre embarrassant.

Nomme tes workflows clairement. "Formulaire contact → Slack + email" plutot que "Workflow 1". Tu te remercieras dans 6 mois quand tu auras 15 workflows actifs.

Garde les workflows courts. 2 a 4 actions maximum par trigger. Si tu as besoin de plus, decoupe en plusieurs workflows. Ca facilite le debug et la maintenance.

Surveille les logs. OttoKit garde un historique de chaque execution. Verifie regulierement que tout fonctionne - surtout apres une mise a jour de plugin.

---

[OUTRO]

OttoKit connecte tous les outils de ton site ZipWP entre eux. Formulaires, achats, CRM, LMS, notifications - tout communique automatiquement.

C'est la derniere piece du puzzle operationnel. Ton site genere avec ZipWP, tes produits vendus avec SureCart ou WooCommerce, tes emails geres par FluentCRM, tes cours sur TutorLMS, tes funnels sur CartFlows - et OttoKit qui orchestre le tout en arriere-plan.

Dans la prochaine lecon, on revient au design pur. Comment creer une landing page de vente optimisee avec ZipWP et les blocs avances de Spectra.

---

## Notes de production

### Captures d'ecran suggerees

1. **OttoKit Dashboard** - Vue d'ensemble avec les workflows actifs
2. **Workflow builder** - Interface trigger → actions avec les blocs connectes
3. **Cas 1** - Workflow formulaire → Slack + email
4. **Cas 2** - Workflow achat → FluentCRM tag + TutorLMS inscription
5. **Logs OttoKit** - Historique d'execution avec statuts

### Transitions

- Intro → Section 1 : ouverture du site OttoKit, installation du connecteur
- Section 1 → Section 2 : liste des triggers avec icones des plugins
- Section 2 → Section 3 : liste des actions disponibles
- Section 3 → Section 4 : creation du premier workflow en live
- Section 4 → Section 5 : retour avatar, conseils bonnes pratiques
- Section 5 → Outro : vue d'ensemble de l'ecosysteme connecte

### Notes HeyGen / ElevenLabs

- Ton energique et pratique - montrer la puissance de l'automatisation
- Section 2 et 3 (triggers/actions) : rythme enumeration, bien poser chaque element
- Section 4 (cas concrets) : rythme tutoriel, montrer la creation du workflow etape par etape
- Eviter le jargon technique excessif - rester accessible
