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
  titre: "🏗 Modèle Média (schoolsWP) + Agency (SASU)",
  objectif: "Que schoolsWP devienne ta machine d’autorité et que la SASU devienne ta machine de cash premium. Sans cannibalisation ni confusion.",
};

const SECTIONS = [
  {
    titre: "🧠 1️⃣ Rôle clair de chaque entité",
    blocs: [
      {
        type: "h3",
        texte: "🟢 schoolsWP = Autorité + Audience + Confiance"
      },
      {
        type: "cal",
        emoji: "🎓",
        texte: "Positionnement : Pédagogue expert WordPress orienté systèmes.",
        note: "Mission : Éduquer • Comparer • Expliquer • Structurer\nMonétisation : Affiliation • Produits digitaux • Newsletter • Sponsoring"
      },
      {
        type: "h3",
        texte: "🔵 SASU = Transformation + Implémentation + Premium"
      },
      {
        type: "cal",
        emoji: "🏗️",
        texte: "Positionnement : Architecte de systèmes WordPress rentables.",
        note: "Mission : Implémenter • Structurer • Optimiser • Automatiser\nMonétisation : Audits • Projets structurés • Accompagnement • Maintenance"
      }
    ]
  },
  {
    titre: "🎯 2️⃣ Le pont stratégique (La passerelle)",
    blocs: [
      {
        type: "p",
        texte: "schoolsWP ne vend pas directement des prestations. Il vend de la clarté, de la méthode, de la vision."
      },
      {
        type: "cal",
        emoji: "🌉",
        texte: "La transition (Subtile, pas agressive) :",
        note: "👉 CTA vers Audit stratégique\n👉 Diagnostic WordPress Business\n👉 Appel architecture système"
      }
    ]
  },
  {
    titre: "🧱 3️⃣ Architecture Funnel idéale",
    blocs: [
      {
        type: "num",
        items: [
          "Article SEO décisionnel (ex: CRM WordPress : lequel choisir ?)",
          "CTA intelligent (« Si vous voulez structurer votre système... je propose un audit »)",
          "Formulaire qualifiant (CA actuel, outils, budget, objectifs)",
          "Appel Stratégique (On ne vend pas un 'site', on vend une 'architecture')"
        ]
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "📈 4️⃣ Ratio de Contenu Stratégique",
    blocs: [
      {
        type: "p",
        texte: "Le mix éditorial parfait pour nourrir l'Agency :"
      },
      {
        type: "cal",
        emoji: "📊",
        texte: "La règle des 40/40/20",
        note: "40 % Contenu informationnel\n40 % Contenu décisionnel (Comparatifs, choix outils)\n20 % Contenu orienté architecture système (Pour les leads Premium)"
      }
    ]
  },
  {
    titre: "💰 5️⃣ Logique de Monétisation Croisée",
    blocs: [
      {
        type: "p",
        texte: "Ce n'est plus du SEO. C'est du capital actif."
      },
      {
        type: "cal",
        emoji: "💎",
        texte: "La puissance d'un seul article bien placé :",
        note: "100 € affiliation\n+ 1 lead qualifié\n+ 1 client à 3 000 €\n+ 1 témoignage = Effet boule de neige"
      }
    ]
  },
  {
    titre: "🏗 6️⃣ & 7️⃣ Plan 12 mois & Différenciation",
    blocs: [
      {
        type: "p",
        texte: "Tu ne deviens pas 'Encore un freelance WordPress'. Tu deviens l'expert qui pense WordPress comme un système business complet."
      },
      {
        type: "h3",
        texte: "Mois 1–3 : Les fondations"
      },
      {
        type: "bul",
        items: [
          "1 cluster fort (CRM ou LMS)",
          "5 articles décisionnels",
          "Page Audit prête"
        ]
      },
      {
        type: "h3",
        texte: "Mois 4–6 : La validation"
      },
      {
        type: "bul",
        items: [
          "Études de cas réelles",
          "Témoignages clients",
          "1 offre signature agency claire"
        ]
      },
      {
        type: "h3",
        texte: "Mois 7–12 : La domination"
      },
      {
        type: "bul",
        items: [
          "Optimisation systématique des CTA",
          "Domination SEO complète du cluster",
          "Positionnement premium totalement assumé"
        ]
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

  // Clôture
  blocks.push(
    h2("🔥 8️⃣ Avantage Stratégique Énorme"),
    p("Ta force unique :"),
    bul("Tu maîtrises le contenu"),
    bul("Tu maîtrises le SEO"),
    bul("Tu maîtrises l'automatisation"),
    bul("Tu maîtrises l'architecture des systèmes"),
    p(""),
    cal("🥷", "La conclusion logique :", "Tu peux créer une Agency invisible (pas de bruit, juste un tunnel SEO -> Audit) mais ultra qualitative et premium.")
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

  console.log(`🎉 Terminé — Modèle Média + Agency déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});