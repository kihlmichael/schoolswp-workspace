# Procédure de push des mu-plugins vers schoolswp.com

> Séquence canonique pour pousser un mu-plugin PHP depuis ce dossier vers le répertoire mu-plugins sur schoolswp.com (prod). Ancrée sur le MCP Novamira et les patterns mémoires validés. Toujours suivre cette procédure avant tout push prod.

## Pourquoi cette procédure

schoolswp.com tourne sur EasyHoster derrière openresty avec un WAF Imunify qui inspecte le body des requêtes PHP. Le push direct vers le répertoire mu-plugins via write-file brut est rejeté. Il faut un détour par une sandbox plus base64.

De plus, OPcache cache les PHP files. Une copy sans invalidation égale code source mis à jour mais ancien bytecode toujours en mémoire, donc bug obstiné.

Enfin, un doublon sandbox plus mu-plugins du même fichier après copy égale Cannot redeclare function au prochain reload PHP.

## Séquence canonique (5 étapes)

### 1. Préparer le base64 local

Encoder le fichier PHP en base64 dans un fichier .b64.tmp colocalisé. Le fichier .b64.tmp reste local, ne pas le commit dans git (gitignored).

Exemple manuel via PowerShell :

    [Convert]::ToBase64String([System.IO.File]::ReadAllBytes("schoolswp-affiliate-cloaks.php")) > schoolswp-affiliate-cloaks.b64.tmp

Calcul du SHA-256 local pour comparaison post-push :

    Get-FileHash schoolswp-affiliate-cloaks.php -Algorithm SHA256

### 2. Push vers sandbox via Novamira write-file

Utiliser l'ability `novamira/write-file`. Cible : `wp-content/novamira-sandbox/<plugin-slug>.b64.txt`.

**Important** : la sandbox Novamira est `wp-content/novamira-sandbox/`, créée et gérée automatiquement par le plugin Novamira. Pour les fichiers PHP, c'est la SEULE destination autorisée par `write-file`. Pour un fichier en base64 (extension .txt), n'importe quel chemin sous ABSPATH fonctionne, mais on utilise `novamira-sandbox/` par convention.

Le contenu envoyé est le base64 du fichier PHP, pas le PHP brut (extension .txt = non-PHP).

Si le fichier dépasse 12 000 caractères, chunker en plusieurs write-file successifs puis concaténer côté serveur via Novamira execute-php (cf. mémoire reference_novamira_large_content_push).

### 3. Vérifier le SHA-256 côté serveur

Avant la copy, comparer le hash serveur au hash local. Via Novamira execute-php, lancer un md5_file ou hash_file sur le contenu décodé du fichier sandbox txt.

Si mismatch : abort. Investiguer (corruption transport, encoding, chunk perdu) avant de continuer.

### 4. Copy plus OPcache invalidate

Via Novamira execute-php, en une seule transaction PHP :

1. Lire le contenu sandbox, décoder le base64.
2. Écrire le résultat dans le répertoire mu-plugins avec le nom final .php.
3. Appeler opcache_invalidate sur le chemin destination si la fonction existe.
4. Appeler opcache_reset si la fonction existe (défense en profondeur).
5. Supprimer le fichier sandbox via unlink. **Étape critique** : sans cette suppression, un autoload futur de la sandbox plus du mu-plugins déclenche Cannot redeclare function (cf. mémoire feedback_novamira_sandbox_doublon_after_copy).

### 5. Test post-deploy

Trois vérifs minimum :

1. Status 200 sur la home schoolswp.com (curl -I). Si 500 ou 503, rollback immédiat.
2. Vérifier que la fonction principale du mu-plugin est active. Exemple pour affiliate-cloaks : curl -I sur l'URL cloakée doit retourner 302 plus header Location vers la destination affiliée.
3. Pour les mu-plugins qui injectent du JSON-LD : curl la page concernée, grep le bloc application slash ld plus json, vérifier qu'il est présent et bien formé. Optionnel : passer la sortie dans search.google.com slash test slash rich-results.

## Rollback

Si le test post-deploy échoue :

- **Plan A** : restaurer la version précédente depuis git via Novamira (read-file de la version dans .bak local, puis re-push via la séquence 1 à 4).
- **Plan B** : Novamira execute-php pour supprimer le mu-plugin (unlink le chemin dans mu-plugins, puis opcache_reset) puis investiguer en local.

Toujours préférer le plan A. Le plan B laisse le site sans la fonctionnalité.

## Notification post-deploy

