<?php
/**
 * schoolsWP — Security Snippets
 *
 * A ajouter dans le thème enfant Kadence : functions.php
 * Ou via un plugin MU : wp-content/mu-plugins/schoolswp-security.php
 *
 * Généré suite au pentest du 2026-03-15.
 * Findings couverts : F1 (user enumeration), F2 (plugin fingerprinting), F6 (app passwords)
 */

// =============================================================================
// F1 — Bloquer l'accès non-authentifié aux endpoints /wp-json/wp/v2/users
// Sévérité : HIGH — User enumeration username admin
// =============================================================================
add_filter('rest_endpoints', function (array $endpoints): array {
    if (is_user_logged_in()) {
        return $endpoints;
    }
    unset($endpoints['/wp/v2/users']);
    unset($endpoints['/wp/v2/users/(?P<id>[\d]+)']);
    return $endpoints;
});

// =============================================================================
// F2 — Masquer les namespaces et routes REST API pour les non-connectés
// Sévérité : MEDIUM — Plugin fingerprinting (50+ namespaces exposés)
// =============================================================================
add_filter('rest_index_response', function (WP_REST_Response $response): WP_REST_Response {
    if (is_user_logged_in()) {
        return $response;
    }
    $data = $response->get_data();
    unset($data['namespaces']);
    unset($data['routes']);
    $response->set_data($data);
    return $response;
});

// =============================================================================
// F6 — Désactiver Application Passwords si non utilisé
// Sévérité : INFO — Surface d'attaque inutile
// Décommenter si les Application Passwords ne sont pas utilisés sur ce site.
// =============================================================================
// add_filter('wp_is_application_passwords_available', '__return_false');

// =============================================================================
// BONUS — Empêcher l'énumération des utilisateurs via l'URL ?author=N
// (déjà bloqué sur le site mais double sécurité)
// =============================================================================
add_action('template_redirect', function (): void {
    if (is_author() && !is_user_logged_in()) {
        wp_redirect(home_url(), 301);
        exit;
    }
});

// =============================================================================
// BONUS — Supprimer la balise generator WordPress du <head>
// =============================================================================
remove_action('wp_head', 'wp_generator');
