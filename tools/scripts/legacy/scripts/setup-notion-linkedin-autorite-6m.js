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
  titre: "🏆 Stratégie Autorité LinkedIn — 6 Mois",
  objectif: "Objectif : Leads premium, pas visibilité vanity. Influence ciblée, pas 'créateur de contenu'. Devenir l'autorité B2B.",
};

const SECTIONS = [
  {
    titre: "🟢 MOIS 1 — Clarté & Signal Fort",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif : Être immédiatement identifiable comme spécialiste."
      },
      {
        type: "h3",
        texte: "Actions & Contenus"
      },
      {
        type: "bul",
        items: [
          "Optimisation profil complète (titre + bannière + résumé)",
          "12 posts (3/semaine) : Problèmes B2B, Architecture LMS, Erreurs",
          "Hooks tranchés, ton pédagogique, zéro jargon, zéro 'tips génériques'"
        ]
      },
      {
        type: "p",
        texte: "👉 Résultat attendu : Créer une perception de spécialisation immédiate."
      }
    ]
  },
  {
    titre: "🔵 MOIS 2 — Profondeur & Méthode",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif : Montrer que tu as une vraie approche structurée."
      },
      {
        type: "h3",
        texte: "Actions & Contenus"
      },
      {
        type: "bul",
        items: [
          "Décomposer ton architecture type",
          "Expliquer la segmentation CRM B2B",
          "Montrer la logique d'onboarding entreprise",
          "Utiliser des visuels simples (schémas architecture)"
        ]
      },
      {
        type: "p",
        texte: "👉 Résultat attendu : Construire la crédibilité technique et méthodologique."
      }
    ]
  },
  {
    titre: "🟣 MOIS 3 — Preuve & Légitimité",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif : Introduire la preuve sociale et les cas réels."
      },
      {
        type: "h3",
        texte: "Actions & Contenus"
      },
      {
        type: "bul",
        items: [
          "Étude de cas anonymisée",
          "Avant / Après d'architecture",
          "Erreur technique corrigée chez un client",
          "Résultat concret obtenu"
        ]
      },
      {
        type: "p",
        texte: "👉 Résultat attendu : Passer du discours théorique à la démonstration pratique."
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "🟡 MOIS 4 — Diagnostic & Conversation",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif : Transformer l'audience passive en conversations DM."
      },
      {
        type: "h3",
        texte: "Actions & Contenus"
      },
      {
        type: "bul",
        items: [
          "Posts orientés diagnostic : 'Si votre LMS ne gère pas X, vous avez un problème.'",
          "Posts d'alerte : 'Voici 3 signaux que votre CRM B2B est mal structuré.'",
          "Call to Action Soft : 'Si vous voulez savoir si votre architecture tient la route, envoyez-moi ARCHI.'"
        ]
      },
      {
        type: "p",
        texte: "👉 Résultat attendu : Générer des DM entrants naturels et qualifiés."
      }
    ]
  },
  {
    titre: "🟠 MOIS 5 — Positionnement Premium",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif : Assumer ton prix, ton niveau, et filtrer."
      },
      {
        type: "h3",
        texte: "Actions & Contenus"
      },
      {
        type: "bul",
        items: [
          "Démonter le low-cost : 'Pourquoi les projets LMS à 1 500 € sont mal conçus.'",
          "Démontrer la complexité : 'Pourquoi un système B2B demande une vraie réflexion.'",
          "Chiffrer l'erreur : 'Pourquoi l’automatisation mal faite coûte très cher à long terme.'"
        ]
      },
      {
        type: "p",
        texte: "👉 Résultat attendu : Filtrer drastiquement les prospects à bas budget."
      }
    ]
  },
  {
    titre: "🔴 MOIS 6 — Autorité Installée",
    blocs: [
      {
        type: "cal",
        emoji: "🎯",
        texte: "Objectif : Être perçu comme LA référence de la niche."
      },
      {
        type: "h3",
        texte: "Actions & Contenus"
      },
      {
        type: "bul",
        items: [
          "Thread / Carrousel long format très stratégique",
          "Mini-guide PDF offert via LinkedIn",
          "Analyse détaillée d'une architecture complexe",
          "Partage de ta vision sur le futur des LMS B2B"
        ]
      },
      {
        type: "p",
        texte: "👉 Résultat attendu : Ancrer définitivement le statut d’expert incontournable."
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

  // KPIs & Règle d'or
  blocks.push(
    h2("📊 KPI Visés (à 6 mois)"),
    bul("1 500 – 5 000 abonnés ultra-ciblés"),
    bul("10 – 20 conversations qualifiées / mois"),
    bul("3 – 5 appels stratégiques / mois"),
    bul("1 – 3 projets signés / mois"),
    p(""),
    div(),
    h2("🔥 La Règle d’Or du Contenu"),
    cal("🚫", "NE JAMAIS :", "Poster sur du WordPress générique\nDonner des astuces techniques basiques\nParler d'un plugin sans contexte business"),
    cal("✅", "TOUJOURS :", "Parler de système\nParler d'architecture globale\nParler de rentabilité\nParler de structuration")
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

  console.log(`🎉 Terminé — Stratégie Autorité LinkedIn 6 Mois déployée dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});