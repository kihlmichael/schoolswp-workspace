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
  titre: "📅 Plan LinkedIn 30 jours — Domination Formateurs B2B",
  objectif: "Installer ton positionnement → Générer des conversations qualifiées → Amener vers l'Audit B2B → Poser ton autorité sur l'architecture système.",
};

const KPI = [
  "8–12 conversations qualifiées",
  "4–8 appels stratégiques",
  "1–3 clients potentiels",
  "Positionnement clair d'Architecte Système installé"
];

const STRUCTURE_POST = [
  "1. Ligne courte punch (Hook)",
  "2. Problème concret (Friction client)",
  "3. Explication claire (Pourquoi ça bloque)",
  "4. Insight stratégique (Le changement de paradigme)",
  "5. Mini solution (La piste de l'architecture)",
  "6. Question ou CTA léger (Ouverture conversation)"
];

const WEEKS = [
  {
    titre: "SEMAINE 1 — Positionnement & Problème",
    posts: [
      {
        num: 1,
        sujet: "Le problème des formateurs B2B n’est pas leur contenu. C’est leur architecture.",
        details: "Angle : LMS mal structuré, CRM absent, Onboarding manuel, Pas scalable.",
        cta: "« Votre système est-il pensé pour gérer 10 entreprises ? »"
      },
      {
        num: 2,
        sujet: "Pourquoi un LMS seul ne suffit pas en B2B",
        details: "Expliquer : Gestion multi-comptes, Reporting entreprise, Automatisation onboarding.",
        cta: "« Comment gérez-vous vos clients corporate aujourd’hui ? »"
      },
      {
        num: 3,
        sujet: "Ce que j’ai corrigé chez un formateur B2B cette semaine (Mini étude de cas)",
        details: "Structure : Problème → Correction → Résultat.",
        cta: "Ouverture sur l'importance d'auditer son système."
      }
    ]
  },
  {
    titre: "SEMAINE 2 — Méthode & Architecture",
    posts: [
      {
        num: 4,
        sujet: "L’architecture WordPress idéale pour un formateur B2B (Visuel)",
        details: "Décrire : LMS + CRM + Tunnel + Automatisation.",
        cta: "Inciter à sauvegarder le post pour référence."
      },
      {
        num: 5,
        sujet: "3 erreurs techniques qui bloquent les formateurs B2B",
        details: "Exemples : Pas de segmentation entreprise, Pas d’automatisation, Pas de pipeline clair.",
        cta: "Demander laquelle des 3 erreurs ils rencontrent."
      },
      {
        num: 6,
        sujet: "Je ne crée pas des sites WordPress. Je structure des systèmes business.",
        details: "Développer : Positionnement différenciant. La différence entre un site vitrine et une machine de vente B2B.",
        cta: "Affirmer son autorité."
      }
    ]
  },
  {
    titre: "SEMAINE 3 — Autorité & Preuve",
    posts: [
      {
        num: 7,
        sujet: "SaaS externe vs WordPress structuré en B2B",
        details: "Angle business : Contrôle, Données, Scalabilité, Coûts cachés.",
        cta: "Lancer le débat en commentaires."
      },
      {
        num: 8,
        sujet: "Pourquoi vos entreprises clientes ne renouvellent pas",
        details: "Lien caché : Expérience apprenant, Reporting inexistant, Automatisation faible.",
        cta: "Mettre le doigt sur la douleur de la rétention."
      },
      {
        num: 9,
        sujet: "La segmentation que 90 % des formateurs B2B ignorent",
        details: "Insight CRM : Séparer les décideurs RH des apprenants dans la base de données.",
        cta: "Inviter à évaluer sa propre base."
      }
    ]
  },
  {
    titre: "SEMAINE 4 — Conversion subtile",
    posts: [
      {
        num: 10,
        sujet: "Test rapide : votre architecture WordPress est-elle prête pour le B2B ?",
        details: "Format : Checklist simple (5 points clés).",
        cta: "Demander leur score sur 5 en commentaires."
      },
      {
        num: 11,
        sujet: "Un formateur B2B rentable a besoin d’un système, pas d’un site.",
        details: "Vision long terme : La tech au service de la croissance, pas l'inverse.",
        cta: "Préparer le terrain pour l'offre."
      },
      {
        num: 12,
        sujet: "Si vous vendez des formations aux entreprises...",
        details: "Pitch direct mais éducatif.",
        cta: "« Je propose un audit stratégique WordPress B2B. Objectif : identifier les points de blocage structurels. DM pour en parler. »"
      }
    ]
  }
];

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
const p = (...parts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: parts.flat() } });
const bul = (...parts) => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: parts.flat() } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (emoji, ...parts) => ({ object: "block", type: "callout", callout: { rich_text: parts.flat(), icon: { type: "emoji", emoji } } });

// ════════════════════════════════════════════════════════
//  TEMPLATE BUILDER
// ════════════════════════════════════════════════════════

function buildTemplate() {
  const blocks = [];

  // Header & Objectifs
  blocks.push(
    cal("🎯", rt("Objectif du plan : ", { bold: true }), rt(PAGE.objectif)),
    p()
  );

  blocks.push(h3("📊 Objectifs fin des 30 jours :"));
  for (const kpi of KPI) {
    blocks.push(bul(rt(kpi, { bold: true, color: "blue" })));
  }
  blocks.push(div());

  // Structure type
  blocks.push(h3("🏗️ Structure type d'un post performant :"));
  const structureBlocks = STRUCTURE_POST.map(s => rt(s + "\n"));
  blocks.push(cal("💡", ...structureBlocks));
  blocks.push(div());

  // Boucle sur les semaines
  for (const week of WEEKS) {
    blocks.push(h2(`🗓️ ${week.titre}`));
    
    for (const post of week.posts) {
      blocks.push(
        h3(`🔹 Post ${post.num} — ${post.sujet}`),
        p(rt("Détails : ", { bold: true }), rt(post.details, { color: "gray" })),
        p(rt("CTA / Question : ", { bold: true }), rt(post.cta, { italic: true })),
        cal("✍️", rt("Rédige ton post ici...", { color: "gray", italic: true })),
        p()
      );
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

  console.log(`🎉 Terminé — Plan de 30 jours (12 posts) déployé dans Notion.`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});