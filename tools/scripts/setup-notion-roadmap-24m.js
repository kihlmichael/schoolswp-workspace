#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ════════════════════════════════════════════════════════
//  DATA
// ════════════════════════════════════════════════════════

const PAGE = {
  titre: "🗺 Roadmap 24 mois — Domination Niche Formateurs B2B",
  objectif: "Te positionner comme LA référence francophone des architectures WordPress pour formateurs B2B. Sans dispersion. Sans bruit. Avec logique.",
};

const PHASES = [
  {
    titre: "🧭 PHASE 1 — FONDATIONS STRATÉGIQUES (Mois 1–6)",
    objectif: "Clarifier positionnement + poser 1 cluster fort + signer 3–5 premiers clients B2B.",
    sections: [
      {
        h3: "🧱 1️⃣ Positionnement officiel",
        cal: "J’aide les formateurs B2B à structurer un système WordPress rentable, automatisé et scalable.",
        items: ["Bio schoolsWP", "Page À propos", "CTA Audit B2B", "Signature LinkedIn"]
      },
      {
        h3: "📚 2️⃣ Cluster prioritaire #1 : LMS WordPress B2B",
        cal: "Guide pilier :\n“Structurer un LMS WordPress pour formateurs B2B”",
        items: [
          "Comptes entreprise multi-utilisateurs",
          "Reporting apprenants entreprise",
          "Tutor LMS pour corporate",
          "Sécurisation accès formation B2B",
          "Paiement & facturation entreprise"
        ]
      },
      {
        h3: "💰 3️⃣ Offre Signature V1",
        cal: "Lancement de l'offre :\nB2B WordPress System — Audit & Architecture",
        items: [
          "Objectif : 3–5 clients",
          "Récupérer des études de cas",
          "Collecter des témoignages",
          "Accumuler des données réelles"
        ]
      }
    ]
  },
  {
    titre: "🚀 PHASE 2 — EXPANSION & AUTORITÉ (Mois 7–12)",
    objectif: "Devenir identifiable comme spécialiste B2B WordPress.",
    sections: [
      {
        h3: "🧠 1️⃣ Cluster #2 — CRM & Automatisation B2B",
        cal: "Guide pilier :\nCRM WordPress pour formateurs B2B",
        items: [
          "Segmentation entreprise",
          "Automatisation onboarding",
          "Pipeline devis B2B",
          "Relances automatisées"
        ]
      },
      {
        h3: "📈 2️⃣ Contenu décisionnel fort",
        cal: "Articles ciblés pour prospects en fin de funnel (BOFU)",
        items: [
          "“Quel LMS WordPress pour entreprise ?”",
          "“FluentCRM pour formation B2B”",
          "“Comment gérer 10 entreprises clientes sur WordPress ?”"
        ]
      },
      {
        h3: "🏢 3️⃣ Études de cas",
        cal: "La preuve par le résultat",
        items: [
          "Minimum 3 études de cas détaillées",
          "1 témoignage vidéo",
          "KPI concrets (temps gagné, automatisation, CA)"
        ]
      }
    ]
  }
];
const PHASES_PART_2 = [
  {
    titre: "💎 PHASE 3 — PREMIUM & SCALING (Année 2)",
    objectif: "Augmenter panier moyen + installer l'autorité définitive.",
    sections: [
      {
        h3: "🧱 1️⃣ Augmentation prix",
        cal: "Justifier l'augmentation de valeur",
        items: [
          "Basé sur les résultats clients",
          "Témoignages accumulés",
          "Autorité SEO (trafic entrant qualifié)",
          "Rareté de la niche"
        ]
      },
      {
        h3: "🟣 2️⃣ Produit Signature B2B",
        cal: "Passer de la prestation au produit (Scaling)",
        items: [
          "Formation : “Construire votre écosystème WordPress B2B”",
          "OU",
          "Template système B2B prêt à configurer (Produit digital clé en main)"
        ]
      },
      {
        h3: "📊 3️⃣ Cluster #3 — Performance & optimisation B2B",
        cal: "Fidélisation et augmentation de la LTV",
        items: [
          "KPI formation entreprise",
          "Optimisation renouvellement contrat",
          "Upsell formation avancée",
          "Reporting avancé"
        ]
      }
    ]
  }
];

