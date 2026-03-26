#!/usr/bin/env node
"use strict";

/**
 * setup-notion-pricing-premium-calibre.js
 * Crée la page Notion : 💰 Pricing Premium Calibré B2B — Architecte Système WordPress
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-pricing-premium-calibre.js
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

const PRINCIPE = {
  axiome: "Tu ne vends pas des heures. Tu vends un résultat business.",
  pas: [
    "Du temps (heures, jours, semaines)",
    "Des plugins installés",
    "Des pages créées",
    "Une prestation technique",
  ],
  oui: [
    { valeur: "Architecture business", impact: "Le client comprend son système entier, pas juste son LMS." },
    { valeur: "Structuration B2B", impact: "Son offre formation devient crédible auprès des entreprises." },
    { valeur: "Réduction de complexité", impact: "Il gère 10 clients entreprise avec le même effort que 2." },
    { valeur: "Accélération des revenus", impact: "Cycle de vente plus court, renouvellements automatisés." },
    { valeur: "Sécurisation B2B", impact: "Il ne perd plus de contrats à cause d'un LMS mal structuré." },
  ],
  conclusion: "Pricing basé sur la valeur perçue — pas sur le temps passé. Le client paie ce que ça lui apporte, pas ce que ça te coûte.",
};

const OFFRES = [
  {
    rang: "🥉",
    num: "1",
    nom: "Audit & Architecture B2B",
    emoji_statut: "🟢",
    objectif: "Diagnostiquer et structurer. Clarifier avant d'implémenter.",
    role: "Entrée premium sans implémentation. Filtre les clients sérieux. Ouvre naturellement l'Offre 2.",
    prix_mini: 1200,
    prix_maxi: 2000,
    prix_affiche: "1 200 € – 2 000 €",
    prix_cible: 1500,
    inclus: [
      { item: "Audit technique WordPress", detail: "Stack, performance, sécurité, dette technique, scalabilité." },
      { item: "Audit LMS", detail: "Structure multi-entreprises, scalabilité, UX corporate, gestion cohortes." },
      { item: "Audit CRM", detail: "Segmentation, pipeline, automatisations actives vs manquantes." },
      { item: "Audit tunnel B2B", detail: "De la prospection à la facturation. Points de fuite identifiés." },
      { item: "Roadmap d'architecture personnalisée", detail: "Actions priorisées par impact/effort sur 90 jours." },
      { item: "Call stratégique 90 min", detail: "Restitution complète. Recommandations hiérarchisées. Questions/réponses." },
      { item: "Document PDF structuré (20–30 pages)", detail: "Rapport professionnel. Livré dans les 10 jours ouvrés." },
    ],
    duree: "2 semaines",
    paiement: "100% à la signature",
    cible: "Tout formateur B2B — c'est le point d'entrée universel.",
    justification_prix: [
      "Un formateur B2B vend 3 000 € à 15 000 € par mission entreprise",
      "Un audit à 1 500 € = 10 à 50% d'une mission entreprise du client",
      "Si l'audit améliore 1 seul renouvellement → ROI immédiat",
      "Comparaison : un consultant stratégique facture 1 500 € / jour",
    ],
    upsell: "Offre 2 — B2B WordPress System (implémentation sur mesure basée sur l'audit)",
    signal_acheteur: "Budget formation confirmé. Minimum 5 clients entreprise existants ou en cours.",
  },
  {
    rang: "🥈",
    num: "2",
    nom: "B2B WordPress System™",
    emoji_statut: "🔵",
    objectif: "Construire ou restructurer le système complet. La transformation réelle.",
    role: "Cœur de business. Mission principale. Meilleur ratio valeur créée / temps investi.",
    prix_mini: 4000,
    prix_maxi: 8000,
    prix_affiche: "4 000 € – 8 000 €",
    prix_cible: 6000,
    inclus: [
      { item: "Architecture LMS B2B", detail: "Structuration multi-entreprises, cohortes, accès groupés, sécurité." },
      { item: "Comptes entreprises", detail: "Gestion séparée par client, permissions granulaires, interface corporate." },
      { item: "CRM segmenté", detail: "Tripartite : décideur / apprenant / RH. Pipelines distincts par rôle." },
      { item: "Automatisation onboarding", detail: "De la signature à l'accès LMS : flux entier automatisé." },
      { item: "Tunnel B2B", detail: "Page offre corporate, formulaire qualifiant, scoring prospect." },
      { item: "Paramétrage clé", detail: "Tracking GA4, performance Core Web Vitals, backups, sécurité." },
      { item: "Formation client", detail: "1 à 2 sessions de prise en main + vidéos Loom + documentation." },
    ],
    duree: "6 à 10 semaines",
    paiement: "40% signature · 40% mi-mission · 20% livraison",
    cible: "Formateur B2B avec base clients existante, veut structurer pour scaler.",
    variables_prix: [
      { variable: "Nombre d'entreprises clientes actuelles", impact: "+500 € si > 15 entreprises" },
      { variable: "Présence d'automatisations à migrer", impact: "+300 – 800 € selon complexité" },
      { variable: "Migration depuis un autre LMS (Kajabi, Teachable...)", impact: "+500 – 1 500 € selon volume" },
      { variable: "Historique CRM existant à intégrer", impact: "+300 – 600 € selon état" },
      { variable: "Urgence (délai < 4 semaines)", impact: "+20% sur le total" },
    ],
    justification_prix: [
      "Si 5 missions entreprise à 4 000 € = 20 000 € CA formateur",
      "Un système à 6 000 € = 30% d'une seule année de CA",
      "Si le système améliore le taux de renouvellement de 20% → +4 000 €/an sur une base de 5 clients",
      "ROI moyen estimé : × 3 à × 5 en 12 mois selon la taille de la base clients",
    ],
    upsell: "Offre 3 — Optimisation & Scalabilité (après 3 à 6 mois d'utilisation)",
    signal_acheteur: "A déjà complété l'Audit (Offre 1). Résultats de l'audit confirment le périmètre.",
  },
  {
    rang: "🥇",
    num: "3",
    nom: "Optimisation & Scalabilité B2B",
    emoji_statut: "🟣",
    objectif: "Optimiser les performances, automatiser les renouvellements, structurer la croissance.",
    role: "Crée le MRR. Stabilise la relation client long terme. Meilleure marge sur le temps investi.",
    prix_mini: 2500,
    prix_maxi: 5000,
    prix_affiche: "2 500 € – 5 000 € · ou retainer 800 – 1 500 €/mois",
    prix_cible: 1200,
    prix_retainer_mini: 800,
    prix_retainer_maxi: 1500,
    inclus: [
      { item: "Analyse KPI mensuelle", detail: "Dashboard : taux complétion, renouvellement, conversion tunnel, LTV." },
      { item: "Optimisation tunnel", detail: "Tests sur les pages offre, formulaires, séquences email — basé sur données réelles." },
      { item: "Segmentation avancée", detail: "Affinage des segments CRM. Scoring prospect affiné. Tagging comportemental." },
      { item: "Automatisations avancées", detail: "Nouvelles séquences (renouvellement, upsell, inactif), triggers avancés." },
      { item: "Upsell structuré", detail: "Parcours montée en gamme : de la formation de base vers l'accompagnement récurrent." },
    ],
    duree: "Contrat mensuel · minimum 3 mois",
    paiement: "Mensuel, 1er du mois, prélèvement ou virement",
    cible: "Client Offre 2 livré depuis 3 à 6 mois. Système en place. Prêt à optimiser.",
    objectif_mrr: "3 à 5 clients simultanés en retainer = 2 400 – 7 500 €/mois récurrent",
    justification_prix: [
      "800 – 1 500 €/mois = 2% à 5% du CA mensuel moyen d'un formateur B2B actif",
      "Le client ne reconstruit rien. Il optimise sur base existante.",
      "Accès expertise continue sans relancer un appel d'offres",
      "Valeur perçue : consultant stratégique dédié, pas un prestataire ponctuel",
    ],
    upsell: "Produit digital ou formation avancée (si profil adapté)",
    signal_acheteur: "Mission Offre 2 livrée depuis 2+ mois. Client satisfait. Premier résultat mesurable.",
  },
];

const JUSTIFICATION_MARCHE = {
  profil_client: "Formateur B2B francophone",
  ca_mission_mini: 3000,
  ca_mission_maxi: 15000,
  nb_missions_an: { mini: 5, maxi: 20 },
  ca_annuel_exemple: { mini: 5 * 3000, maxi: 20 * 15000 },
  besoins_qui_justifient_premium: [
    { besoin: "Cycles de vente longs (2 à 8 semaines)", impact_ton_offre: "Pipeline CRM + relances automatisées = cycles mieux gérés" },
    { besoin: "Clients qui travaillent avec des entreprises (DRH, RH)", impact_ton_offre: "LMS corporate + UX professionnelle = crédibilité renforcée" },
    { besoin: "Besoin de crédibilité pour accéder aux grands comptes", impact_ton_offre: "Architecture structurée = confiance acheteur institutionnel" },
    { besoin: "Besoin d'automatisation pour gérer le volume sans équipe", impact_ton_offre: "Onboarding auto + relances = gestion 10 clients sans effort manuel" },
    { besoin: "Besoin de reporting pour prouver la valeur aux DRH", impact_ton_offre: "Dashboard KPI = livrables clients décideurs, pas juste apprenants" },
  ],
  exemple_roi: {
    missions_an: 5,
    ca_par_mission: 4000,
    ca_total: 5 * 4000,
    investissement_offre2: 6000,
    ratio: (5 * 4000) / 6000,
  },
};

const STRATEGIE_AUGMENTATION = [
  {
    annee: "Année 1",
    emoji: "🌱",
    strategie: "Positionnement bas fourchette. Construire portefeuille + études de cas.",
    prix_offre1: "1 200 – 1 500 €",
    prix_offre2: "4 000 – 6 000 €",
    prix_offre3: "800 – 1 000 €/mois",
    objectif_missions: "3 à 5 missions",
    objectif_ca: "40 000 – 60 000 €",
    focus: [
      "Livrer 3 missions avec excellence documentée",
      "Obtenir 3 témoignages avec KPIs mesurés",
      "Publier 2 études de cas sur schoolswp.com",
      "Tester le process de vente (appel → audit → mission)",
    ],
    pourquoi_pas_plus_cher: "Pas encore d'études de cas publiées. La preuve sociale manque. Le positionnement se construit.",
  },
  {
    annee: "Année 2",
    emoji: "📈",
    strategie: "+20% sur les prix. S'appuyer sur les preuves An1.",
    prix_offre1: "1 500 – 2 000 €",
    prix_offre2: "5 000 – 8 000 €",
    prix_offre3: "1 000 – 1 500 €/mois",
    objectif_missions: "6 à 10 missions",
    objectif_ca: "70 000 – 120 000 €",
    focus: [
      "Augmenter les prix dès M13 — sans s'excuser",
      "Utiliser les témoignages An1 pour justifier la hausse",
      "Refuser activement les projets sous-calibrés",
      "Lancer le produit digital (template ou formation)",
    ],
    pourquoi_plus_cher: "3 études de cas publiées. Témoignages clients. Présence SEO amorcée. Crédibilité établie.",
  },
  {
    annee: "Année 3",
    emoji: "💎",
    strategie: "Sélection clients. Refus assumé. Rareté réelle.",
    prix_offre1: "1 800 – 2 500 €",
    prix_offre2: "7 000 – 15 000 €",
    prix_offre3: "1 500 – 2 500 €/mois",
    objectif_missions: "8 à 12 missions premium",
    objectif_ca: "100 000 – 200 000 €",
    focus: [
      "Refuser 30 à 50% des demandes (positionnement rareté)",
      "Clients uniquement par recommandation ou inbound SEO/LinkedIn",
      "Full System™ uniquement — pas d'Audit isolé",
      "MRR accompagnement : 5 à 8 clients simultanés",
    ],
    pourquoi_premium_assume: "Référence établie. AI Overviews. Études de cas solides. Plus besoin de convaincre.",
  },
];

const REGLES_PRICING = [
  {
    categorie: "JAMAIS",
    emoji: "⛔",
    regles: [
      { regle: "Afficher un prix bas pour 'attirer'", detail: "Un prix bas attire les mauvais clients. La rareté attire les bons clients." },
      { regle: "Justifier le prix en heures", detail: "'Ça représente 40h de travail' → tu te repositionnes en prestataire. Jamais." },
      { regle: "Proposer 12 options tarifaires", detail: "Trop de choix = paralysie. 3 niveaux maximum. Orienter le client." },
      { regle: "Baisser le prix sous la pression", detail: "Ajuster le périmètre si le budget ne suit pas. Jamais le prix." },
      { regle: "Commencer sans acompte", detail: "Acompte = engagement. Sans acompte, le client ne s'implique pas." },
      { regle: "Annoncer le prix avant d'avoir compris le contexte", detail: "Le prix vient après le diagnostic. Toujours." },
    ],
  },
  {
    categorie: "TOUJOURS",
    emoji: "✅",
    regles: [
      { regle: "Montrer la transformation", detail: "Le client voit où il est. Il voit où il sera. Le prix est entre les deux." },
      { regle: "Parler architecture, pas plugins", detail: "'Je structure votre architecture B2B' — pas 'j'installe FluentLMS et FluentCRM'." },
      { regle: "Parler performance business", detail: "Taux de renouvellement, cycle de vente, LTV, QUALIOPI. La langue du client." },
      { regle: "Parler scalabilité", detail: "'Dans 12 mois, vous pouvez doubler vos clients entreprise sans refondre.' Concret." },
      { regle: "Orienter naturellement vers l'offre adaptée", detail: "Pas Low/Mid/High. 'Vu votre situation, voici ce qui vous convient.'." },
      { regle: "Qualifier le budget avant tout discours commercial", detail: "Sans budget qualifié, pas de proposition. Économise du temps des deux côtés." },
    ],
  },
];

const DISCOURS_PREMIUM = [
  {
    contexte: "Présentation de l'activité",
    mauvais: "Je crée des LMS WordPress pour les formateurs.",
    bon: "Je structure l'architecture WordPress des formateurs B2B pour rendre leur offre rentable, automatisée et scalable.",
    pourquoi: "LMS = produit. Architecture = expertise. Formateurs B2B = niche précise. Rentable + automatisée + scalable = langue business.",
  },
  {
    contexte: "Réponse à 'vous faites quoi concrètement ?'",
    mauvais: "Je configure LMS, CRM, page de vente… bref, tout ce qui est WordPress.",
    bon: "Je prends un formateur B2B dont le système WordPress ralentit sa croissance — LMS pas scalable, CRM absent, tunnel non qualifiant — et je lui livre un écosystème complet qui tourne seul dans 10 semaines.",
    pourquoi: "Problème précis → solution précise → résultat chiffré. Pas une liste de tâches.",
  },
  {
    contexte: "Justification du tarif",
    mauvais: "C'est 6 000 € parce que ça me prend environ 6 semaines à 1 000 €/semaine.",
    bon: "Si votre système améliore votre taux de renouvellement de 15% sur vos 8 clients actuels à 4 000 € la mission — c'est 4 800 € de CA supplémentaire par an. Mon investissement est de 6 000 €. ROI en 15 mois.",
    pourquoi: "Prix justifié par le retour sur investissement du client, pas par le coût de production.",
  },
  {
    contexte: "Gestion de l'objection 'c'est cher'",
    mauvais: "Je comprends, on peut peut-être trouver une solution pour réduire le budget…",
    bon: "Permettez-moi de vous poser une question : combien vous coûte actuellement le fait de ne pas avoir ce système ? En temps d'administration, en missions perdues, en renouvellements non automatisés ?",
    pourquoi: "Retourner la question du coût vers le statu quo. Le problème non résolu est toujours plus cher que la solution.",
  },
  {
    contexte: "Réponse à 'j'ai trouvé moins cher'",
    mauvais: "Ah oui, mais moi je fais plus de choses, je suis plus qualitatif…",
    bon: "C'est possible. La question n'est pas le prix — c'est ce que vous obtenez. Un développeur peut vous configurer un LMS. Moi, je vous livre un système business complet avec CRM, automatisations et reporting. Ce sont deux choses différentes.",
    pourquoi: "Ne pas défendre. Clarifier la différence de valeur. Laisser le client décider en connaissance de cause.",
  },
];

const SCENARIOS_CA = [
  {
    label: "Démarrage An1",
    detail: "2 Audits + 2 Offres 2 + 1 MRR (6 mois)",
    calcul: {
      audits: { nb: 2, prix: 1500 },
      offres2: { nb: 2, prix: 5000 },
      mrr: { nb: 1, prix: 1200, mois: 6 },
    },
  },
  {
    label: "Régime de croisière An1",
    detail: "3 Audits + 3 Offres 2 + 2 MRR (8 mois)",
    calcul: {
      audits: { nb: 3, prix: 1500 },
      offres2: { nb: 3, prix: 6000 },
      mrr: { nb: 2, prix: 1200, mois: 8 },
    },
  },
  {
    label: "Objectif An2",
    detail: "3 Audits + 3 Offres 2 + 1 Offre 3 + 4 MRR (10 mois)",
    calcul: {
      audits: { nb: 3, prix: 1800 },
      offres2: { nb: 3, prix: 7000 },
      offres3: { nb: 1, prix: 3500 },
      mrr: { nb: 4, prix: 1300, mois: 10 },
    },
  },
  {
    label: "Dominance An3",
    detail: "2 Audits + 4 Offres 2/3 + 6 MRR (12 mois)",
    calcul: {
      audits: { nb: 2, prix: 2000 },
      offres2: { nb: 4, prix: 9000 },
      mrr: { nb: 6, prix: 1800, mois: 12 },
    },
  },
];

// ─── CALC ─────────────────────────────────────────────────────────────────────

const calcScenario = (sc) => {
  const { calcul } = sc;
  return (
    (calcul.audits ? calcul.audits.nb * calcul.audits.prix : 0) +
    (calcul.offres2 ? calcul.offres2.nb * calcul.offres2.prix : 0) +
    (calcul.offres3 ? calcul.offres3.nb * calcul.offres3.prix : 0) +
    (calcul.mrr ? calcul.mrr.nb * calcul.mrr.prix * calcul.mrr.mois : 0)
  );
};

const roi_exemple = JUSTIFICATION_MARCHE.exemple_roi;

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

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("💰 Pricing Premium Calibré B2B · Architecte Système WordPress · schoolsWP Agency", "yellow_background"));
  blocks.push(p([rt("Structure, cohérence, logique. Pas des prix au hasard.", { italic: true, bold: true })]));
  blocks.push(div());

  // ── PRINCIPE CLÉ ──
  blocks.push(h1("💎 Principe Clé — Tu ne Vends pas des Heures"));
  blocks.push(cal([rt(PRINCIPE.axiome, { bold: true })], "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Tu ne vends PAS :"));
  PRINCIPE.pas.forEach((item) => blocks.push(bul([rt("✗  " + item, { color: "red" })], "red_background")));
  blocks.push(p(""));

  blocks.push(h2("Tu vends :"));
  PRINCIPE.oui.forEach((item) => {
    blocks.push(bul([rt("✓  " + item.valeur + " : ", { bold: true, color: "green" }), rt(item.impact)], "green_background"));
  });
  blocks.push(p(""));
  blocks.push(qot(PRINCIPE.conclusion, "blue_background"));
  blocks.push(div());

  // ── 3 OFFRES ──
  blocks.push(h1("🧱 Structure d'Offre — 3 Niveaux"));
  blocks.push(p([rt("3 niveaux. Toujours démarrer par l'Offre 1 (Audit). L'Offre 2 se vend après l'Audit. L'Offre 3 se propose après 3 mois d'utilisation.", { italic: true })]));
  blocks.push(p(""));

  for (const offre of OFFRES) {
    const header = `${offre.rang} Offre ${offre.num} — ${offre.nom}  ·  ${offre.prix_affiche}`;
    const children = [];

    children.push(cal([rt(offre.role, { bold: true })], "gray_background"));
    children.push(p(""));
    children.push(p([rt("🎯 Objectif : ", { bold: true }), rt(offre.objectif, { italic: true })]));
    children.push(p([
      rt("💶 Prix : ", { bold: true }),
      rt(offre.prix_affiche, { bold: true, color: "green" }),
    ]));
    children.push(p([rt("⏱ Durée : ", { bold: true }), rt(offre.duree)]));
    children.push(p([rt("💳 Paiement : ", { bold: true }), rt(offre.paiement)]));
    children.push(p([rt("🎯 Cible : ", { bold: true }), rt(offre.cible)]));
    children.push(p(""));

    // Inclus
    children.push(h3("Ce qui est inclus"));
    for (const inc of offre.inclus) {
      const incChildren = [p([rt("Détail : ", { bold: true }), rt(inc.detail, { italic: true })])];
      children.push(tog(`→ ${inc.item}`, incChildren));
    }
    children.push(p(""));

    // Variables de prix (Offre 2 seulement)
    if (offre.variables_prix) {
      children.push(h3("Variables qui font monter le prix"));
      offre.variables_prix.forEach((v) => {
        children.push(bul([rt(`${v.variable} : `, { bold: true }), rt(v.impact, { color: "green" })]));
      });
      children.push(p(""));
    }

    // MRR cible (Offre 3 seulement)
    if (offre.objectif_mrr) {
      children.push(h3("Objectif MRR"));
      children.push(cal([rt(offre.objectif_mrr, { bold: true })], "purple_background"));
      children.push(p(""));
    }

    // Justification prix
    children.push(h3("Pourquoi ce prix est cohérent"));
    offre.justification_prix.forEach((j) => children.push(bul(j)));
    children.push(p(""));

    // Signal acheteur + upsell
    children.push(p([rt("→ Signal acheteur : ", { bold: true, color: "gray" }), rt(offre.signal_acheteur, { italic: true })]));
    children.push(p([rt("→ Upsell naturel : ", { bold: true, color: "gray" }), rt(offre.upsell, { italic: true })]));

    blocks.push(tog(header, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── JUSTIFICATION MARCHÉ ──
  blocks.push(h1("📈 Pourquoi ces Prix sont Cohérents — Contexte Marché"));
  blocks.push(p(""));

  const ca_mini = JUSTIFICATION_MARCHE.ca_annuel_exemple.mini;
  const ca_maxi = JUSTIFICATION_MARCHE.ca_annuel_exemple.maxi;

  blocks.push(p([
    rt("Un formateur B2B vend ", {}),
    rt(`${JUSTIFICATION_MARCHE.ca_mission_mini.toLocaleString("fr-FR")} – ${JUSTIFICATION_MARCHE.ca_mission_maxi.toLocaleString("fr-FR")} €`, { bold: true, color: "green" }),
    rt(" par mission entreprise, avec "),
    rt(`${JUSTIFICATION_MARCHE.nb_missions_an.mini} à ${JUSTIFICATION_MARCHE.nb_missions_an.maxi} contrats / an`),
    rt(` → ${ca_mini.toLocaleString("fr-FR")} – ${ca_maxi.toLocaleString("fr-FR")} €/an.`, { bold: true }),
  ]));
  blocks.push(p(""));

  blocks.push(h2("Besoins qui justifient le pricing premium"));
  JUSTIFICATION_MARCHE.besoins_qui_justifient_premium.forEach((b) => {
    const children = [
      p([rt("Impact de ton offre : ", { bold: true }), rt(b.impact_ton_offre, { color: "green" })]),
    ];
    blocks.push(tog(`→ ${b.besoin}`, children));
    blocks.push(p(""));
  });

  blocks.push(p(""));
  blocks.push(h2("Exemple ROI concret"));
  blocks.push(p([
    rt(`${roi_exemple.missions_an} missions entreprise × ${roi_exemple.ca_par_mission.toLocaleString("fr-FR")} € = `, {}),
    rt(`${roi_exemple.ca_total.toLocaleString("fr-FR")} € de CA`, { bold: true, color: "green" }),
  ]));
  blocks.push(p([
    rt("Investissement architecture : ", {}),
    rt(`${roi_exemple.investissement_offre2.toLocaleString("fr-FR")} €`, { bold: true }),
    rt(` = ${Math.round((roi_exemple.investissement_offre2 / roi_exemple.ca_total) * 100)}% du CA annuel`, { italic: true, color: "gray" }),
  ]));
  blocks.push(cal(
    `Ratio investissement/CA : × ${roi_exemple.ratio.toFixed(1)} — Le client récupère son investissement dès qu'il améliore 1 renouvellement.`,
    "green_background"
  ));
  blocks.push(div());

  // ── STRATÉGIE AUGMENTATION ──
  blocks.push(h1("🧠 Stratégie d'Augmentation Progressive — 3 ans"));
  blocks.push(p([rt("Le prix augmente quand la preuve augmente. Pas avant. Pas après.", { italic: true, bold: true })]));
  blocks.push(p(""));

  for (const annee of STRATEGIE_AUGMENTATION) {
    const children = [];
    children.push(p([rt("Stratégie : ", { bold: true }), rt(annee.strategie, { italic: true })]));
    children.push(p(""));
    children.push(p([rt("Prix Offre 1 : ", { bold: true }), rt(annee.prix_offre1, { color: "green" })]));
    children.push(p([rt("Prix Offre 2 : ", { bold: true }), rt(annee.prix_offre2, { bold: true, color: "green" })]));
    children.push(p([rt("Prix Offre 3 : ", { bold: true }), rt(annee.prix_offre3, { color: "green" })]));
    children.push(p([rt("Objectif missions : ", { bold: true }), rt(annee.objectif_missions)]));
    children.push(p([rt("Objectif CA : ", { bold: true }), rt(annee.objectif_ca, { bold: true, color: "green" })]));
    children.push(p(""));
    children.push(h3("Actions prioritaires"));
    annee.focus.forEach((f) => children.push(bul(f)));
    children.push(p(""));
    const raisonKey = annee.annee === "Année 1" ? "pourquoi_pas_plus_cher" : "pourquoi_plus_cher" in annee ? "pourquoi_plus_cher" : "pourquoi_premium_assume";
    children.push(qot(annee[raisonKey] || "", "blue_background"));

    blocks.push(tog(`${annee.emoji} ${annee.annee}  ·  ${annee.objectif_ca}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── RÈGLES PRICING ──
  blocks.push(h1("🏗 Règles Pricing Premium — Ce qui se fait / ne se fait jamais"));
  blocks.push(p(""));

  for (const cat of REGLES_PRICING) {
    blocks.push(h2(`${cat.emoji} ${cat.categorie}`));
    for (const r of cat.regles) {
      const children = [
        p([rt("Pourquoi : ", { bold: true }), rt(r.detail, { italic: true })]),
      ];
      const color = cat.categorie === "JAMAIS" ? "red_background" : "green_background";
      blocks.push(tog(`${cat.categorie === "JAMAIS" ? "⛔" : "✅"}  ${r.regle}`, children));
      blocks.push(p(""));
    }
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── DISCOURS PREMIUM ──
  blocks.push(h1("🔥 Discours Premium — Mot pour Mot"));
  blocks.push(p([rt("Ces formulations s'apprennent. Elles s'entraînent à voix haute. 5 min par jour pendant 2 semaines.", { italic: true })]));
  blocks.push(p(""));

  for (const d of DISCOURS_PREMIUM) {
    const children = [];
    children.push(p([rt("Contexte : ", { bold: true }), rt(d.contexte, { italic: true })]));
    children.push(p(""));
    children.push(bul([rt("✗  Mauvais : ", { bold: true, color: "red" }), rt(`"${d.mauvais}"`, { italic: true })], "red_background"));
    children.push(bul([rt("✓  Bon : ", { bold: true, color: "green" }), rt(`"${d.bon}"`, { italic: true })], "green_background"));
    children.push(p(""));
    children.push(p([rt("Pourquoi ça change tout : ", { bold: true }), rt(d.pourquoi, { italic: true, color: "gray" })]));

    blocks.push(tog(`🎤 ${d.contexte}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SCÉNARIOS CA ──
  blocks.push(h1("📊 Scénarios CA — Hypothèses Réalistes"));
  blocks.push(p(""));

  for (const sc of SCENARIOS_CA) {
    const ca = calcScenario(sc);
    const children = [];
    children.push(p([rt("Détail : ", { bold: true }), rt(sc.detail, { italic: true })]));
    children.push(p(""));
    const { calcul } = sc;
    if (calcul.audits) children.push(bul([rt(`${calcul.audits.nb} Audit(s) × ${calcul.audits.prix.toLocaleString("fr-FR")} € = ${(calcul.audits.nb * calcul.audits.prix).toLocaleString("fr-FR")} €`)]));
    if (calcul.offres2) children.push(bul([rt(`${calcul.offres2.nb} Offre(s) 2 × ${calcul.offres2.prix.toLocaleString("fr-FR")} € = ${(calcul.offres2.nb * calcul.offres2.prix).toLocaleString("fr-FR")} €`)]));
    if (calcul.offres3) children.push(bul([rt(`${calcul.offres3.nb} Offre(s) 3 × ${calcul.offres3.prix.toLocaleString("fr-FR")} € = ${(calcul.offres3.nb * calcul.offres3.prix).toLocaleString("fr-FR")} €`)]));
    if (calcul.mrr) children.push(bul([rt(`${calcul.mrr.nb} MRR × ${calcul.mrr.prix.toLocaleString("fr-FR")} € × ${calcul.mrr.mois} mois = ${(calcul.mrr.nb * calcul.mrr.prix * calcul.mrr.mois).toLocaleString("fr-FR")} €`)]));
    children.push(p(""));
    children.push(cal([rt("Total : ", { bold: true }), rt(`${ca.toLocaleString("fr-FR")} €`, { bold: true, color: "green" })], "green_background"));

    blocks.push(tog(`${sc.label}  —  ${ca.toLocaleString("fr-FR")} €`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(qot(
    [
      rt("Récapitulatif : ", { bold: true }),
      ...SCENARIOS_CA.map((sc, i) => rt(`${sc.label} = ${calcScenario(sc).toLocaleString("fr-FR")} €${i < SCENARIOS_CA.length - 1 ? "  ·  " : ""}`)),
    ],
    "gray_background"
  ));
  blocks.push(div());

  // ── CHECKLIST ──
  blocks.push(h1("✅ Checklist — Pricing Opérationnel"));
  blocks.push(p(""));

  const checklist = [
    "Grille tarifaire 3 niveaux sauvegardée (Notion + PDF)",
    "Règle interne : jamais annoncer un prix avant d'avoir qualifié le budget",
    "Template devis Offre 1 (PDF SASU) · Template devis Offre 2 (3 variantes) prêts",
    "Process paiement opérationnel (Stripe ou virement · acompte automatique)",
    "Formules de discours premium mémorisées et testées à voix haute",
    "Réponse à l'objection 'c'est cher' préparée (script écrit dans Notion)",
    "Grille de qualification client : 6 critères · 3 éliminatoires documentés",
    "Stratégie An1 confirmée : bas de fourchette · études de cas prioritaires",
  ];

  checklist.forEach((item) => {
    blocks.push({
      object: "block", type: "to_do",
      to_do: { rich_text: [rt(item)], checked: false },
    });
  });

  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🌟 Ce que ce Pricing dit de toi"));
  blocks.push(p(""));
  blocks.push(cal(
    "Un prix premium ne se justifie pas. Il se prouve. Chaque mission livrée avec excellence est la meilleure justification du prochain prix.",
    "purple_background"
  ));
  blocks.push(p(""));

  const synthese = SCENARIOS_CA.map((sc) => `${sc.label.split(" ")[0] + " " + sc.label.split(" ")[1]} = ${calcScenario(sc).toLocaleString("fr-FR")} €`).join("  ·  ");
  blocks.push(qot(synthese, "green_background"));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la page Pricing Premium Calibré B2B...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "💰" },
    properties: {
      title: { title: [{ text: { content: "💰 Pricing Premium Calibré B2B — Architecte Système WordPress" } }] },
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
  console.log("📊  Scénarios CA :");
  SCENARIOS_CA.forEach((sc) => {
    console.log(`   ${sc.label.padEnd(26)} : ${calcScenario(sc).toLocaleString("fr-FR").padStart(9)} €`);
  });
  console.log("");
  console.log(`💡  ROI exemple : Formateur ${roi_exemple.missions_an} missions × ${roi_exemple.ca_par_mission.toLocaleString("fr-FR")} € = ${roi_exemple.ca_total.toLocaleString("fr-FR")} €`);
  console.log(`   Investissement : ${roi_exemple.investissement_offre2.toLocaleString("fr-FR")} € · Ratio : × ${roi_exemple.ratio.toFixed(1)}`);
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
