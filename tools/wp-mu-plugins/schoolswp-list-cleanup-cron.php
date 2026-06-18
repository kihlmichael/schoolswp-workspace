<?php
/**
 * Plugin Name: schoolsWP List Cleanup Cron
 * Description: Tague automatiquement les contacts FluentCRM inactifs depuis N jours avec le tag `abonne_inactif`, ce qui declenche le funnel de reengagement #29. Mu-plugin = toujours actif, jamais desactivable via UI.
 * Version: 1.0.0
 * Author: schoolsWP
 */

if (!defined('ABSPATH')) {
    exit;
}

// =========================================================================
// CONFIG
// =========================================================================

// Mode securite: true = log les candidats sans tagger; false = tagging reel.
// A basculer manuellement apres validation du premier dry-run.
const SCHOOLSWP_LCC_DRY_RUN = false;

// IDs subscriber FluentCRM a EXCLURE definitivement du nettoyage automatique
// (famille, partenaires, comptes test). Plus fort qu'un tag protection.
const SCHOOLSWP_LCC_EXCLUDE_SUBSCRIBER_IDS = [
    488, // kidkihl+vanessa@gmail.com (famille)
];

// Nombre de jours d'inactivite a partir desquels un contact est considere inactif.
const SCHOOLSWP_LCC_INACTIVE_DAYS = 180;

// Plafond par execution (anti-blast). 22 inactifs actuels -> 2 jours pour les vider.
const SCHOOLSWP_LCC_BATCH_LIMIT = 20;

// Tag a appliquer (declencheur du funnel #29).
const SCHOOLSWP_LCC_INACTIVE_TAG_ID = 446; // abonne_inactif

// Identifiant de la tache cron WP.
const SCHOOLSWP_LCC_HOOK = 'schoolswp_list_cleanup_daily';

// Tags qui IMMUNISENT un contact contre le marquage inactif.
// Toujours sur-proteger plutot que sous-proteger.
const SCHOOLSWP_LCC_PROTECT_TAG_IDS = [
    449, // client_formations
    450, // client_prestations
    451, // client_produits
    452, // client_vip
    454, // etudiant_actif
    456, // etudiant_formation_terminee
    460, // fluentcart_commande_validee
    463, // fluentcart_upsell_accepte
    771, // comportement_engaged (sortie YES du funnel #29)
    772, // novamira_mirror_acheteur
    773, // novamira_mirror_audit_acheteur
    774, // novamira_mirror_bump_acheteur
    775, // abonne_reengagement_echoue (deja passe par le funnel)
];

// =========================================================================
// SCHEDULER
// =========================================================================

add_action('init', 'schoolswp_lcc_maybe_schedule');
function schoolswp_lcc_maybe_schedule()
{
    if (!wp_next_scheduled(SCHOOLSWP_LCC_HOOK)) {
        wp_schedule_event(time() + 60, 'daily', SCHOOLSWP_LCC_HOOK);
    }
}

add_action(SCHOOLSWP_LCC_HOOK, 'schoolswp_lcc_run');

// =========================================================================
// LOGGER
// =========================================================================

function schoolswp_lcc_log($message)
{
    $upload = wp_upload_dir();
    $dir = trailingslashit($upload['basedir']) . 'schoolswp-logs';
    if (!is_dir($dir)) {
        wp_mkdir_p($dir);
    }
    $line = '[' . gmdate('c') . '] ' . $message . PHP_EOL;
    @file_put_contents($dir . '/list-cleanup.log', $line, FILE_APPEND);
}

// =========================================================================
// CORE
// =========================================================================

function schoolswp_lcc_run()
{
    global $wpdb;

    if (!class_exists('\\FluentCrm\\App\\Models\\Subscriber')) {
        schoolswp_lcc_log('SKIP - FluentCRM not loaded');
        return;
    }

    $threshold = gmdate('Y-m-d H:i:s', strtotime('-' . SCHOOLSWP_LCC_INACTIVE_DAYS . ' days'));

    $protect = array_merge(SCHOOLSWP_LCC_PROTECT_TAG_IDS, [SCHOOLSWP_LCC_INACTIVE_TAG_ID]);
    $protect_csv = implode(',', array_map('intval', $protect));

    $exclude_ids = SCHOOLSWP_LCC_EXCLUDE_SUBSCRIBER_IDS;
    $exclude_clause = '';
    if (!empty($exclude_ids)) {
        $exclude_csv = implode(',', array_map('intval', $exclude_ids));
        $exclude_clause = " AND s.id NOT IN ($exclude_csv) ";
    }

    $sql = "
        SELECT s.id, s.email, s.last_activity
        FROM {$wpdb->prefix}fc_subscribers s
        WHERE s.status = 'subscribed'
          AND (s.last_activity IS NULL OR s.last_activity < %s)
          $exclude_clause
          AND s.id NOT IN (
              SELECT sp.subscriber_id
              FROM {$wpdb->prefix}fc_subscriber_pivot sp
              WHERE sp.object_type = 'FluentCrm\\\\App\\\\Models\\\\Tag'
                AND sp.object_id IN ($protect_csv)
          )
        ORDER BY (s.last_activity IS NULL) DESC, s.last_activity ASC
        LIMIT %d
    ";

    $contacts = $wpdb->get_results(
        $wpdb->prepare($sql, $threshold, SCHOOLSWP_LCC_BATCH_LIMIT),
        ARRAY_A
    );
    $count = count($contacts);

    schoolswp_lcc_log(sprintf(
        'RUN start - threshold=%s dry_run=%s batch_limit=%d candidates=%d',
        $threshold,
        SCHOOLSWP_LCC_DRY_RUN ? 'YES' : 'NO',
        SCHOOLSWP_LCC_BATCH_LIMIT,
        $count
    ));

    if ($count === 0) {
        schoolswp_lcc_log('RUN end - no candidates');
        return;
    }

    $tagged = 0;
    foreach ($contacts as $c) {
        schoolswp_lcc_log(sprintf(
            '  candidate id=%d email=%s last_activity=%s',
            $c['id'],
            $c['email'],
            $c['last_activity'] ?: 'NULL'
        ));

        if (SCHOOLSWP_LCC_DRY_RUN) {
            continue;
        }

        $sub = \FluentCrm\App\Models\Subscriber::find($c['id']);
        if ($sub) {
            $sub->attachTags([SCHOOLSWP_LCC_INACTIVE_TAG_ID]);
            $tagged++;
        }
    }

    schoolswp_lcc_log(sprintf(
        'RUN end - %s; candidates=%d tagged=%d',
        SCHOOLSWP_LCC_DRY_RUN ? 'DRY RUN (no DB write)' : 'LIVE',
        $count,
        $tagged
    ));
}

// =========================================================================
// MANUAL TRIGGER (admin-only AJAX) - for testing without waiting for cron
// Usage: visit /wp-admin/admin-ajax.php?action=schoolswp_lcc_now
// =========================================================================

add_action('wp_ajax_schoolswp_lcc_now', function () {
    if (!current_user_can('manage_options')) {
        wp_die('forbidden', 403);
    }
    schoolswp_lcc_run();
    echo "OK - see wp-content/uploads/schoolswp-logs/list-cleanup.log";
    wp_die();
});
