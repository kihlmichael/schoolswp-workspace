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

const PLAN = {
  titre: "📅 Plan Contenu B2B Détaillé — 6 Mois",
  objectif:
    "Installer l'autorité schoolsWP sur la niche Formateurs B2B + WordPress + Systèmes. Contenu chirurgical, stratégique, décisionnel — pas du contenu large.",
};

const MOIS = [
  {
    num: 1,
    cluster: 1,
    cluster_label: "LMS WordPress B2B",
    theme: "Pilier Fondamental",
    emoji: "🎯",
    pilier: {
      titre: "Comment structurer un LMS WordPress pour formateurs B2B",
      slug: "structurer-lms-wordpress-formateurs-b2b",
      intention: "informationnelle expert",
      priorite: "HAUTE",
    },
    satellites: [
      { titre: "Gérer plusieurs entreprises sur un LMS WordPress", intention: "informationnelle" },
      { titre: "Comptes groupe & gestion multi-apprenants", intention: "informationnelle" },
      { titre: "Sécuriser les accès formation entreprise", intention: "informationnelle" },
      { titre: "Reporting apprenant pour clients B2B", intention: "informationnelle" },
    ],
    decisionnel: {
      titre: "Quel LMS WordPress choisir pour formation entreprise ?",
      intention: "décisionnelle",
    },
    objectif_mois:
      "Capter toute la demande LMS B2B niveau entrée. Établir schoolsWP comme référence technique sur le sujet.",
  },
  {
    num: 2,
    cluster: 1,
    cluster_label: "LMS WordPress B2B",
    theme: "Architecture & Performance",
    emoji: "🏗",
    pilier: {
      titre: "Architecture idéale WordPress pour formation B2B",
      slug: "architecture-wordpress-formation-b2b",
      intention: "informationnelle expert",
      priorite: "HAUTE",
    },
    satellites: [
      { titre: "Tutor LMS pour formateurs B2B : avantages et limites", intention: "comparative" },
      {
        titre: "WooCommerce vs système externe pour facturation entreprise",
        intention: "comparative",
      },
      { titre: "Automatiser l'onboarding formation B2B", intention: "informationnelle" },
      { titre: "Gérer renouvellements & accès annuels", intention: "informationnelle" },
    ],
    decisionnel: {
      titre: "Tutor LMS vs plateforme SaaS pour formation B2B ?",
      intention: "comparative",
    },
    objectif_mois:
      "Approfondir l'architecture technique. Capter les comparateurs outillés (Tutor LMS vs SaaS).",
  },
  {
    num: 3,
    cluster: 1,
    cluster_label: "LMS WordPress B2B",
    theme: "Optimisation & Rentabilité",
    emoji: "💰",
    pilier: {
      titre: "Optimiser la rentabilité d'un LMS WordPress B2B",
      slug: "rentabilite-lms-wordpress-b2b",
      intention: "informationnelle expert",
      priorite: "HAUTE",
    },
    satellites: [
      { titre: "Upsell formation entreprise", intention: "informationnelle" },
      { titre: "Segmentation clients B2B", intention: "informationnelle" },
      { titre: "Automatisation email corporate", intention: "informationnelle" },
      { titre: "KPI formation entreprise", intention: "informationnelle" },
    ],
    decisionnel: {
      titre: "CRM WordPress pour formateurs B2B : lequel choisir ?",
      intention: "décisionnelle",
    },
    objectif_mois:
      "Capitaliser sur le Cluster 1. Pivot naturel vers le Cluster 2 (CRM) via l'article décisionnel.",
  },
  {
    num: 4,
    cluster: 2,
    cluster_label: "CRM & Automatisation B2B",
    theme: "CRM stratégique",
    emoji: "🧩",
    pilier: {
      titre: "Structurer un CRM WordPress pour formateurs B2B",
      slug: "crm-wordpress-formateurs-b2b",
      intention: "informationnelle expert",
      priorite: "HAUTE",
    },
    satellites: [
      { titre: "Segmentation entreprise dans FluentCRM", intention: "informationnelle" },
      { titre: "Pipeline devis B2B automatisé", intention: "informationnelle" },
      { titre: "Automatiser relances devis", intention: "informationnelle" },
      { titre: "Cycle de vente long B2B", intention: "informationnelle" },
    ],
    decisionnel: {
      titre: "FluentCRM vs HubSpot pour formateurs B2B",
      intention: "comparative",
    },
    objectif_mois:
      "Ouvrir le Cluster 2 avec un pilier fort. FluentCRM vs HubSpot = article décisionnel haute valeur.",
  },
  {
    num: 5,
    cluster: 2,
    cluster_label: "CRM & Automatisation B2B",
    theme: "Tunnel & Acquisition",
    emoji: "🎯",
    pilier: {
      titre: "Tunnel WordPress pour vendre des formations B2B",
      slug: "tunnel-wordpress-formation-b2b",
      intention: "informationnelle expert",
      priorite: "HAUTE",
    },
    satellites: [
      { titre: "Page offre corporate efficace", intention: "informationnelle" },
      { titre: "Formulaire qualification entreprise", intention: "informationnelle" },
      { titre: "Automatisation prise de rendez-vous", intention: "informationnelle" },
      { titre: "Intégration CRM + LMS", intention: "informationnelle" },
    ],
    decisionnel: {
      titre: "Faut-il un tunnel complexe pour vendre en B2B ?",
      intention: "décisionnelle",
    },
    objectif_mois:
      "Couvrir l'acquisition B2B de A à Z. L'article décisionnel brise une croyance forte (tunnel complexe).",
  },
  {
    num: 6,
    cluster: 2,
    cluster_label: "CRM & Automatisation B2B",
    theme: "Autorité & Scalabilité",
    emoji: "🚀",
    pilier: {
      titre: "Scaler une activité de formation B2B avec WordPress",
      slug: "scaler-formation-b2b-wordpress",
      intention: "informationnelle expert",
      priorite: "HAUTE",
    },
    satellites: [
      { titre: "Gestion multi-clients entreprise", intention: "informationnelle" },
      { titre: "Optimisation renouvellement contrat", intention: "informationnelle" },
      { titre: "Reporting stratégique client", intention: "informationnelle" },
      { titre: "Maintenance & support premium", intention: "informationnelle" },
    ],
    decisionnel: {
      titre: "WordPress est-il adapté au B2B à grande échelle ?",
      intention: "décisionnelle",
    },
    objectif_mois:
      "Clore le cycle avec un signal d'autorité maximum. L'article décisionnel répond à l'objection ultime.",
  },
];

