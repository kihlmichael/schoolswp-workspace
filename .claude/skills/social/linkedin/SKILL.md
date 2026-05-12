---
name: linkedin
description: >
  Cree des posts LinkedIn pour schoolsWP (Michael KIHL). Utilise ce skill des que l'utilisateur
  veut un post LinkedIn, une accroche LinkedIn, du contenu LinkedIn, un carrousel LinkedIn,
  ou dit "post LinkedIn", "LinkedIn", "publie sur LinkedIn", "ecris pour LinkedIn".
  Aussi utilisable depuis Dispatch mobile pour produire un post rapide et exploitable.
  Ne pas confondre avec le skill social-content (multi-plateformes) — ce skill est spécialisé LinkedIn.
user-invocable: true
allowed-tools:
  - WebFetch
  - WebSearch
  - Read
  - Write
---

# Post LinkedIn schoolsWP

Tu crees des posts LinkedIn pour le compte de Michael KIHL / schoolsWP.
Ton objectif : produire un post pret a publier, utile, credible et engageant.

---

## Identite

- **Auteur** : Michael KIHL, fondateur de schoolsWP
- **Positionnement** : expert WordPress pedagogique, pas gourou marketing
- **Ton** : humain, direct, credible, pedagogique
- **Tutoiement** : non sur LinkedIn (vouvoiement ou neutre)
- **Ce qu'on ne fait jamais** : jargon marketing creux, storytelling inutile, phrases gonflees, emojis en rafale

---

## Entree attendue

L'utilisateur fournit au minimum **un** de ces elements :

| Entree | Comment la traiter |
|---|---|
| **Sujet brut** | "ecris un post LinkedIn sur les LMS WordPress" |
| **Article a transformer** | URL ou fichier — extraire l'idee cle et reformuler |
| **Idee vague** | Proposer un angle avant de rediger |
| **Brief structure** | Sujet + angle + CTA — rediger directement |

Si l'angle n'est pas clair, proposer 2-3 angles avant de rediger.

---

## Structure d'un post LinkedIn schoolsWP

### 1. Accroche (1-2 lignes)

La premiere ligne decide si le post est lu. Elle doit :
- Capter l'attention immediatement
- Donner envie de cliquer "voir plus"
- Etre comprehensible seule (elle apparait dans le feed sans le reste)

Formules qui fonctionnent :
- Affirmation forte : "WordPress n'est pas un CMS. C'est un systeme d'exploitation."
- Question provocante : "Pourquoi 90% des formations WordPress echouent ?"
- Constat contre-intuitif : "Le meilleur plugin SEO WordPress... c'est aucun plugin."
- Experience personnelle : "J'ai teste 12 LMS WordPress en 6 mois. Voici ce que j'ai appris."

### 2. Corps (developpement)

- Progression fluide, 1 idee claire
- Paragraphes courts : 1-2 phrases max
- Sauter une ligne entre chaque paragraphe (obligatoire pour la lisibilite mobile)
- Exemples concrets WordPress quand possible
- Pas de liste a puces de plus de 5 elements
- Si le post contient une lecon, la formuler en une phrase memorable

### 3. Fin

- Conclusion utile OU question engageante (pas les deux)
- CTA naturel si pertinent (pas de "Likez si vous etes d'accord")
- 3-5 hashtags maximum, en fin de post uniquement

---

## Regles de redaction

- **Longueur** : 800-1300 caracteres ideal (LinkedIn coupe a ~210 caracteres avant "voir plus")
- **Espacement** : une ligne vide entre chaque paragraphe
- **Pas de hashtags dans le corps** — uniquement en fin de post
- **Pas d'emojis** sauf usage ponctuel et pertinent (1-2 max)
- **Pas de "je suis ravi de"**, "je suis fier de", "je suis heureux de"
- **Pas de lien dans le corps** — LinkedIn penalise les liens. Si lien necessaire, le mettre en commentaire
- **Valeur concrete des la premiere ligne** apres l'accroche

---

## Formats speciaux

### Carrousel (slide deck)

Si l'utilisateur demande un carrousel :
1. Produire le texte de chaque slide (titre + 2-3 lignes max par slide)
2. Slide 1 = accroche forte (titre du carrousel)
3. Slide finale = CTA + rappel du compte
4. 6-10 slides max
5. Fournir aussi le texte du post qui accompagne le carrousel

### Sondage

Si l'utilisateur demande un sondage :
1. Question claire et engageante
2. 2-4 options (pas plus)
3. Texte d'accompagnement court expliquant le contexte
4. Les options doivent etre equilibrees (pas de reponse evidente)

---

## Format de sortie

```
## Post LinkedIn

[Texte du post pret a copier-coller]

---

## Notes
- **Angle** : [description courte de l'angle choisi]
- **Objectif** : [awareness / engagement / trafic / conversion]
- **Meilleur moment** : [suggestion de jour/heure si pertinent]
- **Lien en commentaire** : [URL a mettre en premier commentaire, si applicable]
```

---

## Mode Dispatch Mobile

Quand le skill est invoque depuis Dispatch (mobile), produire directement le post
sans les notes detaillees :

```
## Post LinkedIn

[Texte pret a copier-coller]

## Lien commentaire
[URL si applicable, sinon omettre]

## Prochaine action
[UNE suggestion : publier, adapter en thread X, ou creer un carrousel]
```

Contraintes mobile : pas de notes longues, pas d'alternatives, juste le post final.
