#!/usr/bin/env node
"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;

const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ════════════════════════════════════════════════════════
//  DATA — 10 posts complets
// ════════════════════════════════════════════════════════

const PAGE = {
  titre: "✍️ 10 Posts LinkedIn B2B — Banque de contenu schoolsWP Agency",
  objectif:
    "10 posts LinkedIn ultra ciblés, entièrement rédigés, prêts à publier. Niche : formateurs B2B. Positionnement : architecte système WordPress. Structure : Hook → Problème → Explication → Insight → Question.",
};

// Pilier 1 = Problèmes B2B réels (🟢)
// Pilier 2 = Architecture & méthode (🔵)
// Pilier 3 = Études de cas & terrain (🟣)

const POSTS = [
  {
    num: 1,
    pilier: 1,
    jour_recommande: "Lundi",
    titre: "Votre LMS n'est pas le problème",
    angle: "Le vrai problème est l'architecture globale : CRM + onboarding + reporting.",
    objectif_cache: "Introduire ton expertise système. Repositionner le problème.",
    hook: "Votre LMS WordPress n'est probablement pas votre vrai problème.",
    probleme:
      "La plupart des formateurs B2B passent des heures à chercher le bon plugin LMS.\nEt pourtant, ça coince toujours au même endroit.",
    explication: [
      "Le vrai problème, c'est l'architecture globale :",
      "→ CRM non aligné avec le LMS",
      "→ Onboarding manuel qui ralentit tout",
      "→ Reporting inexistant pour les clients entreprise",
    ],
    insight:
      "J'ai audité des dizaines de systèmes WordPress pour formateurs B2B.\nDans 90 % des cas, le LMS fonctionne.\nLe reste ne suit pas.",
    question: "Est-ce que votre CRM sait ce que fait votre LMS ?",
  },
  {
    num: 2,
    pilier: 1,
    jour_recommande: "Lundi",
    titre: "Former des entreprises ≠ vendre des formations",
    angle: "Cycle long, validation interne, décision multi-personnes — autre modèle, autre architecture.",
    objectif_cache: "Montrer que tu comprends le business model B2B mieux que quiconque.",
    hook: "Le B2B ne fonctionne pas comme le B2C.\nPourtant, beaucoup utilisent la même architecture WordPress.",
    probleme:
      "Cycle long, validation interne, décision multi-personnes.\nCe n'est pas le même chemin d'achat.",
    explication: [
      "En B2C : 1 décideur, achat possible en 10 minutes.",
      "En B2B :",
      "→ 2 à 4 personnes impliquées dans la décision",
      "→ Devis, bon de commande, facturation centralisée",
      "→ Suivi par groupe — pas par individu",
      "→ Reporting attendu par le DRH ou le manager",
    ],
    insight:
      "Si votre WordPress est pensé B2C, il freinera systématiquement votre développement B2B.",
    question:
      "Votre système actuel peut-il gérer une commande groupe avec facturation centralisée ?",
  },
  {
    num: 3,
    pilier: 2,
    jour_recommande: "Mercredi",
    titre: "Gérer 10 entreprises clientes sur WordPress",
    angle: "Problème multi-comptes / segmentation. Passer à l'échelle nécessite une refonte de structure.",
    objectif_cache: "Préparer mentalement le prospect à l'idée d'un audit système.",
    hook: "Si vous formez plusieurs entreprises,\nvotre WordPress doit gérer des groupes — pas des individus.",
    probleme:
      "Passer de 2 à 10 clients entreprise, c'est un changement d'architecture.\nPas un changement d'outil.",
    explication: [
      "Ce que ça implique concrètement :",
      "→ Accès isolés par entreprise cliente",
      "→ Gestion des apprenants par groupe",
      "→ Tableau de bord client séparé",
      "→ Facturation et relances automatisées par compte",
    ],
    insight:
      "Un LMS pensé 'individuel' devient un gouffre de temps à partir du 3e client enterprise.\nC'est systématique.",
    question:
      "Combien de temps tu passes chaque semaine à gérer manuellement les accès de tes clients B2B ?",
  },
  {
    num: 4,
    pilier: 1,
    jour_recommande: "Lundi",
    titre: "Le CRM est plus important que le LMS",
    angle: "Le cycle de vente B2B bloque avant même l'entrée dans le LMS.",
    objectif_cache: "Amener naturellement vers un audit CRM. Montrer l'angle qu'ils n'avaient pas.",
    hook: "La plupart des formateurs B2B optimisent leur LMS.\nTrès peu optimisent leur CRM.",
    probleme:
      "Pourtant, les 3/4 des problèmes de croissance viennent du pipeline.\nPas de la plateforme.",
    explication: [
      "Un CRM B2B bien structuré, c'est :",
      "→ Segmentation par taille d'entreprise et secteur",
      "→ Pipeline de devis automatisé avec relances",
      "→ Historique client complet : contrats, accès, renouvellements",
      "→ Alertes renouvellement avant résiliation",
    ],
    insight:
      "Sans CRM aligné, chaque nouveau client B2B coûte plus d'énergie que le précédent.\nLa croissance devient épuisante.",
    question: "Est-ce que ton CRM sait quand ton prochain contrat enterprise expire ?",
  },
  {
    num: 5,
    pilier: 2,
    jour_recommande: "Mercredi",
    titre: "Onboarding entreprise automatisé",
    angle: "Automatisation complète des accès, emails et suivi dès la signature.",
    objectif_cache: "Montrer l'expertise automatisation. Faire réaliser le coût du manuel.",
    hook: "Chaque nouvelle entreprise cliente devrait déclencher un système.\nPas une checklist manuelle.",
    probleme:
      "Un onboarding manuel, c'est 2 à 4 heures perdues à chaque nouveau client.\nMultiplié par 10, c'est ton plein temps.",
    explication: [
      "Un onboarding automatisé, c'est :",
      "→ Formulaire de collecte → CRM auto-rempli",
      "→ Création des accès LMS par groupe en 1 clic",
      "→ Email de bienvenue personnalisé entreprise",
      "→ Invitation Calendly pour la réunion de lancement",
      "→ Dashboard accès envoyé au contact RH",
    ],
    insight:
      "L'onboarding est le premier signal de professionnalisme pour un client entreprise.\nIl conditionne le renouvellement du contrat.",
    question: "Combien d'étapes manuelles ton onboarding B2B contient-il aujourd'hui ?",
  },
  {
    num: 6,
    pilier: 1,
    jour_recommande: "Lundi",
    titre: "Pourquoi votre tunnel B2B ne convertit pas",
    angle: "Absence de qualification → appels inutiles → taux de closing catastrophique.",
    objectif_cache: "Amener vers l'audit stratégique /audit-b2b. La solution est le formulaire éliminatoire.",
    hook: "Si vous passez 45 minutes en appel avec des prospects non qualifiés,\nvotre problème est structurel.",
    probleme:
      "Pas de filtre = pas de qualification.\nRésultat : trop d'appels, trop peu de closings.",
    explication: [
      "Un tunnel B2B qui convertit, c'est :",
      "→ Formulaire éliminatoire : CA, budget, nb clients entreprise",
      "→ Page d'offre claire avec preuve sociale corporate",
      "→ Appel court 20 min pour confirmer le fit — pas vendre",
      "→ Proposition envoyée dans les 48h",
    ],
    insight:
      "En B2B, la valeur de l'appel se décide avant l'appel.\nLe formulaire fait le tri. Pas toi.",
    question: "Ton formulaire de contact actuel filtre-t-il les prospects qui n'ont pas le budget ?",
  },
  {
    num: 7,
    pilier: 3,
    jour_recommande: "Vendredi",
    titre: "Ce que les entreprises achètent vraiment",
    angle: "Les entreprises n'achètent pas une formation. Elles achètent un résultat mesurable.",
    objectif_cache: "Positionner l'expertise corporate. Montrer que tu parles le langage des DRH.",
    hook: "Les entreprises n'achètent pas une formation.\nElles achètent un résultat mesurable.",
    probleme:
      "Si tu ne peux pas leur montrer les données, tu ne peux pas justifier le renouvellement.\nEt le renouvellement, c'est ton MRR.",
    explication: [
      "Ce qu'un client entreprise attend concrètement :",
      "→ Taux de complétion par apprenant",
      "→ Temps moyen passé sur les modules",
      "→ Résultats aux quiz et évaluations",
      "→ Export PDF mensuel pour le manager RH",
    ],
    insight:
      "Le reporting transforme une prestation en partenariat long terme.\nC'est aussi ce qui justifie une augmentation de tarif annuelle.",
    question:
      "Est-ce que tu peux envoyer un rapport de formation à ton client entreprise en moins de 10 minutes ?",
  },
  {
    num: 8,
    pilier: 2,
    jour_recommande: "Mercredi",
    titre: "Architecture WordPress B2B idéale",
    angle: "Donner un schéma complet, lisible, structuré. Autorité technique maximale.",
    objectif_cache: "Devenir la référence mentale sur ce sujet. Ce post se sauvegarde et se partage.",
    hook: "Voici l'architecture WordPress que j'utilise pour les formateurs B2B.",
    probleme:
      "La majorité des systèmes que j'audite ont les bons outils.\nMais pas la bonne structure.",
    explication: [
      "L'architecture complète, couche par couche :",
      "→ LMS : Tutor LMS + groupes entreprise + reporting apprenant",
      "→ CRM : FluentCRM + segmentation B2B + pipeline devis",
      "→ Facturation : WooCommerce + facturation automatique + relances",
      "→ Tunnel : page offre + formulaire qualifiant + Calendly",
      "→ Automatisations : onboarding · relances · alertes renouvellement",
    ],
    insight:
      "Chaque couche a un rôle précis.\nAucun outil ne fait tout.\nL'architecture, c'est ce qui fait tenir le tout ensemble.",
    question: "Quelle est la couche la plus fragile dans ton système actuel ?",
  },
  {
    num: 9,
    pilier: 3,
    jour_recommande: "Vendredi",
    titre: "Les 3 erreurs fréquentes des formateurs B2B sur WordPress",
    angle: "Erreur = opportunité de repositionnement. Ce post crée de l'interaction forte.",
    objectif_cache: "Crédibilité terrain + identification du prospect dans les erreurs = DM entrants.",
    hook: "3 erreurs que je vois presque systématiquement chez les formateurs B2B :",
    probleme:
      "Ces erreurs ne bloquent pas au départ.\nElles frappent au moment où tu commences à scaler.",
    explication: [
      "Erreur 1 → LMS pensé individuel utilisé pour des groupes",
      "Résultat : accès manuels, erreurs d'attribution, perte de temps\n",
      "Erreur 2 → CRM généraliste non segmenté B2B",
      "Résultat : pipeline de devis inexistant, relances oubliées, churn silencieux\n",
      "Erreur 3 → Tunnel conçu pour du B2C",
      "Résultat : appels non qualifiés, pricing flou, closings rares",
    ],
    insight:
      "Ces 3 erreurs coexistent souvent.\nEt elles se renforcent mutuellement.\nCorrection partielle = résultats partiels.",
    question: "Laquelle de ces 3 erreurs te parle le plus ?",
  },
  {
    num: 10,
    pilier: 1,
    jour_recommande: "Lundi",
    titre: "Quand faut-il refondre son système WordPress B2B ?",
    angle: "Signaux déclencheurs. Ce post touche les prospects déjà en douleur.",
    objectif_cache: "Préparer la conversion audit. Le prospect se reconnaît dans les signaux.",
    hook: "Si votre système WordPress repose sur des contournements,\nil est probablement temps de le restructurer.",
    probleme:
      "Le problème avec les contournements, c'est qu'on s'y habitue.\nJusqu'au jour où un client important part.",
    explication: [
      "Les signaux qui ne trompent pas :",
      "→ Tu crées les accès manuellement à chaque nouveau client",
      "→ Ton CRM n'est pas synchronisé avec ton LMS",
      "→ Tu ne sais pas combien de contrats expirent ce trimestre",
      "→ La facturation te prend plus d'1h par mois",
      "→ Tu ne peux pas déléguer l'onboarding",
    ],
    insight:
      "Une refonte ne coûte pas cher si elle est bien architecturée.\nElle coûte très cher si elle arrive après une crise.",
    question:
      "Si tu devais doubler ton nombre de clients B2B demain, qu'est-ce qui casserait en premier ?",
  },
];

