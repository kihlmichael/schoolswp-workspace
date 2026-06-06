<?php
/**
 * Setup FluentCRM welcome sequence - Formation "Oser augmenter tes tarifs"
 *
 * Crée :
 *   - tag formation_tarifs_acheteur
 *   - 5 campaigns (E1 à E5) au format funnel_email_campaign, design_template = raw_html
 *   - funnel SEQ "Welcome Formation Tarifs" (trigger fluentcrm_contact_added_to_tags) avec 10 steps
 *   - funnel SYNC "FluentCart Order Paid Formation Tarifs" (trigger fluent_cart/order_paid_done) avec 1 step
 *
 * Idempotent : détecte les entités existantes par slug/title et les met à jour au lieu de dupliquer.
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

$url_course = 'https://schoolswp.com/formation/oser-augmenter-tes-tarifs/';

/* 1. Tag formation_tarifs_acheteur ----------------------------------- */
$tag_slug = 'formation_tarifs_acheteur';
$tag = FluentCrm\App\Models\Tag::where('slug', $tag_slug)->first();
if (!$tag) {
    $tag = FluentCrm\App\Models\Tag::create([
        'title' => 'formation_tarifs_acheteur',
        'slug'  => $tag_slug,
    ]);
    $report['tag'] = ['action' => 'created', 'id' => $tag->id];
} else {
    $report['tag'] = ['action' => 'kept', 'id' => $tag->id];
}
$tag_id = (int) $tag->id;

/* 2. Email bodies (HTML email-safe, FluentCRM smartcodes) ------------ */
$opener = '<p>{{contact.first_name|"Salut"}},</p>';
$signoff_short = '<p>À demain,<br>Michaël<br>schoolsWP</p>';
$signoff_close = '<p>À bientôt,<br>Michaël<br>schoolsWP</p>';

$body_e1 = $opener . "\n\n"
    . '<p>Bienvenue dans la formation. Ton accès est actif.</p>' . "\n\n"
    . '<p>Tu peux te connecter maintenant depuis cette page :</p>' . "\n\n"
    . '<p><a href="' . $url_course . '" target="_blank" rel="noopener">schoolswp.com/formation/oser-augmenter-tes-tarifs</a></p>' . "\n\n"
    . '<p>Je te conseille de commencer par le <strong>Module 1 : Pourquoi tu n\'oses pas augmenter</strong>. Pas parce que c\'est le premier, mais parce que c\'est le plus important. Il t\'aide à identifier ton profil exact : peur du clash, peur d\'être rejeté, ou conviction que tu ne vaux pas encore ce tarif. Ces trois archétypes ne se traitent pas de la même façon, et la formation est construite autour de ça.</p>' . "\n\n"
    . '<p>Le module prend environ 20 minutes. Tu peux le faire ce soir.</p>' . "\n\n"
    . $btn($url_course, 'Accéder à la formation') . "\n\n"
    . '<p>Dans les prochains jours, je t\'envoie un email par module clé, avec du contenu bonus que tu ne trouves pas dans les leçons. Je veux que tu aies le plus haut taux de complétion possible, pas juste un accès qui dort dans tes favoris.</p>' . "\n\n"
    . '<p>Si tu as une question, tu réponds directement à cet email. Je lis tout.</p>' . "\n\n"
    . $signoff_short;

$body_e2 = $opener . "\n\n"
    . '<p>Hier tu as eu accès à la formation. Aujourd\'hui je veux qu\'on parle de ce qui bloque vraiment.</p>' . "\n\n"
    . '<p>Dans le Module 1, j\'ai décrit trois profils. Pas des cases théoriques : des patterns que j\'ai vus chez des dizaines de freelances et consultants.</p>' . "\n\n"
    . '<p><strong>Profil 1 : la peur du clash.</strong> Tu anticipes déjà la réaction du client. Tu imagines qu\'il va s\'énerver, te mettre la pression, ou te faire un retour blessant. Alors tu évites.</p>' . "\n\n"
    . '<p><strong>Profil 2 : la peur du rejet.</strong> Tu n\'as pas peur de la scène. Tu as peur qu\'il parte. Et qu\'il parte en te disant que tu n\'en vaux pas le prix.</p>' . "\n\n"
    . '<p><strong>Profil 3 : la conviction de ne pas valoir le tarif.</strong> Le problème n\'est pas le client. C\'est toi. Tu es convaincu qu\'il faut encore "faire tes preuves" avant d\'augmenter.</p>' . "\n\n"
    . '<p>Ces trois profils ont des déclencheurs différents et des scripts différents dans la formation.</p>' . "\n\n"
    . '<p><strong>Réponds-moi : tu es quel profil ? Ou un mélange de deux ?</strong></p>' . "\n\n"
    . '<p>Je lis chaque réponse. Et si tu ne sais pas encore, le module te donne un diagnostic clair en moins de 20 minutes.</p>' . "\n\n"
    . $btn($url_course, 'Faire le module 1') . "\n\n"
    . $signoff_short;

