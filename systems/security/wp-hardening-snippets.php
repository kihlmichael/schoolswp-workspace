<?php
/**
 * schoolsWP — Security hardening snippets
 *
 * Add to theme functions.php or as mu-plugin (wp-content/mu-plugins/schoolswp-hardening.php)
 *
 * @see systems/security/pentest-report.md — Findings F9
 */

/**
 * F9 — Disable user enumeration via REST API
 * Blocks /wp-json/wp/v2/users for unauthenticated requests.
 */
add_filter('rest_endpoints', function ($endpoints) {
    if (!is_user_logged_in()) {
        if (isset($endpoints['/wp/v2/users'])) {
            unset($endpoints['/wp/v2/users']);
        }
        if (isset($endpoints['/wp/v2/users/(?P<id>[\d]+)'])) {
            unset($endpoints['/wp/v2/users/(?P<id>[\d]+)']);
        }
    }
    return $endpoints;
});
