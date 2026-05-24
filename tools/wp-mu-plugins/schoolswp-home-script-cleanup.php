<?php
/**
 * Plugin Name: schoolsWP Home Script Cleanup
 * Description: Dequeue ciblé sur la home (FR/EN/DE) des assets frontend Tutor LMS qui sont chargés inutilement (la home n'affiche aucun cours, leçon, quiz, dashboard étudiant). Conservatif : ne touche QUE la home, ne touche QUE Tutor. Si la page courante est une page Tutor (cours, leçon, dashboard), aucun dequeue n'est fait.
 * Version: 1.0.0
 * Author: Michael KIHL
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Détecte si on est sur la home page (FR par défaut, EN ou DE Polylang).
 */
function schoolswp_home_cleanup_is_home() {
    if (is_admin() || (defined('DOING_AJAX') && DOING_AJAX) || (defined('REST_REQUEST') && REST_REQUEST)) {
        return false;
    }
    if (is_front_page()) {
        return true;
    }
    // Fallback Polylang : compare l'URL courante aux 3 home URLs connues.
    if (function_exists('pll_current_language')) {
        global $wp;
        $request_path = isset($wp->request) ? trim((string) $wp->request, '/') : '';
        if ($request_path === '' || in_array($request_path, ['en', 'de', 'fr'], true)) {
            return true;
        }
    }
    return false;
}

/**
 * Détecte si la page courante est une page Tutor LMS (cours, leçon, quiz, dashboard).
 * Sécurité : si Tutor estime que c'est sa page, on ne dequeue PAS ses assets.
 */
function schoolswp_home_cleanup_is_tutor_page() {
    if (function_exists('tutor_utils')) {
        $utils = tutor_utils();
        if (is_object($utils) && method_exists($utils, 'is_tutor_page')) {
            return (bool) $utils->is_tutor_page();
        }
    }
    // Fallback : test sur les post_type Tutor
    $tutor_post_types = ['courses', 'lesson', 'tutor_quiz', 'tutor_assignments', 'tutor_enrolled'];
    foreach ($tutor_post_types as $pt) {
        if (is_singular($pt) || is_post_type_archive($pt)) {
            return true;
        }
    }
    return false;
}

/**
 * Handles Tutor frontend à dequeue sur la home.
 * Filtrable via `schoolswp_home_cleanup_tutor_scripts` et `schoolswp_home_cleanup_tutor_styles`.
 */
function schoolswp_home_cleanup_tutor_scripts() {
    return apply_filters('schoolswp_home_cleanup_tutor_scripts', [
        'tutor-script',
        'tutor-social-share',
        'tutor-frontend',
        'tutor-prism-js',
        'tutor-prism-script',
        'tutor-pro-front',
    ]);
}

function schoolswp_home_cleanup_tutor_styles() {
    return apply_filters('schoolswp_home_cleanup_tutor_styles', [
        'tutor-icon',
        'tutor',
        'tutor-frontend',
        'tutor-prism-css',
        'tutor-pro-front',
        'kadence-tutorlms',
    ]);
}

/**
 * Dequeue handler : tourne en priorité 100 pour passer APRÈS les enqueue des plugins (priorité 10 par défaut).
 * Sinon Tutor re-enqueue après nous.
 */
add_action('wp_enqueue_scripts', 'schoolswp_home_cleanup_dequeue', 100);

function schoolswp_home_cleanup_dequeue() {
    if (!schoolswp_home_cleanup_is_home()) {
        return;
    }
    if (schoolswp_home_cleanup_is_tutor_page()) {
        // Garde-fou : si Tutor pense être chez lui, on respecte
        return;
    }

    foreach (schoolswp_home_cleanup_tutor_scripts() as $handle) {
        wp_dequeue_script($handle);
        wp_deregister_script($handle);
    }
    foreach (schoolswp_home_cleanup_tutor_styles() as $handle) {
        wp_dequeue_style($handle);
        wp_deregister_style($handle);
    }
}

/**
 * Belt-and-suspenders : second passage tard dans wp_print_scripts/wp_print_styles
 * au cas où un plugin enqueue Tutor en wp_footer.
 */
add_action('wp_print_scripts', 'schoolswp_home_cleanup_dequeue_late', 100);
add_action('wp_print_styles', 'schoolswp_home_cleanup_dequeue_late', 100);

function schoolswp_home_cleanup_dequeue_late() {
    if (!schoolswp_home_cleanup_is_home() || schoolswp_home_cleanup_is_tutor_page()) {
        return;
    }
    foreach (schoolswp_home_cleanup_tutor_scripts() as $handle) {
        wp_dequeue_script($handle);
    }
    foreach (schoolswp_home_cleanup_tutor_styles() as $handle) {
        wp_dequeue_style($handle);
    }
}
