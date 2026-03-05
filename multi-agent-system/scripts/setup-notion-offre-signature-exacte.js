#!/usr/bin/env node
"use strict";

/**
 * setup-notion-offre-signature-exacte.js
 * Crée la page Notion : 💎 Offre Signature Exacte — B2B WordPress System™ · schoolsWP Agency
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-offre-signature-exacte.js
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ─── DATA ────────────────────────────────────────────────────────────────────

const PROMESSE = {
  centrale: "Structurer un écosystème WordPress rentable, automatisé et scalable pour formateurs B2B.",
  pas: "Un site WordPress.",
  oui: "Une architecture business complète.",
  tagline: "Tu es architecte. Pas technicien.",
  signature: "B2B WordPress System™ · schoolsWP Agency",
};

const PHASES_OFFRE = [
  {
    num: "1",
    emoji: "🔹",
    titre: "Audit Stratégique B2B",
    sous_titre: "Fondation — Clarté avant action.",
    duree: "1 à 2 semaines",
    prix_mini: 1200,
    prix_maxi: 2000,
    objectif: "Comprendre la réalité exacte du client avant d'implémenter quoi que ce soit. Révéler ce que ni le client ni son équipe ne voient.",
    livrables: [
      {
        nom: "Audit écosystème actuel",
        detail: "Cartographie complète : LMS, CRM, tunnel, automatisations existantes, stack WordPress.",
        format: "Analyse structurée avec scoring",
      },
      {
        nom: "Analyse modèle économique B2B",
        detail: "Cycle de vente, panier moyen, taux de renouvellement actuel, friction business principale.",
        format: "Tableau diagnostique",
      },
      {
        nom: "Analyse tunnel & cycle de vente",
        detail: "De la prospection à la facturation. Points de fuite. Étapes manuelles automatisables.",
        format: "Cartographie visuelle + commentaires",
      },
      {
        nom: "Diagnostic LMS",
        detail: "Scalabilité multi-entreprises, gestion comptes, expérience apprenant, QUALIOPI compliance.",
        format: "Score 0–10 sur 8 critères",
      },
      {
        nom: "Diagnostic CRM",
        detail: "Segmentation, pipeline, automatisations actives, taux d'utilisation réel.",
        format: "Score 0–10 sur 6 critères",
      },
      {
        nom: "Rapport PDF stratégique 20–30 pages",
        detail: "Document structuré. Diagnostic global. Points de friction priorisés. Recommandations hiérarchisées.",
        format: "PDF professionnel SASU + branding schoolsWP",
      },
      {
        nom: "Roadmap priorisée 90 jours",
        detail: "Actions classées par impact/effort. Ce qui doit être fait en J1–J30, J31–J60, J61–J90.",
        format: "Tableau avec colonnes Priorité / Action / Impact / Responsable",
      },
    ],
    valeur_cle: "À l'issue de la Phase 1, le client sait exactement ce qui freine son CA. Il a un plan. Il comprend pourquoi il n'avait pas avancé seul.",
    role_commercial: "La Phase 1 est le filtre. Elle identifie les clients sérieux. Elle révèle le périmètre réel de la Phase 2. Elle vend naturellement la suite.",
  },
  {
    num: "2",
    emoji: "🔹",
    titre: "Architecture & Implémentation",
    sous_titre: "Le cœur. La transformation réelle.",
    duree: "4 à 8 semaines",
    prix_mini: 4500,
    prix_maxi: 13000,
    objectif: "Implémenter l'architecture définie en Phase 1. Chaque bloc est indépendant mais connecté aux autres. Livraison progressive avec jalons validés.",
    blocs: [
      {
        num: "1",
        emoji: "🎓",
        titre: "LMS B2B",
        objectif_bloc: "Un LMS scalable, professionnel, crédible auprès des RH et DRH.",
        actions: [
          "Structuration multi-entreprises (comptes séparés, espaces distincts)",
          "Gestion comptes groupes (cohortes, accès par lot, quotas)",
          "Organisation modules & parcours (catalogue structuré, prérequis, certificats)",
          "Sécurisation des accès (tokens, expiration, gestion départs salariés)",
          "Expérience apprenant corporate (interface sobre, UX professionnelle, mobile-ready)",
          "Tests de charge et validation scalabilité (simulation 50+ apprenants simultanés)",
        ],
        kpi_livraison: "Le client peut onboarder 1 nouvelle entreprise cliente en moins de 2 heures.",
      },
      {
        num: "2",
        emoji: "🧠",
        titre: "CRM & Automatisation",
        objectif_bloc: "Un CRM qui transforme le cycle long en flux prévisible sans intervention manuelle.",
        actions: [
          "Segmentation tripartite (entreprise / décideur / apprenant — 3 pipelines distincts)",
          "Automatisation onboarding complet (accès LMS → email welcome → kick-off → activation)",
          "Relances devis automatisées (J+3, J+7, J+14 avec contenu différencié)",
          "Pipeline commercial structuré (6 étapes, scoring prospect, assignation automatique)",
          "Séquences email B2B (bienvenue, activation, engagement, renouvellement J-90/60/30)",
          "Tableau de bord CRM pour le formateur (vue pipeline + CA prévisionnel)",
        ],
        kpi_livraison: "0 relance manuelle. Le CRM gère le cycle commercial de A à Z.",
      },
      {
        num: "3",
        emoji: "💼",
        titre: "Tunnel B2B",
        objectif_bloc: "Un tunnel qui filtre les bons prospects et automatise la qualification avant tout appel.",
        actions: [
          "Page offre corporate (crédibilité, preuves, process, pricing ou 'sur devis')",
          "Formulaire de qualification intelligent (budget estimé, taille équipe, urgence, contexte)",
          "Tracking conversions complet (GTM, événements clés, attribution source)",
          "Automatisation devis (accusé-réception, scoring, routage vers agenda ou CRM)",
          "Page de restitution audit (résumé des livrables, next steps, signature électronique)",
          "Intégration calendrier (Calendly ou natif WP) pour appels de découverte qualifiés",
        ],
        kpi_livraison: "80% des leads entrants ont déjà rempli le formulaire de qualification avant tout contact.",
      },
      {
        num: "4",
        emoji: "⚙️",
        titre: "Optimisation Technique",
        objectif_bloc: "Une fondation technique qui tient dans le temps. Pas de dette technique cachée.",
        actions: [
          "Performance Core Web Vitals (LCP < 2.5s, CLS < 0.1, INP < 200ms)",
          "Sécurité WordPress (permissions, fichiers sensibles, monitoring brute force)",
          "Tracking KPI business (GA4 configuré, événements LMS + CRM + tunnel remontés)",
          "Structure SEO stratégique (schema Article, FAQPage, BreadcrumbList, balises canoniques)",
          "Backups automatisés (quotidien site + base, rétention 30 jours, test restauration)",
          "Documentation technique (stack, versions, procédures d'urgence)",
        ],
        kpi_livraison: "Score Lighthouse > 85. Backup testé. Tracking GA4 validé dans Search Console.",
      },
    ],
    note_modularite: "Chaque bloc peut être inclus ou exclu selon les résultats de la Phase 1. Le devis Phase 2 est construit sur mesure après la restitution de l'Audit.",
  },
  {
    num: "3",
    emoji: "🔹",
    titre: "Transmission & Scalabilité",
    sous_titre: "Indépendance client. Pas de dépendance.",
    duree: "1 à 2 semaines",
    prix_inclus: true,
    note_prix: "Incluse dans toutes les offres Niveau 2 et 3",
    objectif: "Le client repart autonome. Son équipe sait utiliser le système. Il sait quoi optimiser ensuite.",
    livrables: [
      {
        nom: "Documentation système complète",
        detail: "Pas un template générique. Un document écrit pour CE client, CE système, CETTE équipe.",
        format: "Notion ou PDF structuré · 15–40 pages",
      },
      {
        nom: "Formation équipe",
        detail: "1 à 3 sessions selon taille équipe. Enregistrées si besoin. Focus opérationnel.",
        format: "Visio + replay Loom",
      },
      {
        nom: "Vidéos Loom explicatives",
        detail: "5 à 10 vidéos courtes (3–5 min) sur les process clés : onboarder un client, relancer un devis, exporter un rapport QUALIOPI.",
        format: "Loom · Livrées dans un espace dédié",
      },
      {
        nom: "Plan d'optimisation continue",
        detail: "Ce qui doit être optimisé à 30, 60, 90 jours après livraison. Priorisé et actionnable.",
        format: "Tableau Notion avec colonnes Quand / Quoi / Pourquoi / Impact estimé",
      },
      {
        nom: "Recommandations croissance",
        detail: "Prochaines étapes naturelles : nouvelles automatisations, clusters SEO, produit digital, MRR.",
        format: "Section dédiée dans le rapport de clôture",
      },
    ],
    valeur_cle: "Un client autonome revient pour évoluer. Un client dépendant revient pour réparer. La Phase 3 construit la relation long terme.",
  },
];

const FORMAT = {
  duree_totale: "6 à 10 semaines selon périmètre",
  modalites: [
    { etape: "Semaine 1–2", action: "Audit initial (Phase 1)", livrable: "Rapport PDF + Roadmap 90 jours" },
    { etape: "Semaine 2–3", action: "Restitution + validation architecture Phase 2", livrable: "Devis Phase 2 sur mesure" },
    { etape: "Semaine 3–8", action: "Implémentation structurée (blocs 1 à 4)", livrable: "Jalons validés par bloc livré" },
    { etape: "Semaine 8–10", action: "Transmission + formation équipe (Phase 3)", livrable: "Documentation + vidéos Loom + plan optimisation" },
    { etape: "J+30", action: "Point de suivi post-livraison (30 min)", livrable: "Ajustements mineurs + proposition accompagnement" },
  ],
  points_hebdo: "Chaque jeudi : point 30 min (avancement + blocages + décisions en attente)",
  livraison_finale: "Rapport de clôture + remise des accès + signature passation",
};

const CLIENT_IDEAL = {
  profil: "Formateur B2B avec une offre formation établie, déjà en contact avec des entreprises, qui veut structurer et scaler son système.",
  criteres: [
    { critere: "Offre formation ≥ 1 500 € / mission entreprise", type: "ÉLIMINATOIRE", raison: "Sous ce seuil, le ROI de l'architecture ne justifie pas l'investissement." },
    { critere: "Minimum 5–10 entreprises clientes existantes ou en cours", type: "ÉLIMINATOIRE", raison: "Sans base client B2B, pas de problème d'architecture à résoudre." },
    { critere: "Budget structuration ≥ 4 000 €", type: "ÉLIMINATOIRE", raison: "Ne pas démarrer une mission si le budget ne couvre pas la Phase 1 + Phase 2 a minima." },
    { critere: "Ambition de croissance explicite", type: "FORT", raison: "Un client qui 'veut juste que ça marche' n'achète pas une architecture premium." },
    { critere: "Quelqu'un dans l'équipe pour utiliser le système livré", type: "FORT", raison: "Un formateur seul sans équipe ne peut pas exploiter 80% du système." },
    { critere: "Secteur B2B clair (OF, consultant, académicien, cabinet)", type: "INDICATIF", raison: "Si B2C dominant, recadrer vers une architecture différente." },
  ],
};

const ANTI_CIBLES = [
  { profil: "Site vitrine simple", raison: "Pas de problème d'architecture. Pas de ROI justifiable.", rediriger: "Recommander un prestataire Elementor." },
  { profil: "Elementor 'design only'", raison: "Ce n'est pas ton métier. Perte de temps et de positionnement.", rediriger: "Dire clairement : 'Ce n'est pas ce que je fais.'"},
  { profil: "Support technique à la carte", raison: "Pas de vision long terme. Pas de transformation. Hourly = pas premium.", rediriger: "Proposer uniquement si client existant + accompagnement mensuel en place." },
  { profil: "Petit budget bricolage (< 1 500 €)", raison: "Incompatible avec le positionnement. Dévalue l'offre.", rediriger: "Orienter vers les ressources gratuites schoolsWP ou le produit digital." },
  { profil: "Formateur B2C uniquement", raison: "Problématiques différentes. Audience différente. Pas dans la niche.", rediriger: "Potentiellement orienté vers d'autres agents schoolsWP." },
  { profil: "Demande urgente sans audit préalable", raison: "Sans diagnostic, risque de livrer quelque chose d'inadapté.", rediriger: "Proposer toujours la Phase 1 (Audit) comme point d'entrée." },
];

const TARIFICATION = {
  principe: "Tu factures la valeur business créée — pas le temps passé.",
  anti_patterns: [
    "Jamais de tarif journalier (compare à des freelances, non à un architecte)",
    "Jamais de prix à la page ou au plugin installé",
    "Jamais de remise sur le prix — ajuster le périmètre si budget insuffisant",
    "Jamais commencer sans acompte 40% (acompte = engagement du client)",
  ],
  grille: [
    {
      niveau: "Phase 1 seule — Audit Stratégique",
      prix: "1 200 – 2 000 €",
      prix_mini: 1200,
      prix_maxi: 2000,
      usage: "Entrée premium. Filtre. Souvent upsell naturel vers Phase 2.",
      delai_paiement: "100% à la signature",
    },
    {
      niveau: "Phase 1 + Phase 2 (Blocs 1–2) — Essentiel",
      prix: "5 500 – 8 000 €",
      prix_mini: 5500,
      prix_maxi: 8000,
      usage: "Formateur B2B naissant (3–8 clients entreprise). Structurer LMS + CRM.",
      delai_paiement: "40% signature · 40% mi-mission · 20% livraison",
    },
    {
      niveau: "Phase 1 + Phase 2 complète (4 blocs) — Avancé",
      prix: "8 000 – 13 000 €",
      prix_mini: 8000,
      prix_maxi: 13000,
      usage: "Formateur B2B structuré (10+ clients). LMS + CRM + Tunnel + Technique.",
      delai_paiement: "40% signature · 40% mi-mission · 20% livraison",
    },
    {
      niveau: "Phase 1 + Phase 2 + Phase 3 — Full System™",
      prix: "10 000 – 18 000 €",
      prix_mini: 10000,
      prix_maxi: 18000,
      usage: "Formateur ambitieux. CA > 100k€. Veut système complet + équipe formée.",
      delai_paiement: "40% signature · 30% mi-mission · 30% livraison",
    },
    {
      niveau: "Accompagnement mensuel post-livraison",
      prix: "800 – 2 000 € / mois",
      prix_mini: 800,
      prix_maxi: 2000,
      usage: "Optimisation continue. Ajustements. Suivi KPI. 3–5 clients max simultanément.",
      delai_paiement: "Mensuel, début de mois",
    },
  ],
};

const DIFFERENCIATEURS = [
  {
    competence: "SEO stratégique B2B",
    pourquoi_rare: "La plupart des experts SEO ne comprennent pas le cycle long B2B. La plupart des freelances WordPress ne font pas de SEO.",
    preuve: "schoolsWP.com — cluster LMS B2B + cluster CRM + AI Overviews monitoring",
  },
  {
    competence: "CRM WordPress natif",
    pourquoi_rare: "80% des formateurs utilisent HubSpot ou Pipedrive. Personne ne propose de CRM WordPress souverain connecté au LMS.",
    preuve: "FluentCRM · pipeline B2B · séquences renouvellement · segmentation tripartite",
  },
  {
    competence: "LMS WordPress multi-entreprises",
    pourquoi_rare: "Les tutoriels LMS s'adressent aux formateurs B2C. Personne ne documente la configuration B2B multi-clients en français.",
    preuve: "Articles pilier sur tutorLMS corporate · études de cas · architecture multi-cohortes",
  },
  {
    competence: "Automatisation WordPress native",
    pourquoi_rare: "Les agences automatisent avec Zapier ou Make (coût récurrent). Tu automatises nativement dans WordPress (coût unique).",
    preuve: "FluentCRM automations · hooks WP natifs · séquences trigger-based sans SaaS externe",
  },
  {
    competence: "Vision business formateurs B2B",
    pourquoi_rare: "Les développeurs WordPress pensent technique. Toi, tu penses cycle long, renouvellement, LTV, QUALIOPI, scalabilité.",
    preuve: "Audit incluant analyse modèle économique · Roadmap CA · KPIs renouvellement",
  },
];

const SCRIPTS_VENTE = [
  {
    moment: "Premier appel découverte (20 min)",
    objectif_appel: "Comprendre la situation. Qualifier le budget. Proposer la Phase 1.",
    script: [
      "Qu'est-ce qui vous a amené à chercher quelqu'un pour votre architecture WordPress ?",
      "[Écouter sans interrompre. Reformuler en termes business.]",
      "Si je comprends bien, le vrai problème est [reformulation]. C'est ça ?",
      "Combien d'entreprises clientes avez-vous en ce moment ? Et quel est votre panier moyen ?",
      "Avant d'aller plus loin — avez-vous un budget en tête pour cette structuration ?",
      "[Si budget < 4 000 € → orienter vers ressources schoolsWP. Si ≥ 4 000 € → continuer.]",
      "Ce que je propose dans ce cas, c'est de commencer par un Audit Stratégique. 2 semaines, un rapport complet, une roadmap précise. C'est 1 500 €. À partir de là, on voit ensemble ce qui fait le plus sens pour la suite.",
    ],
  },
  {
    moment: "Restitution Audit → Vente Phase 2",
    objectif_appel: "Présenter les résultats. Créer l'urgence sur les points critiques. Proposer la Phase 2 calibrée.",
    script: [
      "Voici les 3 points critiques que j'ai identifiés. [Présenter avec chiffres et impact CA.]",
      "Le plus urgent à traiter est [problème 1]. Voici pourquoi ça freine directement votre renouvellement.",
      "Sur la base de cet audit, j'ai préparé une proposition pour la Phase 2. Elle couvre [blocs X, Y, Z].",
      "Le périmètre que je recommande est [version X] pour [raison basée sur le diagnostic].",
      "Le budget est de [fourchette]. On démarre dans les 5 jours ouvrés après signature.",
      "Des questions sur ce que je propose ?",
    ],
  },
  {
    moment: "Gestion de l'hésitation prix",
    objectif_appel: "Recadrer sur la valeur, pas le coût.",
    script: [
      "[Ne pas défendre le prix. Revenir sur les enjeux.]",
      "Je comprends. Permettez-moi de vous poser une question : combien vous coûte actuellement le fait de ne pas avoir ce système ?",
      "[Laisser le silence. Laisser le client calculer.]",
      "Si on améliore votre taux de renouvellement de 15%, sur votre base actuelle de [X clients], ça représente [calcul rapide] €/an.",
      "Ce n'est pas une dépense. C'est un investissement avec un retour mesurable.",
      "Si le budget est un frein, on peut commencer par les blocs 1–2 uniquement. Ça couvre l'essentiel.",
    ],
  },
];

const PROCESSUS_COMPLET = [
  { etape: "1", action: "Formulaire de qualification soumis", kpi: "Budget déclaré · Contexte B2B confirmé", duree: "Asynchrone" },
  { etape: "2", action: "Appel découverte 20 min", kpi: "Qualification finale : GO / NO-GO", duree: "J+2 à J+5" },
  { etape: "3", action: "Devis Phase 1 (Audit) envoyé", kpi: "Délai signature < 48h", duree: "Dans les 24h post-appel" },
  { etape: "4", action: "Acompte 100% reçu", kpi: "Démarrage audit confirmé", duree: "J+2 à J+5 après devis" },
  { etape: "5", action: "Audit Phase 1 (2 semaines)", kpi: "Rapport PDF + Roadmap livrés", duree: "2 semaines" },
  { etape: "6", action: "Restitution audit (1h)", kpi: "Proposition Phase 2 présentée", duree: "1h · J+14" },
  { etape: "7", action: "Devis Phase 2 envoyé sur mesure", kpi: "Délai signature < 5 jours", duree: "Dans les 24h post-restitution" },
  { etape: "8", action: "Acompte 40% Phase 2 reçu", kpi: "Démarrage implémentation J+5", duree: "Décision < 5 jours" },
  { etape: "9", action: "Implémentation Phase 2 (4–8 semaines)", kpi: "Jalons validés par bloc · Point hebdo jeudi", duree: "4 à 8 semaines" },
  { etape: "10", action: "Transmission Phase 3 (1–2 semaines)", kpi: "Documentation livrée · Équipe formée", duree: "1 à 2 semaines" },
  { etape: "11", action: "Livraison finale + rapport clôture", kpi: "Solde 20–30% payé · Témoignage demandé", duree: "Fin de mission" },
  { etape: "12", action: "Point J+30 + proposition accompagnement", kpi: "Taux conversion → accompagnement mensuel", duree: "J+30 post-livraison" },
];

const TEMPLATES_EMAIL = [
  {
    moment: "Après formulaire de qualification",
    sujet: "Votre demande d'audit — prochaine étape",
    corps: `Bonjour [Prénom],

J'ai bien reçu votre demande. Votre contexte est clair : [résumé en 1 phrase du formulaire].

Avant de démarrer quoi que ce soit, je prends un temps de découverte de 20 minutes pour m'assurer qu'on est bien alignés.

Voici mon agenda : [lien Calendly]

Si aucun créneau ne convient, répondez à cet email avec vos disponibilités.

À très vite,
[Prénom] · schoolsWP Agency`,
  },
  {
    moment: "Envoi devis Phase 1",
    sujet: "Audit Architecture B2B — Proposition",
    corps: `Bonjour [Prénom],

Suite à notre échange de ce [jour], voici la proposition pour l'Audit Stratégique B2B.

Ce que vous recevrez dans 2 semaines :
→ Rapport PDF 20–30 pages (diagnostic complet de votre écosystème)
→ Roadmap priorisée 90 jours (ce qui doit être fait, dans quel ordre, pour quel impact)

Investissement : [prix] €
Démarrage : dans les 5 jours ouvrés après signature et réception du règlement.

Le devis est joint à cet email.

Pour toute question : répondez à cet email ou appelez-moi directement.

[Prénom] · schoolsWP Agency`,
  },
  {
    moment: "Demande de témoignage post-livraison",
    sujet: "Un retour rapide de votre côté ?",
    corps: `Bonjour [Prénom],

Maintenant que le système est en place et que vous l'utilisez depuis quelques semaines, j'aurais une requête simple.

Si vous deviez expliquer à un autre formateur B2B ce que cette mission a changé concrètement pour vous, que lui diriez-vous ?

Pas besoin d'être exhaustif. 2 à 4 phrases sincères, c'est largement suffisant.

Si vous préférez le faire en vidéo (Loom, 1–2 min), je peux vous envoyer un lien.

Merci d'avance — votre retour m'aide directement à affiner l'offre.

[Prénom] · schoolsWP Agency`,
  },
];

// ─── CALC ─────────────────────────────────────────────────────────────────────

const prix_moyen = (niveau) => Math.round((niveau.prix_mini + niveau.prix_maxi) / 2);

const scenario_an1 = {
  // 3 Audits + 2 Essentiels + 2 Avancés + 3 MRR
  mini: 3 * 1200 + 2 * 5500 + 2 * 8000 + 3 * 800 * 12,
  cible: 3 * 2000 + 2 * 8000 + 2 * 13000 + 3 * 2000 * 12,
};

// ─── NOTION HELPERS ───────────────────────────────────────────────────────────

async function notionRequest(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Notion-Version": NOTION_VERSION,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const json = await resp.json();
  if (!resp.ok) throw new Error(`Notion ${resp.status}: ${JSON.stringify(json)}`);
  return json;
}

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

// ─── BLOCK BUILDERS ──────────────────────────────────────────────────────────

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: String(text) },
  annotations: { bold: opts.bold || false, italic: opts.italic || false, code: opts.code || false, color: opts.color || "default" },
});
const h1 = (t) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (rts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const bul = (rts, color = "default") => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)], color } });
const num = (rts) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const qot = (text, color = "gray_background") => ({ object: "block", type: "quote", quote: { rich_text: Array.isArray(text) ? text : [rt(text)], color } });
const cal = (text, color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: Array.isArray(text) ? text : [rt(text)], icon: { type: "emoji", emoji: "💡" }, color },
});
const tog = (text, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(text, { bold: true })], children },
});
const todo = (text, checked = false) => ({
  object: "block", type: "to_do",
  to_do: { rich_text: [rt(text)], checked },
});

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("💎 Offre Signature Exacte · B2B WordPress System™ · schoolsWP Agency · Confidentiel", "yellow_background"));
  blocks.push(p([rt("Ce document définit l'offre. Ce que tu vends. Ce que tu ne vends pas. Comment tu le vends.", { italic: true, bold: true })]));
  blocks.push(div());

  // ── PROMESSE CENTRALE ──
  blocks.push(h1("🎯 Promesse Centrale"));
  blocks.push(p(""));
  blocks.push(cal([rt(PROMESSE.centrale, { bold: true })], "green_background"));
  blocks.push(p(""));
  blocks.push(p([rt("Tu vends : ", { bold: true }), rt(PROMESSE.pas, { color: "red" }), rt("  ✗", { bold: true, color: "red" })]));
  blocks.push(p([rt("Tu vends : ", { bold: true }), rt(PROMESSE.oui, { bold: true, color: "green" }), rt("  ✓", { bold: true, color: "green" })]));
  blocks.push(p(""));
  blocks.push(qot(PROMESSE.tagline, "blue_background"));
  blocks.push(div());

  // ── PHASES DE L'OFFRE ──
  blocks.push(h1("🧱 Structure de l'Offre — 3 Phases"));
  blocks.push(p([rt("Phase 1 = toujours le point d'entrée. Phase 2 = la transformation. Phase 3 = incluse dans toutes les offres Niveau 2+.", { italic: true })]));
  blocks.push(p(""));

  for (const phase of PHASES_OFFRE) {
    const headerPhase = `${phase.emoji} Phase ${phase.num} — ${phase.titre}  (${phase.duree})`;
    const phaseChildren = [];

    phaseChildren.push(cal([rt(phase.sous_titre, { bold: true })], "gray_background"));
    phaseChildren.push(p(""));
    phaseChildren.push(p([rt("Objectif : ", { bold: true }), rt(phase.objectif, { italic: true })]));

    if (phase.prix_mini) {
      phaseChildren.push(p([rt("Prix : ", { bold: true }), rt(`${phase.prix_mini.toLocaleString("fr-FR")} – ${phase.prix_maxi.toLocaleString("fr-FR")} €`, { bold: true, color: "green" })]));
    }
    if (phase.note_prix) {
      phaseChildren.push(p([rt("📌 ", {}), rt(phase.note_prix, { italic: true, color: "gray" })]));
    }

    phaseChildren.push(p(""));

    // Livrables Phase 1 et 3
    if (phase.livrables) {
      phaseChildren.push(h3("Livrables"));
      for (const livr of phase.livrables) {
        const livrChildren = [
          p([rt("Contenu : ", { bold: true }), rt(livr.detail)]),
          p([rt("Format : ", { bold: true }), rt(livr.format, { code: true })]),
        ];
        phaseChildren.push(tog(`📄 ${livr.nom}`, livrChildren));
        phaseChildren.push(p(""));
      }
    }

    // Blocs Phase 2
    if (phase.blocs) {
      phaseChildren.push(h3("4 Blocs d'Implémentation"));
      for (const bloc of phase.blocs) {
        const blocChildren = [];
        blocChildren.push(p([rt("Objectif du bloc : ", { bold: true }), rt(bloc.objectif_bloc, { italic: true })]));
        blocChildren.push(p(""));
        bloc.actions.forEach((a) => blocChildren.push(bul(a)));
        blocChildren.push(p(""));
        blocChildren.push(cal([rt("KPI livraison : ", { bold: true }), rt(bloc.kpi_livraison)], "green_background"));
        phaseChildren.push(tog(`${bloc.emoji} Bloc ${bloc.num} — ${bloc.titre}`, blocChildren));
        phaseChildren.push(p(""));
      }
      phaseChildren.push(p([rt("→ Note : ", { bold: true, color: "gray" }), rt(phase.note_modularite, { italic: true })]));
    }

    // Valeur clé + rôle commercial
    if (phase.valeur_cle) {
      phaseChildren.push(p(""));
      phaseChildren.push(qot(phase.valeur_cle, "blue_background"));
    }
    if (phase.role_commercial) {
      phaseChildren.push(p(""));
      phaseChildren.push(p([rt("Rôle commercial : ", { bold: true, color: "gray" }), rt(phase.role_commercial, { italic: true })]));
    }

    blocks.push(tog(headerPhase, phaseChildren));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── FORMAT ──
  blocks.push(h1("📦 Format & Modalités"));
  blocks.push(p([rt(`Durée totale : `, { bold: true }), rt(FORMAT.duree_totale, { bold: true, color: "green" })]));
  blocks.push(p(""));

  for (const m of FORMAT.modalites) {
    blocks.push(bul([
      rt(`${m.etape} : `, { bold: true }),
      rt(`${m.action} `, {}),
      rt(`→ ${m.livrable}`, { italic: true, color: "gray" }),
    ]));
  }

  blocks.push(p(""));
  blocks.push(p([rt("Points hebdo : ", { bold: true }), rt(FORMAT.points_hebdo)]));
  blocks.push(p([rt("Livraison finale : ", { bold: true }), rt(FORMAT.livraison_finale)]));
  blocks.push(div());

  // ── CLIENT IDÉAL ──
  blocks.push(h1("🎯 Client Idéal — Matrice de Qualification"));
  blocks.push(p([rt("Profil : ", { bold: true }), rt(CLIENT_IDEAL.profil, { italic: true })]));
  blocks.push(p(""));

  for (const c of CLIENT_IDEAL.criteres) {
    const isEliminatoire = c.type === "ÉLIMINATOIRE";
    const children = [
      p([rt("Raison : ", { bold: true }), rt(c.raison, { italic: true })]),
    ];
    blocks.push(tog(
      `${isEliminatoire ? "🔴 ÉLIMINATOIRE" : c.type === "FORT" ? "🟠 FORT" : "🟡 INDICATIF"} — ${c.critere}`,
      children
    ));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── ANTI-CIBLES ──
  blocks.push(h1("❌ Ce que tu ne Fais PAS"));
  blocks.push(cal("Refuser ces demandes protège ton positionnement. Chaque 'oui' à un mauvais client = 1 mission premium refusée.", "red_background"));
  blocks.push(p(""));

  for (const ac of ANTI_CIBLES) {
    const children = [
      p([rt("Raison du refus : ", { bold: true }), rt(ac.raison)]),
      p([rt("Comment rediriger : ", { bold: true }), rt(ac.rediriger, { italic: true })]),
    ];
    blocks.push(tog(`✗  ${ac.profil}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── TARIFICATION ──
  blocks.push(h1("💰 Tarification — Grille Complète"));
  blocks.push(cal([rt(TARIFICATION.principe, { bold: true })], "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Anti-patterns à éviter"));
  TARIFICATION.anti_patterns.forEach((ap) => blocks.push(bul([rt("⛔  " + ap, { bold: true })], "red_background")));
  blocks.push(p(""));

  blocks.push(h2("Grille de Prix"));
  for (const t of TARIFICATION.grille) {
    const children = [];
    children.push(p([rt("Prix : ", { bold: true }), rt(t.prix, { bold: true, color: "green" })]));
    children.push(p([rt("Profil / usage : ", { bold: true }), rt(t.usage)]));
    children.push(p([rt("Paiement : ", { bold: true }), rt(t.delai_paiement)]));

    blocks.push(tog(`${t.niveau}  ·  ${t.prix}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(h2("Projection CA An 1 (hypothèse modérée)"));
  blocks.push(p([rt("3 Audits + 2 Essentiels + 2 Avancés + 3 MRR (12 mois)", { italic: true })]));
  blocks.push(p(""));
  blocks.push(bul([rt("Conservateur : ", { bold: true }), rt(`${scenario_an1.mini.toLocaleString("fr-FR")} €/an`, { bold: true, color: "blue" })]));
  blocks.push(bul([rt("Cible : ", { bold: true }), rt(`${scenario_an1.cible.toLocaleString("fr-FR")} €/an`, { bold: true, color: "green" })]));
  blocks.push(div());

  // ── DIFFÉRENCIATEURS ──
  blocks.push(h1("🧠 Différenciation — Les 5 Compétences Combinées"));
  blocks.push(p([rt("Très peu savent faire les 5 ensemble. C'est ton avantage structurel.", { italic: true })]));
  blocks.push(p(""));

  for (const diff of DIFFERENCIATEURS) {
    const children = [];
    children.push(p([rt("Pourquoi c'est rare : ", { bold: true }), rt(diff.pourquoi_rare)]));
    children.push(p([rt("Preuve concrète : ", { bold: true }), rt(diff.preuve, { italic: true, color: "green" })]));
    blocks.push(tog(`✓ ${diff.competence}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SCRIPTS DE VENTE ──
  blocks.push(h1("🎤 Scripts de Vente — Mot pour Mot"));
  blocks.push(p([rt("Ces scripts ne s'improvisent pas. Les lire à voix haute avant chaque appel.", { italic: true, bold: true })]));
  blocks.push(p(""));

  for (const script of SCRIPTS_VENTE) {
    const children = [];
    children.push(p([rt("Objectif de l'appel : ", { bold: true }), rt(script.objectif_appel, { italic: true })]));
    children.push(p(""));
    script.script.forEach((ligne) => {
      if (ligne.startsWith("[")) {
        children.push(p([rt(ligne, { italic: true, color: "gray" })]));
      } else {
        children.push(bul([rt('"'), rt(ligne, { italic: true }), rt('"')]));
      }
    });
    blocks.push(tog(`📞 ${script.moment}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── PROCESSUS COMPLET ──
  blocks.push(h1("🗺 Processus de Vente — De la Demande à la Mission"));
  blocks.push(p(""));

  for (const etape of PROCESSUS_COMPLET) {
    blocks.push(bul([
      rt(`${etape.etape.padStart(2, "0")} — `, { bold: true }),
      rt(`${etape.action} `, { bold: true }),
      rt(`(${etape.duree})`, { italic: true, color: "gray" }),
    ]));
    blocks.push(bul([rt(`→ KPI : ${etape.kpi}`, { italic: true })], "gray_background"));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── TEMPLATES EMAIL ──
  blocks.push(h1("📧 Templates Email — Prêts à Envoyer"));
  blocks.push(p([rt("Adapter [Prénom] et [contexte]. Ne pas sur-personnaliser — la clarté > la personnalisation.", { italic: true })]));
  blocks.push(p(""));

  for (const tpl of TEMPLATES_EMAIL) {
    const children = [];
    children.push(p([rt("Sujet : ", { bold: true }), rt(tpl.sujet, { code: true })]));
    children.push(p(""));
    tpl.corps.split("\n").forEach((ligne) => {
      if (ligne === "") {
        children.push(p(""));
      } else {
        children.push(p(ligne));
      }
    });
    blocks.push(tog(`✉️ ${tpl.moment}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── CHECKLIST AVANT DÉMARRAGE ──
  blocks.push(h1("✅ Checklist — Avant de Proposer l'Offre"));
  blocks.push(p(""));

  const checklist = [
    "Page /audit-b2b active, formulaire testé, emails de confirmation envoyés",
    "Template devis Phase 1 (PDF SASU) finalisé, relu, signé de ton côté",
    "Template devis Phase 2 (3 versions : Essentiel / Avancé / Full) prêts",
    "Process de paiement opérationnel (virement SASU ou lien Stripe)",
    "Espace client créé dans Notion ou Drive (1 dossier par mission)",
    "Template rapport audit PDF créé (squelette de 20–30 pages)",
    "Modèle de roadmap 90 jours prêt à personnaliser",
    "Loom Pro activé pour les vidéos de transmission",
    "Calendrier partageable (Calendly ou équivalent) avec créneaux réservés",
    "Pipeline CRM créé : Formulaire → Appel → Audit → Mission → MRR",
  ];

  checklist.forEach((item) => blocks.push(todo(item)));
  blocks.push(div());

  // ── RÈGLES D'OR ──
  blocks.push(h1("⚡ Règles d'Or — Ce qui ne se Négocie Pas"));
  blocks.push(p(""));

  const regles = [
    "Phase 1 (Audit) est le point d'entrée absolu — jamais démarrer directement en Phase 2",
    "Acompte 40% avant tout démarrage — pas d'exception",
    "Pas de prix sans comprendre le contexte complet du client",
    "1 seul client en Phase 2 à la fois (qualité > volume sur les premières missions)",
    "Documenter chaque mission en temps réel — matière première pour études de cas",
    "Demander le témoignage dans les 2 semaines post-livraison — jamais après",
    "Proposer l'accompagnement mensuel systématiquement à J+30 — sans attendre que le client demande",
  ];

  regles.forEach((r) => blocks.push(bul([rt("⚡  " + r, { bold: true })], "yellow_background")));
  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🌟 Ce que cette Offre Construit"));
  blocks.push(p(""));
  blocks.push(cal(
    "Chaque mission livrée est une étude de cas. Chaque étude de cas est un article SEO. Chaque article est un lead LinkedIn. Chaque lead est une mission. C'est un volant, pas une prestation isolée.",
    "purple_background"
  ));
  blocks.push(p(""));
  blocks.push(qot(
    `CA An1 estimé : ${scenario_an1.mini.toLocaleString("fr-FR")} – ${scenario_an1.cible.toLocaleString("fr-FR")} €  ·  Positionnement : L'architecte WordPress des formateurs B2B francophones`,
    "green_background"
  ));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de l'Offre Signature Exacte B2B WordPress System™...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "💎" },
    properties: {
      title: { title: [{ text: { content: "💎 Offre Signature — B2B WordPress System™ · schoolsWP Agency" } }] },
    },
    children: firstChunk,
  });

  const pageId = page.id;
  console.log(`✅  Page créée : ${pageId}`);

  let i = 0;
  while (i < rest.length) {
    const batch = rest.slice(i, i + CHUNK);
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, { children: batch });
    i += CHUNK;
    console.log(`   ↳ Batch ${Math.ceil(i / CHUNK) + 1} envoyé (${Math.min(i, rest.length)}/${rest.length} blocs)`);
  }

  console.log("");
  console.log("✅  Page complète créée avec succès !");
  console.log(`🔗  https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📋  Sections créées :");
  console.log("   · Promesse centrale + ce qui se vend / ne se vend pas");
  console.log("   · 3 phases (Audit · Architecture 4 blocs · Transmission)");
  console.log("   · 7 livrables Phase 1 détaillés");
  console.log("   · 4 blocs Phase 2 avec KPIs de livraison");
  console.log("   · Matrice client idéal (6 critères dont 3 éliminatoires)");
  console.log("   · 6 anti-cibles avec redirection");
  console.log("   · Grille tarifaire 5 niveaux");
  console.log("   · 5 différenciateurs avec preuve");
  console.log("   · 3 scripts de vente mot pour mot");
  console.log("   · Processus complet 12 étapes");
  console.log("   · 3 templates email prêts à envoyer");
  console.log("   · Checklist 10 points + 7 règles d'or");
  console.log("");
  console.log(`💰  CA An1 estimé : ${scenario_an1.mini.toLocaleString("fr-FR")} – ${scenario_an1.cible.toLocaleString("fr-FR")} €`);
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
