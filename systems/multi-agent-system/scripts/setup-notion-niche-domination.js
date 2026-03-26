#!/usr/bin/env node
/**
 * setup-notion-niche-domination.js — Stratégie domination niche schoolsWP
 *
 * Crée la page "🎯 Niche Domination — [Niche choisie]" avec :
 *   Section 1 — Comparatif des 5 niches candidates (scoring)
 *   Section 2 — Niche choisie + Angle stratégique
 *   Section 3 — Structure de domination (Pilier → 6 satellites → 3 comparatifs → 3 transactionnels)
 *   Section 4 — Plan 90 jours (Mois 1 Fondations / Mois 2 Comparatifs / Mois 3 Optimisation)
 *   Section 5 — KPI de domination (SEO · LLM · Business)
 *   Section 6 — Effet business attendu (affiliés · lead magnet · formation · SASU)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   node scripts/setup-notion-niche-domination.js [--niche crm|lms|automatisation|consultant|performance]
 *
 * Défaut : --niche crm
 * Pré-requis : Node 18+
 */

const API_KEY = process.env.NOTION_API_KEY;
const PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;

if (!API_KEY || !PAGE_ID) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY + NOTION_PARENT_PAGE_ID');
  process.exit(1);
}

const args    = process.argv.slice(2);
const getArg  = (flag, def) => { const i = args.indexOf(flag); return i !== -1 && args[i + 1] ? args[i + 1] : def; };
const NICHE   = getArg('--niche', 'crm').toLowerCase();

// ─── Configurations des 5 niches ──────────────────────────────────────────────

