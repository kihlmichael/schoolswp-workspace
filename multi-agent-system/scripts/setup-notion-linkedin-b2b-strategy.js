#!/usr/bin/env node
"use strict";

/**
 * setup-notion-linkedin-b2b-strategy.js
 * Crée la page Notion : 🔗 Stratégie LinkedIn B2B — Machine à Crédibilité
 * Usage : NOTION_API_KEY=ntn_xxx NOTION_PARENT_PAGE_ID=yyy node setup-notion-linkedin-b2b-strategy.js
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

const PROFIL = {
  bio_a_ne_pas_dire: [
    "Expert WordPress | Développeur freelance",
    "Passionné de WordPress et de technologie",
    "Je crée des sites WordPress pour les entrepreneurs",
    "Consultant WordPress | LMS | Formation en ligne",
  ],
  bio_cible: "J'aide les formateurs B2B à structurer un système WordPress rentable — LMS multi-entreprises, CRM automatisé, tunnel corporate.",
  tagline_court: "Architecte WordPress B2B · schoolsWP",
  section_a_propos: [
    "Tu es formateur ou organisme de formation. Tu travailles avec des entreprises.",
    "Ton problème n'est pas le contenu. C'est le système qui le délivre.",
    "",
    "LMS mal structuré → onboarding chaotique → clients insatisfaits → renouvellements perdus.",
    "CRM absent → pipeline flou → cycle de vente à 3 mois non maîtrisé.",
    "Tunnel B2C → prospects entreprise non qualifiés → perte de temps.",
    "",
    "Je structure l'architecture WordPress qui transforme ton offre formation en système B2B rentable :",
    "→ LMS multi-entreprises (comptes séparés, cohortes, accès groupés)",
    "→ CRM automatisé (onboarding, relances, renouvellement J-90)",
    "→ Tunnel corporate (filtrage, devis, qualification automatique)",
    "",
    "Résultat : tu onboardes plus vite, tu renouvelles plus souvent, tu signes plus haut.",
    "",
    "📌 schoolsWP.com — la référence WordPress pour formateurs B2B",
    "📧 Audit Architecture B2B : lien en bio",
  ],
  lien_bio: "https://schoolswp.com/audit-b2b",
  banner_message: "Architecture WordPress B2B · LMS + CRM + Automatisation · schoolsWP",
};

const PILIERS = [
  {
    num: "1",
    emoji: "🟢",
    nom: "Architecture Système B2B",
    objectif: "Te positionner comme architecte stratégique. Pas un technicien — un expert qui pense business avant plugin.",
    frequence: "1 post / semaine",
    sujets: [
      "Pourquoi 80% des LMS WordPress B2B sont mal structurés (et comment le corriger)",
      "Le vrai problème des formateurs entreprise : ce n'est pas le contenu",
      "CRM mal segmenté = contrats perdus silencieusement",
      "La différence entre un LMS pour particuliers et un LMS pour entreprises",
      "Architecture WordPress B2B : ce que personne ne te dit avant de commencer",
      "Multi-entreprises sur WordPress : comment structurer sans tout recommencer dans 6 mois",
      "Onboarding apprenant B2B : les 3 étapes que la plupart des formateurs sautent",
      "Pourquoi ton CRM et ton LMS doivent parler le même langage",
    ],
    templates: [
      {
        label: "Post Architecture — Format Observation",
        hook: "80% des formateurs B2B ont un LMS WordPress. 20% ont un système.",
        corps: [
          "La différence ?",
          "",
          "Un LMS, c'est : une plateforme où les apprenants se connectent.",
          "Un système, c'est : LMS + CRM + accès groupés + onboarding auto + reporting client.",
          "",
          "Quand tu as un LMS :",
          "→ Tu gères manuellement les accès de chaque apprenant",
          "→ Tu relances à la main les RH pour les renouvellements",
          "→ Tu n'as aucune vue sur qui a vraiment utilisé ta formation",
          "",
          "Quand tu as un système :",
          "→ Un nouveau client entreprise s'onboarde en 48h sans toi",
          "→ Le renouvellement est relancé automatiquement à J-90",
          "→ Tu peux montrer à un DRH un tableau de bord de progression en temps réel",
          "",
          "Le problème ? Personne ne vend 'un système'.",
          "Tout le monde vend un LMS.",
          "",
          "C'est ce que je structure avec mes clients.",
        ],
        cta: "Tu es formateur B2B et ton WordPress commence à ressembler à un patchwork ? Je propose un audit architecture. Lien en bio.",
        format: "Observation + liste comparée",
        longueur_cible: "900 – 1 200 caractères",
      },
      {
        label: "Post Architecture — Format Question",
        hook: "Combien de temps tu passes chaque semaine à gérer manuellement des accès formation ?",
        corps: [
          "Si c'est plus de 2h, tu n'as pas un problème de productivité.",
          "Tu as un problème d'architecture.",
          "",
          "Un formateur B2B avec 10 entreprises clientes :",
          "Envoie des accès manuellement → 45 min / client",
          "Relance les RH pour les renouvellements → 1h / trimestre / client",
          "Génère des rapports QUALIOPI à la main → 3h / session",
          "",
          "Total : entre 8h et 15h / semaine d'administration pure.",
          "",
          "Sur WordPress, tout ça peut être automatisé.",
          "Onboarding → automatique.",
          "Relances → automatiques.",
          "Rapports → générés automatiquement.",
          "",
          "Ce n'est pas de la magie.",
          "C'est une architecture CRM + LMS bien structurée.",
        ],
        cta: "Si tu veux voir à quoi ressemble cette architecture sur ton cas précis, je propose un audit stratégique de 2 semaines.",
        format: "Question + chiffrage problème + solution",
        longueur_cible: "900 – 1 100 caractères",
      },
    ],
  },
  {
    num: "2",
    emoji: "🔵",
    nom: "Erreurs Fréquentes",
    objectif: "Créer de la tension → montrer l'expertise par la reconnaissance du problème. Les gens partagent ce qui les décrit.",
    frequence: "1 post / semaine",
    sujets: [
      "Créer un LMS sans penser multi-entreprise dès le début",
      "Vendre de la formation B2B avec un tunnel pensé pour les particuliers",
      "Ne pas automatiser l'onboarding : la première erreur qui coûte des renouvellements",
      "Confondre Kajabi et WordPress : ce que ça dit de ta stratégie",
      "Facturer à l'heure une prestation qui devrait être facturée au résultat",
      "Lancer QUALIOPI sans configurer le reporting WordPress",
      "Avoir 3 CRM différents et aucun pipeline B2B structuré",
      "Oublier la segmentation décideur / apprenant / RH dans son CRM",
    ],
    templates: [
      {
        label: "Post Erreur — Format Diagnostic",
        hook: "L'erreur que j'observe le plus souvent chez les formateurs B2B WordPress :",
        corps: [
          "Construire un LMS pour des particuliers, puis essayer de vendre à des entreprises.",
          "",
          "Concrètement :",
          "→ Un seul compte par apprenant (impossible à gérer en cohortes)",
          "→ Pas de vue 'entreprise cliente' dans le back-office",
          "→ Aucune segmentation RH / décideur / apprenant",
          "→ Rapports apprenants non exportables pour les DRH",
          "",
          "Résultat :",
          "Tu vends une prestation B2B avec un outil B2C.",
          "Ça fonctionne au début. Ça explose à la 5e entreprise cliente.",
          "",
          "La bonne architecture commence par une question :",
          "'Comment je veux gérer 20 entreprises dans 18 mois ?'",
          "",
          "Pas : 'Quel plugin LMS je prends ?'",
        ],
        cta: "Tu es dans cette situation ? Audit architecture en 2 semaines — lien en bio.",
        format: "Erreur + symptômes + racine + bonne question",
        longueur_cible: "850 – 1 050 caractères",
      },
    ],
  },
  {
    num: "3",
    emoji: "🟣",
    nom: "Études de Cas & Micro-Analyses",
    objectif: "Montrer l'expertise par l'exemple concret. Crédibilité maximale. Posts les plus partagés.",
    frequence: "1 post toutes les 2 semaines",
    sujets: [
      "Analyse d'un site formation B2B (structure, erreurs, recommandations)",
      "Décryptage architecture LMS d'un OF indépendant",
      "Comment j'optimiserais ce système WordPress en 3 points",
      "Avant / Après : architecture LMS B2B restructurée",
      "Ce que j'ai découvert en auditant 5 sites formation B2B",
      "Étude de cas : onboarding automatisé pour formateur corporate",
      "Micro-analyse : pourquoi ce tunnel formation B2B ne convertit pas",
      "Le CRM de ce formateur B2B : 3 problèmes cachés, 3 solutions simples",
    ],
    templates: [
      {
        label: "Post Analyse — Format Décryptage",
        hook: "J'ai analysé 5 sites de formateurs B2B cette semaine. Voici ce que j'ai trouvé.",
        corps: [
          "Même architecture, mêmes problèmes.",
          "",
          "Problème 1 — Le LMS est configuré pour des particuliers",
          "Pas de gestion multi-entreprises.",
          "Un compte = un apprenant. Impossible à scaler.",
          "",
          "Problème 2 — Pas de CRM structuré",
          "Les relances de renouvellement sont faites à la main.",
          "Ou pas faites du tout.",
          "",
          "Problème 3 — Le tunnel n'est pas qualifiant",
          "Le formulaire de contact est le même pour un particulier et un DRH.",
          "Résultat : 80% de leads non qualifiés.",
          "",
          "Ce que j'aurais restructuré en priorité :",
          "→ Passer à une architecture multi-comptes sur le LMS",
          "→ Installer FluentCRM avec une segmentation tripartite",
          "→ Créer une page devis B2B avec formulaire qualifiant",
          "",
          "3 changements. Impact immédiat sur la scalabilité.",
        ],
        cta: "Si tu veux que j'analyse ton architecture, je propose un audit stratégique de 2 semaines.",
        format: "Analyse + problèmes récurrents + recommandations",
        longueur_cible: "1 000 – 1 300 caractères",
      },
    ],
  },
];

const RYTHME = {
  freq: "2 à 3 posts / semaine",
  freq_mini: 2,
  freq_maxi: 3,
  jours_optimaux: ["Mardi", "Jeudi", "vendredi (optionnel)"],
  heure_optimale: "7h30 – 8h30",
  structure_post: [
    { partie: "Hook (ligne 1)", role: "Arrêter le scroll. Chiffre, affirmation forte, ou question directe.", longueur: "1 ligne, max 80 caractères" },
    { partie: "Développement", role: "Développer en 4 à 8 blocs courts. 1 idée par bloc. Pas de paragraphes denses.", longueur: "500 – 900 caractères" },
    { partie: "Mini-structure", role: "Liste à 3 points, comparaison Avant/Après, ou étapes numérotées.", longueur: "3 à 5 lignes" },
    { partie: "Conclusion", role: "Reformuler l'idée clé en 1 phrase. Orientée système, pas outil.", longueur: "1 à 2 lignes" },
    { partie: "CTA", role: "Doux, expert, non agressif. 1 seul CTA par post.", longueur: "1 à 2 lignes" },
  ],
  regles: [
    "Pas de blabla motivationnel vide",
    "Pas de '5 astuces pour...' généralistes",
    "Chaque post doit parler à un formateur B2B précis",
    "Jamais vendre directement — positionner, pas pitcher",
    "Maximum 1 lien externe par post (en commentaire si possible)",
    "Pas d'émojis décoratifs — seulement fonctionnels (→, ✓, ✗)",
    "Sauts de ligne entre chaque bloc — jamais de blocs denses",
    "Toujours en rapport avec architecture, rentabilité, ou automatisation B2B",
  ],
};

const HOOKS_BANK = [
  // Chiffres
  "80% des formateurs B2B ont un LMS. 20% ont un système.",
  "Un formateur B2B perd en moyenne 10h/semaine en administration évitable.",
  "3 formateurs B2B sur 4 n'automatisent pas leur renouvellement de contrat.",
  "Le taux de renouvellement moyen en formation B2B : 40%. Le mien après restructuration LMS : 72%.",
  // Questions
  "Combien de temps tu passes à gérer manuellement les accès de tes apprenants B2B ?",
  "Ton LMS WordPress est-il configuré pour des particuliers ou pour des entreprises ?",
  "Si tu perds un DRH après 1 an de formation, tu sais exactement pourquoi ?",
  "Ton onboarding client entreprise prend combien de jours aujourd'hui ?",
  // Affirmations fortes
  "Le problème des formateurs B2B n'est pas le contenu. C'est l'architecture.",
  "Un CRM sans segmentation B2B, ce n'est pas un CRM. C'est un carnet d'adresses.",
  "Kajabi ne peut pas faire ce que WordPress fait en B2B. Ce n'est pas une opinion — c'est une architecture.",
  "Un tunnel B2C ne convertit pas des RH. Jamais.",
  // Observations
  "J'ai audité 5 sites formation B2B cette semaine. Même problème partout.",
  "Ce que personne ne te dit avant de configurer un LMS WordPress B2B :",
  "L'erreur que j'observe le plus souvent chez les formateurs B2B :",
  "Voici ce qui se passe quand ton LMS n'est pas pensé multi-entreprises :",
];

const STRATEGIE_LEAD = {
  cta_standard: "Tu es formateur B2B et ton système WordPress commence à montrer ses limites ? Je propose un audit architecture en 2 semaines. Lien en bio.",
  cta_court: "Audit Architecture B2B — lien en bio.",
  cta_question: "Si tu veux que j'analyse ton architecture, je propose un audit stratégique.",
  regles_cta: [
    "1 seul CTA par post — jamais 2",
    "Toujours en fin de post, jamais au milieu",
    "Jamais un prix dans le post — l'audit filtre",
    "Formuler comme une invitation, pas une vente",
    "Varier les formulations toutes les 3 semaines",
  ],
};

const FUNNEL = [
  { etape: "1", action: "Post LinkedIn", role: "Attraction. Crédibilité. Visibilité niche.", kpi: "Impressions + taux engagement" },
  { etape: "2", action: "Profil optimisé", role: "Conversion visiteur → lead. Bio + section à propos + lien bio.", kpi: "Clics sur lien bio" },
  { etape: "3", action: "Message entrant (DM ou formulaire)", role: "Signal d'intérêt qualifié.", kpi: "DM entrants + formulaires soumis" },
  { etape: "4", action: "Qualification rapide", role: "Message de qualification en 1-2 questions.", kpi: "Taux de réponse qualifiée" },
  { etape: "5", action: "Audit Architecture B2B (1 200 – 1 800 €)", role: "Premier ticket. Filtre. Découverte du périmètre.", kpi: "Taux conversion entretien → audit signé" },
  { etape: "6", action: "Appel de restitution", role: "Restitution audit + proposition mission Niveau 2 ou 3.", kpi: "Taux conversion audit → proposition" },
  { etape: "7", action: "Proposition mission", role: "Devis Niveau 2 (4 500–7 000 €) ou Niveau 3 (8 000–15 000 €).", kpi: "Taux closing + panier moyen" },
];

const SEQUENCES_DM = [
  {
    declencheur: "Quelqu'un like un post",
    message: null,
    action: "Ne pas envoyer de DM immédiatement. Liker ses posts récents à la place.",
    regle: "L'intérêt doit venir de lui.",
  },
  {
    declencheur: "Quelqu'un commente un post",
    message: "Merci pour ton commentaire. Tu formes des entreprises actuellement ?",
    action: "Réponse publique d'abord. DM seulement si échange continue.",
    regle: "Question de qualification — jamais un pitch dans la foulée.",
  },
  {
    declencheur: "Quelqu'un visite le profil",
    message: "Bonjour [Prénom], j'ai vu que tu avais visité mon profil. Tu travailles dans la formation B2B ?",
    action: "Envoyer seulement si le profil visiteur est clairement B2B / formateur.",
    regle: "Ne pas envoyer si le profil ne correspond pas à la niche. Jamais en masse.",
  },
  {
    declencheur: "Quelqu'un répond positivement à la qualification",
    message: "Super. Est-ce que tu as déjà une architecture WordPress en place, ou tu pars de zéro ?",
    action: "Question 2 de qualification — comprendre la maturité.",
    regle: "L'objectif est de comprendre, pas de pitcher. Le pitch vient après 3-4 échanges.",
  },
  {
    declencheur: "Lead qualifié confirmé",
    message: "Dans ce cas, ça vaut le coup qu'on explore ça ensemble. Je propose un audit architecture de 2 semaines qui donne un plan précis. Tu veux qu'on planifie un appel de 20 min pour que je t'explique comment ça fonctionne ?",
    action: "Inviter à un appel — jamais envoyer le devis d'emblée.",
    regle: "L'appel de 20 min qualifie définitivement avant de proposer l'audit.",
  },
];

const KPIS = [
  {
    kpi: "Taux d'engagement",
    definition: "(Likes + commentaires + partages) / impressions × 100",
    objectif_m3: "> 3%",
    objectif_m6: "> 4%",
    objectif_m12: "> 5%",
    comment_mesurer: "LinkedIn Analytics natif — onglet Publications",
    alerte: "< 2% : revoir hooks et sujets",
  },
  {
    kpi: "DM entrants qualifiés",
    definition: "Messages reçus provenant de formateurs B2B avec un contexte précis",
    objectif_m3: "2 – 4 / mois",
    objectif_m6: "5 – 10 / mois",
    objectif_m12: "10 – 20 / mois",
    comment_mesurer: "Comptage manuel dans les DM + tag 'Qualifié' dans CRM",
    alerte: "0 DM après 6 semaines de posts : revoir la niche ciblée ou le CTA",
  },
  {
    kpi: "Demandes d'audit",
    definition: "Formulaire audit soumis OU DM demandant explicitement l'audit",
    objectif_m3: "1 – 2 / mois",
    objectif_m6: "3 – 5 / mois",
    objectif_m12: "5 – 10 / mois",
    comment_mesurer: "Formulaire schoolswp.com/audit-b2b + suivi CRM",
    alerte: "0 demande après 3 mois : revoir lien bio et CTA dans les posts",
  },
  {
    kpi: "Appels de découverte réalisés",
    definition: "Appels de 20 min avec leads qualifiés",
    objectif_m3: "1 – 2 / mois",
    objectif_m6: "3 – 5 / mois",
    objectif_m12: "6 – 10 / mois",
    comment_mesurer: "Calendrier + CRM",
    alerte: "< 50% de taux de présence : revoir processus de confirmation",
  },
  {
    kpi: "Taux de closing audit",
    definition: "Appels de découverte → audit signé",
    objectif_m3: "> 30%",
    objectif_m6: "> 40%",
    objectif_m12: "> 50%",
    comment_mesurer: "CRM pipeline",
    alerte: "< 20% : revoir présentation audit et qualification amont",
  },
  {
    kpi: "Panier moyen mission",
    definition: "CA total missions / nombre missions signées",
    objectif_m6: "> 5 000 €",
    objectif_m12: "> 8 000 €",
    comment_mesurer: "Factures émises / missions signées",
    alerte: "< 4 000 € : revoir positionnement et process de qualification",
  },
];

const SYNERGIE_SEO_LINKEDIN = [
  {
    etape: "1",
    action: "Article SEO B2B publié sur schoolswp.com",
    exemple: "Guide : LMS WordPress pour entreprises — architecture complète",
  },
  {
    etape: "2",
    action: "Post LinkedIn résumé (angle + hook fort)",
    exemple: "Post : 'Pourquoi un LMS standard ne suffit pas pour la formation B2B' (résume l'article en 1 000 caractères)",
  },
  {
    etape: "3",
    action: "Lien vers l'article dans le 1er commentaire (pas dans le post)",
    exemple: "Commentaire : 'J'ai détaillé l'architecture complète ici : [lien article]'",
  },
  {
    etape: "4",
    action: "CTA audit en fin de post",
    exemple: "Si tu reconnais ton système, je propose un audit architecture — lien en bio.",
  },
  {
    etape: "5",
    action: "Leads entrants vers formulaire audit → qualification → mission",
    exemple: "Formulaire schoolswp.com/audit-b2b avec 5 questions qualifiantes",
  },
];

const CALENDRIER_TYPE = [
  {
    semaine: 1,
    posts: [
      { jour: "Mardi", pilier: "P1 — Architecture", sujet: "Pourquoi 80% des LMS B2B sont mal structurés", hook: "80% des formateurs B2B ont un LMS. 20% ont un système." },
      { jour: "Jeudi", pilier: "P2 — Erreur", sujet: "Vendre en B2B avec un tunnel B2C", hook: "Un tunnel B2C ne convertit pas des RH. Jamais." },
    ],
  },
  {
    semaine: 2,
    posts: [
      { jour: "Mardi", pilier: "P1 — Architecture", sujet: "CRM mal segmenté = contrats perdus silencieusement", hook: "Un CRM sans segmentation B2B, ce n'est pas un CRM. C'est un carnet d'adresses." },
      { jour: "Jeudi", pilier: "P3 — Étude de cas", sujet: "J'ai audité 5 sites formation B2B — voici ce que j'ai trouvé", hook: "J'ai analysé 5 sites de formateurs B2B cette semaine. Même problème partout." },
      { jour: "Vendredi", pilier: "P2 — Erreur", sujet: "Ne pas automatiser l'onboarding entreprise", hook: "Combien de temps tu passes à gérer manuellement les accès formation ?" },
    ],
  },
  {
    semaine: 3,
    posts: [
      { jour: "Mardi", pilier: "P1 — Architecture", sujet: "Architecture idéale LMS WordPress B2B", hook: "Ce que personne ne te dit avant de configurer un LMS WordPress B2B :" },
      { jour: "Jeudi", pilier: "P2 — Erreur", sujet: "Confondre Kajabi et WordPress pour le B2B", hook: "Kajabi ne peut pas faire ce que WordPress fait en B2B. Ce n'est pas une opinion — c'est une architecture." },
    ],
  },
  {
    semaine: 4,
    posts: [
      { jour: "Mardi", pilier: "P3 — Étude de cas", sujet: "Avant / Après : LMS restructuré pour formateur B2B", hook: "Avant l'audit : 8h/semaine d'administration manuelle. Après : 45 min." },
      { jour: "Jeudi", pilier: "P1 — Architecture", sujet: "Renouvellement contrat formation : comment l'automatiser", hook: "3 formateurs B2B sur 4 n'automatisent pas leur renouvellement de contrat." },
    ],
  },
];

const DIFFERENCIATEURS = {
  majorite_dit: ["Design", "Performance", "Plugins", "Vitesse de chargement", "Thèmes", "Sécurité"],
  toi_tu_dis: ["Architecture", "Rentabilité", "Structuration B2B", "Automatisation cycle long", "Scalabilité multi-clients", "Vision LTV"],
  angle_cle: "Tu parles la langue des décideurs B2B — pas la langue des développeurs.",
  preuves: [
    "Tu utilises des termes business (pipeline, LTV, renouvellement, cycle long, QUALIOPI)",
    "Tu chiffres l'impact (heures économisées, taux de renouvellement, CA généré)",
    "Tu penses système, pas outil",
    "Tu cites des cas concrets, pas des théories générales",
    "Tu parles à la personne, pas à son problème technique",
  ],
};

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

// ─── TEMPLATE ────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // HEADER
  blocks.push(qot("🔗 Stratégie LinkedIn B2B · schoolsWP · Machine à Crédibilité · Document Stratégique", "yellow_background"));
  blocks.push(p([rt("Pas du contenu LinkedIn. Une machine à crédibilité, qualification et rendez-vous premium.", { italic: true, bold: true })]));
  blocks.push(div());

  // ── PROFIL LINKEDIN ──
  blocks.push(h1("🎯 Profil LinkedIn — La Fondation"));
  blocks.push(p([rt("Le profil convertit. Un post peut attirer 1 000 vues. Si le profil ne convertit pas, c'est 0 lead.", { italic: true })]));
  blocks.push(p(""));

  blocks.push(h2("Bio — Ce qui ne doit PAS y être :"));
  PROFIL.bio_a_ne_pas_dire.forEach((b) => blocks.push(bul([rt("✗  " + b, { color: "red" })], "red_background")));
  blocks.push(p(""));

  blocks.push(h2("Bio — Ce qu'elle doit dire :"));
  blocks.push(cal([rt(PROFIL.bio_cible, { bold: true })], "green_background"));
  blocks.push(p(""));

  blocks.push(p([rt("Tagline court : ", { bold: true }), rt(PROFIL.tagline_court, { italic: true })]));
  blocks.push(p([rt("Lien bio : ", { bold: true }), rt(PROFIL.lien_bio, { code: true })]));
  blocks.push(p([rt("Banner : ", { bold: true }), rt(PROFIL.banner_message, { italic: true })]));
  blocks.push(p(""));

  blocks.push(h2("Section À propos — Texte complet"));
  const aProposChildren = [];
  PROFIL.section_a_propos.forEach((ligne) => {
    if (ligne === "") {
      aProposChildren.push(p(""));
    } else {
      aProposChildren.push(p(ligne));
    }
  });
  blocks.push(tog("📝 Voir le texte complet de la section À propos", aProposChildren));
  blocks.push(div());

  // ── 3 PILIERS ──
  blocks.push(h1("🧠 Stratégie Éditoriale — 3 Piliers"));
  blocks.push(p([rt("Chaque post appartient à 1 pilier. Rotation équilibrée. Cohérence thématique.", { italic: true })]));
  blocks.push(p(""));

  for (const pilier of PILIERS) {
    blocks.push(h2(`${pilier.emoji} Pilier ${pilier.num} — ${pilier.nom}`));
    blocks.push(p([rt("Objectif : ", { bold: true }), rt(pilier.objectif)]));
    blocks.push(p([rt("Fréquence : ", { bold: true }), rt(pilier.frequence)]));
    blocks.push(p(""));

    blocks.push(h3("Sujets à traiter"));
    pilier.sujets.forEach((s, i) => blocks.push(bul([rt(`${i + 1}. `, { bold: true }), rt(s)])));
    blocks.push(p(""));

    blocks.push(h3("Templates de posts"));
    for (const tpl of pilier.templates) {
      const tplChildren = [];
      tplChildren.push(p([rt("Format : ", { bold: true }), rt(tpl.format)]));
      tplChildren.push(p([rt("Longueur cible : ", { bold: true }), rt(tpl.longueur_cible)]));
      tplChildren.push(p(""));
      tplChildren.push(h3("Hook"));
      tplChildren.push(qot(tpl.hook, "blue_background"));
      tplChildren.push(p(""));
      tplChildren.push(h3("Corps"));
      tpl.corps.forEach((ligne) => {
        if (ligne === "") {
          tplChildren.push(p(""));
        } else {
          tplChildren.push(p(ligne));
        }
      });
      tplChildren.push(p(""));
      tplChildren.push(h3("CTA"));
      tplChildren.push(cal(tpl.cta, "green_background"));

      blocks.push(tog(`📄 ${tpl.label}`, tplChildren));
      blocks.push(p(""));
    }

    blocks.push(div());
  }

  // ── BANQUE DE HOOKS ──
  blocks.push(h1("🎣 Banque de Hooks — 16 Formulations Testables"));
  blocks.push(p([rt("Le hook = la 1ère ligne. C'est elle qui détermine si le post est lu. Tester 1 nouveau hook toutes les 2 semaines.", { italic: true })]));
  blocks.push(p(""));

  const hookCategories = [
    { label: "Hooks Chiffres", items: HOOKS_BANK.slice(0, 4) },
    { label: "Hooks Questions", items: HOOKS_BANK.slice(4, 8) },
    { label: "Hooks Affirmations Fortes", items: HOOKS_BANK.slice(8, 12) },
    { label: "Hooks Observations", items: HOOKS_BANK.slice(12, 16) },
  ];

  for (const cat of hookCategories) {
    const children = cat.items.map((h) => bul([rt('"'), rt(h, { italic: true }), rt('"')]));
    blocks.push(tog(cat.label, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── RYTHME & STRUCTURE ──
  blocks.push(h1("📅 Rythme & Structure des Posts"));
  blocks.push(p(""));
  blocks.push(bul([rt("Fréquence : ", { bold: true }), rt(RYTHME.freq, { bold: true, color: "green" })]));
  blocks.push(bul([rt("Jours optimaux : ", { bold: true }), rt(RYTHME.jours_optimaux.join(", "))]));
  blocks.push(bul([rt("Heure idéale : ", { bold: true }), rt(RYTHME.heure_optimale)]));
  blocks.push(p(""));

  blocks.push(h2("Structure Anatomiée d'un Post"));
  for (const s of RYTHME.structure_post) {
    const children = [
      p([rt("Rôle : ", { bold: true }), rt(s.role)]),
      p([rt("Longueur : ", { bold: true }), rt(s.longueur)]),
    ];
    blocks.push(tog(s.partie, children));
    blocks.push(p(""));
  }

  blocks.push(h2("Règles Non Négociables"));
  RYTHME.regles.forEach((r) => blocks.push(bul([rt("⛔  " + r, { bold: true })], "red_background")));
  blocks.push(div());

  // ── STRATÉGIE LEAD ──
  blocks.push(h1("🧲 Stratégie Lead — CTA & Funnel"));
  blocks.push(p(""));

  blocks.push(h2("CTAs Variantes"));
  blocks.push(bul([rt("Standard : ", { bold: true }), rt(`"${STRATEGIE_LEAD.cta_standard}"`, { italic: true })]));
  blocks.push(bul([rt("Court : ", { bold: true }), rt(`"${STRATEGIE_LEAD.cta_court}"`, { italic: true })]));
  blocks.push(bul([rt("Question : ", { bold: true }), rt(`"${STRATEGIE_LEAD.cta_question}"`, { italic: true })]));
  blocks.push(p(""));

  blocks.push(h2("Règles des CTAs"));
  STRATEGIE_LEAD.regles_cta.forEach((r) => blocks.push(bul(r)));
  blocks.push(p(""));

  blocks.push(h2("Funnel LinkedIn Complet"));
  for (const f of FUNNEL) {
    const children = [
      p([rt("Rôle : ", { bold: true }), rt(f.role)]),
      p([rt("KPI : ", { bold: true }), rt(f.kpi)]),
    ];
    blocks.push(tog(`Étape ${f.etape} — ${f.action}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SÉQUENCES DM ──
  blocks.push(h1("💬 Séquences DM — Qualification Intelligente"));
  blocks.push(cal("Jamais pitcher directement. Qualifier d'abord. L'objectif du DM : comprendre, pas vendre.", "yellow_background"));
  blocks.push(p(""));

  for (const dm of SEQUENCES_DM) {
    const children = [];
    children.push(p([rt("Déclencheur : ", { bold: true }), rt(dm.declencheur, { italic: true })]));
    if (dm.message) {
      children.push(p(""));
      children.push(h3("Message à envoyer"));
      children.push(qot(`"${dm.message}"`, "blue_background"));
    }
    children.push(p(""));
    children.push(p([rt("Action complémentaire : ", { bold: true }), rt(dm.action)]));
    children.push(p([rt("Règle : ", { bold: true }), rt(dm.regle, { italic: true, color: "gray" })]));

    blocks.push(tog(`📩 ${dm.declencheur}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── KPIs ──
  blocks.push(h1("📈 KPIs LinkedIn à Suivre"));
  blocks.push(p([rt("Un KPI non mesuré n'existe pas. Tableau de bord mensuel, 30 minutes max.", { italic: true })]));
  blocks.push(p(""));

  for (const kpi of KPIS) {
    const children = [];
    children.push(p([rt("Définition : ", { bold: true }), rt(kpi.definition)]));
    if (kpi.objectif_m3) children.push(p([rt("Objectif M3 : ", { bold: true }), rt(kpi.objectif_m3, { color: "green" })]));
    if (kpi.objectif_m6) children.push(p([rt("Objectif M6 : ", { bold: true }), rt(kpi.objectif_m6, { bold: true, color: "green" })]));
    if (kpi.objectif_m12) children.push(p([rt("Objectif M12 : ", { bold: true }), rt(kpi.objectif_m12, { bold: true, color: "green" })]));
    children.push(p([rt("Comment mesurer : ", { bold: true }), rt(kpi.comment_mesurer)]));
    children.push(p([rt("⚠️  Alerte : ", { bold: true, color: "red" }), rt(kpi.alerte, { color: "red" })]));

    blocks.push(tog(`📊 ${kpi.kpi}`, children));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── SYNERGIE SEO + LINKEDIN ──
  blocks.push(h1("🚀 Synergie SEO + LinkedIn"));
  blocks.push(cal("Chaque contenu doit vivre 2 fois. Article SEO → Post LinkedIn. Un travail, deux canaux.", "green_background"));
  blocks.push(p(""));

  for (const s of SYNERGIE_SEO_LINKEDIN) {
    blocks.push(bul([
      rt(`Étape ${s.etape} — `, { bold: true }),
      rt(s.action, { bold: true }),
    ]));
    blocks.push(bul([rt(`→ Exemple : ${s.exemple}`, { italic: true, color: "gray" })], "gray_background"));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── CALENDRIER TYPE 4 SEMAINES ──
  blocks.push(h1("📅 Calendrier Type — 4 Semaines"));
  blocks.push(p([rt("Modèle à adapter chaque mois selon les articles SEO publiés.", { italic: true })]));
  blocks.push(p(""));

  for (const sem of CALENDRIER_TYPE) {
    const semChildren = [];
    for (const post of sem.posts) {
      semChildren.push(bul([
        rt(`${post.jour} · `, { bold: true }),
        rt(`${post.pilier}`, { bold: true, color: "blue" }),
        rt(` — ${post.sujet}`),
      ]));
      semChildren.push(bul([rt(`Hook : "${post.hook}"`, { italic: true, color: "gray" })], "gray_background"));
      semChildren.push(p(""));
    }
    blocks.push(tog(`Semaine ${sem.semaine} — ${sem.posts.length} posts`, semChildren));
    blocks.push(p(""));
  }

  blocks.push(div());

  // ── DIFFÉRENCIATION ──
  blocks.push(h1("🔥 Différenciation — Ce qui Change Tout"));
  blocks.push(p(""));

  blocks.push(h2("Les autres freelances WordPress parlent de :"));
  DIFFERENCIATEURS.majorite_dit.forEach((d) => blocks.push(bul([rt("✗  " + d, { color: "red" })], "red_background")));
  blocks.push(p(""));

  blocks.push(h2("Toi, tu parles de :"));
  DIFFERENCIATEURS.toi_tu_dis.forEach((d) => blocks.push(bul([rt("✓  " + d, { bold: true, color: "green" })], "green_background")));
  blocks.push(p(""));

  blocks.push(qot(DIFFERENCIATEURS.angle_cle, "blue_background"));
  blocks.push(p(""));

  blocks.push(h2("Preuves concrètes de cette différenciation"));
  DIFFERENCIATEURS.preuves.forEach((pr) => blocks.push(bul(pr)));
  blocks.push(div());

  // ── CHECKLIST LANCEMENT ──
  blocks.push(h1("✅ Checklist — Avant de Publier le Premier Post"));
  blocks.push(p(""));

  const checklist = [
    "Bio LinkedIn mise à jour avec le positionnement B2B exact",
    "Section 'À propos' rédigée et publiée",
    "Lien bio pointant vers schoolswp.com/audit-b2b (ou page dédiée)",
    "Banner LinkedIn mis à jour (Architecture WordPress B2B · schoolsWP)",
    "Photo de profil professionnelle (fond neutre, sourire discret, pas de selfie)",
    "10 premiers posts planifiés dans Notion avec hooks et sujets",
    "Pipeline CRM créé pour tracker : DM → Qualifié → Appel → Audit → Mission",
    "Formulaire d'audit actif sur le site (test complet effectué)",
    "Réponse type DM rédigée et sauvegardée (qualification en 2 questions)",
    "KPI dashboard Notion créé (à remplir chaque mois, 30 min)",
  ];

  checklist.forEach((item) => {
    blocks.push({
      object: "block",
      type: "to_do",
      to_do: { rich_text: [rt(item)], checked: false },
    });
  });

  blocks.push(div());

  // ── VISION ──
  blocks.push(h1("🏆 Ce que cette Stratégie construit en 12 mois"));
  blocks.push(p(""));
  blocks.push(cal(
    "Une réputation précise et mémorable dans une niche où personne ne s'est encore positionné clairement. Chaque post renforce l'expertise. Chaque DM qualifie. Chaque audit ouvre une mission.",
    "purple_background"
  ));
  blocks.push(p(""));

  const vision12m = [
    "500 – 2 000 abonnés qualifiés (formateurs B2B, RH, DRH, OFs)",
    "10 – 20 DM qualifiés / mois en régime de croisière",
    "3 – 5 demandes d'audit / mois",
    "2 – 4 missions signées / mois",
    "Synergie SEO + LinkedIn : double exposition sur chaque contenu",
    "Réputation : référence WordPress B2B dans les cercles formateurs francophones",
  ];

  vision12m.forEach((v) => blocks.push(bul([rt("→ " + v, { bold: true })])));
  blocks.push(p(""));
  blocks.push(qot("LinkedIn n'est pas un réseau social pour toi. C'est ton canal de qualification et de crédibilité B2B. Traite-le comme tel.", "green_background"));

  return blocks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("🚀  Création de la page Stratégie LinkedIn B2B...");

  const allBlocks = buildTemplate();
  console.log(`📦  ${allBlocks.length} blocs générés`);

  const firstChunk = allBlocks.slice(0, CHUNK);
  const rest = allBlocks.slice(CHUNK);

  const page = await notionRequest("POST", "/pages", {
    parent: { page_id: PARENT_PAGE_ID },
    icon: { type: "emoji", emoji: "🔗" },
    properties: {
      title: { title: [{ text: { content: "🔗 Stratégie LinkedIn B2B — Machine à Crédibilité" } }] },
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
  console.log("📋  Contenu de la page :");
  console.log("   · Profil LinkedIn optimisé (bio + à propos complet)");
  console.log("   · 3 piliers éditoriaux + sujets + templates de posts");
  console.log("   · 16 hooks testables (4 catégories)");
  console.log("   · Calendrier type 4 semaines (9 posts planifiés)");
  console.log("   · 5 séquences DM qualification intelligente");
  console.log("   · 6 KPIs avec objectifs M3 / M6 / M12");
  console.log("   · Synergie SEO + LinkedIn en 5 étapes");
  console.log("   · Checklist 10 points avant premier post");
}

main().catch((err) => {
  console.error("❌  Erreur :", err.message);
  process.exit(1);
});
