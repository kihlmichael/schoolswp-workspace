# Analytics & Tracking — schoolsWP Marketing

Configuration et audit du tracking analytics pour sites WordPress (GA4, conversions, événements).

## Triggers

- "GA4", "Google Analytics"
- "tracking", "analytics"
- "mesurer les conversions"
- "événements", "events"

## Stack analytics recommandé

### Configuration type schoolsWP

```
┌─────────────────────────────────────────────┐
│              Google Tag Manager             │
│         (orchestration des tags)            │
├─────────────────┬───────────────────────────┤
│      GA4        │    Autres pixels          │
│   (analytics)   │  (Meta, LinkedIn, etc.)   │
└─────────────────┴───────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────┐
│           WordPress + Plugins               │
│  (MonsterInsights, GTM4WP, ou code custom)  │
└─────────────────────────────────────────────┘
```

## Configuration GA4

### Checklist installation

```
COMPTE & PROPRIÉTÉ
□ Compte GA4 créé (pas Universal Analytics)
□ Propriété correctement nommée
□ Fuseau horaire correct
□ Devise correcte (EUR)

DATA STREAM
□ Stream Web configuré
□ Mesure améliorée activée
   □ Pages vues
   □ Défilement
   □ Clics sortants
   □ Recherche sur site
   □ Engagement vidéo
   □ Téléchargements de fichiers

INSTALLATION
□ Tag installé sur toutes les pages
□ Vérifié dans GA4 Realtime
□ Vérifié avec GA Debugger
```

### Installation WordPress

**Option 1 : Plugin (recommandé pour non-dev)**
```
MonsterInsights ou Site Kit by Google
→ Connexion OAuth
→ Configuration guidée
```

**Option 2 : GTM (recommandé pour flexibilité)**
```
Plugin GTM4WP
→ Container ID dans settings
→ Configuration des triggers dans GTM
```

**Option 3 : Code (contrôle total)**
```php
// Dans functions.php ou plugin custom
add_action( 'wp_head', function() {
  ?>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXX');
  </script>
  <?php
}, 1 );
```

## Événements à tracker

### Événements essentiels schoolsWP

| Événement | Trigger | Paramètres |
|-----------|---------|------------|
| `generate_lead` | Soumission formulaire | form_name, page |
| `sign_up` | Inscription newsletter | method |
| `begin_checkout` | Clic bouton achat | value, items |
| `purchase` | Achat complété | value, transaction_id, items |
| `view_item` | Vue page formation | item_name, item_category |
| `scroll_depth` | Scroll 25/50/75/90% | percent_scrolled |
| `file_download` | Téléchargement PDF | file_name, file_extension |
| `video_progress` | Vidéo 25/50/75/100% | video_title, percent |
| `click_cta` | Clic CTA principal | cta_text, cta_location |

### Configuration événement personnalisé

**Dans GTM :**
```
Trigger : Click - All Elements
Condition : Click Text contains "Démarrer la formation"

Tag : GA4 Event
Event Name : click_cta
Parameters :
  - cta_text : {{Click Text}}
  - cta_location : {{Page Path}}
  - page_title : {{Page Title}}
```

**En code (gtag) :**
```javascript
document.querySelectorAll('.cta-principal').forEach(btn => {
  btn.addEventListener('click', () => {
    gtag('event', 'click_cta', {
      cta_text: btn.textContent,
      cta_location: window.location.pathname
    });
  });
});
```

## Conversions GA4

### Définir les conversions

```
GA4 > Admin > Events > Mark as conversion

CONVERSIONS PRIORITAIRES
✅ generate_lead (formulaire contact/lead magnet)
✅ sign_up (inscription newsletter)
✅ purchase (achat formation)
✅ begin_checkout (intention d'achat)
```

### Valeur des conversions

```javascript
// Achat avec valeur
gtag('event', 'purchase', {
  transaction_id: 'T12345',
  value: 397.00,
  currency: 'EUR',
  items: [{
    item_id: 'FORM-PERF-01',
    item_name: 'Formation Performance WordPress',
    price: 397.00,
    quantity: 1
  }]
});
```

