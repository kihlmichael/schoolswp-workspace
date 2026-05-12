---
name: calendrier-edito-schoolswp
description: |
  Lit / audite / met a jour le calendrier editorial schoolsWP (planning multi-canal en Markdown, source `content/calendrier-edito/`). Propose les prochaines publications, signale les gaps, ajoute / deplace / archive des entrees, suggere des slots pour les idees du backlog. Source unique = Markdown versionne, jamais Sheets/Notion (export Sheets disponible separement a la demande).
  Utilise ce skill quand l'utilisateur dit : "calendrier edito", "calendrier editorial", "qu'est-ce que je publie cette semaine", "audit calendrier", "planning edito", "ligne editoriale", "ajoute [X] au calendrier", "deplace l'entree [Y]", "marque [Z] comme published", "prochaines newsletters", "quoi publier sur LinkedIn", "il me manque quoi en mai", "propose-moi un slot pour [idee]", "qu'est-ce que je peux activer dans le backlog".
  NE PAS utiliser pour : taches projet (dev, audit, missions) qui vont dans `core/tasks/todo.md` (commande `/todo`), production de contenu (skills plateforme : `schoolswp-content-studio`, `linkedin`, `pinterest-pipeline`, etc.), gestion de mission active (utiliser TodoWrite), audit SEO ou GSC (utiliser `radar` agent ou `seo-specialist`).
---

# calendrier-edito-schoolswp

## Vue d'ensemble

Source unique : `content/calendrier-edito/` (Markdown). Un fichier par mois (`YYYY-MM.md`) + `_backlog.md` (idees non datees) + `_legende.md` + `README.md`.

Ce skill ne **produit pas de contenu** : il pilote le calendrier (CRUD entrees + audit + suggestions). La production se delegue aux skills plateforme (`schoolswp-content-studio` pour newsletter, `linkedin` pour LinkedIn, etc.).

## Inputs supportes

L'utilisateur peut demander :

1. **Lecture** : "qu'est-ce que je publie cette semaine ?", "audit calendrier mai", "prochaines newsletters", "quoi publier sur Pinterest cette semaine"
2. **Ajout** : "ajoute [sujet] au calendrier le [date] sur [canal]"
3. **Modification statut** : "marque [entree] comme published avec URL [...]", "passe l'entree du 12 mai en draft"
4. **Reschedule** : "deplace l'entree du [date1] au [date2]"
5. **Kill** : "abandonne l'idee [X]" / "passe en killed"
6. **Suggestion** : "propose-moi un slot pour [idee du backlog]", "quelles idees du backlog je peux planifier ?"
7. **Audit gaps** : "il me manque quoi en mai", "ou sont les trous", "j'ai combien de newsletters prevues ce mois"

## Workflow

### Etape 1 - Lire le contexte

**Action obligatoire** : a chaque invocation, lister `content/calendrier-edito/` et lire :

1. `README.md` (conventions a jour)
2. Le fichier du mois en cours (date du jour)
3. `_backlog.md`
4. Les fichiers des mois mentionnes par l'utilisateur

Ne jamais inferer le format des entrees : se baser sur le format documente dans `README.md`.

### Etape 2 - Identifier l'intention

Catalogue parmi 7 intentions :

| Intention | Mots-cles | Action |
| --- | --- | --- |
| Lecture week | "cette semaine", "prochains jours", "a venir" | filter J → J+7, trier par date |
| Lecture canal | "newsletters", "linkedin", "youtube", canal nomme | filter par canal |
| Audit mois | "audit", "qu'est-ce qu'il me manque", "gaps" | analyser densite + cadences |
| Ajout | "ajoute", "planifie", "programme" | creer entree |
| Modif statut | "marque", "passe en", "published" | MAJ statut + URL si pub |
| Reschedule | "deplace", "decale", "repousse" | changer date |
| Suggestion backlog | "propose un slot", "quoi activer" | matcher idee + creneau libre |

Si l'intention est ambigue, demander une seule fois.

### Etape 3 - Executer l'action

#### Lecture (week / canal)

Format de sortie tableau :