const KPI = [
  {
    h3: "🔍 SEO",
    items: ["3 clusters dominés", "30–40 articles ciblés B2B", "Présence AI Overview sur sujets clés"]
  },
  {
    h3: "🏢 Agency",
    items: ["10–20 projets B2B structurants", "Panier moyen premium", "Positionnement clair installé"]
  },
  {
    h3: "📦 Produit",
    items: ["1 produit signature lancé", "20–40 ventes/mois régulières"]
  }
];

const DIFFERENCIATION = {
  avant: "“Expert WordPress” (Générique, forte concurrence, guerre des prix)",
  apres: "L’architecte WordPress des formateurs B2B francophones.",
  pourquoi: "Position rare. Marché solvable. Concurrence floue."
};

const ALL_PHASES = [...PHASES, ...PHASES_PART_2];

// ════════════════════════════════════════════════════════
//  BLOCK BUILDERS
// ════════════════════════════════════════════════════════

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: { bold: !!opts.bold, italic: !!opts.italic, color: opts.color || "default" },
});

const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (...parts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: parts.flat() } });
const bul = (t) => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: [rt(t)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (emoji, t, note) => {
  const parts = [rt(t, { bold: true })];
  if (note) {
    parts.push(rt("\n" + note, { italic: true, color: "gray" }));
  }
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

// ════════════════════════════════════════════════════════
//  TEMPLATE BUILDER
// ════════════════════════════════════════════════════════

function buildTemplate() {
  const blocks = [];

  // Header
  blocks.push(
    cal("🎯", "Objectif", PAGE.objectif),
    p(""),
    div()
  );

  // Phases
  for (const phase of ALL_PHASES) {
    blocks.push(
      h2(phase.titre),
      p(rt("🎯 Objectif de la phase : ", { bold: true }), rt(phase.objectif, { italic: true }))
    );
    
    for (const sec of phase.sections) {
      blocks.push(
        h3(sec.h3),
        cal("💡", sec.cal)
      );
      for (const item of sec.items) {
        blocks.push(bul(item));
      }
      blocks.push(p(""));
    }
    blocks.push(div());
  }

  // KPIs
  blocks.push(h2("📈 KPI 24 mois (Cible)"));
  for (const kpi of KPI) {
    blocks.push(h3(kpi.h3));
    for (const item of kpi.items) {
      blocks.push(bul(item));
    }
  }
  blocks.push(div());

  // Différenciation
  blocks.push(
    h2("🧠 Différenciation finale"),
    p(rt("❌ Tu ne seras plus :", { color: "red", bold: true })),
    cal("🚫", DIFFERENCIATION.avant),
    p(""),
    p(rt("✅ Tu seras :", { color: "green", bold: true })),
    cal("👑", DIFFERENCIATION.apres),
    p(rt("Pourquoi ça marche : ", { bold: true }), rt(DIFFERENCIATION.pourquoi, { italic: true }))
  );

  return blocks;
}

// ════════════════════════════════════════════════════════
//  NOTION API
// ════════════════════════════════════════════════════════

async function notionRequest(method, endpoint, body) {
  const res = await fetch(`https://api.notion.com/v1${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Notion-Version": NOTION_VERSION,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(`Notion ${method} ${endpoint} → ${res.status}: ${JSON.stringify(err)}`);
  }
  return res.json();
}

async function main() {
  if (!NOTION_API_KEY) throw new Error("NOTION_API_KEY manquant");
  if (!NOTION_PARENT_PAGE_ID) throw new Error("NOTION_PARENT_PAGE_ID manquant");

  const allBlocks = buildTemplate();
  const chunks = [];
  for (let i = 0; i < allBlocks.length; i += CHUNK) {
    chunks.push(allBlocks.slice(i, i + CHUNK));
  }

  console.log(`📄 Création page : ${PAGE.titre}`);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: NOTION_PARENT_PAGE_ID },
    properties: {
      title: { title: [{ text: { content: PAGE.titre } }] },
    },
    children: chunks[0],
  });

  console.log(`✅ Page créée : ${page.url}`);

  for (let i = 1; i < chunks.length; i++) {
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${page.id}/children`, { children: chunks[i] });
  }

  console.log(`🎉 Terminé — Roadmap 24 mois déployée dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});