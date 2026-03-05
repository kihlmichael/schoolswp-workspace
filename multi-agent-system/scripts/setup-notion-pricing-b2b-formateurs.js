#!/usr/bin/env node
"use strict";

/**
 * setup-notion-pricing-b2b-formateurs.js
 * Crée la page Notion : 💰 Pricing Premium — Formateurs B2B WordPress
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-pricing-b2b-formateurs.js
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
  pas: [
    "Un site WordPress",
    "Un LMS configuré",
    "Des heures de développement",
    "Une prestation technique",
  ],
  oui: [
    "La structuration d'un système WordPress rentable pour formation B2B",
    "Un levier direct sur le chiffre d'affaires du formateur",
    "Une architecture qui tient 3 ans sans refonte",
    "L'automatisation qui transforme le cycle long en revenu prévisible",
  ],
  axiome: "Tu factures la valeur business créée, pas le temps passé.",
};

const MARCHE_B2B = {
  ca_formateur: { mini: 3000, maxi: 15000, unite: "€ par mission entreprise" },
  contrats_an: { mini: 5, maxi: 20, unite: "contrats / an" },
  leviers_impact: [
    { levier: "Conversion améliorée", impact: "+15 à +40% sur le taux de transformation devis → mission" },
    { levier: "Onboarding automatisé", impact: "−2 à −5h d'administration par nouveau client" },
    { levier: "Crédibilité corporate", impact: "Accès à des contrats 2× plus élevés (RH grands groupes)" },
    { levier: "Automatisation renouvellement", impact: "+30 à +60% de taux de renouvellement contractuel" },
    { levier: "Reporting QUALIOPI", impact: "−3 à −8h par session de formation sur la documentation" },
  ],
  conclusion: "Si ton système améliore 1 seul de ces leviers, l'impact CA du client dépasse largement ton honoraire. C'est pour ça que ton pricing est premium.",
};

const NIVEAUX = [
  {
    rang: "🥉",
    num: "1",
    nom: "Audit Architecture B2B",
    prix_mini: 1200,
    prix_maxi: 1800,
    prix_affiche: "1 200 € – 1 800 €",
    emoji_statut: "🟢",
    role: "Entrée premium. Filtre. Génère du cash court terme.",
    engagement: "1 à 2 semaines",
    livrable: "Document stratégique 10–20 pages + Roadmap personnalisée",
    inclus: [
      "Analyse LMS (structure, accès, scalabilité entreprise)",
      "Analyse CRM (segmentation, automatisations existantes, lacunes)",
      "Analyse tunnel B2B (de la prospection à la facturation)",
      "Analyse parcours apprenant (onboarding → complétion → renouvellement)",
      "Cartographie des points de friction business",
      "Roadmap d'architecture personnalisée avec priorisation",
    ],
    objectifs: [
      "Filtrer les clients sérieux des curieux",
      "Générer un premier cash rapide (< 15 jours)",
      "Identifier le périmètre réel avant de vendre le niveau 2 ou 3",
      "Poser un diagnostic que le client ne peut pas obtenir ailleurs",
    ],
    pitch_client: "Avant d'implémenter quoi que ce soit, je dois comprendre votre réalité. L'audit me prend 2 semaines — et vous donne une vision que vous n'aurez pas avec un développeur classique.",
    upsell_naturel: "Niveau 2 ou 3 selon maturité révélée par l'audit",
  },
  {
    rang: "🥈",
    num: "2",
    nom: "Implémentation Core System",
    prix_mini: 4500,
    prix_maxi: 7000,
    prix_affiche: "4 500 € – 7 000 €",
    emoji_statut: "🔵",
    role: "Cœur de business. Le plus vendu. Le meilleur ratio valeur/temps.",
    engagement: "6 à 10 semaines",
    livrable: "Système WordPress B2B opérationnel, documenté, testé",
    inclus: [
      "Architecture LMS B2B (comptes entreprise, cohortes, accès groupés)",
      "CRM structuré (segmentation décideur/apprenant, pipelines)",
      "Automatisation onboarding (accès, welcome sequence, kick-off auto)",
      "Tunnel B2B simple (page offre corporate + formulaire qualifiant)",
      "Configuration technique complète (plugins, permissions, sécurité)",
      "Session de formation équipe (1 × 2h)",
      "Documentation de prise en main",
    ],
    objectifs: [
      "Livrer un système qui tourne sans intervention quotidienne",
      "Rendre le formateur crédible auprès des RH grands groupes",
      "Réduire le temps d'administration de 60 à 80%",
      "Poser les bases du renouvellement automatisé",
    ],
    pitch_client: "En 10 semaines, vous avez un système WordPress qui onboarde vos clients entreprise seul, segmente vos prospects et vous donne une page offre corporate crédible.",
    upsell_naturel: "Optimisation continue 800–1 500 €/mois après 3 mois",
  },
  {
    rang: "🥇",
    num: "3",
    nom: "Full B2B WordPress System™",
    prix_mini: 8000,
    prix_maxi: 15000,
    prix_affiche: "8 000 € – 15 000 €",
    emoji_statut: "🟣",
    role: "Transformation complète. Clients ambitieux. CA > 100k€/an.",
    engagement: "10 à 14 semaines + 3 mois support",
    livrable: "Tout le Niveau 2 + optimisation conversion + reporting + 3 mois support stratégique",
    inclus: [
      "Tout le Niveau 2 (Core System complet)",
      "Optimisation conversion tunnel B2B (A/B, lead scoring affiné)",
      "Reporting business (KPI LTV, taux renouvellement, dashboard dirigeant)",
      "Segmentation avancée (décideur RH / opérationnel / apprenant / sponsor)",
      "Séquence renouvellement complète (J-90, J-60, J-30, J-7)",
      "Formation équipe étendue (2 à 3 sessions selon taille)",
      "Documentation personnalisée complète (pas un template générique)",
      "Support stratégique 3 mois post-déploiement (sessions mensuelles)",
    ],
    objectifs: [
      "Transformer le formateur en acteur B2B scalable",
      "Automatiser le renouvellement contractuel",
      "Piloter l'activité avec des données, pas des intuitions",
      "Poser les bases d'un MRR agency récurrent",
    ],
    pitch_client: "En 14 semaines, vous avez un système complet — LMS, CRM, tunnel, reporting. Et 3 mois d'accompagnement pour l'optimiser sur données réelles.",
    upsell_naturel: "Accompagnement mensuel 1 200–2 000 €/mois, prolongement naturel",
  },
];

const UPSELL = {
  nom: "Optimisation Continue",
  prix: "800 – 1 500 €  /  mois",
  prix_mini: 800,
  prix_maxi: 1500,
  declencheur: "À proposer 3 à 6 mois après déploiement Niveau 2 ou 3",
  inclus: [
    "Ajustements mensuels (évolutions LMS, CRM, tunnel)",
    "Optimisation conversion sur données réelles",
    "Améliorations automatisations (nouvelles séquences, tests)",
    "Suivi KPI mensuel (session 1h avec le formateur)",
    "Conseil prioritaire (réponse sous 24h ouvrées)",
    "Veille WordPress B2B (plugins, évolutions QUALIOPI)",
  ],
  valeur_pitch: "Votre système est en place. Maintenant, on l'optimise sur vos vraies données. C'est là que le ROI s'accélère.",
  objectif_mrr: "3 à 5 clients en accompagnement = 2 400 – 7 500 €/mois de MRR",
};

const PROJECTIONS = [
  {
    label: "Plancher (démarrage)",
    scenario: "1 mission Niveau 2 / mois",
    ca_mensuel: 1 * 5500,
    ca_annuel: 1 * 5500 * 12,
    note: "Déjà dans une logique premium stable. Suffisant pour valider l'offre.",
  },
  {
    label: "Modéré (objectif M6)",
    scenario: "2 missions Niveau 2 / mois",
    ca_mensuel: 2 * 5500,
    ca_annuel: 2 * 5500 * 12,
    note: "Cible à 6 mois. Correspond à 1 Audit (filtre) + 1 Core System par mois.",
  },
  {
    label: "Stabilisé (objectif M12)",
    scenario: "1 Niveau 2 + 1 Niveau 3 / trimestre + 3 MRR",
    ca_mensuel: Math.round((7000 + 12000 + 3 * 1200) / 3),
    ca_annuel: Math.round(((7000 + 12000 + 3 * 1200) / 3) * 12),
    note: "Mix missions ponctuelles + MRR accompagnement. Modèle hybride stable.",
  },
  {
    label: "Dominance (objectif M18-24)",
    scenario: "2 Niveau 3 / trimestre + 5 MRR",
    ca_mensuel: Math.round((2 * 12000 + 5 * 1200) / 3),
    ca_annuel: Math.round(((2 * 12000 + 5 * 1200) / 3) * 12),
    note: "Référence B2B. Sélection clients. CA prévisible.",
  },
];

const PSYCHOLOGIE_PRICING = {
  piege: "Ne jamais présenter 3 offres en mode Low / Medium / High",
  raison: "Le client compare les prix. Il choisit le middle par défaut. Tu perds la conversation valeur.",
  bonne_approche: "Orienter selon la maturité révélée par l'Audit",
  scripts: [
    {
      situation: "Client avec LMS basique, 2-3 entreprises",
      recommandation: "Niveau 2 — Core System",
      phrase: "Vu votre maturité actuelle, la prochaine étape est de structurer le système avant d'optimiser. Le Niveau 2 est exactement ce qu'il vous faut.",
    },
    {
      situation: "Client structuré, CA > 100k€, veut scaler",
      recommandation: "Niveau 3 — Full System",
      phrase: "Vous avez déjà des bases solides. Ce que vous avez besoin, c'est d'un système complet avec le reporting pour piloter. Le Niveau 3 est fait pour vous.",
    },
    {
      situation: "Client hésitant, budget non confirmé",
      recommandation: "Niveau 1 — Audit en entrée",
      phrase: "Avant de décider quoi que ce soit, faisons l'Audit. Ça prend 2 semaines, c'est 1 200 €, et ça nous dira exactement quoi implémenter — et combien ça coûte.",
    },
  ],
};

const POSITIONNEMENT_VERBAL = [
  {
    a_ne_pas_dire: "Je propose une création LMS",
    a_dire: "J'optimise et structure votre système WordPress pour vendre vos formations B2B avec clarté et automatisation.",
    pourquoi: "LMS = technique → prix bas. Système = valeur business → prix premium.",
  },
  {
    a_ne_pas_dire: "J'installe WordPress et configure FluentLMS",
    a_dire: "Je conçois l'architecture WordPress qui permet à vos formations d'être achetées par des entreprises — et renouvelées.",
    pourquoi: "Installer = prestataire. Concevoir = expert.",
  },
  {
    a_ne_pas_dire: "Mon tarif journalier est de 600 €",
    a_dire: "Ma mission démarre à 1 200 € pour l'Audit et va jusqu'à 15 000 € pour une transformation complète, selon votre maturité et vos objectifs.",
    pourquoi: "Tarif journalier = comparaison avec des freelances. Fourchette mission = conversation valeur.",
  },
  {
    a_ne_pas_dire: "Je vais régler votre problème technique",
    a_dire: "Je structure le système qui transforme vos ventes B2B en flux prévisible.",
    pourquoi: "Technique = coût. Système = investissement. Un investissement, ça se justifie différemment.",
  },
];

const REGLES_NON_NEGOCIABLES = [
  "Toujours commencer par l'Audit (Niveau 1) — jamais démarrer une mission sans diagnostic",
  "Ne jamais baisser le prix — ajuster le périmètre si budget insuffisant",
  "Qualifier le budget dès le premier appel (avant de proposer quoi que ce soit)",
  "Ne pas accepter les missions < 1 200 € (sous ce seuil, pas rentable, pas positionné)",
  "Exiger un acompte 40% à la signature, 40% mi-mission, 20% à la livraison",
  "Refuser les demandes 'juste un LMS rapide' — ce n'est pas ta cible",
];

// ─── CALC ─────────────────────────────────────────────────────────────────────

const prix_moyen_n2 = Math.round((NIVEAUX[1].prix_mini + NIVEAUX[1].prix_maxi) / 2);
const prix_moyen_n3 = Math.round((NIVEAUX[2].prix_mini + NIVEAUX[2].prix_maxi) / 2);

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
const qot = (text, color = "gray_background") => ({ object: "block", type: "quote", quote: { rich_text: [rt(text)], color } });
const cal = (text, color = "blue_background") => ({
  object: "block",
  type: "callout",
  callout: {
    rich_text: Array.isArray(text) ? text : [rt(text)],
    icon: { type: "emoji", emoji: "💡" },
    color,
  },
});
const tog = (text, children = [], color = "default") => ({
  object: "block",
  type: "toggle",
  toggle: { rich_text: [rt(text, { bold: true })], color, children },
});

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("💰 Pricing Premium · Formateurs B2B WordPress · schoolsWP · Document interne", "yellow_background"));
  blocks.push(p([rt("Pricing basé sur la valeur business créée — pas sur le temps passé.", { italic: true })]));
  blocks.push(div());

  // ── PRINCIPE FONDAMENTAL ──
  blocks.push(h1("🧠 Principe Fondamental"));
  blocks.push(cal([rt(PRINCIPE.axiome, { bold: true })], "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Tu ne factures PAS :"));
  PRINCIPE.pas.forEach((item) => blocks.push(bul([rt("✗  " + item, { color: "red" })], "red_background")));
  blocks.push(p(""));

  blocks.push(h2("Tu factures :"));
  PRINCIPE.oui.forEach((item) => blocks.push(bul([rt("✓  " + item, { bold: true, color: "green" })], "green_background")));
  blocks.push(div());

  // ── RÉFÉRENCE MARCHÉ ──
  blocks.push(h1("📊 Référence Marché B2B — Pourquoi le Pricing Premium est Justifié"));
  blocks.push(p(""));

  blocks.push(p([
    rt("Un formateur B2B vend ", {}),
    rt(`${MARCHE_B2B.ca_formateur.mini.toLocaleString("fr-FR")} € – ${MARCHE_B2B.ca_formateur.maxi.toLocaleString("fr-FR")} €`, { bold: true, color: "green" }),
    rt(" par mission entreprise, avec "),
    rt(`${MARCHE_B2B.contrats_an.mini} à ${MARCHE_B2B.contrats_an.maxi} contrats / an`, { bold: true }),
    rt("."),
  ]));
  blocks.push(p(""));

  blocks.push(h2("Leviers d'impact de ton système sur son CA :"));
  MARCHE_B2B.leviers_impact.forEach((l) => {
    blocks.push(bul([
      rt(`${l.levier} : `, { bold: true }),
      rt(l.impact, { color: "green" }),
    ]));
  });

  blocks.push(p(""));
  blocks.push(qot(MARCHE_B2B.conclusion, "blue_background"));
  blocks.push(div());

  // ── NIVEAUX DE PRICING ──
  blocks.push(h1("🏗 Structure Pricing — 3 Niveaux"));
  blocks.push(p([rt("Toujours présenter selon la maturité du client — jamais en mode Low/Medium/High.", { italic: true, bold: true })]));
  blocks.push(p(""));

  for (const niv of NIVEAUX) {
    const header = `${niv.rang} Niveau ${niv.num} — ${niv.nom}  ·  ${niv.prix_affiche}`;
    const children = [];

    children.push(cal([rt(niv.role, { bold: true })], "gray_background"));
    children.push(p(""));

    children.push(p([rt("💶 Prix : ", { bold: true }), rt(niv.prix_affiche, { bold: true, color: "green" })]));
    children.push(p([rt("⏱ Engagement : ", { bold: true }), rt(niv.engagement)]));
    children.push(p([rt("📄 Livrable : ", { bold: true }), rt(niv.livrable)]));
    children.push(p(""));

    children.push(h3("Inclut"));
    niv.inclus.forEach((item) => children.push(bul(item)));
    children.push(p(""));

    children.push(h3("Objectifs de cette offre"));
    niv.objectifs.forEach((item) => children.push(num(item)));
    children.push(p(""));

    children.push(h3("Pitch client"));
    children.push(qot(`"${niv.pitch_client}"`, "blue_background"));
    children.push(p(""));

    children.push(p([rt("→ Upsell naturel : ", { bold: true, color: "gray" }), rt(niv.upsell_naturel, { italic: true })]));

    blocks.push(tog(header, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── UPSELL MRR ──
  blocks.push(h1("🔁 Upsell Stratégique — MRR Récurrent"));
  blocks.push(p(""));

  blocks.push(cal([
    rt(UPSELL.nom + " : ", { bold: true }),
    rt(UPSELL.prix, { bold: true, color: "green" }),
  ], "purple_background"));

  blocks.push(p(""));
  blocks.push(p([rt("Déclencheur : ", { bold: true }), rt(UPSELL.declencheur, { italic: true })]));
  blocks.push(p(""));

  blocks.push(h2("Inclut"));
  UPSELL.inclus.forEach((item) => blocks.push(bul(item)));
  blocks.push(p(""));

  blocks.push(qot(`"${UPSELL.valeur_pitch}"`, "blue_background"));
  blocks.push(p(""));
  blocks.push(bul([rt(UPSELL.objectif_mrr, { bold: true, color: "green" })]));
  blocks.push(div());

  // ── PROJECTIONS ──
  blocks.push(h1("📈 Projections Réalistes"));
  blocks.push(p([rt(`Prix moyen Niveau 2 retenu : ${prix_moyen_n2.toLocaleString("fr-FR")} €  ·  Prix moyen Niveau 3 : ${prix_moyen_n3.toLocaleString("fr-FR")} €`, { italic: true })]));
  blocks.push(p(""));

  for (const proj of PROJECTIONS) {
    const children = [];
    children.push(p([rt("Scénario : ", { bold: true }), rt(proj.scenario)]));
    children.push(p([
      rt("CA mensuel : ", { bold: true }),
      rt(`${proj.ca_mensuel.toLocaleString("fr-FR")} €/mois`, { bold: true, color: "green" }),
      rt(`  →  ${proj.ca_annuel.toLocaleString("fr-FR")} €/an`, { color: "gray" }),
    ]));
    children.push(p([rt("💬 ", {}), rt(proj.note, { italic: true })]));

    blocks.push(tog(`${proj.label}  —  ${proj.ca_mensuel.toLocaleString("fr-FR")} €/mois`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(cal(
    `Même à 1 seul projet Niveau 2 / mois (${prix_moyen_n2.toLocaleString("fr-FR")} €), tu es dans une logique premium stable. C'est le plancher, pas l'objectif.`,
    "green_background"
  ));
  blocks.push(div());

  // ── PSYCHOLOGIE PRICING ──
  blocks.push(h1("🎯 Psychologie Pricing — La Clé qui Change Tout"));
  blocks.push(p(""));

  blocks.push(cal([rt("⚠️  " + PSYCHOLOGIE_PRICING.piege, { bold: true })], "red_background"));
  blocks.push(p([rt("Pourquoi : ", { bold: true }), rt(PSYCHOLOGIE_PRICING.raison)]));
  blocks.push(p(""));
  blocks.push(qot("→ " + PSYCHOLOGIE_PRICING.bonne_approche, "blue_background"));
  blocks.push(p(""));

  blocks.push(h2("Scripts d'orientation selon maturité"));
  blocks.push(p(""));

  for (const script of PSYCHOLOGIE_PRICING.scripts) {
    const children = [];
    children.push(p([rt("Situation : ", { bold: true }), rt(script.situation)]));
    children.push(p([rt("Recommandation : ", { bold: true }), rt(script.recommandation, { color: "green" })]));
    children.push(qot(`"${script.phrase}"`, "blue_background"));

    blocks.push(tog(`→ ${script.situation.substring(0, 55)}...`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── POSITIONNEMENT VERBAL ──
  blocks.push(h1("🔥 Positionnement Verbal — Ce qui Change Tout"));
  blocks.push(p([rt("Les mots que tu utilises définissent le prix que tu peux demander.", { italic: true, bold: true })]));
  blocks.push(p(""));

  for (const pv of POSITIONNEMENT_VERBAL) {
    const children = [];
    children.push(bul([rt("À ne JAMAIS dire : ", { bold: true, color: "red" }), rt(`"${pv.a_ne_pas_dire}"`, { italic: true })], "red_background"));
    children.push(bul([rt("À dire : ", { bold: true, color: "green" }), rt(`"${pv.a_dire}"`, { italic: true })], "green_background"));
    children.push(p([rt("Pourquoi : ", { bold: true }), rt(pv.pourquoi, { italic: true, color: "gray" })]));

    blocks.push(tog(`⚖️  "${pv.a_ne_pas_dire.substring(0, 45)}..."`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── RÈGLES NON NÉGOCIABLES ──
  blocks.push(h1("🛑 Règles Non Négociables"));
  blocks.push(p([rt("Ces règles protègent ton positionnement. En enfreindre une = risque de dévaluation.", { italic: true })]));
  blocks.push(p(""));
  REGLES_NON_NEGOCIABLES.forEach((r) => blocks.push(bul([rt("⛔  " + r, { bold: true })], "red_background")));
  blocks.push(div());

  // ── TABLEAU RÉCAPITULATIF ──
  blocks.push(h1("📋 Tableau Récapitulatif"));
  blocks.push(p(""));

  // Simulation d'un tableau avec des blocs structurés
  const rows = [
    ["Niveau", "Nom", "Prix", "Durée", "Profil cible"],
    ["🥉 N1", "Audit Architecture", "1 200 – 1 800 €", "1-2 sem.", "Tout client (entrée)"],
    ["🥈 N2", "Core System", "4 500 – 7 000 €", "6-10 sem.", "3-10 entreprises clientes"],
    ["🥇 N3", "Full System™", "8 000 – 15 000 €", "10-14 sem.", "CA > 100k€, veut scaler"],
    ["🔁 MRR", "Optimisation Continue", "800 – 1 500 €/mois", "Récurrent", "Post N2 ou N3"],
  ];

  rows.forEach((row, i) => {
    const isHeader = i === 0;
    blocks.push(bul(
      [rt(row.join("  ·  "), { bold: isHeader, code: isHeader })],
      isHeader ? "gray_background" : "default"
    ));
  });

  blocks.push(p(""));

  // Projection synthèse
  blocks.push(h2("Synthèse Projections CA"));
  blocks.push(p(""));
  PROJECTIONS.forEach((proj) => {
    blocks.push(bul([
      rt(`${proj.label} : `, { bold: true }),
      rt(`${proj.ca_mensuel.toLocaleString("fr-FR")} €/mois`, { bold: true, color: "green" }),
      rt(` · ${proj.ca_annuel.toLocaleString("fr-FR")} €/an`, { color: "gray" }),
    ]));
  });

  blocks.push(div());

  // ── CHECKLIST IMPLÉMENTATION ──
  blocks.push(h1("✅ Checklist — Avant de Publier ce Pricing"));
  blocks.push(p(""));

  const checklist = [
    "Page offre schoolswp.com/b2b mise à jour avec les 3 niveaux",
    "Formulaire de qualification B2B actif (questions budget + contexte + urgence)",
    "Template devis Niveau 1 (Audit) finalisé et prêt à envoyer",
    "Template devis Niveau 2 et 3 structurés",
    "Mentions légales SASU à jour (devis, CGV, acomptes)",
    "Pitch verbal testé à voix haute sur les 4 formulations",
    "Processus de restitution Audit documenté",
    "Offre d'upsell MRR présentée systématiquement à J+30 post-livraison",
    "1 étude de cas B2B publiée (même simplifiée) sur le site",
    "Tagline LinkedIn mise à jour avec positionnement B2B WordPress",
  ];

  checklist.forEach((item) => {
    blocks.push({
      object: "block",
      type: "to_do",
      to_do: { rich_text: [rt(item)], checked: false },
    });
  });

  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🏆 Ce que ce Pricing dit de toi"));
  blocks.push(p(""));
  blocks.push(cal(
    "Un expert qu'on sollicite pour la valeur qu'il crée — pas un prestataire qu'on compare sur Malt.",
    "purple_background"
  ));
  blocks.push(p(""));
  blocks.push(qot(
    "Ce pricing n'est pas une grille tarifaire. C'est une déclaration de positionnement. Chaque client qui accepte ce pricing te positionne davantage comme référence B2B. Chaque client que tu refuses de rabaisser te protège.",
    "green_background"
  ));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la page Pricing Premium Formateurs B2B...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "💰" },
    properties: {
      title: { title: [{ text: { content: "💰 Pricing Premium — Formateurs B2B WordPress" } }] },
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
    console.log(`   ↳ Batch ${Math.ceil(i / CHUNK) + 1} envoyé (${Math.min(i + CHUNK, rest.length + CHUNK) - CHUNK}/${rest.length})`);
  }

  console.log("");
  console.log("✅  Page complète créée avec succès !");
  console.log(`🔗  https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📊  Synthèse projections :");
  PROJECTIONS.forEach((p) =>
    console.log(`   ${p.label.padEnd(28)} : ${p.ca_mensuel.toLocaleString("fr-FR").padStart(7)} €/mois  ·  ${p.ca_annuel.toLocaleString("fr-FR").padStart(8)} €/an`)
  );
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
