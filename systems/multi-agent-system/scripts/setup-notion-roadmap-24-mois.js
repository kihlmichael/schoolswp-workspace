#!/usr/bin/env node
/**
 * setup-notion-roadmap-24-mois.js
 * Crée la page "🗺️ Roadmap 24 Mois — schoolsWP Hybride" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-roadmap-24-mois.js
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

// Projections financières par phase (mini / cible)
const PHASES = [
  {
    num: 1,
    emoji: "🟢",
    label: "FONDATIONS",
    periode: "Mois 1–6",
    tagline: "Structurer l'écosystème et générer les premiers revenus solides.",
    enjeu: "Cette phase est celle où tout se construit sans que rien ne soit encore visible. C'est la plus difficile psychologiquement — et la plus déterminante stratégiquement.",
    objectif_principal: "Avoir à fin M6 une offre Agency qui tourne, un cluster SEO solide, et un premier pipeline de leads qualifiés.",
    actions: [
      { categorie: "Agency", items: [
        "Finaliser l'offre signature (Audit 1 200–1 800 € + Architecture 3 500–7 000 €)",
        "Créer la landing page Audit stratégique WordPress",
        "Produire 2 études de cas anonymisées (projets salariat ou beta clients)",
        "Configurer le CRM de prospection (FluentCRM ou Notion pipeline)",
        "Lancer la prospection : 20 contacts qualifiés identifiés et contactés",
      ]},
      { categorie: "schoolsWP — Contenu", items: [
        "Valider 1 cluster prioritaire (CRM WordPress ou LMS WordPress)",
        "Produire 10 à 15 articles décisionnels (brain-lite.bat pour chaque)",
        "Intégrer les CTA intelligents dans chaque article (→ audit, → framework)",
        "Mettre en place le lead magnet principal (checklist ou template)",
        "Configurer la séquence email bienvenue 5 emails",
      ]},
      { categorie: "Infrastructure", items: [
        "Mettre en place le Dashboard KPI (Google Sheets + GA4 paramétré)",
        "Configurer Notion SASU : pipe commercial + suivi missions + finances",
        "Ouvrir la SASU si ce n'est pas encore fait (ou finaliser le statut)",
        "Séparer les finances personnelles et SASU (compte dédié)",
      ]},
    ],
    finances: {
      affiliation: { mini: 500, cible: 1000 },
      agency: { mini: 2000, cible: 4000 },
      produit: { mini: 0, cible: 0 },
    },
    kpis: [
      "Nombre d'articles publiés : ≥ 10",
      "Trafic organique mensuel schoolsWP : +30 % vs M1",
      "Leads qualifiés entrants : ≥ 3/mois en fin M6",
      "Missions Agency signées : ≥ 1 (objectif minimum 1 audit + 1 architecture)",
      "MRR affiliation : ≥ 500 €/mois",
      "Épargne de sécurité constituée : ≥ 15 000 €",
    ],
    risques: [
      { risque: "Aucun client Agency au bout de 3 mois", mitigation: "Débriefer le pitch et l'offre. Revoir la prospection. Baisser le seuil → proposer un audit à 900 €." },
      { risque: "Contenu publié mais aucun trafic", mitigation: "Vérifier le ciblage des mots-clés. Retravailler les H1/H2. Ajouter maillage interne. Attendre — le SEO prend 3 à 6 mois." },
      { risque: "Découragement à M3 (le creux du milieu)", mitigation: "Prévoir ce creux à l'avance. Planifier un jalon de motivation M3 : compter les actifs construits, pas juste le CA." },
    ],
    jalon_go: "3 conditions pour passer en Phase 2 : (1) ≥ 2 missions Agency signées, (2) pipeline avec ≥ 3 prospects actifs, (3) ≥ 8 articles publiés sur le cluster prioritaire.",
  },
  {
    num: 2,
    emoji: "🔵",
    label: "STABILISATION",
    periode: "Mois 7–12",
    tagline: "Consolider les revenus, augmenter l'autorité, lancer le premier produit.",
    enjeu: "À ce stade tu as prouvé que le modèle fonctionne. L'enjeu est de le rendre reproductible sans que chaque vente nécessite un effort de prospection massif.",
    objectif_principal: "Atteindre 6 000 € de CA mensuel récurrent d'ici fin M12, avec au moins 2 clients Agency récurrents (accompagnement mensuel).",
    actions: [
      { categorie: "Agency", items: [
        "Convertir 2 clients Architecture en Accompagnement Mensuel (800–1 500 €/mois)",
        "Collecter 3 témoignages avec métriques (avant/après chiffrés)",
        "Produire 2 études de cas détaillées publiées sur schoolsWP",
        "Automatiser le funnel Audit : formulaire → call auto-planifié → devis → signature",
        "Tester une hausse de tarif sur le prochain devis Architecture (+500 €)",
      ]},
      { categorie: "schoolsWP — Contenu", items: [
        "Lancer le 2e cluster stratégique (LMS si CRM fait, ou inversement)",
        "Optimiser les 5 articles avec le plus de trafic (audit V2 via workflow W1)",
        "Mettre en place la stratégie AI Overviews (FAQ AIO sur les articles piliers)",
        "Lancer la newsletter mensuelle schoolsWP (format court, 300–400 mots)",
        "Atteindre 20 articles publiés minimum sur le cluster 1",
      ]},
      { categorie: "Premier Produit", items: [
        "Valider l'idée de produit auprès de la liste email (sondage 10 questions)",
        "Produire et lancer le framework 'WordPress Business System™' (mini-cours 2h30)",
        "Prix lancement : 97–147 € pour les 50 premiers",
        "Collecter 5 avis post-achat dans les 30 jours",
        "Intégrer le CTA produit dans les 10 articles à plus fort trafic",
      ]},
    ],
    finances: {
      affiliation: { mini: 1500, cible: 2000 },
      agency: { mini: 4000, cible: 6000 },
      produit: { mini: 500, cible: 1000 },
    },
    kpis: [
      "CA mensuel total : ≥ 6 000 €",
      "MRR Agency (accompagnements) : ≥ 2 000 €/mois",
      "Ventes framework cumulées : ≥ 30 unités",
      "Trafic organique schoolsWP : ≥ 2 000 sessions/mois",
      "Taux de conversion landing audit : ≥ 3 %",
      "NPS clients Agency : ≥ 8/10",
    ],
    risques: [
      { risque: "Produit qui ne se vend pas au lancement", mitigation: "Analyser les retours et reformuler le pitch. Ne pas baisser le prix — retravailler l'angle de valeur." },
      { risque: "Saturation du temps (Agency + contenu + produit)", mitigation: "Prioriser Agency (CA immédiat) → Contenu (actif long terme) → Produit (effort ponctuel). Réduire le rythme de publication si besoin." },
      { risque: "Dépendance à 1 ou 2 gros clients Agency", mitigation: "Diversifier : jamais plus de 40 % du CA Agency chez un seul client." },
    ],
    jalon_go: "3 conditions pour passer en Phase 3 : (1) MRR Agency ≥ 2 000 €, (2) framework lancé avec ≥ 20 ventes, (3) 2 clusters SEO actifs avec ≥ 30 articles combinés.",
  },
  {
    num: 3,
    emoji: "🟣",
    label: "EXPANSION",
    periode: "Mois 13–18",
    tagline: "Augmenter la marge et réduire la dépendance au temps.",
    enjeu: "Tu ne vends plus ton temps à l'heure. Tu vends un système, une méthode, une transformation. L'enjeu est d'augmenter le ticket moyen Agency et de faire monter le produit en gamme.",
    objectif_principal: "Atteindre 10 000 € de CA mensuel avec une répartition plus équilibrée — moins de dépendance à chaque mission individuelle.",
    actions: [
      { categorie: "Agency", items: [
        "Revoir les tarifs à la hausse : Audit → 1 500–2 000 €, Architecture → 5 000–8 000 €",
        "Viser 4 à 5 clients en Accompagnement Mensuel (MRR stable)",
        "Développer le discours de référence : cas client publié sur schoolsWP chaque trimestre",
        "Explorer la sous-traitance partielle (dev front, rédaction) pour libérer du temps stratégique",
        "Créer un document de process interne (onboarding client standardisé)",
      ]},
      { categorie: "schoolsWP — Contenu & Autorité", items: [
        "Lancer le 3e cluster de domination (Performance WordPress ou E-commerce WP)",
        "Optimiser pour AI Overviews : 15 articles avec FAQ AIO + JSON-LD",
        "Démarrer le recyclage contenu : articles → newsletter → LinkedIn → thread X",
        "Viser la position 1 sur 5 mots-clés décisionnels du cluster 1",
        "Atteindre 5 000 sessions/mois organiques",
      ]},
      { categorie: "Produit — Montée en gamme", items: [
        "Lancer la V2 du framework à 197–297 € (prix stable post-lancement)",
        "Développer le premier produit complémentaire (templates, checklist premium, ou module avancé)",
        "Créer un tunnel dédié produit : article → email → landing → checkout",
        "Tester une offre bundle : framework + 1h de call = 497 €",
        "Objectif : 30 à 50 ventes/mois en régime stable",
      ]},
    ],
    finances: {
      affiliation: { mini: 2000, cible: 3000 },
      agency: { mini: 6000, cible: 8000 },
      produit: { mini: 2000, cible: 4000 },
    },
    kpis: [
      "CA mensuel total : ≥ 10 000 €",
      "MRR Agency (accompagnements) : ≥ 4 000 €/mois",
      "Ventes produits/mois : ≥ 30 unités",
      "CA affiliation mensuel : ≥ 2 000 €",
      "Trafic organique : ≥ 5 000 sessions/mois",
      "Nombre de clusters SEO actifs : ≥ 3",
    ],
    risques: [
      { risque: "Résistance client à la hausse tarifaire", mitigation: "Les nouveaux clients ne connaissent pas les anciens tarifs. Appliquer la hausse sur les nouveaux devis uniquement." },
      { risque: "Produit ne décolle pas à 197 €", mitigation: "Analyser le funnel : est-ce le prix, la landing, le trafic, ou l'offre ? Tester un bonus limité dans le temps." },
      { risque: "Épuisement sur les 3 fronts simultanément", mitigation: "Phase 3 = déléguer ou ralentir sur 1 axe. Jamais tout en même temps. Prioriser par ROI immédiat." },
    ],
    jalon_go: "3 conditions pour passer en Phase 4 : (1) CA mensuel ≥ 10 000 € pendant 2 mois consécutifs, (2) ≥ 4 clients Accompagnement actifs, (3) produit avec ≥ 20 ventes/mois en régime stable.",
  },
  {
    num: 4,
    emoji: "🟡",
    label: "LEVIER",
    periode: "Mois 19–24",
    tagline: "Rééquilibrer vers la scalabilité — moins de temps, plus de marge.",
    enjeu: "À 18 mois, le piège est de stagner par confort. L'enjeu est de passer d'un modèle 'expert qui exécute' à 'système qui tourne'. Moins de missions directes, plus d'actifs récurrents.",
    objectif_principal: "Atteindre 12 000–18 000 € de CA mensuel avec une répartition 30/35/35 (Affiliation/Agency/Produit), moins dépendante de ton temps direct.",
    actions: [
      { categorie: "Agency — Scalabilité", items: [
        "Standardiser l'onboarding client (automatisé : accueil email + Notion partagé + accès calendrier)",
        "Explorer la sous-traitance sur les missions techniques (garder le stratégique)",
        "Augmenter le ticket Accompagnement Mensuel : 1 500 € minimum pour nouveaux clients",
        "Limiter à 5 missions simultanées maximum — qualité avant volume",
        "Si croissance forte : étudier la structure holding (SASU opérationnelle + holding)",
      ]},
      { categorie: "schoolsWP — Automatisation éditoriale", items: [
        "Mettre en place le workflow W3 (Content Factory) pour la production multi-format",
        "Automatiser le recyclage contenu : 1 article → 5 formats (newsletter, LinkedIn, thread, FAQ, YouTube)",
        "Optimiser le top 20 % des articles (les 10 articles qui génèrent 80 % du trafic)",
        "Démarrer l'optimisation LLM systématique sur tous les articles piliers",
        "Viser 10 000 sessions/mois organiques",
      ]},
      { categorie: "Produit — Gamme complète", items: [
        "Lancer le produit premium (formation complète 197–497 € ou programme accompagné 997 €)",
        "Créer l'upsell naturel : framework → session de démarrage → accompagnement mensuel léger",
        "Tester une offre annuelle ou un abonnement (accès ressources + updates + Q&A mensuel)",
        "Construire le catalogue : framework + templates avancés + checklist pro = bundle 497 €",
        "Objectif : 50 à 100 ventes/mois (toutes offres produit confondues)",
      ]},
    ],
    finances: {
      affiliation: { mini: 3000, cible: 4000 },
      agency: { mini: 5000, cible: 7000 },
      produit: { mini: 4000, cible: 6000 },
    },
    kpis: [
      "CA mensuel total : ≥ 12 000 €",
      "MRR total (Agency + Produit récurrents) : ≥ 7 000 €/mois",
      "Trafic organique : ≥ 10 000 sessions/mois",
      "Ratio CA produit / CA total : ≥ 30 %",
      "Nombre de missions Agency simultanées : ≤ 5",
      "Satisfaction client NPS : ≥ 8,5/10",
    ],
    risques: [
      { risque: "Difficultés à déléguer (peur de la qualité)", mitigation: "Documenter les process avant de déléguer. Commencer par des tâches répétitives et à faible risque." },
      { risque: "Complexité fiscale avec la croissance (holding, TVA, etc.)", mitigation: "Prendre un expert-comptable dédié dès M12. Ne pas attendre d'avoir un problème pour structurer." },
      { risque: "Perte de cohérence éditoriale avec l'automatisation", mitigation: "Rester rédacteur en chef même en délégant. Chaque article publié passe par une revue personnelle." },
    ],
    jalon_go: "Bilan 24 mois : (1) CA annuel ≥ 120 000 €, (2) MRR ≥ 7 000 €, (3) trafic ≥ 10 000 sessions/mois, (4) 3 clusters SEO en position dominante.",
  },
];

// Calculs de progression globale
const progression = PHASES.map((ph) => ({
  label: ph.label,
  periode: ph.periode,
  ca_mini: ph.finances.affiliation.mini + ph.finances.agency.mini + ph.finances.produit.mini,
  ca_cible: ph.finances.affiliation.cible + ph.finances.agency.cible + ph.finances.produit.cible,
  ca_annuel_mini: (ph.finances.affiliation.mini + ph.finances.agency.mini + ph.finances.produit.mini) * 6,
  ca_annuel_cible: (ph.finances.affiliation.cible + ph.finances.agency.cible + ph.finances.produit.cible) * 6,
}));

const REPARTITION_CIBLE = [
  { source: "Affiliation", part: "30 %", description: "Revenus passifs, faible effort, long terme. Programmes CRM, LMS, hébergement, SEO.", plafond: "Difficile de dépasser 4 000–5 000 €/mois sans audience massive." },
  { source: "Agency", part: "30–40 %", description: "CA solide, prévisible avec MRR. 3 à 5 clients en accompagnement = socle stable.", plafond: "Plafonner volontairement à 5 missions simultanées pour préserver la qualité et la marge." },
  { source: "Produit", part: "30–40 %", description: "Levier le plus scalable. 1 vente supplémentaire = 0 heure de travail en plus.", plafond: "Prend 12 à 18 mois à construire. Patience et régularité exigées." },
];

const SECURITE_REGLES = [
  { regle: "6 mois de trésorerie minimum", detail: "Calculé sur charges perso + charges SASU fixes. Jamais passer en dessous. Reconstituer dès que ça descend." },
  { regle: "Pas plus de 5 projets Agency simultanés", detail: "Au-delà, la qualité chute, les délais glissent, la satisfaction client baisse. Mieux vaut refuser et recommander." },
  { regle: "Positionnement premium assumé en permanence", detail: "Ne jamais baisser les prix sous pression. Proposer un périmètre réduit si nécessaire, pas une remise." },
  { regle: "Toujours 1 cluster en construction", detail: "Le SEO est un actif qui prend du temps. Ne jamais s'arrêter de produire — même 1 article/semaine suffit." },
  { regle: "Diversification : aucune source > 50 % du CA", detail: "Si l'Agency représente 80 % du CA, la perte d'un client fait mal. Viser 3 sources équilibrées." },
  { regle: "Revue financière mensuelle sans exception", detail: "CA, charges, marge nette, projection M+3. 30 minutes par mois. Décisions basées sur les chiffres réels." },
];

const FORCES_DISTINCTIVES = [
  { force: "Autorité SEO construite sur la durée", impact: "Tu ne paies jamais pour acquérir des leads. Chaque article est un commercial permanent." },
  { force: "Écosystème hybride (média + agency + produit)", impact: "3 sources de revenus = 3 filets de sécurité. La perte d'un client Agency ne te met pas en danger." },
  { force: "Stack WordPress ultra-spécialisé (SEO + CRM + Auto + Perf)", impact: "Tu n'es pas remplaçable par un généraliste. Ton profil ne se trouve pas sur Malt à 350 €/jour." },
  { force: "schoolsWP comme actif de crédibilité", impact: "Chaque article publié, chaque mise à jour, chaque étude de cas renforce la confiance avant même le premier contact." },
  { force: "Méthode systémique documentée", impact: "Tu peux déléguer, sous-traiter, former. Le système vaut plus que l'exécutant." },
];

// ---------------------------------------------------------------------------
// Template
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // En-tête
  blocks.push(cal("Vision 24 mois — Ambitieuse, chiffrée, cohérente avec ton profil. 4 phases, 3 sources de revenus, 1 système qui se renforce.", "🗺️", "purple_background"));
  blocks.push(p(""));
  blocks.push(qot("\"Tu construis en parallèle : autorité SEO, audience qualifiée, systèmes automatisés, offre premium. Peu de freelances pensent à ce niveau.\""));
  blocks.push(div());

  // Vue d'ensemble financière
  blocks.push(h1("📊 Vue d'Ensemble — Progression Financière"));
  blocks.push(p(""));
  blocks.push(tog("Voir la progression complète par phase", [
    ...progression.map((ph) =>
      p(
        rt(`${ph.periode} (${ph.label}) : `, { bold: true }),
        rt(`${ph.ca_mini.toLocaleString("fr-FR")} – ${ph.ca_cible.toLocaleString("fr-FR")} €/mois`),
        rt(` → ${ph.ca_annuel_mini.toLocaleString("fr-FR")} – ${ph.ca_annuel_cible.toLocaleString("fr-FR")} € sur la période`)
      )
    ),
    p(""),
    p(rt("CA cumulé 24 mois (conservateur) : ", { bold: true }),
      rt(`${progression.reduce((a, p) => a + p.ca_annuel_mini, 0).toLocaleString("fr-FR")} €`)),
    p(rt("CA cumulé 24 mois (cible) : ", { bold: true }),
      rt(`${progression.reduce((a, p) => a + p.ca_annuel_cible, 0).toLocaleString("fr-FR")} €`)),
  ]));
  blocks.push(p(""));

  // Répartition cible
  blocks.push(h3("🎯 Répartition cible à 24 mois"));
  REPARTITION_CIBLE.forEach((src) => {
    blocks.push(bul(rt(`${src.source} (${src.part}) : `, { bold: true }), rt(src.description)));
  });
  blocks.push(div());

  // Les 4 phases
  PHASES.forEach((phase) => {
    const totalMini = phase.finances.affiliation.mini + phase.finances.agency.mini + phase.finances.produit.mini;
    const totalCible = phase.finances.affiliation.cible + phase.finances.agency.cible + phase.finances.produit.cible;

    blocks.push(h1(`${phase.emoji} PHASE ${phase.num} — ${phase.label} (${phase.periode})`));
    blocks.push(cal(phase.tagline, phase.num === 1 ? "🌱" : phase.num === 2 ? "🔵" : phase.num === 3 ? "🚀" : "⚡", "default"));
    blocks.push(p(""));
    blocks.push(h3("Enjeu de la phase"));
    blocks.push(p(phase.enjeu));
    blocks.push(p(""));
    blocks.push(h3("Objectif principal"));
    blocks.push(qot(phase.objectif_principal));
    blocks.push(p(""));

    // Actions par catégorie
    blocks.push(h3("Actions clés"));
    phase.actions.forEach((cat) => {
      const catChildren = cat.items.map((item) => tod(item));
      blocks.push(tog(`📌 ${cat.categorie}`, catChildren));
    });
    blocks.push(p(""));

    // Objectifs financiers
    blocks.push(h3(`💰 Objectifs financiers — fin ${phase.periode.split("–")[1]}`));
    blocks.push(bul(
      rt("Affiliation : ", { bold: true }),
      rt(`${phase.finances.affiliation.mini.toLocaleString("fr-FR")} – ${phase.finances.affiliation.cible.toLocaleString("fr-FR")} €/mois`)
    ));
    blocks.push(bul(
      rt("Agency : ", { bold: true }),
      rt(`${phase.finances.agency.mini.toLocaleString("fr-FR")} – ${phase.finances.agency.cible.toLocaleString("fr-FR")} €/mois`)
    ));
    blocks.push(bul(
      rt("Produit : ", { bold: true }),
      rt(
        phase.finances.produit.cible === 0
          ? "0 € (pas encore lancé)"
          : `${phase.finances.produit.mini.toLocaleString("fr-FR")} – ${phase.finances.produit.cible.toLocaleString("fr-FR")} €/mois`
      )
    ));
    blocks.push(p(""));
    blocks.push(cal(
      `Total cible fin ${phase.periode.split("–")[1]} : ${totalMini.toLocaleString("fr-FR")} – ${totalCible.toLocaleString("fr-FR")} €/mois`,
      "💰",
      phase.num === 1 ? "yellow_background" : phase.num === 2 ? "blue_background" : phase.num === 3 ? "purple_background" : "green_background"
    ));
    blocks.push(p(""));

    // KPIs
    const kpiChildren = phase.kpis.map((kpi) => bul(kpi));
    blocks.push(tog(`📊 KPIs à suivre (${phase.kpis.length})`, kpiChildren));
    blocks.push(p(""));

    // Risques + jalon
    const risqueChildren = [
      ...phase.risques.flatMap((r) => [
        p(rt(`⚠️ ${r.risque}`, { bold: true })),
        p(rt("Mitigation : ", { italic: true }), rt(r.mitigation)),
        p(""),
      ]),
    ];
    blocks.push(tog(`⚠️ Risques identifiés (${phase.risques.length})`, risqueChildren));
    blocks.push(p(""));
    blocks.push(cal(`🚦 Jalon GO Phase ${phase.num + 1 > 4 ? "finale" : phase.num + 1} : ${phase.jalon_go}`, "🚦", "yellow_background"));
    blocks.push(div());
  });

  // Section — Sécurité stratégique
  blocks.push(h1("🔐 Règles de Sécurité Stratégique"));
  blocks.push(p("À appliquer à chaque phase, sans exception. Ce sont les garde-fous qui évitent de tout perdre sur un mauvais mois."));
  blocks.push(p(""));
  SECURITE_REGLES.forEach((r, i) => {
    blocks.push(h3(`${i + 1}. ${r.regle}`));
    blocks.push(p(r.detail));
    blocks.push(p(""));
  });
  blocks.push(div());

  // Section — Forces distinctives
  blocks.push(h1("🎯 Tes Forces Distinctives — Pourquoi Ce Modèle Fonctionne"));
  blocks.push(cal("Peu de freelances pensent à ce niveau. C'est exactement ce qui te différencie.", "⚡", "green_background"));
  blocks.push(p(""));
  FORCES_DISTINCTIVES.forEach((f) => {
    blocks.push(tog(f.force, [
      p(rt("Impact : ", { bold: true }), rt(f.impact)),
    ]));
  });
  blocks.push(div());

  // Section — Checklist de pilotage mensuel
  blocks.push(h1("📋 Checklist de Pilotage Mensuel"));
  blocks.push(p("30 minutes par mois. Pas plus. Suffit pour garder le cap."));
  blocks.push(p(""));

  blocks.push(h3("Finance"));
  blocks.push(tod("Calculer le CA du mois par source (Affiliation / Agency / Produit)"));
  blocks.push(tod("Mettre à jour le Dashboard KPI (Google Sheets)"));
  blocks.push(tod("Vérifier la trésorerie : ≥ 6 mois de charges ?"));
  blocks.push(tod("Calculer la marge nette (CA – charges SASU – charges perso)"));

  blocks.push(p(""));
  blocks.push(h3("Agency"));
  blocks.push(tod("Lister les missions actives et leur statut"));
  blocks.push(tod("Identifier 3 prospects à relancer ou contacter"));
  blocks.push(tod("Vérifier les NPS des clients en accompagnement (envoyer si M+1)"));

  blocks.push(p(""));
  blocks.push(h3("schoolsWP — Contenu"));
  blocks.push(tod("Compter les articles publiés ce mois"));
  blocks.push(tod("Vérifier la progression SEO des 5 articles prioritaires (positions)"));
  blocks.push(tod("Identifier le prochain article à produire (brain-lite.bat)"));
  blocks.push(tod("Mesurer le trafic organique vs mois précédent (GA4)"));

  blocks.push(p(""));
  blocks.push(h3("Produit"));
  blocks.push(tod("Compter les ventes du mois"));
  blocks.push(tod("Lire les retours/questions des acheteurs"));
  blocks.push(tod("Identifier 1 amélioration ou 1 action de visibilité à faire"));

  blocks.push(p(""));
  blocks.push(h3("Stratégie (bilan trimestriel — 1x/3 mois)"));
  blocks.push(tod("Vérifier si les jalons de phase sont atteints"));
  blocks.push(tod("Décider si on passe à la phase suivante ou si on consolide"));
  blocks.push(tod("Documenter les 3 apprentissages clés du trimestre"));

  blocks.push(p(""));
  blocks.push(div());

  // Footer
  blocks.push(cal(
    `CA cumulé 24 mois — Conservateur : ${progression.reduce((a, p) => a + p.ca_annuel_mini, 0).toLocaleString("fr-FR")} € — Cible : ${progression.reduce((a, p) => a + p.ca_annuel_cible, 0).toLocaleString("fr-FR")} €. Ce n'est pas un plan théorique. C'est un système qui se construit mois après mois.`,
    "🏁",
    "green_background"
  ));

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page 'Roadmap 24 Mois — schoolsWP Hybride'...");

  const template = buildTemplate();
  const totalBlocks = template.length;
  const totalBatches = Math.ceil(totalBlocks / CHUNK);
  console.log(`📦 ${totalBlocks} blocs — ${totalBatches} batch(es) de ${CHUNK}`);

  const batch1 = template.slice(0, CHUNK);
  const pageRes = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🗺️" },
    properties: {
      title: { title: [{ text: { content: "🗺️ Roadmap 24 Mois — schoolsWP Hybride" } }] },
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

  const ca_mini = progression.reduce((a, p) => a + p.ca_annuel_mini, 0);
  const ca_cible = progression.reduce((a, p) => a + p.ca_annuel_cible, 0);

  console.log("");
  console.log("🎉 Page créée avec succès !");
  console.log(`🔗 https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📋 Récapitulatif :");
  console.log(`   • ${PHASES.length} phases avec actions, KPIs, risques et jalons GO`);
  console.log(`   • ${PHASES.reduce((a, p) => a + p.actions.reduce((b, c) => b + c.items.length, 0), 0)} actions total (cases à cocher)`);
  console.log(`   • ${PHASES.reduce((a, p) => a + p.kpis.length, 0)} KPIs de suivi`);
  console.log(`   • ${PHASES.reduce((a, p) => a + p.risques.length, 0)} risques identifiés avec mitigation`);
  console.log(`   • ${SECURITE_REGLES.length} règles de sécurité stratégique`);
  console.log(`   • ${FORCES_DISTINCTIVES.length} forces distinctives documentées`);
  console.log(`   • CA cumulé 24 mois : ${ca_mini.toLocaleString("fr-FR")} – ${ca_cible.toLocaleString("fr-FR")} €`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
