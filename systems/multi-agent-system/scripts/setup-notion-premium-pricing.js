#!/usr/bin/env node
/**
 * setup-notion-premium-pricing.js
 * Crée la page "💎 Pricing Premium — Architecte Systèmes WordPress" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-premium-pricing.js
 */

"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ---------------------------------------------------------------------------
// API helpers
// ---------------------------------------------------------------------------

async function notionRequest(method, path, body) {
  const res = await fetch(`https://api.notion.com/v1${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Content-Type": "application/json",
      "Notion-Version": "2022-06-28",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Notion API ${res.status} — ${err}`);
  }
  return res.json();
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------------------
// Block builders
// ---------------------------------------------------------------------------

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
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
const p = (...parts) => ({
  object: "block", type: "paragraph",
  paragraph: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const bul = (...parts) => ({
  object: "block", type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const num = (text) => ({
  object: "block", type: "numbered_list_item",
  numbered_list_item: { rich_text: [rt(text)] },
});
const tod = (text, checked = false) => ({
  object: "block", type: "to_do",
  to_do: { rich_text: [rt(text)], checked },
});
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (text, emoji = "💡", color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji }, color },
});
const qot = (text) => ({
  object: "block", type: "quote",
  quote: { rich_text: [rt(text)] },
});
const tog = (title, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(title, { bold: true })], children },
});

// ---------------------------------------------------------------------------
// Données
// ---------------------------------------------------------------------------

const POSITIONNEMENT = {
  pas: [
    "Freelance low-cost",
    "Créateur de site vitrine",
    "Dépanneur WordPress à la demande",
    "Développeur qui facture à l'heure",
    "Agence généraliste qui 'fait tout'",
  ],
  oui: [
    "Architecte de systèmes WordPress business",
    "Expert qui structure des écosystèmes WordPress rentables",
    "Partenaire technique et stratégique sur le long terme",
    "Spécialiste de l'automatisation et de la performance WordPress",
    "Référence schoolsWP — le seul qui combine SEO, CRM, automatisation et performance sur un seul stack",
  ],
  anti_slogans: [
    { mauvais: "Je crée votre site WordPress.", bon: "Je structure votre écosystème WordPress pour qu'il soutienne réellement votre activité et automatise vos processus." },
    { mauvais: "Je fais de la refonte WordPress.", bon: "Je transforme votre WordPress en système qui génère des leads et des clients sans intervention manuelle quotidienne." },
    { mauvais: "Je m'occupe de votre WordPress.", bon: "Je construis l'infrastructure WordPress qui fait travailler votre expertise pour vous — même quand vous n'êtes pas là." },
  ],
};

const PRINCIPE_FACTURATION = {
  pas: [
    "10 pages créées",
    "15 plugins installés et configurés",
    "20 heures de travail",
    "1 livrable technique",
  ],
  oui: [
    "La clarté là où il y avait de la confusion",
    "Un système automatisé là où il y avait des tâches manuelles",
    "Des leads qualifiés là où il y avait du trafic non converti",
    "Une infrastructure WordPress alignée avec les objectifs business",
  ],
  formule: "Valeur délivrée = (Gain de revenus potentiel + Temps libéré + Réduction du risque) ÷ Prix de la mission",
};

