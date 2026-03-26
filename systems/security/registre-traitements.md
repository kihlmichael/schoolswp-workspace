# Registre des traitements — Art. 30 RGPD

**Responsable de traitement** : Michael KIHL — contact@michaelkihl.fr
**Date** : 2026-03-15
**Mise à jour** : À chaque nouveau traitement ou modification substantielle

---

## Traitement 1 — Génération de contenu SEO (Content Machine)

| Champ | Valeur |
|-------|--------|
| **Finalité** | Génération automatisée d'articles SEO pour schoolswp.com |
| **Base légale** | Art. 6.1.f — Intérêt légitime (activité éditoriale) |
| **Catégories de données** | Mots-clés, sujets (données non-personnelles) |
| **Catégories de personnes** | Aucune (données éditoriales internes) |
| **Destinataires** | Anthropic Claude (génération), Google Sheets/Docs (stockage), Notion (tracking) |
| **Transferts hors UE** | Anthropic (🇺🇸 USA) — SCCs à vérifier |
| **Durée conservation** | Indéfinie — **Action : limiter à 36 mois** |
| **Mesures sécurité** | HTTPS, API key chiffrée, validation inputs Google Sheets |
| **Sous-traitants** | Anthropic, Google, Notion |

---

## Traitement 2 — Analyse SEO (Google Search Console Sync)

| Champ | Valeur |
|-------|--------|
| **Finalité** | Suivi des performances SEO du site schoolswp.com |
| **Base légale** | Art. 6.1.f — Intérêt légitime (analytics propre) |
| **Catégories de données** | URLs de pages, clics, impressions, CTR, position (données agrégées — non-personnelles) |
| **Catégories de personnes** | Visiteurs anonymes du site (données agrégées, non individualisées) |
| **Destinataires** | Google Search Console (collecte), Notion (stockage KPI) |
| **Transferts hors UE** | Google (🇺🇸 USA) — Google Cloud SCCs ✅ |
| **Durée conservation** | Indéfinie — **Action : archiver > 24 mois** |
| **Mesures sécurité** | OAuth2 scope limité (lecture seule GSC), HTTPS |
| **Sous-traitants** | Google (collecte + stockage), Notion |

---

## Traitement 3 — Monitoring contenu (Thruuu)

| Champ | Valeur |
|-------|--------|
| **Finalité** | Surveillance des positions et performances des articles publiés |
| **Base légale** | Art. 6.1.f — Intérêt légitime (veille concurrentielle) |
| **Catégories de données** | URLs, positions SERP, données de requêtes (non-personnelles) |
| **Catégories de personnes** | Aucune |
| **Destinataires** | Thruuu API, Google Sheets (via n8n) |
| **Transferts hors UE** | Thruuu (localisation à clarifier) |
| **Durée conservation** | Durée de vie du JWT (~30j) — données Google Sheets indéfinies |
| **Mesures sécurité** | JWT Bearer token, rotation 90 jours |
| **Sous-traitants** | Thruuu, Google |

---

## Traitement 4 — Telegram Bot (@schoolswpbot)

| Champ | Valeur |
|-------|--------|
| **Finalité** | Notifications opérationnelles (statuts workflows, alertes) |
| **Base légale** | Art. 6.1.a — Consentement (via CCPA handler dans l'app) |
| **Catégories de données** | User ID Telegram, username, messages, métadonnées (timezone, langue) |
| **Catégories de personnes** | Utilisateur du bot (Michael KIHL uniquement en production) |
| **Destinataires** | Telegram (stockage messages) |
| **Transferts hors UE** | Telegram (🇷🇺 Russie / 🇺🇸 USA) — ❌ **NON CONFORME** |
| **Durée conservation** | Indéfinie (Telegram servers) |
| **Mesures sécurité** | Bot token gitignored, ccpa.config.json gitignored |
| **Sous-traitants** | Telegram |
| **Action requise** | Évaluer arrêt ou migration vers alternative EU |

---

## Traitement 5 — Logs exécution n8n

| Champ | Valeur |
|-------|--------|
| **Finalité** | Audit et débogage des workflows automatisés |
| **Base légale** | Art. 6.1.f — Intérêt légitime (sécurité opérationnelle) |
| **Catégories de données** | Inputs/outputs workflows, tokens OAuth transitoires, timestamps |
| **Catégories de personnes** | Aucune (données opérationnelles) |
| **Destinataires** | n8n (PostgreSQL interne) |
| **Transferts hors UE** | Aucun (hébergement EU — wp1.host) |
| **Durée conservation** | ⚠️ À configurer — **Action : 30 jours max** |
| **Mesures sécurité** | PostgreSQL chiffré (N8N_ENCRYPTION_KEY), HTTPS n8n UI |
| **Sous-traitants** | wp1.host (hébergeur) |
| **Action requise** | Activer rétention 30j dans n8n Settings |

---

## Traitement 6 — Scraping social (RapidAPI LinkedIn/Twitter/Instagram/YouTube)

| Champ | Valeur |
|-------|--------|
| **Finalité** | Veille concurrentielle, analyse de contenu social |
| **Base légale** | Art. 6.1.f — Intérêt légitime (veille) — **À réévaluer** |
| **Catégories de données** | Profils publics, posts, engagements (données pseudonymisées) |
| **Catégories de personnes** | Auteurs de contenus publics |
| **Destinataires** | RapidAPI (collecte), n8n (traitement) |
| **Transferts hors UE** | RapidAPI (🇺🇸 USA) — SCCs à vérifier |
| **Durée conservation** | Non persistées (usage ponctuel) |
| **Mesures sécurité** | API key partagée (4 services) — **Action : séparer les clés** |
| **Sous-traitants** | RapidAPI |
| **Action requise** | Vérifier conformité GDPR scraping réseaux sociaux (Art. 6.4) |

---

## Sous-traitants — Tableau récapitulatif

| Sous-traitant | Rôle | DPA | SCCs | Contact DPA |
|---------------|------|-----|------|-------------|
| Anthropic | Génération contenu IA | ❌ À signer | ⚠️ À vérifier | anthropic.com/legal/dpa |
| OpenAI | Audit SEO IA | ❌ À signer | ⚠️ À vérifier | openai.com/policies/dpa |
| Google | Storage + GSC + OAuth | ✅ Cloud Terms | ✅ SCCs | cloud.google.com/terms/data-processing-addendum |
| Notion | KPI tracking | ❌ À signer | ⚠️ À vérifier | notion.so/dpa |
| Airtable | Content DB | ❌ À signer | ⚠️ À vérifier | airtable.com/legal/dpa |
| Slack | Notifications | ❌ À signer | ⚠️ À vérifier | slack.com/terms-of-service/data-processing |
| Discord | Notifications | ❌ À signer | ⚠️ À vérifier | discord.com/developers/docs/policies |
| Firecrawl | Web scraping | ❌ À signer | ⚠️ À vérifier | firecrawl.dev |
| RapidAPI | Social data | ❌ À signer | ⚠️ À vérifier | rapidapi.com/terms |
| Telegram | Bot / messaging | ❌ AUCUN | ❌ NON CONFORME | — |
| HeyGen | Vidéo IA | ❌ À signer | ⚠️ À vérifier | heygen.com/legal |
| ElevenLabs | Voix IA | ❌ À signer | ✅ UK Adequacy | elevenlabs.io/dpa |
| wp1.host (n8n) | Hébergement | ⚠️ À vérifier | ✅ EU probable | wp1.host |

---

*Ce registre doit être mis à jour à chaque nouveau service intégré ou modification de traitement.*