const REPARTITION = [
  {
    pct: 40,
    label: "Informationnel expert",
    desc: "Piliers + satellites — autorité thématique profonde, indexation long terme",
    emoji: "📚",
  },
  {
    pct: 35,
    label: "Comparative",
    desc: "Outils, plugins, plateformes — attirer les décideurs en phase de recherche active",
    emoji: "⚖️",
  },
  {
    pct: 25,
    label: "Décisionnel fort",
    desc: "Articles d'achat / choix — convertir les prospects chauds en leads qualifiés",
    emoji: "💰",
  },
];

const OPTIMISATION_CONTINUE = [
  "Audit mensuel Search Console — identifier les articles proches du top 3 pour quick win",
  "Enrichissement piliers chaque trimestre : exemples clients réels, données chiffrées, FAQ AIO",
  "Maillage interne progressif : chaque article linke vers son pilier + 2 satellites existants",
  "Mise à jour des comparatifs si contexte outils change (Tutor LMS, FluentCRM, WooCommerce)",
  "Monitoring GEO/AIO via Thruuu : vérifier la présence dans les réponses IA sur requêtes pilier",
];

const CTA_SOFT = {
  texte:
    "Tu formes des entreprises et ton système WordPress devient complexe ? Je propose un audit stratégique spécialisé B2B.",
  url: "schoolswp.com/audit-b2b",
  placement:
    "Fin d'article — après 'Pour aller plus loin', jamais en ouverture, jamais en milieu de développement.",
};

const RESULTATS = [
  "2 clusters thématiques forts — LMS B2B + CRM & Automatisation",
  "36 contenus planifiés : 6 piliers + 24 satellites + 6 articles décisionnels",
  "Autorité perçue = référence WordPress pour formateurs B2B",
  "Leads ultra qualifiés via /audit-b2b — formulaire éliminatoire 3 critères",
  "Positionnement unique : architecte système WordPress B2B",
];

// Computed stats
const total_piliers = MOIS.length;
const total_satellites = MOIS.reduce((a, m) => a + m.satellites.length, 0);
const total_decisionnels = MOIS.length;
const total_articles = total_piliers + total_satellites + total_decisionnels;

// ════════════════════════════════════════════════════════
//  BLOCK BUILDERS
// ════════════════════════════════════════════════════════

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text, link: opts.url ? { url: opts.url } : null },
  annotations: {
    bold: !!opts.bold,
    italic: !!opts.italic,
    code: !!opts.code,
    color: opts.color || "default",
  },
});