const OFFRES = [
  {
    num: "1",
    emoji: "🟢",
    nom: "Audit Stratégique WordPress",
    objectif: "Diagnostic exhaustif + roadmap d'actions priorisées par ROI.",
    pitch: "Avant d'investir dans une refonte ou une restructuration, tu sais exactement ce qui fonctionne, ce qui fuit, et dans quel ordre agir.",
    duree: "3 à 5 jours ouvrés",
    format: "Rapport PDF + session de restitution 90 min + plan d'action partagé",
    inclus: [
      "Audit technique WordPress : plugins, stack, dette, dépendances, performances réelles",
      "Audit structure business : cohérence offre / audience / prix / pages de conversion",
      "Audit SEO : structure cluster, maillage, opportunités non exploitées",
      "Audit automatisation : CRM, séquences email, scénarios actifs ou manquants",
      "Audit performance : Core Web Vitals, mobile, TTFB, cache",
      "Plan d'action priorisé par impact ROI (Quick Wins, 30j, 90j, 6 mois)",
    ],
    prix_mini: 1200,
    prix_maxi: 1800,
    prix_affiche: "1 200 € – 1 800 €",
    pourquoi_ce_prix: "Accessible pour les profils sérieux avec une activité existante. Filtre naturel : un prospect qui hésite sur 1 500 € n'est pas prêt pour une mission à 5 000 €.",
    signal_acheteur: "CA existant > 30 000 €/an, site WordPress en production, problème identifié mais roadmap floue.",
    upsell_naturel: "70 % des audits débouchent sur une mission Architecture si le rapport est bien construit.",
    differenciateur: "Chaque audit utilise la méthode schoolsWP : 4 dimensions systémiques, jamais un audit technique isolé.",
    regles: [
      "Jamais moins de 1 200 € — en dessous, le client ne prend pas les recommandations au sérieux",
      "Proposer en premier, avant toute mission de production",
      "L'audit est facturable même si aucune mission ne suit",
    ],
  },
  {
    num: "2",
    emoji: "🔵",
    nom: "Architecture & Structuration Système",
    objectif: "Transformer le WordPress existant en système business opérationnel.",
    pitch: "Ton site WordPress fonctionne. Mais il ne travaille pas pour toi. En 4 à 8 semaines, on construit l'infrastructure qui convertit, automatise et soutient ta croissance.",
    duree: "4 à 8 semaines selon périmètre",
    format: "Mission complète avec points hebdomadaires + documentation livrée + formation client finale",
    inclus: [
      "Refactoring architecture WordPress (structure, navigation, hiérarchie de pages)",
      "Mise en place ou optimisation CRM natif (FluentCRM) + segmentation",
      "Construction tunnel simple : lead magnet → séquence email → page offre → checkout",
      "Optimisation performance : cache, images, CDN, Core Web Vitals",
      "Mise en place automatisations prioritaires (3 à 5 scénarios)",
      "Formation client : prise en main de son système, documentation complète",
      "Dashboard de suivi livré (Google Sheets + GA4 paramétré)",
    ],
    prix_mini: 3500,
    prix_maxi: 7000,
    prix_affiche: "3 500 € – 7 000 €",
    pourquoi_ce_prix: "Transformation complète, pas une prestation ponctuelle. Le client repart avec un actif durable. À 5 000 €, le ROI est visible dès le 3e mois pour un site qui convertit 2× mieux.",
    signal_acheteur: "A fait (ou veut faire) l'audit en amont. Activité existante qui génère du CA. Comprend que son WordPress est un investissement, pas un coût.",
    upsell_naturel: "Débouche naturellement sur l'Accompagnement Mensuel pour maintenir et optimiser le système.",
    differenciateur: "Méthode en 4 phases : Audit → Architecture → Implémentation → Formation. Pas un 'on verra au fur et à mesure'.",
    regles: [
      "Toujours proposer un audit en amont — même rapide et offert sur 30 min — avant de signer",
      "Inclure impérativement la formation client : un client autonome ne revient pas se plaindre",
      "Ne jamais aller sous 3 500 € même pour un périmètre réduit — proposer une version allégée avec périmètre clair",
    ],
  },
  {
    num: "3",
    emoji: "🟣",
    nom: "Accompagnement Stratégique Mensuel",
    objectif: "Partenaire technique et stratégique sur la durée — optimisation continue.",
    pitch: "Ton système est en place. Maintenant on l'optimise, on mesure, on ajuste. Et tu as un expert WordPress dans la poche pour chaque décision technique ou stratégique.",
    duree: "Engagement minimum 3 mois, puis mensuel reconductible",
    format: "1 session stratégique mensuelle (60 min) + accès async (Slack/email) + compte-rendu mensuel",
    inclus: [
      "Suivi mensuel des KPIs (conversions, email, SEO, performance)",
      "Optimisation continue : tests A/B landing pages, ajustements séquences email",
      "SEO stratégique : planification cluster, brief articles, revue maillage",
      "Automatisations avancées : nouveaux scénarios, optimisation existants",
      "Ajustements business : si le modèle évolue, le WordPress suit",
      "Réponse async sous 24h (jours ouvrés) pour les questions ponctuelles",
    ],
    prix_mini: 800,
    prix_maxi: 1500,
    prix_affiche: "800 € – 1 500 € / mois",
    pourquoi_ce_prix: "Revenue récurrent, prévisible, à fort impact par heure engagée. À 1 000 €/mois, 3 clients = 3 000 €/mois de MRR. Stable, pas de prospection constante.",
    signal_acheteur: "A déjà une mission Architecture ou Audit. Comprend la valeur du suivi. Pas en mode 'survie'.",
    upsell_naturel: "Peut inclure des modules supplémentaires facturés en extra (refonte page, nouveau tunnel, nouveau LMS).",
    differenciateur: "Pas du support technique. Du pilotage stratégique mensuel avec une expertise cross-stack (SEO + CRM + Auto + Perf).",
    regles: [
      "Engagement minimum 3 mois — pour que les actions produisent des résultats mesurables",
      "Maximum 4 à 5 clients simultanément pour maintenir la qualité",
      "Le prix mensuel ne baisse jamais — proposer un périmètre réduit plutôt qu'une réduction tarifaire",
    ],
  },
];