```markdown
## Calendrier - [periode]

| Date | Canal | Pilier | Sujet | Statut |
| --- | --- | --- | --- | --- |
| 2026-05-12 | newsletter | automatisation | Pinterest pipeline | draft |
| 2026-05-13 | linkedin | LMS | Tutor LMS 3.0 eCommerce | idea |
| ... |

**Resume** : X entrees, Y publiees, Z drafts, W ideas.
**Trous** : [dates sans publication sur les canaux a cadence reguliere].
```

#### Ajout

Demander si manquant : date, canal, pilier, sujet, CTA.

Format de l'entree (a respecter exact dans le `.md`) :

```markdown
## YYYY-MM-DD - <canal> - <sujet court>

- **Statut** : <statut>
- **Canal** : <canal>
- **Pilier** : <pilier>
- **Sujet** : <phrase>
- **Lien output** : <chemin ou null>
- **Inspiration** : <chemin fiche ou null>
- **CTA** : <URL cloak schoolswp.com/<slug>/>
- **Notes** : <optionnel>
```

Ecrire l'entree dans le fichier `<YYYY-MM>.md` correspondant. Si le fichier n'existe pas pour ce mois, le creer avec un H1 standard.

Verifier avant ecriture : pas deja une entree sur le meme jour + meme canal. Si oui, signaler conflit.

#### Modification statut

Trouver l'entree par date+canal ou par sujet. MAJ la ligne `- **Statut** :`. Si statut = `published`, demander URL live et ajouter dans Notes.

#### Reschedule

Couper l'entree depuis le fichier source (mois courant) et la recoller dans le fichier cible (mois cible). Si meme mois, juste reordonner dans le fichier.

Conserver l'historique : ajouter en Notes : `Reschedule : YYYY-MM-DD → YYYY-MM-DD le YYYY-MM-DD`.

#### Kill

MAJ statut a `killed`. Garder l'entree pour historique. Ne jamais supprimer du fichier.

#### Suggestion backlog

1. Lire `_backlog.md`
2. Lire le mois courant + suivant
3. Identifier les **canaux sous-cadencees** (newsletter < 1/sem, linkedin < 2/sem, etc.)
4. Proposer un appariement idee → date libre

Format :

```markdown
## Suggestions backlog → calendrier

| Idee backlog | Slot propose | Pourquoi |
| --- | --- | --- |
| `idea-pinterest-pipeline-recap` | 2026-05-19 (newsletter) | Newsletter manquante semaine 21, sujet automatisation aligne |
| `idea-fluentboards-formation-tease` | 2026-05-26 (newsletter) | Aligner sur fin mai pour preparer juin |

Dis-moi lesquels tu valides et je deplace les entrees du backlog vers le mois.
```

#### Audit mois

Analyser :

- **Densite par canal** : nombre d'entrees vs cadence cible (cf README cadences)
- **Trous calendaires** : jours sans publication sur canaux reguliers (newsletter, linkedin)
- **Statuts orphelins** : entrees `draft` sans `Lien output`, entrees `scheduled` a J-2 sans validation
- **Manque pilier** : si un pilier majeur (LMS, CRM, SEO) n'apparait pas du tout dans le mois
- **Backlog dormant** : idees du backlog depuis > 30j sans planning

Format de sortie :

```markdown
## Audit calendrier - [mois]

### Densite par canal
- newsletter : X / 4 (cible 1/sem) - [OK | sous-cadence]
- linkedin : X / 12 (cible 2-3/sem) - [...]
- ...

### Trous a combler
- 2026-05-19 : pas de newsletter
- 2026-05-21 → 2026-05-25 : pas de LinkedIn

### Drafts en retard
- 2026-05-12 newsletter (statut draft, lien output null) → a finaliser

### Piliers absents
- Aucun contenu LMS programme ce mois

### Backlog dormant
- `idea-pinterest-pipeline-recap` (en backlog depuis 18j)

### Suggestions
- [...]
```

### Etape 4 - Confirmer l'ecriture

Avant chaque modification de fichier, **annoncer le diff** :

