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
  titre: "♟️ Stratégie LinkedIn Acquisition B2B",
  objectif: "Générer des leads qualifiés → Installer ton autorité → Pré-vendre ton audit B2B.",
};

const SECTIONS = [
  {
    titre: "🧠 1️⃣ Positionnement LinkedIn (fondation obligatoire)",
    blocs: [
      {
        type: "h3",
        texte: "🎯 Titre optimisé"
      },
      {
        type: "cal",
        emoji: "💡",
        texte: "Architecte de systèmes WordPress B2B | LMS • CRM • Automatisation | J’aide les formateurs à structurer un écosystème rentable",
        note: "Clair. Spécifique. Pas générique."
      },
      {
        type: "h3",
        texte: "📝 Bannière"
      },
      {
        type: "cal",
        emoji: "🖼️",
        texte: "Structurer votre système WordPress B2B\nLMS • CRM • Automatisation • Scalabilité\n\n👉 CTA discret : Audit stratégique B2B"
      }
    ]
  },
  {
    titre: "🧱 2️⃣ Stratégie de contenu LinkedIn (3 piliers)",
    blocs: [
      {
        type: "p",
        texte: "Tu ne publies pas au hasard."
      },
      {
        type: "h3",
        texte: "🟢 PILIER 1 — Problèmes B2B réels"
      },
      {
        type: "bul",
        items: [
          "“Votre LMS WordPress n’est pas conçu pour gérer 10 entreprises.”",
          "“Le vrai problème des formateurs B2B n’est pas le LMS, c’est le CRM.”",
          "“Pourquoi votre tunnel B2B WordPress bloque vos ventes ?”"
        ]
      },
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif :\n👉 Faire réfléchir\n👉 Créer tension\n👉 Montrer expertise"
      },
      {
        type: "h3",
        texte: "🔵 PILIER 2 — Architecture & méthode"
      },
      {
        type: "bul",
        items: [
          "“Voici l’architecture WordPress que j’utilise pour les formateurs B2B.”",
          "“Comment structurer un onboarding entreprise automatisé.”",
          "“La segmentation CRM que 90 % des formateurs ignorent.”"
        ]
      },
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif :\n👉 Montrer profondeur\n👉 Montrer méthode\n👉 Crédibilité technique"
      },
      {
        type: "h3",
        texte: "🟣 PILIER 3 — Études de cas & retours terrain"
      },
      {
        type: "bul",
        items: [
          "“Comment un formateur B2B a automatisé son onboarding.”",
          "“Avant / Après : architecture LMS B2B.”",
          "“3 erreurs que j’ai corrigées chez un client formation entreprise.”"
        ]
      },
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif :\n👉 Preuve sociale\n👉 Concret\n👉 Autorité"
      }
    ]
  },
  {
    titre: "📅 3️⃣ Rythme optimal",
    blocs: [
      {
        type: "p",
        texte: "3 posts / semaine suffisent."
      },
      {
        type: "bul",
        items: [
          "Lundi → Problème B2B",
          "Mercredi → Architecture",
          "Vendredi → Cas réel / insight"
        ]
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🎯 4️⃣ Stratégie DM intelligente",
    blocs: [
      {
        type: "p",
        texte: "Ne pas spammer. Process :"
      },
      {
        type: "num",
        items: [
          "Publier contenu utile",
          "Interagir avec formateurs B2B",
          "Commentaires stratégiques",
          "DM naturel :"
        ]
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "J’ai vu que vous proposez des formations entreprise.\nEst-ce que votre architecture WordPress est pensée pour gérer plusieurs clients corporate ?"
      },
      {
        type: "p",
        texte: "Pas vente directe. Diagnostic."
      }
    ]
  },
  {
    titre: "💬 5️⃣ Structure post LinkedIn performante",
    blocs: [
      {
        type: "p",
        texte: "Format recommandé :"
      },
      {
        type: "num",
        items: [
          "Hook fort (1 ligne)",
          "Problème clair",
          "Explication simple",
          "Insight expert",
          "Mini solution",
          "Question ouverte"
        ]
      }
    ]
  },
  {
    titre: "📈 6️⃣ KPI LinkedIn B2B",
    blocs: [
      {
        type: "bul",
        items: [
          "Taux engagement > 3 %",
          "3–5 conversations qualifiées / semaine",
          "1–2 appels / semaine",
          "1 closing / mois minimum"
        ]
      }
    ]
  },
  {
    titre: "💰 7️⃣ Tunnel LinkedIn → Agency",
    blocs: [
      {
        type: "cal",
        emoji: "🔄",
        texte: "Post\n↓\nProfil optimisé\n↓\nAudit B2B\n↓\nAppel stratégique\n↓\nProposition premium"
      }
    ]
  },
  {
    titre: "🧠 8️⃣ Différenciation clé",
    blocs: [
      {
        type: "p",
        texte: "Ne parle pas : “Plugin X est super.”"
      },
      {
        type: "p",
        texte: "Parle : “Voici pourquoi votre architecture WordPress limite votre croissance B2B.”"
      },
      {
        type: "cal",
        emoji: "🔥",
        texte: "Tu ne vends pas un outil.\nTu vends une structure."
      }
    ]
  }
];

const ALL_SECTIONS = [...SECTIONS, ...SECTIONS_PART_2];

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
const num = (t) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: [rt(t)] } });
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

  // Header
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
      if (b.type === "num") {
        for (const item of b.items) blocks.push(num(item));
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

  console.log(`🎉 Terminé — Stratégie LinkedIn B2B déployée dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});