const VALEUR_PERCUE = [
  { gain: "Gain de temps", description: "Le client ne gère plus les problèmes techniques WordPress. Il se concentre sur son métier.", exemple: "2 à 4 heures/semaine récupérées sur la maintenance, les bugs, les mises à jour problématiques." },
  { gain: "Gain de clarté", description: "Il sait exactement comment son WordPress fonctionne, ce qui convertit, ce qui bloque.", exemple: "Un rapport d'audit = fin de la confusion. Il sait quoi faire en priorité, dans quel ordre, pourquoi." },
  { gain: "Gain de revenus", description: "Un site qui convertit 2× mieux avec le même trafic = CA doublé sans plus de pub.", exemple: "Passage de 1 % à 2,5 % de taux de conversion = +150 % de leads pour 0 € de budget supplémentaire." },
  { gain: "Réduction du risque", description: "Moins de dépendances fragiles, moins de bugs critiques, architecture documentée.", exemple: "Fin de la peur de 'toucher à quelque chose et tout casser'. Système testé, documenté, formé." },
  { gain: "Vision long terme", description: "Il comprend où va son WordPress dans 12, 24, 36 mois. Pas de refonte surprise tous les 2 ans.", exemple: "Roadmap claire : ce qui est fait, ce qui est prévu, ce qui sera ajouté quand l'activité évolue." },
];

const REGLES_PRICING = [
  {
    regle: "Jamais justifier le prix par les heures",
    explication: "Dire 'j'ai passé 40 heures' ne vend rien. Dire 'votre taux de conversion a augmenté de 180 %' vend tout.",
    à_dire: "Ce que vous payez, c'est la transformation — pas mon agenda.",
    à_ne_pas_dire: "Ça représente environ 35 heures de travail à mon TJM.",
  },
  {
    regle: "Toujours parler résultats et transformation",
    explication: "Le client achète un état futur désirable. Toujours ancrer la conversation dans ce résultat.",
    à_dire: "À l'issue de la mission, votre WordPress génère des leads qualifiés en automatique.",
    à_ne_pas_dire: "Je vais refactoriser l'architecture et mettre en place FluentCRM.",
  },
  {
    regle: "Avoir un process clair et le montrer",
    explication: "Un process visible réduit le risque perçu. Le client sait ce qui va se passer, dans quel ordre, avec quels livrables.",
    à_dire: "Voici les 4 phases de la mission avec les livrables attendus à chaque étape.",
    à_ne_pas_dire: "On va voir ensemble au fur et à mesure de ce dont vous avez besoin.",
  },
  {
    regle: "Afficher la méthode, pas les outils",
    explication: "Les outils changent. La méthode systémique est le vrai actif différenciant.",
    à_dire: "Mon approche : toujours commencer par comprendre vos objectifs business avant de toucher au code.",
    à_ne_pas_dire: "J'utilise Elementor, FluentCRM, FlyingPress et WP Rocket.",
  },
  {
    regle: "Avoir une offre phare — une seule",
    explication: "La clarté vend. Trop d'options = paralysie du choix. L'offre Architecture est l'offre phare. Le reste est entrée (Audit) ou continuité (Accompagnement).",
    à_dire: "Mon offre principale est l'Architecture Système. L'audit est le point de départ naturel.",
    à_ne_pas_dire: "J'ai 7 formules différentes selon votre budget et vos besoins.",
  },
];

