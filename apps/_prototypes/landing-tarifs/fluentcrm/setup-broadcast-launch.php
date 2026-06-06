<?php
/**
 * Setup FluentCRM broadcast campaign - Lancement formation "Oser augmenter tes tarifs"
 *
 * Crée :
 *   - 1 campaign type=campaign status=draft (broadcast manuel à scheduler depuis l'admin)
 *   - target : tag abonne_newsletter (id 447) intersection lang_fr (id 768)
 *   - design_template = raw_html
 *   - body avec smartcode {{contact.first_name|"Salut"}} + CTA bouton brand email-safe
 *
 * Idempotent : si campaign avec ce slug existe deja, update en place.
 */

if (!defined('ABSPATH')) {
    return ['error' => 'WordPress non chargé'];
}

global $wpdb;
$report = [];

/* Helper : bouton email-safe (gradient palette1 -> palette2, flèche unicode)
 * Source : mémoire reference_kadence_email_button_pattern.md */
$btn = static function ($href, $label) {
    return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin: 24px auto;">'
         . '<tr><td align="center" style="background-color: #00d400; background-image: linear-gradient(135deg, #00d400 0%, #00a100 100%); border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">'
         . '<a href="' . esc_url($href) . '" target="_blank" style="display: inline-block; padding: 14px 28px; color: #fafbfd; text-decoration: none; font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif; font-size: 16px; font-weight: 700; line-height: 1; border: 1px solid #fafbfd; border-radius: 6px;">'
         . esc_html($label) . '&nbsp;&rarr;'
         . '</a></td></tr></table>';
};

$url_sales = 'https://schoolswp.com/oser-augmenter-tes-tarifs/';

$wp_green = '<span style="color:#00D400">WP</span>';

$body  = '<p>{{contact.first_name|"Salut"}},</p>' . "\n\n";
$body .= '<p>Il y a deux ans, j\'avais un client à 450 € par mois. Maintenance WordPress, petites évolutions, un peu de SEO. Le tarif datait de 2021. On était en 2024. Je faisais le double du travail prévu, et je n\'osais pas en parler.</p>' . "\n\n";
$body .= '<p>Chaque fois que j\'ouvrais le mail pour annoncer la hausse, je le refermais. Je trouvais un prétexte : "pas le bon moment", "il vient de signer un nouveau projet", "j\'attends la fin du trimestre". En vrai, j\'avais juste peur. Peur du clash. Peur qu\'il dise non et qu\'il parte. Peur de me faire répondre "tu aurais pu prévenir plus tôt".</p>' . "\n\n";
$body .= '<p>Tu connais ce mail que tu repousses depuis des mois ?</p>' . "\n\n";
$body .= '<p>J\'ai fini par l\'envoyer. Pas en improvisant. Avec un script précis, un palier calculé, un timing choisi. Le client a accepté en 48 heures. Sans négocier. Et il m\'a remercié d\'avoir été clair.</p>' . "\n\n";
$body .= '<p>C\'est cette mécanique que j\'ai mise dans une formation : <strong>Oser augmenter tes tarifs sans perdre tes clients</strong>.</p>' . "\n\n";
$body .= '<p>Ce n\'est pas un cours sur la "valeur perçue" ou le "mindset". C\'est de l\'opérationnel. Tu sors avec :</p>' . "\n\n";
$body .= '<ul>' . "\n";
$body .= '  <li>Le script mail exact à envoyer (mot pour mot, à adapter)</li>' . "\n";
$body .= '  <li>Le script de l\'appel téléphonique si tu préfères annoncer en direct</li>' . "\n";
$body .= '  <li>Les 7 objections classiques décortiquées une par une, avec la réponse à donner. "C\'est cher", "je vais réfléchir", "tu aurais pu prévenir plus tôt", "j\'ai besoin de voir avec mon associé"... toutes y sont.</li>' . "\n";
$body .= '  <li>La méthode pour tenir bon si un client menace de résilier, sans céder ni paniquer</li>' . "\n";
$body .= '</ul>' . "\n\n";
$body .= '<p>Il y a aussi un module sur les 3 raisons pour lesquelles tu n\'oses pas (peur du clash, peur du rejet, conviction de ne pas valoir le tarif). Pas pour faire du développement personnel. Pour que tu identifies ton blocage et que tu saches quel script t\'adresser à toi-même avant d\'envoyer le mail.</p>' . "\n\n";
$body .= '<p>En bonus : le script appel format long en PDF + audio (pour l\'écouter en marchant), et une checklist 30 minutes à dérouler avant chaque annonce. Ce sont les outils que j\'utilise moi-même.</p>' . "\n\n";
$body .= '<p><strong>À qui je l\'ai écrite :</strong> freelance WordPress, consultant, prestataire en services récurrents, qui as des clients depuis plus d\'un an et qui n\'as jamais bougé tes tarifs. Tu sais que tu sous-factures. Tu hésites depuis trop longtemps.</p>' . "\n\n";
$body .= '<p><strong>À qui ce n\'est pas adressé :</strong> si tu démarres et que tu n\'as pas encore de portefeuille, ou si tu vends du one-shot sans récurrent, l\'angle ne sera pas le bon. Garde ton argent pour autre chose.</p>' . "\n\n";
$body .= '<p>Prix : <strong>197 €, paiement unique</strong>. Pas d\'abonnement, pas de mensualité qui revient. Accès permanent à la formation et aux mises à jour.</p>' . "\n\n";
$body .= '<p><strong>Garantie 30 jours satisfait ou remboursé.</strong> Si tu déroules les modules, que tu testes le script et que ça ne te sert à rien, tu m\'écris à <a href="mailto:contact@michaelkihl.fr">contact@michaelkihl.fr</a> et je rembourse. Sans interrogatoire.</p>' . "\n\n";
$body .= $btn($url_sales, 'Découvrir la formation') . "\n\n";
$body .= '<p>Si tu as une question avant d\'acheter, réponds simplement à ce mail. Je lis tout, je réponds moi-même.</p>' . "\n\n";
$body .= '<p>Michaël<br>schools' . $wp_green . '</p>' . "\n\n";
$body .= '<p style="font-size:14px;color:#57556d;border-top:1px solid #edf0f8;padding-top:16px;margin-top:32px;">PS : si tu envoies ce mail tarifs aujourd\'hui, sans cette formation, fais au moins une chose. Calcule ton nouveau tarif AVANT d\'écrire le message. Le pire mail est celui qu\'on rédige avec le chiffre dans la tête mais pas posé sur papier. C\'est là que tu cèdes à la première objection.</p>';

