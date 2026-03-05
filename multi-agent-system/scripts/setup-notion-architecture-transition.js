#!/usr/bin/env node
/**
 * setup-notion-architecture-transition.js
 * Crée la page "Architecture de Transition — Salarié → SASU WordPress" dans Notion.
 *
 * Usage :
 *   NOTION_API_KEY=... NOTION_PARENT_PAGE_ID=... node setup-notion-architecture-transition.js
 */

"use strict";

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ---------------------------------------------------------------------------
// API helpers
// ---------------------------------------------------------------------------

async function notionRequest(method, path, body) {
  const res = await fetch(`https://api.notion.com/v1${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Content-Type": "application/json",
      "Notion-Version": "2022-06-28",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Notion API ${res.status} — ${err}`);
  }
  return res.json();
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------------------
// Block builders
// ---------------------------------------------------------------------------

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: text },
  annotations: {
    bold: opts.bold || false,
    italic: opts.italic || false,
    code: opts.code || false,
    color: opts.color || "default",
  },
});

const h1 = (t) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (...parts) => ({
  object: "block", type: "paragraph",
  paragraph: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const bul = (...parts) => ({
  object: "block", type: "bulleted_list_item",
  bulleted_list_item: { rich_text: parts.map((x) => (typeof x === "string" ? rt(x) : x)) },
});
const num = (t) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: [rt(t)] } });
const tod = (t, checked = false) => ({ object: "block", type: "to_do", to_do: { rich_text: [rt(t)], checked } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const cal = (text, emoji = "💡", color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: [rt(text)], icon: { type: "emoji", emoji }, color },
});
const qot = (t) => ({ object: "block", type: "quote", quote: { rich_text: [rt(t)] } });
const tog = (title, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(title, { bold: true })], children },
});

// ---------------------------------------------------------------------------
// Données — calculs financiers
// ---------------------------------------------------------------------------

const CHARGES_PERSO_MOIS = 2500;     // € — charges personnelles mensuelles estimées
const CHARGES_SASU_FIXES_MOIS = 800; // € — charges fixes SASU (compta, assurance, outils)
const TOTAL_MENSUEL = CHARGES_PERSO_MOIS + CHARGES_SASU_FIXES_MOIS;

const SECURITE_MOIS = 6;
const EPARGNE_SECURITE = CHARGES_PERSO_MOIS * SECURITE_MOIS;

const OBJECTIFS_CA = [
  { periode: "M1–M2", label: "Validation modèle", appels: "3 à 5", projets: "1 à 2", ca_mini: 4000, ca_cible: 8000 },
  { periode: "M3–M4", label: "Accélération", appels: "5 à 8", projets: "2 à 3", ca_mini: 8000, ca_cible: 15000 },
  { periode: "M5–M6", label: "Stabilisation", appels: "6 à 10", projets: "3 à 4", ca_mini: 12000, ca_cible: 20000 },
];

const CA_AN1_MINI = 40000;
const CA_AN1_CIBLE = 65000;
const PROJETS_PAR_TRIM_MINI = 3;
const PROJETS_PAR_TRIM_CIBLE = 5;

// ---------------------------------------------------------------------------
// Page content
// ---------------------------------------------------------------------------

