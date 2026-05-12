---
name: n8n-reverse-engineer
description: |
  Reverse-engineer un export JSON n8n vers une analyse exhaustive (16 sections) puis vers un Skill Claude Code reproductible : cartographie des nodes, extraction prompts / credentials / expressions, plan de reproduction fidèle, génération du dossier skill complet (SKILL.md + scripts/ + prompts/ + .env + references/).
  Utilise ce skill quand l'utilisateur dit : "j'ai un JSON n8n, fais-en un skill", "analyse ce workflow n8n", "reproduis cette automatisation en code", "migre ce pipeline n8n en Python", "transforme ce n8n en quelque chose de maintenable", ou pour documenter exhaustivement un workflow externe.
  NE PAS utiliser pour : adapter un template externe pour l'instance schoolsWP (utiliser n8n-workflow-adapter), créer un workflow from scratch (utiliser n8n-workflow-architect après cadrage par n8n-orchestrator), ou pour rechercher un template existant (utiliser n8n-template-finder).
---

# n8n Reverse Engineer

Transformer un export JSON n8n en analyse exhaustive puis en Skill Claude Code reproductible.

---

## Pourquoi ce skill existe

Les workflows n8n sont des boites noires : la logique est dispersee entre nodes, expressions, credentials et prompts imbriques. Sans methode, on finit par "s'inspirer" du workflow au lieu de le reproduire fidelement. Ce skill impose une demarche forensique : on prouve d'abord ce que le workflow fait reellement, on identifie ce qu'on ne peut pas prouver, puis on reconstruit.

---

## Entrees attendues

L'utilisateur fournit un ou plusieurs de ces elements :

| Type | Format | Exemple |
|------|--------|---------|
| Export(s) JSON n8n | `.json` | `workflow-youtube-bot.json` |
| Description textuelle | texte libre | "c'est un bot Telegram qui prend un lien YouTube..." |
| Fichiers complementaires | `.md`, `.py`, `.env.example`, `.yaml` | README, scripts, config |

**Minimum requis** : au moins un fichier JSON n8n exporté.

---

## Sorties produites

| Livrable | Format | Contenu |
|----------|--------|---------|
| Analyse complete | Markdown (16 sections) | Cartographie, noeuds, dependances, prompts, ambiguites |
| Plan de reproduction | Markdown (7 sections) | Strategie, structure cible, mapping, scripts, .env, plan sequentiel |
| Skill reproductible | Dossier skill complet | SKILL.md + scripts/ + prompts/ + .env + references/ |

L'analyse et le plan sont produits **avant** toute implementation.

---

## Methode en 3 phases

### Phase 0 — Extraction automatique

Avant d'analyser manuellement, lancer le script `scripts/parse_n8n_workflow.py` sur chaque JSON n8n fourni. Le script extrait automatiquement :

- inventaire des noeuds (type, nom, position dans le flux)
- connexions entre noeuds (graphe)
- expressions n8n presentes
- prompts trouves dans les noeuds Code, Set, HTTP Request, OpenAI, Anthropic
- credentials references (noms, pas les valeurs)
- parametres HTTP (endpoints, methodes, headers)
- code JavaScript/Python embarque dans les noeuds Code

```bash
.venv/Scripts/python scripts/parse_n8n_workflow.py workflow.json
```

Le script produit un rapport structure qui sert de base a l'analyse humaine. Ne pas analyser manuellement ce que le script peut extraire.

### Phase 1 — Analyse (pas d'implementation)

Objectif : comprendre exactement ce que le workflow fait, sans rien inventer.

**Principe de preuve** — Chaque affirmation doit etre fondee sur un element observable :

| Niveau | Signification | Quand l'utiliser |
|--------|--------------|------------------|
| confirme | Directement visible dans un noeud, expression, prompt ou payload | Donne extraite du JSON |
| probable | Coherent avec le contexte mais pas directement lisible | Credential reference sans details |
| incertain | Plusieurs interpretations possibles | Noeud ambigu, branche morte |
| introuvable | Element manquant pour conclure | Sub-workflow non exporte, API inconnue |

La raison de ce systeme : un Skill base sur des suppositions reproduira des comportements fantomes. Mieux vaut un trou explicite qu'une certitude inventee.

**Perimetre d'inspection** — Ne pas se limiter aux JSON. Inspecter aussi :

- README, docs, notes, `.md`, `.txt`
- Scripts `.py`, `.js`, `.sh`
- Fichiers `.env.example`, `.mcp.json`, `.yaml`, `.yml`
- Dossiers `skills/`, `tools/`, `scripts/`, `agents/`, `workflows/`, `telegram/`, `youtube/`, `prompts/`, `config/`
- Sous-workflows references par des noeuds `Execute Workflow`

**Tri production vs archive** — S'il y a plusieurs workflows :

- Identifier lesquels sont actifs (connectes a des triggers reels, complets, sans noeuds desactives)
- Identifier les brouillons/tests (noms generiques, noeuds deconnectes, dates anciennes)
- Justifier le tri par des indices observables, pas par intuition

