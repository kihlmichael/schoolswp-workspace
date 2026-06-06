# Novamira MIRROR - IDs log FluentCart + FluentCRM (rollback)

Date : 2026-05-16
Site : schoolswp.com
Stack : FluentCart 1.3.28 + FluentCart Pro 1.3.28 + FluentCRM 3.0.5 + FluentCampaign Pro 3.0.3
Auteur : Michaël KIHL (user_id = 2)

## Produits FluentCart

Post_type = fluent-products. Variations dans table fct_product_variations.

- Formation Novamira MIRROR - Post 2900025 / Variation 6 - slug novamira-mirror-formation - prix 67 EUR - attachment featured 2899120 - tag déclenché 772 (acheteur) - funnel 38
- Pack avancé Migrations (order bump) - Post 2900031 / Variation 7 - slug à définir - prix 27 EUR - attachment featured 2899120 (à remplacer) - tag déclenché 774 (bump_acheteur) - funnel 40
- Audit personnalisé Novamira (upsell) - Post 2900032 / Variation 8 - slug novamira-mirror-upsell-audit - prix 97 EUR - attachment featured 2903727 (cover audit dédiée) - tag déclenché 773 (audit_acheteur) - funnel 39

## Tags FluentCRM

- 772 - novamira_mirror_acheteur - Acheteur formation 67 EUR
- 773 - novamira_mirror_audit_acheteur - Acheteur upsell audit 97 EUR
- 774 - novamira_mirror_bump_acheteur - Acheteur order bump migrations 27 EUR

## Funnels FluentCRM

- 38 - SYNC Formation Novamira vers TutorLMS - trigger fluent_cart/order_paid_done - filter product 2900025 - actions sequence 192 (enrol cours 2899133) + sequence 193 (tag 772)
- 39 - SYNC Upsell Audit 97 EUR - trigger fluent_cart/order_paid_done - filter product 2900032 - action apply tag 773 (à enrichir avec email post-achat)
- 40 - SYNC Bump Migrations 27 EUR - trigger fluent_cart/order_paid_done - filter product 2900031 - action apply tag 774 (à enrichir avec email post-achat)

## Cours TutorLMS

Course post 2899133. Déroulement complet documenté dans tutorlms-ids-log.md du même dossier.

## Attachments média

- 2899120 - novamira-mirror-formation-cover.webp - Cover formation 67 EUR + actuellement cover bump 2900031
- 2903727 - novamira-mirror-audit-cover.webp - Cover upsell audit 97 EUR (nouvelle, brand-aligned via HTML+Playwright)

## mu-plugins schoolsWP créés cette session

- wp-content/mu-plugins/schoolswp-tutor-fluentcart-bridge.php - v1.0.0 - Remplace le bouton Enroll Now TutorLMS par redirect vers FluentCart product page (mapping cours vers produit)
- wp-content/mu-plugins/schoolswp-fluentcart-fr-overrides.php - v1.4.0 - Gettext FR 140+ entrées + render_block filter pour status slugs (paid vers payée, Card vers Carte, etc.)
- wp-content/mu-plugins/schoolswp-tutor-fr-overrides.php - v1.0.0 - Override Privacy Policy vers Politique de confidentialité (TutorLMS)

## Template PDF facture

Option receipt_pdf_templates dans table fct_meta (object_type=option). Tous les labels FR (FACTURE / ÉMETTEUR / FACTURÉ À / Numéro de facture / Date / Mode de paiement / Statut du paiement / Sous-total / Réduction / TVA / Livraison / Total) + footer mentions auto-entrepreneur (SIRET 881 547 962 00012 + APE 4791A + TVA 293B + contact).

## Settings FluentCart Stripe

- Mode test (sandbox)
- Account Stripe acct_1KeJr0HftHK3jNaM (FR)
- Compte SCHOOLSWP Administrator
- Live credentials nettoyés (vides) pour éviter le bandeau erreur API
- Webhook configuré URL https://schoolswp.com?fluent-cart=fct_payment_listener_ipn&method=stripe (8 événements actifs)

## Commandes test à nettoyer avant launch

- Order 1 INV-SWP1 - 67 EUR - paid (Card 4242) - Test formation seule, enrolment course 2902488
- Order 2 INV-SWP2 - TBD - TBD - Test probable
- Order 3 INV-SWP3 - 97 EUR - paid (Card 4242) - Test upsell seul, tag 773 retro-appliqué

