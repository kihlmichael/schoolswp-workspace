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
  titre: "📩 Script DM Premium — Qualification B2B",
  objectif: "Filtrer les petits budgets. Positionner l'expertise. Ne jamais paraître vendeur. Tu es architecte, pas commercial.",
};

const SECTIONS = [
  {
    titre: "🧠 Logique du Script",
    blocs: [
      {
        type: "p",
        texte: "Un DM ne sert pas à vendre. Il sert à :"
      },
      {
        type: "bul",
        items: [
          "Comprendre la situation",
          "Identifier le problème structurel",
          "Créer un déclic",
          "Proposer un diagnostic"
        ]
      }
    ]
  },
  {
    titre: "🟢 Étape 1 — Ouverture Naturelle",
    blocs: [
      {
        type: "p",
        texte: "Après interaction (commentaire / post / connexion acceptée) :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Bonjour {{Prénom}},\n\nJ’ai vu que vous proposez des formations en entreprise.\n\nPar curiosité : votre système WordPress est-il pensé pour gérer plusieurs clients corporate simultanément ?",
        note: "➡ Question ouverte.\n➡ Pas de vente.\n➡ Diagnostic implicite."
      }
    ]
  },
  {
    titre: "🔵 Étape 2 — Exploration Douce",
    blocs: [
      {
        type: "p",
        texte: "S’il répond : Intéressant..."
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Est-ce que vous gérez :\n– des comptes entreprise multi-utilisateurs ?\n– un onboarding automatisé ?\n– un CRM segmenté par client ?",
        note: "But : Faire émerger les manques sans les pointer agressivement."
      }
    ]
  },
  {
    titre: "🟣 Étape 3 — Création du Déclic",
    blocs: [
      {
        type: "p",
        texte: "Selon sa réponse, introduire la norme du marché :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Beaucoup de formateurs B2B que j’accompagne ont un LMS qui fonctionne…\nmais l’architecture globale n’est pas pensée pour la scalabilité entreprise."
      },
      {
        type: "p",
        texte: "Pause. Laisse maturer."
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🟡 Étape 4 — Proposition Non Agressive",
    blocs: [
      {
        type: "p",
        texte: "Si l'intérêt est détecté :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Si vous voulez, je peux jeter un œil rapide à votre architecture actuelle et vous dire en 15 minutes si elle est optimisée pour le B2B.",
        note: "Pas : “Réservez un appel.”\nMais : “Jeter un œil.”"
      }
    ]
  },
  {
    titre: "🔴 Étape 5 — Qualification Premium Avant Appel",
    blocs: [
      {
        type: "p",
        texte: "AVANT de donner un lien Calendly :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Pour que ce soit pertinent, vous êtes plutôt sur :\n– quelques clients entreprise ?\n– ou déjà une dizaine ?\n\nEt votre objectif 12 mois, c’est plutôt stabiliser ou scaler ?",
        note: "Objectif : Tu qualifies son niveau de maturité."
      }
    ]
  },
  {
    titre: "💰 Filtrage Intelligent (Savoir dire NON)",
    blocs: [
      {
        type: "p",
        texte: "Si le budget ou la maturité est trop faible :"
      },
      {
        type: "cal",
        emoji: "💬",
        texte: "Je pense que votre priorité est d’abord de clarifier votre offre B2B. Je vous recommande de structurer X avant d’investir dans l’architecture.",
        note: "Tu restes expert. Pas frustré. Tu gardes la porte ouverte pour plus tard."
      }
    ]
  },
  {
    titre: "📈 Les Attentes (Conversion)",
    blocs: [
      {
        type: "p",
        texte: "Sur 10 conversations initiées :"
      },
      {
        type: "bul",
        items: [
          "3 vrais échanges",
          "1 appel booké",
          "1 proposition envoyée",
          "0.5 à 1 closing"
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

  // Conclusion Forte
  blocks.push(
    h2("🧠 RAPPEL DU POSITIONNEMENT IMPLICITE"),
    p("Tu n'es pas Freelance WordPress."),
    cal("👑", "Tu es : Architecte des systèmes WordPress B2B.", "Le DM doit respirer la structure et l'expertise technique, jamais le besoin de vendre.")
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

  console.log(`🎉 Terminé — Script DM Premium déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});