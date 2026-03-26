#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGE = {
  titre: "📩 Script DM Premium — Formateurs B2B (structuré)",
  objectif: "Diagnostic naturel, pas de pitch. Filtrer bas budget, amener vers appel stratégique.",
};

const SECTIONS = [
  {
    titre: "🧠 Principes",
    blocs: [
      { type: "p", texte: "Tu ne vends pas. Tu observes. Tu diagnostiques. Tu qualifies." },
      { type: "p", texte: "Le DM doit sonner comme une conversation d'expert, pas un tunnel de vente." },
    ],
  },
  {
    titre: "🟢 Etape 1 — Ouverture naturelle",
    blocs: [
      { type: "p", texte: "Apres interaction sur un post ou profil :" },
      {
        type: "cal",
        emoji: "💬",
        texte: "Bonjour {{Prenom}},\n\nJ'ai vu que vous proposez des formations pour entreprises.\n\nPar curiosite : votre architecture WordPress est-elle pensee pour gerer plusieurs clients corporate (multi-comptes, reporting, onboarding) ?",
        note: "Objectif : question strategique, pas vente.",
      },
    ],
  },
  {
    titre: "🔵 Etape 2 — Diagnostic leger",
    blocs: [
      { type: "p", texte: "S'ils repondent :" },
      {
        type: "cal",
        emoji: "💬",
        texte: "Interessant.\n\nVous gerez actuellement combien d'entreprises differentes sur votre LMS ?\n\nEt votre CRM segmente par entreprise ou uniquement par utilisateur ?",
        note: "On teste : volume, complexite, niveau de maturite.",
      },
    ],
  },
];
const SECTIONS_PART_2 = [
  {
    titre: "🟣 Etape 3 — Mise en lumiere d'un angle",
    blocs: [
      { type: "p", texte: "Selon reponse :" },
      {
        type: "cal",
        emoji: "💬",
        texte: "Je pose la question parce que beaucoup de formateurs B2B ont un LMS correct,\nmais un CRM mal structure pour le cycle entreprise.\n\nCa cree des frictions invisibles.",
        note: "Toujours pedagogique. Jamais accusateur.",
      },
    ],
  },
  {
    titre: "🟡 Etape 4 — Proposition soft",
    blocs: [
      {
        type: "cal",
        emoji: "💬",
        texte: "Si vous voulez, je peux vous dire en 15-20 minutes si votre architecture est optimisee pour du B2B.\n\nCe sera simplement un echange strategique, pas un pitch.",
        note: "Clair. Direct. Non agressif.",
      },
    ],
  },
  {
    titre: "🧱 Version plus directe (lead chaud)",
    blocs: [
      {
        type: "cal",
        emoji: "💬",
        texte: "Je travaille exclusivement avec des formateurs B2B sur la structuration de leur systeme WordPress (LMS + CRM + automatisation).\n\nSi votre objectif est de scaler cote entreprise, un audit rapide peut etre utile.",
      },
    ],
  },
];

const SECTIONS_PART_3 = [
  {
    titre: "🎯 Filtrage premium (avant appel)",
    blocs: [
      { type: "p", texte: "Avant de proposer un lien :" },
      {
        type: "cal",
        emoji: "💬",
        texte: "Pour que l'echange soit pertinent :\n\n- Vous facturez combien en moyenne une formation entreprise ?\n- Combien d'entreprises actives actuellement ?\n- Objectif 12 mois ?",
      },
    ],
  },
  {
    titre: "🧠 Ton a maintenir",
    blocs: [
      { type: "bul", items: ["Calme", "Expert", "Diagnostic", "Jamais insistant", "Jamais commercial"] },
    ],
  },
];

const ALL_SECTIONS = [...SECTIONS, ...SECTIONS_PART_2, ...SECTIONS_PART_3];
const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: { bold: !!opts.bold, italic: !!opts.italic, color: opts.color || "default" },
});

const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
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

  for (const section of ALL_SECTIONS) {
    blocks.push(h2(section.titre));
    for (const b of section.blocs) {
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

  console.log("Termine - Script DM Premium B2B deploye dans Notion.");
}

main().catch((err) => {
  console.error("Erreur :", err.message);
  process.exit(1);
});