```markdown
**A modifier** : `content/calendrier-edito/2026-05.md`
**Action** : ajouter entree `2026-05-19 - newsletter - Pinterest pipeline pas a pas`
**Statut** : idea → idea (nouveau)

OK pour ecrire ?
```

Sauf si auto-mode est actif et que la modification est triviale (status passage idea → draft, MAJ Notes), demander confirmation pour : ajout, reschedule, kill, MAJ massif.

## Regles critiques

1. **Source unique = Markdown.** Ne jamais creer une copie Sheets/Notion en parallele. L'export Sheets est un script optionnel a la demande, jamais sync auto.
2. **Format d'entree strict.** Respecter exactement le format documente dans `README.md`. Le skill ne doit pas devier (sinon les futurs audits cassent).
3. **Ne jamais ecraser une entree existante** sans confirmation. Si conflit (meme jour + meme canal), demander.
4. **Conserver l'historique.** Les entrees `published` et `killed` restent dans le fichier mensuel. Pas de suppression.
5. **CTA toujours en URL cloak interne** (`schoolswp.com/<slug>/`), jamais `/go/`, jamais marchand direct (cf feedback_kadence_cta_template.md).
6. **Date toujours en `YYYY-MM-DD`.** Pas de relatif ("la semaine prochaine"), convertir en date absolue avec la date du jour comme reference (today : voir `currentDate` dans le contexte).
7. **Tutoiement et "je"** dans les retours utilisateur. Voix schoolsWP comme partout.
8. **Pas d'em-dash** dans le contenu produit.
9. **Si le mois cible n'existe pas** comme fichier, le creer avec le titre H1 standard (`# Calendrier editorial - <Mois> <Annee>`) avant d'y ajouter l'entree.
10. **Distinction stricte avec `core/tasks/todo.md`** : ce skill ne touche jamais `todo.md` (taches projet) ni n'utilise TodoWrite (mission en cours). Calendrier edito = publications. Todo = travail dev/audit.

## Anti-patterns

- **Inventer des entrees** : si l'utilisateur demande "qu'est-ce que je publie cette semaine" et que rien n'est dans le calendrier, repondre "rien n'est planifie" + suggerer le backlog. Ne pas halluciner.
- **Dupliquer entree** : verifier toujours date+canal avant ajout.
- **Modifier sans confirmer** : sauf cas trivial, toujours annoncer le diff.
- **Pousser vers Sheets / Notion** : jamais. Si Michael demande explicitement un export Sheets, dire "OK, mais la source reste Markdown - l'export est un script ponctuel".
- **Toucher au calendrier pour des taches dev** : si la demande concerne un bug, un audit code, une mission technique, rediriger vers `core/tasks/todo.md` ou TodoWrite.

## Integration avec d'autres skills

- **schoolswp-content-studio** : produit le draft d'une entree planifiee. Quand le draft est ecrit, MAJ le statut a `draft` et renseigne `Lien output`.
- **lead-magnet-schoolswp** : si une entree concerne un lead magnet, le skill produit le funnel + on cree une entree calendrier `email-promo`.
- **linkedin** / `instagram-strategy` / `pinterest-pipeline` / `schoolswp-youtube-studio` : meme flow - produire le contenu, MAJ entree calendrier.
- **brain-autonome** : audit strategique macro (tous cocons, tous canaux, tous mois). Le calendrier est une donnee d'entree pour brain-autonome.
- **capture-inspiration** : les fiches `content/inspirations/` peuvent etre liees a une entree via le champ `Inspiration`.

## Convention de creation d'un nouveau mois

Si l'utilisateur demande d'ajouter une entree pour un mois sans fichier existant, creer le fichier avec ce template :

```markdown
# Calendrier editorial - <Mois en francais> <Annee>

> Mois <statut>. Ajouter chaque publication au format defini dans `README.md`.

---

## YYYY-MM-DD - <canal> - <sujet>

- **Statut** : ...
- ...
```

Statut : "en cours" si mois courant, "a venir" si mois futur, "passe" si mois passe (rare cas de back-dating).
