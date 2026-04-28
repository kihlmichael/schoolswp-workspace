<?php
/**
 * Plugin Name: Disable SecuPress DCTS Frontend JS
 * Description: Workaround for ReferenceError "element is not defined" in secupress-antispam.min.js. The DCTS (Disable Comment Submission Timer) module of SecuPress Pro ships JS that references an undeclared `element` variable, crashing on every page with a comment form. This mu-plugin dequeues that script on the public frontend. Remove this file once SecuPress fixes the bug upstream.
 * Author: schoolsWP
 * Version: 1.0
 */

if (!defined('ABSPATH')) {
    exit;
}

add_action('wp_print_scripts', function () {
    if (is_admin()) {
        return;
    }
    global $wp_scripts;
    if (empty($wp_scripts) || empty($wp_scripts->registered)) {
        return;
    }
    foreach ($wp_scripts->registered as $handle => $script) {
        if (!empty($script->src) && strpos($script->src, 'secupress-antispam') !== false) {
            wp_dequeue_script($handle);
            wp_deregister_script($handle);
        }
    }
}, 100);