$body_e3 = $opener . "\n\n"
    . '<p>La partie que tout le monde redoute, c\'est rarement le "est-ce que j\'augmente", c\'est le "comment je le dis".</p>' . "\n\n"
    . '<p>Le Module 3 règle ça. Il contient deux scripts complets : un pour annoncer l\'augmentation par email, un pour le faire par téléphone. Pas des trames vagues avec des accolades à remplir. Des formulations calibrées, testées, avec les mots exacts qui ouvrent la conversation plutôt que la fermer.</p>' . "\n\n"
    . '<p>Voilà la logique du script email :</p>' . "\n\n"
    . '<p>Tu n\'annonces pas une augmentation. Tu invites le client à une conversation sur la suite de votre collaboration. Le mot "augmentation" n\'apparaît pas dans le premier paragraphe. La structure : ouverture personnalisée, rappel de la valeur délivrée, transition vers le nouveau tarif, proposition concrète. Quatre blocs. Environ 150 mots.</p>' . "\n\n"
    . '<p>Tu peux l\'adapter ce matin et l\'envoyer cet après-midi.</p>' . "\n\n"
    . '<p>Le module contient aussi le script appel, plus court mais plus direct, parce que l\'oral obéit à d\'autres règles que l\'écrit.</p>' . "\n\n"
    . '<p>Le bonus PDF (script appel long format avec les formulations audio) est inclus dans ta formation.</p>' . "\n\n"
    . $btn($url_course, 'Accéder au Module 3') . "\n\n"
    . $signoff_short;

$body_e4 = $opener . "\n\n"
    . '<p>Le Module 4 recense les 7 objections que tu vas entendre. Pas les 7 que j\'ai imaginées : les 7 qui reviennent systématiquement, que le client soit direct ou hésitant.</p>' . "\n\n"
    . '<p>Je te donne le script pour la première ici, maintenant.</p>' . "\n\n"
    . '<p><strong>Objection : "C\'est cher."</strong></p>' . "\n\n"
    . '<p>Ce que tu ne dois pas faire : justifier, détailler tes charges, ou baisser immédiatement.</p>' . "\n\n"
    . '<p>Ce que tu dis :</p>' . "\n\n"
    . '<blockquote style="border-left: 4px solid #00d400; padding: 12px 16px; margin: 16px 0; background-color: #f4f6fb; font-style: italic; color: #12111f;">"Je comprends que ça représente un budget. Qu\'est-ce qui te fait dire ça par rapport à ce qu\'on a fait ensemble jusqu\'ici ?"</blockquote>' . "\n\n"
    . '<p>Une question. Ouverte. Qui déplace la conversation du prix vers la valeur. Neuf fois sur dix, le client va reformuler. Et cette reformulation te donne exactement ce dont tu as besoin pour répondre.</p>' . "\n\n"
    . '<p>Les six autres objections dans le module : "je vais réfléchir", "les autres font moins cher", "je ne peux pas en ce moment", "on n\'avait pas prévu ça dans notre accord", "tu aurais pu me prévenir plus tôt", et "j\'ai besoin de voir avec mon associé/directeur".</p>' . "\n\n"
    . '<p>Chacune a son script. Aucun n\'est agressif. Tous sont conçus pour tenir la relation, pas juste tenir le tarif.</p>' . "\n\n"
    . $btn($url_course, 'Voir les 7 objections complètes') . "\n\n"
    . $signoff_short;

