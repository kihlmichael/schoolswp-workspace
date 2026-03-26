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
  titre: "📜 Manifeste de Positionnement — Architecte B2B",
  objectif: "Ne plus cibler 'les formateurs'. Viser : les formateurs B2B premium utilisant WordPress.",
};

const SECTIONS = [
  {
    titre: "🧠 1️⃣ Pourquoi la niche “Formateurs B2B” est stratégique",
    blocs: [
      {
        type: "cal",
        emoji: "📉",
        texte: "Le Formateur B2C",
        note: "Vend à 97€ / 297€\nTravaille au volume\nBudget technique limité"
      },
      {
        type: "cal",
        emoji: "📈",
        texte: "Le Formateur B2B",
        note: "Vend à 1 500€ / 5 000€ / 15 000€\nVend aux entreprises\nBudget technique conséquent"
      },
      {
        type: "h3",
        texte: "Les besoins B2B (Problématique complexe = forte valeur)"
      },
      {
        type: "bul",
        items: [
          "CRM structuré",
          "Segmentation avancée",
          "Onboarding",
          "Reporting",
          "Espace formation sécurisé",
          "Facturation propre"
        ]
      }
    ]
  },
  {
    titre: "🏗 2️⃣ Positionnement ultra précis",
    blocs: [
      {
        type: "p",
        texte: "Tu ne deviens pas :"
      },
      {
        type: "cal",
        emoji: "❌",
        texte: "“Expert WordPress LMS”"
      },
      {
        type: "p",
        texte: "Tu deviens :"
      },
      {
        type: "cal",
        emoji: "✅",
        texte: "Architecte des systèmes WordPress pour formateurs B2B ambitieux."
      },
      {
        type: "h3",
        texte: "Le Vocabulaire"
      },
      {
        type: "bul",
        items: [
          "Rentabilité",
          "Structuration",
          "Automatisation",
          "Scalabilité",
          "Crédibilité entreprise"
        ]
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🧱 3️⃣ Problèmes spécifiques B2B (Clusters SEO + Agency)",
    blocs: [
      {
        type: "h3",
        texte: "🎓 LMS WordPress B2B"
      },
      {
        type: "bul",
        items: [
          "Gestion multi-entreprises",
          "Comptes groupe",
          "Accès par cohorte",
          "Reporting apprenant"
        ]
      },
      {
        type: "h3",
        texte: "🧠 CRM WordPress B2B"
      },
      {
        type: "bul",
        items: [
          "Segmentation entreprise",
          "Automatisation onboarding",
          "Relances devis",
          "Cycle long"
        ]
      },
      {
        type: "h3",
        texte: "💼 Tunnel WordPress B2B"
      },
      {
        type: "bul",
        items: [
          "Page offre corporate",
          "Formulaire qualification",
          "Devis automatisé",
          "Pipeline commercial"
        ]
      },
      {
        type: "h3",
        texte: "📊 Reporting & Performance"
      },
      {
        type: "bul",
        items: [
          "Tracking formation",
          "KPI entreprise",
          "Renouvellement (Renewal)"
        ]
      }
    ]
  },
  {
    titre: "💰 4️⃣ Offre Signature Agency (version premium)",
    blocs: [
      {
        type: "cal",
        emoji: "🚀",
        texte: "B2B WordPress System™"
      },
      {
        type: "p",
        texte: "Ce qu'elle inclut :"
      },
      {
        type: "bul",
        items: [
          "Audit stratégique",
          "Architecture LMS",
          "CRM segmenté",
          "Tunnel B2B",
          "Automatisation onboarding",
          "Optimisation conversion entreprise"
        ]
      },
      {
        type: "p",
        texte: "Positionnement prix : Premium assumé."
      }
    ]
  }
];
const SECTIONS_PART_3 = [
  {
    titre: "📈 5️⃣ SEO domination ultra spécifique",
    blocs: [
      {
        type: "p",
        texte: "Exemples d'articles :"
      },
      {
        type: "bul",
        items: [
          "“Comment structurer un LMS WordPress pour entreprises ?”",
          "“CRM WordPress pour formateurs B2B : quelle architecture ?”",
          "“Gérer plusieurs clients entreprise sur Tutor LMS”",
          "“Automatiser l’onboarding formation B2B”"
        ]
      },
      {
        type: "cal",
        emoji: "🔥",
        texte: "Concurrence faible. Intention forte. Clients qualifiés."
      }
    ]
  },
  {
    titre: "🧠 6️⃣ Produit digital futur aligné",
    blocs: [
      {
        type: "bul",
        items: [
          "Template “Système B2B WordPress”",
          "Formation “Structurer votre offre formation entreprise”",
          "Checklist architecture LMS corporate"
        ]
      }
    ]
  },
  {
    titre: "🚀 7️⃣ Ce que ça change pour toi",
    blocs: [
      {
        type: "p",
        texte: "Tu passes de :"
      },
      {
        type: "cal",
        emoji: "🚫",
        texte: "“Expert WordPress avancé”"
      },
      {
        type: "p",
        texte: "À :"
      },
      {
        type: "cal",
        emoji: "👑",
        texte: "“Spécialiste des architectures WordPress B2B”",
        note: "C’est rare.\nC’est premium.\nC’est crédible."
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

  console.log(`🎉 Terminé — Manifeste de Positionnement déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});