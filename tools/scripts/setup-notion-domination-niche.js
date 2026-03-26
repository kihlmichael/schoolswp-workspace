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
  titre: "🌋 Plan de Domination : Niche Ultra-Précise",
  objectif: "Arrêter d'être 'expert WordPress large'. Devenir LA référence évidente des formateurs en ligne utilisant WordPress.",
};

const SECTIONS = [
  {
    titre: "🎯 1️⃣ Pourquoi la niche est stratégique pour toi",
    blocs: [
      {
        type: "p",
        texte: "Avec schoolsWP + Agency :"
      },
      {
        type: "bul",
        items: [
          "Le SEO est plus rapide",
          "L’autorité est plus forte",
          "Le closing est plus simple",
          "Le pricing peut être premium",
          "La concurrence est floue"
        ]
      },
      {
        type: "cal",
        emoji: "❌",
        texte: "Tu ne veux pas :\n“Tous les utilisateurs WordPress”"
      },
      {
        type: "cal",
        emoji: "✅",
        texte: "Tu veux :\nUn profil qui a un vrai problème business."
      }
    ]
  },
  {
    titre: "🧠 2️⃣ Les niches cohérentes avec TON ADN",
    blocs: [
      {
        type: "p",
        texte: "Vu ton positionnement (SEO + CRM + LMS + automatisation) :"
      },
      {
        type: "h3",
        texte: "Option A — Formateurs & créateurs de formations"
      },
      {
        type: "cal",
        emoji: "🥇",
        texte: "LMS • Tunnel email • CRM • Automatisation • Upsell • Membership\nTrès aligné avec Fluent, Tutor, etc."
      },
      {
        type: "h3",
        texte: "Option B — Freelances & consultants digitaux"
      },
      {
        type: "cal",
        emoji: "🥈",
        texte: "Structuration offre • Tunnel simple • CRM • SEO • Automatisation onboarding\nPlus large mais rentable."
      },
      {
        type: "h3",
        texte: "Option C — Coaches & infopreneurs"
      },
      {
        type: "cal",
        emoji: "🥉",
        texte: "Systèmes de vente • Webinaires • CRM avancé • Segmentation\nTrès business mais plus marketing."
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🏆 3️⃣ Niche recommandée stratégique",
    blocs: [
      {
        type: "cal",
        emoji: "👉",
        texte: "Formateurs / créateurs de formations en ligne utilisant WordPress"
      },
      {
        type: "p",
        texte: "Pourquoi ?"
      },
      {
        type: "bul",
        items: [
          "Fort besoin technique",
          "Budget supérieur à la moyenne",
          "Problématique CRM + LMS complexe",
          "Peu d’experts spécialisés",
          "Compatible contenu SEO",
          "Compatible Agency premium",
          "Compatible produit digital"
        ]
      },
      {
        type: "h3",
        texte: "L'Objectif"
      },
      {
        type: "cal",
        emoji: "🏛️",
        texte: "Tu peux devenir : L’architecte WordPress des formateurs en ligne."
      }
    ]
  },
  {
    titre: "🧱 4️⃣ Stratégie domination en 3 couches",
    blocs: [
      {
        type: "h3",
        texte: "Couche 1 — SEO ciblé niche"
      },
      {
        type: "bul",
        items: [
          "LMS WordPress complet",
          "CRM pour formateurs",
          "Tunnel WordPress pour formation",
          "Automatisation email formation",
          "Paiement & upsell WordPress"
        ]
      },
      {
        type: "p",
        texte: "Objectif : Dominer 1 univers précis."
      },
      {
        type: "h3",
        texte: "Couche 2 — Offre Agency ultra alignée"
      },
      {
        type: "cal",
        emoji: "💼",
        texte: "Offre signature : “Système WordPress rentable pour formateurs”",
        note: "Inclut : LMS structuré, CRM segmenté, Tunnel simple, Email automation, Optimisation conversion.\nPositionnement : Transformation business, pas technique."
      },
      {
        type: "h3",
        texte: "Couche 3 — Produit signature futur"
      },
      {
        type: "bul",
        items: [
          "Formation “Construire votre écosystème WordPress de formation”",
          "Template système LMS + CRM",
          "Masterclass automatisation pour formateurs"
        ]
      }
    ]
  }
];
const SECTIONS_PART_3 = [
  {
    titre: "💰 5️⃣ Impact pricing",
    blocs: [
      {
        type: "cal",
        emoji: "💵",
        texte: "Un freelance généraliste vend 1 500–2 500 €."
      },
      {
        type: "cal",
        emoji: "💎",
        texte: "Un expert niche peut vendre : 4 000–8 000 €.",
        note: "Parce qu’il comprend : Le business modèle • Les métriques • La logique funnel • L’optimisation"
      }
    ]
  },
  {
    titre: "📈 6️⃣ Vision 24 mois",
    blocs: [
      {
        type: "h3",
        texte: "Année 1"
      },
      {
        type: "bul",
        items: [
          "Dominer SEO LMS WordPress",
          "5–10 projets formateurs",
          "1 produit digital"
        ]
      },
      {
        type: "h3",
        texte: "Année 2"
      },
      {
        type: "bul",
        items: [
          "Autorité claire",
          "Témoignages",
          "Upsell optimisation",
          "Augmentation prix"
        ]
      }
    ]
  },
  {
    titre: "🔥 7️⃣ Différenciation forte",
    blocs: [
      {
        type: "p",
        texte: "Tu ne dis pas :"
      },
      {
        type: "cal",
        emoji: "🚫",
        texte: "“Je crée des LMS WordPress”"
      },
      {
        type: "p",
        texte: "Tu dis :"
      },
      {
        type: "cal",
        emoji: "👑",
        texte: "Je structure l’architecture WordPress rentable des formateurs ambitieux."
      }
    ]
  }
];

const ALL_SECTIONS = [...SECTIONS, ...SECTIONS_PART_2, ...SECTIONS_PART_3];

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
const p = (t) => ({ object: "block", type: "paragraph", paragraph: { rich_text: [rt(t)] } });
const bul = (t) => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: [rt(t)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (emoji, t, note) => {
  const parts = [rt(t, { bold: true })];
  if (note) {
    parts.push(rt("\n\n" + note, { italic: true, color: "gray" }));
  }
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

// ════════════════════════════════════════════════════════
//  TEMPLATE BUILDER
// ════════════════════════════════════════════════════════

function buildTemplate() {
  const blocks = [];

  blocks.push(
    cal("🎯", PAGE.objectif),
    p(""),
    div()
  );

  for (const section of ALL_SECTIONS) {
    blocks.push(h2(section.titre));
    
    for (const b of section.blocs) {
      if (b.type === "h3") blocks.push(h3(b.texte));
      if (b.type === "p") blocks.push(p(b.texte));
      if (b.type === "cal") blocks.push(cal(b.emoji, b.texte, b.note));
      if (b.type === "bul") {
        for (const item of b.items) blocks.push(bul(item));
      }
    }
    blocks.push(div());
  }

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

  console.log(`🎉 Terminé — Plan de Domination Niche déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});