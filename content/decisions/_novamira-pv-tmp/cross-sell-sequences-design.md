# Cross-sell sequences - Novamira MIRROR

Date : 2026-05-16
Stack : FluentCRM 3.0.5 + FluentCampaign Pro 3.0.3
Objectif : démarcher les acheteurs formation qui n'ont pas pris l'upsell audit ou l'order bump migrations

## Principe

Quand un visiteur achète la formation, le funnel SYNC 38 applique le tag 772 (novamira_mirror_acheteur). Ce tag déclenche deux séquences cross-sell parallèles, qui suivent chacune leur propre cadence et leurs propres conditions de sortie.

L'astuce : chaque séquence vérifie à chaque étape si le contact a entre temps acheté le produit cible (tag 773 audit ou 774 bump). Si oui, exit silencieux. Si non, on continue à pitcher.

## Séquence 1 - Cross-sell Audit personnalisé (97 EUR)

### Trigger

- Event : fluentcrm/contact_tag_added
- Setting tag : 772 (novamira_mirror_acheteur)
- Run once per contact (oui)

### Conditions de sortie permanentes

- Si tag 773 (audit_acheteur) déjà appliqué au moment du trigger : exit immédiat (déjà acheté en bundle)

### Cadence

| Étape | Délai | Action | Condition |
| :-: | :-: | :-- | :-- |
| 1 | J+7 | Conditional split sur tag 773 | YES → END / NO → étape 2 |
| 2 | immédiat | Send email "Comment va ton intégration Novamira ?" | - |
| 3 | J+3 | Conditional split sur tag 773 | YES → END / NO → étape 4 |
| 4 | immédiat | Send email "Le cas pratique audit que tu peux résoudre seul" | - |
| 5 | J+4 | Conditional split sur tag 773 | YES → END / NO → étape 6 |
| 6 | immédiat | Send email "Dernière fenêtre audit -10% jusqu'à dimanche" | - |

### Drafts emails (placeholders à rédiger par Michael)

**Email 1 (J+7)** - Tone soft, valeur, pas pitch direct
- Subject : "{{contact.first_name}}, comment vas ton intégration Novamira ?"
- Hook : check-in, demande où le contact en est, propose 1-2 ressources gratuites
- CTA : aucun pitch direct, juste lien vers ressource ou FAQ
- Objectif : engagement, ouverture

**Email 2 (J+10)** - Pitch direct mais doux
- Subject : "Le pattern que personne ne sait diagnostiquer seul"
- Hook : raconte 1 cas concret où l'audit a débloqué un freelance bloqué sur un staging
- Pitch : présente l'audit (45 min Loom + 5 actions + routine perso + Q/R 7j) - 97 EUR
- CTA : lien vers /item/novamira-mirror-upsell-audit/

**Email 3 (J+14)** - Urgence soft
- Subject : "Dernière fenêtre cette semaine"
- Hook : rappelle l'audit + ajoute une réduction limitée (-10% jusqu'à dimanche) ou un bonus (audit + routine premium incluse)
- CTA : lien vers /item/novamira-mirror-upsell-audit/ avec code promo

## Séquence 2 - Cross-sell Pack avancé Migrations (27 EUR)

### Trigger

- Event : fluentcrm/contact_tag_added
- Setting tag : 772 (novamira_mirror_acheteur)
- Run once per contact (oui)

### Conditions de sortie permanentes

- Si tag 774 (bump_acheteur) déjà appliqué au moment du trigger : exit immédiat

### Cadence

| Étape | Délai | Action | Condition |
| :-: | :-: | :-- | :-- |
| 1 | J+5 | Conditional split sur tag 774 | YES → END / NO → étape 2 |
| 2 | immédiat | Send email "Tu en es où dans le module Migrations ?" | - |
| 3 | J+7 | Conditional split sur tag 774 | YES → END / NO → étape 4 |
| 4 | immédiat | Send email "Le pack avancé = 5 recettes prêtes à déployer" | - |

### Drafts emails (placeholders à rédiger par Michael)

**Email 1 (J+5)** - Engagement check sur le module M5
- Subject : "{{contact.first_name}}, le module Migrations te semble OK ?"
- Hook : check-in spécifique sur le module M5 (Workflows fondamentaux : conversion Classic vers Gutenberg, nettoyage transients, création posts via CSV, etc.)
- CTA : aucun pitch direct, juste rappelle qu'il existe un pack avancé si besoin de recettes prêtes-à-l'emploi

**Email 2 (J+12)** - Pitch direct sur le pack
- Subject : "5 recettes Novamira prêtes à déployer en 1 commande"
- Hook : raconte 1 cas d'usage où le pack a sauvé 4h de boulot manuel
- Pitch : présente le pack (5 recettes WP-CLI, scripts PHP commentés, manifeste rollback, modèle de log session) - 27 EUR
- CTA : lien vers /item/novamira-mirror-bump-migrations/ (slug à confirmer)

## Garde-fous techniques

- Toutes les sequences en draft initial. Michael complète les emails puis publish.
- Conditional split utilise l'action FluentCRM `fluentcrm_check_tag` ou équivalent `tag_based_branching` (à confirmer côté UI).
- Le tag 772 est appliqué une seule fois par achat (la condition run_once est posée). Donc ces 2 séquences se déclenchent une seule fois par acheteur.
- Si Michael propose plus tard une variation tarifaire (audit -10% en série), prévoir un tag de coupon pour exit la séquence après usage.

## Implémentation

Les funnels coquilles 41 (cross-sell audit) et 42 (cross-sell bump) sont créés en DRAFT côté DB par execute-php. Michael ouvre l'UI FluentCRM > Automations > funnel 41 puis 42, complète les actions send_custom_email avec ses propres emails rédigés, valide, et bascule en Published quand prêt.

Pour le pitch des emails, garde-fous brand schoolsWP :
- Tutoiement strict (jamais vouvoyer)
- Je au singulier (jamais nous/notre/on)
- Voix authentique, pas marketing creep
- Mention SIRET en footer (déjà géré par template global FluentCRM)
- Wordmark schoolsWP avec WP en vert via inline HTML (le footer FluentCRM HTML accepte)

## Métriques à suivre

Après 30 jours de mise en prod :
- Taux d'ouverture par email (objectif >40%)
- Taux de conversion cross-sell audit (objectif 5-8% des acheteurs formation)
- Taux de conversion cross-sell bump (objectif 12-18% - plus accessible car 27 EUR)
- Taux de désabonnement (objectif <0.5% par email)

Si conversion <2% sur 30 jours, refaire les drafts emails ou raccourcir les délais.