// Projections financières
const calc = () => {
  // Scénario conservative An1
  const audit_an1 = 6 * 1500;      // 6 audits × 1 500 €
  const archi_an1 = 4 * 5000;      // 4 missions × 5 000 €
  const mrr_an1_fin = 3 * 1000;    // 3 clients MRR × 1 000 € en fin d'an1
  const mrr_an1_total = 1000 * 6;  // 6 mois de MRR en moyenne

  // Scénario cible An1
  const audit_an1_cible = 10 * 1800;
  const archi_an1_cible = 6 * 6500;
  const mrr_an1_cible = 4 * 1200 * 8; // 4 clients × 1 200 € × 8 mois moyens

  // An2
  const audit_an2 = 8 * 1600;
  const archi_an2 = 6 * 5500;
  const mrr_an2 = 5 * 1200 * 12;

  return {
    an1_mini: audit_an1 + archi_an1 + mrr_an1_total,
    an1_cible: audit_an1_cible + archi_an1_cible + mrr_an1_cible,
    an2_mini: audit_an2 + archi_an2 + mrr_an2,
    an1_mrr_fin: mrr_an1_fin,
    an2_mrr: 5 * 1200,
  };
};
const FIN = calc();

const QUALIFICATION_CLIENT = [
  { critere: "CA existant", seuil_mini: "> 30 000 €/an", éliminatoire: true, pourquoi: "Sous ce seuil, le ROI d'une mission premium est trop long à matérialiser. Le client ne peut pas absorber l'investissement." },
  { critere: "WordPress déjà en production", seuil_mini: "Site en ligne depuis > 6 mois", éliminatoire: true, pourquoi: "On optimise un système existant — on ne construit pas de zéro (hors périmètre de l'offre standard)." },
  { critere: "Budget clairement disponible", seuil_mini: "Pas d'hésitation sur le budget minimal", éliminatoire: true, pourquoi: "Un client qui négocie dès le premier call sur 200 € ne respectera pas les étapes du process." },
  { critere: "Problème identifié", seuil_mini: "Sait nommer son blocage principal", éliminatoire: false, pourquoi: "S'il n'a pas identifié son problème, l'audit est l'étape 1 — pas un signal d'exclusion." },
  { critere: "Horizon mission > 3 mois", seuil_mini: "Pense sur 6 à 12 mois", éliminatoire: false, pourquoi: "Les résultats d'un système WordPress prennent 2 à 3 mois à apparaître. Un client qui veut du résultat à 4 semaines sera insatisfait." },
  { critere: "Autonomie post-mission souhaitée", seuil_mini: "Veut comprendre, pas juste déléguer", éliminatoire: false, pourquoi: "Les meilleurs clients sont ceux qui apprennent. Ils deviennent ambassadeurs et recommandent." },
];

const OBJECTIONS = [
  {
    objection: "C'est cher pour refaire un site WordPress.",
    réponse: "On ne refait pas 'un site'. On restructure le système qui soutient votre activité. Si votre site actuel génère 5 leads qualifiés par mois et qu'après la mission il en génère 20, combien ça vaut pour vous ?",
    principe: "Ancrer dans le résultat, pas dans le livrable.",
  },
  {
    objection: "J'ai eu des devis à 1 500 € pour une refonte complète.",
    réponse: "Vous avez eu des devis pour créer des pages WordPress. Ce n'est pas ce que je fais. Je construis le système business derrière — CRM, automatisation, SEO, performance — pas juste les pages.",
    principe: "Repositionner la comparaison — ne jamais se battre sur le prix contre une offre différente.",
  },
  {
    objection: "Je ne sais pas si j'en ai vraiment besoin.",
    réponse: "C'est exactement ce que l'audit est fait pour clarifier. Avec 1 500 €, on regarde ensemble ce qui fonctionne, ce qui fuit, et si une mission complète se justifie — ou pas. Si la réponse est non, vous repartez avec une roadmap claire et actionnaire.",
    principe: "Rediriger vers l'audit — jamais forcer la mission principale sans diagnostic.",
  },
  {
    objection: "Je vais y réfléchir.",
    réponse: "Bien sûr. Pour vous aider à décider : qu'est-ce qui vous ferait dire que c'est le bon moment ? Qu'est-ce qui vous retient ?",
    principe: "Identifier le vrai blocage — budget, timing, confiance, priorité. Ne pas relancer à l'aveugle.",
  },
];

