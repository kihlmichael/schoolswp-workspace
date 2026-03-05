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
  titre: "🏛️ Architecture Légale & Fiscale SASU",
  objectif: "Créer une structure propre, optimisée, scalable, alignée avec schoolsWP (média) et l'Agency WordPress premium. La SASU comme véhicule stratégique d’actifs.",
};

const SECTIONS = [
  {
    titre: "🏗 1️⃣ Architecture globale recommandée",
    blocs: [
      {
        type: "cal",
        emoji: "🏢",
        texte: "Option stratégique : SASU à l’IS (Impôt sur les Sociétés)"
      },
      {
        type: "p",
        texte: "Pourquoi ce choix ?"
      },
      {
        type: "bul",
        items: [
          "Séparation claire et étanche perso / pro",
          "Protection absolue de la responsabilité",
          "Optimisation fiscale par les dividendes",
          "Crédibilité B2B maximale face aux entreprises",
          "Compatible avec une croissance agence"
        ]
      }
    ]
  },
  {
    titre: "🧱 2️⃣ Répartition stratégique des activités",
    blocs: [
      {
        type: "h3",
        texte: "Les deux flux de revenus :"
      },
      {
        type: "num",
        items: [
          "Revenus média / affiliation (schoolsWP) : Affiliation plugins, Sponsoring, Produits digitaux.",
          "Revenus prestations (SASU Agency) : Audit, Structuration WordPress, Automatisation, Accompagnement."
        ]
      },
      {
        type: "cal",
        emoji: "🎯",
        texte: "Stratégie recommandée : TOUT CENTRALISER dans la SASU",
        note: "schoolsWP devient une marque commerciale hébergée par la SASU."
      },
      {
        type: "p",
        texte: "Avantages de la centralisation :"
      },
      {
        type: "bul",
        items: [
          "Simplification comptable (1 seul bilan)",
          "Image professionnelle unifiée",
          "Pas de conflit d'intérêts ou de requalification Micro / Société",
          "Possibilité de déduire 100% des outils (hébergement, SaaS, IA) sur le CA global"
        ]
      }
    ]
  }
];
const SECTIONS_PART_2 = [
  {
    titre: "💰 3️⃣ Optimisation fiscale intelligente",
    blocs: [
      {
        type: "h3",
        texte: "🧠 Schéma classique de rémunération"
      },
      {
        type: "bul",
        items: [
          "Année 1 : Rémunération faible ou nulle → Capitaliser la trésorerie → Optimiser les charges déductibles.",
          "Années suivantes : Salaire modéré (pour la protection sociale) + Complément en dividendes (flat tax)."
        ]
      },
      {
        type: "cal",
        emoji: "⚖️",
        texte: "Objectif de l'ingénierie financière :",
        note: "Minimiser les charges sociales tout en conservant une protection minimale et en maximisant le cash-flow réinvestissable."
      }
    ]
  },
  {
    titre: "🧾 4️⃣ Dépenses stratégiques déductibles",
    blocs: [
      {
        type: "p",
        texte: "Le grand avantage de la SASU pour ton activité tech :"
      },
      {
        type: "bul",
        items: [
          "Hébergements web & serveurs",
          "Plugins WordPress premium",
          "Outils SEO & Marketing",
          "API OpenAI / Outils IA",
          "Abonnements SaaS métiers",
          "Matériel informatique",
          "Formation (MSc, certifications)",
          "Déplacements professionnels"
        ]
      }
    ]
  },
  {
    titre: "🏢 5️⃣ Structure comptable (Dès le Jour 1)",
    blocs: [
      {
        type: "cal",
        emoji: "📋",
        texte: "La Checklist du Dirigeant Carré :"
      },
      {
        type: "bul",
        items: [
          "Compte bancaire pro dédié (Qonto, Shine, etc.)",
          "Outil comptable en ligne (Indy, Dougs, Pennylane)",
          "Facturation 100% automatisée",
          "Suivi KPI mensuel strict",
          "Provision systématique URSSAF / IS"
        ]
      }
    ]
  }
];
const SECTIONS_PART_3 = [
  {
    titre: "🔐 6️⃣ Protection stratégique",
    blocs: [
      {
        type: "p",
        texte: "Le B2B demande des process inattaquables :"
      },
      {
        type: "bul",
        items: [
          "RC Pro (Responsabilité Civile Professionnelle) obligatoire",
          "CGV solides adaptées aux prestations techniques",
          "Contrat de prestation type (avec clauses de limites de garantie)",
          "Clause de cession de propriété intellectuelle explicite",
          "Mentions d'affiliation transparentes sur schoolsWP"
        ]
      }
    ]
  },
  {
    titre: "📈 7️⃣ Vision à 3 ans",
    blocs: [
      {
        type: "cal",
        emoji: "🔭",
        texte: "La trajectoire corporate :"
      },
      {
        type: "num",
        items: [
          "Année 1 → Structuration et capitalisation",
          "Année 2 → Stabilisation des revenus récurrents",
          "Année 3 → Option Holding si la croissance l'exige"
        ]
      },
      {
        type: "p",
        texte: "Holding pertinente si : Multiples activités (agences séparées), Investissements immo/bourse, ou Revente potentielle."
      }
    ]
  },
  {
    titre: "⚠️ 8️⃣ Pièges à éviter (Checklist Mortelle)",
    blocs: [
      {
        type: "cal",
        emoji: "☠️",
        texte: "Les erreurs qui tuent les agences :",
        note: "1. Mélanger Micro-entreprise et SASU trop longtemps\n2. Se verser un salaire trop tôt (assécher la tréso)\n3. Sous-estimer les charges sociales futures\n4. Négliger la trésorerie de secours\n5. Multiplier les offres au lieu de scaler la Signature"
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

  // Conclusion finale forte
  blocks.push(
    h2("🎯 9️⃣ Stratégie cohérente avec ton profil"),
    p("Vu le média schoolsWP, l'approche système, et la volonté premium, la conclusion légale s'impose :"),
    cal("💎", "La SASU doit être pensée comme :", "« Un Véhicule Stratégique d’Actifs WordPress »\nPas juste une 'agence' ou un statut de freelance.")
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

  console.log(`🎉 Terminé — Architecture SASU déployée dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});