const NICHES = {
  crm: {
    emoji: '💬',
    nom: 'CRM WordPress pour formateurs',
    angle: 'Automatiser son activité de formation avec WordPress natif.',
    differentiation: 'Perspective formateur/solopreneur, pas agence ou e-commerce',
    plugin_principal: 'FluentCRM',
    scoring: { expertise: 5, affilie: 5, specificite: 4, concurrence: 4, coherence: 5, total: 23 },
    verdict: 'RECOMMANDÉ — expertise réelle + affiliés forts + angle différenciant',
    pilier: {
      titre: 'CRM WordPress : Guide complet pour formateurs',
      keyword: 'CRM WordPress formateur',
      intent: 'Informationnelle + Autorité'
    },
    phase1: [
      { titre: 'FluentCRM vs MailerLite : lequel choisir pour son école WordPress ?', intent: 'Comparative' },
      { titre: 'Automatisation email LMS WordPress : le guide complet',               intent: 'Informationnelle' },
      { titre: 'Segmentation avancée WordPress avec FluentCRM',                       intent: 'Informationnelle' },
      { titre: 'Tunnel email formation WordPress : configuration pas à pas',           intent: 'Informationnelle' },
      { titre: 'CRM natif WordPress vs SaaS : ce que personne ne te dit',             intent: 'Comparative'      },
      { titre: '7 erreurs CRM WordPress qui font perdre des leads',                   intent: 'Informationnelle' }
    ],
    phase2: [
      { titre: 'FluentCRM vs ActiveCampaign : le comparatif honnête',                intent: 'Comparative' },
      { titre: 'FluentCRM + Tutor LMS : le système complet école en ligne',          intent: 'Intégration'  },
      { titre: 'CRM WordPress gratuit vs premium : ce que vaut vraiment chaque option', intent: 'Comparative' }
    ],
    phase3: [
      { titre: 'Avis FluentCRM 2026 : mon retour après 12 mois d\'utilisation',       intent: 'Décisionnelle' },
      { titre: 'Tutor LMS + FluentCRM : ma stack complète de formation',              intent: 'Décisionnelle' },
      { titre: 'Pack CRM WordPress recommandé par schoolsWP',                         intent: 'Décisionnelle' }
    ],
    affilies: ['FluentCRM — ~25€/vente', 'Tutor LMS — ~30€/vente'],
    lead_magnet: '"Checklist Stack CRM WordPress pour formateurs" (PDF)',
    formation_future: '"Système automatisé WordPress pour formateurs" (formation)',
    kpi_seo: [
      'Pilier en position 1-5 sur "CRM WordPress"',
      '5 satellites en top 10 sur leurs mots-clés respectifs',
      'Domination "FluentCRM WordPress francophone"'
    ],
    kpi_llm: [
      'Cité comme référence "CRM WordPress formateur" dans Perplexity + ChatGPT',
      'Blocs FAQ indexés en AI Overview Google sur "FluentCRM" et "CRM WordPress"'
    ],
    kpi_biz: [
      'Revenus affiliés FluentCRM > 200€/mois en fin de Q3',
      'Lead magnet : 50+ téléchargements/mois',
      'Taux clic affilié > 5% sur les 3 articles transactionnels'
    ]
  },

  lms: {
    emoji: '🎓',
    nom: 'LMS WordPress avancé — Tutor LMS deep dive',
    angle: 'Construire une école en ligne rentable avec WordPress.',
    differentiation: 'Focus profitabilité et automatisation, pas "comment installer Tutor LMS"',
    plugin_principal: 'Tutor LMS',
    scoring: { expertise: 5, affilie: 5, specificite: 5, concurrence: 4, coherence: 5, total: 24 },
    verdict: 'TRÈS FORT — cohérence schoolsWP maximale + marché en croissance',
    pilier: {
      titre: 'Tutor LMS : Guide complet pour construire une école en ligne rentable',
      keyword: 'LMS WordPress rentable école en ligne',
      intent: 'Informationnelle + Autorité'
    },
    phase1: [
      { titre: 'Paiement LMS WordPress : WooCommerce vs plugins natifs Tutor',          intent: 'Comparative'      },
      { titre: 'Automatiser son école en ligne avec Tutor LMS et FluentCRM',           intent: 'Informationnelle' },
      { titre: 'Tracking apprenants WordPress : mesurer ce qui compte vraiment',        intent: 'Informationnelle' },
      { titre: 'Upsell école en ligne WordPress : stratégie pas à pas',                intent: 'Informationnelle' },
      { titre: 'Abonnement LMS WordPress : configurer un accès récurrent',             intent: 'Informationnelle' },
      { titre: 'Tutor LMS vs LearnPress : comparatif honnête 2026',                   intent: 'Comparative'      }
    ],
    phase2: [
      { titre: 'Tutor LMS vs LearnDash : lequel choisir pour son école ?',            intent: 'Comparative'  },
      { titre: 'Tutor LMS vs LifterLMS : le vrai comparatif 2026',                   intent: 'Comparative'  },
      { titre: 'Tutor LMS + FluentCRM : le système école en ligne complet',           intent: 'Intégration'  }
    ],
    phase3: [
      { titre: 'Avis Tutor LMS 2026 : mon retour complet après 18 mois',             intent: 'Décisionnelle' },
      { titre: 'Meilleur LMS WordPress gratuit : ce que je recommande vraiment',      intent: 'Décisionnelle' },
      { titre: 'Pack école en ligne WordPress recommandé par schoolsWP',              intent: 'Décisionnelle' }
    ],
    affilies: ['Tutor LMS — ~30€/vente', 'FluentCRM — ~25€/vente'],
    lead_magnet: '"Blueprint École en Ligne WordPress Rentable" (template Notion)',
    formation_future: '"De 0 à 10 000€/mois avec son école WordPress" (formation)',
    kpi_seo: [
      'Pilier en position 1-5 sur "LMS WordPress"',
      'Comparatifs Tutor LMS vs en top 3 SERP francophone',
      'Domination "Tutor LMS français"'
    ],
    kpi_llm: [
      'Référence "LMS WordPress" dans les réponses IA généralistes',
      'FAQ LMS indexée en AI Overview Google'
    ],
    kpi_biz: [
      'Revenus affiliés Tutor LMS > 300€/mois en fin de Q3',
      'Lead magnet Blueprint : 100+ téléchargements/mois',
      'Articles comparatifs : CTR affilié > 6%'
    ]
  },

  automatisation: {
    emoji: '⚙️',
    nom: 'Automatisation WordPress pour solopreneurs',
    angle: 'Remplacer 5 SaaS par un système WordPress optimisé.',
    differentiation: 'Angle souveraineté numérique + économies SaaS — pas juste "automatiser"',
    plugin_principal: 'n8n',
    scoring: { expertise: 5, affilie: 4, specificite: 5, concurrence: 5, coherence: 5, total: 24 },
    verdict: 'DIFFÉRENCIANT — angle unique sur le marché francophone WordPress',
    pilier: {
      titre: 'Automatisation WordPress : Remplacer 5 SaaS avec un système natif',
      keyword: 'automatisation WordPress solopreneur',
      intent: 'Informationnelle + Autorité'
    },
    phase1: [
      { titre: 'n8n + WordPress : automatiser sans Zapier ni Make',                   intent: 'Informationnelle' },
      { titre: 'CRM natif WordPress : zéro abonnement SaaS',                         intent: 'Informationnelle' },
      { titre: 'Booking WordPress sans plugin payant : la configuration complète',    intent: 'Informationnelle' },
      { titre: 'Tunnel de vente WordPress sans ClickFunnels',                         intent: 'Comparative'      },
      { titre: 'Webhooks WordPress : connecter n\'importe quel outil externe',        intent: 'Informationnelle' },
      { titre: 'Stack solopreneur WordPress : les 7 plugins qui remplacent tout',     intent: 'Décisionnelle'    }
    ],
    phase2: [
      { titre: 'n8n vs Zapier pour WordPress : le vrai comparatif 2026',             intent: 'Comparative'  },
      { titre: 'Make vs n8n : lequel choisir pour automatiser WordPress ?',          intent: 'Comparative'  },
      { titre: 'Automatisation email WordPress : n8n + FluentCRM complet',           intent: 'Intégration'  }
    ],
    phase3: [
      { titre: 'Avis n8n 2026 : mon retour après 1 an d\'automatisation WordPress', intent: 'Décisionnelle' },
      { titre: 'Stack automatisation WordPress gratuit : ce qui marche vraiment',    intent: 'Décisionnelle' },
      { titre: 'Pack automatisation solopreneur recommandé par schoolsWP',           intent: 'Décisionnelle' }
    ],
    affilies: ['n8n Cloud — ~40€/vente', 'FluentCRM — ~25€/vente'],
    lead_magnet: '"Audit Stack SaaS → WordPress : combien tu peux économiser" (calculateur)',
    formation_future: '"WordPress Autonome : le système solopreneur sans abonnements" (formation)',
    kpi_seo: [
      'Pilier en position 1-5 sur "automatisation WordPress"',
      'Domination requêtes "n8n WordPress" en francophone',
      'Top 3 sur "remplacer Zapier WordPress"'
    ],
    kpi_llm: [
      'Cité sur "remplacer SaaS WordPress" dans Perplexity et ChatGPT',
      'Blocs définitions "automation WordPress" indexés en AI Overview'
    ],
    kpi_biz: [
      'Revenus affiliés n8n Cloud > 200€/mois en fin de Q3',
      'Calculateur téléchargé 200+ fois/mois',
      'Taux clic affilié n8n > 4% sur article "Avis n8n"'
    ]
  },

  consultant: {
    emoji: '💼',
    nom: 'WordPress pour consultants et coachs',
    angle: 'Site WordPress structuré pour vendre des services à haute valeur.',
    differentiation: 'Focus vente de services et positionnement expert, pas technique WordPress pure',
    plugin_principal: 'FluentCRM',
    scoring: { expertise: 4, affilie: 4, specificite: 4, concurrence: 3, coherence: 4, total: 19 },
    verdict: 'BON — marché large mais moins différenciant que CRM ou LMS pour schoolsWP',
    pilier: {
      titre: 'WordPress pour coachs : site structuré pour vendre vos services',
      keyword: 'site WordPress coach consultant',
      intent: 'Informationnelle + Autorité'
    },
    phase1: [
      { titre: 'Calendrier de réservation WordPress : la configuration complète',     intent: 'Informationnelle' },
      { titre: 'Paiement consultation WordPress : encaisser sans Stripe seul',        intent: 'Informationnelle' },
      { titre: 'CRM pour coachs WordPress : gérer ses clients sans SaaS',            intent: 'Informationnelle' },
      { titre: 'Séquence email service WordPress : convertir les prospects',          intent: 'Informationnelle' },
      { titre: 'Tunnel de vente services WordPress : de la landing au paiement',     intent: 'Informationnelle' },
      { titre: 'Site coach WordPress vs Squarespace : ce que les coachs ne disent pas', intent: 'Comparative'   }
    ],
    phase2: [
      { titre: 'Calendly vs WordPress natif pour consultants : le vrai comparatif',  intent: 'Comparative' },
      { titre: 'Site coach WordPress vs Linktree + Notion : l\'analyse complète',    intent: 'Comparative' },
      { titre: 'CRM coach : FluentCRM vs HubSpot gratuit vs Notion',                intent: 'Comparative' }
    ],
    phase3: [
      { titre: 'Les meilleurs outils WordPress pour coachs en 2026',                 intent: 'Décisionnelle' },
      { titre: 'Pack site coach WordPress : ma recommandation complète',             intent: 'Décisionnelle' },
      { titre: 'Site coach rentable WordPress : le blueprint schoolsWP',             intent: 'Décisionnelle' }
    ],
    affilies: ['FluentCRM — ~25€/vente', 'Elementor Pro — ~50€/vente'],
    lead_magnet: '"Checklist Site WordPress pour Coachs : 20 points à vérifier" (PDF)',
    formation_future: '"WordPress pour coachs : de 0 à 5 clients/mois" (mini-formation)',
    kpi_seo: [
      'Pilier en position 1-5 sur "site WordPress coach"',
      'Domination "consultant WordPress" + "coach WordPress francophone"'
    ],
    kpi_llm: [
      'Cité comme référence coach+WordPress dans les réponses IA',
      'Comparatifs Calendly indexés en AI Overview'
    ],
    kpi_biz: [
      'Revenus affiliés Elementor > 150€/mois en fin de Q3',
      'Lead magnet checklist : 80+ téléchargements/mois'
    ]
  },

  performance: {
    emoji: '⚡',
    nom: 'Performance + Rentabilité WordPress',
    angle: 'Optimiser WordPress pour le business, pas pour le score PageSpeed.',
    differentiation: 'Angle ROI et conversion — "la vitesse qui vend", pas technique pure',
    plugin_principal: 'WP Rocket',
    scoring: { expertise: 4, affilie: 4, specificite: 4, concurrence: 3, coherence: 4, total: 19 },
    verdict: 'BON — angle branding fort mais monétisation indirecte (hébergement + cache)',
    pilier: {
      titre: 'Performance WordPress : optimiser pour le business, pas PageSpeed',
      keyword: 'performance WordPress business conversion',
      intent: 'Informationnelle + Autorité'
    },
    phase1: [
      { titre: 'Cache WordPress business : WP Rocket vs LiteSpeed en conditions réelles', intent: 'Comparative'   },
      { titre: 'Core Web Vitals e-commerce WordPress : ce qui impacte les ventes',       intent: 'Informationnelle' },
      { titre: 'Images WordPress SEO + performance : la configuration complète',          intent: 'Informationnelle' },
      { titre: 'Performance LMS WordPress : Tutor LMS à pleine vitesse',                 intent: 'Informationnelle' },
      { titre: 'Hébergement WordPress business : benchmark 2026',                        intent: 'Comparative'      },
      { titre: '7 plugins WordPress qui ralentissent ton business sans que tu le saches', intent: 'Informationnelle' }
    ],
    phase2: [
      { titre: 'LiteSpeed vs WP Rocket : le comparatif honnête 2026',                  intent: 'Comparative'  },
      { titre: 'Hébergement WordPress : Kinsta vs o2switch vs SiteGround',              intent: 'Comparative'  },
      { titre: 'Vitesse vs conversion WordPress : ce que les données disent',           intent: 'Étude'        }
    ],
    phase3: [
      { titre: 'Audit performance WordPress : les 10 points à vérifier',               intent: 'Décisionnelle' },
      { titre: 'Pack performance WordPress recommandé par schoolsWP',                  intent: 'Décisionnelle' },
      { titre: 'Hébergement WordPress : ce que je recommande pour chaque budget',      intent: 'Décisionnelle' }
    ],
    affilies: ['WP Rocket — ~30€/vente', 'Kinsta — ~50-200€ selon plan'],
    lead_magnet: '"Checklist Performance WordPress : 15 points pour booster vos conversions"',
    formation_future: '"WordPress Rapide : optimisation complète de A à Z" (formation)',
    kpi_seo: [
      'Pilier en position 1-5 sur "performance WordPress"',
      'Comparatifs hébergement en position 1-3 SERP francophone'
    ],
    kpi_llm: [
      'Cité sur "performance WordPress business" dans les IA',
      'Blocs "Réponse rapide" performance indexés en AI Overview'
    ],
    kpi_biz: [
      'Revenus affiliés hébergement > 300€/mois en fin de Q3',
      'Checklist : 120+ téléchargements/mois'
    ]
  }
};

