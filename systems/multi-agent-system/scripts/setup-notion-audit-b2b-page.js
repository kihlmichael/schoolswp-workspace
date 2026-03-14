#!/usr/bin/env node
"use strict";

/**
 * setup-notion-audit-b2b-page.js
 * Crée la page Notion : 🔍 Audit Architecture B2B — Stratégie & Copie Complète
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-audit-b2b-page.js
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

const META = {
  slug: "/audit-b2b",
  titre_seo: "Diagnostic WordPress B2B — Audit Architecture LMS & CRM | schoolsWP",
  description_seo: "Audit stratégique de votre architecture WordPress pour formateurs B2B. LMS multi-entreprises, CRM, automatisation, tunnel B2B. Réservé aux acteurs avec chiffre établi.",
  og_image: "Titre fort sur fond sombre · schoolsWP · Diagnostic WordPress B2B",
  url_cible: "https://schoolswp.com/audit-b2b",
  positionnement: "Machine de qualification haut niveau — pas un formulaire de contact générique.",
  message_cle: "Vous ne manquez pas d'outils. Vous manquez d'architecture.",
};

const HERO = {
  titre: "Votre système WordPress est-il vraiment prêt pour vendre aux entreprises ?",
  sous_titre: "Audit stratégique pour formateurs B2B utilisant WordPress\n(LMS, CRM, automatisation, tunnel, reporting)",
  cta_primaire: "Demander un diagnostic stratégique",
  cta_anchor: "#formulaire-audit",
  note_sous_cta: "Diagnostic réservé aux formateurs B2B avec chiffre établi. Sélection stricte.",
  elements_credibilite: [
    "Spécialiste LMS + CRM WordPress B2B",
    "Audit livré sous 10 jours ouvrés",
    "Rapport structuré 20–30 pages",
    "Pas de vente agressive — diagnostic d'abord",
  ],
};

const PROBLEMES = {
  intro: "Chaque semaine, je rencontre des formateurs B2B qui ont le même profil.",
  liste: [
    {
      probleme: "Gestion multi-entreprises complexe",
      detail: "Un seul espace LMS pour tout le monde. Impossible de séparer les cohortes, gérer les accès par client ou fournir un reporting individuel par entreprise.",
      cout_invisible: "Vous passez 3 à 5h/semaine à gérer manuellement ce qu'un système bien structuré ferait seul.",
    },
    {
      probleme: "Reporting inexistant ou artisanal",
      detail: "Vos clients DRH vous demandent des rapports de progression. Vous les générez à la main dans un Excel. À chaque session. Pour chaque entreprise.",
      cout_invisible: "2 à 4h par session de formation. Ce temps n'est pas facturé. Ce n'est pas de la valeur ajoutée.",
    },
    {
      probleme: "CRM mal segmenté ou absent",
      detail: "Vous avez peut-être HubSpot ou Notion. Mais aucune segmentation tripartite : décideur, apprenant, RH. Résultat : vous envoyez le même email à tout le monde.",
      cout_invisible: "Taux de renouvellement en dessous du marché. Des décideurs qui ne comprennent pas la valeur de votre offre.",
    },
    {
      probleme: "Onboarding manuel à chaque client",
      detail: "Un nouveau client entreprise ? Vous créez les accès à la main, envoyez les identifiants par email, relancez pour confirmer la connexion.",
      cout_invisible: "45 min à 2h par nouveau client. × 10 clients = 1 journée de travail non facturée tous les mois.",
    },
    {
      probleme: "Tunnel mal structuré pour le B2B",
      detail: "Votre page de vente est pensée pour des particuliers. Le formulaire ne filtre pas. Vous recevez des demandes de devis à 300 € et des appels non qualifiés.",
      cout_invisible: "3 à 5 appels perdus par mois avec des prospects hors cible. Du temps et de l'énergie dépensés sans ROI.",
    },
    {
      probleme: "Facturation et cycle de vente confus",
      detail: "Devis envoyés par email, suivis dans une feuille Google. Relances manuelles. Aucune visibilité sur le pipeline à 60 ou 90 jours.",
      cout_invisible: "Des contrats qui traînent. Des renouvellements oubliés. Un taux de closing qui stagne à 20-30% alors qu'il pourrait dépasser 50%.",
    },
  ],
  conclusion: "Le problème n'est pas le plugin. C'est l'architecture globale.",
  reponse: "Un LMS mal configuré, un CRM absent et un tunnel B2C ne deviendront jamais un système B2B performant en changeant d'outil. Ils le deviendront avec une architecture pensée de A à Z.",
};

const PILIERS_AUDIT = [
  {
    num: "01",
    emoji: "🎓",
    titre: "Architecture LMS B2B",
    description: "Scalabilité multi-entreprises, gestion des comptes, cohortes, accès groupés, sécurité des espaces.",
    questions_clés: [
      "Votre LMS peut-il gérer 20 entreprises clientes distinctes sans intervention manuelle ?",
      "Les apprenants d'une entreprise peuvent-ils voir les contenus d'une autre ?",
      "Comment un DRH accède-t-il au suivi de ses collaborateurs ?",
    ],
    livrable: "Score de maturité LMS B2B + recommandations prioritaires",
  },
  {
    num: "02",
    emoji: "🧠",
    titre: "Structure CRM & Segmentation",
    description: "Segmentation décideur / apprenant / RH, pipeline commercial, automatisations actives vs manquantes.",
    questions_clés: [
      "Avez-vous des pipelines distincts pour la vente initiale et le renouvellement ?",
      "Comment distinguez-vous le DRH qui signe, le RH qui gère et l'apprenant qui suit ?",
      "Combien de relances manuelles faites-vous par mois en B2B ?",
    ],
    livrable: "Cartographie CRM actuel + architecture cible + séquences manquantes",
  },
  {
    num: "03",
    emoji: "💼",
    titre: "Tunnel B2B & Qualification",
    description: "Page offre corporate, formulaire qualifiant, scoring prospect, automatisation pré-vente.",
    questions_clés: [
      "Votre formulaire de contact filtre-t-il les particuliers des entreprises ?",
      "Recevez-vous des demandes non qualifiées (budget trop faible, mauvais profil) ?",
      "Avez-vous une page dédiée aux entreprises ou renvoyez-vous vers votre page générale ?",
    ],
    livrable: "Audit tunnel + score de qualification + wireframe page offre B2B recommandée",
  },
  {
    num: "04",
    emoji: "⚙️",
    titre: "Automatisation Onboarding Entreprise",
    description: "De la signature à l'accès LMS. Séquences email B2B. Relances renouvellement J-90/60/30.",
    questions_clés: [
      "Combien de temps entre la signature d'un contrat et le premier accès LMS de l'apprenant ?",
      "Avez-vous une séquence d'activation automatique pour les nouveaux groupes ?",
      "Votre système relance-t-il automatiquement les renouvellements en fin de contrat ?",
    ],
    livrable: "Cartographie des flux automatisés + gaps + séquences à implémenter",
  },
  {
    num: "05",
    emoji: "📊",
    titre: "Performance & Scalabilité",
    description: "Core Web Vitals, sécurité, tracking KPI B2B, structure SEO, capacité de montée en charge.",
    questions_clés: [
      "Votre LMS tient-il si 50 apprenants se connectent simultanément ?",
      "Avez-vous un tableau de bord KPI pour piloter votre activité B2B ?",
      "Votre architecture est-elle documentée pour qu'un nouveau prestataire puisse la reprendre ?",
    ],
    livrable: "Score technique + recommandations performance + plan scalabilité",
  },
];

const CIBLES = {
  oui: [
    { profil: "Formateur vendant aux entreprises", detail: "Vous facturez déjà des entreprises, associations, organismes professionnels." },
    { profil: "Organisme de formation indépendant", detail: "OF certifié QUALIOPI ou en cours de certification. Formations inter ou intra-entreprises." },
    { profil: "Expert souhaitant structurer son offre B2B", detail: "Vous avez une expertise forte. Vous voulez la vendre aux entreprises de manière systématique." },
    { profil: "Acteur avec chiffre d'affaires établi", detail: "Votre offre fonctionne. Vous voulez scaler sans complexité administrative supplémentaire." },
  ],
  non: [
    { profil: "Débutant total en formation", detail: "Cet audit suppose un minimum d'activité B2B existante. Pas encore de clients entreprises ? Ce n'est pas pour vous." },
    { profil: "Chercheur d'un site vitrine simple", detail: "Si votre besoin est un site WordPress 'propre', je ne suis pas votre prestataire." },
    { profil: "Budget inférieur à 3 000 €", detail: "La structuration B2B nécessite un investissement minimum. En dessous, le ROI n'est pas au rendez-vous." },
    { profil: "Recherche d'un développeur à l'heure", detail: "Je ne facture pas au temps. Si vous avez besoin d'un dev WordPress classique, orientez-vous ailleurs." },
  ],
};

const FORMAT_AUDIT = [
  {
    etape: "01",
    emoji: "📋",
    label: "Questionnaire stratégique",
    duree: "10 à 15 min",
    description: "Formulaire de qualification complet. Vous répondez à votre rythme. Je lis chaque réponse avant de répondre.",
    note: "Pas de question générique. Chaque question a un rôle précis dans l'analyse.",
  },
  {
    etape: "02",
    emoji: "🔎",
    label: "Analyse de votre architecture",
    duree: "5 à 7 jours ouvrés",
    description: "J'analyse votre site, votre LMS, votre CRM (accès partagé ou captures d'écran). Je cartographie l'existant et j'identifie les frictions.",
    note: "Cette phase est silencieuse. Je travaille. Je ne vous bombarde pas de questions.",
  },
  {
    etape: "03",
    emoji: "📞",
    label: "Appel de restitution 45 min",
    duree: "45 minutes",
    description: "Je vous présente les résultats. On en discute. Vous posez vos questions. Pas de vente agressive — on parle architecture.",
    note: "C'est souvent l'appel où le client réalise l'ampleur réelle du problème. En bien.",
  },
  {
    etape: "04",
    emoji: "📄",
    label: "Plan d'action structuré",
    duree: "Livré sous 3 jours post-appel",
    description: "Document PDF 20–30 pages. Diagnostic complet. Recommandations priorisées par impact. Roadmap 90 jours.",
    note: "Ce document est actionnable seul. Vous n'êtes pas obligé de travailler avec moi ensuite.",
  },
];

const RESULTATS = [
  {
    resultat: "Cartographie claire de votre système",
    detail: "Une vue d'ensemble visuelle et commentée de votre écosystème WordPress actuel — ce qui fonctionne, ce qui freine, ce qui manque.",
  },
  {
    resultat: "Identification précise des frictions business",
    detail: "Chaque point de friction est documenté avec son impact estimé sur le CA, le temps administratif et la crédibilité auprès des entreprises.",
  },
  {
    resultat: "Recommandations priorisées par impact",
    detail: "Pas une liste de 40 actions. 5 à 8 recommandations classées par impact / effort. Ce qui doit être fait en J1–J30, J31–J60, J61–J90.",
  },
  {
    resultat: "Vision d'optimisation long terme",
    detail: "Ce à quoi ressemblera votre système dans 12 mois si vous implémentez les recommandations. Avec des KPIs cibles.",
  },
  {
    resultat: "Clarté totale sur les prochaines étapes",
    detail: "Après l'audit, vous savez exactement quoi faire — seul, avec votre équipe, ou en mission avec moi.",
  },
];

const FORMULAIRE = {
  intro: "Remplissez ce questionnaire avec soin. Chaque réponse m'aide à préparer un diagnostic utile — pas générique.",
  champs: [
    {
      label: "Votre prénom et nom",
      type: "text",
      required: true,
      placeholder: "Jean Dupont",
      role_interne: "Identification basique.",
    },
    {
      label: "Votre email professionnel",
      type: "email",
      required: true,
      placeholder: "jean@monorganisme.fr",
      role_interne: "Contact + ajout au CRM FluentCRM (tag : Audit-B2B).",
    },
    {
      label: "Votre site WordPress (URL)",
      type: "url",
      required: true,
      placeholder: "https://monsite.com",
      role_interne: "Analyse technique préalable avant l'appel.",
    },
    {
      label: "CA annuel estimé de votre activité formation",
      type: "select",
      required: true,
      options: [
        "< 30 000 €/an",
        "30 000 – 60 000 €/an",
        "60 000 – 100 000 €/an",
        "100 000 – 200 000 €/an",
        "> 200 000 €/an",
        "Préfère ne pas répondre",
      ],
      role_interne: "ÉLIMINATOIRE si < 30k. En dessous, ROI non justifiable.",
    },
    {
      label: "Nombre d'entreprises clientes actuelles",
      type: "select",
      required: true,
      options: [
        "0 (je vise ce marché)",
        "1 à 3",
        "4 à 10",
        "11 à 20",
        "Plus de 20",
      ],
      role_interne: "ÉLIMINATOIRE si 0. Audit sur l'existant, pas sur le projet.",
    },
    {
      label: "LMS WordPress utilisé",
      type: "select",
      required: true,
      options: [
        "Tutor LMS",
        "LearnDash",
        "LifterLMS",
        "FluentCommunity / BuddyBoss",
        "Autre (préciser en commentaire)",
        "Pas encore de LMS WordPress",
      ],
      role_interne: "Détermine l'angle technique de l'audit.",
    },
    {
      label: "CRM ou outil de gestion client utilisé",
      type: "select",
      required: true,
      options: [
        "FluentCRM (WordPress natif)",
        "HubSpot",
        "Pipedrive",
        "Notion ou Airtable",
        "Feuille Excel / Google Sheets",
        "Aucun CRM structuré",
        "Autre",
      ],
      role_interne: "Diagnostique l'état CRM. 'Aucun' = gap majeur identifié.",
    },
    {
      label: "Quel est votre problème principal en ce moment ?",
      type: "textarea",
      required: true,
      placeholder: "Décrivez en 2–3 phrases ce qui vous bloque ou vous frustre dans votre système actuel.",
      role_interne: "Signal qualitatif fort. Révèle l'urgence réelle.",
    },
    {
      label: "Budget envisagé pour structurer votre système",
      type: "select",
      required: true,
      options: [
        "< 2 000 €",
        "2 000 – 4 000 €",
        "4 000 – 8 000 €",
        "8 000 – 15 000 €",
        "> 15 000 €",
      ],
      role_interne: "ÉLIMINATOIRE si < 2 000 €. Qualifier le budget avant tout.",
    },
    {
      label: "Quel est votre objectif à 12 mois ?",
      type: "textarea",
      required: true,
      placeholder: "Ex : passer de 8 à 20 clients entreprises, automatiser mon onboarding, structurer mon offre QUALIOPI…",
      role_interne: "Permet d'aligner l'audit sur les vrais objectifs business.",
    },
    {
      label: "Comment avez-vous entendu parler de schoolsWP ?",
      type: "select",
      required: false,
      options: [
        "Recherche Google",
        "LinkedIn",
        "Recommandation",
        "Article de blog",
        "Autre",
      ],
      role_interne: "Attribution marketing. Renseigner source dans FluentCRM.",
    },
  ],
  message_post_soumission: "Merci. J'ai bien reçu votre questionnaire. Je le lis attentivement et reviens vers vous sous 48h ouvrées pour confirmer si l'audit est adapté à votre situation.",
  email_accusé_reception: {
    sujet: "Votre demande d'audit reçue — prochaine étape",
    corps: `Bonjour [Prénom],

J'ai bien reçu votre questionnaire. Merci pour les détails — ça m'aide à préparer quelque chose d'utile, pas de générique.

Je le lis dans les 24 à 48h et reviens vers vous pour confirmer si l'audit est adapté à votre situation — et si oui, pour planifier la prochaine étape.

Si votre profil correspond à ce que je recherche, vous recevrez un email avec les modalités et le lien de paiement (option payante) ou une confirmation directe (option gratuite).

À très vite,
[Prénom] · schoolsWP Agency`,
  },
};

const OPTIONS_PRICING = [
  {
    option: "A",
    nom: "Diagnostic gratuit ultra-qualifié",
    prix: "Gratuit",
    selection: "Stricte — 3 à 4 diagnostics par mois maximum",
    avantages: [
      "Supprime la barrière financière d'entrée",
      "Attire plus de demandes → plus de choix pour sélectionner",
      "Lead magnet puissant si bien positionné ('gratuit' ≠ 'sans valeur')",
      "Crédibilité maximale — le client voit la qualité avant d'acheter",
    ],
    inconvenients: [
      "Attire des prospects non qualifiés malgré le formulaire",
      "Risque de clients qui veulent le diagnostic sans passer à l'implémentation",
      "Demande plus de temps de sélection manuelle",
    ],
    recommande_si: "Tu veux construire rapidement un portefeuille d'études de cas (An1). Tu peux te permettre 4 diagnostics/mois.",
    process: "Formulaire → Sélection manuelle (Go/No-Go sous 48h) → Confirmation → Audit → Restitution",
  },
  {
    option: "B",
    nom: "Diagnostic payant remboursé si mission",
    prix: "297 – 497 €",
    prix_mini: 297,
    prix_maxi: 497,
    selection: "Financière — le prix filtre naturellement",
    avantages: [
      "Filtre naturel : seuls les prospects sérieux paient",
      "Génère un CA direct (3 à 5 audits/mois = 900 – 2 500 €)",
      "Augmente la valeur perçue de l'audit",
      "Si mission signée → déduit du devis → moteur d'upsell naturel",
    ],
    inconvenients: [
      "Réduit le volume de demandes",
      "Peut rebuter des prospects sérieux mais hésitants sur le processus",
      "Nécessite un argumentaire clair sur 'pourquoi c'est payant'",
    ],
    recommande_si: "Tu veux un filtre financier fort dès le départ. Tu as déjà 1–2 études de cas. Tu veux un CA audit régulier.",
    process: "Formulaire → Évaluation → Lien paiement sous 24h → Paiement → Démarrage audit → Restitution → Déduit si mission",
    mention_remboursement: "Le montant de l'audit est intégralement déduit du devis si vous décidez de travailler ensemble.",
  },
];

const COPIE_PAGE = {
  section2_titre: "Ce que j'observe chaque semaine",
  section3_titre: "Ce que l'audit analyse",
  section3_intro: "5 piliers. Chacun révèle une partie du problème. Ensemble, ils donnent une vision complète.",
  section4_titre: "Pour qui est cet audit ?",
  section5_titre: "Comment ça se passe",
  section5_intro: "Pas de vente agressive. Diagnostic d'abord. Action ensuite.",
  section6_titre: "Ce que vous obtenez",
  section6_intro: "Un document actionnable. Pas un rapport générique de 5 pages qui finit dans un tiroir.",
  section7_titre: "Demander votre diagnostic",
  section7_intro: "15 minutes de votre temps. Un diagnostic structuré en retour. Réservé aux formateurs B2B sérieux.",
  ton: "Calme. Premium. Structuré. Pas de hype. Pas de 'vous allez transformer votre business'. Juste des faits.",
  mots_interdits: ["révolutionnaire", "incroyable", "game-changer", "hack", "magique", "en un clic", "sans effort"],
};

const KPIS_PAGE = [
  { kpi: "Taux de complétion formulaire", objectif: "> 60% (ceux qui arrivent sur la page remplissent le formulaire)", alerte: "< 40% → revoir le message ou le formulaire" },
  { kpi: "Taux de qualification Go/No-Go", objectif: "40–60% Go (les autres sont filtrés)", alerte: "< 20% Go → formulaire pas assez qualifiant" },
  { kpi: "Taux de conversion audit → mission", objectif: "> 50% (ceux qui font l'audit passent à l'implémentation)", alerte: "< 30% → revoir la restitution ou l'offre Phase 2" },
  { kpi: "CA audit mensuel (option B)", objectif: "900 – 2 500 €/mois (3 à 5 audits payants)", alerte: "< 2 audits/mois → activer LinkedIn + SEO" },
  { kpi: "Délai formulaire → restitution", objectif: "< 10 jours ouvrés", alerte: "> 14 jours → réviser le process ou limiter les audits par mois" },
  { kpi: "NPS post-audit", objectif: "> 8/10", alerte: "< 7 → améliorer la qualité du rapport ou le call de restitution" },
];

const TECH_STACK_PAGE = [
  { element: "Page WordPress", detail: "Divi ou Elementor avec template premium sobre. Pas de template formation générique." },
  { element: "Formulaire", detail: "FluentForms ou Gravity Forms. Conditions logiques sur chaque champ." },
  { element: "Automatisation post-formulaire", detail: "FluentCRM : tag 'Audit-B2B', séquence accusé-réception, tâche CRM assignée." },
  { element: "Paiement (option B)", detail: "WooCommerce simple ou Stripe natif. 1 produit 'Audit B2B' à prix fixe." },
  { element: "Calendrier restitution", detail: "Calendly intégré ou WP-Apointly. Créneau disponible uniquement après paiement (option B)." },
  { element: "Tracking", detail: "GA4 + événement 'audit_form_submit' + événement 'audit_payment_complete' (option B)." },
];

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

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

// ─── BLOCK BUILDERS ──────────────────────────────────────────────────────────

const rt = (text, opts = {}) => ({
  type: "text", text: { content: String(text) },
  annotations: { bold: opts.bold || false, italic: opts.italic || false, code: opts.code || false, color: opts.color || "default" },
});
const h1 = (t) => ({ object: "block", type: "heading_1", heading_1: { rich_text: [rt(t)] } });
const h2 = (t) => ({ object: "block", type: "heading_2", heading_2: { rich_text: [rt(t)] } });
const h3 = (t) => ({ object: "block", type: "heading_3", heading_3: { rich_text: [rt(t)] } });
const p = (rts) => ({ object: "block", type: "paragraph", paragraph: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const bul = (rts, color = "default") => ({ object: "block", type: "bulleted_list_item", bulleted_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)], color } });
const num = (rts) => ({ object: "block", type: "numbered_list_item", numbered_list_item: { rich_text: Array.isArray(rts) ? rts : [rt(rts)] } });
const div = () => ({ object: "block", type: "divider", divider: {} });
const qot = (text, color = "gray_background") => ({ object: "block", type: "quote", quote: { rich_text: Array.isArray(text) ? text : [rt(text)], color } });
const cal = (text, color = "blue_background") => ({
  object: "block", type: "callout",
  callout: { rich_text: Array.isArray(text) ? text : [rt(text)], icon: { type: "emoji", emoji: "💡" }, color },
});
const tog = (text, children = []) => ({
  object: "block", type: "toggle",
  toggle: { rich_text: [rt(text, { bold: true })], children },
});
const todo = (text, checked = false) => ({
  object: "block", type: "to_do",
  to_do: { rich_text: [rt(text)], checked },
});

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("🔍 Audit Architecture B2B · Page schoolswp.com/audit-b2b · Brief complet", "yellow_background"));
  blocks.push(p([rt("Ce document contient : positionnement · copie complète · formulaire · options pricing · stack technique · KPIs.", { italic: true })]));
  blocks.push(div());

  // ── META SEO ──
  blocks.push(h1("🌐 Meta & Positionnement"));
  blocks.push(p(""));
  blocks.push(p([rt("URL cible : ", { bold: true }), rt(META.url_cible, { code: true })]));
  blocks.push(p([rt("Titre SEO : ", { bold: true }), rt(META.titre_seo, { italic: true })]));
  blocks.push(p([rt("Description : ", { bold: true }), rt(META.description_seo, { italic: true })]));
  blocks.push(p(""));
  blocks.push(cal([rt("Positionnement : ", { bold: true }), rt(META.positionnement)], "green_background"));
  blocks.push(p(""));
  blocks.push(qot(META.message_cle, "blue_background"));
  blocks.push(div());

  // ── SECTION 1 — HERO ──
  blocks.push(h1("1️⃣ Hero Section"));
  blocks.push(p(""));
  blocks.push(h2("Titre principal (H1)"));
  blocks.push(cal([rt(HERO.titre, { bold: true })], "purple_background"));
  blocks.push(p(""));
  blocks.push(h2("Sous-titre"));
  blocks.push(qot(HERO.sous_titre, "blue_background"));
  blocks.push(p(""));
  blocks.push(h2("CTA Primaire"));
  blocks.push(bul([rt(`Bouton : "${HERO.cta_primaire}"`, { bold: true, color: "green" })]));
  blocks.push(bul([rt(`Ancre : ${HERO.cta_anchor}`, { code: true })]));
  blocks.push(bul([rt(`Note sous CTA : "${HERO.note_sous_cta}"`, { italic: true, color: "gray" })]));
  blocks.push(p(""));
  blocks.push(h2("Éléments de crédibilité (icônes)"));
  HERO.elements_credibilite.forEach((e) => blocks.push(bul([rt("✓  " + e, { bold: true })])));
  blocks.push(div());

  // ── SECTION 2 — LE VRAI PROBLÈME ──
  blocks.push(h1("2️⃣ Section : Le Vrai Problème"));
  blocks.push(p([rt("Texte d'intro : ", { bold: true }), rt(PROBLEMES.intro, { italic: true })]));
  blocks.push(p(""));

  for (const pb of PROBLEMES.liste) {
    const children = [];
    children.push(p([rt("Détail : ", { bold: true }), rt(pb.detail)]));
    children.push(p(""));
    children.push(p([rt("⏱ Coût invisible : ", { bold: true, color: "red" }), rt(pb.cout_invisible, { italic: true })]));
    blocks.push(tog(`⚠️  ${pb.probleme}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(cal([
    rt(PROBLEMES.conclusion + "\n", { bold: true }),
    rt(PROBLEMES.reponse, { italic: true }),
  ], "red_background"));
  blocks.push(div());

  // ── SECTION 3 — PILIERS AUDIT ──
  blocks.push(h1("3️⃣ Section : Ce que l'Audit Analyse — 5 Piliers"));
  blocks.push(p([rt(COPIE_PAGE.section3_intro, { italic: true })]));
  blocks.push(p(""));

  for (const pilier of PILIERS_AUDIT) {
    const children = [];
    children.push(p([rt(pilier.description)]));
    children.push(p(""));
    children.push(h3("Questions clés que j'analyse"));
    pilier.questions_clés.forEach((q) => children.push(bul([rt("→ " + q, { italic: true })])));
    children.push(p(""));
    children.push(p([rt("📄 Livrable : ", { bold: true }), rt(pilier.livrable, { color: "green" })]));

    blocks.push(tog(`${pilier.emoji} ${pilier.num} — ${pilier.titre}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SECTION 4 — CIBLES ──
  blocks.push(h1("4️⃣ Section : Pour qui est cet Audit ?"));
  blocks.push(p(""));

  blocks.push(h2("✅ Oui, cet audit est fait pour vous si :"));
  for (const c of CIBLES.oui) {
    const children = [p([rt(c.detail, { italic: true })])];
    blocks.push(tog(`✓  ${c.profil}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(h2("🚫 Non, cet audit n'est PAS adapté si :"));
  for (const c of CIBLES.non) {
    const children = [p([rt(c.detail, { italic: true })])];
    blocks.push(tog(`✗  ${c.profil}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(cal("Filtrer clairement = attirer les bons clients. Chaque 'non' sur la page éloigne les mauvais prospects et renforce la crédibilité.", "yellow_background"));
  blocks.push(div());

  // ── SECTION 5 — FORMAT ──
  blocks.push(h1("5️⃣ Section : Comment ça se Passe"));
  blocks.push(p([rt(COPIE_PAGE.section5_intro, { italic: true })]));
  blocks.push(p(""));

  for (const f of FORMAT_AUDIT) {
    const children = [];
    children.push(p([rt("Durée : ", { bold: true }), rt(f.duree)]));
    children.push(p([rt("Description : ", { bold: true }), rt(f.description)]));
    children.push(p(""));
    children.push(qot(f.note, "gray_background"));

    blocks.push(tog(`${f.emoji} Étape ${f.etape} — ${f.label}  (${f.duree})`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SECTION 6 — RÉSULTATS ──
  blocks.push(h1("6️⃣ Section : Ce que vous Obtenez"));
  blocks.push(p([rt(COPIE_PAGE.section6_intro, { italic: true })]));
  blocks.push(p(""));

  for (const r of RESULTATS) {
    const children = [p([rt(r.detail)])];
    blocks.push(tog(`✓ ${r.resultat}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SECTION 7 — FORMULAIRE ──
  blocks.push(h1("7️⃣ Formulaire de Qualification — Spécifications Complètes"));
  blocks.push(p([rt(FORMULAIRE.intro, { italic: true })]));
  blocks.push(p(""));

  for (const champ of FORMULAIRE.champs) {
    const children = [];
    children.push(p([rt("Type : ", { bold: true }), rt(champ.type, { code: true }), rt("  ·  "), rt(champ.required ? "Obligatoire" : "Optionnel", { bold: true, color: champ.required ? "red" : "gray" })]));
    if (champ.placeholder) children.push(p([rt("Placeholder : ", { bold: true }), rt(champ.placeholder, { italic: true })]));
    if (champ.options) {
      children.push(p([rt("Options : ", { bold: true })]));
      champ.options.forEach((o) => children.push(bul(o)));
    }
    children.push(p(""));
    children.push(p([rt("Rôle interne : ", { bold: true, color: "gray" }), rt(champ.role_interne, { italic: true, color: "gray" })]));

    const isEliminatoire = champ.role_interne.includes("ÉLIMINATOIRE");
    blocks.push(tog(
      `${isEliminatoire ? "🔴 FILTRE — " : ""}${champ.label}`,
      children
    ));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(h2("Message post-soumission"));
  blocks.push(qot(FORMULAIRE.message_post_soumission, "green_background"));
  blocks.push(p(""));

  blocks.push(h2("Email automatique d'accusé de réception"));
  const emailChildren = [];
  emailChildren.push(p([rt("Sujet : ", { bold: true }), rt(FORMULAIRE.email_accusé_reception.sujet, { code: true })]));
  emailChildren.push(p(""));
  FORMULAIRE.email_accusé_reception.corps.split("\n").forEach((ligne) => {
    emailChildren.push(ligne === "" ? p("") : p(ligne));
  });
  blocks.push(tog("✉️ Voir l'email complet", emailChildren));
  blocks.push(div());

  // ── OPTIONS PRICING ──
  blocks.push(h1("💰 Options Pricing — Gratuit vs Payant"));
  blocks.push(p([rt("Deux stratégies valides. Le choix dépend de votre stade et de votre objectif.", { italic: true })]));
  blocks.push(p(""));

  for (const opt of OPTIONS_PRICING) {
    const children = [];
    children.push(p([rt("Prix : ", { bold: true }), rt(opt.prix, { bold: true, color: "green" })]));
    children.push(p([rt("Sélection : ", { bold: true }), rt(opt.selection)]));
    if (opt.mention_remboursement) {
      children.push(p(""));
      children.push(cal([rt("💡 Mention clé sur la page : ", { bold: true }), rt(`"${opt.mention_remboursement}"`)], "blue_background"));
    }
    children.push(p(""));
    children.push(h3("✅ Avantages"));
    opt.avantages.forEach((a) => children.push(bul([rt("✓  " + a, { color: "green" })], "green_background")));
    children.push(p(""));
    children.push(h3("⚠️ Inconvénients"));
    opt.inconvenients.forEach((i) => children.push(bul([rt("⚠  " + i)], "yellow_background")));
    children.push(p(""));
    children.push(p([rt("Recommandé si : ", { bold: true }), rt(opt.recommande_si, { italic: true })]));
    children.push(p([rt("Process : ", { bold: true }), rt(opt.process, { italic: true })]));

    blocks.push(tog(`Option ${opt.option} — ${opt.nom}  ·  ${opt.prix}`, children));
    blocks.push(p(""));
  }

  blocks.push(p(""));
  blocks.push(cal(
    "Recommandation schoolsWP : commencer par l'Option A (gratuit sélectif) en An1 pour construire les études de cas. Passer à l'Option B (payant) dès An2 avec les preuves en main.",
    "green_background"
  ));
  blocks.push(div());

  // ── STACK TECHNIQUE ──
  blocks.push(h1("⚙️ Stack Technique Recommandé"));
  blocks.push(p(""));
  for (const s of TECH_STACK_PAGE) {
    blocks.push(bul([rt(`${s.element} : `, { bold: true }), rt(s.detail)]));
  }
  blocks.push(div());

  // ── KPIs ──
  blocks.push(h1("📊 KPIs à Suivre"));
  blocks.push(p([rt("Ces métriques pilotent l'efficacité de la page. À mesurer mensuellement.", { italic: true })]));
  blocks.push(p(""));
  for (const k of KPIS_PAGE) {
    const children = [];
    children.push(p([rt("Objectif : ", { bold: true }), rt(k.objectif, { color: "green" })]));
    children.push(p([rt("Alerte si : ", { bold: true, color: "red" }), rt(k.alerte, { color: "red" })]));
    blocks.push(tog(k.kpi, children));
    blocks.push(p(""));
  }
  blocks.push(div());

  // ── TON & RÈGLES COPIE ──
  blocks.push(h1("✍️ Ton & Règles Copie"));
  blocks.push(p(""));
  blocks.push(p([rt("Ton : ", { bold: true }), rt(COPIE_PAGE.ton)]));
  blocks.push(p(""));
  blocks.push(h2("Mots interdits sur cette page"));
  COPIE_PAGE.mots_interdits.forEach((m) => blocks.push(bul([rt(`✗  "${m}"`, { color: "red" })], "red_background")));
  blocks.push(div());

  // ── CHECKLIST MISE EN LIGNE ──
  blocks.push(h1("✅ Checklist — Avant Mise en Ligne"));
  blocks.push(p(""));

  const checklist = [
    "URL /audit-b2b créée et slug WordPress configuré",
    "Titre H1 identique au Meta Title (cohérence SEO)",
    "FluentForms configuré avec toutes les conditions logiques des champs éliminatoires",
    "FluentCRM : tag 'Audit-B2B' ajouté automatiquement + tâche assignée",
    "Email accusé de réception configuré et testé (délai : immédiat post-soumission)",
    "Option B : WooCommerce produit 'Audit B2B' créé · Stripe configuré",
    "Option B : Calendly visible uniquement après paiement confirmé",
    "GA4 : événements 'audit_form_submit' et 'audit_cta_click' configurés",
    "Test complet du tunnel : soumission → email → paiement → confirmation",
    "Mobile : formulaire testé sur iOS et Android (champs select natifs)",
    "Page relue : zéro mot interdit · ton calme et premium vérifié",
    "Lien /audit-b2b ajouté en bio LinkedIn et dans la navigation WordPress",
  ];

  checklist.forEach((item) => blocks.push(todo(item)));
  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🌟 Ce que cette Page Construit"));
  blocks.push(p(""));
  blocks.push(cal(
    "Cette page ne vend pas un service. Elle filtre, qualifie et positionne. Chaque visite renforce l'image d'expert. Chaque formulaire soumis est un lead qualifié. Chaque audit livré est une étude de cas en devenir.",
    "purple_background"
  ));
  blocks.push(p(""));
  blocks.push(qot(
    "L'audit n'est pas l'entrée de gamme. C'est la porte d'entrée d'un système premium. La qualité du diagnostic définit la qualité du client qui signe la mission.",
    "green_background"
  ));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la page Audit B2B Stratégique...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🔍" },
    properties: {
      title: { title: [{ text: { content: "🔍 Audit Architecture B2B — Brief & Copie Complète" } }] },
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
  console.log("📋  Sections créées :");
  console.log("   · Meta & SEO (titre, description, URL)");
  console.log("   · Hero (titre H1 · sous-titre · CTA · crédibilité)");
  console.log("   · 6 problèmes B2B avec coût invisible chiffré");
  console.log("   · 5 piliers d'audit avec questions clés et livrables");
  console.log("   · Matrice cibles Oui/Non (4+4 profils)");
  console.log("   · Process 4 étapes chronométrées");
  console.log("   · 5 résultats concrets");
  console.log("   · Formulaire 11 champs (3 éliminatoires + email auto)");
  console.log("   · Options pricing A vs B (gratuit vs payant)");
  console.log("   · Stack technique recommandé");
  console.log("   · 6 KPIs avec objectifs et seuils d'alerte");
  console.log("   · Checklist 12 points avant mise en ligne");
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