## Funnel tracking

### Funnel type formation schoolsWP

```
ÉTAPES À TRACKER

1. view_item
   └── Vue page de vente

2. add_to_cart (optionnel)
   └── Clic "Je veux cette formation"

3. begin_checkout
   └── Arrivée page paiement

4. add_payment_info
   └── Saisie infos paiement

5. purchase
   └── Confirmation achat
```

### Rapport funnel GA4

```
GA4 > Explore > Funnel exploration

Étapes :
1. page_view (page: /formation-performance)
2. click_cta (cta: "Démarrer")
3. begin_checkout
4. purchase

Analyse :
- Taux de passage entre étapes
- Points de friction
- Segmentation par source
```

## Audit analytics existant

### Checklist audit

```
INSTALLATION
□ GA4 présent sur toutes les pages
□ Pas de double tracking
□ GTM bien configuré (si utilisé)
□ Pas de code en double

CONFIGURATION
□ Mesure améliorée activée
□ Conversions définies
□ Paramètres UTM tracés
□ Référents non exclus par erreur
□ Filtres internes (IP équipe)

DATA QUALITY
□ Taux de rebond réaliste (pas 0% ni 100%)
□ Durée session cohérente
□ Pas de spam referral
□ Sessions vs Users logique

ÉVÉNEMENTS
□ Événements clés configurés
□ Paramètres renseignés
□ Conversions marquées
□ Valeurs assignées
```

### Problèmes courants WordPress

| Problème | Symptôme | Solution |
|----------|----------|----------|
| Double tracking | Rebond 0%, sessions doublées | Vérifier plugins + code |
| Cache agressif | Events non envoyés | Exclure scripts analytics du cache |
| Consent mode | Données partielles | Configurer correctement le consentement |
| SPA/AJAX | Pages vues manquantes | Events manuels ou plugin adapté |
| WooCommerce | Pas d'e-commerce | Configurer enhanced ecommerce |

## RGPD & Consentement

### Configuration conforme

```
AVANT CONSENTEMENT
gtag('consent', 'default', {
  'analytics_storage': 'denied',
  'ad_storage': 'denied'
});

APRÈS ACCEPTATION
gtag('consent', 'update', {
  'analytics_storage': 'granted'
});
```

### Plugins WordPress recommandés

- **Complianz** : Gestion consentement + GTM intégration
- **CookieYes** : Bannière + blocage scripts
- **GDPR Cookie Compliance** : Solution légère

## Rapports essentiels

### Tableau de bord schoolsWP

```
ACQUISITION
- Sessions par source/medium
- Nouveaux vs Returning
- Campagnes (UTM)

ENGAGEMENT
- Pages les plus vues
- Temps moyen par page
- Taux de scroll

CONVERSION
- Taux de conversion par source
- Valeur par conversion
- Funnel drop-off

TECHNIQUE
- Core Web Vitals (CrUX)
- Appareils
- Navigateurs
```

### Looker Studio (Data Studio)

Template de dashboard :
```
Page 1 : Vue d'ensemble
- KPIs principaux (sessions, users, conversions)
- Tendance 30 jours
- Top sources

Page 2 : Acquisition
- Breakdown par canal
- Performance campagnes
- Landing pages

Page 3 : Conversions
- Funnel visualisé
- Conversions par page
- Valeur générée

Page 4 : Contenu
- Pages populaires
- Engagement articles
- Recherches internes
```

## Checklist finale

```
INSTALLATION
□ GA4 configuré correctement
□ GTM si nécessaire
□ Vérifié en temps réel

ÉVÉNEMENTS
□ Événements clés définis
□ Conversions marquées
□ Valeurs configurées

CONFORMITÉ
□ Bannière consentement
□ Consent mode configuré
□ Documentation RGPD

REPORTING
□ Dashboard configuré
□ Alertes importantes
□ Accès équipe
```

## Ressources

- [ab-testing.md](../conversion/ab-testing.md) — Tests avec analytics
- [page-cro.md](../conversion/page-cro.md) — Optimisation basée données
- [GA4 Documentation](https://developers.google.com/analytics/devguides/collection/ga4)