## Procédure rollback rapide

Toutes les opérations via Novamira execute-php ou phpMyAdmin.

Annuler les 2 nouveaux funnels : supprimer les rows de fc_funnel_sequences où funnel_id IN (39, 40), puis supprimer fc_funnels où id IN (39, 40).

Annuler les 2 nouveaux tags : supprimer fc_subscriber_pivot où object_type pointe sur Tag et object_id IN (773, 774), puis supprimer fc_tags où id IN (773, 774).

Restaurer l'ancienne cover upsell : update wp_postmeta meta_value vers 2899120 où post_id=2900032 et meta_key=_thumbnail_id, puis update fct_product_variations media_id vers 2899120 où post_id=2900032, puis supprimer l'attachment 2903727 via UI Médiathèque.

Remettre les strings FluentCart en EN : supprimer manuellement via Explorer Windows les 3 mu-plugins schoolsWP listés ci-dessus. Restaurer template PDF via UI FluentCart > Storage Settings > Receipt template.

## Pattern HTML+Playwright pour featured images

Voir mémoire reference_featured_images_html_pipeline.md pour le pipeline complet (HTML > capture.mjs > ffmpeg WebP > Novamira upload multipart > execute-php wp_insert_attachment).

Source HTML versionnée pour cover audit : assets/featured-images/post-2900032/slide-01-cover-upsell.html

À répliquer pour cover bump (post 2900031) avec ces ajustements de texte :
- Pretitle BUMP schoolsWP (BUMP en vert, schools en noir, WP en vert)
- Titre Pack avancé / Migrations (2 lignes)
- Baseline Recettes Novamira pour migrations et imports massifs

## Limitations connues

- Le footer PDF n'accepte pas de HTML inline (esc_html appliqué). Le wordmark schoolsWP du footer est rendu en mono-couleur, le WP en vert n'est pas applicable.
- Filter render_block fluent-cart/receipt-meta intercepte le PDF et la page web compte, mais l'ancienne facture INV-SWP3 télécharée AVANT le fix reste en EN (PDF figé).
- Pour Card vers Carte sur les anciennes factures déjà émises, il faut re-télécharger via WP admin (regenerate PDF) ou refaire un test d'achat.

## Order bump activé (2026-05-19)

- Module FluentCart `order_bump` activé via option `fluent_cart_modules_settings`.
- Table `fct_order_promotions` créée par migration (PromotionalInit::maybeMigrateDB).
- Row id 1 : type=order_bump, status=active, src_object_id=7 (variation Pack Migrations 27 €), priority=10.
- Conditions JSON : se déclenche sur le checkout dès que la variation 6 (formation 67 €) est dans le panier.
- Config JSON : aucun discount, pas de free shipping. Coupon désactivé sur la variation bump.
- Hash interne : généré automatiquement à l'insert.

Vérification UI attendue : FluentCart > Promotions > Order Bumps doit montrer "Ajouter le Pack avancé Migrations" en active.

## Emails post-achat + cross-sell (status draft, 2026-05-19)

7 campagnes FluentCRM `funnel_email_campaign` créées en `draft` :

| ID | Funnel | Slug | Sujet | Délai |
| :-: | :-: | :-- | :-- | :-: |
| 204 | 39 | funnel-39-postachat-audit-confirmation | {{first_name}}, ton audit Novamira, on lance quand tu veux | immédiat |
| 205 | 40 | funnel-40-postachat-bump-confirmation | Ton Pack Migrations est dispo dans ton compte | immédiat |
| 206 | 41 | funnel-41-crosssell-audit-e1-checkin | {{first_name}}, comment ça va ton intégration Novamira ? | J+7 |
| 207 | 41 | funnel-41-crosssell-audit-e2-pitch | Le pattern Novamira que personne ne diagnostique seul | J+10 |
| 208 | 41 | funnel-41-crosssell-audit-e3-derniere-fenetre | Dernière fenêtre audit cette semaine | J+14 |
| 209 | 42 | funnel-42-crosssell-bump-e1-checkin-m5 | Module Migrations, ça avance de ton côté ? | J+5 |
| 210 | 42 | funnel-42-crosssell-bump-e2-pitch-pack | 5 recettes Novamira prêtes à déployer (Pack avancé 27 €) | J+12 |