// ---------------------------------------------------------------------------
// Template
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Principe fondamental : tu ne factures pas des heures ou des pages. Tu factures une transformation business structurée.", "💎", "purple_background"));
  blocks.push(p(""));
  blocks.push(qot("\"Je structure votre écosystème WordPress pour qu'il soutienne réellement votre activité et automatise vos processus.\""));
  blocks.push(div());

  // Section 1 — Positionnement
  blocks.push(h1("🧠 Positionnement — Qui tu es (et qui tu n'es pas)"));
  blocks.push(p(""));
  blocks.push(h3("Ce que tu n'es PAS"));
  POSITIONNEMENT.pas.forEach((item) => bul(item));
  POSITIONNEMENT.pas.forEach((item) => blocks.push(bul(rt("✗ ", { color: "red" }), rt(item))));
  blocks.push(p(""));
  blocks.push(h3("Ce que tu ES"));
  POSITIONNEMENT.oui.forEach((item) => blocks.push(bul(rt("✓ ", { color: "green" }), rt(item))));
  blocks.push(p(""));

  // Anti-slogans en toggles
  blocks.push(h3("Reformulations — Avant / Après"));
  POSITIONNEMENT.anti_slogans.forEach((s, i) => {
    blocks.push(tog(`Formulation ${i + 1}`, [
      p(rt("❌ Ne pas dire : ", { bold: true, color: "red" }), rt(s.mauvais, { italic: true })),
      p(rt("✅ Dire : ", { bold: true, color: "green" }), rt(s.bon, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 2 — Principe facturation
  blocks.push(h1("💰 Principe Fondamental du Pricing"));
  blocks.push(p(""));
  blocks.push(h3("Ce que tu NE factures PAS"));
  PRINCIPE_FACTURATION.pas.forEach((item) => blocks.push(bul(rt("✗ ", { color: "red" }), rt(item))));
  blocks.push(p(""));
  blocks.push(h3("Ce que tu factures VRAIMENT"));
  PRINCIPE_FACTURATION.oui.forEach((item) => blocks.push(bul(rt("✓ ", { color: "green" }), rt(item))));
  blocks.push(p(""));
  blocks.push(cal(`Formule de valeur : ${PRINCIPE_FACTURATION.formule}`, "🧮", "yellow_background"));
  blocks.push(div());

  // Section 3 — Les 3 offres
  blocks.push(h1("🏗️ Structure des 3 Offres"));
  blocks.push(cal("Une entrée (Audit) → Une offre phare (Architecture) → Une continuité (Accompagnement). Pas de confusion, pas de choix paralysant.", "🎯", "orange_background"));
  blocks.push(p(""));

  OFFRES.forEach((offre) => {
    blocks.push(h2(`${offre.emoji} Offre ${offre.num} — ${offre.nom}`));
    blocks.push(p(rt("Objectif : ", { bold: true }), rt(offre.objectif)));
    blocks.push(qot(offre.pitch));
    blocks.push(p(""));
    blocks.push(p(rt("Durée : ", { bold: true }), rt(offre.duree)));
    blocks.push(p(rt("Format : ", { bold: true }), rt(offre.format)));
    blocks.push(p(""));

    // Inclus en toggle
    const inclusChildren = offre.inclus.map((item) => bul(item));
    blocks.push(tog(`📋 Inclus dans l'offre (${offre.inclus.length} éléments)`, inclusChildren));
    blocks.push(p(""));

    // Prix
    blocks.push(h3(`💰 Prix : ${offre.prix_affiche}`));
    blocks.push(p(rt("Pourquoi ce prix : ", { bold: true }), rt(offre.pourquoi_ce_prix)));
    blocks.push(p(""));

    // Détails en toggle
    blocks.push(tog("🔍 Détails stratégiques", [
      p(rt("Profil acheteur cible : ", { bold: true }), rt(offre.signal_acheteur)),
      p(rt("Upsell naturel : ", { bold: true }), rt(offre.upsell_naturel)),
      p(rt("Différenciateur : ", { bold: true }), rt(offre.differenciateur)),
      p(""),
      p(rt("Règles de cette offre :", { bold: true })),
      ...offre.regles.map((r) => bul(r)),
    ]));
    blocks.push(p(""));
  });

  blocks.push(div());

  // Section 4 — Valeur perçue
  blocks.push(h1("📈 Logique de Valeur Perçue"));
  blocks.push(p("Le client doit percevoir 5 gains distincts. Pas un seul. Cinq. Chaque gain réduit l'élasticité au prix."));
  blocks.push(p(""));

  VALEUR_PERCUE.forEach((item, i) => {
    blocks.push(tog(`${i + 1}. ${item.gain}`, [
      p(item.description),
      p(rt("Exemple concret : ", { bold: true }), rt(item.exemple, { italic: true })),
    ]));
  });
  blocks.push(div());

  // Section 5 — Règles pricing
  blocks.push(h1("📏 Les 5 Règles du Pricing Premium"));
  blocks.push(p(""));

  REGLES_PRICING.forEach((r, i) => {
    blocks.push(h3(`${i + 1}. ${r.regle}`));
    blocks.push(p(r.explication));
    blocks.push(bul(rt("✅ À dire : ", { bold: true, color: "green" }), rt(`"${r.à_dire}"`)));
    blocks.push(bul(rt("❌ À ne pas dire : ", { bold: true, color: "red" }), rt(`"${r.à_ne_pas_dire}"`)));
    blocks.push(p(""));
  });

  blocks.push(div());

  // Section 6 — Qualification client
  blocks.push(h1("🎯 Grille de Qualification Client"));
  blocks.push(cal("Mieux vaut refuser 3 mauvais clients que d'en accepter 1 qui va bloquer 3 mois de ton agenda et casser ta motivation.", "⚠️", "red_background"));
  blocks.push(p(""));

  QUALIFICATION_CLIENT.forEach((q, i) => {
    blocks.push(tog(
      `${q.éliminatoire ? "🔴 ÉLIMINATOIRE" : "🟡 Important"} — ${q.critere} : ${q.seuil_mini}`,
      [
        p(rt("Pourquoi : ", { bold: true }), rt(q.pourquoi)),
      ]
    ));
  });
  blocks.push(p(""));
  blocks.push(div());

  // Section 7 — Objections
  blocks.push(h1("💬 Réponses aux Objections Clés"));
  blocks.push(p(""));

  OBJECTIONS.forEach((o, i) => {
    blocks.push(tog(`Objection ${i + 1} — "${o.objection}"`, [
      p(rt("Réponse : ", { bold: true }), rt(o.réponse, { italic: true })),
      p(rt("Principe : ", { bold: true }), rt(o.principe)),
    ]));
  });
  blocks.push(div());

  // Section 8 — Projections
  blocks.push(h1("📊 Projections Financières"));
  blocks.push(p(""));
  blocks.push(cal("2 projets Architecture à 5 000 € + 3 clients MRR à 1 000 €/mois = 10 000 € + 3 000 € MRR. Sans surcharger ton temps.", "🔑", "green_background"));
  blocks.push(p(""));

  blocks.push(h3("An 1 — Démarrage SASU"));
  blocks.push(bul(rt("Scénario conservateur : ", { bold: true }), rt(`${FIN.an1_mini.toLocaleString("fr-FR")} € CA total`)));
  blocks.push(bul(rt("Scénario cible : ", { bold: true }), rt(`${FIN.an1_cible.toLocaleString("fr-FR")} € CA total`)));
  blocks.push(bul(rt("MRR en fin d'An 1 : ", { bold: true }), rt(`${FIN.an1_mrr_fin.toLocaleString("fr-FR")} €/mois (3 clients accompagnement)`)));
  blocks.push(p(""));

  blocks.push(h3("An 2 — Système stabilisé"));
  blocks.push(bul(rt("CA total mini : ", { bold: true }), rt(`${FIN.an2_mini.toLocaleString("fr-FR")} €`)));
  blocks.push(bul(rt("MRR An 2 : ", { bold: true }), rt(`${FIN.an2_mrr.toLocaleString("fr-FR")} €/mois (5 clients accompagnement)`)));
  blocks.push(p(""));

  blocks.push(tog("Voir le détail par offre", [
    p(rt("An 1 — Scénario conservateur :", { bold: true })),
    bul("6 audits × 1 500 € = 9 000 €"),
    bul("4 missions Architecture × 5 000 € = 20 000 €"),
    bul("3 clients accompagnement × 1 000 € × 6 mois moyens = 18 000 €"),
    bul("Affiliation + framework : estimé 3 000 à 5 000 €"),
    p(""),
    p(rt("An 1 — Scénario cible :", { bold: true })),
    bul("10 audits × 1 800 € = 18 000 €"),
    bul("6 missions Architecture × 6 500 € = 39 000 €"),
    bul("4 clients accompagnement × 1 200 € × 8 mois = 38 400 €"),
    p(""),
    cal("Objectif réaliste An 1 : 50 000 à 70 000 € CA. Sans recruter. Sans s'épuiser. En restant sur 1 stack maîtrisé.", "🎯", "green_background"),
  ]));
  blocks.push(p(""));

  // Section 9 — Checklist lancement pricing
  blocks.push(div());
  blocks.push(h1("✅ Checklist — Lancer le Pricing Premium"));
  blocks.push(p(""));

  blocks.push(h3("Positionnement (à faire avant tout)"));
  blocks.push(tod("Réécrire le pitch en 3 formats (10s / 45s / 120 mots) avec la nouvelle formulation"));
  blocks.push(tod("Mettre à jour le profil LinkedIn : supprimer 'freelance' et 'création de site'"));
  blocks.push(tod("Retravailler le tagline schoolsWP pour refléter le positionnement système"));
  blocks.push(tod("Préparer 3 études de cas anonymisées (avant/après avec métriques)"));

  blocks.push(p(""));
  blocks.push(h3("Offres et process"));
  blocks.push(tod("Créer le modèle de rapport d'audit (Notion ou PDF template)"));
  blocks.push(tod("Rédiger la page de vente de l'audit (landing page dédiée)"));
  blocks.push(tod("Créer le devis type pour l'offre Architecture (avec les 4 phases)"));
  blocks.push(tod("Rédiger le contrat de mission type (inclure clause de confidentialité)"));
  blocks.push(tod("Configurer le tunnel : formulaire demande → call → devis → signature → onboarding"));

  blocks.push(p(""));
  blocks.push(h3("Prospection et visibilité"));
  blocks.push(tod("Identifier 20 prospects qualifiés (CA > 30k, WordPress, activité en ligne)"));
  blocks.push(tod("Préparer le post LinkedIn de positionnement (annonce de l'offre)"));
  blocks.push(tod("Envoyer l'email de lancement à la liste schoolsWP"));
  blocks.push(tod("Programmer 3 posts LinkedIn sur la méthode (1 par semaine)"));
  blocks.push(tod("Ajouter le CTA 'Demander un audit' sur schoolsWP (sidebar + articles ciblés)"));

  blocks.push(p(""));
  blocks.push(div());

  // Footer
  blocks.push(cal("Tu passes de 'expert qui explique' à 'expert qui structure des systèmes'. Ce n'est pas juste un changement de prix — c'est un changement d'identité professionnelle.", "🏁", "green_background"));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'Pricing Premium — Architecte Systèmes WordPress'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "💎" },
    properties: {
      title: { title: [{ text: { content: "💎 Pricing Premium — Architecte Systèmes WordPress" } }] },
    },
    children: batch1,
  });

  const pageId = pageRes.id;
  console.log(`✅ Page créée : ${pageId}`);

  for (let i = 1; i < totalBatches; i++) {
    const start = i * CHUNK;
    const end = Math.min(start + CHUNK, totalBlocks);
    const batch = template.slice(start, end);
    console.log(`⏳ Batch ${i + 1}/${totalBatches} (blocs ${start + 1}–${end})...`);
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, { children: batch });
    console.log(`✅ Batch ${i + 1} ajouté.`);
  }

  console.log("");
  console.log("🎉 Page créée avec succès !");
  console.log(`🔗 https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📋 Récapitulatif :");
  console.log(`   • ${OFFRES.length} offres avec inclus + règles + signaux acheteur`);
  console.log(`   • ${VALEUR_PERCUE.length} dimensions de valeur perçue`);
  console.log(`   • ${REGLES_PRICING.length} règles de pricing avec formulations avant/après`);
  console.log(`   • ${QUALIFICATION_CLIENT.length} critères de qualification (${QUALIFICATION_CLIENT.filter(q => q.éliminatoire).length} éliminatoires)`);
  console.log(`   • ${OBJECTIONS.length} objections avec réponses et principes`);
  console.log(`   • Projections An1 (${FIN.an1_mini.toLocaleString("fr-FR")} – ${FIN.an1_cible.toLocaleString("fr-FR")} €)`);
  console.log(`   • Checklist lancement 15 points`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
