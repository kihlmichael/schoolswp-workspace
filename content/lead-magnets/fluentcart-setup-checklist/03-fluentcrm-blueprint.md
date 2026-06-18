# Blueprint FluentCRM — Checklist FluentCart Setup

Plan de construction du tunnel. Réplique le pattern éprouvé du lead magnet welcome-template-fluentcrm
(form 15 vers merci vers PDF vers funnel délais cumulés vers tag bascule), adapté à 7 emails.

Statut : NON CONSTRUIT. Build à lancer quand les gates ci-dessous sont satisfaites.

---

## Gates avant build live

| Gate | Description | Bloque |
|---|---|---|
| **G1 — PDF en WP media** | Le PDF est sur Drive uniquement. Le publier en média WP schoolswp.com, récupérer l'URL stable (URL_PDF). | Email 1, page merci |
| **G2 — Pages WP** | Construire la landing /checklist-fluentcart-setup/ (form embarqué) + la page merci /merci-checklist-fluentcart/ (noindex, lien PDF). | Capture |
| **G3 — LAUNCH vendable** | La formation LAUNCH doit avoir une page de vente + checkout actifs avant d'activer les emails 5 à 7 (offre -50%). Roadmap : LAUNCH live vers J+35. | Emails 5, 6, 7 |
| **G4 — Témoignage** | Email 6 : recueillir un vrai témoignage de beta testeur, sinon garder la version "parcours type" (aucune citation inventée). | Email 6 (version finale) |
| **G5 — Articles cibles** | Les liens E2/E3/E4 pointent vers des articles schoolsWP (Free vs Pro, Migration EDD, Abonnements/LTV). Vérifier qu'ils existent ou les écrire, sinon pointer vers le plus proche. | Emails 2, 3, 4 |
| **G6 — Discord** | Lien d'invitation Discord schoolsWP (URL_DISCORD), mentionné dans le PDF. | PDF / bonus |

**Séquençage recommandé** : G1 + G2 + G5 permettent de lancer la capture et les emails de valeur (1 à 4) dès maintenant. Les emails 5 à 7 (offre) restent désactivés tant que G3 n'est pas satisfaite. On peut donc ouvrir le tunnel en "mode acquisition seule", puis activer la bascule offre à la sortie de LAUNCH.

---

## Tags à créer

| Tag | Famille | Rôle |
|---|---|---|
| freebie_fluentcart_setup_fr | trigger | Déclenche le funnel. Appliqué par le form. |
| lang_fr (768, existant) | langue | Identification langue. Appliqué par le form. |
| seq_fluentcart_e1 ... e7 | traçabilité | Un par email, posé à l'envoi. |
| client_launch_formation | conversion | Posé à l'achat de LAUNCH. Sert de goal de sortie. |

Convention respectée (voir reference_fluentcrm_tags_convention) : 1 trigger + 1 lang sur le form.

---

## Structure du funnel

- **Nom** : SEQ - LM Checklist FluentCart Setup
- **Trigger** : contact ajouté au tag freebie_fluentcart_setup_fr
- **Réglages** : select_type any, subscription_status subscribed
- **Séquence** (délais cumulatifs depuis l'inscription) :

| Ordre | Action | Délai cumulé | Campaign |
|---|---|---|---|
| 1 | Envoi E1 + tag seq_fluentcart_e1 | J0 | à créer |
| 2 | Envoi E2 + tag seq_fluentcart_e2 | J2 | à créer |
| 3 | Envoi E3 + tag seq_fluentcart_e3 | J4 | à créer |
| 4 | Envoi E4 + tag seq_fluentcart_e4 | J7 | à créer |
| 5 | Goal d'achat (sortie si client_launch_formation) | J7+ | — |
| 6 | Envoi E5 + tag seq_fluentcart_e5 | J10 | à créer |
| 7 | Envoi E6 + tag seq_fluentcart_e6 | J12 | à créer |
| 8 | Envoi E7 + tag seq_fluentcart_e7 | J14 | à créer |
| 9 | Tag sequence_fluentcart_termine + end | J14 | — |

**Sortie sur conversion** : le goal d'achat (ordre 5) sort les acheteurs LAUNCH avant les emails 5 à 7. Ne PAS utiliser une action de tag linéaire après un goal optionnel : leçon du tunnel welcome (une action de tag placée après un goal optionnel s'applique à TOUT LE MONDE, pas seulement aux acheteurs). La sortie doit être un vrai goal qui gate le flux.

---

## Méthode de build

- Le corps des emails vit dans la table des campaigns FluentCRM (colonne email_body), PAS dans les settings de la séquence de funnel (qui ne fait que référencer la campaign).
- Le MCP de création de funnel FluentCRM est cassé (500 systématique, voir reference_fluentcrm_mcp_funnel_create_broken). Construire le funnel via PHP exécuté (Novamira) sur la table des séquences de funnel, ou via l'UI FluentCRM.
- Colonnes de la séquence de funnel : action_name, type, settings (PHP-serialize), conditions (vide), delay et c_delay (cumulatif en secondes), sequence (ordre), parent_id 0.
- Liens affiliés FluentCart : utiliser la ref by=40 (voir feedback_wpmanageninja_affiliate_refs), via cloak mu-plugin si possible.
- Test bout-en-bout sûr : ajouter le tag déclencheur à un contact de test pour lancer le funnel, annuler l'automation ensuite pour nettoyer, et utiliser l'envoi d'email de test pour vérifier le contenu sans inscription (méthode validée sur le tunnel welcome).

---

## Substitutions de placeholders

| Token | Valeur (à renseigner au build) |
|---|---|
| URL_PDF | URL média WP stable du PDF (gate G1) |
| URL_FREE_VS_PRO | Article schoolsWP "FluentCart Free vs Pro" |
| URL_MIGRATION_EDD | Article schoolsWP "Migrer de EDD vers FluentCart" |
| URL_SUBSCRIPTIONS_LTV | Article schoolsWP "Abonnements FluentCart et valeur client" |
| URL_LAUNCH | Page de vente formation LAUNCH (gate G3) |
| URL_BUNDLE | Page bundle LAUNCH+SHIP+CART |
| URL_DISCORD | Invitation Discord schoolsWP |

Vérifier qu'aucun placeholder à double accolades ne subsiste avant publication (cf. incident CTA_STANDARD : grep des placeholders avant push).

---

## KPIs à suivre

- **Taux d'opt-in** de la landing (visiteurs vers inscrits).
- **Taux d'ouverture** par email (E1 à E7).
- **Taux de clic** vers la destination de chaque email (PDF, articles, LAUNCH).
- **Taux de réponse** à l'email 1 (signal d'engagement direct).
- **Taux de conversion** séquence vers achat LAUNCH (tag client_launch_formation).
- **Taux de désinscription** par email (alerte si pic sur E5, l'email d'offre).

---

## Cohérence funnel (récap)

Landing (promesse : ouvrir sa boutique FluentCart en une demi-journée) vers inscription vers Email 1 (livre le PDF, même promesse) vers PDF (7 phases). Emails 2 à 4 nourrissent. Emails 5 à 7 proposent LAUNCH, qui prolonge exactement la checklist en méthode guidée. Aucune promesse non tenue, aucune rupture de ton.