**Livrable** : analyse Markdown suivant le template `references/analysis-template.md` (16 sections). Lire ce template avant de commencer.

### Phase 2 — Plan de reproduction

Une fois l'analyse validee par l'utilisateur, construire le plan de reproduction.

**Decisions a prendre** :

| Question | Critere de decision |
|----------|-------------------|
| Quoi garder a l'identique ? | Prompts, logique metier, format de sortie |
| Quoi migrer de n8n vers Python ? | Appels API, transformations complexes, code embarque |
| Quoi documenter sans coder ? | Credentials, config manuelle, setup initial |
| Quoi marquer "a confirmer" ? | Tout element au niveau incertain ou introuvable |

**Gestion des secrets** — Toutes les cles, tokens, IDs sensibles doivent sortir du code :

```env
# .env — placeholders uniquement, jamais de vraies valeurs
TELEGRAM_BOT_TOKEN=__A_REMPLIR__
OPENAI_API_KEY=__A_REMPLIR__
```

**Livrable** : plan Markdown suivant les sections 9-15 de `references/analysis-template.md`.

### Phase 3 — Implementation

Seulement apres validation du plan par l'utilisateur. Creer le Skill avec :

- `SKILL.md` — instructions pour reproduire le pipeline
- `scripts/` — scripts Python remplacant les noeuds n8n
- `prompts/` — prompts extraits des noeuds IA (texte brut, un fichier par prompt)
- `.env` — placeholders pour tous les secrets
- `references/` — documentation, schemas, notes

---

## Checklist qualite (avant de livrer chaque phase)

### Phase 1 (analyse)

- [ ] Le script `parse_n8n_workflow.py` a ete execute sur chaque JSON
- [ ] Chaque affirmation porte un niveau de preuve
- [ ] Les prompts sont cites textuellement, pas reformules
- [ ] Les sub-workflows references sont identifies (meme si non exportes)
- [ ] Les credentials sont listes comme dependances (sans valeurs)
- [ ] Les expressions n8n complexes sont documentees mot pour mot
- [ ] Les zones d'ambiguite ont une section dediee

### Phase 2 (plan)

- [ ] Le mapping original -> reproduction couvre chaque noeud
- [ ] Aucune cle sensible en dur
- [ ] Les scripts Python ont des entrees/sorties definies
- [ ] Les dependances Python sont listees
- [ ] L'ordre d'implementation respecte les dependances
- [ ] Les criteres d'acceptation sont verifiables

---

## Ce qu'il ne faut pas faire

L'experience montre que les echecs de reverse-engineering viennent presque toujours de :

| Erreur | Consequence |
|--------|-------------|
| Reformuler un prompt au lieu de le citer | Le comportement IA change |
| Supposer le role d'un credential non exporte | Integration cassee |
| Ignorer un noeud "Set" ou "Edit Fields" | Variables manquantes en aval |
| Fusionner analyse et implementation | Bugs fondes sur des suppositions |
| Traiter un workflow inactif comme actif | Travail inutile |
| Ignorer les expressions n8n dans les champs | Logique dynamique perdue |

La regle est simple : si tu ne l'as pas vu dans le JSON, tu ne peux pas affirmer que ca existe.

---

## Interaction avec les autres skills

| Skill | Quand l'utiliser en complement |
|-------|-------------------------------|
| `n8n-workflow-architect` | Pour la conception du nouveau workflow si on reconstruit dans n8n |
| `n8n-workflow-patterns` | Pour valider que les patterns reproduits sont corrects |
| `n8n-node-configuration` | Pour les details de configuration de noeuds specifiques |
| `workflow-doc` | Pour documenter le resultat final |
| `n8n-code-python` | Pour les noeuds Code Python a migrer |
| `n8n-code-javascript` | Pour les noeuds Code JavaScript a migrer |

---

## Exemple rapide

**Entree** : `workflow-telegram-youtube.json` (export n8n)

**Phase 0** (script) :
```
Workflow: "YouTube Description Generator"
Nodes: 12 (Telegram Trigger → Set → HTTP Request → OpenAI Chat → ...)
Credentials: telegram-bot-api, openai-api
Expressions: 7 found
Code nodes: 1 (JavaScript, 23 lines)
Prompts: 2 (system + user in OpenAI Chat node)
```

**Phase 1** (analyse) : document Markdown 16 sections, ~2000 mots

**Phase 2** (plan) : document Markdown 7 sections avec mapping noeud→script

**Phase 3** (skill) : dossier complet pret a l'emploi

---

## Ressources bundled

| Fichier | Role | Quand le lire |
|---------|------|---------------|
| `references/analysis-template.md` | Template complet des 16 sections d'analyse + 7 sections plan | Avant de commencer Phase 1 |
| `references/node-types-checklist.md` | Quoi extraire de chaque type de noeud n8n | Pendant l'analyse noeud par noeud |
| `scripts/parse_n8n_workflow.py` | Parseur automatique de JSON n8n | Phase 0, avant toute analyse manuelle |
| `examples/sample-analysis-excerpt.md` | Extrait d'analyse reelle pour reference | Si besoin de voir le format attendu |
