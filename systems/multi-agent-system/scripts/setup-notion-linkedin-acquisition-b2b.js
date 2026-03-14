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
  titre: "🔗 Stratégie LinkedIn Acquisition B2B — schoolsWP Agency",
  objectif:
    "Générer des leads qualifiés · Installer l'autorité architecte système · Pré-vendre l'audit B2B. Niche : formateurs B2B. ADN : clair, structuré, zéro bullshit.",
};

const POSITIONNEMENT = {
  titre_profil:
    "Architecte de systèmes WordPress B2B | LMS • CRM • Automatisation | J'aide les formateurs à structurer un écosystème rentable",
  banniere: {
    message: "Structurer votre système WordPress B2B\nLMS • CRM • Automatisation • Scalabilité",
    cta: "👉 Audit stratégique B2B",
    url: "schoolswp.com/audit-b2b",
  },
  logique:
    "Titre : clair, spécifique, pas générique. Chaque mot porte un signal. LMS + CRM + Automatisation = trifecta B2B. 'Architecte' positionne en tant que métier, pas prestataire.",
};

const PILIERS = [
  {
    num: 1,
    couleur: "🟢",
    nom: "Problèmes B2B réels",
    objectif: "Faire réfléchir · Créer tension · Montrer expertise",
    logique:
      "Le lecteur se reconnaît dans le problème. Il ne savait pas qu'il avait ce problème. Tu viens de te positionner comme celui qui le voit.",
    exemples: [
      "Votre LMS WordPress n'est pas conçu pour gérer 10 entreprises.",
      "Le vrai problème des formateurs B2B n'est pas le LMS, c'est le CRM.",
      "Pourquoi votre tunnel B2B WordPress bloque vos ventes ?",
      "Vous avez un LMS. Pas un système. C'est pour ça que ça freine.",
      "3 signaux que votre architecture WordPress n'est pas prête pour le B2B.",
    ],
    trigger_psychologique:
      "Inconfort productif : le prospect réalise qu'il a un angle mort. Réaction naturelle = en savoir plus.",
  },
  {
    num: 2,
    couleur: "🔵",
    nom: "Architecture & méthode",
    objectif: "Montrer profondeur · Montrer méthode · Crédibilité technique",
    logique:
      "Tu ne parles pas de toi. Tu expliques une logique. Le lecteur apprend quelque chose de concret. Il commence à voir que tu maîtrises ce sujet mieux que quiconque dans son réseau.",
    exemples: [
      "Voici l'architecture WordPress que j'utilise pour les formateurs B2B.",
      "Comment structurer un onboarding entreprise automatisé.",
      "La segmentation CRM que 90 % des formateurs ignorent.",
      "Architecture LMS B2B : les 4 couches que personne ne montre.",
      "Mon process pour auditer un système WordPress B2B en 2h.",
    ],
    trigger_psychologique:
      "Autorité par la méthode : le prospect comprend qu'il lui manque une vision systémique. Réaction = sauvegarder le post, partager, DM.",
  },
  {
    num: 3,
    couleur: "🟣",
    nom: "Études de cas & retours terrain",
    objectif: "Preuve sociale · Concret · Autorité",
    logique:
      "Tu ne parles plus de théorie. Tu montres ce que tu as fait. Le lecteur se projette. Il se demande si son propre système a les mêmes lacunes.",
    exemples: [
      "Comment un formateur B2B a automatisé son onboarding en 3 semaines.",
      "Avant / Après : architecture LMS B2B restructurée.",
      "3 erreurs que j'ai corrigées chez un client formation entreprise.",
      "Ce que j'ai trouvé lors d'un audit WordPress B2B — et comment on l'a corrigé.",
      "Résultat client : 0 → 12 entreprises gérées sur un seul LMS WordPress.",
    ],
    trigger_psychologique:
      "Preuve par l'exemple : le prospect visualise le résultat. La transformation est tangible. Réaction = DM ou formulaire /audit-b2b.",
  },
];

