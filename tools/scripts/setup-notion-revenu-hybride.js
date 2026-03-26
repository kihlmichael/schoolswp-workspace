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
  titre: "💰 Modèle de Revenu Hybride schoolsWP",
  objectif: "Affiliation + Agency + Produit = stabilité + scalabilité + premium. Ne jamais dépendre d’un seul flux.",
};

const SECTIONS = [
  {
    titre: "🧠 1️⃣ Architecture du modèle hybride (3 piliers)",
    blocs: [
      {
        type: "h3",
        texte: "🟢 PILIER 1 — Affiliation (Cash organique)"
      },
      {
        type: "cal",
        emoji: "💸",
        texte: "Rôle : Monétisation naturelle de l'audience SEO.",
        note: "Sources : Plugins WordPress (CRM, LMS, e-commerce), Hébergement, Outils SEO, Outils IA.\nAvantages : Revenus passifs, Scalabilité, Aucun coût marginal, Compatible SEO.\nLimite : Dépendance au trafic."
      },
      {
        type: "h3",
        texte: "🔵 PILIER 2 — Agency (Cash premium)"
      },
      {
        type: "cal",
        emoji: "💎",
        texte: "Rôle : Monétisation forte valeur.",
        note: "Offre type : Audit + structuration + automatisation.\nAvantages : Panier élevé, Cash-flow rapide, Témoignages, Études de cas.\nLimite : Temps limité (nécessite sélection clients)."
      },
      {
        type: "h3",
        texte: "🟣 PILIER 3 — Produits (Cash scalable)"
      },
      {
        type: "cal",
        emoji: "📦",
        texte: "Rôle : Scalabilité absolue et détachement du temps.",
        note: "Types : Formation stratégique, Template système, Checklist avancée.\nAvantages : Marge élevée, Indépendance, Autorité renforcée."
      }
    ]
  },
  {
    titre: "⚖️ 2️⃣ & 3️⃣ Répartition et Évolution",
    blocs: [
      {
        type: "h3",
        texte: "Objectif Année 1 (Équilibre court/moyen terme)"
      },
      {
        type: "cal",
        emoji: "📊",
        texte: "40 % Affiliation • 40 % Agency • 20 % Produits",
        note: "Pourquoi ?\nAffiliation = socle\nAgency = accélérateur\nProduit = futur"
      },
      {
        type: "h3",
        texte: "Objectif Année 3 (Scalabilité)"
      },
      {
        type: "cal",
        emoji: "🚀",
        texte: "30 % Affiliation • 30 % Agency • 40 % Produits",
        note: "Pourquoi ?\nProduit = liberté totale + scalabilité infinie."
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🧱 4️⃣ Synergie entre les 3 piliers (Effet Levier)",
    blocs: [
      {
        type: "p",
        texte: "Tout actif doit servir plusieurs objectifs."
      },
      {
        type: "cal",
        emoji: "📝",
        texte: "Un article SEO peut :",
        note: "→ Générer de l'affiliation\n→ Générer un lead Agency\n→ Nourrir une formation future"
      },
      {
        type: "cal",
        emoji: "🤝",
        texte: "Une mission Agency peut :",
        note: "→ Produire une étude de cas (Preuve)\n→ Inspirer un contenu SEO\n→ Tester un module de formation"
      },
      {
        type: "cal",
        emoji: "📦",
        texte: "Un produit digital peut :",
        note: "→ Qualifier les leads (Ceux qui achètent peuvent vouloir plus)\n→ Filtrer les demandes basiques\n→ Attirer des clients premium"
      }
    ]
  },
  {
    titre: "🎯 5️⃣ Exemple concret schoolsWP",
    blocs: [
      {
        type: "p",
        texte: "Un seul actif → 5 monétisations possibles."
      },
      {
        type: "cal",
        emoji: "✨",
        texte: "Article : “FluentCRM vs MailerLite”",
        note: "1. Affiliation FluentCRM\n2. Lead pour Audit CRM (Agency)\n3. Module pour formation “CRM WordPress stratégique”\n4. Base pour Vidéo YouTube\n5. Contenu Newsletter"
      }
    ]
  },
  {
    titre: "🔥 6️⃣ & 7️⃣ Stratégie d'exécution & Pièges",
    blocs: [
      {
        type: "h3",
        texte: "Séquençage des phases"
      },
      {
        type: "bul",
        items: [
          "Phase 1 : SEO + Affiliation + 1 offre Agency",
          "Phase 2 : Ajout 1 mini-produit (ex : système CRM)",
          "Phase 3 : Programme signature premium"
        ]
      },
      {
        type: "h3",
        texte: "⚠️ Pièges mortels à éviter"
      },
      {
        type: "cal",
        emoji: "🚫",
        texte: "NE PAS :",
        note: "Créer 5 formations trop tôt\nMultiplier les offres agency\nDiluer le positionnement"
      },
      {
        type: "cal",
        emoji: "✅",
        texte: "TOUJOURS :",
        note: "Garder un système cohérent\nAvoir un message clair\nBâtir une autorité forte"
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

  // Conclusion finale
  blocks.push(
    h2("🚀 Ce que ça donne dans 24 mois"),
    bul("Revenus récurrents affiliation"),
    bul("3–5 missions premium / mois"),
    bul("1 produit signature"),
    p(""),
    cal("👑", "Et surtout : Indépendance totale.", "Tu ne dépends plus des algorithmes ni des caprices d'un seul client.")
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

  console.log(`🎉 Terminé — Modèle de Revenu Hybride déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});