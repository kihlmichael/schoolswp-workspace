#!/usr/bin/env node
"use strict";

/**
 * setup-notion-seo-domination-b2b-12mois.js
 * Crée la page Notion : 🗺 Stratégie SEO Domination B2B — 12 Mois
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-seo-domination-b2b-12mois.js
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

const POSITIONNEMENT_EDITORIAL = {
  pas: [
    { kw: '"Tutor LMS avis"', pourquoi: "Concurrence frontale WPMarmite. Volume fragmenté. Intention d'achat plugin, pas système." },
    { kw: '"Quel LMS choisir ?"', pourquoi: "Question généraliste. Résultats noyés. Audience formateurs B2B = 2% du trafic total." },
    { kw: '"Meilleur plugin formation WordPress"', pourquoi: "Information, pas transformation. Audience : amateurs, pas professionnels B2B." },
    { kw: '"Tutor LMS vs LearnDash"', pourquoi: "Comparatif commodité. Terrain occupé. Intention : couper les coûts, pas scaler." },
  ],
  oui: [
    { kw: '"Structurer un LMS WordPress pour entreprise"', intent: "informationnelle → décisionnelle", opportunite: "Zéro article expert en FR. Audience ultra qualifiée." },
    { kw: '"Architecture CRM pour formation B2B"', intent: "informationnelle experte", opportunite: "Terme 'CRM + formation B2B' = terrain 100% vierge." },
    { kw: '"Onboarding automatisé clients corporate WordPress"', intent: "décisionnelle", opportunite: "Requête longue tail. 0 concurrent direct. Intention acheteur." },
    { kw: '"LMS WordPress multi-entreprises"', intent: "informationnelle experte", opportunite: "Volume faible, valeur haute. Formateurs B2B en recherche active." },
    { kw: '"Reporting formation QUALIOPI WordPress"', intent: "informationnelle urgente", opportunite: "Conformité réglementaire = motivation forte. Terrain vierge." },
  ],
  axiome: "On parle système, pas plugin isolé. On parle architecture, pas installation.",
};

const TRIMESTRES = [
  {
    num: "1",
    emoji: "🔵",
    label: "FONDATION CLUSTER PILIER",
    periode: "Mois 1 – 3",
    objectif: "Créer 1 pilier ultra-fort + 5 satellites. Poser l'autorité de base.",
    couleur: "blue_background",
    pilier: {
      titre: "LMS WordPress pour entreprises : architecture, CRM et automatisation complète",
      slug: "lms-wordpress-entreprise-architecture",
      type: "Guide complet",
      longueur: "3 500 – 5 000 mots",
      angle: "Pas un tutoriel plugin — une vision d'architecte système B2B",
      structure: [
        "Pourquoi un LMS grand public ne suffit pas en B2B",
        "Multi-entreprises : gestion des comptes, cohortes, accès groupés",
        "Segmentation tripartite (décideur / apprenant / RH)",
        "Onboarding automatisé step-by-step",
        "CRM intégré : pipeline + renouvellement",
        "Reporting formateur : KPIs B2B réels",
        "Architecture WordPress recommandée (plugins, coût, échelle)",
        "Erreurs classiques à éviter",
        "CTA Audit Architecture B2B",
      ],
      cibles_ai: [
        "Comment structurer un LMS WordPress pour plusieurs entreprises ?",
        "Quelle architecture WordPress pour formateur B2B ?",
        "LMS WordPress multi-clients : comment faire ?",
      ],
    },
    satellites: [
      {
        titre: "Gérer plusieurs entreprises sur Tutor LMS : guide complet",
        slug: "gerer-plusieurs-entreprises-tutor-lms",
        intent: "informationnelle experte",
        mots_cibles: ["tutor lms multi-entreprises", "gérer entreprises lms wordpress"],
        priorite: "🔴 M1",
        angle: "Technique + business : comment facturer, séparer les accès, suivre par client",
      },
      {
        titre: "CRM WordPress pour cycle de vente B2B long : configuration FluentCRM",
        slug: "crm-wordpress-cycle-vente-b2b",
        intent: "informationnelle → décisionnelle",
        mots_cibles: ["crm wordpress formation b2b", "fluentcrm cycle vente long"],
        priorite: "🔴 M1",
        angle: "Pipeline prospects entreprise, scoring, relances, renouvellement",
      },
      {
        titre: "Automatiser l'onboarding formation entreprise sur WordPress",
        slug: "automatiser-onboarding-formation-entreprise-wordpress",
        intent: "informationnelle",
        mots_cibles: ["onboarding formation entreprise wordpress", "automatisation accès lms"],
        priorite: "🟠 M2",
        angle: "Séquence complète : signature → accès → bienvenue → activation → suivi",
      },
      {
        titre: "Tunnel WordPress pour offre corporate : structure et conversion",
        slug: "tunnel-wordpress-offre-corporate",
        intent: "décisionnelle",
        mots_cibles: ["tunnel vente formation corporate wordpress", "page offre b2b wordpress"],
        priorite: "🟠 M2",
        angle: "Filtrer les RH des curieux. Lead scoring. Qualification avant devis.",
      },
      {
        titre: "Reporting apprenant B2B sur WordPress : quels KPIs mesurer ?",
        slug: "reporting-apprenant-b2b-wordpress-kpi",
        intent: "informationnelle",
        mots_cibles: ["reporting formation b2b wordpress", "kpi apprenant lms entreprise"],
        priorite: "🟡 M3",
        angle: "Tableaux de bord décideur (DRH) vs tableau formateur. Ce qui convainc un renouvellement.",
      },
    ],
    kpis: [
      "6 contenus stratégiques publiés (pilier + 5 satellites)",
      "Score Autorité Pilier > 85 (évaluation PillarAuthorityAgent)",
      "Maillage interne dense entre les 6 contenus",
      "Position Top 20 sur 3 requêtes niche longue traîne",
      "1 schema FAQ + JSON-LD sur chaque page",
      "Page pilier indexée et crawlée (Search Console)",
    ],
    actions_techniques: [
      "Créer le cluster dans n8n/Notion avec suivi position GSC",
      "Installer schema FAQ sur toutes les pages",
      "Maillage interne : chaque satellite renvoie vers le pilier",
      "Soumettre le sitemap après chaque publication",
      "Ouvrir un projet Search Console dédié cluster B2B",
    ],
  },
  {
    num: "2",
    emoji: "🟢",
    label: "PROFONDEUR & AUTORITÉ",
    periode: "Mois 4 – 6",
    objectif: "Doubler la profondeur du cluster. Couvrir les angles manquants. Amorcer les AI Overviews.",
    couleur: "green_background",
    nouveaux_contenus: [
      {
        titre: "Comparatif LMS B2B WordPress : Tutor LMS, LearnDash, LifterLMS pour entreprise",
        intent: "comparative",
        angle: "Pas un comparatif standard — sous l'angle B2B exclusivement : multi-accès, groupes, QUALIOPI",
        priorite: "🔴 M4",
      },
      {
        titre: "CRM natif WordPress vs HubSpot pour formateurs B2B : lequel choisir ?",
        intent: "comparative décisionnelle",
        angle: "Angle schoolsWP : garder WordPress souverain vs dépendance SaaS. Coût total, autonomie, données.",
        priorite: "🔴 M4",
      },
      {
        titre: "Structurer les contrats et espaces apprenants sur WordPress",
        intent: "informationnelle",
        angle: "Juridique + technique. Accords-cadres, CGU formation, espace client sécurisé.",
        priorite: "🟠 M5",
      },
      {
        titre: "Automatiser le renouvellement contrat formation B2B avec WordPress",
        intent: "informationnelle → décisionnelle",
        angle: "Séquence J-90/J-60/J-30. FluentCRM. Pipeline renouvellement. Taux moyen marché.",
        priorite: "🟠 M5",
      },
      {
        titre: "Sécuriser les accès formation entreprise sur WordPress",
        intent: "informationnelle",
        angle: "Tokens, SSO simplifié, gestion des départs salariés, RGPD données apprenants.",
        priorite: "🟡 M6",
      },
      {
        titre: "Étude de cas : système WordPress formation B2B — de l'audit à l'automatisation",
        intent: "décisionnelle",
        angle: "Cas structuré (anonymisé). Avant/après. Résultats mesurés. Crédibilité maximale.",
        priorite: "🔴 M6",
      },
    ],
    kpis: [
      "12 à 15 articles niche publiés au total",
      "1 étude de cas complète publiée",
      "Début d'apparition en AI Overviews (vérification Thruuu)",
      "3 à 5 leads qualifiés entrants (formulaire qualification)",
      "Position Top 10 sur 2 requêtes longue traîne",
      "Partages LinkedIn sur au moins 3 articles",
    ],
    actions_techniques: [
      "Créer prompts Thruuu pour monitoring AI mentions (ChatGPT, Perplexity, Gemini)",
      "Optimiser les H2/H3 pour format question-réponse AIO",
      "Ajouter schema Article + BreadcrumbList",
      "Analyser les questions GSC et enrichir le pilier",
      "Contacter 2 formateurs B2B pour témoignage (même informel)",
    ],
  },
  {
    num: "3",
    emoji: "🟣",
    label: "DÉCISION & CONVERSION",
    periode: "Mois 7 – 9",
    objectif: "Créer du contenu décisionnel fort. Transformer le trafic en leads qualifiés.",
    couleur: "purple_background",
    nouveaux_contenus: [
      {
        titre: "Combien coûte un LMS WordPress B2B ? Prix réel et architecture",
        intent: "décisionnelle",
        angle: "Transparence totale. Fourchettes réelles. Coût total possession vs SaaS. CTA Audit.",
        priorite: "🔴 M7",
      },
      {
        titre: "Architecture idéale pour formateur corporate WordPress en 2026",
        intent: "décisionnelle",
        angle: "Blueprint complet. Stack recommandé. Budget. Timeline. Erreurs à éviter.",
        priorite: "🔴 M7",
      },
      {
        titre: "7 erreurs critiques des formateurs B2B sur WordPress",
        intent: "informationnelle",
        angle: "Erreurs réelles vécues. Coût de chaque erreur. Solution pour chacune. Ton direct.",
        priorite: "🟠 M8",
      },
      {
        titre: "Checklist audit LMS B2B WordPress : 25 points à vérifier",
        intent: "informationnelle → décisionnelle",
        angle: "Asset téléchargeable. Génère des leads naturellement. Lead magnet SEO.",
        priorite: "🟠 M8",
      },
      {
        titre: "QUALIOPI et WordPress : ce que les formateurs ne configurent jamais",
        intent: "informationnelle urgente",
        angle: "Réglementation + technique. Zéro concurrent. Anxiété forte chez les OFs.",
        priorite: "🔴 M9",
      },
    ],
    ctas_a_ajouter: [
      "CTA Audit Architecture B2B (1 200–1 800 €) sur chaque article",
      "CTA Checklist téléchargeable (lead magnet → liste email)",
      "CTA Prise de contact directe (formulaire qualifiant)",
      "Popup intention de sortie sur articles décisionnels",
    ],
    kpis: [
      "5 à 10 leads qualifiés entrants sur le trimestre",
      "2 à 3 missions premium signées (Niveau 2 ou 3)",
      "Top 5 sur au moins 1 requête niche principale",
      "Taux de conversion formulaire > 15%",
      "Apparition régulière en AI Overviews (Perplexity / ChatGPT)",
      "1 000+ visiteurs/mois sur le cluster",
    ],
    actions_techniques: [
      "A/B test CTA Audit (version courte vs argumentée)",
      "Heatmap sur pages à fort trafic (Clarity ou Hotjar)",
      "Optimiser la page schoolswp.com/b2b (conversion + SEO)",
      "Créer page /checklist-lms-b2b avec lead magnet",
      "Analyse GSC : requêtes position 6-15 à booster",
    ],
  },
  {
    num: "4",
    emoji: "🔴",
    label: "DOMINATION & OPTIMISATION",
    periode: "Mois 10 – 12",
    objectif: "Consolider l'autorité. Optimiser sur données réelles. Renforcer les signaux E-E-A-T.",
    couleur: "red_background",
    actions: [
      {
        cat: "Mise à jour contenus",
        items: [
          "Mise à jour pilier principal (nouvelles données, études de cas, stats)",
          "Enrichissement des 5 premiers satellites (FAQ, examples, schémas)",
          "Réactualisation dates et statistiques QUALIOPI + marché LMS",
          "Ajout de vrais témoignages clients sur articles décisionnels",
        ],
      },
      {
        cat: "LLM & AIO Optimisation",
        items: [
          "Passer tous les articles via LlmOptimizerAgent (encadrés définition, réponse rapide)",
          "Ajouter blocs 'Ce qu'il faut retenir' sur chaque article",
          "Optimiser les réponses directes (format question→réponse en 2 phrases)",
          "Vérifier présence sur ChatGPT, Perplexity, Gemini via Thruuu",
        ],
      },
      {
        cat: "Conversion & Optimisation",
        items: [
          "Optimiser pages à fort trafic mais faible conversion (heatmap + tests)",
          "Créer un funnel email post-lead-magnet (5 emails, 10 jours)",
          "Améliorer les CTAs selon données réelles (taux clic, taux lead)",
          "Tester landing page dédiée 'Audit Architecture B2B'",
        ],
      },
      {
        cat: "Autorité Externe",
        items: [
          "2 guest posts ciblés (blogs formation, WordPress, QUALIOPI)",
          "Interview ou podcast formateurs B2B WordPress",
          "Contribution forum QUALIOPI ou LinkedIn Formateurs Pro",
          "Backlinks ciblés depuis ressources OF et CFA",
        ],
      },
      {
        cat: "Maillage & Technique",
        items: [
          "Audit maillage interne complet (liens orphelins, opportunités manquées)",
          "Core Web Vitals : optimiser les 3 pages à plus fort trafic",
          "Canonicals vérifiés sur toutes les pages cluster",
          "Sitemap XML mis à jour et résoumis",
        ],
      },
    ],
    kpis: [
      "Top 5 sur au moins 3 requêtes niche principales",
      "Top 10 sur 5 requêtes longue traîne",
      "10+ leads qualifiés / trimestre",
      "5+ projets premium réalisés ou en cours",
      "Études de cas publiées et rankeées",
      "MRR accompagnement : 2 400 – 5 000 €/mois",
      "Mention régulière en AI Overviews (ChatGPT, Perplexity, Gemini)",
    ],
  },
];

const STRATEGIE_EDITORIALE = {
  ratio: [
    { pct: 40, categorie: "Architecture système", description: "LMS multi-entreprises, stack WordPress B2B, blueprints complets, guides d'implémentation" },
    { pct: 30, categorie: "CRM B2B", description: "Pipeline commercial, automatisations, renouvellement, segmentation décideur/apprenant" },
    { pct: 20, categorie: "LMS technique", description: "Configuration avancée, sécurité accès, QUALIOPI, reporting, multi-cohortes" },
    { pct: 10, categorie: "SEO niche spécifique", description: "Comparatifs B2B, coûts réels, erreurs critiques, checklists téléchargeables" },
  ],
  formats: [
    { format: "Guide complet", freq: "1 / mois", longueur: "3 500 – 5 000 mots", role: "Autorité + AI Overviews" },
    { format: "Article satellite", freq: "1-2 / mois", longueur: "1 800 – 2 500 mots", role: "Longue traîne + maillage" },
    { format: "Comparatif B2B", freq: "1 / trimestre", longueur: "2 500 – 3 500 mots", role: "Intention décisionnelle haute" },
    { format: "Étude de cas", freq: "1 / semestre", longueur: "2 000 – 3 000 mots", role: "Crédibilité + leads qualifiés" },
    { format: "Checklist", freq: "1 / trimestre", longueur: "500 – 800 mots + PDF", role: "Lead magnet + positionnement expert" },
  ],
  frequence_cible: "2 articles / mois minimum — qualité > quantité",
  ton: "Direct. Expert. Concret. Jamais condescendant. Tutoiement. Pas de jargon marketing.",
};

const SIGNAUX_DOMINATION = [
  {
    signal: "Tu es cité en AI Overviews",
    detail: "ChatGPT, Perplexity, Gemini te mentionnent sur les requêtes 'LMS WordPress B2B' et 'architecture formation entreprise'.",
    comment_mesurer: "Thruuu monitoring + tests manuels mensuels sur 10 prompts clés",
  },
  {
    signal: "Tes articles apparaissent sur requêtes longues niche",
    detail: "Requêtes de 5-8 mots très précises ('lms wordpress multi-entreprises qualiopi') → tes articles ressortent en Top 5.",
    comment_mesurer: "Search Console + Ahrefs / DataForSEO sur les requêtes cibles",
  },
  {
    signal: "Tu reçois des leads qualifiés organiquement",
    detail: "Des formateurs B2B te contactent via le formulaire d'audit, avec un contexte précis et un budget estimé.",
    comment_mesurer: "Taux de leads qualifiés (budget > 3 000 €) / total leads entrants",
  },
  {
    signal: "Tes études de cas rankent",
    detail: "Tes études de cas apparaissent en Top 10 sur les requêtes 'système formation B2B WordPress'.",
    comment_mesurer: "Position GSC sur URLs des études de cas, taux de clic",
  },
  {
    signal: "Les formateurs B2B partagent tes contenus",
    detail: "Tes articles circulent sur LinkedIn dans les cercles formation B2B sans que tu les pousses.",
    comment_mesurer: "LinkedIn analytics sur partages organiques, mentions de @schoolsWP",
  },
];

const IMPACT_BUSINESS = {
  scenarios: [
    {
      label: "Conservateur",
      an1_leads: "8 – 12 leads qualifiés",
      an1_missions: "3 à 5 missions signées",
      ca_an1: "15 000 – 30 000 €",
      note: "Objectif réaliste pour une première année sur un marché vierge.",
    },
    {
      label: "Ciblé",
      an1_leads: "15 – 25 leads qualifiés",
      an1_missions: "6 à 10 missions signées",
      ca_an1: "35 000 – 65 000 €",
      note: "Possible si exécution régulière + LinkedIn actif + 1 étude de cas forte.",
    },
    {
      label: "Dominant",
      an1_leads: "30+ leads qualifiés",
      an1_missions: "12+ missions signées",
      ca_an1: "80 000 – 130 000 €",
      note: "Si référence établie + MRR accompagnement + affiliation + 1 produit digital.",
    },
  ],
  revenus_annexes: [
    { source: "Affiliation (Tutor LMS, FluentCRM, WooCommerce)", potentiel: "500 – 2 000 €/mois", delai: "Dès M6 si trafic suffisant" },
    { source: "Produit digital (template B2B WordPress System™)", potentiel: "1 000 – 3 000 €/mois", delai: "Dès M9 si étude de cas publiée" },
    { source: "MRR accompagnement (3 à 5 clients)", potentiel: "2 400 – 7 500 €/mois", delai: "Dès M8 si premières missions livrées" },
  ],
  ca_total_an1: {
    mini: 15000 + 6 * 500 + 3 * 1200,
    maxi: 130000 + 12 * 2000 + 12 * 3000,
  },
};

const OUTILS_MONITORING = [
  { outil: "Google Search Console", usage: "Positions, impressions, requêtes émergentes, CTR", freq: "Hebdomadaire" },
  { outil: "Thruuu", usage: "Monitoring AI Overviews sur 10-20 prompts clés B2B", freq: "Mensuel" },
  { outil: "Ahrefs / DataForSEO", usage: "Autorité domaine, backlinks, positions concurrents", freq: "Mensuel" },
  { outil: "KnowledgeGraphAgent", usage: "Cartographie entités, zones blanches, cohérence cluster", freq: "Trimestriel" },
  { outil: "PillarAuthorityAgent", usage: "Score autorité pilier /100, recommandations", freq: "Trimestriel" },
  { outil: "Microsoft Clarity", usage: "Heatmaps, sessions, scroll depth sur pages à fort trafic", freq: "Mensuel" },
];

// ─── CALC ─────────────────────────────────────────────────────────────────────

const total_articles = TRIMESTRES.reduce((acc, t) => {
  if (t.satellites) return acc + 1 + t.satellites.length;
  if (t.nouveaux_contenus) return acc + t.nouveaux_contenus.length;
  return acc;
}, 0);

// T1: 6, T2: 6, T3: 5, T4: optimisations → ~17 nouveaux + 4 mises à jour
const articles_nouveaux = 6 + 6 + 5;
const articles_maj = 4;

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

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

// ─── BLOCK BUILDERS ──────────────────────────────────────────────────────────

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: String(text) },
  annotations: {
    bold: opts.bold || false,
    italic: opts.italic || false,
    code: opts.code || false,
    color: opts.color || "default",
  },
});

const h1 = (text) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(text)] } });
const h2 = (text) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(text)] } });
const h3 = (text) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(text)] } });
const p = (rts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const bul = (rts, color = "default") => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)], color } });
const num = (rts) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const qot = (text, color = "gray_background") => ({ object: "block", type: "quote", quote: { rich_text: Array.isArray(text) ? text : [rt(text)], color } });
const cal = (text, color = "blue_background") => ({
  object: "block",
  type: "callout",
  callout: {
    rich_text: Array.isArray(text) ? text : [rt(text)],
    icon: { type: "emoji", emoji: "💡" },
    color,
  },
});
const tog = (text, children = []) => ({
  object: "block",
  type: "toggle",
  toggle: { rich_text: [rt(text, { bold: true })], children },
});

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("🗺 Stratégie SEO Domination B2B · schoolsWP · 12 Mois · Document Stratégique", "yellow_background"));
  blocks.push(p([
    rt("Objectif : Devenir la référence francophone WordPress pour formateurs B2B. ", { italic: true }),
    rt(`${articles_nouveaux} articles · ${articles_maj} mises à jour · 4 trimestres exécutables.`, { italic: true, color: "gray" }),
  ]));
  blocks.push(div());

  // ── PHASE 0 — POSITIONNEMENT ÉDITORIAL ──
  blocks.push(h1("🧠 Phase 0 — Positionnement Éditorial"));
  blocks.push(cal([rt(POSITIONNEMENT_EDITORIAL.axiome, { bold: true })], "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Tu ne produis PAS ces contenus :"));
  POSITIONNEMENT_EDITORIAL.pas.forEach((item) => {
    const children = [
      p([rt("Pourquoi non : ", { bold: true }), rt(item.pourquoi, { italic: true })]),
    ];
    blocks.push(tog(`✗  ${item.kw}`, children));
  });
  blocks.push(p(""));

  blocks.push(h2("Tu produis CES contenus :"));
  POSITIONNEMENT_EDITORIAL.oui.forEach((item) => {
    const children = [
      p([rt("Intention : ", { bold: true }), rt(item.intent)]),
      p([rt("Opportunité : ", { bold: true }), rt(item.opportunite, { color: "green" })]),
    ];
    blocks.push(tog(`✓  ${item.kw}`, children));
  });
  blocks.push(div());

  // ── VUE D'ENSEMBLE ──
  blocks.push(h1("📋 Vue d'Ensemble — 12 Mois"));
  blocks.push(p(""));

  const vue = [
    ["Trimestre", "Période", "Focus", "Nouveaux contenus", "Objectif clé"],
    ["T1 🔵", "M1–M3", "Fondation Cluster Pilier", "6 (pilier + 5 satellites)", "Top 20 requêtes niche"],
    ["T2 🟢", "M4–M6", "Profondeur & Autorité", "6 (dont 1 étude de cas)", "Début AI Overviews"],
    ["T3 🟣", "M7–M9", "Décision & Conversion", "5 (décisionnels)", "5–10 leads qualifiés"],
    ["T4 🔴", "M10–M12", "Domination & Optimisation", "4 mises à jour + backlinks", "Top 5 × 3 requêtes"],
  ];
  vue.forEach((row, i) => {
    blocks.push(bul(
      [rt(row.join("  ·  "), { bold: i === 0, code: i === 0 })],
      i === 0 ? "gray_background" : "default"
    ));
  });
  blocks.push(p(""));
  blocks.push(bul([
    rt("Total : ", { bold: true }),
    rt(`${articles_nouveaux} nouveaux articles + ${articles_maj} mises à jour majeures · Rythme : 2 articles / mois minimum`),
  ]));
  blocks.push(div());

  // ── TRIMESTRES ──
  for (const t of TRIMESTRES) {
    blocks.push(h1(`${t.emoji} Trimestre ${t.num} — ${t.label}  (${t.periode})`));
    blocks.push(cal([rt(t.objectif)], t.couleur));
    blocks.push(p(""));

    // T1 — Pilier + Satellites
    if (t.pilier) {
      blocks.push(h2("🧱 Pilier Principal"));
      const pilierChildren = [];
      pilierChildren.push(p([rt("Type : ", { bold: true }), rt(t.pilier.type)]));
      pilierChildren.push(p([rt("Longueur : ", { bold: true }), rt(t.pilier.longueur)]));
      pilierChildren.push(p([rt("Slug cible : ", { bold: true }), rt(t.pilier.slug, { code: true })]));
      pilierChildren.push(p([rt("Angle rédactionnel : ", { bold: true }), rt(t.pilier.angle, { italic: true })]));
      pilierChildren.push(p(""));
      pilierChildren.push(h3("Structure recommandée"));
      t.pilier.structure.forEach((s, i) => pilierChildren.push(num(`${s}`)));
      pilierChildren.push(p(""));
      pilierChildren.push(h3("Questions cibles AI Overviews"));
      t.pilier.cibles_ai.forEach((q) => pilierChildren.push(bul([rt("→ ", { color: "blue" }), rt(q, { italic: true })])));

      blocks.push(tog(`📌 ${t.pilier.titre}`, pilierChildren));
      blocks.push(p(""));

      blocks.push(h2("🧩 5 Satellites"));
      for (const sat of t.satellites) {
        const satChildren = [];
        satChildren.push(p([rt("Priorité : ", { bold: true }), rt(sat.priorite)]));
        satChildren.push(p([rt("Slug : ", { bold: true }), rt(sat.slug, { code: true })]));
        satChildren.push(p([rt("Intention : ", { bold: true }), rt(sat.intent)]));
        satChildren.push(p([rt("Mots-clés cibles : ", { bold: true }), rt(sat.mots_cibles.join(", "))]));
        satChildren.push(p([rt("Angle : ", { bold: true }), rt(sat.angle, { italic: true })]));
        blocks.push(tog(`${sat.priorite}  ${sat.titre}`, satChildren));
        blocks.push(p(""));
      }
    }

    // T2 — Nouveaux contenus
    if (t.nouveaux_contenus) {
      blocks.push(h2("📝 Nouveaux Contenus"));
      for (const c of t.nouveaux_contenus) {
        const cChildren = [];
        cChildren.push(p([rt("Priorité : ", { bold: true }), rt(c.priorite)]));
        cChildren.push(p([rt("Intention : ", { bold: true }), rt(c.intent)]));
        cChildren.push(p([rt("Angle : ", { bold: true }), rt(c.angle, { italic: true })]));
        blocks.push(tog(`${c.priorite}  ${c.titre}`, cChildren));
        blocks.push(p(""));
      }
    }

    // T3 — Contenus décisionnels + CTAs
    if (t.ctas_a_ajouter) {
      blocks.push(h2("🎯 CTAs à Ajouter sur Tous les Articles"));
      t.ctas_a_ajouter.forEach((cta) => blocks.push(bul([rt("→ " + cta, { bold: true })])));
      blocks.push(p(""));
    }

    // T4 — Actions par catégorie
    if (t.actions) {
      blocks.push(h2("⚙️ Actions par Catégorie"));
      for (const cat of t.actions) {
        const catChildren = [];
        cat.items.forEach((item) => catChildren.push(bul(item)));
        blocks.push(tog(`📂 ${cat.cat}`, catChildren));
        blocks.push(p(""));
      }
    }

    // KPIs
    blocks.push(h2(`📊 KPIs T${t.num}`));
    t.kpis.forEach((kpi) => {
      blocks.push({
        object: "block",
        type: "to_do",
        to_do: { rich_text: [rt(kpi)], checked: false },
      });
    });

    // Actions techniques (T1 et T2)
    if (t.actions_techniques) {
      blocks.push(p(""));
      blocks.push(h2("⚙️ Actions Techniques"));
      t.actions_techniques.forEach((a) => blocks.push(bul(a)));
    }

    blocks.push(div());
  }

  // ── STRATÉGIE ÉDITORIALE ──
  blocks.push(h1("🧠 Stratégie Éditoriale — Le Ratio qui Définit l'Autorité"));
  blocks.push(p(""));
  blocks.push(bul([rt(`Fréquence cible : ${STRATEGIE_EDITORIALE.frequence_cible}`, { bold: true })]));
  blocks.push(bul([rt(`Ton : ${STRATEGIE_EDITORIALE.ton}`, { italic: true })]));
  blocks.push(p(""));

  blocks.push(h2("Ratio Contenu Cible"));
  STRATEGIE_EDITORIALE.ratio.forEach((r) => {
    blocks.push(bul([
      rt(`${r.pct}%  `, { bold: true, color: "green" }),
      rt(`${r.categorie}`, { bold: true }),
      rt(` — ${r.description}`, { italic: true }),
    ]));
  });
  blocks.push(p(""));

  blocks.push(h2("Formats & Fréquences"));
  for (const fmt of STRATEGIE_EDITORIALE.formats) {
    const children = [];
    children.push(p([rt("Fréquence : ", { bold: true }), rt(fmt.freq)]));
    children.push(p([rt("Longueur : ", { bold: true }), rt(fmt.longueur)]));
    children.push(p([rt("Rôle SEO : ", { bold: true }), rt(fmt.role)]));
    blocks.push(tog(`📄 ${fmt.format}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SIGNAUX DE DOMINATION ──
  blocks.push(h1("📈 Signaux de Domination Réelle"));
  blocks.push(p([rt("Tu sais que tu domines quand ces 5 signaux sont présents :", { italic: true })]));
  blocks.push(p(""));

  for (const signal of SIGNAUX_DOMINATION) {
    const children = [];
    children.push(qot(signal.detail, "blue_background"));
    children.push(p([rt("Comment mesurer : ", { bold: true }), rt(signal.comment_mesurer, { italic: true })]));
    blocks.push(tog(`✓ ${signal.signal}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── IMPACT BUSINESS ──
  blocks.push(h1("💰 Impact Business Potentiel — An 1"));
  blocks.push(p(""));

  for (const sc of IMPACT_BUSINESS.scenarios) {
    const children = [];
    children.push(p([rt("Leads qualifiés : ", { bold: true }), rt(sc.an1_leads)]));
    children.push(p([rt("Missions signées : ", { bold: true }), rt(sc.an1_missions)]));
    children.push(p([rt("CA missions : ", { bold: true }), rt(sc.ca_an1, { bold: true, color: "green" })]));
    children.push(p([rt("Note : ", { bold: true, color: "gray" }), rt(sc.note, { italic: true })]));
    blocks.push(tog(`📊 Scénario ${sc.label}  —  ${sc.ca_an1}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(h2("Revenus Annexes (non comptés dans projections missions)"));
  IMPACT_BUSINESS.revenus_annexes.forEach((r) => {
    blocks.push(bul([
      rt(`${r.source} : `, { bold: true }),
      rt(`${r.potentiel}`, { bold: true, color: "green" }),
      rt(` · Délai : ${r.delai}`, { italic: true, color: "gray" }),
    ]));
  });
  blocks.push(p(""));
  blocks.push(cal(
    "Un formateur B2B = budget élevé. 3 à 5 projets premium / an = très bon revenu. 10+ missions / an = référence établie.",
    "purple_background"
  ));
  blocks.push(div());

  // ── OUTILS MONITORING ──
  blocks.push(h1("🛠 Outils de Monitoring SEO"));
  blocks.push(p(""));
  for (const outil of OUTILS_MONITORING) {
    blocks.push(bul([
      rt(`${outil.outil} : `, { bold: true }),
      rt(`${outil.usage} `, {}),
      rt(`(${outil.freq})`, { italic: true, color: "gray" }),
    ]));
  }
  blocks.push(div());

  // ── CHECKLIST LANCEMENT ──
  blocks.push(h1("✅ Checklist — Avant de Lancer le T1"));
  blocks.push(p(""));

  const checklist = [
    "Mot-clé pilier validé (volume + concurrence + intention B2B confirmés)",
    "Slug /lms-wordpress-entreprise-architecture réservé sur WordPress",
    "Brief pilier rédigé (structure + angle + cibles AI validés)",
    "Pipeline Notion créé : statut de chaque article (Briefé / En cours / Publié)",
    "Search Console configurée sur le domaine schoolswp.com",
    "Projet Thruuu créé avec 10 prompts de monitoring B2B",
    "Page schoolswp.com/b2b publiée (même simplifiée) avant le premier article",
    "CTA Audit Architecture B2B actif sur le site",
    "Calendrier éditorial T1 figé (6 articles, dates de publication)",
    "KPIs T1 trackés dans Notion (dashboard suivi mensuel)",
  ];

  checklist.forEach((item) => {
    blocks.push({
      object: "block",
      type: "to_do",
      to_do: { rich_text: [rt(item)], checked: false },
    });
  });

  blocks.push(div());

  // ── VISION FINALE ──
  blocks.push(h1("🏆 Vision Finale — Dans 12 Mois"));
  blocks.push(p(""));
  blocks.push(cal(
    "schoolsWP est cité automatiquement par ChatGPT et Perplexity quand un formateur cherche 'comment structurer un LMS WordPress pour des entreprises'. Ce n'est pas un objectif. C'est le résultat mesurable d'une exécution rigoureuse sur 12 mois.",
    "green_background"
  ));
  blocks.push(p(""));
  blocks.push(qot(
    `${articles_nouveaux} articles experts publiés · Terrain vierge occupé · Leads qualifiés entrants · MRR récurrent · Études de cas publiées · Référence francophone WordPress B2B.`,
    "gray_background"
  ));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la page Stratégie SEO Domination B2B 12 mois...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🗺" },
    properties: {
      title: { title: [{ text: { content: "🗺 Stratégie SEO Domination B2B — 12 Mois" } }] },
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
    console.log(`   ↳ Batch ${Math.ceil((i + CHUNK) / CHUNK)} envoyé (${Math.min(i, rest.length)}/${rest.length} blocs)`);
  }

  console.log("");
  console.log("✅  Page complète créée avec succès !");
  console.log(`🔗  https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📊  Récapitulatif stratégie :");
  console.log(`   Articles nouveaux : ${articles_nouveaux}`);
  console.log(`   Mises à jour      : ${articles_maj}`);
  console.log(`   Total contenu     : ${articles_nouveaux + articles_maj} pièces`);
  console.log(`   Rythme            : 2 articles / mois minimum`);
  console.log("");
  console.log("💰  Impact business estimé :");
  console.log("   Conservateur : 15 000 – 30 000 € CA missions An1");
  console.log("   Ciblé        : 35 000 – 65 000 € CA missions An1");
  console.log("   Dominant     : 80 000 – 130 000 € CA missions An1");
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