Séquences ajoutées dans `fc_funnel_sequences` (toutes en `draft`) :

- Funnel 39 : seq 2 = send_custom_email → campaign 204.
- Funnel 40 : seq 2 = send_custom_email → campaign 205.
- Funnel 41 : seq 1 wait 7j, seq 2 email 206, seq 3 wait 3j, seq 4 email 207, seq 5 wait 4j, seq 6 email 208, seq 7 end_this_funnel.
- Funnel 42 : seq 1 wait 5j, seq 2 email 209, seq 3 wait 7j, seq 4 email 210, seq 5 end_this_funnel.

Action Michael côté UI FluentCRM :

1. Ouvrir Campaigns > brouillons > relire/ajuster les 7 emails, puis Publish.
2. Ouvrir Automations > funnel 39, puis 40 : publier les nouvelles sequences (status draft → published) une fois la copy validée.
3. Idem funnels 41 et 42, plus flipper le funnel lui-même en Published.
4. Optionnel mais recommandé : ajouter dans 41 et 42 une étape `fluentcrm_if_else` en tête qui exit si tag 773 (resp. 774) déjà présent, pour éviter les cross-sell envoyés aux acheteurs qui ont déjà pris l'option en bundle au checkout.

## Plan test remboursement sandbox

Objectif : valider que l'email de confirmation de remboursement part bien en FR (mu-plugin v1.5 confirme via `__()` que les 4 strings clés sont traduites).

Procédure recommandée (commande fresh, pas les anciens INV-SWP1/3 dont l'email a déjà été envoyé avant le fix) :

1. Lancer un nouveau test d'achat sandbox sur `/item/novamira-mirror/` avec carte Stripe `4242 4242 4242 4242`, exp `12/30`, CVC `123`. Renseigner ton email perso pour recevoir l'email refund.
2. Une fois la commande au statut `paid`, ouvrir FluentCart > Orders > la commande > bouton "Refund" (Stripe sandbox).
3. Sélectionner "Full refund", cocher "Send refund email to customer".
4. Vérifier dans la boîte mail :
   - Sujet = "Confirmation de remboursement - schoolsWP" (PAS "Refund Confirmation from...").
   - Corps : "J'ai traité le remboursement de ta commande récente" + "Merci pour ta compréhension..." + "Le remboursement devrait apparaître sur ton compte sous 5 à 10 jours ouvrés, selon ton mode de paiement.".
   - Montant en € correctement formaté.
5. Vérifier que l'admin reçoit aussi sa notif refund traduite (si tu as activé Admin notifications dans FluentCart Settings > Notifications).

Si une string reste en EN après envoi, c'est une chaîne du template gettext non couverte. Capturer la string EN exacte (depuis l'email reçu), m'envoyer pour l'ajouter au map du mu-plugin schoolswp-fluentcart-fr-overrides.php.

## Plan cleanup commandes test pré-launch

Pré-requis : confirmer avec Michael que tous les tests sont OK et qu'on n'a plus besoin des orders SWP1/2/3.

Ordre des opérations (one-shot execute-php) :

1. Détacher les enrolments TutorLMS auto-créés (course 2899133) pour les customers test : delete wp_posts + wp_postmeta liés au post_type=tutor_enrolled correspondant.
2. Delete fct_order_items où order_id IN (1,2,3).
3. Delete fct_order_transactions où order_id IN (1,2,3).
4. Delete fct_order_addresses où order_id IN (1,2,3).
5. Delete fct_order_operations où order_id IN (1,2,3).
6. Delete fct_order_meta où order_id IN (1,2,3).
7. Delete fct_orders où id IN (1,2,3).
8. Detag les customers test (subscriber_id liés via fct_customers.email) : remove tags 772, 773, 774 si présents.
9. Optionnel : delete fct_customers si plus aucune commande active rattachée.
10. Vider la table fct_carts pour purger les paniers abandonnés test.
11. Reset numérotation invoice : pas nécessaire, le compteur FluentCart est offsétté côté option.

Sécurité : un dry-run AVANT (afficher les rows à supprimer sans les supprimer) puis Michael valide avant le commit réel.
