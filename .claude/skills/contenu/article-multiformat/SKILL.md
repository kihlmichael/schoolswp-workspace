---
name: article-multiformat
description: |
  Dérive un article schoolsWP publié en 4-6 formats prêts à coller : newsletter email, post LinkedIn/Bluesky, pin Pinterest (titre + description + board + brief visuel), script YouTube, checklist/lead magnet et citation/punchline. Chaque dérivation reste fidèle au contenu source sans rien inventer.
  Utilise ce skill quand l'utilisateur dit : "multiformat", "déclinaisons", "dérive l'article", "newsletter + LinkedIn", "fais les formats pour...", "repurpose", "contenu social pour cet article", ou veut décliner un article publié sur plusieurs canaux.
  NE PAS utiliser pour : créer du contenu social original sans article source (utiliser `linkedin`, `pinterest-strategy`, `instagram-strategy`), rédiger l'article lui-même (utiliser `schoolswp-article-workflow`), ou recycler un email reçu (utiliser `email-to-content`).
---

# /article-multiformat — Derivation multi-format schoolsWP

Transforme un article schoolsWP en 4-6 formats prets a publier sur differents canaux.

## Entrees

`$ARGUMENTS` — chemin vers un fichier markdown article.

- Si un chemin `.md` est fourni, lire le fichier et produire toutes les derivations.
- Si aucun argument, chercher le fichier `.md` le plus recent dans `content/articles/` et demander confirmation.

**Etape 1** : lire l'article complet. Identifier le titre, le mot-cle, le cluster, les points cles, la FAQ et la conclusion.

---

## Regles generales

Ces regles s'appliquent a toutes les derivations :

1. **Fidelite au contenu source** : ne jamais inventer d'information, de chiffre ou d'avis qui n'est pas dans l'article.
2. **Ton schoolsWP** : direct, utile, concret, humain, pedagogique. Tutoiement systematique.
3. **Pas de references temporelles fragiles** : pas de "cette semaine", "hier", "recemment". Formulations intemporelles.
4. **Noms d'outils explicites** : "FluentCRM", pas "cet outil". "OttoKit", pas "ce plugin".
5. **Signature** : les formats signes utilisent "Michael" (newsletter, post social).
6. **Longueur stricte** : respecter les fourchettes indiquees pour chaque format.

---

## Format 1 — Newsletter schoolsWP News

**Canal** : email via FluentCRM
**Longueur** : 300-500 mots
**Frequence** : 1 newsletter par article publie (max 1/semaine)

### Structure

```
OBJET : {Lecon en 1 phrase — max 50 caracteres, percutant, sans clickbait}

---

{ACCROCHE PERSONNELLE}
1-2 phrases. Anecdote, observation ou constat personnel lie au sujet de l'article.
Ton conversationnel, comme si Michael ecrivait a un ami.

{LECON OU INSIGHT}
2-3 phrases. Le point cle de l'article, reformule en mode conversationnel.
Pas un resume — une lecon. Ce que le lecteur doit retenir.

{APPLICATION PRATIQUE}
1-2 phrases. Ce que le lecteur peut faire tout de suite, concretement.
Actionnable et specifique.

{LIEN VERS L'ARTICLE}
1 phrase d'invitation naturelle + lien.
Pas "cliquez ici". Plutot "J'ai detaille les X etapes dans mon dernier article."

{CLOTURE}
1 phrase signature + prenom.

A la semaine prochaine,
Michael
```

### Exemple (article securite)

```
OBJET : La securite WordPress, c'est 80% de maintenance

---

J'ai audite un site client la semaine derniere. Resultat : 3 plugins pas mis a jour depuis 8 mois.

C'est le premier point d'entree des attaques WordPress. Pas les hackers sophistiques. Juste des mises a jour oubliees.

En clair : la securite WordPress, c'est surtout de la rigueur sur les fondamentaux.

Tu peux securiser ton site en 30 minutes avec les 10 etapes que j'ai detaillees dans mon dernier article.

→ Lire l'article : [lien]

A la semaine prochaine,
Michael
```

---

## Format 2 — Post LinkedIn / Bluesky

**Canal** : LinkedIn, Bluesky
**Longueur** : 100-200 mots
**Frequence** : 1 post par article publie

### Structure