Recommandé après tout push prod réussi : push une ligne dans Discord channel alerts via le webhook schoolsWP-Routines (cf. mémoire reference_discord_webhook_routines).

**Script réutilisable** : [notify-discord-deploy.ps1](notify-discord-deploy.ps1)

Usage :

    .\notify-discord-deploy.ps1 -PluginName "schoolswp-affiliate-cloaks" -Version "1.1.1" -PhpFile "schoolswp-affiliate-cloaks.php"

Le script calcule le SHA-256 (12 premiers chars) et pousse une ligne formatée dans le channel #alerts. Pré-requis : variable d'env DISCORD_SCHOOLSWP_ROUTINES_URL définie (HKCU\Environment) ou param -WebhookUrl explicite.

Exemple format push :

> :ship: mu-plugin pushed : schoolswp-affiliate-cloaks v1.1.1
> SHA-256 (12) : abc123def456
> Timestamp : 2026-05-25 14:32
> Status : success

Cette notif facilite le tracking et le diff entre déploiements.

## Anti-patterns à éviter

- Pousser directement vers mu-plugins slash plugin point php via write-file. WAF Imunify bloque le body PHP.
- Skip la vérification SHA-256 entre sandbox et copy. Risque corruption silencieuse.
- Skip l'unlink du sandbox après copy. Garantit un Cannot redeclare au prochain reload.
- Skip opcache_invalidate. Code source à jour mais bytecode obsolète égale bug obstiné qui résiste au refresh.
- Pousser un .b64.tmp dans git. Ces fichiers sont locaux, gitignored par convention.
- Push sans backup local préalable. Préparer un .bak ou s'assurer que le commit précédent est accessible.
- Considérer un User OK comme deployed sans curl prod (cf. mémoire feedback_verify_prod_after_user_ok).

## Audit pré-push

Avant chaque push, lancer le skill production-audit-schoolswp sur le fichier cible (surface 1 mu-plugin PHP). Voir le SKILL.md dans .claude slash skills slash dev slash production-audit-schoolswp.

Le skill check :

- Lint PHP, secrets hardcode, hooks WP, route REST nonce
- OPcache invalidate prévu
- SHA-256 prévu
- Doublon sandbox géré
- Rollback path explicite
- Test post-deploy planifié
- Pixel-perfect wptexturize si JSON-LD
- Logging conditionné WP_DEBUG (v1.1)
- Whitelist langue si multi-langue (v1.1)

Score minimum souhaité avant push : 85 sur 100 (bande Prêt). En dessous, corriger les blockers d'abord.

## Mémoires de référence

- reference_mu_plugin_push_pattern_sandbox : pattern complet sandbox plus copy plus OPcache
- feedback_novamira_sandbox_doublon_after_copy : pourquoi l'unlink sandbox est critique
- reference_imunify_waf_php_body_inspect : pourquoi extension txt obligatoire en sandbox
- reference_mu_plugin_in_place_patch : alternative str_replace via execute-php pour modifs ponctuelles (5 modifs max)
- feedback_mu_plugin_opcache_hygiene : hygiène opcache invalidate plus reset
- reference_novamira_large_content_push : chunking b64 si fichier dépasse 12 000 chars
- reference_kadence_wptexturize_pixel_perfect : apostrophes typographiques en JSON-LD
- feedback_verify_prod_after_user_ok : toujours re-vérifier prod après User OK
- reference_discord_webhook_routines : webhook Discord pour notif post-deploy

## Mu-plugins actuellement gérés par cette procédure

| Fichier | Version | Rôle |
| --- | --- | --- |
| schoolswp-llms-txt.php | 1.0.0 | Override llms.txt Rank Math (UTF-8 propre, articles par pilier, pages clés, attribution) via hook rank_math/llms_txt/before_output |
| schoolswp-affiliate-cloaks.php | 1.1.1 | Cloaks marque plus affiliés (logging WP_DEBUG) |
| schoolswp-home-schema.php | 1.0.7 | JSON-LD enrichi home (FR plus EN plus DE, logging WP_DEBUG + garde-fous) |
| schoolswp-ai-summary.php | (voir source) | 5 pills LLM sur articles |
| schoolswp-ai-summary-langs.php | (voir source) | Variantes langue AI summary |
| schoolswp-list-cleanup-cron.php | (voir source) | Cron cleanup listes |
| schoolswp-home-script-cleanup.php | (voir source) | Cleanup scripts home |

Ajouter une ligne à ce tableau lors de la création d'un nouveau mu-plugin.