const RYTHME = {
  posts_semaine: 3,
  jours: [
    {
      jour: "Lundi",
      type: "Problème B2B",
      pilier: 1,
      logique: "Début de semaine : créer une tension utile. Le prospect commence sa semaine avec une question qu'il n'avait pas.",
    },
    {
      jour: "Mercredi",
      type: "Architecture & méthode",
      pilier: 2,
      logique: "Milieu de semaine : l'engagement est fort. Le post technique tire vers le haut la crédibilité perçue.",
    },
    {
      jour: "Vendredi",
      type: "Cas réel / insight terrain",
      pilier: 3,
      logique: "Fin de semaine : le cas concret clôture le cycle. Réactions émotionnelles + sauvegardes = meilleure portée.",
    },
  ],
  note: "3 posts / semaine suffisent. La régularité prime sur le volume. Mieux vaut 3 posts de qualité qu'un flux quotidien de contenu creux.",
};

const DM_PROCESS = {
  principe: "Ne pas spammer. Le DM arrive après une interaction réelle. C'est un prolongement naturel de la conversation.",
  etapes: [
    { num: 1, action: "Publier contenu utile", detail: "Le contenu attire les bonnes personnes dans ton réseau." },
    { num: 2, action: "Identifier les formateurs B2B actifs", detail: "Chercher : 'formateur B2B', 'formation entreprise', 'LMS entreprise' dans les profils + commentaires." },
    { num: 3, action: "Commentaires stratégiques sur leurs posts", detail: "Commentaire pertinent, pas générique. Ajouter une valeur réelle. Objectif : être remarqué avant le DM." },
    { num: 4, action: "DM naturel après 2–3 interactions", detail: "Le contexte est posé. Le DM n'arrive pas de nulle part." },
    { num: 5, action: "Pas de vente — diagnostic", detail: "Proposer une perspective, pas une offre. L'objectif = obtenir un appel de 20 min." },
  ],
  dm_template: {
    objet: "DM post-interaction — formateur B2B",
    message:
      "Bonjour [Prénom],\n\nJ'ai vu que tu proposes des formations en entreprise — super positionnement.\n\nJ'ai une question directe : ton architecture WordPress est-elle pensée pour gérer plusieurs clients corporate en parallèle ?\n\nC'est souvent là que ça bloque, sans qu'on sache vraiment pourquoi.\n\nSi tu veux qu'on regarde ça ensemble en 20 min, je suis dispo — sans engagement.",
    ton: "Direct, pas vendeur. Curiosité sincère. Proposer — pas forcer.",
    regle: "Jamais en premier message. Toujours après au moins une interaction publique.",
  },
};

const POST_STRUCTURE = {
  principe: "Chaque post suit une mécanique précise. La structure fait 80 % du travail.",
  elements: [
    { num: 1, nom: "Hook fort", detail: "1 ligne. Provoque, interpelle, ou contre-intuitif. Doit stopper le scroll.", exemple: "Votre LMS WordPress n'est pas fait pour le B2B." },
    { num: 2, nom: "Problème clair", detail: "2–3 lignes. Le lecteur se reconnaît.", exemple: "La plupart des formateurs ont un outil. Pas un système. Et c'est pour ça que tout freine dès qu'on passe à 3 entreprises clientes." },
    { num: 3, nom: "Explication simple", detail: "Pas de jargon. Structure logique. Une idée par ligne.", exemple: "Un LMS B2B, c'est :\n→ Des accès isolés par entreprise\n→ Un reporting client par compte\n→ Une facturation automatisée" },
    { num: 4, nom: "Insight expert", detail: "La chose que seul quelqu'un qui a fait ce travail peut dire.", exemple: "90 % des problèmes que je vois viennent du CRM — pas du LMS." },
    { num: 5, nom: "Mini solution ou principe", detail: "Donner une valeur concrète. Pas la solution complète.", exemple: "La première chose à structurer : la segmentation entreprise dans FluentCRM." },
    { num: 6, nom: "Question ouverte", detail: "Invite à réagir. Ouvre la conversation.", exemple: "Est-ce que ton système actuel peut gérer 10 entreprises demain ?" },
  ],
  longueur_ideale: "150–300 mots. Jamais sous 100, jamais au-dessus de 500 sauf cas étude.",
  format: "Une idée par ligne. Retours à la ligne fréquents. Pas de paragraphes lourds.",
};