function buildTemplate() {
  const blocks = [];

  // EN-TÊTE — PHILOSOPHIE
  blocks.push(
    cal(
      "On ne fait pas ça « à l'émotion ». On fait ça en architecture de transition — méthodique, sécurisée, stratégique. Chaque étape a ses conditions. Chaque condition a ses indicateurs.",
      "🧭", "purple_background"
    ),
    p(rt("Mis à jour : mars 2026 · Profil : salarié en transition, schoolsWP actif, SASU à lancer", { color: "gray" })),
    div()
  );

  // ───────────────────────────────────────────
  // PRINCIPE FONDATEUR
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧠 Principe Fondateur"),
    p(""),

    h2("Les 3 erreurs de transition classiques"),
    bul(rt("Partir trop tôt", { bold: true }), rt(" — avant d'avoir validé l'offre, le pricing et le premier lead entrant")),
    bul(rt("Partir à l'émotion", { bold: true }), rt(" — après une mauvaise semaine au travail, sans trésorerie prête")),
    bul(rt("Partir sans pipeline", { bold: true }), rt(" — avec une idée d'offre mais zéro preuve que des clients vont payer")),
    p(""),

    h2("La règle unique"),
    cal(
      "Tu quittes quand les conditions sont remplies — pas avant. Le salaire actuel est ta runway. Utilise-la pour construire, pas pour subir.",
      "🔒", "red_background"
    ),
    p(""),

    h2("Ton avantage stratégique"),
    bul(rt("schoolsWP existe", { bold: true }), rt(" — l'autorité se construit PENDANT que tu es encore salarié")),
    bul(rt("Tu penses en systèmes", { bold: true }), rt(" — tu ne vas pas improviser, tu vas architecturer")),
    bul(rt("Tu as le temps de valider", { bold: true }), rt(" — chaque lead reçu pendant la période salariée prouve le modèle avant le saut")),
    bul(rt("Tu n'es pas débutant", { bold: true }), rt(" — ton expertise WordPress, CRM, automatisation existe déjà, schoolsWP en est la preuve publique")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PHASE 1 — STABILISATION
  // ───────────────────────────────────────────
  blocks.push(
    h1("🟡 Phase 1 — Stabilisation & Préparation"),
    cal("Durée : 0 à 3 mois. Objectif : construire une base solide AVANT la bascule. Ne pas quitter trop tôt.", "📋", "yellow_background"),
    p("")
  );

  blocks.push(
    h2("1.1 — Clarifier le modèle (4 questions sans ambiguïté)"),
    cal(
      "Si tu ne peux pas répondre à ces 4 questions en 30 secondes chacune → Phase 1 non terminée.",
      "⚠️", "orange_background"
    ),
    p(""),
    tog("❓ Quelle est mon offre signature ?", [
      p(""),
      p(rt("Réponse attendue :", { bold: true })),
      qot("Le WordPress Business System™ — structuration d'un système WordPress rentable et automatisé en 6 à 8 semaines. 3 niveaux : Audit (1 500 €) / Standard (3–6k€) / Premium (7–12k€)."),
      p(""),
      tod("J'ai une page offre rédigée et une URL active"),
      tod("J'ai un deck de présentation en 5 slides"),
      tod("J'ai un tarif plancher non négociable (Audit : 1 500 €)"),
    ]),
    tog("❓ Quel problème précis je résous ?", [
      p(""),
      p(rt("Réponse attendue :", { bold: true })),
      qot("Un WordPress bricolé (plugins empilés, CRM inexistant, tunnel bancal) fait perdre 20 à 30 % de CA à des freelances et formateurs qui font déjà du chiffre. Je structure le système pour qu'il génère du CA au lieu d'en coûter."),
      p(""),
      tod("Je peux l'expliquer sans notes en moins de 45 secondes"),
      tod("Mon CTA schoolsWP est aligné avec cette formulation"),
    ]),
    tog("❓ Pour qui exactement ?", [
      p(""),
      p(rt("Réponse attendue :", { bold: true })),
      qot("Freelances, formateurs et solopreneurs qui font déjà > 30k€/an, ont un WordPress en production, et se sentent bloqués par leur système. Pas les débutants. Pas les budgets < 1 500 €."),
      p(""),
      tod("Mon formulaire de qualification filtre ces 3 critères"),
      tod("Mon CTA principal ne s'adresse qu'à cette cible"),
    ]),
    tog("❓ Combien je facture ?", [
      p(""),
      p(rt("Réponse attendue :", { bold: true })),
      qot("Audit Stratégique : 1 500 €. WBS Standard : 3 000 à 6 000 €. WBS Premium : 7 000 à 12 000 €. Maintenance : 400 à 700 €/mois. Pas de tarif journalier. Pas de devis à 800 €."),
      p(""),
      tod("Mon pricing est fixé et écrit dans mes CGV"),
      tod("J'ai refusé au moins 1 demande hors cible (preuve de positionnement)"),
    ]),
    p("")
  );

  blocks.push(
    h2("1.2 — Objectif financier minimum avant départ"),
    p(""),
    tog(`💰 Calcul de sécurité personnalisé (base : ${CHARGES_PERSO_MOIS.toLocaleString("fr")} €/mois)`, [
      p(""),
      p(rt("Charges personnelles mensuelles : ", { bold: true }), rt(`${CHARGES_PERSO_MOIS.toLocaleString("fr")} €`)),
      p(rt("Charges SASU fixes mensuelles : ", { bold: true }), rt(`${CHARGES_SASU_FIXES_MOIS.toLocaleString("fr")} € (compta, assurance RC Pro, outils)`)),
      p(rt("Total mensuel à couvrir en autonomie : ", { bold: true }), rt(`${TOTAL_MENSUEL.toLocaleString("fr")} €`)),
      p(""),
      p(rt(`Épargne de sécurité recommandée (${SECURITE_MOIS} mois perso) : `, { bold: true }), rt(`${EPARGNE_SECURITE.toLocaleString("fr")} €`, { bold: true })),
      p(""),
      p(rt("+ Pipeline actif requis avant départ :", { bold: true })),
      bul("1 projet signé ou en négociation avancée (acompte versé de préférence)"),
      bul("2 à 3 prospects qualifiés en pipeline (appels passés, devis envoyé)"),
      bul("Estimation CA visible M1 : > 3 000 € minimum"),
      p(""),
      p(rt("En résumé : ", { bold: true })),
      bul(rt(`${EPARGNE_SECURITE.toLocaleString("fr")} € d'épargne sécurité + 1 mission signée = conditions minimales de départ.`, { bold: true })),
    ]),
    p("")
  );

  blocks.push(
    h2("1.3 — Activer le pont schoolsWP → Leads"),
    p("Avant de démissionner, ces 5 éléments doivent être actifs et générateurs de signaux :"),
    p(""),
    bul(rt("Page Audit active", { bold: true }), rt(" — formulaire de qualification opérationnel, prix visible, lien Cal.com fonctionnel")),
    bul(rt("5 articles décisionnels publiés", { bold: true }), rt(" — au moins 3 dans le cluster CRM ou LMS, CTA intégrés")),
    bul(rt("CTA cohérents dans chaque article", { bold: true }), rt(" — lien vers Audit Stratégique, pas vers une page de contact générique")),
    bul(rt("Formulaire de qualification actif", { bold: true }), rt(" — 5 questions filtrantes, connecté à ton agenda")),
    bul(rt("Signaux de marché visibles", { bold: true }), rt(" — au moins 1 appel découverte passé, 1 lead qualifié entré dans le pipeline")),
    p(""),
    qot("Tu n'as pas besoin d'un client signé avant de partir. Tu as besoin de voir que le pipeline existe et fonctionne."),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // CHECKLIST DE DÉPART
  // ───────────────────────────────────────────
  blocks.push(
    h1("🔴 Checklist de Départ — Les 7 Conditions"),
    cal(
      "Tu coches les 7. Pas 5. Pas 6. Les 7. Sinon tu restes en Phase 1 et tu optimises ce qui manque.",
      "🔒", "red_background"
    ),
    p(""),
    tod("✅  Offre signature documentée — page offre + pricing + CGV prêts"),
    tod("✅  Trésorerie sécurité — 6 mois de charges perso en épargne disponible"),
    tod("✅  Pipeline actif — au moins 1 projet signé ou 2 prospects qualifiés chauds"),
    tod("✅  Pont schoolsWP opérationnel — 5 articles + page Audit + formulaire + Cal.com"),
    tod("✅  SASU prête à créer — capital décidé, expert-comptable identifié"),
    tod("✅  Exit salarié planifié — rupture conventionnelle ou préavis, timing calculé"),
    tod("✅  Runway mentale — tu quittes dans la sérénité, pas dans l'urgence"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PHASE 2 — LANCEMENT SASU
  // ───────────────────────────────────────────
  blocks.push(
    h1("🟠 Phase 2 — Lancement Contrôlé SASU"),
    cal("Mois 0 — Le moment de création. Tu ne démissionnes pas pour voir. Tu démissionnes parce que les conditions sont remplies.", "🏗", "orange_background"),
    p("")
  );

  blocks.push(
    h2("2.1 — Timing de création de la SASU"),
    tog("📅 Option A — Créer la SASU avant de quitter (recommandé)", [
      p(""),
      bul("Créer la SASU 4 à 6 semaines avant la fin du contrat salarié"),
      bul("Avantage : SASU active, numéro SIREN et IBAN disponibles dès le départ"),
      bul("Avantage : premières factures possibles dès la sortie du salariat"),
      bul("Point de vigilance : vérifier la clause d'exclusivité du contrat de travail"),
      bul("Solution : activité schoolsWP (media) non concurrente du contrat = légalement protégé"),
    ]),
    tog("📅 Option B — Créer la SASU après la sortie", [
      p(""),
      bul("Créer la SASU dans les 2 premières semaines post-sortie"),
      bul("Avantage : simplicité, aucun risque juridique lié au contrat de travail"),
      bul("Inconvénient : 2 semaines sans structure juridique pour facturer"),
      bul("Acceptable si un client peut attendre le 1er SIREN pour la facture"),
    ]),
    p(""),

    h2("2.2 — Les premières règles SASU"),
    bul(rt("Règle 1 : ne pas se payer immédiatement", { bold: true }), rt(" — construire d'abord la trésorerie SASU (objectif : 3 mois de charges fixes en réserve)")),
    bul(rt("Règle 2 : la règle des 40 %", { bold: true }), rt(" — sur chaque encaissement HT : 40 % → sous-compte « Charges fiscales » (TVA + IS + URSSAF)")),
    bul(rt("Règle 3 : expert-comptable dès J+1", { bold: true }), rt(" — pas en DIY sur la compta SASU à l'IS, le coût est déductible et l'erreur est trop chère")),
    bul(rt("Règle 4 : RC Pro immédiatement", { bold: true }), rt(" — avant la 1ère mission signée, sans exception")),
    bul(rt("Règle 5 : contrat client avant chaque mission", { bold: true }), rt(" — même pour un audit à 1 500 €, CGV + bon de commande signé")),
    p(""),

    h2("2.3 — Positionnement dès J1"),
    p("Le premier message LinkedIn après la sortie :"),
    p(""),
    qot("J'aide les indépendants, freelances et formateurs à structurer un système WordPress rentable et automatisé. Ce que j'ai construit sur schoolsWP, je le structure maintenant pour d'autres."),
    p(""),
    bul(rt("Pas : ", { bold: true }), rt('"Je suis disponible pour des missions WordPress"')),
    bul(rt("Pas : ", { bold: true }), rt('"Je crée des sites WordPress"')),
    bul(rt("Pas : ", { bold: true }), rt('"Freelance WordPress disponible" → tu n'es pas freelance, tu es architecte système')),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // PHASE 3 — 6 MOIS POST-DÉPART
  // ───────────────────────────────────────────
  blocks.push(
    h1("🟢 Phase 3 — 6 Mois Post-Départ"),
    cal("Objectif : valider que le modèle fonctionne, pas « tout réussir ». Un modèle validé vaut mieux qu'un trimestre exceptionnel.", "📈", "green_background"),
    p("")
  );

  for (const obj of OBJECTIFS_CA) {
    blocks.push(
      tog(`📅 ${obj.periode} — ${obj.label}`, [
        p(""),
        p(rt("Appels découverte cible : ", { bold: true }), rt(obj.appels)),
        p(rt("Projets signés objectif : ", { bold: true }), rt(obj.projets)),
        p(rt("CA minimum acceptable : ", { bold: true }), rt(`${obj.ca_mini.toLocaleString("fr")} €`)),
        p(rt("CA cible réaliste : ", { bold: true }), rt(`${obj.ca_cible.toLocaleString("fr")} €`)),
        p(""),
        ...(obj.periode === "M1–M2" ? [
          h3("Priorités M1–M2"),
          bul("Signer 1 à 2 audits WBS (1 500 € chacun) — porte d'entrée, pas de négociation"),
          bul("Réaliser les audits avec rigueur — ce sont tes premières références"),
          bul("Affiner le pitch en conditions réelles (call → pitch → objections → signature)"),
          bul("Ne pas baisser les prix pour signer plus vite — ce serait une erreur de positionnement"),
          bul("Continuer schoolsWP : 1 à 2 articles par semaine dans le cluster CRM"),
        ] : []),
        ...(obj.periode === "M3–M4" ? [
          h3("Priorités M3–M4"),
          bul("Transformer les audits en missions complètes (WBS Standard ou Premium)"),
          bul("Produire 1 étude de cas avec résultats mesurés (avant/après)"),
          bul("Ajuster le pricing si tu es en dessous du marché (signal : aucune objection sur le prix)"),
          bul("Proposer la maintenance WBS aux 2 premiers clients (MRR démarrage)"),
          bul("Évaluer : est-ce que le pipeline se remplit sans démarchage actif ?"),
        ] : []),
        ...(obj.periode === "M5–M6" ? [
          h3("Priorités M5–M6"),
          bul("Stabiliser le pipeline à 3 à 5 appels par mois sans action active"),
          bul("Augmenter les prix si le taux de conversion est > 60 % (signe d'un pricing trop bas)"),
          bul("Structurer la récurrence : 3 à 5 clients maintenance (MRR 1 200 à 3 500 €)"),
          bul("Planifier l'Année 2 : quelle niche approfondir ? Quel cluster SEO suivant ?"),
          bul("Évaluer la nécessité d'un sous-traitant si la charge dépasse 4 missions/trimestre"),
        ] : []),
      ])
    );
  }

  blocks.push(p(""), div());

  // ───────────────────────────────────────────
  // OBJECTIFS AN1 RÉALISTES
  // ───────────────────────────────────────────
  blocks.push(
    h1("💰 Objectifs Financiers — Première Année"),
    cal(
      "Ne vise pas l'explosion. Vise la validation — un modèle prévisible vaut 10 fois mieux qu'un trimestre exceptionnel.",
      "💰", "blue_background"
    ),
    p(""),

    h2("Scénario réaliste Année 1 (post-sortie)"),
    tog(`📊 Projections CA Année 1 (base schoolsWP active + WBS)`, [
      p(""),
      p(rt("Missions WBS (3 à 5 projets/trimestre × 2 trimestres actifs) :", { bold: true })),
      bul(`Objectif minimum : ${CA_AN1_MINI.toLocaleString("fr")} € CA total sur l'année`),
      bul(`Objectif réaliste : ${CA_AN1_CIBLE.toLocaleString("fr")} € CA total sur l'année`),
      bul(`Tarif moyen mission : 4 000 à 8 000 € (Audit + WBS Standard principalement)`),
      p(""),
      p(rt("Récurrence maintenance WBS (à partir de M3) :", { bold: true })),
      bul("3 clients à 400 €/mois = 1 200 €/mois MRR à M6"),
      bul("5 clients à 500 €/mois = 2 500 €/mois MRR à M12"),
      p(""),
      p(rt("Affiliation schoolsWP (à partir de M3–M4) :", { bold: true })),
      bul("Objectif : 200 à 500 €/mois à M12 (cluster CRM actif)"),
      p(""),
      p(rt("Total Année 1 estimé : ", { bold: true }), rt(`${CA_AN1_MINI.toLocaleString("fr")} à ${CA_AN1_CIBLE.toLocaleString("fr")} €`, { bold: true })),
      p(rt("Dont MRR M12 : ", { bold: true }), rt("1 700 à 3 000 €/mois récurrents (maintenance + affiliation)")),
    ]),
    p(""),

    h2("Ce que tu dois éviter impérativement"),
    bul(rt("Baisser tes prix pour remplir le planning", { bold: true }), rt(" — c'est l'erreur classique M1-M2. Tu définis le positionnement une fois pour toutes.")),
    bul(rt("Accepter tous les projets", { bold: true }), rt(" — un mauvais client prend autant de temps qu'un bon, pour moins de CA et plus de stress")),
    bul(rt("Négliger schoolsWP pendant les missions", { bold: true }), rt(" — c'est le pipeline long terme. Sans lui, à M12 tu prospectes encore à froid.")),
    bul(rt("Dépenser avant de construire la trésorerie SASU", { bold: true }), rt(" — objectif : 3 mois de charges fixes SASU en réserve avant premier salaire")),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // SÉCURITÉ MENTALE
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧠 Sécurité Mentale & Financière"),
    p(""),

    h2("Les 5 signaux qui indiquent que tu pars au bon moment"),
    bul(rt("Signal 1 — Tu es calme", { bold: true }), rt(" — la décision est analytique, pas émotionnelle. Tu pars parce que les conditions sont là.")),
    bul(rt("Signal 2 — Tu as un premier projet visible", { bold: true }), rt(" — pas nécessairement signé, mais une conversation sérieuse en cours")),
    bul(rt("Signal 3 — Tu n'as pas besoin que « ça marche du premier coup »", { bold: true }), rt(" — tu as 6 mois de runway pour ajuster")),
    bul(rt("Signal 4 — schoolsWP produit déjà des signaux", { bold: true }), rt(" — clics, formulaires remplis, appels demandés")),
    bul(rt("Signal 5 — Tu as une date", { bold: true }), rt(" — pas « bientôt ». Une date. Dans X semaines, j'enclenche la procédure.")),
    p(""),

    h2("Les 3 signaux d'alarme — ne pas partir"),
    bul(rt("Alarme 1 — Tu pars pour fuir", { bold: true }), rt(" — suite à un conflit, une déception, une fatigue. C'est le pire timing.")),
    bul(rt("Alarme 2 — Tu n'as pas encore été payé par un client", { bold: true }), rt(" — aucune validation marché → Phase 1 non terminée")),
    bul(rt("Alarme 3 — Tu n'as pas les 6 mois d'épargne", { bold: true }), rt(` — en dessous de ${EPARGNE_SECURITE.toLocaleString("fr")} € disponibles : attendre`)),
    p(""),

    h2("La question clé à te poser chaque mois"),
    qot("Si je pars aujourd'hui avec ce que j'ai — trésorerie, pipeline, offre, schoolsWP — est-ce que je me donne 12 mois confortables pour valider le modèle, ou est-ce que je me mets sous pression dès M2 ?"),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // ROADMAP ULTRA-CONCRÈTE
  // ───────────────────────────────────────────
  blocks.push(
    h1("🗺 Roadmap Ultra-Concrète"),
    p("")
  );

  blocks.push(
    h2("0 à 90 jours — Construire la base"),
    p(""),
    tog("📋 Semaine 1–2 — Offre & Outils", [
      p(""),
      tod("Finaliser le nom et le positionnement exact de l'offre (WordPress Business System™)"),
      tod("Rédiger et publier la page offre sur la SASU (ou un domaine dédié en attendant)"),
      tod("Fixer les 3 tarifs définitifs (Audit / Standard / Premium)"),
      tod("Créer les CGV et le contrat client type"),
      tod("Configurer Cal.com avec formulaire de qualification 5 questions"),
    ]),
    tog("📋 Semaine 3–4 — Cluster CRM schoolsWP", [
      p(""),
      tod("Lancer le Workflow W1 sur « crm wordpress » (pilier)"),
      tod("Produire et publier « FluentCRM vs MailerLite »"),
      tod("Intégrer le CTA Audit dans les articles publiés"),
      tod("Configurer le tracking affiliation FluentCRM"),
      tod("Mettre en place la newsletter (Brevo ou MailPoet)"),
    ]),
    tog("📋 Semaine 5–8 — Pipeline & Signaux", [
      p(""),
      tod("Produire 3 articles supplémentaires du cluster CRM"),
      tod("Activer l'annonce LinkedIn de positionnement (pas de vente, angle pédagogique)"),
      tod("Préparer 1 post LinkedIn par semaine issu des articles schoolsWP (W3 linkedin)"),
      tod("Chercher activement 1 projet test (prix réduit contre étude de cas)"),
      tod("Mesurer : nombre de formulaires remplis, appels demandés, clics CTA"),
    ]),
    tog("📋 Semaine 9–12 — Validation Conditions Départ", [
      p(""),
      tod("Vérifier la checklist des 7 conditions de départ"),
      tod("Évaluer la trésorerie sécurité (objectif : > 15 000 €)"),
      tod("Évaluer le pipeline (objectif : 1 projet signé ou 2 prospects chauds)"),
      tod("Prendre la décision : départ dans X semaines ou prolongation Phase 1"),
      tod("Si GO : enclencher la procédure de sortie (rupture conventionnelle ou préavis)"),
    ]),
    p(""),

    h2("90 à 180 jours — Valider le modèle"),
    p(""),
    tog("📋 M3–M4 — Premières références", [
      p(""),
      tod("Réaliser 2 à 3 missions WBS avec rigueur et documentation"),
      tod("Collecter 2 témoignages structurés (résultat avant/après)"),
      tod("Produire la 1ère étude de cas client (avec permission)"),
      tod("Publier l'étude de cas sur schoolsWP + LinkedIn"),
      tod("Proposer la maintenance WBS à chaque client en fin de mission"),
    ]),
    tog("📋 M4–M5 — Ajustements & Récurrence", [
      p(""),
      tod("Évaluer le taux de conversion appels → projets (objectif > 40 %)"),
      tod("Ajuster le pricing si > 60 % de conversion (signe de pricing trop bas)"),
      tod("Structurer le MRR maintenance : objectif 3 clients actifs"),
      tod("Continuer le cluster CRM : 1 article par semaine, LLM-optimisé"),
      tod("Démarrer les articles du cluster LMS (pont naturel avec le cluster CRM)"),
    ]),
    tog("📋 M5–M6 — Stabilisation & Projection", [
      p(""),
      tod("Évaluer le CA cumulé vs objectif (objectif M6 : > 20 000 € CA SASU)"),
      tod("Mesurer le MRR : objectif M6 : 1 200 à 2 500 €/mois récurrents"),
      tod("Planifier Année 2 : niche LMS ? Cluster LMS ? Embauche sous-traitant ?"),
      tod("Revue stratégique complète : offre, pricing, positioning, schoolsWP"),
      tod("Célébrer — tu as validé le modèle. C'est le vrai signal de réussite."),
    ]),
    p(""),
    div()
  );

  // ───────────────────────────────────────────
  // TRACKER MENSUEL
  // ───────────────────────────────────────────
  blocks.push(
    h1("📊 Tracker Mensuel — À Remplir en Temps Réel"),
    p("")
  );

  const moisLabels = ["M-2 (Prép.)", "M-1 (Prép.)", "M0 (Sortie)", "M1", "M2", "M3", "M4", "M5", "M6"];
  for (const mois of moisLabels) {
    blocks.push(
      tog(`📅 ${mois}`, [
        p(""),
        p(rt("CA encaissé : ", { bold: true }), rt("____ €")),
        p(rt("CA signé : ", { bold: true }), rt("____ €")),
        p(rt("MRR actif : ", { bold: true }), rt("____ €/mois")),
        p(rt("Appels découverte : ", { bold: true }), rt("____ appels")),
        p(rt("Projets signés : ", { bold: true }), rt("____ projets")),
        p(rt("Articles publiés : ", { bold: true }), rt("____ articles")),
        p(rt("Leads Audit entrants : ", { bold: true }), rt("____ leads")),
        p(rt("Affiliation cumulée : ", { bold: true }), rt("____ €")),
        p(rt("Trésorerie SASU : ", { bold: true }), rt("____ €")),
        p(rt("Trésorerie perso : ", { bold: true }), rt("____ €")),
        p(""),
        p(rt("Note / Apprentissage clé du mois :", { bold: true })),
        p(""),
      ])
    );
  }

  blocks.push(div());

  // ───────────────────────────────────────────
  // VISION FINALE
  // ───────────────────────────────────────────
  blocks.push(
    h1("🧩 Vision — Dans 18 Mois"),
    p(""),
    tog("📌 État cible M18 — SASU WordPress stable et scalable", [
      p(""),
      p(rt("schoolsWP", { bold: true })),
      bul("Cluster CRM dominé (14 articles, Top 5 sur « crm wordpress »)"),
      bul("Cluster LMS en cours (8 articles publiés)"),
      bul("Newsletter : 800 à 1 500 abonnés qualifiés"),
      bul("Affiliation : 500 à 1 000 €/mois récurrents"),
      p(""),
      p(rt("SASU WordPress Business System™", { bold: true })),
      bul("8 à 12 missions WBS réalisées"),
      bul("Tarif moyen mission M18 : 6 000 à 10 000 €"),
      bul("MRR maintenance : 2 000 à 5 000 €/mois"),
      bul("3 à 5 études de cas publiées avec résultats réels"),
      bul("0 démarchage — pipeline 100 % inbound"),
      p(""),
      p(rt("Situation personnelle", { bold: true })),
      bul("Salaire SASU : 2 000 à 2 500 €/mois brut (optimisé IS + dividendes)"),
      bul("Trésorerie SASU : 20 000 à 40 000 € (réserve + provisions)"),
      bul("Temps de travail : 4 jours/semaine (missions + contenu)"),
      bul("Holding en réflexion si CA > 120 000 €"),
    ]),
    p(""),
    cal(
      "Ta transition n'est pas un pari. C'est une architecture. Chaque condition remplie est une brique posée. Quand la maison est stable, tu entres dedans.",
      "🧭", "purple_background"
    )
  );

  return blocks;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  console.log("🚀 Création de la page Architecture de Transition — Salarié → SASU WordPress...");

  const template = buildTemplate();
  const batches = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`\n📦 ${template.length} blocs · ${batches.length} batch(es)`);

  // Batch 1 — Création de la page
  console.log(`\n📄 Création de la page (batch 1/${batches.length})...`);
  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🧭" },
    properties: {
      title: {
        title: [
          { type: "text", text: { content: "🧭 Architecture de Transition — Salarié → SASU WordPress" } },
        ],
      },
    },
    children: batches[0],
  });

  const pageId = page.id;
  console.log(`  ✅ Page créée : ${page.url}`);

  // Batches suivants
  for (let i = 1; i < batches.length; i++) {
    await sleep(600);
    console.log(`\n📦 Ajout batch ${i + 1}/${batches.length}...`);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, {
      children: batches[i],
    });
    console.log(`  ✅ Batch ${i + 1} ajouté`);
  }

  console.log("\n✅  Page créée avec succès !");
  console.log(`   URL : ${page.url}`);
  console.log("\n   Sections :");
  console.log("   🧠  Principe Fondateur — les 3 erreurs + la règle unique");
  console.log("   🟡  Phase 1 — Stabilisation (4 questions offre + calcul trésorerie + pont schoolsWP)");
  console.log("   🔴  Checklist Départ — 7 conditions non négociables (checkboxes)");
  console.log("   🟠  Phase 2 — Lancement SASU (timing, règles, positionnement J1)");
  console.log("   🟢  Phase 3 — 6 mois post-départ (objectifs chiffrés M1-M2 / M3-M4 / M5-M6)");
  console.log(`   💰  Objectifs An1 — CA ${(40000).toLocaleString("fr")}–${(65000).toLocaleString("fr")} € + MRR`);
  console.log("   🧠  Sécurité mentale — 5 signaux GO + 3 alarmes + question clé");
  console.log("   🗺  Roadmap 0–90j + 90–180j (checkboxes par semaine)");
  console.log("   📊  Tracker mensuel M-2 à M6 (9 toggles à remplir en temps réel)");
  console.log("   🧩  Vision M18 — état cible schoolsWP + SASU + situation perso");
}

main().catch((err) => {
  console.error("❌ Erreur :", err.message);
  process.exit(1);
});
