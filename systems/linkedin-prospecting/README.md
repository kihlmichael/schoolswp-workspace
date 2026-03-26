# Pipeline LinkedIn Prospecting from Post URL

**Version** : V4 — Kit SOP complet
**Statut** : pret a implementer
**Stack** : Apify + Unipile + Claude + Hunter.io (optionnel) + n8n

## Flow

```
URL post LinkedIn
       |
       v
Apify — scrape + detection mots-cles
       |
       v
Unipile — tous les commentateurs (100/page)
       |
       v
Unipile — enrichissement profil complet
       |
       v
Scoring ICP — qualifie / non qualifie
       |
       v
Claude — score ICP + role + secteur
       |
       v
Claude — messages personnalises (1 par qualifie)
       |
       v
Rapport HTML final + Hunter.io si confirmation
```

## Structure du kit

```
systems/linkedin-prospecting/
├── README.md                          # Ce fichier
├── sops/
│   ├── SOP-00-master-orchestrator.md  # Orchestration globale
│   ├── SOP-01-collecte-apify.md       # Scrape + normalisation
│   ├── SOP-02-analyse-intent.md       # Detection intention
│   ├── SOP-03-enrichissement.md       # Unipile enrichissement
│   ├── SOP-04-qualification-icp.md    # Qualification ICP
│   ├── SOP-05-scoring.md              # Scoring commercial /100
│   ├── SOP-06-messages.md             # Messages personnalises
│   ├── SOP-07-hunter.md               # Verification email
│   └── SOP-08-rapport.md              # Rapport final JSON + HTML
├── schemas/
│   ├── apify-normalized.json          # Schema sortie Apify
│   ├── enriched-lead.json             # Schema lead enrichi
│   ├── scoring-output.json            # Schema scoring
│   └── final-pipeline-output.json     # Schema JSON final
└── prompts/
    ├── prompt-master.md               # Prompt maitre Claude
    ├── prompt-01-apify.md             # Prompt normalisation Apify
    ├── prompt-02-intent.md            # Prompt detection intention
    ├── prompt-04-05-scoring.md        # Prompt qualification + scoring
    ├── prompt-06-messages.md          # Prompt messages
    └── prompt-08-rapport.md           # Prompt rapport HTML
```

## Variables globales

| Variable | Description | Obligatoire |
|---|---|---|
| `linkedin_post_url` | URL du post LinkedIn | oui |
| `offre` | Description de l'offre | oui |
| `icp_principal` | Description de l'ICP | oui |
| `roles_cibles` | Roles decision/influence cibles | oui |
| `secteurs_cibles` | Secteurs prioritaires | oui |
| `tailles_entreprise_cibles` | Fourchettes de taille | non |
| `zones_geographiques` | Pays/regions cibles | non |
| `langues_cibles` | Langues acceptees | non |
| `signaux_forts` | Mots-cles = intention forte | oui |
| `signaux_faibles` | Mots-cles = interet faible | non |
| `exclusions` | Roles/secteurs/mots a exclure | non |
| `ton_message` | Ton des messages outbound | oui |
| `enable_hunter` | Activer verification email | non |
| `score_contact_threshold` | Seuil "contacter" (defaut: 70) | non |
| `score_review_threshold` | Seuil "review" (defaut: 45) | non |
