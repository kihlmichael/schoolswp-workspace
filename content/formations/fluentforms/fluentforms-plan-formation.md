# FluentForms - Plan de formation schoolsWP

## Architecture globale

```
FluentForms/
├── FRM-011 : Quick Start (offerte)              → Lead magnet, 5 lecons, ~30 min
└── FRM-012 : Masterclass Formulaires (premium)  → 7 modules, ~50 lecons, ~7h
```

**Plateforme** : TutorLMS Pro sur schoolsWP
**Format** : Videos HeyGen + voix ElevenLabs (francais, tutoiement)
**Page builder** : Gutenberg + Kadence Blocks (theme Kadence)

---

## FRM-011 - FluentForms Quick Start (offerte)

**Objectif** : Creer un formulaire de contact professionnel + capture d'email en 30 min.
**Role** : Lead magnet → upsell Masterclass.
**Acces** : 100% gratuit.

### Lecon 1 - Pourquoi tes formulaires WordPress sont nuls (et comment les reparer) (5 min)
- Le probleme : Contact Form 7 basique, pas de design, pas d'integrations, pas de donnees
- FluentForms : drag-and-drop, 35+ champs gratuits, logique conditionnelle, anti-spam, integrations
- Ce qu'on va faire : 2 formulaires pro en 30 min (contact + capture email)

### Lecon 2 - Installer FluentForms en 2 minutes (5 min)
- Extensions → Ajouter → "fluent forms"
- Activer, tour du dashboard
- Les formulaires pre-configures (templates)
- Conseil : "La version gratuite suffit pour 90% des besoins"

### Lecon 3 - Creer un formulaire de contact pro (8 min)
- Nouveau formulaire → template "Contact Form" ou page blanche
- Drag-and-drop : nom, email, sujet (select), message (textarea)
- Anti-spam : Honeypot + reCAPTCHA/Turnstile
- Notification email : configurer l'adresse de reception
- Message de confirmation personnalise
- Inserer dans une page avec le shortcode ou le bloc Gutenberg

### Lecon 4 - Creer un formulaire de capture d'email (8 min)
- Formulaire minimaliste : prenom + email + bouton "Je m'inscris"
- Connecter a FluentCRM (si installe) ou afficher les soumissions dans le dashboard
- Design inline (horizontal) vs vertical
- Ou placer le formulaire : sidebar, footer, popup, page dediee
- Conseil : "Moins de champs = plus d'inscriptions. Prenom + email, c'est tout."

### Lecon 5 - Personnaliser le design et publier (4 min)
- Styler le formulaire : couleurs, bordures, boutons (via le styler integre ou CSS custom basique)
- Preview sur mobile
- Recap : 2 formulaires pro, en ligne, en 30 min
- Teaser Masterclass : logique conditionnelle, paiements, multi-step, FluentCRM, quiz

---

## FRM-012 - FluentForms Masterclass Formulaires (premium)

### Module 1 - Fondations (6 lecons)

| # | Lecon | Duree |
|---|---|---|
| 1.1 | FluentForms Free vs Pro : tout debloquer ou rester gratuit ? | 8 min |
| 1.2 | L'interface du builder : champs, settings, preview | 8 min |
| 1.3 | Les 35+ types de champs (tour complet avec exemples) | 10 min |
| 1.4 | Notifications email : configurer, personnaliser, conditionner | 8 min |
| 1.5 | Anti-spam : Honeypot, reCAPTCHA, hCaptcha, Turnstile | 6 min |
| 1.6 | Import/Export et migration depuis CF7, WPForms, Gravity Forms | 8 min |

### Module 2 - Logique conditionnelle (7 lecons)

| # | Lecon | Duree |
|---|---|---|
| 2.1 | Qu'est-ce que la logique conditionnelle (et pourquoi c'est puissant) | 6 min |
| 2.2 | Afficher/masquer des champs selon les reponses | 8 min |
| 2.3 | Notifications conditionnelles : email different selon le choix | 8 min |
| 2.4 | Messages de confirmation conditionnels | 6 min |
| 2.5 | Advanced Conditional Groups (Pro) : combiner plusieurs conditions | 10 min |
| 2.6 | Cas pratique : formulaire de devis automatique | 10 min |
| 2.7 | Cas pratique : formulaire d'inscription evenement avec options | 8 min |

### Module 3 - Formulaires avances (8 lecons)

