<?php
/**
 * Plugin Name: schoolsWP Affiliate Cloaks
 * Description: Cloaks marque + affiliés (schoolswp.com/<slug>/ -> destination tierce). Couvre profils sociaux Michael KIHL + partenaires affiliés. Single source of truth dans la fonction schoolswp_affiliate_cloaks().
 * Version: 1.1.1
 * Author: Michaël KIHL
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Map des cloaks actifs.
 * Clé = slug case-insensitive (sans slash de début ni fin), valeur = URL destination.
 * Le préfixe langue Polylang (fr/en/de) est strippé avant matching.
 *
 * 2 familles :
 *   - Partenaires affiliés (ref/aff dans la querystring)
 *   - Profils sociaux Michael KIHL (cohérence URL marque + résilience aux changements d'URL natives)
 */
function schoolswp_affiliate_cloaks() {
    return [
        // Partenaires affiliés
        'novamira'      => 'https://www.dynamic.ooo?ref=734',
        'rank-math'     => 'https://rankmath.com/?ref=contact1975',
        'booknetic'     => 'https://www.booknetic.com?ref=aajfwp',

        // Profils sociaux Michael KIHL (cloaked pour cohérence marque + traçabilité)
        'linkedin'      => 'https://www.linkedin.com/in/michaelkihl/',
        'x'             => 'https://x.com/MichaelKihl',
        'feed-youtube'  => 'https://www.youtube.com/@MichaelKihl?sub_confirmation=1',
    ];
}

/**
 * Code HTTP utilisé pour les redirects affiliés.
 * 302 par défaut pour rester transparent SEO et faciliter la modification ultérieure sans cache navigateur agressif.
 */
function schoolswp_affiliate_cloak_status() {
    return 302;
}

add_action('init', 'schoolswp_affiliate_cloaks_handler', 1);

function schoolswp_affiliate_cloaks_handler() {
    if (is_admin() || (defined('DOING_AJAX') && DOING_AJAX) || (defined('REST_REQUEST') && REST_REQUEST)) {
        return;
    }

    $request_uri = isset($_SERVER['REQUEST_URI']) ? (string) $_SERVER['REQUEST_URI'] : '';
    if ($request_uri === '') {
        return;
    }

    $path = parse_url($request_uri, PHP_URL_PATH);
    if (!is_string($path)) {
        return;
    }

    $path = trim($path, '/');
    if ($path === '') {
        return;
    }

    // Strip Polylang language prefix (fr/, en/, de/) si présent.
    $path = preg_replace('#^(fr|en|de)/#i', '', $path);

    // Strip query / fragment éventuel et garder seulement le 1er segment pour matching exact.
    $segments = explode('/', $path);
    $first = isset($segments[0]) ? strtolower($segments[0]) : '';

    $cloaks = schoolswp_affiliate_cloaks();
    if (!isset($cloaks[$first])) {
        return;
    }

    // Match strict : exactement 1 segment (schoolswp.com/Novamira/ ou /Novamira). Sinon on laisse WP gérer.
    if (count($segments) > 1 && trim($segments[1]) !== '') {
        return;
    }

    $destination = $cloaks[$first];

    // Traçabilité WP_DEBUG uniquement (pas de log en prod par défaut)
    if (defined('WP_DEBUG') && WP_DEBUG) {
        error_log(sprintf('[schoolsWP cloak] %s -> %s', $first, $destination));
    }

    nocache_headers();
    wp_redirect($destination, schoolswp_affiliate_cloak_status());
    exit;
}