$body_e5 = $opener . "\n\n"
    . '<p>Tu as maintenant les quatre modules clés déverrouillés. Le Module 5 (tenir bon face à une résiliation) et le Module 6 (les 5 réflexes avant chaque négociation) finalisent le parcours.</p>' . "\n\n"
    . '<p>Aujourd\'hui je veux te proposer quelque chose de différent.</p>' . "\n\n"
    . '<p>Si tu as un client en tête, un contexte particulier, une annonce que tu dois faire dans les prochaines semaines : réponds à cet email et raconte-moi la situation en deux ou trois lignes. Durée de la relation avec le client, type de prestation, tarif actuel, tarif cible. C\'est tout.</p>' . "\n\n"
    . '<p>Je te réponds avec un retour personnalisé. Pas un email automatique. Pas un chatbot. Moi.</p>' . "\n\n"
    . '<p>Ce n\'est pas un bonus caché dans la formation. C\'est juste ce que je fais pour les gens qui ont investi dans la formation et qui ont un vrai cas concret à résoudre.</p>' . "\n\n"
    . '<p>Si tu n\'as pas encore tout complété, l\'accès reste permanent. Tu peux y revenir à ton rythme.</p>' . "\n\n"
    . '<p>Et si tu as la moindre question sur la plateforme ou sur un module, tu m\'écris à <a href="mailto:contact@michaelkihl.fr">contact@michaelkihl.fr</a>.</p>' . "\n\n"
    . $btn($url_course, 'Accéder à ta formation') . "\n\n"
    . $signoff_close;

$emails = [
    'e1' => [
        'title'           => 'SEQ - Welcome Formation Tarifs (E1 - J0 - Accès)',
        'slug'            => 'funnel-formation-tarifs-e1-acces',
        'email_subject'   => 'Ton accès est prêt, voilà comment commencer',
        'email_pre_header'=> 'Le module 1 prend 20 minutes. Tu peux le faire ce soir.',
        'email_body'      => $body_e1,
    ],
    'e2' => [
        'title'           => 'SEQ - Welcome Formation Tarifs (E2 - J+1 - Archétype)',
        'slug'            => 'funnel-formation-tarifs-e2-archetype',
        'email_subject'   => 'Lequel des 3 t\'empêche d\'augmenter ?',
        'email_pre_header'=> 'Ce n\'est pas une question rhétorique. Réponds-moi.',
        'email_body'      => $body_e2,
    ],
    'e3' => [
        'title'           => 'SEQ - Welcome Formation Tarifs (E3 - J+2 - Script email)',
        'slug'            => 'funnel-formation-tarifs-e3-script-email',
        'email_subject'   => 'Le mail que tu peux envoyer cet après-midi',
        'email_pre_header'=> 'Un script complet pour annoncer l\'augmentation par email.',
        'email_body'      => $body_e3,
    ],
    'e4' => [
        'title'           => 'SEQ - Welcome Formation Tarifs (E4 - J+3 - Objection)',
        'slug'            => 'funnel-formation-tarifs-e4-objection',
        'email_subject'   => '"C\'est cher" : voilà quoi répondre mot pour mot',
        'email_pre_header'=> 'L\'objection la plus courante. Le script exact, dans cet email.',
        'email_body'      => $body_e4,
    ],
    'e5' => [
        'title'           => 'SEQ - Welcome Formation Tarifs (E5 - J+4 - Retour perso)',
        'slug'            => 'funnel-formation-tarifs-e5-retour-perso',
        'email_subject'   => 'Un retour personnalisé, si tu veux',
        'email_pre_header'=> 'Pas d\'upsell. Juste une proposition concrète pour ta situation.',
        'email_body'      => $body_e5,
    ],
];

/* 3. Create or update campaigns -------------------------------------- */
$campaign_table = $wpdb->prefix . 'fc_campaigns';
$campaign_ids = [];
$now = current_time('mysql');
$campaign_settings = serialize([
    'template_config' => ['content_width' => '700'],
    'mailer_settings' => [
        'from_name'      => '',
        'from_email'     => '',
        'reply_to_name'  => '',
        'reply_to_email' => '',
        'is_custom'      => 'no',
    ],
]);

