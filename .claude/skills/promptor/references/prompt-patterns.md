# Prompt Patterns par IA — Reference Promptor

> Ce fichier est consulte par Promptor pour adapter le format et la structure du prompt a l'IA cible.
> Mis a jour : Mars 2026 — Sources : docs officielles OpenAI, Anthropic, Google, Midjourney, Mistral.

## Table des matieres
0. [Claude Code (PRIORITAIRE)](#claude-code)
1. [ChatGPT (OpenAI)](#chatgpt)
2. [Claude (Anthropic)](#claude)
3. [Google Gemini](#gemini)
4. [Image AI (Midjourney, DALL-E, Nano Banana, Flux)](#image-ai)
5. [Coding AI generique (Bolt, Lovable, Cursor)](#coding-ai)
6. [Mistral / Le Chat](#mistral)
7. [Perplexity](#perplexity)
8. [Principes transversaux](#principes)

---

## Claude Code (PRIORITAIRE) <a id="claude-code"></a>

Claude Code est un CLI AI pour le développement logiciel. Les "prompts" pour Claude Code ne sont pas des prompts conversationnels — ce sont des **fichiers de configuration** (CLAUDE.md, SKILL.md, AGENTS.md) ou des **instructions projet** qui persistent entre les sessions.

### Types de "prompts" pour Claude Code

| Type | Format | Usage |
|------|--------|-------|
| **CLAUDE.md** | Markdown structuré | Instructions globales/projet — toujours en contexte |
| **SKILL.md** | YAML frontmatter + Markdown | Skill réutilisable — déclenché par description |
| **AGENTS.md** | Markdown | Instructions pour sous-agents |
| **Prompt conversationnel** | Langage naturel | Tâche ponctuelle dans la session |

### Structure CLAUDE.md — Standard

```markdown
# Titre du projet

## Vue d'ensemble
[Description du projet en 2-3 phrases]

## Stack technique
[Technologies, frameworks, versions]

## Commandes clés
[Les commandes à retenir — avec exemples]

## Conventions de code
[Style, nommage, formatage]

## Architecture
[Structure des dossiers, patterns utilisés]

## Règles absolues
[Ce qui ne doit jamais être fait]
```

### Structure SKILL.md — Format complet

```markdown
---
name: nom-du-skill
description: "Description détaillée — inclure QUAND déclencher et QUELS mots-clés activent le skill. Être légèrement 'pushy' : mentionner les contextes d'utilisation pour que Claude ne sous-déclenche pas."
---

# Titre

## Mission / Objectif
[Ce que le skill fait — le WHY]

## Processus
[Instructions step-by-step]

## Format de sortie
[Template exact si applicable]

## Exemples
[Input → Output si pertinent]
```

### Techniques clés pour Claude Code

- **CLAUDE.md à la racine** : Toujours en contexte. Mettre les conventions et contraintes projet. Max ~500 lignes utiles.
- **Sub-CLAUDE.md** : Claude Code charge automatiquement les CLAUDE.md dans les sous-dossiers actifs — utile pour des conventions par module.
- **Expliquer le pourquoi** : Claude Code performe mieux quand les règles sont justifiées ("ne pas utiliser `rm` parce que..." → il applique le principe plutôt que de bloquer sur la lettre de la règle)
- **Commandes exactes** : Dans CLAUDE.md, toujours montrer les commandes complètes avec chemins absolus ou relatifs précis
- **Hooks** : 13 événements lifecycle (PreToolUse, PostToolUse, Stop…) — configurer dans settings.json pour automatiser des vérifications (linting, tests)
- **Skills = Progressive disclosure** : Metadata (~100 mots) → SKILL.md body (<500 lignes) → references/ (chargé à la demande)
- **Description du skill = le déclencheur** : La description YAML est le seul mécanisme de déclenchement. Elle doit couvrir les formulations que l'utilisateur emploiera réellement.

### Anti-patterns courants Claude Code

- CLAUDE.md trop long (>500 lignes) — alourdit chaque session sans valeur
- Règles sans justification — Claude applique des règles aveuglement si le pourquoi manque
- Skills sans exemples d'input/output — le skill reste flou et se déclenche mal
- Description de skill trop courte — Claude sous-déclenche si les mots-clés sont insuffisants
- Pas de commandes exactes — "lance les tests" est inutile sans la commande précise

### Sources officielles
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [CLAUDE.md conventions](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)

---

## ChatGPT (OpenAI) <a id="chatgpt"></a>

### Structure recommandee
```
[System Prompt]
Role: Define who the AI is
Goal: What it should accomplish
Constraints: Rules, tone, format restrictions

[User Prompt]
Context: Background information
Task: Clear, specific instruction
Format: Expected output structure
Examples: (optional) Input/output pairs
```

### Techniques cles
- **System prompt** : Utiliser le champ systeme pour le role et les regles permanentes
- **Markdown** : ChatGPT comprend tres bien le markdown structure (titres, listes, tableaux)
- **Reading order** : Le modele lit de haut en bas — mettre les infos les plus importantes en premier
- **Prompt caching** : OpenAI cache les prompts automatiquement. Partie statique au debut, contenu variable a la fin (moins cher + rapide)
- **Zero-shot d'abord** : Essayer sans exemples avant d'ajouter du few-shot
- **Few-shot** : Si necessaire, 2-3 exemples input/output pour calibrer le format
- **Delimiteurs** : Utiliser `"""` ou `###` pour separer les sections

### Modeles de raisonnement (o1/o3) vs GPT (4o/5)
- **o1/o3** : Le chain-of-thought est integre. NE PAS ajouter "reflechis etape par etape" (redondant). Garder le prompt simple, decrire le probleme et le resultat attendu
- **GPT-4o/5** : Beneficient d'instructions tres precises et structurees. Etre explicite sur la verbosity, les edge cases et le format
- **En production** : Epingler un snapshot specifique (ex: `gpt-5-2025-08-07`) pour un comportement constant

### Erreurs courantes
- Prompts trop vagues ("ecris-moi un article sur le SEO")
- Ajouter "think step by step" aux modeles de raisonnement (redondant)
- Mettre le contenu variable avant le contenu statique (casse le caching)
- Pas de format de sortie specifie
- Trop de contraintes contradictoires

### Sources officielles
- [Prompt Engineering Guide (OpenAI API)](https://developers.openai.com/api/docs/guides/prompt-engineering/)
- [GPT-5 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)
- [GPT-4.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)

---

## Claude (Anthropic) <a id="claude"></a>

### Structure recommandee
```xml
<role>You are a [specific role] that [specific behavior].</role>

<context>
Background information the model needs.
</context>

<instructions>
1. Step-by-step instructions
2. Constraints and rules
3. Output format specification
</instructions>

<examples>
<example>
<input>Sample input</input>
<output>Expected output</output>
</example>
</examples>

<input>
{{user_data}}
</input>
```

### Techniques cles
- **XML tags** : Signature de Claude. Wrapper chaque type de contenu dans son propre tag. Utiliser des noms coherents et les referencer dans les instructions
- **Nesting** : Tags hierarchiques : `<documents>` > `<document index="1">` > `<document_content>`
- **Claude 4.x est litteral** : Fait exactement ce qu'on demande, rien de plus. Etre explicite
- **Adaptive thinking** : Claude 4.6 utilise `thinking: {type: "adaptive"}` avec parametre `effort`
- **Etre direct** : Instructions directes sans formules de politesse excessives
- **Documents longs** : Excelle sur les longs contextes (200K tokens) — fournir les documents complets plutot que des resumes
- **Flexibilite des tags** : Pas de tags "canoniques". Utiliser des noms qui ont du sens. XML, JSON ou prompting labelle fonctionnent tous
- **Expliquer le pourquoi** : Claude performe mieux quand on explique pourquoi une instruction est importante plutot que juste comment

### Changements Claude 4.6 (IMPORTANT)
- **Prefill deprecie** : Le pre-remplissage du dernier tour assistant est deprecie en Claude 4.6. Migrer vers d'autres techniques
- **Extended thinking** : Preferer le thinking natif plutot qu'un outil "think"
- **Pas de menaces** : Les formulations negatives ("tu seras puni si...") degradent les performances

### Erreurs courantes
- Utiliser le format ChatGPT (markdown au lieu de XML)
- Etre vague quand Claude peut traiter des specs precises (il prend les instructions au pied de la lettre)
- Sous-utiliser le contexte long
- Tags inconsistants entre les sections
- Sur-specifier quand le modele gere deja bien la tache avec un minimum d'instructions

### Use case : Redaction editoriale SEO (schoolsWP)

Workflow valide pour tout article SEO : **SERP → IA → Humain**

Phase 1 — Intelligence SEO (avant de donner le brief a Claude)
- mot-cle cible, intention de recherche, persona, promesse, plan, sources, angle differenciant, CTA

Phase 2 — Production IA (Claude redige section par section)
- intro, H2/H3, comparaisons, FAQ, conclusion
- Claude ne doit jamais inventer : retour d'experience, test reel, opinion vecue, resultat terrain

Phase 3 — Couche humaine (copywriter finalise)
- insights uniques, jugement, vecu terrain, transitions naturelles, conversion

**Template de prompt operationnel (version production) :**

```
Tu es un expert en redaction SEO editoriale WordPress.

Mon contexte : schoolsWP, media WordPress — freelances, createurs, formateurs, entrepreneurs.

Ton editorial : direct, concret, simple, sans blabla, phrases courtes, logique terrain.

Principe : SERP d'abord → IA ensuite → Humain a la fin

Regles non negociables :
- n'invente aucun retour d'experience
- n'invente aucun test reel ou opinion vecue
- n'ecris pas comme une IA generique
- pas de remplissage ni de phrases creuses

Ta mission : produire un draft SEO structure, section par section, en respectant l'intention, le plan et le ton schoolsWP.

Procedure :
1. Lis le brief
2. Resume ce que tu as compris
3. Identifie l'intention de recherche
4. Redige le contenu section par section
5. FAQ + conclusion avec CTA naturel
6. Relecture finale (fluidite, coherence, clarte)

Format de sortie obligatoire :

## 1. Comprehension du brief
- Sujet :
- Persona :
- Intention de recherche :
- Promesse :
- Angle differenciant :
- CTA prevu :

## 2. Ajustements recommandes
- Ce que tu gardes
- Ce que tu ameliorerais
- Ce qui manque eventuellement

## 3. Draft de l'article
[H2/H3 section par section + FAQ + Conclusion]

## 4. Auto-verification finale
- Intention respectee : oui/non
- Parties generiques a retravailler :
- Zones a enrichir humainement :
- Passages a illustrer avec experience terrain :
- CTA coherent : oui/non

Contraintes : phrases courtes, un paragraphe = une idee, style naturel, exemples concrets quand possible.
Si le brief est incomplet, lister exactement ce qu'il manque. Sinon, executer directement.
```

**Mini prompt d'amorcage** (a coller avant chaque brief) :

```
Je vais te donner un brief editorial schoolsWP.
Ta mission : ne rien inventer, respecter l'intention, suivre le plan, ecrire comme un redacteur SEO pedagogique pas comme une IA generique.
Avant de rediger : resume le brief, confirme l'intention, signale les points faibles du plan, puis redige seulement apres.
```

### Sources officielles
- [Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Claude 4 Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Use XML Tags](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags)
- [Extended Thinking Tips](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/extended-thinking-tips)

---

## Google Gemini <a id="gemini"></a>

### Structure recommandee (texte)
```
Goal: [What you want]
Output format: [How you want it]
Context: [Background information]
Constraints: [Rules to follow]
```

Gemini 3 permet des prompts beaucoup plus courts. Objectif + format, puis stop. Ajouter des regles seulement si on observe une derive.

### Structure recommandee (Gemini Canvas / code)
```
Projet : [nom et description]
Stack technique : [technologies]
Fonctionnalites :
1. [feature 1]
2. [feature 2]
Design : [style, couleurs, UX]
Contraintes : [limitations]
```

### Techniques cles
- **Temperature a 1.0** : Le raisonnement de Gemini 3 est optimise pour cette valeur par defaut. NE PAS la baisser
- **Oriente livrable** : Gemini repond mieux quand on decrit le resultat concret attendu
- **Precision produit > jargon technique** : Decrire ce que l'utilisateur voit/fait plutot que l'implementation
- **Markdown structure** : Meilleur avec des sections markdown pour les taches longues
- **Grounding** : Peut verifier les faits via Google Search — l'activer pour les contenus factuels
- **Eviter les negations larges** : "Ne pas inferer" casse la logique. Preferer : "utilise uniquement le contexte fourni"
- **Few-shot avec parcimonie** : Trop d'exemples cause de l'overfitting

### Specificites Nano Banana 2 (generation d'images)
- **Raisonnement avant generation** : Nano Banana Pro raisonne sur le prompt avant de generer, corrigeant les erreurs logiques
- **Texte dans l'image** : Limiter a 25 caracteres. Max 3 phrases pour des compositions propres
- **Images de reference** : Jusqu'a 14 images de reference par prompt pour la coherence
- **Termes photographiques** : Noms de cameras specifiques (GoPro, Fujifilm), types de lentilles, setups d'eclairage
- **4K natif** : Jusqu'a 4096x4096
- **Aspect ratios** : 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
- **Prompts en anglais** : Meilleurs resultats

### Erreurs courantes
- Baisser la temperature en dessous de 1.0 (degrade le raisonnement de Gemini 3)
- Ecrire des prompts longs style 2023 (Gemini 3 prefere court et direct)
- Ne pas preciser le format de sortie dans Canvas
- Depasser 25 caracteres pour du texte dans une image

### Sources officielles
- [Prompt Design Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Gemini 3 Prompting Guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide)
- [Nano Banana Prompting Guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Image Generation with Gemini](https://ai.google.dev/gemini-api/docs/image-generation)

---

## Image AI <a id="image-ai"></a>

### Midjourney V7 — Structure recommandee
```
/imagine [Subject] + [Environment] + [Lighting] + [Style/Medium] --parameters

Debutant :  Subject + Medium + Lighting + --ar
Avance :    Subject + Environment + Lighting + Style + --sref + --ar
```

### Parametres cles Midjourney V7
| Parametre | Description | Plage |
|-----------|-------------|-------|
| `--ar` | Ratio d'aspect | 16:9, 3:2, 1:1, etc. |
| `--s` | Stylize (artistique vs litteral) | 0-1000 |
| `--chaos` | Variete des outputs | 0-100 |
| `--weird` | Elements inattendus | 0-3000 |
| `--exp` | Detail ameliore | 10-25 sweet spot |
| `--sref [URL]` | Reference de style | Plusieurs URLs ok |
| `--sw` | Poids ref style | 0-1000 |
| `--oref [URL]` | Omni reference (coherence) | Single/multiple URLs |
| `--ow` | Poids omni ref | 0-1000 (defaut 100) |

### DALL-E (ChatGPT) — Structure recommandee
```
[Detailed scene description]
Style: [artistic style]
Composition: [framing, angle]
Lighting: [type of lighting]
Color palette: [colors]
Quality: [resolution, detail level]
```

### Techniques cles (toutes IA images)
- **Toujours en anglais** : Les IA d'image sont entrainees principalement en anglais
- **Prompts courts puis iterer** : Ecrire court, choisir le meilleur des 4, ajouter du detail dans cette direction
- **Decrire ce qu'on VEUT** : Les descriptions positives surpassent les negatives
- **Vocabulaire specifique** : "Huge" pas "big", adjectifs precis plutot que generiques
- **Termes cinematographiques** : "Movie still", "cinematic lighting", "depth-of-field", "golden hour"
- **Camera/Lens** : "shot on Canon EOS R5, 85mm f/1.4" ameliore le realisme
- **Style Reference (--sref)** : Applique palette + eclairage + langage visuel. V7 interprete mieux les styles combines
- **Omni Reference (--oref)** : Personnages/objets coherents. Bas --ow = plus d'interpretation

### Erreurs courantes
- Prompts trop longs et verbeux (V7 prefere court et a fort signal)
- Decrire ce qu'il faut eviter plutot que ce qu'on veut
- Mots generiques quand un vocabulaire specifique existe
- Ne pas utiliser --sref/--oref pour la coherence
- Ignorer le parametre --stylize
- Prompts en francais (resultats inferieurs)

### Sources officielles
- [Midjourney Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)
- [Midjourney Style Reference](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference)

---

## Coding AI <a id="coding-ai"></a>

### Framework universel
```
WHAT: [Description de la feature/app/fix]
WHY: [Objectif, probleme utilisateur resolu]
REQUIREMENTS:
- [Requirement 1]
- [Requirement 2]
TECH STACK: [Langages, frameworks, librairies]
CONSTRAINTS: [Performance, securite, accessibilite]
FIRST STEP: [Par ou commencer]
```

### Bolt / Lovable — Structure recommandee
```
## Projet
[Nom et description en 1-2 phrases]

## Stack
[Technologies a utiliser]

## Fonctionnalites (V1)
1. [Feature principale]
2. [Feature 2]
3. [Feature 3]

## Design
- Style : [minimaliste, moderne, glassmorphism...]
- Couleurs : [palette]
- Responsive : [oui/non, mobile-first?]

## Contraintes
- [Monofichier / multi-fichiers]
- [API externes necessaires]
- [Authentification necessaire?]
```

**Bolt** : A un "Prompt Enhancer" integre qui expande les descriptions simples automatiquement. Browser-based, pas de compte necessaire.
**Lovable** : Code React plus propre, excelle sur le design UI. Meilleur quand la qualite visuelle compte.

### Claude Code / Cursor — Structure recommandee
```
## Objectif
[Ce que le code doit faire]

## Contexte technique
[Stack existante, fichiers concernes, conventions du projet]

## Specifications
[Comportement attendu, edge cases]

## Tests
[Comment verifier que ca marche]
```

**Claude Code** : CLAUDE.md a la racine pour les standards, AGENTS.md pour les sous-agents, hooks pour 13 evenements lifecycle.
**Cursor** : Cursor Rules (markdown scope par fichier/dossier). `rule-porter` convertit entre les formats.

### Techniques cles (toutes plateformes)
- **Construire incrementalement** : Jamais l'app entiere en un prompt. Architecture + premier composant, puis iterer
- **Nommer les technologies exactes** : Librairies, versions, frameworks
- **Meta-prompting** : Demander a l'IA d'aider a ecrire un meilleur prompt avant de commencer
- **Specs fonctionnelles > description vague** : "Un bouton qui ajoute un item au panier avec animation slide-in" > "un bouton ajouter au panier"
- **V1 d'abord** : Definir un MVP clair avant les features avancees
- **Error handling** : Preciser comment gerer les erreurs

### Erreurs courantes
- Generer l'app entiere en un seul prompt (erreur #1 du vibe coding)
- Etre vague sur la stack ("make it look nice" vs "use Tailwind + shadcn/ui")
- Ne pas fournir le contexte architecture
- Pas de description du design attendu
- Oublier les edge cases et la gestion d'erreurs

### Sources
- [Bolt Prompting Tips](https://bolt.new/blog/prompting-tips-for-bolt)
- [Claude Code Tips](https://www.builder.io/blog/claude-code)
- [Vibe Coding Prompts](https://vibecodex.io/)

---

## Mistral / Le Chat <a id="mistral"></a>

### Structure recommandee
```
[System Message]
Role: You are a [specific role].
Task: [Clear task definition].
Rules:
- [Constraint 1]
- [Constraint 2]
Output format: [JSON / markdown / plain text]

[User Message]
[Specific request with context]
```

### Techniques cles
- **System prompt d'abord** : Toujours commencer par un role + definition de tache concise. Ca oriente efficacement le modele
- **Concision** : Mistral performe mieux avec des instructions concises et directes
- **Francais natif** : Tres bon en francais — pas besoin de passer en anglais (sauf images)
- **JSON mode** : Setter `response_format: {"type": "json_object"}` ET demander du JSON dans le texte du prompt (le parametre seul ne suffit pas)
- **Magistral** (juin 2025) : Modeles de raisonnement specialises avec chain-of-thought pour la logique multi-etapes
- **Le Chat pour prototyper** : Tester dans le navigateur, puis passer a La Plateforme API pour la production

### Erreurs courantes
- Omettre le system prompt (Mistral beneficie significativement de la definition de role)
- Setter `response_format` en JSON sans aussi demander du JSON dans le prompt
- Copier-coller des prompts ChatGPT sans adapter a Mistral
- Ne pas utiliser Magistral pour les taches de raisonnement multi-etapes

### Sources officielles
- [Prompting Capabilities](https://docs.mistral.ai/capabilities/completion/prompting_capabilities)
- [JSON Mode](https://docs.mistral.ai/capabilities/structured_output/json_mode)
- [Function Calling](https://docs.mistral.ai/capabilities/function_calling)

---

## Perplexity <a id="perplexity"></a>

### Structure recommandee
```
[Question precise et contextuelle]
Focus : [angle specifique]
Sources : [type de sources preferees]
Format : [liste, tableau, paragraphe]
```

### Techniques cles
- **Questions precises** : Perplexity est un moteur de recherche — les questions specifiques fonctionnent mieux
- **Contexte temporel** : Preciser "en 2026" ou "cette semaine" pour des resultats recents
- **Focus** : Preciser l'angle (technique, business, debutant...)
- **Sources** : Demander des sources academiques, officielles, ou communautaires selon le besoin

### Erreurs courantes
- Questions trop generales
- Ne pas preciser la periode temporelle
- Oublier de demander les sources

---

## Principes transversaux <a id="principes"></a>

Ces principes fonctionnent sur TOUTES les IA :

1. **Etre specifique, pas vague** — La plupart des echecs viennent de l'ambiguite, pas des limites du modele
2. **Commencer simple, ajouter la complexite** — Zero-shot avant few-shot. Court avant long
3. **Specifier le format de sortie** — Toujours dire au modele comment structurer sa reponse
4. **Iterer** — Aucun prompt n'est parfait du premier coup. Approche empirique
5. **Separer donnees et instructions** — XML tags, headers markdown, triple quotes
6. **Positif > negatif** — "Fais X" marche mieux que "Ne fais pas Y" sur tous les modeles
7. **Placement du contexte** — Info importante en premier, donnees variables en dernier (aide le caching)
