# Commandes prédéfinies pour le bridge Telegram — schoolsWP

## Architecture proposée

La logique est simple : avant d'envoyer le texte à Claude, le bridge intercepte les commandes
qui commencent par `/` et les remplace par un prompt préconstruit. Le reste du code ne change pas.

```
Message Telegram ("/seo")
        ↓
  resolveCommand()          ← nouvelle fonction
        ↓
  prompt complet (200+ mots)
        ↓
  runClaude(prompt)
        ↓
  réponse → Telegram
```

La séparation entre **mapping commandes** et **logique d'exécution** est intentionnelle :
les prompts vivent dans un objet dédié, modifiable sans toucher à la boucle principale.

---

## Modifications de bridge.js

Quatre changements par rapport au script de base :

1. Ajouter la constante `SCHOOLSWP_PATH`
2. Ajouter l'objet `COMMANDS` et la fonction `resolveCommand()`
3. Remplacer le bloc commandes spéciales dans la boucle
4. Passer `cwd: SCHOOLSWP_PATH` dans `runClaude()`

### 1. Constante à ajouter après MAX_MSG_LENGTH

```javascript
const SCHOOLSWP_PATH = process.env.SCHOOLSWP_PATH ||
  "D:/VS Code/CLAUDE CODE/projects/schoolswp";
```

### 2. Objet COMMANDS + resolveCommand() — insérer avant main()

```javascript
// --- COMMANDES SCHOOLSWP ---
const COMMANDS = {

  "/ping": {
    description: "Vérifie que le bridge est actif",
    handler: async (chatId) => {
      await sendMessage(chatId, "Bridge actif.");
    },
  },

  "/status": {
    description: "Uptime et info du bridge",
    handler: async (chatId) => {
      const info = [
        "Status du bridge :",
        `Uptime : ${process.uptime().toFixed(0)}s`,
        `Offset : ${offset}`,
        `Node : ${process.version}`,
        `Projet : ${SCHOOLSWP_PATH}`,
      ].join("\n");
      await sendMessage(chatId, info);
    },
  },

  "/help": {
    description: "Liste toutes les commandes disponibles",
    handler: async (chatId) => {
      const lines = ["Commandes disponibles :\n"];
      for (const [cmd, cfg] of Object.entries(COMMANDS)) {
        lines.push(`${cmd} — ${cfg.description}`);
      }
      await sendMessage(chatId, lines.join("\n"));
    },
  },

  "/seo": {
    description: "Audit SEO rapide du projet schoolsWP",
    prompt: `Tu es un expert SEO WordPress.
Analyse l'état SEO du projet schoolsWP dans ${SCHOOLSWP_PATH}.

Effectue les vérifications suivantes :
1. Liste les articles récemment générés dans content/articles/ (dates, mots-clés cibles)
2. Identifie les 3 articles les plus proches d'un score de publication >= 80
3. Signale les piliers sans contenu ou sous-développés (LMS, CRM, SEO, automatisation)
4. Suggère la prochaine action prioritaire

Réponds en français, format court (5-10 lignes max). Commence par "Audit SEO rapide :"`,
  },

  "/article": {
    description: "Plan + brouillon du prochain article depuis todo.md",
    prompt: `Tu es le rédacteur principal de schoolsWP.
Lis core/tasks/todo.md dans ${SCHOOLSWP_PATH} pour identifier le prochain article à rédiger.

Si un sujet est identifié :
- Génère un plan en 5-7 parties avec angle éditorial fort
- Propose une introduction accrocheuse (3 phrases)
- Liste les 3 mots-clés sémantiques prioritaires
- Indique la commande brain.bat prête à copier-coller

Si aucun sujet dans todo.md, propose les 3 prochains articles les plus rentables
pour le pilier LMS selon la stratégie schoolsWP.

Réponds en français, format structuré.`,
  },

  "/check": {
    description: "Diagnostic ops : logs, todo, articles en cours",
    prompt: `Tu es l'assistant ops de schoolsWP.
Effectue un check rapide du projet dans ${SCHOOLSWP_PATH}.

Vérifie dans l'ordre :
1. core/tasks/todo.md — tâches en cours et bloquées
2. logs/agents.log — dernière erreur ou warning (5 dernières lignes)
3. content/articles/ — articles en cours (v1.md sans v3.md)
4. .env — présence de ANTHROPIC_API_KEY sans afficher sa valeur

Synthèse en 3 sections : "En cours", "Alertes", "Prochaine action".
Réponds en français, sois direct.`,
  },

  "/plan": {
    description: "Plan éditorial de la semaine depuis todo.md",
    prompt: `Lis core/tasks/todo.md dans ${SCHOOLSWP_PATH}.