foreach ($emails as $key => $em) {
    $existing = (int) $wpdb->get_var($wpdb->prepare(
        "SELECT id FROM {$campaign_table} WHERE slug = %s LIMIT 1",
        $em['slug']
    ));
    if ($existing) {
        $wpdb->update(
            $campaign_table,
            [
                'title'            => $em['title'],
                'email_subject'    => $em['email_subject'],
                'email_pre_header' => $em['email_pre_header'],
                'email_body'       => $em['email_body'],
                'design_template'  => 'raw_html',
                'settings'         => $campaign_settings,
                'updated_at'       => $now,
            ],
            ['id' => $existing]
        );
        $campaign_ids[$key] = $existing;
        $report['campaigns'][$key] = ['action' => 'updated', 'id' => $existing];
    } else {
        $wpdb->insert($campaign_table, [
            'parent_id'        => 0,
            'type'             => 'funnel_email_campaign',
            'title'            => $em['title'],
            'slug'             => $em['slug'],
            'status'           => 'published',
            'template_id'      => 0,
            'email_subject'    => $em['email_subject'],
            'email_pre_header' => $em['email_pre_header'],
            'email_body'       => $em['email_body'],
            'recipients_count' => 0,
            'design_template'  => 'raw_html',
            'utm_status'       => '',
            'settings'         => $campaign_settings,
            'created_by'       => 2,
            'created_at'       => $now,
            'updated_at'       => $now,
        ]);
        $new_id = (int) $wpdb->insert_id;
        $campaign_ids[$key] = $new_id;
        $report['campaigns'][$key] = ['action' => 'created', 'id' => $new_id];
    }
}

/* 4. SEQ funnel ------------------------------------------------------ */
$funnels_table = $wpdb->prefix . 'fc_funnels';
$sequences_table = $wpdb->prefix . 'fc_funnel_sequences';

$seq_title = 'SEQ - Welcome Formation Tarifs';
$seq_id = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT id FROM {$funnels_table} WHERE title = %s LIMIT 1",
    $seq_title
));

$seq_conditions = serialize(['run_multiple' => 'no']);
$seq_settings = serialize([
    'tags' => [(string) $tag_id],
    'select_type' => 'any',
    'subscription_status' => 'subscribed',
    '__force_run_actions' => 'yes',
]);

if ($seq_id) {
    $wpdb->update($funnels_table, [
        'trigger_name' => 'fluentcrm_contact_added_to_tags',
        'status'       => 'published',
        'conditions'   => $seq_conditions,
        'settings'     => $seq_settings,
        'updated_at'   => $now,
    ], ['id' => $seq_id]);
    $wpdb->delete($sequences_table, ['funnel_id' => $seq_id]);
    $report['seq_funnel'] = ['action' => 'updated', 'id' => $seq_id];
} else {
    $wpdb->insert($funnels_table, [
        'type'         => 'funnels',
        'title'        => $seq_title,
        'trigger_name' => 'fluentcrm_contact_added_to_tags',
        'status'       => 'published',
        'conditions'   => $seq_conditions,
        'settings'     => $seq_settings,
        'created_by'   => 2,
        'created_at'   => $now,
        'updated_at'   => $now,
    ]);
    $seq_id = (int) $wpdb->insert_id;
    $report['seq_funnel'] = ['action' => 'created', 'id' => $seq_id];
}

$wait_settings = serialize([
    'wait_time_amount'  => 1,
    'wait_time_unit'    => 'days',
    'wait_type'         => 'unit_wait',
    'to_day'            => [],
    'to_day_time'       => '',
]);
$end_settings = serialize(['automation_ids' => []]);

$make_email_settings = static function (int $campaign_id) {
    return serialize([
        'reference_campaign' => $campaign_id,
        'send_email_to_type' => 'contact',
        'send_email_custom'  => '',
        'campaign'           => [],
        'is_scheduled'       => 'no',
        'scheduled_at'       => '',
        'skip_if_overdue'    => 'no',
        'mailer_settings'    => [
            'from_name'      => '',
            'from_email'     => '',
            'reply_to_name'  => '',
            'reply_to_email' => '',
            'is_custom'      => 'no',
        ],
    ]);
};

