---
name: session-recap
description: |
  Transforme la session de travail Claude Code en cours en récapitulatif Markdown structuré, prêt à coller dans Google Docs ou un journal. Sortie en bloc code avec 8 sections fixes : contexte, sujets, points-clés, décisions, actions cochables, ressources, prochaines étapes, synthèse. Sert à garder une trace claire avant de fermer ou pivoter une session.
  Utilise ce skill quand l'utilisateur dit : "récap de session", "récapitulatif de session", "résume cette session", "résume la conversation", "fais-moi un récap", "trace de la session", "session recap", "synthèse de la session", "fin de session", "ce qu'on a fait aujourd'hui", ou demande un bilan d'une longue conversation Claude Code. Déclencher même si le terme "skill" n'est pas mentionné — toute demande de synthèse de la conversation en cours doit passer ici.
  NE PAS utiliser pour : transformer une note brute ou un process informel en procédure (utiliser note-to-sop), produire une synthèse pour le vault Obsidian via la passerelle (suivre la SOP obsidian-bridge/SOP-claude-obsidian-bridge.md cas d'usage 3, ce skill peut servir de matériau source), gérer l'état de tâches multi-étapes (utiliser todo ou TodoWrite), ou rédiger un article / newsletter / contenu publié (utiliser schoolswp-content-studio ou les skills éditoriaux dédiés).
allowed-tools:
  - Read
  - Write
---

# Session Recap — Récapitulatif Markdown structuré

Tu transformes la conversation Claude Code en cours en un récapitulatif clair, hiérarchisé, prêt à coller dans Google Docs.

---

## Pourquoi ce skill existe

Une session Claude Code longue accumule décisions, hypothèses, fix techniques, idées éditoriales, fichiers touchés, MCP appelés. Sans trace, ce contexte s'évapore à la fermeture. Ce skill produit en une passe un document de travail lisible, archivable, partageable — pas un dump brut, une synthèse hiérarchisée qui priorise ce qui sert demain.

L'output sort dans un bloc code triple backtick markdown pour que Michael puisse le copier-coller intact, sans que les titres dièse ne soient rendus côté Claude Code.

---

## Source d'information

La source unique est la conversation en cours : messages utilisateur, tes propres réponses, résultats d'outils visibles dans le contexte. Tu ne lis pas de fichiers externes pour produire le récap, sauf si l'utilisateur pointe explicitement un fichier à inclure.

Si la session contient peu d'échanges (moins de 5 tours) ou si rien de substantiel n'a été produit, indique-le clairement dans la section "Points à clarifier" plutôt que de remplir artificiellement.

---

## Structure de sortie — 8 sections fixes

Toujours produire exactement cette structure, dans cet ordre, à l'intérieur d'un bloc code markdown (utiliser quatre backticks en délimiteur externe pour pouvoir imbriquer des blocs code à trois backticks à l'intérieur si la session en contenait).

Sections obligatoires :

1. `# Récapitulatif de la session`
2. `## 1. Contexte général` — 2 à 4 phrases : sujet principal de la session, objectif global, période ou projet concerné. Pas de méta-blabla type "Dans cette session nous avons exploré...".
3. `## 2. Sujets abordés` — Liste à puces des grands thèmes traités. 3 à 8 items max. Chaque item = un libellé court qui identifie le thème, pas un résumé.
4. `## 3. Points importants à retenir` — Les informations clés, faits techniques, contraintes découvertes, blocages identifiés. Une puce = un point. Pas de répétition des sujets de la section 2.
5. `## 4. Décisions prises` — Décisions actées ou orientations choisies pendant la session. Si rien n'a été décidé, écrire "Aucune décision formelle prise — session exploratoire."
6. `## 5. Actions à réaliser` — Checklist Markdown des actions concrètes mentionnées. Format : tiret crochets-vides verbe-impératif objet. Pas de "penser à", "envisager". Si aucune action n'a été évoquée, mettre une seule ligne : "Aucune action en attente identifiée."
7. `## 6. Ressources, outils ou références mentionnés` — Outils, MCP, plugins, fichiers, URL, commandes, skills, agents évoqués. Si des chemins de fichiers ou des commandes spécifiques sont apparus, les conserver tels quels.
8. `## 7. Prochaines étapes recommandées` — Suite logique concrète pour avancer. Différent des actions de la section 5 : les actions = ce qui a été décidé ; les prochaines étapes = ce que tu suggères en plus. 2 à 5 items numérotés.
9. `## 8. Synthèse finale` — 3 à 5 lignes maximum. Résume l'essentiel : où on en était, où on en est, ce qui change. Ton clair, sans jargon inutile, sans répéter les sections précédentes.

Section conditionnelle ajoutée après la 8 uniquement si pertinent :

10. `## Points à clarifier` — Ambiguïtés à lever : décision évoquée mais non actée, action sans propriétaire ou échéance, hypothèse non validée.

---

## Règles de rédaction

- Hiérarchiser, ne pas exhaustivement transcrire. Si la session a 40 tours, le récap ne doit pas faire 40 paragraphes — extraire ce qui sert demain.
- Pas de répétitions entre sections. Si un point apparaît en "Sujets abordés", ne pas le redire en "Points importants à retenir" sauf pour ajouter une nuance.
- Ton clair, pédagogique, professionnel. Pas de "nous avons réussi à...", pas de bullshit. Phrases nominales OK si elles sont plus claires.
- Voix au "je" si nécessaire (mémoire feedback_voice_singular_solo.md). Michael travaille seul : éviter "nous", "notre équipe", etc.
- Verbe à l'impératif pour les actions ("Pousser le mu-plugin", "Vérifier que le sitemap a regénéré"), pas l'infinitif vague.
- Conserver les noms propres tels quels : fichiers, commandes, plugins, MCP, slugs, URL — c'est ce qui rend le récap actionnable.
- Pas d'em-dash (mémoire feedback_no_em_dash.md). Privilégier deux-points, tiret simple, point, ou parenthèses.
- Markdown propre : un saut de ligne entre chaque section, listes à puces avec tiret, pas de tableau sauf si la session en contenait un essentiel.
- Si une information manque, créer la section finale "Points à clarifier" avec la liste des ambiguïtés à lever.

---

## Format de livraison

Toujours livrer le récap encapsulé dans un bloc code markdown, en utilisant quatre backticks en délimiteur externe pour préserver le rendu côté Google Docs et permettre des blocs imbriqués si nécessaire.

Aucun texte avant ou après le bloc code, sauf si l'utilisateur demande explicitement une note d'accompagnement. Le livrable doit être copiable d'un seul coup à l'intérieur du bloc.

---

## Variante : sauvegarder le récap

Si l'utilisateur demande explicitement "sauvegarde ce récap" ou "écris-le dans un fichier", écrire le contenu (sans les délimiteurs externes) dans :

```
projects/schoolswp/core/tasks/session-recaps/YYYY-MM-DD-slug-court.md
```

Avec `YYYY-MM-DD` = date du jour (depuis le contexte si disponible) et slug-court dérivé du sujet principal en kebab-case. Confirmer le chemin écrit à l'utilisateur.

Par défaut **ne pas écrire de fichier** — sortir directement le bloc code dans la réponse.

---

## Garde-fous

- Ne pas inventer. Si la session n'a pas évoqué d'action, ne pas en fabriquer pour remplir la section 5.
- Ne pas extrapoler les décisions. Une hypothèse évoquée n'est pas une décision. Une décision = un "OK on fait X" ou une orientation explicitement validée.
- Ne pas exposer de secrets. Si la session contient des clés API, tokens, mots de passe, les masquer (trois étoiles) dans le récap.
- Auto-stop sur session vide. Si la conversation ne contient pas de matière exploitable (1 ou 2 tours triviaux, juste une salutation), ne pas produire les 8 sections vides — répondre brièvement que la session est trop courte et proposer de relancer le skill plus tard.

---

## Quand le skill se déclenche en parallèle d'autres skills

- Si l'utilisateur demande "récap puis on l'envoie à Obsidian" : produire le récap ici, puis pointer vers la SOP passerelle pour la propagation (obsidian-bridge/SOP-claude-obsidian-bridge.md). Ce skill ne pousse pas vers Obsidian de lui-même.
- Si l'utilisateur demande "récap puis crée les todos" : produire le récap, puis proposer d'invoquer TodoWrite pour matérialiser la checklist de la section 5 en todos suivis.
- Si l'utilisateur veut une vraie SOP réutilisable (pas un récap one-shot) : rediriger vers note-to-sop.
- Si la session a produit du matériau stratégique réutilisable, mentionner la possibilité de le pousser via outbox-to-obsidian (réflexe passerelle cas d'usage 3).

---

## Adaptation par contexte

Le récap reste structuré pareil, mais le niveau de détail s'adapte au type de session :

- Session debug technique : insister sur section 3 (faits techniques) et section 6 (commandes, fichiers, mu-plugins touchés).
- Session éditoriale : insister sur section 2 (cocons / pages traitées) et section 6 (briefs, slugs, mots-clés).
- Session stratégie : insister sur section 4 (orientations) et section 7 (suite logique).
- Session exploratoire (brainstorm) : section 4 peut être vide, mettre l'énergie sur section 3 (idées) et section 8 (synthèse).
- Session mobile (Dispatch) : produire la version condensée — sections 1, 4, 5, 8 uniquement, le reste devient optionnel.
