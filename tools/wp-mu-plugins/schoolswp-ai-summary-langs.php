<?php
/**
 * Plugin Name: schoolsWP - AI summary langs config
 * Description: Configure les langues acceptees par l'auto-injection des boutons IA + traductions UI/prompt par langue. Etend le defaut FR a FR + EN + DE. Pour ajouter une langue : 1) traduire les strings via le filtre `swp_ai_summary_strings`, 2) ajouter le code 2 lettres au tableau retourne par `swp_ai_summary_auto_inject_langs`.
 * Author: schoolsWP
 * Version: 1.1.0
 * License: GPL-2.0-or-later
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Etend le scope auto-injection : FR + EN + DE.
 */
add_filter('swp_ai_summary_auto_inject_langs', function () {
    return array('fr', 'en', 'de');
});

/**
 * Ajoute les traductions DE (FR et EN sont deja livres dans le mu-plugin principal).
 */
add_filter('swp_ai_summary_strings', function ($strings) {
    $strings['de'] = array(
        'title_q'    => 'Keine Zeit?',
        'title_c'    => 'Lass es von der KI zusammenfassen',
        'aria_aside' => 'Diesen Artikel mit KI zusammenfassen',
        'aria_pill'  => 'Diesen Artikel mit %s zusammenfassen',
        'prompt'     => 'Lies diesen schoolsWP-Artikel mit dem Titel "%1$s" und gib mir eine klare Zusammenfassung in 5 Kernpunkten, auf Deutsch: %2$s',
    );
    return $strings;
});