```
{ACCROCHE}
1 phrase percutante. Verite, constat surprenant, ou question directe.
Doit donner envie de lire la suite.

{CONTEXTE — optionnel}
1 phrase si necessaire pour poser le cadre.

{3 POINTS CLES}
Extraits des Points cles de l'article, reformules en format court.
→ Point 1
→ Point 2
→ Point 3

{CONCLUSION ENGAGEANTE}
1-2 phrases. Question ouverte ou invitation a reagir.
Pas de CTA commercial. Generer de l'engagement.
```

### Regles specifiques LinkedIn

- Pas de hashtags en exces (max 3, en fin de post)
- Pas d'emojis sauf si explicitement demande
- Sauter des lignes entre chaque bloc pour la lisibilite mobile
- L'accroche doit tenir sur 2 lignes max (visible avant "voir plus")

### Exemple (article monetisation)

```
67% des sites WordPress ne generent aucun revenu.

Pas parce que c'est impossible. Parce que la plupart des createurs n'ont pas de strategie.

Apres avoir teste des dizaines d'approches, voici ce qui marche vraiment :

→ L'affiliation ciblee rapporte plus que la publicite
→ Un espace membre vaut mieux que 10 articles sponsorises
→ L'email marketing reste le levier le plus sous-estime

Quel levier tu utilises sur ton site WordPress ?

#WordPress #Monetisation #Freelance
```

---

## Format 3 — Pin Pinterest

**Canal** : Pinterest (pipeline Placid + Tailwind)
**Frequence** : 2-3 pins par article publie (angles differents)

### Structure (par pin)

```
TITRE : {Titre adapte Pinterest — max 100 caracteres. Clair, benefice visible.}

DESCRIPTION : {Benefice principal + mot-cle + CTA vers article — 150-300 caracteres.
Inclure 2-3 mots-cles naturellement integres.}

BOARD CIBLE : {Choisir parmi :}
- WordPress Securite
- WordPress Business
- Automatisation WordPress
- WordPress Tutoriels
- WordPress Freelance

BRIEF VISUEL :
- Style : schoolsWP
- Fond : blanc ou clair (#FFFFFF ou #F5F5F5)
- Typographie titre : Montserrat Bold
- Couleur accent : #00D400
- Format : 1000x1500px (ratio 2:3)
- Element visuel : {icone, screenshot, ou illustration simple liee au sujet}
```

### Generer 2-3 pins avec des angles differents

Pour un article sur la securite WordPress :
- **Pin 1** (tutoriel) : "10 Etapes Pour Securiser WordPress" — angle pas-a-pas
- **Pin 2** (probleme) : "WordPress Pirate ? Voici Quoi Faire" — angle urgence
- **Pin 3** (liste) : "Checklist Securite WordPress Gratuite" — angle lead magnet

---

## Format 4 — Script YouTube

**Canal** : YouTube
**Duree cible** : 5-15 minutes
**Frequence** : 1 script pour 2-3 articles (selectionner les articles les plus visuels)

### Structure

```
TITRE VIDEO : {Titre YouTube optimise — max 60 caracteres, mot-cle inclus}

DESCRIPTION : {2-3 phrases + liens + timestamps}

---

HOOK (0-5 secondes)
{Probleme ou promesse — 1 phrase directe, percutante.}
Objectif : empecher le scroll. Pas de "Bonjour, bienvenue sur ma chaine".

INTRO (5-30 secondes)
{Ce qu'on va voir + pourquoi c'est utile — 2-3 phrases.}
Pas de longue presentation. Aller droit au sujet.

DEMONSTRATION
{Etapes de l'article adaptees au format visuel.}

Etape 1 : {action}
→ A l'ecran : {ce qu'on voit — capture, interface, schema}
→ Voice-over : {ce qu'on dit — 2-3 phrases max}

Etape 2 : {action}
→ A l'ecran : {ce qu'on voit}
→ Voice-over : {ce qu'on dit}

Etape 3 : {action}
→ A l'ecran : {ce qu'on voit}
→ Voice-over : {ce qu'on dit}

[... autant d'etapes que necessaire]

RECAP (30 secondes)
{3-4 points cles repris en phrases courtes.}
Renforcer le message central.

CTA (15 secondes)
{1. Abonnement si pas encore fait.}
{2. Lien en description vers l'article complet.}
{3. Invitation a tester / question pour les commentaires.}
```

### Regles specifiques YouTube

