<?php
/**
 * Plugin Name: schoolsWP FluentCart x TutorLMS Customizer
 * Description: (1) Traduit en FR les phrases EN hardcodees des emails admin FluentCart, (2) remplace "Powered by FluentCart" par le lien affilie brut, (3) redirige le bouton "S'inscrire" TutorLMS vers la page produit FluentCart quand le course a un _tutor_course_product_id, (4) auto-enroll dans le course TutorLMS lie quand une commande FluentCart est payee.
 * Author: schoolsWP
 * Version: 1.2.0
 */

if (!defined('ABSPATH')) exit;

/**
 * 1. Traduit les chaines passees par __() / esc_html__()
 *    Couvre les templates qui utilisent les helpers WordPress.
 */
add_filter('gettext', function ($translated, $original, $domain) {
    if ($domain !== 'fluent-cart' && $domain !== 'fluent-cart-pro') {
        return $translated;
    }
    static $map = [
        '%s just placed an order. Here are the details:' => '%s vient de passer une commande. Voici le détail :',
        'To view more details of this order, please check the order detail page.' => 'Pour voir tous les détails de cette commande, ouvre la page de commande.',
        'Powered by ' => '',
        'Have a Coupon?' => 'Tu as un code promo ?',
        'Apply Here' => 'Appliquer',
        'Apply' => 'Appliquer',
        'Coupon Code' => 'Code promo',
        'Place order' => 'Valider la commande',
        'No valid public key found! Please contact the site administrator.' => 'Aucune clé publique configurée. Si le total est 0 €, ce moyen de paiement n\'est pas nécessaire.',
    ];
    return isset($map[$original]) ? $map[$original] : $translated;
}, 10, 3);

/**
 * 2. Filtre wp_mail : couvre les templates Pro (Gutenberg en dur) +
 *    remplace le footer "Powered by FluentCart" par le lien affilie brut.
 */
add_filter('wp_mail', function ($args) {
    // 2a. Sujet : traduit le prefixe EN canonique vers FR + neutralise les em-dash du store_name
    if (!empty($args['subject']) && is_string($args['subject'])) {
        $subject = $args['subject'];
        $subject = preg_replace('/^New Sales On /i', 'Nouvelle vente sur ', $subject);
        $subject = str_replace(array("\xE2\x80\x94", "\xE2\x80\x93"), ' : ', $subject);
        $subject = preg_replace('/\s+:\s+/', ' : ', $subject);
        $args['subject'] = $subject;
    }

    if (empty($args['message']) || !is_string($args['message'])) {
        return $args;
    }
    $message = $args['message'];

    // 2b. FR fallback pour les strings hors __() (templates Gutenberg Pro)
    $message = str_replace(
        'just placed an order. Here are the details:',
        'vient de passer une commande. Voici le détail :',
        $message
    );
    $message = str_replace(
        'To view more details of this order, please check the order detail page.',
        'Pour voir tous les détails de cette commande, ouvre la page de commande.',
        $message
    );

    // 2c. Footer FluentCart (lien affilie ?by=40) : phrase brand schoolsWP, distincte du "Propulse par FluentCRM" plus haut.
    $aff_url = 'https://fluentcart.com/?by=40';
    $aff_label = 'Plateforme e-commerce : FluentCart';
    $aff_html = '<a href="' . esc_url($aff_url) . '" style="color:#00d400;text-decoration:none;font-weight:600">' . esc_html($aff_label) . '</a>';

    // Variante 1 : Mailer.php / EmailNotificationMailer.php (div wrapper)
    $message = preg_replace(
        '#<div[^>]*>\s*Powered by\s*<a[^>]*href=[\'"]https?://fluentcart\.com[\'"][^>]*>\s*FluentCart\s*</a>\s*</div>#i',
        '<div style="padding:15px;text-align:center;font-size:13px;color:#2F3448;">' . $aff_html . '</div>',
        $message
    );

    // Variante 2 : components/powered-by-footer.php (prefixe "Global Footer -")
    $message = preg_replace(
        '#Global Footer\s*-\s*Powered by\s*<a[^>]*>\s*FluentCart\s*</a>#i',
        $aff_html,
        $message
    );

    // Variante 3 : pattern HTML simple "Powered by <a>FluentCart</a>"
    $message = preg_replace(
        '#Powered by\s*<a[^>]*href=[\'"]https?://fluentcart\.com[\'"][^>]*>\s*FluentCart\s*</a>#i',
        $aff_html,
        $message
    );

    // Variante 4 : fallback texte brut "Powered by FluentCart" -> phrase brand cliquable
    $message = str_replace('Powered by FluentCart', $aff_html, $message);

    // Variante 5 : URL affiliee deja injectee mais affichee en texte (ancien bug v1.2.0)
    $message = preg_replace('#(?<!href=")(?<!">)' . preg_quote($aff_url, '#') . '(?!")#', $aff_html, $message);

    $args['message'] = $message;
    return $args;
}, 99);