const KPIS = [
  {
    metrique: "Taux d'engagement",
    objectif: "> 3 %",
    calcul: "(Likes + commentaires + partages) / impressions × 100",
    alerte: "< 1.5 % = problème de hook ou de niche ciblée",
    frequence: "Par post",
  },
  {
    metrique: "Conversations qualifiées / semaine",
    objectif: "3 à 5",
    calcul: "DM reçus de formateurs B2B ayant un contexte WordPress",
    alerte: "< 1 / semaine = contenu trop générique ou rythme insuffisant",
    frequence: "Hebdomadaire",
  },
  {
    metrique: "Appels stratégiques / semaine",
    objectif: "1 à 2",
    calcul: "Appels de 20–30 min pré-audit acceptés",
    alerte: "< 1 / 2 semaines = script DM à revoir ou audience à recalibrer",
    frequence: "Hebdomadaire",
  },
  {
    metrique: "Closing / mois",
    objectif: "1 minimum",
    calcul: "Mission signée issue du canal LinkedIn",
    alerte: "0 closing en 2 mois = pipeline à auditer (hook → DM → appel → offre)",
    frequence: "Mensuel",
  },
];

const TUNNEL = [
  {
    etape: 1,
    label: "Post LinkedIn",
    role: "Capter l'attention, créer la tension, positionner l'expertise",
    conversion: "Impression → Engagement (like, commentaire, sauvegarde)",
  },
  {
    etape: 2,
    label: "Profil optimisé",
    role: "Convertir le curieux en prospect. Le profil est le landing page.",
    conversion: "Visite profil → Intérêt qualifié",
  },
  {
    etape: 3,
    label: "Audit B2B (/audit-b2b)",
    role: "Qualifier automatiquement. Seuls les prospects sérieux remplissent le formulaire.",
    conversion: "Intérêt → Demande qualifiée",
  },
  {
    etape: 4,
    label: "Appel stratégique",
    role: "Comprendre le contexte, confirmer le fit, poser les bases de la proposition.",
    conversion: "Demande → RDV (20–30 min)",
  },
  {
    etape: 5,
    label: "Proposition premium",
    role: "Phase 1 Audit (1 200–2 000 €) ou Full System™ selon maturité.",
    conversion: "RDV → Mission signée",
  },
];