- Le hook doit fonctionner sans contexte (les 5 premieres secondes decident tout)
- Chaque etape = 1-2 minutes max. Si c'est plus long, decouper en sous-etapes
- Privilegier les articles avec des interfaces a montrer (plugins, dashboards, configurations)
- Les articles purement strategiques (pas d'interface) → format talking head ou schema anime

---

## Format 5 — Checklist / Lead Magnet

**Canal** : PDF telechargeable, lead magnet newsletter
**Frequence** : 1 checklist pour les articles tutoriels ou guides en etapes

### Structure

```
TITRE : Checklist — {Sujet} en {X} etapes

{Sous-titre optionnel : 1 phrase de contexte}

□ Etape 1 : {action concrete et specifique}
□ Etape 2 : {action concrete}
□ Etape 3 : {action concrete}
□ Etape 4 : {action concrete}
□ Etape 5 : {action concrete}
[... jusqu'a 15 etapes max]

---

Ressource complete : {lien vers l'article}
schoolsWP — WordPress. Clair. Structure. Utile.
```

### Regles

- Chaque etape = 1 phrase actionnable (verbe a l'infinitif ou imperatif)
- Max 15 etapes. Si plus, regrouper par categories
- Pas de contexte ou explication — juste les actions. Le detail est dans l'article

---

## Format 6 — Citation / Punchline

**Canal** : visuels sociaux, newsletters, signatures
**Frequence** : 1-2 citations par article (si une phrase forte se degage)

### Structure

```
"{Citation — 1 phrase percutante, autonome, memorable}"

— Michael KIHL, schoolsWP
```

### Regles

- La phrase doit fonctionner seule, hors contexte
- Pas de jargon technique
- Doit exprimer une conviction, un constat ou une verite utile
- Eviter les phrases generiques applicables a n'importe quel domaine

### Exemples

- "La securite WordPress, c'est 80% de maintenance et 20% d'outils."
- "Un site WordPress qui ne genere rien, c'est un hobby. Pas un business."
- "Automatiser sans strategie, c'est juste accelerer le chaos."

---

## Format de sortie

Produire un document markdown unique avec toutes les derivations :

```markdown
# DERIVATIONS MULTI-FORMAT — {Titre de l'article}

**Article source** : {chemin du fichier}
**Cluster** : {A / B / C}
**Date de derivation** : {date}

---

## 1. Newsletter schoolsWP News

{contenu newsletter complet}

---

## 2. Post LinkedIn / Bluesky

{contenu post complet}

---

## 3. Pins Pinterest (x{nombre})

### Pin 1 — {angle}
{titre, description, board, brief visuel}

### Pin 2 — {angle}
{titre, description, board, brief visuel}

### Pin 3 — {angle}
{titre, description, board, brief visuel}

---

## 4. Script YouTube

{script complet — uniquement si l'article se prete au format video}
{Si non applicable : "Article non adapte au format video (pas d'interface a montrer)."}

---

## 5. Checklist

{checklist complete — uniquement si l'article contient des etapes}
{Si non applicable : "Article sans etapes sequentielles — pas de checklist."}

---

## 6. Citations

{1-2 citations extraites}

---

## Resume de distribution

| Format | Canal | Statut | Priorite |
|--------|-------|--------|----------|
| Newsletter | FluentCRM | Pret a envoyer | Haute |
| Post social | LinkedIn + Bluesky | Pret a publier | Haute |
| Pins | Pinterest (Tailwind) | A designer (Placid) | Haute |
| Script YouTube | YouTube | {Pret / Non applicable} | {Moyenne / -} |
| Checklist | PDF / Lead magnet | {Pret / Non applicable} | {Moyenne / -} |
| Citations | Visuels sociaux | Pret | Basse |
```

---

## Exemple

**Entree** : `/article-multiformat content/articles/securite/a1-securiser-wordpress.md`

**Sortie** : document complet avec :
- Newsletter 400 mots sur la lecon "securite = maintenance"
- Post LinkedIn 150 mots avec accroche "67% des sites..."
- 3 pins Pinterest (tutoriel / urgence / checklist)
- Script YouTube 8 min "Comment securiser WordPress en 10 etapes"
- Checklist 10 etapes a cocher
- 1 citation punchline

---

## Actions suivantes

Apres derivation :
1. Programmer la newsletter dans FluentCRM
2. Programmer le post LinkedIn/Bluesky
3. Envoyer les briefs pins au pipeline Pinterest (Placid + Tailwind)
4. Si script YouTube pertinent, planifier le tournage
5. Si checklist pertinente, creer le PDF lead magnet
