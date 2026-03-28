# Securite et Performance — VS Code Agent Visual

## Table des matieres

1. [Content Security Policy (CSP)](#csp)
2. [Validation des messages](#validation-messages)
3. [SecretStorage](#secret-storage)
4. [Workspace Trust](#workspace-trust)
5. [LocalResourceRoots](#local-resource-roots)
6. [Performance et memoire](#performance)
7. [Gestion reseau](#reseau)
8. [Checklist securite rapide](#checklist-securite)

---

## Content Security Policy (CSP) {#csp}

La CSP est la premiere ligne de defense d'une webview. Elle restreint les sources
de contenu executables et empeche les injections.

### CSP recommandee (stricte)

```html
<meta http-equiv="Content-Security-Policy"
  content="default-src 'none';
           img-src ${cspSource} data:;
           script-src 'nonce-${nonce}';
           style-src ${cspSource} 'nonce-${nonce}';
           font-src ${cspSource};
           connect-src 'none';">
```

### Regles

| Directive | Valeur | Pourquoi |
|-----------|--------|----------|
| `default-src` | `'none'` | Bloque tout par defaut |
| `img-src` | `${cspSource} data:` | Images locales + data URIs (pour Canvas toDataURL) |
| `script-src` | `'nonce-${nonce}'` | Seuls les scripts avec le bon nonce s'executent |
| `style-src` | `${cspSource} 'nonce-${nonce}'` | Styles locaux + inline avec nonce |
| `font-src` | `${cspSource}` | Polices locales uniquement |
| `connect-src` | `'none'` | Pas de fetch/XHR depuis la webview (tout passe par l'extension) |

### Erreurs courantes a eviter

- **`'unsafe-inline'`** : JAMAIS pour les scripts. Utiliser un nonce a la place.
- **`'unsafe-eval'`** : JAMAIS sauf si un framework l'exige (et dans ce cas, changer de framework).
- **`*` ou `https:`** : trop permissif. Lister les sources explicitement.
- **Oublier `connect-src 'none'`** : sans ca, un script injecte pourrait faire des requetes reseau.

### Nonce : generation et injection

Le nonce est un token cryptographique unique par rendu de webview.
Il doit etre genere cote extension (Node.js) et injecte dans le HTML.

```typescript
import * as crypto from 'crypto';
const nonce = crypto.randomBytes(16).toString('hex');
// Puis injecter dans le HTML : <script nonce="${nonce}" src="...">
```

Ne JAMAIS reutiliser un nonce entre deux rendus de la meme webview.

---

## Validation des messages {#validation-messages}

### Principe

Chaque message recu par `onDidReceiveMessage` doit etre valide avant traitement.
La webview est un contexte non fiable (comme un navigateur).

### Pattern de validation

```typescript
// Whitelist des types de messages acceptes
const MESSAGE_TYPES = new Set([
  'chat:send',
  'avatar:request',
  'animation:control',
  'ui:ready'
]);

// Schemas de validation par type
const MESSAGE_SCHEMAS: Record<string, (payload: unknown) => boolean> = {
  'chat:send': (p) => typeof p === 'string' && p.length > 0 && p.length <= 10000,
  'avatar:request': (p) => typeof p === 'string' && /^[a-z0-9-]+$/.test(p),
  'animation:control': (p) => {
    if (typeof p !== 'object' || p === null) return false;
    const action = (p as { action?: string }).action;
    return typeof action === 'string' && ['pause', 'resume', 'stop'].includes(action);
  },
  'ui:ready': () => true
};

function validateMessage(msg: { type?: string; payload?: unknown }): boolean {
  if (!msg.type || !MESSAGE_TYPES.has(msg.type)) return false;
  const validator = MESSAGE_SCHEMAS[msg.type];
  return validator ? validator(msg.payload) : false;
}
```

### Pourquoi c'est important

- Une extension malveillante ou un bug pourrait injecter des messages dans la webview
- Le postMessage est la seule surface d'attaque significative
- Sans validation, un message mal forme pourrait executer du code inattendu dans l'extension host

---

## SecretStorage {#secret-storage}

### Principe

VS Code fournit `context.secrets` (SecretStorage) pour stocker des tokens et cles API.
Le stockage est chiffre par le systeme (Credential Manager sur Windows, Keychain sur macOS).

### Regles absolues

- **JAMAIS** de cle API dans `settings.json`, `globalState`, ou en dur dans le code
- **JAMAIS** de token dans les messages webview (la webview est un contexte non fiable)
- Utiliser `context.secrets.store(key, value)` et `context.secrets.get(key)`
- Offrir une commande pour configurer les secrets : `agentVisual.setApiKey`

### Flux de configuration d'un secret

```
1. Utilisateur lance la commande "Agent Visual: Set API Key"
2. VS Code affiche un InputBox avec { password: true }
3. L'extension stocke via context.secrets.store('agentVisual.apiKey', value)
4. Le secret est lisible via context.secrets.get('agentVisual.apiKey')
5. Le secret n'est JAMAIS transmis a la webview
```

### Implementation

Voir `references/snippets-claude-integration.md` section "SecretStorage" pour le code complet.

---

## Workspace Trust {#workspace-trust}

### Principe

Workspace Trust empeche l'execution de code potentiellement dangereux dans des workspaces
non fiables (ex: un repo clone depuis une source inconnue).

### Ce que l'extension doit faire

1. **Declarer le support dans `package.json`** :

```json
{
  "capabilities": {
    "untrustedWorkspaces": {
      "supported": "limited",
      "description": "L'agent visuel fonctionne en mode lecture seule sans integration Claude Code.",
      "restrictedConfigurations": [
        "agentVisual.claudeIntegration"
      ]
    }
  }
}
```

2. **Verifier `vscode.workspace.isTrusted` au demarrage** :

```typescript
if (!vscode.workspace.isTrusted) {
  // Desactiver les fonctionnalites sensibles
  stateManager.setRestrictedMode(true);
  // L'avatar peut tourner mais pas de chat ni CLI
}
```

3. **Ecouter `onDidGrantWorkspaceTrust`** :

```typescript
context.subscriptions.push(
  vscode.workspace.onDidGrantWorkspaceTrust(() => {
    stateManager.setRestrictedMode(false);
  })
);
```

### Fonctionnalites par mode

| Fonctionnalite | Trusted | Restricted |
|----------------|---------|------------|
| Avatar anime | Oui | Oui |
| Chat (input) | Oui | Non |
| Integration Claude Code | Oui | Non |
| Commandes CLI | Oui | Non |
| Changement d'avatar | Oui | Oui |
| Parametres sensibles | Oui | Non (valeurs par defaut) |

---

## LocalResourceRoots {#local-resource-roots}

### Principe

`localResourceRoots` restreint les dossiers dont la webview peut charger des ressources.
Par defaut, seule la racine de l'extension est autorisee — il faut etre plus restrictif.

### Configuration recommandee

```typescript
webviewView.webview.options = {
  enableScripts: true,
  localResourceRoots: [
    vscode.Uri.joinPath(context.extensionUri, 'media'),
    vscode.Uri.joinPath(context.extensionUri, 'dist')
  ]
};
```

### Pourquoi pas la racine de l'extension ?

Limiter a `media/` et `dist/` empeche la webview de charger des fichiers sources (`src/`),
des fichiers de config, ou d'autres ressources non prevues.

---

## Performance et memoire {#performance}

### Animation : FPS cap

```javascript
const FPS_CAP = 30; // Suffisant pour des animations fluides
const FRAME_DURATION = 1000 / FPS_CAP;

function animationLoop(timestamp) {
  if (timestamp - lastFrameTime < FRAME_DURATION) {
    requestAnimationFrame(animationLoop);
    return;
  }
  lastFrameTime = timestamp;
  // ... render frame
  requestAnimationFrame(animationLoop);
}
```

### Pourquoi 30 FPS ?

- Les avatars n'ont pas besoin de 60 FPS (ce n'est pas un jeu)
- 30 FPS reduit la consommation CPU/GPU de moitie
- Augmenter a 60 seulement pour des animations tres fluides (transitions, particules)

### `retainContextWhenHidden`

**Par defaut : `false`**. Quand la webview est cachee (onglet en arriere-plan), VS Code
detruit son contenu pour economiser la memoire.

Mettre a `true` UNIQUEMENT si :
- L'etat de la webview est couteux a reconstruire (canvas complexe, long historique chat)
- ET l'utilisateur bascule frequemment entre la webview et d'autres vues

Si `true`, attention : la webview consomme de la memoire meme cachee. Toujours implementer
`dispose()` correctement pour liberer les ressources quand la webview est fermee.

### Gestion memoire

```typescript
// Toujours disposer les listeners, timers, et watchers
class AgentPanel {
  private _disposables: vscode.Disposable[] = [];

  dispose() {
    AgentPanel.currentPanel = undefined;
    this._panel.dispose();
    while (this._disposables.length) {
      const d = this._disposables.pop();
      d?.dispose();
    }
  }
}
```

### Limiter le nombre de webviews

Chaque webview = un process Chromium. Limiter a 2-3 webviews max simultanées
(1 sidebar + 1 panel editeur est un bon maximum).

### Reduce motion

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (prefersReducedMotion.matches) {
  // Afficher un avatar statique au lieu d'animer
  drawStaticAvatar();
} else {
  requestAnimationFrame(animationLoop);
}

// Ecouter les changements
prefersReducedMotion.addEventListener('change', (e) => {
  if (e.matches) stopAnimation();
  else startAnimation();
});
```

---

## Gestion reseau {#reseau}

### Principe

La webview ne doit PAS faire de requetes reseau directement.
Tout le reseau passe par l'extension host (Node.js).

### Pourquoi

- La CSP bloque `connect-src` (et c'est voulu)
- Le controle des requetes est cote extension (logging, rate limiting, auth)
- Pas de fuite de tokens/secrets depuis la webview

### Si un chargement remote est necessaire (rare)

- HTTPS uniquement — jamais HTTP
- Ajouter le domaine explicitement dans la CSP : `connect-src https://api.example.com`
- Preferer le passage par l'extension host quand possible

---

## Checklist securite rapide {#checklist-securite}

- [ ] CSP stricte avec `default-src 'none'` et nonce pour les scripts
- [ ] `connect-src 'none'` (pas de requetes reseau depuis la webview)
- [ ] `localResourceRoots` restreint a `media/` et `dist/`
- [ ] Validation de tous les messages (`onDidReceiveMessage`) : type whitelist + payload schema
- [ ] Secrets dans `SecretStorage`, jamais dans settings/globalState/code
- [ ] Workspace Trust : fonctionnalites sensibles desactivees en Restricted Mode
- [ ] Pas de `'unsafe-inline'` ni `'unsafe-eval'` dans la CSP
- [ ] Nonce regenere a chaque rendu de webview
- [ ] `retainContextWhenHidden: false` sauf justification explicite
- [ ] Dispose de toutes les ressources (listeners, watchers, timers) a la fermeture
- [ ] Pas de chargement remote sauf HTTPS explicite + justifie
- [ ] Pas de transmission de secrets a la webview
