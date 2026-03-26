#!/usr/bin/env node
"use strict";

/**
 * setup-notion-roadmap-b2b-24mois.js
 * Crée la page Notion : 🗺 Roadmap 24 mois — Domination Niche Formateurs B2B WordPress
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-roadmap-b2b-24mois.js
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;
const NOTION_VERSION = "2022-06-28";
const CHUNK = 90;

if (!NOTION_API_KEY || !PARENT_PAGE_ID) {
  console.error("❌  Variables manquantes : NOTION_API_KEY et NOTION_PARENT_PAGE_ID requis.");
  process.exit(1);
}

// ─── DATA ────────────────────────────────────────────────────────────────────

const VISION = {
  position_cible: "L'architecte WordPress des formateurs B2B francophones",
  position_pas: "Expert WordPress",
  caracteristiques: [
    "Position rare — personne ne l'occupe encore en FR",
    "Marché solvable — budget élevé, cycle long, renouvellement",
    "Concurrence floue — aucun freelance ne se positionne explicitement B2B",
    "Autorité cumulable — SEO + LinkedIn + études de cas + AI Overviews",
  ],
  formule_positionnement: "J'aide les formateurs B2B à structurer un système WordPress rentable, automatisé et scalable.",
};

const PHASES = [
  {
    num: "1",
    emoji: "🧭",
    label: "FONDATIONS STRATÉGIQUES",
    periode: "Mois 1 – 6",
    couleur: "blue_background",
    objectif: "Clarifier le positionnement · Poser le premier cluster fort · Signer 3–5 premiers clients B2B.",
    jalon_go: "3 missions B2B signées + pilier LMS publié + profil LinkedIn mis à jour",
    finances: {
      mini: { audit: 2 * 1500, core: 1 * 5000, mrr: 0 },
      cible: { audit: 3 * 1800, core: 2 * 6000, mrr: 0 },
    },
    sous_phases: [
      {
        num: "1.1",
        emoji: "🧱",
        titre: "Positionnement officiel",
        actions: [
          { action: "Mettre à jour la bio schoolsWP.com", detail: "Formule exacte : 'J'aide les formateurs B2B à structurer un système WordPress rentable, automatisé et scalable.'", statut: "todo" },
          { action: "Refondre la page À propos schoolsWP.com", detail: "Focus B2B. Pas d'audience généraliste. Architecture, rentabilité, automatisation.", statut: "todo" },
          { action: "Créer la page /audit-b2b", detail: "Landing page audit Architecture B2B (1 200–1 800 €). Formulaire qualifiant 5 questions.", statut: "todo" },
          { action: "Mettre à jour la signature LinkedIn", detail: "Tagline : 'Architecte WordPress B2B · schoolsWP' · Lien bio vers /audit-b2b", statut: "todo" },
          { action: "Rédiger et publier la section À propos LinkedIn", detail: "Texte complet axé formateurs B2B. Problème → Solution → Résultat → CTA.", statut: "todo" },
          { action: "Créer la bannière LinkedIn B2B", detail: "'Architecture WordPress B2B · LMS + CRM + Automatisation · schoolsWP'", statut: "todo" },
        ],
      },
      {
        num: "1.2",
        emoji: "📚",
        titre: "Cluster Prioritaire #1 — LMS WordPress B2B",
        articles: [
          {
            type: "PILIER",
            titre: "Structurer un LMS WordPress pour formateurs B2B — Guide complet",
            slug: "lms-wordpress-formateurs-b2b",
            longueur: "4 000 – 5 000 mots",
            intent: "informationnelle experte",
            mois_cible: "M1",
            priorite: "🔴",
            structure: [
              "Pourquoi un LMS standard ne suffit pas en B2B",
              "Architecture multi-entreprises (comptes, cohortes, accès groupés)",
              "CRM intégré : segmentation décideur / apprenant / RH",
              "Onboarding automatisé step-by-step",
              "Reporting formateur : KPIs B2B réels",
              "QUALIOPI et WordPress : ce qu'il faut configurer",
              "Stack recommandé + coût estimé",
              "CTA Audit Architecture B2B",
            ],
          },
          {
            type: "SATELLITE",
            titre: "Gérer plusieurs comptes entreprise sur Tutor LMS",
            slug: "comptes-entreprise-multi-utilisateurs-tutor-lms",
            longueur: "2 000 – 2 500 mots",
            intent: "informationnelle technique",
            mois_cible: "M1",
            priorite: "🔴",
          },
          {
            type: "SATELLITE",
            titre: "Reporting apprenants entreprise WordPress : quels KPIs pour vos clients RH ?",
            slug: "reporting-apprenants-entreprise-wordpress",
            longueur: "1 800 – 2 200 mots",
            intent: "informationnelle",
            mois_cible: "M2",
            priorite: "🟠",
          },
          {
            type: "SATELLITE",
            titre: "Tutor LMS pour corporate : configuration avancée multi-organisations",
            slug: "tutor-lms-corporate-configuration-avancee",
            longueur: "2 000 – 2 500 mots",
            intent: "informationnelle technique",
            mois_cible: "M2",
            priorite: "🟠",
          },
          {
            type: "SATELLITE",
            titre: "Sécuriser les accès formation B2B sur WordPress : guide complet",
            slug: "securiser-acces-formation-b2b-wordpress",
            longueur: "1 800 – 2 000 mots",
            intent: "informationnelle",
            mois_cible: "M3",
            priorite: "🟡",
          },
          {
            type: "SATELLITE",
            titre: "Paiement et facturation entreprise sur WordPress : structurer le cycle B2B",
            slug: "paiement-facturation-entreprise-wordpress",
            longueur: "1 800 – 2 200 mots",
            intent: "informationnelle → décisionnelle",
            mois_cible: "M3",
            priorite: "🟡",
          },
        ],
        maillage: "Chaque satellite → pilier (lien ancre naturelle). Pilier → chaque satellite (section dédiée).",
      },
      {
        num: "1.3",
        emoji: "💰",
        titre: "Offre Signature V1 — Audit & Architecture",
        actions: [
          { action: "Finaliser les 3 niveaux de prix", detail: "Audit (1 200–1 800 €) · Core System (4 500–7 000 €) · Full System (8 000–15 000 €)", statut: "todo" },
          { action: "Créer le template de devis Audit (Niveau 1)", detail: "PDF SASU propre. Délais. Livrables. Acompte 40%.", statut: "todo" },
          { action: "Signer 3 à 5 premiers clients B2B", detail: "Cible : OFs indépendants, consultants formateurs B2B, entrepreneurs académiques.", statut: "todo" },
          { action: "Documenter chaque mission (photos, données, résultats)", detail: "Matière première pour études de cas M4-M6.", statut: "todo" },
          { action: "Collecter 1 témoignage par client livré", detail: "Texte + si possible vidéo courte (1-2 min). Stocké dans Notion.", statut: "todo" },
        ],
        kpis: [
          "3 à 5 audits signés avant fin M6",
          "2 à 3 missions Core System démarrées",
          "1 pilier + 5 satellites publiés",
          "Profil LinkedIn B2B à jour",
          "Page /audit-b2b active et testée",
          "Score Autorité Pilier LMS > 70 (PillarAuthorityAgent)",
        ],
      },
    ],
    ca_estime: {
      mini: 2 * 1500 + 1 * 5000,
      cible: 3 * 1800 + 2 * 6000,
    },
    risques: [
      "Procrastination sur le positionnement → forcer la décision en M1",
      "Pas de clients B2B → vérifier les DM LinkedIn et relancer le réseau existant",
      "Articles pas indexés → vérifier Search Console, sitemap, crawl budget",
    ],
  },
  {
    num: "2",
    emoji: "🚀",
    label: "EXPANSION & AUTORITÉ",
    periode: "Mois 7 – 12",
    couleur: "green_background",
    objectif: "Devenir identifiable comme spécialiste B2B WordPress. Installer l'autorité SEO. Premiers AI Overviews.",
    jalon_go: "3 études de cas publiées + cluster CRM publié + 5–10 leads qualifiés / trimestre",
    finances: {
      mini: { audit: 3 * 1500, core: 2 * 5000, mrr: 2 * 1000 },
      cible: { audit: 4 * 1800, core: 3 * 7000, mrr: 3 * 1500 },
    },
    sous_phases: [
      {
        num: "2.1",
        emoji: "🧠",
        titre: "Cluster #2 — CRM & Automatisation B2B",
        articles: [
          {
            type: "PILIER",
            titre: "CRM WordPress pour formateurs B2B : pipeline, automatisation et renouvellement",
            slug: "crm-wordpress-formateurs-b2b",
            longueur: "3 500 – 4 500 mots",
            intent: "informationnelle experte",
            mois_cible: "M7",
            priorite: "🔴",
          },
          {
            type: "SATELLITE",
            titre: "Segmentation entreprise WordPress : décideur, apprenant, RH",
            slug: "segmentation-entreprise-wordpress-crm",
            longueur: "1 800 – 2 200 mots",
            intent: "informationnelle",
            mois_cible: "M7",
            priorite: "🔴",
          },
          {
            type: "SATELLITE",
            titre: "Automatisation onboarding formation entreprise avec FluentCRM",
            slug: "automatisation-onboarding-formation-entreprise-fluentcrm",
            longueur: "2 000 – 2 500 mots",
            intent: "informationnelle → décisionnelle",
            mois_cible: "M8",
            priorite: "🟠",
          },
          {
            type: "SATELLITE",
            titre: "Pipeline devis B2B WordPress : structurer et automatiser",
            slug: "pipeline-devis-b2b-wordpress",
            longueur: "1 800 – 2 000 mots",
            intent: "informationnelle",
            mois_cible: "M8",
            priorite: "🟠",
          },
          {
            type: "SATELLITE",
            titre: "Automatiser les relances renouvellement contrat formation B2B",
            slug: "automatiser-relances-renouvellement-contrat-formation",
            longueur: "1 800 – 2 200 mots",
            intent: "décisionnelle",
            mois_cible: "M9",
            priorite: "🟡",
          },
        ],
      },
      {
        num: "2.2",
        emoji: "📈",
        titre: "Contenu Décisionnel Fort",
        articles: [
          {
            type: "COMPARATIF",
            titre: "Quel LMS WordPress pour entreprise en 2026 ? Comparatif B2B complet",
            slug: "quel-lms-wordpress-entreprise-comparatif",
            longueur: "2 500 – 3 500 mots",
            intent: "comparative décisionnelle",
            mois_cible: "M9",
            priorite: "🔴",
          },
          {
            type: "COMPARATIF",
            titre: "FluentCRM pour formation B2B : est-ce le bon choix ?",
            slug: "fluentcrm-formation-b2b-avis",
            longueur: "2 000 – 2 500 mots",
            intent: "comparative",
            mois_cible: "M10",
            priorite: "🟠",
          },
          {
            type: "GUIDE",
            titre: "Comment gérer 10 entreprises clientes sur WordPress LMS",
            slug: "gerer-10-entreprises-wordpress-lms",
            longueur: "2 500 – 3 000 mots",
            intent: "informationnelle → décisionnelle",
            mois_cible: "M10",
            priorite: "🟠",
          },
        ],
      },
      {
        num: "2.3",
        emoji: "🏢",
        titre: "Études de Cas & Preuves Sociales",
        actions: [
          { action: "Publier 3 études de cas détaillées", detail: "Format : Contexte client → Problème → Architecture mise en place → Résultats mesurés (chiffres)", statut: "todo" },
          { action: "Obtenir 1 témoignage vidéo", detail: "1-2 min. Smartphone ou Loom. Pas besoin de production pro. Authenticité > qualité.", statut: "todo" },
          { action: "Créer une page /resultats sur schoolswp.com", detail: "Études de cas + témoignages + KPIs agrégés (temps gagné, taux renouvellement, CA impact)", statut: "todo" },
          { action: "Publier les études de cas sur LinkedIn", detail: "Format post résumé avec hook fort. Lien vers version complète sur le site.", statut: "todo" },
        ],
        format_etude_cas: {
          sections: [
            "Contexte client (secteur, taille, situation avant)",
            "Problème précis (avec chiffres si possible)",
            "Architecture mise en place (LMS + CRM + automatisations)",
            "Résultats mesurés à J+30, J+60, J+90",
            "Ce que le client dit (témoignage direct)",
            "CTA Audit Architecture B2B",
          ],
        },
        kpis: [
          "3 études de cas publiées sur le site",
          "1 témoignage vidéo obtenu et publié",
          "5 pilier CRM publié avec maillage complet",
          "3 articles décisionnels publiés",
          "5 à 10 leads qualifiés / trimestre entrants",
          "Premières apparitions en AI Overviews (Thruuu monitoring)",
          "Top 10 sur 2 requêtes niche longue traîne",
        ],
      },
    ],
    ca_estime: {
      mini: 3 * 1500 + 2 * 5000 + 2 * 1000 * 6,
      cible: 4 * 1800 + 3 * 7000 + 3 * 1500 * 6,
    },
    risques: [
      "Études de cas sans données → demander aux clients des chiffres même approximatifs",
      "Cluster CRM moins performant → renforcer le maillage avec cluster LMS",
      "AI Overviews absents → optimiser format question/réponse dans les H2",
    ],
  },
  {
    num: "3",
    emoji: "💎",
    label: "PREMIUM & SCALING",
    periode: "Année 2 (Mois 13 – 24)",
    couleur: "purple_background",
    objectif: "Augmenter le panier moyen. Installer l'autorité définitive. Lancer le produit signature.",
    jalon_go: "Panier moyen > 8 000 € · Produit digital lancé · 3 clusters actifs · MRR > 5 000 €/mois",
    finances: {
      mini: { core: 3 * 7000, full: 2 * 10000, mrr: 4 * 1200, produit: 20 * 297 },
      cible: { core: 4 * 7000, full: 3 * 12000, mrr: 6 * 1800, produit: 40 * 497 },
    },
    sous_phases: [
      {
        num: "3.1",
        emoji: "🧱",
        titre: "Augmentation Prix & Positionnement Premium",
        actions: [
          { action: "Réviser les prix à la hausse (M13)", detail: "Niveau 2 → 6 000–9 000 €. Niveau 3 → 12 000–18 000 €. Basé sur résultats clients + autorité SEO établie.", statut: "todo" },
          { action: "Créer un processus de sélection client", detail: "Formulaire audit plus exigeant. Entretien obligatoire avant devis. Refuser 30% des leads (positionnement rareté).", statut: "todo" },
          { action: "Ajouter un accompagnement mensuel premium", detail: "1 200–2 000 €/mois. 3–5 clients max. Sessions stratégiques + optimisations continues.", statut: "todo" },
          { action: "Documenter 5+ études de cas avec ROI précis", detail: "CA impact, taux renouvellement, temps gagné. Chiffres réels.", statut: "todo" },
        ],
      },
      {
        num: "3.2",
        emoji: "🟣",
        titre: "Produit Signature B2B",
        options: [
          {
            option: "A",
            type: "Formation",
            nom: "Construire votre écosystème WordPress B2B",
            format: "6 à 8 modules · vidéos + templates + checklists",
            prix: "497 – 997 €",
            cible: "Formateurs B2B qui veulent se former avant d'implémenter ou de déléguer",
            avantages: "MRR stable · Scalable · Génère des leads qualifiés qui deviennent ensuite clients agency",
            inconvenients: "Délai de production : 6–8 semaines · Support communautaire à prévoir",
          },
          {
            option: "B",
            type: "Template Système",
            nom: "B2B WordPress System™ — Template prêt à configurer",
            format: "Package ZIP · Child theme + configuration LMS + CRM + automatisations pré-configurées",
            prix: "297 – 497 €",
            cible: "Formateurs B2B avec un développeur ou un minimum de technique",
            avantages: "Production rapide (3–4 semaines) · Pas de support complexe · CTA naturel vers les missions",
            inconvenients: "Valeur perçue plus basse qu'une formation · Moins de MRR récurrent",
          },
          {
            option: "C (recommandée)",
            type: "Bundle",
            nom: "Template + Guide d'implémentation",
            format: "Template B2B + Guide vidéo 4 modules (2h) + 1 session Q&A de groupe/mois",
            prix: "397 – 697 €",
            cible: "Formateurs B2B avec profil DIY qui veulent un guide + ressources",
            avantages: "Meilleur rapport valeur/production · Leads warm → clients agency naturels",
            inconvenients: "Q&A mensuel à cadencer · Besoin de 30–50 ventes/an pour être rentable",
          },
        ],
        kpis_produit: [
          "Lancement M15 (après 3 études de cas publiées)",
          "Objectif An2 : 20–40 ventes/mois",
          "Prix cible : 397 € (option C)",
          "CA produit mensuel cible : 8 000 – 16 000 €/mois",
          "Taux de conversion acheteur produit → client agency : 5–15%",
        ],
      },
      {
        num: "3.3",
        emoji: "📊",
        titre: "Cluster #3 — Performance & Optimisation B2B",
        articles: [
          {
            type: "PILIER",
            titre: "Optimiser les KPIs de formation entreprise sur WordPress",
            slug: "kpi-formation-entreprise-wordpress-optimisation",
            longueur: "3 500 – 4 000 mots",
            intent: "informationnelle experte",
            mois_cible: "M15",
            priorite: "🟠",
          },
          {
            type: "SATELLITE",
            titre: "Taux de renouvellement contrat formation B2B : comment l'améliorer",
            slug: "taux-renouvellement-contrat-formation-b2b",
            longueur: "1 800 – 2 200 mots",
            intent: "décisionnelle",
            mois_cible: "M16",
            priorite: "🟠",
          },
          {
            type: "SATELLITE",
            titre: "Upsell formation avancée B2B : structurer l'offre montante",
            slug: "upsell-formation-avancee-b2b-wordpress",
            longueur: "1 800 – 2 000 mots",
            intent: "informationnelle",
            mois_cible: "M17",
            priorite: "🟡",
          },
          {
            type: "SATELLITE",
            titre: "Reporting avancé formation B2B WordPress : dashboard dirigeant",
            slug: "reporting-avance-formation-b2b-dashboard",
            longueur: "2 000 – 2 500 mots",
            intent: "informationnelle",
            mois_cible: "M18",
            priorite: "🟡",
          },
        ],
      },
    ],
    ca_estime: {
      mini: 3 * 7000 + 2 * 10000 + 4 * 1200 * 12 + 20 * 297 * 12,
      cible: 4 * 7000 + 3 * 12000 + 6 * 1800 * 12 + 40 * 497 * 12,
    },
    risques: [
      "Lancement produit trop tôt → attendre 3 études de cas publiées minimum",
      "MRR stagnant → relancer les clients livrés avec proposition accompagnement",
      "Augmentation prix mal acceptée → s'appuyer sur les témoignages et résultats",
    ],
  },
];

const KPIS_24_MOIS = {
  seo: [
    { kpi: "Clusters dominés", objectif_m12: "2 clusters (LMS + CRM)", objectif_m24: "3 clusters (LMS + CRM + Performance)" },
    { kpi: "Articles B2B publiés", objectif_m12: "17 articles", objectif_m24: "30–40 articles ciblés" },
    { kpi: "Position requêtes niche", objectif_m12: "Top 10 sur 3 requêtes", objectif_m24: "Top 5 sur 5 requêtes" },
    { kpi: "AI Overviews présence", objectif_m12: "Début (2–3 sujets)", objectif_m24: "Régulier sur 8–10 requêtes clés" },
    { kpi: "Autorité domaine (DR)", objectif_m12: "DR 20–30", objectif_m24: "DR 30–45" },
    { kpi: "Trafic organique cluster B2B", objectif_m12: "500–1 000 /mois", objectif_m24: "2 000–5 000 /mois" },
  ],
  agency: [
    { kpi: "Projets B2B réalisés", objectif_m12: "5–8 missions", objectif_m24: "15–25 missions" },
    { kpi: "Panier moyen mission", objectif_m12: "> 5 500 €", objectif_m24: "> 9 000 €" },
    { kpi: "Taux de renouvellement client", objectif_m12: "> 30%", objectif_m24: "> 50%" },
    { kpi: "MRR accompagnement", objectif_m12: "2 000–4 000 €/mois", objectif_m24: "5 000–10 000 €/mois" },
    { kpi: "Leads qualifiés entrants", objectif_m12: "5–10/trimestre", objectif_m24: "10–20/trimestre" },
    { kpi: "Taux closing audit → mission", objectif_m12: "> 40%", objectif_m24: "> 55%" },
  ],
  produit: [
    { kpi: "Produit signature lancé", objectif_m12: "—", objectif_m24: "Oui (M15 au plus tard)" },
    { kpi: "Ventes produit / mois", objectif_m12: "—", objectif_m24: "20–40 ventes/mois" },
    { kpi: "CA produit mensuel", objectif_m12: "—", objectif_m24: "8 000–20 000 €/mois" },
    { kpi: "Taux conversion acheteur → client agency", objectif_m12: "—", objectif_m24: "5–15%" },
    { kpi: "Affiliation mensuelle", objectif_m12: "500–1 500 €/mois", objectif_m24: "2 000–4 000 €/mois" },
  ],
};

// ─── CALC ─────────────────────────────────────────────────────────────────────

const calcPhase = (fin) => Object.values(fin).reduce((a, b) => a + b, 0);

const ca_phase1 = { mini: PHASES[0].ca_estime.mini, cible: PHASES[0].ca_estime.cible };
const ca_phase2 = { mini: PHASES[1].ca_estime.mini, cible: PHASES[1].ca_estime.cible };
const ca_phase3 = { mini: PHASES[2].ca_estime.mini, cible: PHASES[2].ca_estime.cible };

const ca_total = {
  mini: ca_phase1.mini + ca_phase2.mini + ca_phase3.mini,
  cible: ca_phase1.cible + ca_phase2.cible + ca_phase3.cible,
};

const total_articles = 6 + 5 + 3 + 4;  // cluster1 + cluster2 + décisionnels + cluster3

// ─── NOTION HELPERS ───────────────────────────────────────────────────────────

async function notionRequest(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      "Notion-Version": NOTION_VERSION,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const json = await resp.json();
  if (!resp.ok) throw new Error(`Notion ${resp.status}: ${JSON.stringify(json)}`);
  return json;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

// ─── BLOCK BUILDERS ──────────────────────────────────────────────────────────

const rt = (text, opts = {}) => ({
  type: "text",
  text: { content: String(text) },
  annotations: {
    bold: opts.bold || false,
    italic: opts.italic || false,
    code: opts.code || false,
    color: opts.color || "default",
  },
});

const h1 = (text) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(text)] } });
const h2 = (text) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(text)] } });
const h3 = (text) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(text)] } });
const p = (rts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const bul = (rts, color = "default") => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)], color } });
const num = (rts) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const qot = (text, color = "gray_background") => ({ object: "block", type: "quote", quote: { rich_text: Array.isArray(text) ? text : [rt(text)], color } });
const cal = (text, color = "blue_background") => ({
  object: "block",
  type: "callout",
  callout: {
    rich_text: Array.isArray(text) ? text : [rt(text)],
    icon: { type: "emoji", emoji: "💡" },
    color,
  },
});
const tog = (text, children = []) => ({
  object: "block",
  type: "toggle",
  toggle: { rich_text: [rt(text, { bold: true })], children },
});
const todo = (text, checked = false) => ({
  object: "block",
  type: "to_do",
  to_do: { rich_text: [rt(text)], checked },
});

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("🗺 Roadmap 24 Mois — Domination Niche Formateurs B2B WordPress · schoolsWP · Confidentiel", "yellow_background"));
  blocks.push(p([
    rt("Sans dispersion. Sans bruit. Avec logique.", { italic: true, bold: true }),
    rt(`  ·  ${total_articles} articles · 3 clusters · 3 phases · 1 produit signature`, { italic: true, color: "gray" }),
  ]));
  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🏆 Vision — Position Finale"));
  blocks.push(p(""));
  blocks.push(cal([
    rt("Tu ne seras plus : ", {}),
    rt('"Expert WordPress"', { italic: true }),
    rt("\nTu seras : "),
    rt(VISION.position_cible, { bold: true, color: "green" }),
  ], "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Formule de positionnement"));
  blocks.push(qot(VISION.formule_positionnement, "blue_background"));
  blocks.push(p(""));

  blocks.push(h2("Pourquoi cette position est tenable"));
  VISION.caracteristiques.forEach((c) => blocks.push(bul([rt("✓  " + c, { bold: true, color: "green" })], "green_background")));
  blocks.push(div());

  // ── VUE D'ENSEMBLE ──
  blocks.push(h1("📋 Vue d'Ensemble — 24 Mois"));
  blocks.push(p(""));

  const vue = [
    ["Phase", "Période", "Focus", "Livrables clés", "CA estimé"],
    ["P1 🧭", "M1–M6", "Fondations", "Cluster LMS · 5 missions · Positionnement", `${ca_phase1.mini.toLocaleString("fr-FR")} – ${ca_phase1.cible.toLocaleString("fr-FR")} €`],
    ["P2 🚀", "M7–M12", "Expansion", "Cluster CRM · Études de cas · AI Overviews", `${ca_phase2.mini.toLocaleString("fr-FR")} – ${ca_phase2.cible.toLocaleString("fr-FR")} €`],
    ["P3 💎", "M13–M24", "Premium", "Produit · Cluster Performance · MRR", `${ca_phase3.mini.toLocaleString("fr-FR")} – ${ca_phase3.cible.toLocaleString("fr-FR")} €`],
  ];

  vue.forEach((row, i) => {
    blocks.push(bul(
      [rt(row.join("  ·  "), { bold: i === 0, code: i === 0 })],
      i === 0 ? "gray_background" : "default"
    ));
  });

  blocks.push(p(""));
  blocks.push(bul([
    rt("CA total estimé 24 mois : ", { bold: true }),
    rt(`${ca_total.mini.toLocaleString("fr-FR")} € (conservateur) – ${ca_total.cible.toLocaleString("fr-FR")} € (cible)`, { bold: true, color: "green" }),
  ]));
  blocks.push(div());

  // ── PHASES ──
  for (const phase of PHASES) {
    blocks.push(h1(`${phase.emoji} Phase ${phase.num} — ${phase.label}  (${phase.periode})`));
    blocks.push(cal([rt(phase.objectif)], phase.couleur));
    blocks.push(p(""));
    blocks.push(p([rt("🎯 Jalon GO : ", { bold: true }), rt(phase.jalon_go, { italic: true })]));
    blocks.push(p([
      rt("💶 CA estimé : ", { bold: true }),
      rt(`${phase.ca_estime.mini.toLocaleString("fr-FR")} € – ${phase.ca_estime.cible.toLocaleString("fr-FR")} €`, { bold: true, color: "green" }),
    ]));
    blocks.push(p(""));

    for (const sp of phase.sous_phases) {
      blocks.push(h2(`${sp.emoji} ${sp.num} — ${sp.titre}`));

      // Actions avec todo
      if (sp.actions) {
        for (const a of sp.actions) {
          const children = [
            p([rt("Détail : ", { bold: true }), rt(a.detail, { italic: true })]),
          ];
          blocks.push(tog(`☐  ${a.action}`, children));
          blocks.push(p(""));
        }
      }

      // Articles
      if (sp.articles) {
        blocks.push(h3("Articles à produire"));
        for (const art of sp.articles) {
          const children = [];
          children.push(p([rt("Type : ", { bold: true }), rt(art.type, { code: true })]));
          children.push(p([rt("Slug : ", { bold: true }), rt(art.slug, { code: true })]));
          children.push(p([rt("Longueur : ", { bold: true }), rt(art.longueur)]));
          children.push(p([rt("Intention : ", { bold: true }), rt(art.intent)]));
          children.push(p([rt("Mois cible : ", { bold: true }), rt(art.mois_cible, { bold: true, color: "green" })]));
          if (art.structure) {
            children.push(p(""));
            children.push(h3("Structure recommandée"));
            art.structure.forEach((s, i) => children.push(num(`${s}`)));
          }
          blocks.push(tog(`${art.priorite}  ${art.titre}`, children));
          blocks.push(p(""));
        }

        if (sp.maillage) {
          blocks.push(p([rt("→ Maillage : ", { bold: true, color: "gray" }), rt(sp.maillage, { italic: true })]));
          blocks.push(p(""));
        }
      }

      // Options produit
      if (sp.options) {
        for (const opt of sp.options) {
          const children = [];
          children.push(p([rt("Type : ", { bold: true }), rt(opt.type)]));
          children.push(p([rt("Format : ", { bold: true }), rt(opt.format)]));
          children.push(p([rt("Prix : ", { bold: true }), rt(opt.prix, { bold: true, color: "green" })]));
          children.push(p([rt("Cible : ", { bold: true }), rt(opt.cible)]));
          children.push(p([rt("✓ Avantages : ", { bold: true, color: "green" }), rt(opt.avantages, { italic: true })]));
          children.push(p([rt("⚠ Inconvénients : ", { bold: true, color: "red" }), rt(opt.inconvenients, { italic: true })]));
          blocks.push(tog(`Option ${opt.option} — ${opt.nom}  ·  ${opt.prix}`, children));
          blocks.push(p(""));
        }

        if (sp.kpis_produit) {
          blocks.push(h3("KPIs Produit Signature"));
          sp.kpis_produit.forEach((k) => blocks.push(bul(k)));
          blocks.push(p(""));
        }
      }

      // Format étude de cas
      if (sp.format_etude_cas) {
        blocks.push(h3("Format standard étude de cas"));
        sp.format_etude_cas.sections.forEach((s, i) => blocks.push(num(`${s}`)));
        blocks.push(p(""));
      }

      // KPIs de sous-phase
      if (sp.kpis) {
        blocks.push(h3(`KPIs ${sp.num}`));
        sp.kpis.forEach((k) => blocks.push(todo(k)));
        blocks.push(p(""));
      }
    }

    // Risques par phase
    if (phase.risques) {
      blocks.push(h2("⚠️ Risques & Plans B"));
      phase.risques.forEach((r) => blocks.push(bul([rt("⚠  " + r)], "red_background")));
    }

    blocks.push(div());
  }

  // ── KPIs 24 MOIS ──
  blocks.push(h1("📈 KPIs 24 Mois — Tableau de Bord"));
  blocks.push(p(""));

  for (const [cat, items] of Object.entries(KPIS_24_MOIS)) {
    const label = cat === "seo" ? "🔵 SEO" : cat === "agency" ? "🟢 Agency" : "🟣 Produit";
    const children = [];
    children.push(p(""));
    children.push(bul([rt("KPI  ·  Objectif M12  ·  Objectif M24", { bold: true, code: true })], "gray_background"));
    items.forEach((item) => {
      children.push(bul([
        rt(`${item.kpi} : `, { bold: true }),
        rt(`${item.objectif_m12} `, { color: "blue" }),
        rt("→ ", {}),
        rt(`${item.objectif_m24}`, { bold: true, color: "green" }),
      ]));
    });
    blocks.push(tog(label, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── PILOTAGE MENSUEL ──
  blocks.push(h1("🗓 Pilotage Mensuel — 30 minutes par mois"));
  blocks.push(p([rt("Le 1er lundi de chaque mois. 4 dimensions. 30 minutes max.", { italic: true })]));
  blocks.push(p(""));

  const pilotage = [
    { dim: "SEO", questions: ["Nouveaux articles publiés ce mois ?", "Positions GSC sur les requêtes clés (±) ?", "Nouvelles mentions AI Overviews ?"] },
    { dim: "Agency", questions: ["Leads qualifiés entrants ?", "Missions en cours / signées ?", "CA encaissé vs objectif ?"] },
    { dim: "Contenu LinkedIn", questions: ["Posts publiés (objectif 2–3/sem) ?", "DM entrants qualifiés ?", "Post le plus engagé du mois → pourquoi ?"] },
    { dim: "Produit & Affiliation", questions: ["Ventes produit ce mois ?", "Commissions affiliation ?", "Idée de contenu produit à tester ?"] },
  ];

  for (const dim of pilotage) {
    const children = [];
    dim.questions.forEach((q) => children.push(todo(q)));
    blocks.push(tog(`${dim.dim}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── DIFFÉRENCIATION FINALE ──
  blocks.push(h1("🧠 Différenciation Finale — Ce que tu incarnes"));
  blocks.push(p(""));

  blocks.push(h2("Tu ne seras plus :"));
  blocks.push(bul([rt("✗  Expert WordPress", { bold: true, color: "red" })], "red_background"));
  blocks.push(bul([rt("✗  Freelance LMS", { bold: true, color: "red" })], "red_background"));
  blocks.push(bul([rt("✗  Consultant digital généraliste", { bold: true, color: "red" })], "red_background"));
  blocks.push(p(""));

  blocks.push(h2("Tu seras :"));
  blocks.push(cal([rt(VISION.position_cible, { bold: true })], "green_background"));
  blocks.push(p(""));

  const preuves = [
    "Le seul à parler architecture B2B WordPress en français (pas plugin)",
    "Le seul à connecter LMS + CRM + automatisation dans une offre cohérente",
    "Le seul à publier des études de cas avec KPIs mesurés sur ce segment",
    "Le seul à être cité par les AI Overviews sur 'LMS WordPress entreprise'",
    "Le seul dont le pricing reflète la valeur business créée (pas les heures)",
  ];

  preuves.forEach((pr) => blocks.push(bul([rt("✓  " + pr, { bold: true, color: "green" })], "green_background")));
  blocks.push(div());

  // ── CHECKLIST DÉMARRAGE ──
  blocks.push(h1("✅ Checklist — Les 5 Premiers Jours"));
  blocks.push(p([rt("Avant tout contenu. Avant tout post. La fondation.", { italic: true, bold: true })]));
  blocks.push(p(""));

  const checklist_j5 = [
    "Jour 1 : Mettre à jour la bio LinkedIn + tagline + lien bio /audit-b2b",
    "Jour 1 : Rédiger et publier la section À propos LinkedIn (texte complet)",
    "Jour 2 : Créer la page /audit-b2b sur schoolswp.com (formulaire qualifiant actif)",
    "Jour 2 : Finaliser et sauver le template devis Audit (Niveau 1 · PDF SASU)",
    "Jour 3 : Brief du pilier LMS B2B rédigé (structure + angle + mots-clés validés)",
    "Jour 3 : Créer le pipeline CRM LinkedIn dans Notion (DM → Qualifié → Appel → Audit → Mission)",
    "Jour 4 : 1er post LinkedIn B2B publié (hook fort · pilier Architecture · CTA audit)",
    "Jour 4 : Soumettre le sitemap dans Google Search Console",
    "Jour 5 : Créer le projet Thruuu avec 10 prompts de monitoring B2B",
    "Jour 5 : Dashboard KPI mensuel Notion créé et prêt (30 min/mois)",
  ];

  checklist_j5.forEach((item) => blocks.push(todo(item)));
  blocks.push(div());

  // ── CA SYNTHÈSE ──
  blocks.push(h1("💰 Synthèse CA — 24 Mois"));
  blocks.push(p(""));

  [
    { label: "Phase 1 (M1–M6)", mini: ca_phase1.mini, cible: ca_phase1.cible },
    { label: "Phase 2 (M7–M12)", mini: ca_phase2.mini, cible: ca_phase2.cible },
    { label: "Phase 3 (M13–M24)", mini: ca_phase3.mini, cible: ca_phase3.cible },
  ].forEach((ph) => {
    blocks.push(bul([
      rt(`${ph.label} : `, { bold: true }),
      rt(`${ph.mini.toLocaleString("fr-FR")} €`, { color: "blue" }),
      rt(" – "),
      rt(`${ph.cible.toLocaleString("fr-FR")} €`, { bold: true, color: "green" }),
    ]));
  });

  blocks.push(p(""));
  blocks.push(qot(
    [
      rt("CA TOTAL 24 MOIS : ", { bold: true }),
      rt(`${ca_total.mini.toLocaleString("fr-FR")} € `, { bold: true, color: "blue" }),
      rt("(conservateur) – "),
      rt(`${ca_total.cible.toLocaleString("fr-FR")} €`, { bold: true, color: "green" }),
      rt(" (cible)"),
    ],
    "green_background"
  ));
  blocks.push(p(""));
  blocks.push(p([
    rt(`→ Soit ${Math.round(ca_total.mini / 24).toLocaleString("fr-FR")} – ${Math.round(ca_total.cible / 24).toLocaleString("fr-FR")} €/mois en moyenne sur 24 mois`, { italic: true, color: "gray" }),
  ]));
  blocks.push(div());

  // ── VISION FINALE ──
  blocks.push(h1("🌟 Dans 24 Mois"));
  blocks.push(p(""));
  blocks.push(cal(
    "Un formateur B2B francophone tape 'architecture LMS WordPress entreprise' sur Google ou ChatGPT. Il tombe sur schoolsWP. Il lit l'article. Il remplit le formulaire d'audit. C'est exactement ce que cette roadmap construit.",
    "purple_background"
  ));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la Roadmap 24 Mois Domination B2B...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🗺" },
    properties: {
      title: { title: [{ text: { content: "🗺 Roadmap 24 Mois — Domination Formateurs B2B WordPress" } }] },
    },
    children: firstChunk,
  });

  const pageId = page.id;
  console.log(`✅  Page créée : ${pageId}`);

  let i = 0;
  while (i < rest.length) {
    const batch = rest.slice(i, i + CHUNK);
    await sleep(600);
    await notionRequest("PATCH", `/blocks/${pageId}/children`, { children: batch });
    i += CHUNK;
    console.log(`   ↳ Batch ${Math.ceil(i / CHUNK) + 1} envoyé (${Math.min(i, rest.length)}/${rest.length} blocs)`);
  }

  console.log("");
  console.log("✅  Page complète créée avec succès !");
  console.log(`🔗  https://notion.so/${pageId.replace(/-/g, "")}`);
  console.log("");
  console.log("📊  Synthèse financière 24 mois :");
  console.log(`   Phase 1 (M1–M6)   : ${ca_phase1.mini.toLocaleString("fr-FR")} – ${ca_phase1.cible.toLocaleString("fr-FR")} €`);
  console.log(`   Phase 2 (M7–M12)  : ${ca_phase2.mini.toLocaleString("fr-FR")} – ${ca_phase2.cible.toLocaleString("fr-FR")} €`);
  console.log(`   Phase 3 (M13–M24) : ${ca_phase3.mini.toLocaleString("fr-FR")} – ${ca_phase3.cible.toLocaleString("fr-FR")} €`);
  console.log(`   ────────────────────────────────────────────`);
  console.log(`   TOTAL 24 mois     : ${ca_total.mini.toLocaleString("fr-FR")} – ${ca_total.cible.toLocaleString("fr-FR")} €`);
  console.log(`   Mensuel moyen     : ${Math.round(ca_total.mini / 24).toLocaleString("fr-FR")} – ${Math.round(ca_total.cible / 24).toLocaleString("fr-FR")} €/mois`);
  console.log("");
  console.log(`📝  Articles planifiés : ${total_articles} (3 clusters)`);
  console.log(`🎯  Checklist J5 : 10 actions prioritaires`);
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