/**
 * 3. Redirige le bouton "S'inscrire maintenant" du single course TutorLMS
 *    vers la page produit FluentCart liee via _tutor_course_product_id.
 *
 *    Generique : marche pour TOUT course qui a un _tutor_course_product_id
 *    pointant vers un fluent-products publish.
 *
 *    Approche : interception du POST form "tutor_course_action=_tutor_course_enroll_now"
 *    avant que le handler natif TutorLMS (Course::enroll_now en priorite 10) ne s'execute.
 */
add_action('template_redirect', function () {
    $action = isset($_REQUEST['tutor_course_action']) ? sanitize_text_field((string) wp_unslash($_REQUEST['tutor_course_action'])) : '';
    if ($action !== '_tutor_course_enroll_now') {
        return;
    }

    $course_id = 0;
    if (is_singular('courses')) {
        $course_id = (int) get_queried_object_id();
    }
    if (!$course_id && !empty($_REQUEST['tutor_course_id'])) {
        $course_id = (int) $_REQUEST['tutor_course_id'];
    }
    if (!$course_id) {
        return;
    }

    $product_id = (int) get_post_meta($course_id, '_tutor_course_product_id', true);
    if (!$product_id) {
        return;
    }

    $product = get_post($product_id);
    if (!$product || $product->post_status !== 'publish' || $product->post_type !== 'fluent-products') {
        return;
    }

    $url = get_permalink($product_id);
    if (!$url) {
        return;
    }

    wp_safe_redirect($url, 302);
    exit;
}, 5);

/**
 * 4. Auto-enroll dans le course TutorLMS lie quand une commande FluentCart
 *    est marquee comme payee.
 *
 *    - Cherche, pour chaque ligne d'order, tous les courses qui ont
 *      _tutor_course_product_id == product_id.
 *    - Resout le user_id depuis l'order (user_id direct ou email du customer).
 *    - Cree un post 'tutor_enrolled' (parent = course, author = user, status = completed).
 *    - Idempotent : ne re-enroll pas si une inscription completed existe deja.
 *
 *    Defensif : on enregistre le meme handler sur plusieurs noms de hook
 *    FluentCart possibles, parce que le nom exact varie selon versions
 *    (fluent_cart/order/paid vs payment_complete vs order/processed).
 */
function schoolswp_fc_enroll_user_in_course($user_id, $course_id, $order_id = 0) {
    $user_id = (int) $user_id;
    $course_id = (int) $course_id;
    if ($user_id <= 0 || $course_id <= 0) {
        return false;
    }
    $course = get_post($course_id);
    if (!$course || $course->post_type !== 'courses') {
        return false;
    }

    $existing = get_posts([
        'post_type'   => 'tutor_enrolled',
        'post_parent' => $course_id,
        'author'      => $user_id,
        'post_status' => 'completed',
        'numberposts' => 1,
        'fields'      => 'ids',
    ]);
    if (!empty($existing)) {
        return (int) $existing[0];
    }

    $enrollment_id = wp_insert_post([
        'post_type'   => 'tutor_enrolled',
        'post_title'  => 'Course Enrolled #' . $course_id,
        'post_status' => 'completed',
        'post_parent' => $course_id,
        'post_author' => $user_id,
    ], true);

    if (is_wp_error($enrollment_id) || !$enrollment_id) {
        return false;
    }

    if ($order_id) {
        update_post_meta($enrollment_id, '_tutor_enrolled_by_order_id', (int) $order_id);
    }
    update_post_meta($enrollment_id, '_schoolswp_auto_enroll_source', 'fluentcart');

    if (function_exists('do_action')) {
        do_action('tutor_after_enroll', $course_id, $enrollment_id);
    }

    return (int) $enrollment_id;
}