$seq_steps = [
    ['action_name' => 'send_custom_email',  'settings' => $make_email_settings($campaign_ids['e1']), 'delay' => 0,     'c_delay' => 0,      'sequence' => 1],
    ['action_name' => 'fluentcrm_wait_times','settings' => $wait_settings,                           'delay' => 0,     'c_delay' => 0,      'sequence' => 2],
    ['action_name' => 'send_custom_email',  'settings' => $make_email_settings($campaign_ids['e2']), 'delay' => 86400, 'c_delay' => 86400,  'sequence' => 3],
    ['action_name' => 'fluentcrm_wait_times','settings' => $wait_settings,                           'delay' => 0,     'c_delay' => 86400,  'sequence' => 4],
    ['action_name' => 'send_custom_email',  'settings' => $make_email_settings($campaign_ids['e3']), 'delay' => 86400, 'c_delay' => 172800, 'sequence' => 5],
    ['action_name' => 'fluentcrm_wait_times','settings' => $wait_settings,                           'delay' => 0,     'c_delay' => 172800, 'sequence' => 6],
    ['action_name' => 'send_custom_email',  'settings' => $make_email_settings($campaign_ids['e4']), 'delay' => 86400, 'c_delay' => 259200, 'sequence' => 7],
    ['action_name' => 'fluentcrm_wait_times','settings' => $wait_settings,                           'delay' => 0,     'c_delay' => 259200, 'sequence' => 8],
    ['action_name' => 'send_custom_email',  'settings' => $make_email_settings($campaign_ids['e5']), 'delay' => 86400, 'c_delay' => 345600, 'sequence' => 9],
    ['action_name' => 'end_this_funnel',    'settings' => $end_settings,                             'delay' => 0,     'c_delay' => 345600, 'sequence' => 10],
];

foreach ($seq_steps as $step) {
    $wpdb->insert($sequences_table, [
        'funnel_id'      => $seq_id,
        'action_name'    => $step['action_name'],
        'type'           => 'action',
        'title'          => null,
        'description'    => null,
        'status'         => 'published',
        'conditions'     => serialize([]),
        'settings'       => $step['settings'],
        'note'           => '',
        'delay'          => $step['delay'],
        'c_delay'        => $step['c_delay'],
        'sequence'       => $step['sequence'],
        'created_by'     => 2,
        'created_at'     => $now,
        'updated_at'     => $now,
        'parent_id'      => 0,
        'condition_type' => null,
    ]);
}
$report['seq_steps_inserted'] = count($seq_steps);

/* 5. SYNC funnel : apply tag on order paid --------------------------- */
$sync_title = 'SYNC - FluentCart Order Paid Formation Tarifs (Apply tag)';
$sync_id = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT id FROM {$funnels_table} WHERE title = %s LIMIT 1",
    $sync_title
));

$sync_conditions = serialize([
    'product_ids'        => [2903675],
    'product_categories' => [],
    'run_multiple'       => 'no',
]);
$sync_settings = serialize([
    'subscription_status' => 'subscribed',
    '__force_run_actions' => 'yes',
]);

if ($sync_id) {
    $wpdb->update($funnels_table, [
        'trigger_name' => 'fluent_cart/order_paid_done',
        'status'       => 'published',
        'conditions'   => $sync_conditions,
        'settings'     => $sync_settings,
        'updated_at'   => $now,
    ], ['id' => $sync_id]);
    $wpdb->delete($sequences_table, ['funnel_id' => $sync_id]);
    $report['sync_funnel'] = ['action' => 'updated', 'id' => $sync_id];
} else {
    $wpdb->insert($funnels_table, [
        'type'         => 'funnels',
        'title'        => $sync_title,
        'trigger_name' => 'fluent_cart/order_paid_done',
        'status'       => 'published',
        'conditions'   => $sync_conditions,
        'settings'     => $sync_settings,
        'created_by'   => 2,
        'created_at'   => $now,
        'updated_at'   => $now,
    ]);
    $sync_id = (int) $wpdb->insert_id;
    $report['sync_funnel'] = ['action' => 'created', 'id' => $sync_id];
}

$apply_tag_settings = serialize(['tags' => [(string) $tag_id]]);

$wpdb->insert($sequences_table, [
    'funnel_id'      => $sync_id,
    'action_name'    => 'add_contact_to_tag',
    'type'           => 'action',
    'title'          => null,
    'description'    => null,
    'status'         => 'published',
    'conditions'     => serialize([]),
    'settings'       => $apply_tag_settings,
    'note'           => '',
    'delay'          => 0,
    'c_delay'        => 0,
    'sequence'       => 1,
    'created_by'     => 2,
    'created_at'     => $now,
    'updated_at'     => $now,
    'parent_id'      => 0,
    'condition_type' => null,
]);
$report['sync_steps_inserted'] = 1;

echo json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
