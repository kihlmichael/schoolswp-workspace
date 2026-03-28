# Checklist de validation — VS Code Agent Visual

Utiliser cette checklist avant de considerer l'extension comme prete a tester ou publier.
Chaque item doit etre valide — un "non" bloque la release.

---

## 1. Environnement et prerequis

- [ ] VS Code >= 1.98.0 installe et a jour
- [ ] Node.js >= 18 LTS installe
- [ ] TypeScript >= 5.5 installe
- [ ] Claude Code fonctionne (connexion validee, panneau operationnel)
- [ ] `npm install` sans erreur dans le projet d'extension
- [ ] `npm run compile` sans erreur TypeScript

## 2. Structure du projet

- [ ] `package.json` : `engines.vscode` >= `^1.98.0`
- [ ] `package.json` : `viewsContainers`, `views`, `commands` declares
- [ ] `package.json` : `activationEvents` incluent `onView:agentVisual.sidebar`
- [ ] `package.json` : `capabilities.untrustedWorkspaces` declare
- [ ] `media/icons/agent.svg` existe (icone sidebar)
- [ ] `media/webview/agent.css` et `media/webview/agent.js` existent
- [ ] `media/animations/` contient au moins 1 animation (Lottie JSON ou spritesheet)

## 3. Extension Host (TypeScript)

- [ ] `extension.ts` : `activate()` enregistre le provider et les commandes
- [ ] `extension.ts` : tous les disposables dans `context.subscriptions`
- [ ] `AgentSidebarProvider` : implemente `WebviewViewProvider`
- [ ] `AgentSidebarProvider` : `resolveWebviewView()` configure `enableScripts` + `localResourceRoots`
- [ ] `AgentSidebarProvider` : ecoute `onDidReceiveMessage` avec validation whitelist
- [ ] `AgentPanel` : singleton pattern (`createOrShow`)
- [ ] `AgentPanel` : `dispose()` nettoie toutes les ressources
- [ ] `AgentStateManager` : `EventEmitter` pour notifier les webviews
- [ ] `AgentStateManager` : getState() retourne une copie (pas de reference mutable)

## 4. Webview (HTML/CSS/JS)

- [ ] CSP stricte : `default-src 'none'` + nonce pour scripts et styles
- [ ] Pas de `'unsafe-inline'` ni `'unsafe-eval'`
- [ ] Toutes les ressources via `asWebviewUri()` + `localResourceRoots`
- [ ] `acquireVsCodeApi()` appele une seule fois
- [ ] `postMessage` / `onmessage` : types de messages documentes
- [ ] Animation : FPS cap a 30 (ou moins)
- [ ] Animation : respect `prefers-reduced-motion` (avatar statique si active)
- [ ] Chat : validation input (longueur max, sanitization)
- [ ] Chat : attribut `role="log"` + `aria-live="polite"` sur le conteneur
- [ ] Accessibilite : navigation clavier complete (Tab, Enter, Escape)
- [ ] Accessibilite : attributs `aria-label` sur les elements interactifs
- [ ] Accessibilite : contrastes conformes (utilise les CSS variables VS Code)
- [ ] Theme : utilise `var(--vscode-*)` pour s'adapter au theme actif

## 5. Integration Claude Code

- [ ] Bridge CLI : `claude -p` fonctionne et retourne une reponse
- [ ] Bridge CLI : timeout configure (defaut 120s)
- [ ] Bridge CLI : gestion d'erreur (CLI absent, timeout, exit code non-zero)
- [ ] Bridge CLI : `isAvailable()` teste la presence du CLI avant usage
- [ ] Hooks (si actif) : fichier evenements JSONL cree dans temp
- [ ] Hooks (si actif) : watcher fs.watch fonctionne sans fuite memoire
- [ ] MCP (si actif) : serveur demarre et repond aux outils
- [ ] Secrets : cles API dans `SecretStorage`, pas dans settings
- [ ] Restricted Mode : chat et CLI desactives quand `!isTrusted`

## 6. Commandes VS Code

- [ ] `agentVisual.start` : demarre l'agent (avatar anime)
- [ ] `agentVisual.stop` : arrete l'agent (avatar masque ou grise)
- [ ] `agentVisual.pause` : gele l'animation (agent visible mais statique)
- [ ] `agentVisual.changeAvatar` : QuickPick avec liste d'avatars
- [ ] `agentVisual.setSpeed` : QuickPick 0.5x / 1x / 1.5x / 2x
- [ ] `agentVisual.toggleFocus` : desactive animations non essentielles
- [ ] `agentVisual.openPanel` : ouvre le WebviewPanel dans l'editeur
- [ ] Toutes les commandes dans la palette (Ctrl+Shift+P)
- [ ] Boutons dans la barre de titre de la vue sidebar

## 7. Performance

- [ ] Animation : pas de fuite memoire (verifier dans DevTools > Memory)
- [ ] `retainContextWhenHidden: false` sauf justification documentee
- [ ] Maximum 2-3 webviews simultanees
- [ ] `dispose()` appele sur toutes les ressources a la fermeture
- [ ] Pas de `setInterval` sans nettoyage
- [ ] Bridge CLI : pas de spawn trop frequent (debounce si necessaire)

## 8. Tests et debug

- [ ] Extension Development Host : `F5` lance l'extension sans erreur
- [ ] Webview Developer Tools : accessible et fonctionnel (`Ctrl+Shift+P` > "Developer: Open Webview Developer Tools")
- [ ] Console webview : pas d'erreurs JS au demarrage
- [ ] Console extension host : pas d'erreurs TypeScript au demarrage
- [ ] Test unitaire : au moins 1 test pour `AgentStateManager`
- [ ] Test integration : ouverture de la sidebar sans crash
- [ ] Test sur Windows, macOS, et Linux (ou au moins 2 sur 3)

## 9. Packaging et distribution

- [ ] `vsce package` produit un `.vsix` sans erreur
- [ ] `.vsixmanifest` : permissions minimales
- [ ] README : description, screenshots, instructions d'installation
- [ ] CHANGELOG : version initiale documentee
- [ ] `.vscodeignore` : exclut `src/`, `node_modules/`, fichiers de dev
- [ ] Taille du package < 5 MB (idealement < 2 MB)
- [ ] Icone 128x128 pour le Marketplace (si publication)

## 10. Securite finale

- [ ] Audit CSP : aucune directive permissive
- [ ] Audit messages : whitelist + validation schema
- [ ] Audit secrets : grep pour `apiKey`, `token`, `password` dans le code — rien en clair
- [ ] Audit reseau : `connect-src 'none'` dans la CSP
- [ ] Audit deps : `npm audit` sans vulnerabilites critiques
- [ ] Audit Workspace Trust : fonctionnalites sensibles protegees