$campaign_settings = serialize([
    'mailer_settings' => [
        'from_name'      => '',
        'from_email'     => '',
        'reply_to_name'  => '',
        'reply_to_email' => '',
        'is_custom'      => 'no',
    ],
    'subscribers' => [
        ['list' => 'all', 'tag' => '447'], // abonne_newsletter
    ],
    'excludedSubscribers' => null,
    'sending_filter' => 'list_tag',
    'dynamic_segment' => ['id' => '', 'slug' => ''],
    'sending_type' => 'instant',
    'footer_settings' => [
        'custom_footer' => 'no',
        'footer_content' => '',
    ],
    'advanced_filters' => [[]],
]);

$campaign_table = $wpdb->prefix . 'fc_campaigns';
$slug = 'broadcast-lancement-formation-tarifs';
$title = 'BROADCAST - Lancement Formation Oser augmenter tes tarifs';
$subject = 'La conversation tarifs que je repoussais depuis deux ans';
$preheader = 'Une formation de 6 modules pour passer le cap, sans perdre ton client.';
$now = current_time('mysql');

$existing = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT id FROM {$campaign_table} WHERE slug = %s LIMIT 1",
    $slug
));

if ($existing) {
    $wpdb->update($campaign_table, [
        'title'            => $title,
        'email_subject'    => $subject,
        'email_pre_header' => $preheader,
        'email_body'       => $body,
        'design_template'  => 'raw_html',
        'settings'         => $campaign_settings,
        'status'           => 'draft',
        'updated_at'       => $now,
    ], ['id' => $existing]);
    $campaign_id = $existing;
    $report['action'] = 'updated';
} else {
    $wpdb->insert($campaign_table, [
        'parent_id'        => 0,
        'type'             => 'campaign',
        'title'            => $title,
        'slug'             => $slug,
        'status'           => 'draft',
        'template_id'      => 0,
        'email_subject'    => $subject,
        'email_pre_header' => $preheader,
        'email_body'       => $body,
        'recipients_count' => 0,
        'design_template'  => 'raw_html',
        'utm_status'       => '0',
        'settings'         => $campaign_settings,
        'created_by'       => 2,
        'created_at'       => $now,
        'updated_at'       => $now,
    ]);
    $campaign_id = (int) $wpdb->insert_id;
    $report['action'] = 'created';
}

$report['campaign_id']  = $campaign_id;
$report['title']        = $title;
$report['subject']      = $subject;
$report['preheader']    = $preheader;
$report['target_tag']   = 'abonne_newsletter (447)';
$report['status']       = 'draft';
$report['body_length']  = strlen($body);
$report['admin_url']    = admin_url('admin.php?page=fluentcrm-admin#/email-campaigns/' . $campaign_id);

echo json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
