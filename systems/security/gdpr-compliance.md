# Conformité GDPR — schoolsWP OS

**Date** : 2026-03-15
**Responsable** : Michael KIHL — contact@michaelkihl.fr
**Scope** : Agents Python, workflows n8n, services tiers, Telegram Bot
**Score global** : ⚠️ PARTIELLEMENT CONFORME — 5/10

---

## Statut par article GDPR

| Article | Intitulé | Statut | Action |
|---------|---------|--------|--------|
| Art. 5 | Principes (minimisation, limitation durée) | ⚠️ | Définir rétention logs n8n ≤ 30j |
| Art. 6 | Base légale | ✅ | Intérêt légitime documenté |
| Art. 13-14 | Information des personnes | ⚠️ | Notice privacy WordPress à créer |
| Art. 15-22 | Droits des personnes | ❌ | Procédures à implémenter |
| Art. 25 | Privacy by design | ⚠️ | Validation inputs Google Sheets OK — rétention à faire |
| Art. 28 | Contrats sous-traitants (DPA) | ❌ | DPA manquants pour 8 services |
| Art. 30 | Registre des traitements | ❌ | À créer (voir `registre-traitements.md`) |
| Art. 32 | Sécurité | ✅ | Pre-commit, gitignore, rotation clés, safe_path |
| Art. 33-34 | Notification incidents | ⚠️ | Procédure en place — notif CNIL 72h à formaliser |
| Art. 44-49 | Transferts hors UE | ❌ | 9 services USA sans SCCs confirmés |

---

## Données personnelles traitées

### Ce qui EST traité (données non-personnelles)
- Mots-clés SEO, sujets d'articles, stratégie éditoriale
- URLs Google Search Console (clics, impressions, CTR, position)
- Métadonnées articles (scores, piliers, intents)

### Ce qui POURRAIT contenir des données personnelles
- **Telegram Bot** : User ID, username, messages → données personnelles directes
- **n8n execution logs** : peuvent contenir tokens OAuth, payloads complets
- **Site WordPress schoolswp.com** (non audité ici) : commentaires, formulaires, emails

### Données personnelles confirmées
| Source | Type | Base légale | Risque |
|--------|------|------------|--------|
| Telegram Bot | User ID, messages | Consentement (CCPA handler) | MOYEN |
| n8n logs | Tokens OAuth (transitoires) | Intérêt légitime (audit) | MOYEN |

---

## Transferts hors UE

| Service | Pays | Mécanisme | Statut |
|---------|------|-----------|--------|
| Anthropic | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| OpenAI | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| Google APIs | 🇺🇸 USA | Google Cloud SCCs | ✅ |
| Notion | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| Airtable | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| Firecrawl | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| RapidAPI | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| Discord | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| Slack | 🇺🇸 USA | SCCs à vérifier | ⚠️ |
| Telegram | 🇷🇺 Russie | ❌ Aucun | ❌ NON CONFORME |
| HeyGen | 🇸🇬 Singapour | SCCs à vérifier | ⚠️ |
| ElevenLabs | 🇬🇧 UK | UK Adequacy Decision | ✅ |
| n8n hosted | 🇪🇺 EU (wp1.host) | Pas de transfert | ✅ |
| DataForSEO | À clarifier | À vérifier | ⚠️ |

**Action** : Contacter chaque service ⚠️ et demander le DPA + confirmation SCCs.

---

## DPA sous-traitants (Art. 28)

Liens DPA à vérifier/signer :
- Anthropic : https://www.anthropic.com/legal/data-processing-addendum
- OpenAI : https://openai.com/policies/data-processing-addendum
- Notion : https://www.notion.so/Data-Processing-Addendum-7b0d73c0f9fa4139b1a6e5c2e2b32684
- Airtable : https://airtable.com/legal/data-processing-addendum
- Firecrawl : Contacter support
- Discord : https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service
- Slack : https://slack.com/intl/fr-fr/terms-of-service/data-processing
- HeyGen : Contacter support
- Google : ✅ Inclus dans Google Cloud Terms of Service

---

## Plan d'actions

### Priorité HAUTE (≤ 30 jours)

- [ ] **Activer log rotation n8n** : `Settings → General → Execution data retention` → 30 jours max
- [ ] **Auditer les logs n8n actuels** : vérifier qu'aucun token OAuth n'est exposé en clair
- [ ] **Créer le registre des traitements** (`registre-traitements.md`) — ✅ fait
- [ ] **Signer DPA Anthropic** (principal sous-traitant)
- [ ] **Évaluer Telegram Bot** : arrêter transmission de données personnelles ou migrer vers alternative EU

### Priorité MOYENNE (≤ 60 jours)

- [ ] **Signer DPA** : OpenAI, Notion, Airtable, Slack, Discord
- [ ] **Vérifier SCCs** pour tous les services USA
- [ ] **Formaliser procédure droit d'accès/oubli** (formulaire email simple suffit)
- [ ] **Notice privacy WordPress** : ajouter page `/politique-confidentialite` sur schoolswp.com
- [ ] **Configurer rétention** Google Sheets/Notion (archivage articles > 24 mois)

### Priorité BASSE (≤ 90 jours)

- [ ] **AEPD impact assessment** pour transferts USA (post-Schrems II 2024)
- [ ] **Audit WordPress** : cookies, analytics, formulaires, commentaires
- [ ] **Alertes quota** Anthropic (seuil 80%) → détection utilisation anormale
- [ ] **Rate limiting webhooks** n8n (Nginx ou Cloudflare devant l'instance)

---

## Procédure notification incident CNIL (Art. 33)

En cas de violation de données personnelles :

1. **Détecter** : monitoring n8n, alertes Discord/Slack
2. **Évaluer** dans les 24h : type de données, nombre de personnes concernées, impact
3. **Notifier CNIL** dans les **72h** si risque pour les personnes : https://notifications.cnil.fr/
4. **Documenter** dans `systems/security/incidents/YYYY-MM-DD-nom.md`
5. **Informer les personnes** si risque élevé (Art. 34)

**Contact CNIL** : https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles

---

## Droits des personnes (Art. 15-22)

**Procédure actuelle** : aucune formalisée.

**Procédure minimale à implémenter** :
- Toute demande d'exercice de droits → email à contact@michaelkihl.fr
- Réponse sous 30 jours (Art. 12.3)
- Pour droit à l'oubli : supprimer dans Google Sheets, Notion, Airtable, logs n8n + informer les sous-traitants

---

## Références

- Règlement (UE) 2016/679 — RGPD
- `systems/security/registre-traitements.md` — Registre Art. 30
- `systems/security/threat-model.md` — Analyse STRIDE
- `systems/security/rotation-policy.md` — Rotation clés API
- CNIL — https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on