const STRUCTURE_POST = [
  { num: 1, label: "Hook court", role: "Stopper le scroll. 1 ligne. Provoque, interpelle, contre-intuitif." },
  { num: 2, label: "Problème réel", role: "2-3 lignes. Le lecteur se reconnaît dans sa propre situation." },
  { num: 3, label: "Explication simple", role: "Structure lisible. Une idée par ligne. Flèches →. Pas de jargon." },
  { num: 4, label: "Insight expert", role: "La chose que seul quelqu'un qui a fait ce travail peut dire." },
  { num: 5, label: "Question ouverte", role: "Invite à réagir. Ouvre la conversation. Prépare le DM." },
];

const CALENDRIER_SUGGESTION = [
  { semaine: 1, lundi: 1, mercredi: 8, vendredi: 9 },
  { semaine: 2, lundi: 2, mercredi: 3, vendredi: 7 },
  { semaine: 3, lundi: 4, mercredi: 5, vendredi: null },
  { semaine: 4, lundi: 6, mercredi: null, vendredi: 10 },
];

const PILIER_LABELS = {
  1: { emoji: "🟢", nom: "Problèmes B2B réels" },
  2: { emoji: "🔵", nom: "Architecture & méthode" },
  3: { emoji: "🟣", nom: "Études de cas & terrain" },
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

const h1 = (t) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });

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
      rt("📊 10 posts complets · ", { bold: true }),
      rt("🟢 5 × Pilier 1 (Problèmes)  ·  🔵 3 × Pilier 2 (Architecture)  ·  🟣 2 × Pilier 3 (Terrain)")
    ),
    p(
      rt("Structure par post : ", { bold: true }),
      rt("Hook → Problème réel → Explication → Insight expert → Question finale")
    ),
    div()
  );

  // ── STRUCTURE RAPPEL ─────────────────────────────────
  blocks.push(
    h2("📐 Structure type — rappel"),
    p(rt("À appliquer pour chaque post, dans cet ordre exact :", { italic: true }))
  );

  for (const s of STRUCTURE_POST) {
    blocks.push(
      num(
        rt(`${s.label} — `, { bold: true }),
        rt(s.role)
      )
    );
  }

  blocks.push(
    p(),
    cal(
      "⚠️",
      rt("Format : ", { bold: true }),
      rt("Une idée par ligne. Retours fréquents. Jamais de pavé. 150–300 mots par post.")
    ),
    div()
  );

  // ── CALENDRIER SUGGESTION ────────────────────────────
  blocks.push(
    h2("📅 Calendrier de publication suggéré"),
    p(rt("Rythme : 3 posts / semaine · Lundi (Problème) · Mercredi (Architecture) · Vendredi (Terrain)", { italic: true }))
  );

  for (const sem of CALENDRIER_SUGGESTION) {
    const lundi = sem.lundi ? `Post #${sem.lundi}` : "—";
    const mercredi = sem.mercredi ? `Post #${sem.mercredi}` : "—";
    const vendredi = sem.vendredi ? `Post #${sem.vendredi}` : "—";
    blocks.push(
      bul(
        rt(`Semaine ${sem.semaine} : `, { bold: true }),
        rt(`Lundi → ${lundi}   ·   Mercredi → ${mercredi}   ·   Vendredi → ${vendredi}`)
      )
    );
  }

  blocks.push(div());

  // ── 10 POSTS ─────────────────────────────────────────
  blocks.push(h2("✍️ Les 10 posts rédigés"));

  for (const post of POSTS) {
    const pilier = PILIER_LABELS[post.pilier];

    // Post header
    blocks.push(
      h3(`${pilier.emoji} Post #${post.num} — "${post.titre}"`),
      p(
        rt("Pilier : ", { bold: true }),
        rt(`${pilier.nom}  `),
        rt("  |  Jour : ", { bold: true }),
        rt(post.jour_recommande),
        rt("  |  Objectif : ", { bold: true }),
        rt(post.objectif_cache, { italic: true, color: "gray" })
      ),
      p(rt("Angle : ", { bold: true }), rt(post.angle, { italic: true }))
    );

    // Post complet dans un callout
    const lignes_post = [
      rt(post.hook + "\n\n", { bold: true }),
      rt(post.probleme + "\n\n"),
      ...post.explication.map((l) => rt(l + "\n")),
      rt("\n" + post.insight + "\n\n"),
      rt(post.question, { italic: true }),
    ];

    blocks.push(
      cal("✍️", ...lignes_post)
    );

    // Méta
    blocks.push(
      p(
        rt("Hook : ", { bold: true, color: "blue" }),
        rt(`"${post.hook.split("\n")[0]}"`, { italic: true })
      ),
      p(
        rt("Insight clé : ", { bold: true, color: "orange" }),
        rt(post.insight.split("\n")[0], { italic: true })
      ),
      div()
    );
  }

  // ── NOTES D'USAGE ────────────────────────────────────
  blocks.push(
    h2("🧠 Notes d'usage"),
    bul(rt("✅ Chaque post peut être publié tel quel ou personnalisé avec un exemple client réel")),
    bul(rt("✅ Les posts #3, #8, #9 génèrent le plus de sauvegardes (contenu pratique + schéma)")),
    bul(rt("✅ Les posts #1, #4, #6, #10 génèrent le plus de DM (tension créée, auto-identification)")),
    bul(rt("✅ Post #9 (3 erreurs) = fort taux de commentaires — surveiller et répondre à chacun")),
    bul(rt("✅ Après chaque post, scanner les commentaires pour identifier les formateurs B2B actifs → DM")),
    p(),
    cal(
      "🔥",
      rt("Règle d'or : ", { bold: true }),
      rt(
        "Tu ne vends pas dans le post. Tu crées une tension utile. Le profil vend. Le formulaire /audit-b2b qualifie. L'appel confirme."
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

  console.log(`\n🎉 Terminé — Banque de 10 posts LinkedIn B2B créée dans Notion`);
  console.log(`✍️ ${POSTS.length} posts complets · 4 semaines de contenu prêt à publier`);
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
