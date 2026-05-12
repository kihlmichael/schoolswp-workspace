---
name: email-reply-schoolswp
description: |
  Drafte une reponse email dans le ton schoolsWP (tutoiement, "je", concis, pas de "nous"/"on"). Prend en input un email recu (collé en texte brut, ou capture/screenshot avec image_path), produit un brouillon Markdown pret a relire et envoyer.
  Utilise ce skill quand l'utilisateur dit : "reponds a cet email", "drafte une reponse", "draft email", "email reply", "ecris-moi une reponse a", "reponse email", "comment je reponds a", ou colle un email recu en attendant un draft.
  NE PAS utiliser pour : transformer un email promotionnel en contenu marketing (utiliser `schoolswp-email-to-content`), créer une sequence email FluentCRM (utiliser `lead-magnet-schoolswp` ou `plugin-email-sequence`), rediger une newsletter (utiliser `schoolswp-content-studio`).
---

# email-reply-schoolswp

## Vue d'ensemble

Ce skill produit un **draft de reponse email** dans le ton schoolsWP. Pas un email parfait : un brouillon que Michael relit, ajuste et envoie depuis Gmail (ou via le MCP Gmail s'il l'invoque).

Le skill ne pousse rien dans Gmail tout seul. Il ecrit le draft en Markdown dans la conversation. Si Michael dit explicitement "cree le draft dans Gmail", invoquer alors le tool `mcp__claude_ai_Gmail__create_draft` apres validation.

## Inputs attendus

L'utilisateur peut fournir :

1. **Email colle en texte brut** dans le message - extraction directe.
2. **Screenshot** (Telegram avec `image_path`, capture VS Code) - Read l'image et OCR mentale.
3. **Resume du contexte** sans email source - Michael decrit ce qu'il a recu et ce qu'il veut repondre.

Si l'email source est absent ou flou, demander une seule fois :
- "C'est quoi le contenu exact de l'email recu ?"
- "Tu veux quel angle dans ta reponse (accord, refus poli, demande de precision, redirection) ?"

## Workflow

### Etape 1 - Lire le contexte voix schoolsWP

**Action obligatoire** : lire `content/docs/BRAND_RULES.md` (regles de marque) AVANT de drafter.

Points cles a respecter :
- Tutoiement systematique
- "je" (Michael est seul, jamais "nous"/"on" sauf citation)
- Pas d'em-dash (`—`) ni d'en-dash (`–`)
- Pas de "schoolswp", "SchoolsWP" : toujours `schoolsWP`
- Pas de mots interdits du brand book

### Etape 2 - Identifier l'intention de reponse

Cataloguer la reponse parmi 6 intentions courantes :

| Intention | Quand l'utiliser | Tonalite |
| --- | --- | --- |
| Accord / suite | Demande raisonnable, deal aligne | Direct, breve, action concrete |
| Refus poli | Sollicitation hors-perimetre, partenariat non aligne | Honnete, sans excuses excessives, redirige si possible |
| Demande de precision | Email vague ou incomplet | 2-3 questions max, format puce |
| Redirection | Mauvais interlocuteur | Pointe vers la bonne ressource ou personne |
| Negociation | Tarif, scope, deadline | Propose une alternative concrete, pas que des objections |
| Suivi / relance | Pas de reponse depuis X | Ton leger, ajoute de la valeur, pas de culpabilisation |

Si l'intention n'est pas claire, demander.

### Etape 3 - Drafter le brouillon

Structure type :

```markdown
**Objet** : Re: [reprend l'objet recu OU nouvel objet si change le contexte]

Salut [prenom],

[1ere phrase qui reconnait l'email recu sans le paraphraser. Concret.]

[2-4 phrases qui repondent a l'intention identifiee. Une idee par phrase.]

[Optionnel : un seul appel a l'action concret. Pas 3.]

[Phrase de cloture courte. Pas de "n'hesite pas a me recontacter pour toute question".]

A bientot,
Michael
```

### Etape 4 - Self-check avant rendu

Avant de rendre le draft, verifier :

- [ ] Tutoiement uniquement ("tu", "te", "ton", "tes")
- [ ] "Je" et jamais "nous"/"on"
- [ ] Aucun em-dash ni en-dash
- [ ] schoolsWP orthographie correctement
- [ ] Phrases de 8-15 mots en moyenne, jamais plus de 20
- [ ] Pas de jargon non explique
- [ ] Pas de cliche email francais ("dans l'attente de votre retour", "bien cordialement", "n'hesitez pas a")
- [ ] Un seul CTA si CTA il y a
- [ ] Signature : "A bientot, Michael" (jamais "Cordialement", jamais "Best regards")

### Etape 5 - Rendre le draft

Format de sortie :

````markdown
## Draft email - [intention identifiee]

**Objet** : Re: [...]

---

[corps de l'email]

---

**Notes pour Michael** :
- Angle pris : [1 phrase]
- Points sensibles : [si applicable, ce que j'ai evite]
- A verifier avant envoi : [montant, date, lien - uniquement si concret]

**Push vers Gmail draft ?** Reponds "oui crée le draft" si tu veux que je l'envoie via le MCP Gmail (sinon copie-colle).
````

## Regles critiques

1. **Jamais d'em-dash.** Remplacer par ` : ` ou ` - ` ou `(...)`.
2. **Jamais de "nous"/"on".** Michael est seul derriere schoolsWP. Reformuler en "je".
3. **Tutoiement systematique.** Meme avec un inconnu - c'est la voix schoolsWP.
4. **Pas de sur-formalisme francais.** Pas de "Madame, Monsieur", pas de "veuillez agreer".
5. **Pas de promesse en l'air.** Si Michael dit "je verrai", ecrire "je regarde et je te dis cette semaine", pas "je m'en occupe".
6. **Ne jamais creer un draft Gmail sans validation explicite.** Le skill rend du Markdown, l'envoi est une action separee qui exige "oui crée le draft" ou equivalent.
7. **Si l'email recu contient une demande sensible** (paiement, donnees client, acces admin), flagger explicitement dans les Notes : "verification identite necessaire avant action".

## Anti-patterns a bannir

- "J'espere que vous allez bien" - neutre, pas de plus-value, supprime.
- "N'hesitez pas a..." - formule cliche, supprime.
- "Comme vous le savez deja..." - condescendant, supprime.
- "Je reviens vers vous des que possible" - vague, remplace par une date concrete.
- "Bien a vous" / "Cordialement" - pas la voix schoolsWP.
- Em-dash partout - interdit.
- Paraphraser l'email recu - fait perdre du temps au lecteur.

## Cas particuliers

### Reponse a un partenariat / sponsoring

Toujours ouvrir avec : est-ce aligne avec le pilier (LMS / CRM / SEO / WordPress) ? Si oui, demander brief + budget. Si non, refuser proprement et rediriger vers une autre creator si possible.

### Reponse a une question technique (lecteur newsletter)

Format : reponse en 2-3 phrases + lien vers article schoolsWP pertinent (cloak interne uniquement, pas /go/, pas de lien marchand direct).

### Reponse a une demande presse / interview

Demander angle + questions par ecrit avant d'accepter. Jamais d'oui sans brief.

### Reponse a un refus / annulation

Sec et court. Pas de plaidoyer. Si pertinent, garder la porte ouverte d'une phrase.