// ─── Validation ───────────────────────────────────────────────────────────────

if (!NICHES[NICHE]) {
  console.error(`❌  Niche inconnue : "${NICHE}"`);
  console.error('    Niches disponibles : crm · lms · automatisation · consultant · performance');
  process.exit(1);
}

const N = NICHES[NICHE];

// ─── API helpers ──────────────────────────────────────────────────────────────

async function notion(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1/${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json'
    },
    body: body ? JSON.stringify(body) : undefined
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`${method} /${endpoint} → ${resp.status}: ${err.message || JSON.stringify(err)}`);
  }
  return resp.json();
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// ─── Block helpers ────────────────────────────────────────────────────────────

const rt  = (t) => [{ type: 'text', text: { content: t } }];
const h1  = (t) => ({ type: 'heading_1', heading_1: { rich_text: rt(t) } });
const h2  = (t) => ({ type: 'heading_2', heading_2: { rich_text: rt(t) } });
const h3  = (t) => ({ type: 'heading_3', heading_3: { rich_text: rt(t) } });
const p   = (t = '') => ({ type: 'paragraph', paragraph: { rich_text: t ? rt(t) : [] } });
const bul = (t) => ({ type: 'bulleted_list_item', bulleted_list_item: { rich_text: rt(t) } });
const tod = (t) => ({ type: 'to_do', to_do: { rich_text: rt(t), checked: false } });
const div = () => ({ type: 'divider', divider: {} });
const qot = (t) => ({ type: 'quote', quote: { rich_text: rt(t) } });
const cal = (text, emoji = '💡', color = 'gray_background') => ({
  type: 'callout',
  callout: { rich_text: rt(text), icon: { type: 'emoji', emoji }, color }
});