Présente les tâches sous forme de plan hebdomadaire :
- Urgentes (aujourd'hui)
- En cours (démarrées, à finir)
- Planifiées (cette semaine)
- En attente (bloquées ou dépendantes)

Format : listes à puces avec statut clair. Réponds en français.`,
  },

  "/cluster": {
    description: "Analyse pilier LMS et articles manquants",
    prompt: `Tu es l'architecte éditorial de schoolsWP.
Analyse le pilier LMS dans ${SCHOOLSWP_PATH}.

1. Liste les articles existants dans content/articles/ liés au LMS
2. Identifie les intentions non couvertes (informationnelle, commerciale, comparative)
3. Propose 5 articles de cluster avec mot-clé principal
4. Pour chaque article : intent, pilier, commande brain.bat prête

Réponds en français, tableau pour les propositions.`,
  },

};

function resolveCommand(text) {
  const [cmd, ...args] = text.trim().split(/\s+/);
  const config = COMMANDS[cmd];

  if (!config) return { type: 'prompt', value: text };
  if (config.handler) return { type: 'handler', handler: config.handler };

  if (config.prompt) {
    let prompt = config.prompt;
    if (args.length > 0) {
      prompt += `\n\nContexte supplémentaire : "${args.join(" ")}"`;  // ex: /seo learnpress
    }
    return { type: 'prompt', value: prompt };
  }

  return { type: 'prompt', value: text };
}
```

### 3. Remplacer le bloc commandes dans la boucle principale

```javascript
// AVANT (supprimer ces lignes)
if (text === "/ping") { ... }
if (text === "/status") { ... }
await sendMessage(chatId, "Traitement en cours...");
const response = runClaude(text);
await sendMessage(chatId, response);

// APRÈS
const resolved = resolveCommand(text);

if (resolved.type === 'handler') {
  await resolved.handler(chatId);
  continue;
}

await sendMessage(chatId, "Traitement en cours...");
const response = runClaude(resolved.value);
await sendMessage(chatId, response);
```

### 4. CWD dans runClaude()

```javascript
const output = execSync(cmd, {
  timeout: 120000,
  encoding: "utf-8",
  cwd: SCHOOLSWP_PATH,   // était process.env.HOME
});
```

---

## .env : ajouter la variable

```bash
SCHOOLSWP_PATH=D:/VS Code/CLAUDE CODE/projects/schoolswp
```

---

## Mapping commandes → prompts

| Commande | Intention | CWD Claude | Durée estimée |
|---|---|---|---|
| `/seo` | Audit rapide, état des articles, priorité | schoolsWP | 20-40s |
| `/article` | Brouillon basé sur todo.md, plan + intro | schoolsWP | 30-60s |
| `/check` | Diagnostic ops (logs, todo, .env) | schoolsWP | 15-30s |
| `/plan` | Plan hebdomadaire depuis todo.md | schoolsWP | 10-20s |
| `/cluster` | Analyse pilier LMS, articles manquants | schoolsWP | 40-60s |
| `/ping` | Built-in — pas de Claude | — | <1s |
| `/status` | Built-in — pas de Claude | — | <1s |
| `/help` | Built-in — liste les commandes | — | <1s |

---

## Commandes avec argument optionnel

`resolveCommand()` injecte les mots après la commande dans le prompt.

Exemple depuis Telegram :
```
/seo learnpress-vs-learndash
```

Le bridge envoie le prompt `/seo` complet plus :
> `Contexte supplémentaire : "learnpress-vs-learndash"`

Aucune commande dédiée par variante — un seul point d'entrée par thème.

---

## Ajouter une nouvelle commande

Une seule entrée dans `COMMANDS`. Exemple pour un audit NER :

```javascript
"/ner": {
  description: "Audit NER sur le dernier article généré",
  prompt: `Identifie les entités nommées manquantes dans le dernier article v3.md
de content/articles/ dans ${SCHOOLSWP_PATH}.
Compare avec les entités des 3 premiers résultats SERP pour le mot-clé cible.
Liste par catégorie : personnes, outils, concepts, marques.`,
},
```

---

## Points d'architecture importants

**1. CWD = schoolsWP, pas HOME**

C'est le changement le plus impactant. Claude Code charge automatiquement le `CLAUDE.md`
du répertoire courant. En pointant sur schoolsWP, Claude dispose du contexte projet complet
(branding, agents, structure) sans avoir besoin de le réexpliquer dans chaque prompt.

**2. Built-in vs prompts**

Les commandes sans Claude (`/ping`, `/status`, `/help`) utilisent un `handler` async direct.
Réponse en moins d'une seconde, zéro token consommé.

**3. Timeout**

`/cluster` et `/article` génèrent des réponses longues. Si le timeout de 2 minutes est souvent
atteint, augmenter `timeout: 180000` dans `runClaude()` ou ajouter une contrainte de longueur
dans les prompts ("Réponds en 200 mots max").

**4. Évolution : prompts dans des fichiers externes**

Pour modifier les prompts sans redémarrer le bridge :

```javascript
function loadPrompt(name) {
  const p = `./prompts/${name}.md`;
  return fs.existsSync(p) ? fs.readFileSync(p, "utf-8") : null;
}

// Dans COMMANDS :
"/seo": {
  description: "Audit SEO rapide",
  get prompt() { return loadPrompt("seo"); },
},
```

Structure cible :
```
~/claude-telegram-bridge/
├── bridge.js
├── .env
└── prompts/
    ├── seo.md
    ├── article.md
    ├── check.md
    └── cluster.md
```

Les prompts deviennent éditables depuis n'importe quel éditeur sans toucher au code.