const h1 = (text) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(text)] } });
const h2 = (text) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(text)] } });
const h3 = (text) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(text)] } });

const p = (...parts) => ({
  object: "block",
  type: "paragraph",
  paragraph: { rich_text: parts.flat() },
});

const bul = (...parts) => ({
  object: "block",
  type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.flat() },
});

const num = (...parts) => ({
  object: "block",
  type: "numbered_list_item",
  numbered_list_item: { rich_text: parts.flat() },
});

const div = () => ({ object: "block", type: "divider", divider: {} });

const cal = (emoji, ...parts) => ({
  object: "block",
  type: "callout",
  callout: { rich_text: parts.flat(), icon: { type: "emoji", emoji } },
});

const qot = (...parts) => ({
  object: "block",
  type: "quote",
  quote: { rich_text: parts.flat() },
});

// ════════════════════════════════════════════════════════
//  TEMPLATE BUILDER
// ════════════════════════════════════════════════════════

function buildTemplate() {
  const blocks = [];

  // ── HEADER ──────────────────────────────────────────
  blocks.push(
    cal("📌", rt("Objectif : ", { bold: true }), rt(PLAN.objectif)),
    p(
      rt(`📊 ${total_articles} contenus planifiés`, { bold: true }),
      rt(
        ` — ${total_piliers} piliers · ${total_satellites} satellites · ${total_decisionnels} décisionnels`
      )
    ),
    p(
      rt("🗓 Durée : ", { bold: true }),
      rt("6 mois  "),
      rt("  |  🗺 Clusters : ", { bold: true }),
      rt("2  "),
      rt("  |  📚 1 pilier / mois  "),
      rt("  |  🧩 4 satellites / mois  "),
      rt("  |  💰 1 décisionnel / mois")
    ),
    div()
  );

  // ── CALENDRIER SYNTHÉTIQUE ──────────────────────────
  blocks.push(h2("📅 Calendrier de production synthétique"));

  for (const m of MOIS) {
    const clusterEmoji = m.cluster === 1 ? "🗺" : "⚙️";
    blocks.push(
      cal(
        m.emoji,
        rt(`Mois ${m.num} — ${m.theme}  `, { bold: true }),
        rt(`[${clusterEmoji} Cluster ${m.cluster} : ${m.cluster_label}]`, { italic: true }),
        rt(`\nPilier : `),
        rt(m.pilier.titre, { bold: true }),
        rt(
          `\n${m.satellites.length} satellites · Décisionnel : ${m.decisionnel.titre}`
        )
      )
    );
  }

  blocks.push(div());

  // ── CLUSTERS ────────────────────────────────────────
  const clusters = [
    {
      num: 1,
      label: "🗺 CLUSTER 1 — LMS WordPress B2B",
      periode: "Mois 1–3",
      desc: "Devenir la référence technique LMS pour formateurs qui vendent aux entreprises. Couvrir toute la chaîne : architecture → performance → rentabilité.",
    },
    {
      num: 2,
      label: "⚙️ CLUSTER 2 — CRM & Automatisation B2B",
      periode: "Mois 4–6",
      desc: "Asseoir l'autorité sur l'architecture systèmes : CRM, tunnels d'acquisition, scalabilité. Répondre aux objections des décideurs.",
    },
  ];

  for (const cluster of clusters) {
    const moisCluster = MOIS.filter((m) => m.cluster === cluster.num);

    blocks.push(
      h2(`${cluster.label} (${cluster.periode})`),
      p(rt(cluster.desc, { italic: true })),
      p()
    );

    for (const mois of moisCluster) {
      // Month header
      blocks.push(h3(`${mois.emoji} Mois ${mois.num} — ${mois.theme}`));

      // Objectif mois
      blocks.push(
        p(rt("🎯 Objectif : ", { bold: true }), rt(mois.objectif_mois, { italic: true }))
      );

      // Pilier callout
      blocks.push(
        cal(
          "📌",
          rt("PILIER — ", { bold: true, color: "blue" }),
          rt(mois.pilier.titre, { bold: true })
        ),
        p(
          rt("Slug : ", { bold: true }),
          rt(`/${mois.pilier.slug}`, { code: true }),
          rt("  |  Intention : ", { bold: true }),
          rt(mois.pilier.intention),
          rt("  |  Priorité : ", { bold: true }),
          rt(mois.pilier.priorite, { color: "red", bold: true })
        )
      );

      // Satellites header
      blocks.push(p(rt(`🧩 Satellites (${mois.satellites.length}) :`, { bold: true })));

      for (const sat of mois.satellites) {
        blocks.push(
          bul(
            rt(sat.titre),
            rt(`  — `, { color: "gray" }),
            rt(sat.intention, { italic: true, color: "gray" })
          )
        );
      }

      // Décisionnel callout
      blocks.push(
        p(),
        cal(
          "💰",
          rt("DÉCISIONNEL — ", { bold: true, color: "orange" }),
          rt(mois.decisionnel.titre)
        ),
        p(
          rt("Intention : ", { bold: true }),
          rt(mois.decisionnel.intention),
          rt(
            "  |  Cible : prospect en phase de choix final — conversion directe vers /audit-b2b",
            { italic: true, color: "gray" }
          )
        ),
        div()
      );
    }
  }

  // ── RÉPARTITION INTENTION ────────────────────────────
  blocks.push(h2("📈 Répartition Intention (sur 6 mois)"));
  blocks.push(
    p(
      rt(
        "Équilibre stratégique entre autorité long terme, capture décisionnelle et comparatifs outils.",
        { italic: true }
      )
    )
  );

  for (const r of REPARTITION) {
    blocks.push(
      bul(
        rt(`${r.emoji} ${r.pct}% — `, { bold: true }),
        rt(r.label, { bold: true }),
        rt(` : ${r.desc}`)
      )
    );
  }

  blocks.push(div());

  // ── OPTIMISATION CONTINUE ────────────────────────────
  blocks.push(
    h2("🔁 Optimisation continue"),
    p(
      rt(
        "Publication ≠ fin. Chaque article entre dans un cycle d'amélioration trimestriel :",
        { italic: true }
      )
    )
  );

  for (const item of OPTIMISATION_CONTINUE) {
    blocks.push(bul(rt(item)));
  }

  blocks.push(div());

  // ── INTÉGRATION AGENCY ───────────────────────────────
  blocks.push(
    h2("💼 Intégration Agency — CTA Soft"),
    p(
      rt(
        "Chaque pilier et chaque article décisionnel inclut un bloc CTA non intrusif :",
        { italic: true }
      )
    ),
    cal("🔥", rt(CTA_SOFT.texte, { bold: true })),
    p(rt("URL cible : ", { bold: true }), rt(CTA_SOFT.url, { code: true })),
    p(rt("Placement : ", { bold: true }), rt(CTA_SOFT.placement)),
    qot(
      rt(
        "Règle d'or : le CTA est utile, pas commercial. Il propose — il n'interrompt pas.",
        { italic: true }
      )
    ),
    div()
  );

  // ── RÉSULTATS ────────────────────────────────────────
  blocks.push(
    h2("🏆 Ce que ça donne à 6 mois"),
    p(rt("En publiant et optimisant ce plan de façon constante :", { italic: true }))
  );

  for (const r of RESULTATS) {
    blocks.push(bul(rt("✅ "), rt(r)));
  }

  blocks.push(
    p(),
    cal(
      "🚀",
      rt("Positionnement final : ", { bold: true }),
      rt(
        "schoolsWP = architecte système WordPress B2B. La référence technique pour les formateurs qui vendent sérieusement aux entreprises."
      )
    ),
    p(),
    cal(
      "📊",
      rt(`${total_articles} contenus planifiés`, { bold: true }),
      rt(
        ` — ${total_piliers} piliers fondateurs · ${total_satellites} satellites ciblés · ${total_decisionnels} articles décisionnels à fort potentiel de conversion`
      )
    )
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

  console.log(`📄 Création page : ${PLAN.titre}`);
  console.log(`📦 ${allBlocks.length} blocs → ${chunks.length} batch(es)`);

  // Create page with first chunk
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: NOTION_PARENT_PAGE_ID },
    properties: {
      title: { title: [{ text: { content: PLAN.titre } }] },
    },
    children: chunks[0],
  });

  console.log(`✅ Page créée : ${page.url}`);

  // Append remaining chunks
  for (let i = 1; i < chunks.length; i++) {
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${page.id}/children`, { children: chunks[i] });
    console.log(`  ↳ Batch ${i + 1}/${chunks.length} envoyé`);
  }

  console.log(`\n🎉 Terminé — Plan contenu B2B 6 mois créé dans Notion`);
  console.log(
    `📊 ${total_articles} articles planifiés : ${total_piliers} piliers + ${total_satellites} satellites + ${total_decisionnels} décisionnels`
  );
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