function stars(n, max = 5) {
  return '★'.repeat(n) + '☆'.repeat(max - n);
}

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];

  // ── HEADER ──────────────────────────────────────────────────────────────────
  blocks.push(cal(
    `NICHE    : ${N.nom}\n` +
    `ANGLE    : ${N.angle}\n` +
    `PLUGIN   : ${N.plugin_principal}\n` +
    `SCORE    : ${N.scoring.total}/25  →  ${N.verdict}`,
    N.emoji, 'purple_background'
  ));
  blocks.push(div());

  // ── SECTION 1 — COMPARATIF 5 NICHES ─────────────────────────────────────────
  blocks.push(h1('📊 1 — COMPARATIF DES 5 NICHES CANDIDATES'));
  blocks.push(p('Évaluation : Expertise réelle · Potentiel affilié · Spécificité · Concurrence atteignable · Cohérence schoolsWP  (chacun /5)'));
  blocks.push(p(''));

  for (const [key, nc] of Object.entries(NICHES)) {
    const isSelected = key === NICHE;
    const scoreBar   = stars(Math.round(nc.scoring.total / 5));
    const line =
      `${nc.emoji}  ${nc.nom}  [${nc.scoring.total}/25  ${scoreBar}]\n` +
      `   Angle : ${nc.angle}\n` +
      `   Expertise: ${stars(nc.scoring.expertise)}  Affilié: ${stars(nc.scoring.affilie)}  Spécificité: ${stars(nc.scoring.specificite)}  Concurrence: ${stars(nc.scoring.concurrence)}  Cohérence: ${stars(nc.scoring.coherence)}\n` +
      `   → ${nc.verdict}`;
    blocks.push(cal(line, isSelected ? '✅' : '○', isSelected ? 'green_background' : 'gray_background'));
  }

  blocks.push(div());

  // ── SECTION 2 — NICHE CHOISIE ────────────────────────────────────────────────
  blocks.push(h1(`🎯 2 — NICHE CHOISIE : ${N.nom.toUpperCase()}`));
  blocks.push(cal(
    `Niche          : ${N.nom}\n` +
    `Angle          : ${N.angle}\n` +
    `Différenciation: ${N.differentiation}\n` +
    `Plugin pivot   : ${N.plugin_principal}`,
    N.emoji, 'yellow_background'
  ));
  blocks.push(bul(`Lead magnet cible : ${N.lead_magnet}`));
  blocks.push(bul(`Formation future  : ${N.formation_future}`));
  blocks.push(p(''));
  blocks.push(qot(
    'Règle schoolsWP : chaque article doit servir soit l\'affilié, soit le lead magnet, soit les deux. ' +
    'Si le sujet ne mène à aucun des deux → le déprioritiser.'
  ));
  blocks.push(div());

  // ── SECTION 3 — STRUCTURE DE DOMINATION ─────────────────────────────────────
  blocks.push(h1('🧱 3 — STRUCTURE DE DOMINATION (12 articles)'));

  // Phase 0 — Pilier
  blocks.push(h2('PHASE 0 — Pilier (Semaines 1-2)'));
  blocks.push(cal(
    `Pilier : "${N.pilier.titre}"\n` +
    `Keyword : ${N.pilier.keyword}\n` +
    `Intent  : ${N.pilier.intent}\n` +
    `Format  : Guide complet 4000-6000 mots · Tableaux · FAQ · Blocs LLM`,
    '🏛️', 'blue_background'
  ));
  blocks.push(tod(`Créer le pilier : "${N.pilier.titre}"`));
  blocks.push(tod(`Ajouter dans le cluster "${N.nom}" dans Notion`));
  blocks.push(tod('Configurer blocs "Réponse rapide" + FAQ + maillage (≥ 3 liens sortants)'));
  blocks.push(tod('Ajouter CTA affilié structuré + lien lead magnet en fin d\'article'));
  blocks.push(p(''));

  // Phase 1 — Satellites
  blocks.push(h2('PHASE 1 — Satellites (Mois 1 · 6 articles)'));
  blocks.push(cal(
    '6 satellites qui renforcent le pilier et ciblent des requêtes complémentaires.\n' +
    'Chaque satellite : ≥ 2 liens vers le pilier + 1 lien vers un autre satellite.',
    '📡', 'gray_background'
  ));
  N.phase1.forEach((a, i) => {
    blocks.push(tod(`S${i + 1} [${a.intent}] — ${a.titre}`));
  });
  blocks.push(p(''));

  // Phase 2 — Comparatifs
  blocks.push(h2('PHASE 2 — Comparatifs décisionnels (Mois 2 · 3 articles)'));
  blocks.push(cal(
    'Comparatifs à fort intent décisionnel → trafic qualifié + taux clic affilié élevé.\n' +
    'Format : tableau comparatif + verdict clair + CTA affilié principal.',
    '⚖️', 'orange_background'
  ));
  N.phase2.forEach((a, i) => {
    blocks.push(tod(`C${i + 1} [${a.intent}] — ${a.titre}`));
  });
  blocks.push(p(''));

  // Phase 3 — Transactionnels
  blocks.push(h2('PHASE 3 — Contenus transactionnels (Mois 3 · 3 articles)'));
  blocks.push(cal(
    'Articles avec intent d\'achat fort → priorité absolue sur les CTA affiliés.\n' +
    'Format : avis honnête + tableaux + "ce que je recommande vraiment".',
    '💰', 'green_background'
  ));
  N.phase3.forEach((a, i) => {
    blocks.push(tod(`T${i + 1} [${a.intent}] — ${a.titre}`));
  });
  blocks.push(div());

  // ── SECTION 4 — PLAN 90 JOURS ────────────────────────────────────────────────
  blocks.push(h1('🗓 4 — PLAN 90 JOURS'));

  // Mois 1
  blocks.push(h2('🧱 Mois 1 — Fondations'));
  blocks.push(cal(
    `Focus : Pilier + 3 premiers satellites + maillage de base.\n` +
    `KPI fin Mois 1 : Pilier indexé + 3 satellites publiés + cluster créé dans Notion.`,
    '🧱', 'gray_background'
  ));
  blocks.push(tod('Semaine 1-2 : Rédiger et publier le Pilier (Phase 0)'));
  blocks.push(tod(`Semaine 2-3 : Satellite 1 — ${N.phase1[0]?.titre}`));
  blocks.push(tod(`Semaine 3   : Satellite 2 — ${N.phase1[1]?.titre}`));
  blocks.push(tod(`Semaine 4   : Satellite 3 — ${N.phase1[2]?.titre}`));
  blocks.push(tod('Maillage : vérifier que chaque article pointe vers le Pilier'));
  blocks.push(tod('Créer le cluster dans la base Clusters Notion + relier les 4 articles'));
  blocks.push(p(''));

  // Mois 2
  blocks.push(h2('🚀 Mois 2 — Expansion'));
  blocks.push(cal(
    'Focus : Satellites 4-6 + 3 Comparatifs décisionnels + renforcement maillage.\n' +
    `KPI fin Mois 2 : 9 articles publiés + 2 comparatifs en top 20 SERP.`,
    '🚀', 'blue_background'
  ));
  blocks.push(tod(`Semaine 1 : Satellite 4 — ${N.phase1[3]?.titre}`));
  blocks.push(tod(`Semaine 2 : Satellite 5 — ${N.phase1[4]?.titre}`));
  blocks.push(tod(`Semaine 3 : Satellite 6 — ${N.phase1[5]?.titre}`));
  blocks.push(tod(`Semaine 2-3 : Comparatif 1 — ${N.phase2[0]?.titre}`));
  blocks.push(tod(`Semaine 3-4 : Comparatif 2 — ${N.phase2[1]?.titre}`));
  blocks.push(tod('Maillage : ≥ 3 liens entrants par article du cluster'));
  blocks.push(p(''));

  // Mois 3
  blocks.push(h2('💰 Mois 3 — Optimisation & Revenus'));
  blocks.push(cal(
    'Focus : Contenus transactionnels + optimisation CTA + audit Score Global.\n' +
    'KPI fin Mois 3 : 12 articles publiés + Revenus affiliés > 0 + Score moyen > 80.',
    '💰', 'green_background'
  ));
  blocks.push(tod(`Semaine 1 : Comparatif 3 — ${N.phase2[2]?.titre}`));
  blocks.push(tod(`Semaine 2 : Transactionnel 1 — ${N.phase3[0]?.titre}`));
  blocks.push(tod(`Semaine 3 : Transactionnel 2 — ${N.phase3[1]?.titre}`));
  blocks.push(tod(`Semaine 4 : Transactionnel 3 — ${N.phase3[2]?.titre}`));
  blocks.push(tod('Audit : lancer brain-lite.bat sur les 3 articles les plus visités → optimiser Score < 85'));
  blocks.push(tod('Bilan 90 jours : mettre à jour Score ROI Cluster dans Notion'));
  blocks.push(div());

  // ── SECTION 5 — KPI DOMINATION ───────────────────────────────────────────────
  blocks.push(h1('📈 5 — KPI DE DOMINATION'));

  // SEO
  blocks.push(h2('📊 SEO'));
  N.kpi_seo.forEach(k => blocks.push(tod(k)));
  blocks.push(tod('Position moyenne cluster < 15 en fin de Mois 3'));
  blocks.push(p(''));

  // LLM
  blocks.push(h2('🤖 LLM / AI Visibility'));
  N.kpi_llm.forEach(k => blocks.push(tod(k)));
  blocks.push(tod('Bloc "Réponse rapide" sur le Pilier et les 3 comparatifs'));
  blocks.push(p(''));

  // Business
  blocks.push(h2('💰 Business'));
  N.kpi_biz.forEach(k => blocks.push(tod(k)));
  blocks.push(div());

  // ── SECTION 6 — EFFET BUSINESS ───────────────────────────────────────────────
  blocks.push(h1('💰 6 — EFFET BUSINESS ATTENDU'));
  blocks.push(cal(
    `AFFILIÉS  : ${N.affilies.join(' + ')}\n` +
    `           → Revenus concentrés sur 2 plugins cohérents avec la niche\n\n` +
    `LEAD      : ${N.lead_magnet}\n` +
    `           → Capture email qualifiée sur l'audience cible\n\n` +
    `FORMATION : ${N.formation_future}\n` +
    `           → Monétisation future quand l'audience est suffisante\n\n` +
    `SASU      : Expertise "${N.nom}" clairement positionnée et prouvée\n` +
    `           → Crédibilité pour missions de conseil / formation entreprise`,
    '💡', 'yellow_background'
  ));
  blocks.push(p(''));
  blocks.push(bul(`Google comprend : schoolsWP = autorité sur "${N.nom}"`));
  blocks.push(bul(`Les LLM comprennent : schoolsWP = expert ${N.plugin_principal} + WordPress francophone`));
  blocks.push(bul('L\'audience comprend : schoolsWP = la source de référence, pas juste un blog'));
  blocks.push(p(''));
  blocks.push(qot(
    'Tu publies moins. Tu publies mieux. Tu publies stratégique. ' +
    'Chaque article sert le cluster, le cluster sert l\'autorité, l\'autorité sert le business.'
  ));
  blocks.push(p(''));

  // Footer
  blocks.push(cal(
    `Niche Domination ${N.nom} — schoolsWP\nWordPress. Clair. Structuré. Utile.`,
    N.emoji, 'purple_background'
  ));

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log(`🚀  schoolsWP — Niche Domination : ${N.nom}\n`);
  console.log(`  Angle    : ${N.angle}`);
  console.log(`  Plugin   : ${N.plugin_principal}`);
  console.log(`  Score    : ${N.scoring.total}/25  →  ${N.verdict}\n`);

  const template = buildTemplate();
  const CHUNK    = 90;
  const batch1   = template.slice(0, CHUNK);
  const batch2   = template.slice(CHUNK);

  console.log(`  📄  Création page (${template.length} blocs, ${batch1.length} + ${batch2.length})...`);

  const page = await notion('POST', 'pages', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: N.emoji },
    properties: {
      title: [{ type: 'text', text: { content: `🎯 Niche Domination — ${N.nom}` } }]
    },
    children: batch1
  });
  console.log(`        ✅  Page créée : ${page.id}`);

  if (batch2.length > 0) {
    await sleep(600);
    await notion('PATCH', `blocks/${page.id}/children`, { children: batch2 });
    console.log(`        ✅  Batch 2 ajouté (${batch2.length} blocs)`);
  }

  const pageUrl = page.url || `https://www.notion.so/${page.id.replace(/-/g, '')}`;

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log(`✅  Plan de domination créé !\n`);
  console.log(`  🔗  ${pageUrl}\n`);

  console.log('  📋  Récapitulatif — 12 articles à produire :\n');
  console.log(`  PILIER   : ${N.pilier.titre}`);
  console.log('');
  console.log('  PHASE 1 — Satellites :');
  N.phase1.forEach((a, i) => console.log(`  S${i + 1}. [${a.intent}] ${a.titre}`));
  console.log('');
  console.log('  PHASE 2 — Comparatifs :');
  N.phase2.forEach((a, i) => console.log(`  C${i + 1}. [${a.intent}] ${a.titre}`));
  console.log('');
  console.log('  PHASE 3 — Transactionnels :');
  N.phase3.forEach((a, i) => console.log(`  T${i + 1}. [${a.intent}] ${a.titre}`));

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  💡  Prochaines étapes :\n');
  console.log(`  □  Ouvrir la page dans Notion et valider les 12 titres`);
  console.log(`  □  Ajouter dans la base Articles : statut "Idée" pour les 12`);
  console.log(`  □  Scorer chaque idée via : node scripts/score-idea.js --batch`);
  console.log(`  □  Lancer le Pilier via   : brain-lite.bat --keyword "${N.pilier.keyword}"`);
  console.log(`  □  Créer le cluster "${N.nom}" dans la base Clusters Notion`);
  console.log(`  □  Relier Revenue Engine au cluster : plugin principal = ${N.plugin_principal}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('');

  // Générer toutes les commandes brain-lite
  console.log('  🤖  Commandes brain-lite pour les 12 articles :\n');
  const allArticles = [
    { label: 'PILIER', titre: N.pilier.keyword, intent: 'informationnelle' },
    ...N.phase1.map((a, i) => ({ label: `S${i + 1}`, titre: a.titre.slice(0, 50) + '...', intent: a.intent.toLowerCase() })),
    ...N.phase2.map((a, i) => ({ label: `C${i + 1}`, titre: a.titre.slice(0, 50) + '...', intent: 'comparative' })),
    ...N.phase3.map((a, i) => ({ label: `T${i + 1}`, titre: a.titre.slice(0, 50) + '...', intent: 'décisionnelle' }))
  ];

  allArticles.forEach(a => {
    const intent = a.intent.includes('info') ? 'informationnelle' : a.intent.includes('compar') ? 'comparative' : 'décisionnelle';
    console.log(`  brain-lite.bat --keyword "${a.titre}" --intent ${intent}`);
  });

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
