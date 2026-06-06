<?php
/**
 * update_form_5.php
 *
 * Script qui charge WordPress, récupère le formulaire FluentForms ID 5,
 * modifie son JSON pour :
 *   • remplacer le champ « Niveau » (laisser uniquement « rassemblement »)
 *   • ajouter un bloc HTML descriptif (texte fourni)
 *   • ajouter les champs obligatoires « Adresse postale » et « Numéro de téléphone »
 *   • mettre à jour la case à cocher de consentement avec la mention du tirage au sort
 *   • ajouter (ou mettre à jour) le champ « Refreshments » avec le placeholder indiqué
 *
 * Le script ré‑écrit le JSON dans la table wp_fluentform_forms.
 * À exécuter sur une copie de **staging** avant de le lancer en production.
 */

define('WP_USE_THEMES', false);
require_once __DIR__ . '/wp-load.php'; // chemin vers le wp‑load.php du projet

global $wpdb;

// -------------------------------------------------------------------
// 1️⃣ Récupération du formulaire (ID 5)
$form_id = 5;
$table   = $wpdb->prefix . 'fluentform_forms';

$raw = $wpdb->get_var( $wpdb->prepare(
    "SELECT form_fields FROM $table WHERE id = %d",
    $form_id
) );

if ( ! $raw ) {
    die("❌ Formulaire ID $form_id introuvable.\n");
}

// Décodage du JSON
$form = json_decode( $raw, true );
if ( json_last_error() !== JSON_ERROR_NONE ) {
    die("❌ Erreur de décodage JSON : " . json_last_error_msg() . "\n");
}

// -------------------------------------------------------------------
// 2️⃣ Helper – recherche d’un champ par son label (ou key)
function find_field_index( $fields, $needle ) {
    foreach ( $fields as $idx => $field ) {
        if ( ! empty( $field['label'] ) && stripos( $field['label'], $needle ) !== false ) {
            return $idx;
        }
        if ( ! empty( $field['name'] ) && stripos( $field['name'], $needle ) !== false ) {
            return $idx;
        }
    }
    return false;
}

// -------------------------------------------------------------------
// 3️⃣ Mise à jour du champ « Niveau »
$niveauIdx = find_field_index( $form['form_fields'], 'Niveau' );
if ( $niveauIdx !== false ) {
    $form['form_fields'][ $niveauIdx ]['options'] = [ 'rassemblement' ];
    $form['form_fields'][ $niveauIdx ]['placeholder'] = 'rassemblement';
}

// -------------------------------------------------------------------
// 4️⃣ Ajout du bloc HTML descriptif (en haut du formulaire)
$descriptionHtml = <<<HTML
<div class="custom-description">
  <p>Animateur de la section locale et amoureux inconditionnel des routes rémoises et de la Montagne de Reims. Mon but est simple : offrir à tous les amateurs de cyclisme un peloton structuré, sécurisant et bienveillant. Ici, on progresse dans la bonne humeur, on partage nos astuces d’entraînement, et on s’offre un bon café de départ. Hâte de rouler avec toi !</p>
  <p>Moselle copain</p>
  <p>On s’offre du souvenir avant tout</p>
  <p>Et pourquoi pas plus</p>
  <p>Pas de spoile 😉</p>
  <p>Marque cycliste, agence locale, organisateur d’événement, café/restaurant Grand Est, magasin de vélo</p>
</div>
HTML;

$htmlField = [
    'type'        => 'html',
    'label'       => '',
    'value'       => $descriptionHtml,
    'required'    => false,
    'name'        => 'custom_description_' . time(),
    'order'       => 0,
];

array_unshift( $form['form_fields'], $htmlField );

// -------------------------------------------------------------------
// 5️⃣ Ajout des champs « Adresse postale » et « Numéro de téléphone »
$addressField = [
    'type'        => 'input',
    'input_type'  => 'text',
    'label'       => 'Adresse postale',
    'name'        => 'adresse_postale',
    'required'    => true,
    'placeholder' => '',
    'order'       => 1,
];
$phoneField = [
    'type'        => 'input',
    'input_type'  => 'text',
    'label'       => 'Numéro de téléphone',
    'name'        => 'numero_telephone',
    'required'    => true,
    'placeholder' => '',
    'order'       => 2,
];

array_splice( $form['form_fields'], 1, 0, [ $addressField, $phoneField ] );

// -------------------------------------------------------------------
// 6️⃣ Mise à jour de la case à cocher de consentement (RGPD)
$consentIdx = find_field_index( $form['form_fields'], 'rgpd' ); // clé habituelle
if ( $consentIdx !== false ) {
    $form['form_fields'][ $consentIdx ]['label'] = "J'accepte le traitement de mes données";
    $form['form_fields'][ $consentIdx ]['description'] = '* Vous participez automatiquement au tirage au sort pour être sur la caravane du tout de France Mulhouse Markensteik.';
    $form['form_fields'][ $consentIdx ]['help_text'] = 'Vous ne vouliez pas cocher cette case … Pour ne pas prendre la place d’un autre disponible tu sais.';
}

// -------------------------------------------------------------------
// 7️⃣ Champ « Refreshments » (optionnel) avec placeholder
$refreshIdx = find_field_index( $form['form_fields'], 'refreshments' );
if ( $refreshIdx === false ) {
    $refreshField = [
        'type'        => 'input',
        'input_type'  => 'text',
        'label'       => 'Ce que vous désirez (ex : jus, café, croissant, bretzel…) ',
        'name'        => 'refreshments',
        'required'    => false,
        'placeholder' => 'sa peut être un jus un café croissant bretzel etc',
        'order'       => 3,
    ];
    // insérer après le champ téléphone
    array_splice( $form['form_fields'], 4, 0, [ $refreshField ] );
}

// -------------------------------------------------------------------
// 8️⃣ Ré‑encodage et sauvegarde
$newJson = wp_json_encode( $form );
if ( $newJson === false ) {
    die("❌ Impossible d’encoder le JSON final.\n");
}

$updated = $wpdb->query( $wpdb->prepare(
    "UPDATE $table SET form_fields = %s WHERE id = %d",
    $newJson,
    $form_id
) );

if ( $updated === false ) {
    die("❌ Échec de la mise à jour en base.\n");
}

echo "✅ Formulaire ID $form_id mis à jour avec succès.\n";
?>