const DIFFERENCIATION = {
  principe:
    "Tu ne vends pas un outil. Tu vends une structure. Tu ne parles pas de plugins. Tu parles d'architecture.",
  ne_pas_dire: [
    "Plugin X est super.",
    "Tutor LMS est le meilleur LMS WordPress.",
    "FluentCRM est moins cher que HubSpot.",
    "Je développe des sites WordPress.",
    "Je peux vous aider avec votre LMS.",
  ],
  dire_a_la_place: [
    "Voici pourquoi votre architecture WordPress limite votre croissance B2B.",
    "Un LMS sans CRM aligné, c'est un moteur sans transmission.",
    "FluentCRM n'est pas un outil moins cher — c'est un outil différemment positionné.",
    "Je structure des systèmes WordPress pour que les formateurs puissent gérer 20 entreprises sans chaos.",
    "Mon rôle : architecte système — pas développeur.",
  ],
  formule: "Problème d'architecture > Comparaison d'outils > Promesse générique.",
  positionnement_final:
    "schoolsWP Agency = le seul interlocuteur qui comprend à la fois le LMS, le CRM, l'automatisation ET la réalité business du formateur B2B.",
};

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
    cal("📌", rt("Objectif : ", { bold: true }), rt(PAGE.objectif)),
    p(
      rt("Niche : ", { bold: true }), rt("Formateurs B2B  "),
      rt("  |  Positionnement : ", { bold: true }), rt("Architecte WordPress système  "),
      rt("  |  ADN : ", { bold: true }), rt("Clair · Structuré · Zéro bullshit")
    ),
    div()
  );

  // ── 1. POSITIONNEMENT ───────────────────────────────
  blocks.push(
    h2("🧠 1️⃣ Positionnement LinkedIn — Fondation obligatoire"),
    p(rt("Le profil est le landing page. Chaque visite doit convertir le curieux en prospect.", { italic: true })),
    p()
  );

  // Titre profil
  blocks.push(
    h3("🎯 Titre optimisé"),
    cal("✏️", rt(POSITIONNEMENT.titre_profil, { bold: true })),
    p(rt("Logique : ", { bold: true }), rt(POSITIONNEMENT.logique))
  );

  // Bannière
  blocks.push(
    h3("📸 Bannière"),
    cal(
      "🖼",
      rt("Message principal : ", { bold: true }),
      rt(POSITIONNEMENT.banniere.message),
      rt("\nCTA : ", { bold: true }),
      rt(POSITIONNEMENT.banniere.cta),
      rt("  →  ", { color: "gray" }),
      rt(POSITIONNEMENT.banniere.url, { code: true })
    ),
    div()
  );

  // ── 2. PILIERS ───────────────────────────────────────
  blocks.push(
    h2("🧱 2️⃣ Stratégie de contenu — 3 piliers"),
    p(rt("Tu ne publies pas au hasard. Chaque post appartient à un pilier. Chaque pilier a un rôle précis dans le tunnel.", { italic: true })),
    p()
  );

  for (const pilier of PILIERS) {
    blocks.push(
      h3(`${pilier.couleur} Pilier ${pilier.num} — ${pilier.nom}`)
    );

    blocks.push(
      cal("🎯", rt("Objectif : ", { bold: true }), rt(pilier.objectif)),
      p(rt("Logique : ", { bold: true }), rt(pilier.logique, { italic: true })),
      p(rt("Exemples de posts :", { bold: true }))
    );

    for (const ex of pilier.exemples) {
      blocks.push(bul(rt("→ ", { color: "gray" }), rt(`"${ex}"`)));
    }

    blocks.push(
      p(rt("Trigger psychologique : ", { bold: true }), rt(pilier.trigger_psychologique)),
      p()
    );
  }

  blocks.push(div());

  // ── 3. RYTHME ────────────────────────────────────────
  blocks.push(
    h2("📅 3️⃣ Rythme optimal — Semaine type"),
    cal(
      "📌",
      rt(`${RYTHME.posts_semaine} posts / semaine. `, { bold: true }),
      rt(RYTHME.note)
    ),
    p()
  );

  for (const j of RYTHME.jours) {
    blocks.push(
      cal(
        j.pilier === 1 ? "🟢" : j.pilier === 2 ? "🔵" : "🟣",
        rt(`${j.jour} — `, { bold: true }),
        rt(j.type, { bold: true }),
        rt(`  [Pilier ${j.pilier}]\n`),
        rt(j.logique, { italic: true })
      )
    );
  }

  blocks.push(div());

  // ── 4. DM ────────────────────────────────────────────
  blocks.push(
    h2("🎯 4️⃣ Stratégie DM intelligente"),
    cal("⚠️", rt("Principe : ", { bold: true }), rt(DM_PROCESS.principe)),
    p()
  );

  blocks.push(p(rt("Process en 5 étapes :", { bold: true })));
  for (const e of DM_PROCESS.etapes) {
    blocks.push(
      num(
        rt(`${e.action} — `, { bold: true }),
        rt(e.detail)
      )
    );
  }

  blocks.push(
    p(),
    h3("💬 Template DM"),
    cal(
      "✉️",
      rt(DM_PROCESS.dm_template.message)
    ),
    p(rt("Ton : ", { bold: true }), rt(DM_PROCESS.dm_template.ton)),
    qot(rt("Règle absolue : ", { bold: true }), rt(DM_PROCESS.dm_template.regle, { italic: true })),
    div()
  );

  // ── 5. STRUCTURE POST ────────────────────────────────
  blocks.push(
    h2("💬 5️⃣ Structure post LinkedIn performante"),
    cal(
      "📐",
      rt("Principe : ", { bold: true }),
      rt(POST_STRUCTURE.principe),
      rt(`\nLongueur idéale : `, { bold: true }),
      rt(POST_STRUCTURE.longueur_ideale),
      rt(`\nFormat : `, { bold: true }),
      rt(POST_STRUCTURE.format)
    ),
    p()
  );

  for (const el of POST_STRUCTURE.elements) {
    blocks.push(
      bul(
        rt(`${el.num}. ${el.nom} — `, { bold: true }),
        rt(el.detail)
      ),
      p(
        rt("    Exemple : ", { bold: true, color: "gray" }),
        rt(`"${el.exemple}"`, { italic: true, color: "gray" })
      )
    );
  }

  blocks.push(div());

  // ── 6. KPI ───────────────────────────────────────────
  blocks.push(
    h2("📈 6️⃣ KPI LinkedIn B2B"),
    p(rt("4 métriques clés. Mesurer chaque semaine. Ajuster si nécessaire.", { italic: true })),
    p()
  );

  for (const kpi of KPIS) {
    blocks.push(
      cal(
        "📊",
        rt(`${kpi.metrique}`, { bold: true }),
        rt(`  →  Objectif : `, { color: "gray" }),
        rt(kpi.objectif, { bold: true, color: "green" }),
        rt(`\nCalcul : `, { bold: true }),
        rt(kpi.calcul),
        rt(`\n⚠️ Alerte : `, { bold: true }),
        rt(kpi.alerte, { color: "red" }),
        rt(`  |  Fréquence : `, { bold: true }),
        rt(kpi.frequence)
      )
    );
  }

  blocks.push(div());

  // ── 7. TUNNEL ────────────────────────────────────────
  blocks.push(
    h2("💰 7️⃣ Tunnel LinkedIn → Agency"),
    p(rt("Chaque post alimente le début du tunnel. Chaque étape a un seul rôle.", { italic: true })),
    p()
  );

  for (const t of TUNNEL) {
    blocks.push(
      cal(
        t.etape <= 2 ? "🔵" : t.etape <= 4 ? "🟡" : "🟢",
        rt(`${t.etape}. ${t.label}`, { bold: true }),
        rt(`\nRôle : `),
        rt(t.role),
        rt(`\nConversion : `, { bold: true }),
        rt(t.conversion, { italic: true })
      )
    );
  }

  blocks.push(
    p(),
    qot(
      rt("Vitesse cible : ", { bold: true }),
      rt("Post → DM en 3–5 jours · DM → Appel en 3–7 jours · Appel → Proposition en 48h")
    ),
    div()
  );

  // ── 8. DIFFÉRENCIATION ──────────────────────────────
  blocks.push(
    h2("🧠 8️⃣ Différenciation clé — Ce que tu dis vs ce que les autres disent"),
    cal("📌", rt("Principe : ", { bold: true }), rt(DIFFERENCIATION.principe)),
    p()
  );

  blocks.push(h3("❌ Ne parle PAS :"));
  for (const item of DIFFERENCIATION.ne_pas_dire) {
    blocks.push(bul(rt("✗ ", { color: "red" }), rt(`"${item}"`)));
  }

  blocks.push(p(), h3("✅ Parle :"));
  for (const item of DIFFERENCIATION.dire_a_la_place) {
    blocks.push(bul(rt("✓ ", { color: "green" }), rt(`"${item}"`)));
  }

  blocks.push(
    p(),
    cal(
      "🎯",
      rt("Formule gagnante : ", { bold: true }),
      rt(DIFFERENCIATION.formule)
    ),
    p(),
    cal(
      "🏆",
      rt("Positionnement final : ", { bold: true }),
      rt(DIFFERENCIATION.positionnement_final)
    ),
    div()
  );

  // ── RÉCAP EXÉCUTIF ──────────────────────────────────
  blocks.push(
    h2("🚀 Récapitulatif exécutif"),
    p(rt("Ce que ça donne si tu exécutes pendant 90 jours :", { italic: true })),
    bul(rt("✅ Profil optimisé reconnu dans la niche formateurs B2B")),
    bul(rt("✅ 3 piliers actifs · 3 posts / semaine · 36 posts / trimestre")),
    bul(rt("✅ 3–5 conversations qualifiées / semaine")),
    bul(rt("✅ 1–2 appels stratégiques / semaine")),
    bul(rt("✅ 1 closing minimum / mois → 4+ missions / trimestre")),
    p(),
    cal(
      "💰",
      rt("Objectif CA LinkedIn Q1 : ", { bold: true }),
      rt("4 missions × 5 000 € moyen = "),
      rt("20 000 €", { bold: true, color: "green" }),
      rt("  (scénario conservateur Phase 1 Audit × closings Core System™)")
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

  console.log(`📄 Création page : ${PAGE.titre}`);
  console.log(`📦 ${allBlocks.length} blocs → ${chunks.length} batch(es)`);

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
    console.log(`  ↳ Batch ${i + 1}/${chunks.length} envoyé`);
  }

  console.log(`\n🎉 Terminé — Stratégie LinkedIn Acquisition B2B créée dans Notion`);
  console.log(`📊 3 piliers · ${KPIS.length} KPIs · ${TUNNEL.length} étapes tunnel · template DM complet`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
