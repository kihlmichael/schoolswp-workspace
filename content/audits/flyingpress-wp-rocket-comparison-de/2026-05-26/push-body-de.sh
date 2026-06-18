#!/usr/bin/env bash
# Script-helper pour pousser le body DE refondu au retour Novamira.
# Mode d'emploi :
#   - Ouvrir une session Claude Code avec accès Novamira MCP
#   - Dire : "Exécute push-body-de.sh pour finir le P0 DE FlyingPress vs WP Rocket"
#   - L'agent récupère le body, l'encode, le pousse via novamira/execute-php, purge le cache, vérifie.
#
# Ce fichier est un mémo procédural, PAS un script bash exécutable.
# Le push réel se fait via le MCP Novamira (execute-php), pas via PowerShell ou bash local.

set -euo pipefail

cat <<'EOF'
═══════════════════════════════════════════════════════════════
PROCEDURE PUSH BODY DE — flyingpress-wp-rocket-comparison-de
═══════════════════════════════════════════════════════════════

CONTEXTE :
- Post ID : 343161
- Permalink : https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/
- Body local : content/audits/flyingpress-wp-rocket-comparison-de/2026-05-26/body-de-ready-to-push.html
- Etat pre-push : metas DE patchees, image patchee, body FR (en mauvaise langue).

ETAPES :

1. Lire le body local (Read) :
   d:\VS Code\CLAUDE CODE\projects\schoolswp\content\audits\flyingpress-wp-rocket-comparison-de\2026-05-26\body-de-ready-to-push.html

2. Encoder en base64 (pour eviter problemes d'echappement PHP) :
   $body_b64 = base64_encode(file contents)

3. Pousser via novamira/execute-php :

   global $wpdb;
   $body = base64_decode('<B64_CONTENT>');
   $r = $wpdb->update($wpdb->posts, [
       'post_content' => $body,
       'post_modified' => current_time('mysql'),
       'post_modified_gmt' => current_time('mysql', true),
   ], ['ID' => 343161]);
   clean_post_cache(343161);

   // Verify
   $post_after = get_post(343161);
   $content = $post_after->post_content;
   $lang_de = 0; $lang_fr = 0;
   foreach (['der ', 'die ', 'das ', 'und ', 'mit ', 'ist ', 'sind ', 'fuer ', 'auf ', 'eine ', 'einen ', 'sich '] as $m) {
       $lang_de += substr_count(mb_strtolower(strip_tags($content)), $m);
   }
   foreach (['le ', 'la ', 'les ', 'des ', 'pour ', 'avec ', 'mais ', 'tu ', 'ton ', 'ta ', 'voici '] as $m) {
       $lang_fr += substr_count(mb_strtolower(strip_tags($content)), $m);
   }
   return [
       'wpdb_result' => $r,
       'sha_after' => hash('sha256', $content),
       'lang_de' => $lang_de,
       'lang_fr' => $lang_fr,
       'em_dash_count' => mb_substr_count($content, "\xE2\x80\x94"),
       'en_dash_count' => mb_substr_count($content, "\xE2\x80\x93"),
       '2024_count' => substr_count($content, '2024'),
       '2025_count' => substr_count($content, '2025'),
       'kadence_btn_count' => preg_match_all('/wp:kadence\/advancedbtn/', $content),
   ];

   ATTENDU :
   - wpdb_result = 1
   - lang_de >> lang_fr (renversement du verdict)
   - em_dash + en_dash = 0
   - 2024 + 2025 = 0 (sauf "Stand Maerz 2026" qui ne contient pas ces tokens)
   - kadence_btn_count = 2

4. Cache purges (execute-php) :

   $permalink = get_permalink(343161);
   do_action('flying_press_purge_url', $permalink);
   do_action('flying_press_purge_post', 343161);
   do_action('fp_purge_url', $permalink);

   // Disk delete
   $cache_dir = '/home/schoolsw/public_html/wp-content/cache/flying-press/schoolswp.com/de/vergleich-flyingpress-wp-rocket';
   foreach (glob($cache_dir . '/*') as $f) {
       if (is_file($f)) @unlink($f);
   }

5. Round-trip prod :

   $resp = wp_remote_get($permalink . '?nocache=' . time(), ['timeout' => 20]);
   $body = wp_remote_retrieve_body($resp);
   // Verify presence d'un marqueur DE specifique
   $has_neue_heading = strpos($body, 'Optimale Einstellungen') !== false;
   $has_french_residual = strpos($body, 'Choisis FlyingPress') !== false;

6. GSC :
   - Inspect URL de la page
   - Request Indexing
   - Note : recrawl typique sous 24-72h, SERP devrait refleter le DE natif d'ici 2026-05-29

7. Update state-after.json (passer phase de "P0_partial" a "P0_complete")
   et journaliser dans audit.md section 15.

═══════════════════════════════════════════════════════════════
EOF
