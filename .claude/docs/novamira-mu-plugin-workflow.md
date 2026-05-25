# Workflow Novamira — pousser et patcher un mu-plugin en sécurité

Source de vérité pour pousser, patcher et vérifier un mu-plugin PHP sur la prod schoolswp.com via le MCP Novamira, sans risquer un site DOWN. Issu de la session du 2026-05-24/25 (incident push corrompu + récupération).

## TL;DR

| Cas | Méthode recommandée | Pourquoi |
| --- | --- | --- |
| Nouveau mu-plugin ou réécriture complète | Push sandbox + SHA256 verify + copy mu-plugins (workflow A ci-dessous) | Atomique, abort si corruption, backup auto |
| Patch léger (5 lignes max, ex. version bump, str fix) | str_replace in-place via execute-php (workflow B) | Zéro upload, zéro risque de corruption b64 |
| Hotfix urgent | file_get_contents + modif PHP côté serveur + file_put_contents + SHA256 check | Pas besoin de Git roundtrip |

## Contraintes Novamira / serveur

- **novamira/write-file** : les fichiers PHP ne peuvent être écrits QUE dans wp-content/novamira-sandbox/. Tout autre chemin = erreur.
- **novamira/create-upload-link** : génère une URL signée pour upload binaire via curl PUT. Limite : WAF (Imunify360) rejette tout body contenant l'ouverture PHP même en .txt → inutilisable pour des PHP files.
- **novamira/execute-php** : peut lire/écrire/copier dans tout l'arbo WP. Path absolu obligatoire. Pas de limite WAF (passe par REST authentifié).

## Workflow A — Push d'un mu-plugin complet (nouveau ou réécriture)

### Étape 1 — Préparer le fichier local

Commandes Bash :

- sha256sum tools/wp-mu-plugins/PLUGIN.php → noter le hash attendu
- base64 -w 0 tools/wp-mu-plugins/PLUGIN.php > tools/wp-mu-plugins/PLUGIN.b64.tmp
- wc -c tools/wp-mu-plugins/PLUGIN.php → noter la taille attendue

Le fichier .b64.tmp est gitignored via tools/wp-mu-plugins/*.b64.tmp (vérifié dans .gitignore).

### Étape 2 — Lire le b64 puis push sandbox

**Critique** : Read le .b64.tmp pour avoir le contenu **exact**. Ne jamais retaper le b64 manuellement dans un tool call — l'incident du 2026-05-24 (corruption 1 caractère → site DOWN) est venu d'un retape manuel.

Appel novamira/write-file avec :

- path : wp-content/novamira-sandbox/PLUGIN.php
- content : le b64 lu (passe direct, sans transformation)
- encoding : base64
- mode : overwrite

Si le bytes_written n'est pas égal à la taille locale, **abort immédiatement** : corruption détectée au stade sandbox, mu-plugins intact.

### Étape 3 — Verify SHA256, syntax check, backup, copy

Un seul execute-php atomique. Les opérations à enchaîner :

1. hash_file('sha256', sandbox_path) ; si différent du hash attendu → abort
2. php -l via shell_exec sur le sandbox ; si pas de "No syntax errors detected" → abort
3. Si mu-plugin existe → copy() vers backup .vX.Y.Z.bak
4. copy() sandbox vers mu-plugin path + chmod 0644
5. Re-hash le mu-plugin path ; si différent du hash attendu → abort
6. opcache_invalidate(mu_path, true) si la fonction existe
7. unlink() le sandbox file
8. Retourner status complet pour traçabilité

### Étape 4 — Smoke test fonctionnel

Commande Bash : curl -sS -A "Mozilla/5.0 Chrome/121" "https://schoolswp.com/FEATURE-URL" -I

Vérifier 200 / 302 / contenu attendu selon le mu-plugin.

Si FlyingPress actif : purger les URLs concernées via FlyingPress\Purge::purge_urls (array d'URLs).

## Workflow B — Patch léger in-place (5 modifications max ciblées)

Bien plus safe que ré-uploader le fichier complet quand on ne change que quelques lignes (ex. fix typo, version bump, ajout d'une entrée dans un array).

Pattern execute-php :

1. Backup : copy(mu_path, mu_path . '.vX.Y.Z.bak')
2. content = file_get_contents(mu_path)
3. Définir le tableau des replacements (needle => replacement), avec les caractères spéciaux Unicode construits via chr(0xE2) . chr(0x80) . chr(0x99) pour U+2019 par exemple
4. Boucle foreach avec str_replace($needle, $repl, $new, $count) pour compter chaque substitution
5. file_put_contents(mu_path, new_content)
6. hash_file('sha256', mu_path) → vérifier == sha256 local attendu
7. php -l via shell_exec → vérifier "No syntax errors detected"
8. opcache_invalidate(mu_path, true)
9. Retourner counts + sha_match + syntax pour traçabilité

**Avantages** :

- Aucun upload, donc zéro risque de corruption b64
- Aucune restriction WAF (execute-php passe par REST authentifié)
- Backup auto avant patch, rollback simple via mv .bak
- SHA256 match = preuve que la prod = source locale

## Récupération après site DOWN

Si un push corrompu casse WordPress (PHP fatal au boot, site renvoie 500) :

1. **execute-php / write-file ne marchent plus** (eux aussi passent par le boot WP) → tu es bloqué côté MCP
2. **Seule solution** : renommer manuellement le mu-plugin fautif en .disabled via cPanel File Manager ou SFTP :
   - cPanel → File Manager → public_html/wp-content/mu-plugins/
   - Rename PLUGIN.php en PLUGIN.php.disabled
   - Site UP immédiatement (les mu-plugins sont scannés à chaque request)
3. Une fois UP, refaire le push proprement via Workflow A ou B

## Bonnes pratiques

- **Toujours bumper la version** du mu-plugin à chaque modif (header Version X.Y.Z) — facilite la traçabilité et identifie la version en prod via get_file_data() ou grep
- **SHA256 local et SHA256 prod doivent matcher byte-perfect** — ne JAMAIS continuer si mismatch
- **Backup .bak versionné** avant tout patch destructif — rollback en 1 commande
- **OPcache invalidate** obligatoire après chaque modif, sinon l'ancienne version reste en mémoire jusqu'à reload Apache ou PHP-FPM
- **FlyingPress purge** après modif si l'output frontend change (head schema, body content, etc.)
- **Smoke test fonctionnel** systématique après push — ne JAMAIS marquer "deployed" sans curl/HEAD prod

## Anti-patterns connus

- Retaper un b64 long (15 KB et plus) dans un tool call execute-php → corruption silencieuse quasi-garantie
- Push complet pour 2 lignes modifiées → préférer in-place str_replace
- wp_unslash() après lecture wp_options Kadence → casse les antislashs des blocs (cf. mémoire feedback_wp_update_post_unslash_kadence)
- Tenter create-upload-link pour un PHP en .txt → WAF inspecte le body, rejet sur l'ouverture PHP
- Modifier .mcp.json pour flipper un safety guard MCP → classifier auto-mode refuse (cf. mémoire reference_auto_mode_classifier_destructive_guard)

## Mémoires liées

- reference_mu_plugin_push_pattern_sandbox.md
- feedback_verify_prod_after_user_ok.md
- feedback_mu_plugin_opcache_hygiene.md
- reference_novamira_mcp_capabilities.md
- reference_novamira_large_content_push.md
- reference_auto_mode_classifier_destructive_guard.md