function schoolswp_fc_handle_paid_order($order) {
    if (!$order) {
        return;
    }
    // Order peut etre un object OrderModel, un array, ou un order_id (int).
    $order_arr = null;
    if (is_numeric($order)) {
        $order_id = (int) $order;
        $order_arr = ['id' => $order_id];
    } elseif (is_object($order)) {
        $order_arr = method_exists($order, 'toArray') ? $order->toArray() : (array) $order;
    } elseif (is_array($order)) {
        $order_arr = $order;
    } else {
        return;
    }

    $order_id = isset($order_arr['id']) ? (int) $order_arr['id'] : 0;
    $user_id = isset($order_arr['user_id']) ? (int) $order_arr['user_id'] : 0;
    $customer_id = isset($order_arr['customer_id']) ? (int) $order_arr['customer_id'] : 0;
    $customer_email = isset($order_arr['customer_email']) ? (string) $order_arr['customer_email'] : '';

    if (!$user_id) {
        // Resolution depuis la table fct_customers
        if ($customer_id) {
            $row = $GLOBALS['wpdb']->get_row(
                $GLOBALS['wpdb']->prepare("SELECT user_id, email FROM yym2fb_fct_customers WHERE id = %d", $customer_id),
                ARRAY_A
            );
            if ($row) {
                if (!empty($row['user_id'])) {
                    $user_id = (int) $row['user_id'];
                } elseif (!$customer_email && !empty($row['email'])) {
                    $customer_email = (string) $row['email'];
                }
            }
        }
    }
    if (!$user_id && $customer_email) {
        $user = get_user_by('email', $customer_email);
        if ($user) {
            $user_id = (int) $user->ID;
        }
    }
    if (!$user_id) {
        return;
    }

    // Recupere les lignes d'order : essaye d'abord l'objet, sinon DB directe
    $items = isset($order_arr['items']) && is_array($order_arr['items']) ? $order_arr['items'] : null;
    if ($items === null && $order_id) {
        $items = $GLOBALS['wpdb']->get_results(
            $GLOBALS['wpdb']->prepare("SELECT post_id FROM yym2fb_fct_order_items WHERE order_id = %d", $order_id),
            ARRAY_A
        );
    }
    if (empty($items)) {
        return;
    }

    foreach ($items as $item) {
        $product_id = 0;
        if (is_array($item)) {
            $product_id = (int) ($item['post_id'] ?? $item['product_id'] ?? 0);
        } elseif (is_object($item)) {
            $product_id = (int) ($item->post_id ?? $item->product_id ?? 0);
        }
        if (!$product_id) {
            continue;
        }

        $courses = get_posts([
            'post_type'   => 'courses',
            'post_status' => 'publish',
            'numberposts' => 10,
            'meta_key'    => '_tutor_course_product_id',
            'meta_value'  => $product_id,
            'fields'      => 'ids',
        ]);

        foreach ($courses as $course_id) {
            schoolswp_fc_enroll_user_in_course($user_id, $course_id, $order_id);
        }
    }
}

// Enregistre le handler sur plusieurs noms de hook FluentCart par defense.
// Le nom canonique utilise par FluentCart >= 1.3.x est 'fluent_cart/order_paid_done'.
add_action('fluent_cart/order_paid_done', 'schoolswp_fc_handle_paid_order', 10, 1);
add_action('fluent_cart/order/paid', 'schoolswp_fc_handle_paid_order', 10, 1);
add_action('fluent_cart/order/payment_complete', 'schoolswp_fc_handle_paid_order', 10, 1);
add_action('fluent_cart/order/processed', 'schoolswp_fc_handle_paid_order', 10, 1);
add_action('fluent_cart/order_paid', 'schoolswp_fc_handle_paid_order', 10, 1);
add_action('fluent_cart/payment_success', 'schoolswp_fc_handle_paid_order', 10, 1);
