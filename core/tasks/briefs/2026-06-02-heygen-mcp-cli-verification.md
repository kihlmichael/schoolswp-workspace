# Brief fin de session — Vérification MCP + CLI HeyGen — 2026-06-02

Session de diagnostic (read-only sur la prod, aucune génération vidéo, aucune dépense de crédit). Objectif : confirmer que la stack HeyGen est fonctionnelle dans le workflow.

## Demande initiale

« Rassure-moi : est-ce que le MCP HeyGen est fonctionnel dans mon workflow ? » puis « Et le CLI ? ».

## Verdict

| Surface        | Statut                                       | Détail                                                |
| -------------- | -------------------------------------------- | ----------------------------------------------------- |
| **MCP HeyGen** | ✅ Pleinement fonctionnel                    | OAuth valide, `get_current_user` répond               |
| **CLI HeyGen** | ⚠️ Installé + authentifié, mais wallet à sec | Binaire OK, auth persistée, mais 0,00 $ de crédit API |

## 1. MCP — la voie de production

- Endpoint `https://mcp.heygen.com/mcp/v1/`, auth OAuth (pas de clé API).
- Compte : contact@michaelkihl.fr.
- `billing_type: subscription`, plan **Creator**.
- **542 crédits premium** (reset 2027-05-29) + **100 crédits add-on**.
- Tous les outils `mcp__heygen__*` exposés en session (video-agent, lipsync, translation, avatars, voix, +extras `clone_voice`, `create_video_from_avatar_shots`, `list_brand_kits`).
- **C'est la voie à utiliser pour produire** — elle a les crédits, elle est connectée.

## 2. CLI — prêt mais en standby

- Binaire : `C:\Users\conta\.local\bin\heygen.exe`, **PE32+ Windows natif**, v0.0.7 (daté 2026-04-28).
  - La doc upstream dit « Windows coming soon, WSL recommended » → **faux**, build native déjà présente, tourne directement.
  - `~/.local/bin` **pas dans le PATH** → appeler le chemin complet (même cas que ExifTool).
- **Auth rendue persistante** cette session :
  - Commande : `$env:HEYGEN_API_KEY | & "$env:USERPROFILE\.local\bin\heygen.exe" auth login`
  - Écrit `~/.heygen/credentials` → indépendant du shell, visible par `.bat`/n8n/futures sessions.
  - Vérifié depuis un process séparé : `auth status` → `EXIT 0`.
  - (La variable d'env seule est éphémère, current-shell-only → invisible aux autres process.)
- **Point critique — billing étanche** : le CLI utilise la **clé API → `billing_type: wallet` = 0,00 $**. La clé API **ne tape PAS** dans les 542 crédits de l'abonnement. Les deux surfaces sont séparées sur le même compte.
  - Conséquence : le CLI est « prêt » mais **ne rendra aucune vidéo** tant que le wallet API n'est pas crédité (dépense distincte de l'abonnement Creator).

## Décision actée

- **Produire des vidéos → MCP** (pattern validé 2026-05-06 : ElevenLabs TTS → audioUrl HTTPS public → `create_video_from_avatar` sur le digital twin de Michaël).
- **CLI → standby.** Authentifié, pas désactivé. À réactiver seulement si besoin de headless hors Claude Code (scripts, n8n, CI) ET budget wallet API dédié.

## Traces

- Mémoire `project_heygen_install.md` mise à jour (section CLI 2026-06-02 + correction de l'ancienne note « pas de CLI Windows »).
- Entrée `LOG.md` 2026-06-02 (update).

## Reste à faire (si un jour le CLI devient utile)

1. Créditer le wallet API sur https://app.heygen.com/settings/api.
2. (Optionnel) Ajouter `~/.local/bin` au PATH Windows pour appeler `heygen` sans chemin complet.
3. Tester une génération CLI réelle (`video-agent create --wait`) pour valider le pipeline headless.
