#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "💎 Offre Signature — B2B WordPress System",
  objectif: "Offre claire, premium, differenciante. Tu ne vends pas un site, tu vends une architecture business.",
};

const SECTIONS = [
  {
    titre: "🧠 Promesse centrale",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Je structure et optimise votre systeme WordPress pour qu'il supporte la vente, la gestion et l'automatisation de formations B2B, sans complexite inutile.",
      },
      {
        type: "p",
        texte: "Tu ne vends pas un site. Tu vends une architecture business."
      },
    ],
  },
  {
    titre: "🧱 Structure de l'offre (5 modules)",
    blocs: [
      {
        type: "h3",
        texte: "1 - Audit Strategique B2B (Fondation)"
      },
      {
        type: "bul",
        items: [
          "Analyse complete de l'existant",
          "Diagnostic architecture LMS",
          "Diagnostic CRM et segmentation",
          "Analyse tunnel et cycle long B2B",
          "Rapport PDF structure",
          "Roadmap priorisee"
        ]
      },
      {
        type: "p",
        texte: "Objectif : Identifier les blocages structurels."
      },
      {
        type: "h3",
        texte: "2 - Architecture LMS B2B"
      },
      {
        type: "bul",
        items: [
          "Structuration multi-entreprises",
          "Gestion comptes groupe",
          "Cohortes et acces segmentes",
          "Securisation acces",
          "Optimisation UX apprenant entreprise"
        ]
      },
      {
        type: "p",
        texte: "Objectif : Rendre le LMS scalable."
      },
      {
        type: "h3",
        texte: "3 - CRM et Automatisation B2B"
      },
      {
        type: "bul",
        items: [
          "Segmentation par entreprise",
          "Pipeline devis",
          "Automatisation onboarding",
          "Relances cycle long",
          "Sequences email adaptees B2B"
        ]
      },
      {
        type: "p",
        texte: "Objectif : Fluidifier le cycle commercial."
      }
    ],
  },
  {
    titre: "🧱 Structure de l'offre (suite)",
    blocs: [
      {
        type: "h3",
        texte: "4 - Tunnel et Conversion Corporate"
      },
      {
        type: "bul",
        items: [
          "Page offre entreprise optimisee",
          "Formulaire qualification",
          "Automatisation pre-appel",
          "Structuration proposition"
        ]
      },
      {
        type: "p",
        texte: "Objectif : Transformer trafic en contrats."
      },
      {
        type: "h3",
        texte: "5 - Optimisation et Scalabilite"
      },
      {
        type: "bul",
        items: [
          "Maillage interne strategique",
          "Optimisation performance",
          "Recommandations long terme",
          "Documentation systeme",
          "Session formation client"
        ]
      },
      {
        type: "p",
        texte: "Objectif : Autonomie et durabilite."
      }
    ],
  },
  {
    titre: "💰 Positionnement prix",
    blocs: [
      {
        type: "bul",
        items: [
          "Audit seul : 1 000 - 2 000 EUR",
          "Systeme complet : 4 000 - 8 000 EUR",
          "Version avancee : 8 000 - 15 000 EUR"
        ]
      },
      {
        type: "p",
        texte: "Le prix depend : complexite architecture, volume clients entreprise, niveau automatisation."
      }
    ],
  },
  {
    titre: "🎯 Pour qui ?",
    blocs: [
      {
        type: "bul",
        items: [
          "Formateurs vendant deja aux entreprises",
          "CA minimum existant",
          "Ambition de croissance",
          "Prets a structurer"
        ]
      }
    ],
  },
  {
    titre: "🚫 Pour qui ce n'est pas ?",
    blocs: [
      {
        type: "bul",
        items: [
          "Debutants",
          "B2C uniquement",
          "Budget limite",
          "Je veux juste un plugin"
        ]
      }
    ],
  },
  {
    titre: "🧠 Differenciation forte",
    blocs: [
      {
        type: "cal",
        emoji: "🚫",
        texte: "Tu ne dis pas : Je mets en place Tutor LMS."
      },
      {
        type: "cal",
        emoji: "✅",
        texte: "Tu dis : Je conçois l'architecture WordPress qui soutient votre croissance B2B."
      }
    ],
  },
  {
    titre: "📈 Strategie d'evolution",
    blocs: [
      {
        type: "bul",
        items: [
          "Annee 1 : Offre personnalisee",
          "Annee 2 : Methodologie packagee",
          "Annee 3 : Produit signature B2B WordPress"
        ]
      }
    ],
  }
];

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
  if (note) parts.push(rt("\n\n" + note, { italic: true, color: "gray" }));
  return { object: "block", type: "callout", callout: { rich_text: parts, icon: { type: "emoji", emoji } } };
};

function buildTemplate() {
  const blocks = [];
  blocks.push(cal("🎯", PAGE.objectif), p(""), div());

  for (const section of SECTIONS) {
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
    throw new Error(`Notion ${method} ${endpoint} -> ${res.status}: ${JSON.stringify(err)}`);
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

  console.log(`Creation page : ${PAGE.titre}`);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: NOTION_PARENT_PAGE_ID },
    properties: {
      title: { title: [{ text: { content: PAGE.titre } }] },
    },
    children: chunks[0],
  });

  console.log(`Page creee : ${page.url}`);

  for (let i = 1; i < chunks.length; i++) {
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${page.id}/children`, { children: chunks[i] });
  }

  console.log("Termine - Offre signature B2B WordPress deployee dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});