| # | Lecon | Duree |
|---|---|---|
| 3.1 | Multi-step forms : diviser un long formulaire en etapes | 10 min |
| 3.2 | Conversational forms : l'alternative Typeform gratuite | 10 min |
| 3.3 | Calculs dynamiques : devis, simulateurs, calculateurs | 10 min |
| 3.4 | Upload de fichiers et images | 6 min |
| 3.5 | Save & Resume : sauvegarder et reprendre plus tard | 6 min |
| 3.6 | Creation de posts WordPress depuis un formulaire | 8 min |
| 3.7 | Enregistrement utilisateur via formulaire | 8 min |
| 3.8 | AI Form Builder : creer un formulaire par prompt | 6 min |

### Module 4 - Paiements (7 lecons)

| # | Lecon | Duree |
|---|---|---|
| 4.1 | Les passerelles de paiement FluentForms (Stripe, PayPal, Mollie) | 8 min |
| 4.2 | Creer un formulaire de paiement simple (produit ou service) | 10 min |
| 4.3 | Paiements recurrents : abonnements et subscriptions | 8 min |
| 4.4 | Tarification conditionnelle : prix qui change selon les options | 10 min |
| 4.5 | Gestion d'inventaire : limiter les quantites disponibles | 6 min |
| 4.6 | Coupons de reduction dans les formulaires | 6 min |
| 4.7 | Cas pratique : formulaire de reservation avec paiement | 10 min |

### Module 5 - FluentForms + FluentCRM (7 lecons)

| # | Lecon | Duree |
|---|---|---|
| 5.1 | Pourquoi connecter tes formulaires a ton CRM | 6 min |
| 5.2 | Configurer l'integration FluentForms → FluentCRM | 8 min |
| 5.3 | Listes et tags automatiques selon le formulaire soumis | 10 min |
| 5.4 | Tags dynamiques : tagger selon les reponses du formulaire | 10 min |
| 5.5 | Declencher une automation FluentCRM a la soumission | 10 min |
| 5.6 | Cas pratique : lead magnet → tag → sequence email → upsell | 12 min |
| 5.7 | Cas pratique : formulaire inscription formation → FluentCRM → TutorLMS | 10 min |

### Module 6 - Quiz, surveys et analytics (6 lecons)

| # | Lecon | Duree |
|---|---|---|
| 6.1 | Quiz builder : creer un quiz avec scoring | 10 min |
| 6.2 | Personality quiz : resultats differents selon les reponses | 8 min |
| 6.3 | Surveys et sondages : collecter des donnees structurees | 8 min |
| 6.4 | Le Reports Dashboard : analyser les soumissions | 8 min |
| 6.5 | PDF generator : transformer les soumissions en PDF | 8 min |
| 6.6 | Partial entries : analyser les abandons de formulaire | 6 min |

### Module 7 - Ecosysteme et integrations (9 lecons)

| # | Lecon | Duree |
|---|---|---|
| 7.1 | L'ecosysteme WPManageNinja au complet | 8 min |
| 7.2 | FluentForms + FluentSMTP : delivrabilite email | 6 min |
| 7.3 | FluentForms + FluentBooking : prise de rendez-vous | 8 min |
| 7.4 | FluentForms + FluentSupport : soumission → ticket support | 8 min |
| 7.5 | FluentForms + Brevo (Sendinblue) : email marketing FR | 8 min |
| 7.6 | FluentForms + Google Sheets : centraliser les donnees | 6 min |
| 7.7 | Webhooks et Zapier : connecter a 3000+ apps | 10 min |
| 7.8 | Formulaires RGPD : consentement, mentions legales, conformite | 10 min |
| 7.9 | FluentForms vs WPForms vs Gravity Forms : verdict schoolsWP | 10 min |

**Total Masterclass** : 7 modules, 50 lecons, ~7h

---

## Recapitulatif

| Formation | Modules | Lecons | Duree | Acces |
|---|---|---|---|---|
| FRM-011 Quick Start | 1 | 5 | ~30 min | Gratuit |
| FRM-012 Masterclass | 7 | 50 | ~7h | Premium |
| **Total** | **8** | **55** | **~7h30** | |

## Pipeline de production

1. **Recherche** : terminee
2. **Plan** : termine
3. **Scripts** : a produire - Quick Start (5) puis Masterclass (50)
4. **Production video** : HeyGen + ElevenLabs
5. **Publication** : TutorLMS sur schoolsWP
