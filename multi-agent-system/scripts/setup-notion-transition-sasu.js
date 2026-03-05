#!/usr/bin/env node
/**
 * setup-notion-transition-sasu.js — Plan de transition Salarié → SASU
 *
 * Crée dans Notion la page stratégique complète :
 *   "🚀 Transition Salarié → SASU — Plan Stratégique"
 *
 * Contenu :
 *   Vue d'ensemble + signaux de déclenchement GO
 *   Phase 1 — Avant la sortie (0-6 mois) avec checkboxes actionnables
 *   Phase 2 — Structuration SASU
 *   Phase 3 — 90 jours après lancement
 *   Budget de transition (template à remplir)
 *   KPI de transition
 *   Stratégie intelligente (éviter vs viser)
 *   Dashboard de suivi — master checklist
 *
 * Variables :
 *   NOTION_API_KEY          — obligatoire
 *   NOTION_PARENT_PAGE_ID   — page parente (obligatoire)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   node scripts/setup-notion-transition-sasu.js
 *
 * Pré-requis : Node 18+
 */

const API_KEY   = process.env.NOTION_API_KEY;
const PARENT_ID = process.env.NOTION_PARENT_PAGE_ID;

if (!API_KEY || !PARENT_ID) {
  console.error('❌  Variables manquantes : NOTION_API_KEY + NOTION_PARENT_PAGE_ID');
  process.exit(1);
}

// ─── API ──────────────────────────────────────────────────────────────────────

async function notion(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1/${endpoint}`, {
    method,
    headers: {
      Authorization:  `Bearer ${API_KEY}`,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`${method} ${endpoint} → ${resp.status}: ${err.message || JSON.stringify(err)}`);
  }
  return resp.json();
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ─── Blocks ───────────────────────────────────────────────────────────────────

const rt = (txt, opts = {}) => ({ type: 'text', text: { content: txt }, annotations: opts });
const rtb = (txt) => rt(txt, { bold: true });

const h1 = (txt) => ({ object: 'block', type: 'heading_1', heading_1: { rich_text: [rt(txt)] } });
const h2 = (txt) => ({ object: 'block', type: 'heading_2', heading_2: { rich_text: [rt(txt)] } });
const h3 = (txt) => ({ object: 'block', type: 'heading_3', heading_3: { rich_text: [rt(txt)] } });

const p = (txt = '') => ({
  object: 'block', type: 'paragraph',
  paragraph: { rich_text: txt ? [rt(txt)] : [] },
});
const pb = (txt) => ({
  object: 'block', type: 'paragraph',
  paragraph: { rich_text: [rtb(txt)] },
});

const bul = (txt)  => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rt(txt)] } });
const bulb = (txt) => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: [rtb(txt)] } });
const num = (txt)  => ({ object: 'block', type: 'numbered_list_item', numbered_list_item: { rich_text: [rt(txt)] } });

const tod = (txt, checked = false) => ({
  object: 'block', type: 'to_do',
  to_do: { rich_text: [rt(txt)], checked },
});

const div = () => ({ object: 'block', type: 'divider', divider: {} });

const cal = (emoji, txt, color = 'gray_background') => ({
  object: 'block', type: 'callout',
  callout: { icon: { type: 'emoji', emoji }, rich_text: [rt(txt)], color },
});

const qot = (txt) => ({
  object: 'block', type: 'quote',
  quote: { rich_text: [rt(txt)] },
});

const tog = (title, children = []) => ({
  object: 'block', type: 'toggle',
  toggle: { rich_text: [rtb(title)], children },
});

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate() {
  const blocks = [];
  const add    = (...b) => blocks.push(...b);

  // ── En-tête ────────────────────────────────────────────────────────────────
  add(
    cal('🧭', 'Stratégique. Pas émotionnel. Quitter intelligemment. Lancer proprement. Sécuriser le cash.', 'blue_background'),
    p(),
    qot('Tu ne quittes pas ton job. Tu actives un système préparé.'),
    p(),
  );

  // ── Vue d'ensemble ─────────────────────────────────────────────────────────
  add(
    h2('🗺 Vue d\'ensemble — 3 phases'),
    p(),
    bul('Phase 1 — Avant la sortie (0 à 6 mois)  →  Préparer, tester, amorcer'),
    bul('Phase 2 — Structuration SASU             →  Immatriculer, structurer, protéger'),
    bul('Phase 3 — 90 jours après lancement       →  Stabiliser, optimiser, accélérer'),
    p(),
    div(),
  );

  // ── Signaux GO ────────────────────────────────────────────────────────────
  add(
    h2('🟢 Signaux de déclenchement — Quand partir ?'),
    p('Ne pas quitter sur une envie. Quitter sur des faits.'),
    p(),
    cal('✅', 'GO quand les 5 signaux sont verts. Pas avant.', 'green_background'),
    p(),
  );
  add(
    tog('Voir les 5 signaux GO', [
      tod('Signal 1 — Offre vendue au moins 2 fois (validation marché réelle)'),
      tod('Signal 2 — Trésorerie perso ≥ 6 mois de charges couvertes'),
      tod('Signal 3 — Pipeline actif : ≥ 3 prospects qualifiés identifiés'),
      tod('Signal 4 — MRR schoolsWP + récurrences ≥ 300 €/mois (même symbolique)'),
      tod('Signal 5 — Positionnement clair + page offre publiée sur schoolsWP.com'),
      p(),
      cal('⚠️', 'Si 3 signaux seulement → ne pas quitter. Activer le mois 5-6 de préparation.', 'red_background'),
    ]),
    p(),
    div(),
  );

  // ── Phase 1 ────────────────────────────────────────────────────────────────
  add(
    h1('🧱 Phase 1 — Avant la sortie (0 à 6 mois)'),
    p(),
  );

  // 1.1 Clarifier le modèle
  add(
    h2('1.1 Clarifier le modèle cible'),
    p('Sans ça, la transition sera désordonnée.'),
    p(),
    bul('1 offre principale claire — WordPress Learning System™ (CORE ou PREMIUM)'),
    bul('1 positionnement fort — formateurs en ligne sous WordPress'),
    bul('1 cible précise — 3 profils ICP documentés'),
    bul('1 tunnel minimal fonctionnel — page offre + formulaire + CTA Audit'),
    p(),
    cal('🎯', 'Si tu ne peux pas expliquer ton offre en 1 phrase → pas encore prêt à quitter.', 'yellow_background'),
    p(),
    tod('Offre principale définie et documentée dans Notion'),
    tod('Page "WordPress Learning System™" publiée sur schoolsWP.com'),
    tod('Positionnement formateurs visible sur le site et le profil LinkedIn'),
    tod('Tunnel minimal en place (CTA → formulaire → appel découverte)'),
    p(),
  );

  // 1.2 Trésorerie
  add(
    h2('1.2 Sécuriser la trésorerie'),
    p('Tu lances une SASU, pas un pari.'),
    p(),
    cal('💰', 'Objectif minimum : 6 mois de charges perso couvertes + budget outils + marge sécurité.', 'green_background'),
    p(),
  );
  add(
    tog('📊 Budget de transition — Template à remplir', [
      p('Charges perso mensuelles (loyer, courses, abonnements, transports)'),
      p('→  [À remplir] _____ €/mois'),
      p(),
      p('× 6 mois = Cible trésorerie minimum'),
      p('→  [À calculer] _____ €'),
      p(),
      p('Budget outils SASU (Compte pro, compta, assurance RC Pro, logiciel facturation)'),
      p('→  Estimation : 80 – 150 €/mois → 960 – 1 800 €/an'),
      p(),
      p('Budget marketing initial (ads, LinkedIn, lead magnet)'),
      p('→  Estimation : 200 – 500 €/mois les 3 premiers mois'),
      p(),
      p('Budget immatriculation + frais lancement'),
      p('→  Estimation : 300 – 500 € (greffe + capital + éventuellement expert-comptable)'),
      p(),
      p('─────────────────────────────────────'),
      p('TOTAL TRÉSORERIE CIBLE AVANT LANCEMENT'),
      p('→  [À calculer] _____ €  (= 6 mois perso + outils + marketing + frais)'),
      p(),
      cal('💡', 'Règle simple : ne pas quitter avant d\'avoir ce montant disponible sur le compte perso.', 'blue_background'),
    ]),
    p(),
    tod('Calcul charges perso mensuelles effectué'),
    tod('Objectif trésorerie défini et écrit ici : _____ €'),
    tod('Trésorerie cible atteinte ou plan pour l\'atteindre en place'),
    p(),
  );

  // 1.3 Tester le marché
  add(
    h2('1.3 Tester le marché AVANT immatriculation'),
    p('La validation marché passe avant la structure juridique.'),
    p(),
    bul('Objectif : vendre 1 à 3 missions en freelance (déclaré, même en AE si déjà actif)'),
    bul('Mesurer : le pricing tient-il face au marché réel ?'),
    bul('Observer : combien de temps prend vraiment un projet ?'),
    bul('Identifier : où sont les frictions client (onboarding, scope, livrables) ?'),
    p(),
    cal('🧪', 'Si ça ne se vend pas en 3 mois de prospection active → ajuster l\'offre, pas le prix.', 'orange_background'),
    p(),
    tod('Premier entretien de découverte réalisé (même gratuit)'),
    tod('Devis envoyé à au moins 3 prospects'),
    tod('Première mission signée (avant SASU si possible)'),
    tod('Temps réel mesuré sur le premier projet'),
    tod('Pricing validé par 2 clients signés'),
    p(),
  );

  // 1.4 schoolsWP comme levier
  add(
    h2('1.4 Utiliser schoolsWP comme levier d\'acquisition'),
    p('Pendant que tu es encore salarié, schoolsWP prépare le pipeline.'),
    p(),
    bul('Ajouter CTA Audit sur les 10 articles à plus fort trafic formateurs'),
    bul('Créer la page "Diagnostic WordPress Business" (formulaire qualifiant)'),
    bul('Installer un formulaire de contact avec 3 questions de qualification'),
    bul('Commencer à construire la liste email segment "formateurs WordPress"'),
    bul('Publier 2 posts LinkedIn par semaine sur l\'angle "formateurs + WordPress"'),
    p(),
    cal('📈', 'Chaque article publié maintenant = prospect potentiel dans 3 à 6 mois. Semer avant de quitter.', 'blue_background'),
    p(),
    tod('CTA Audit ajouté sur les 10 articles stratégiques'),
    tod('Page "Diagnostic WordPress Business" créée et publiée'),
    tod('Formulaire qualifiant installé (3 questions minimum)'),
    tod('Séquence email "formateurs" démarrée (même 10 contacts)'),
    tod('20 articles cluster formateurs publiés ou planifiés'),
    p(),
    div(),
  );

  // ── Phase 2 ────────────────────────────────────────────────────────────────
  add(
    h1('🏗 Phase 2 — Structuration SASU'),
    p(),
    h2('Pourquoi SASU et pas rester Auto-Entrepreneur ?'),
    p(),
    bul('Plafond AE dépassable dès la 2e ou 3e mission à prix premium'),
    bul('Crédibilité premium (la SASU inspire plus confiance qu\'un AE en B2B)'),
    bul('Structure de croissance (associés, employé plus tard si besoin)'),
    bul('Optimisation fiscale long terme (IS + dividendes vs IR AE)'),
    bul('Séparation claire patrimoine perso / professionnel'),
    p(),
    cal('⚠️', 'La SASU coûte plus cher à gérer qu\'un AE. La valider UNIQUEMENT si CA estimé dépasse 40 000 €/an.', 'yellow_background'),
    p(),
  );

  add(
    h2('Structure recommandée'),
    p(),
    bul('SASU à l\'IS (Impôt sur les Sociétés) — pas IR'),
    bul('Capital : 1 € symbolique ou 1 000 € pour crédibilité'),
    bul('Compte pro séparé dès le premier jour (Shine, Qonto ou banque classique)'),
    bul('Expert-comptable en ligne dès M1 (Indy, Dougs, Comptastart — ~50-80 €/mois)'),
    bul('Assurance RC Pro dès M1 (obligatoire pour facturer en prestation IT)'),
    bul('Logiciel facturation (Zervant, Facture.net ou module comptable de l\'EC)'),
    p(),
  );

  add(
    h2('Rémunération — Règles importantes'),
    p(),
    cal('💡', 'Ne pas se verser un salaire plein dès le mois 1. Construire d\'abord la trésorerie SASU.', 'blue_background'),
    p(),
    bul('Mois 1-3 : salaire minimal (0 ou SMIC partiel) — consolider la trésorerie'),
    bul('Mois 4-6 : ajuster selon le CA réel et les charges sociales supportables'),
    bul('Mois 7+ : salaire cible progressif + dividendes si bénéfices'),
    p(),
    tog('Simulation simplifiée revenus SASU', [
      p('Hypothèse : CA mensuel 5 000 € HT'),
      p(),
      p('Charges sociales président SASU (salaire 2 000 €/mois brut) :'),
      p('→  ~800 € de cotisations patronales + salariales'),
      p(),
      p('Résultat avant IS : 5 000 – 2 800 (salaire brut + charges) – ~500 (frais EC + outils)'),
      p('→  ~1 700 € résultat brut (imposé à l\'IS : 15% jusqu\'à 42 500 € bénéfice)'),
      p(),
      p('Net perçu chaque mois :'),
      p('→  Salaire net main : ~1 600 €'),
      p('→  Dividendes possibles en fin d\'exercice : bénéfice × 70% (après IS 15%)'),
      p(),
      cal('💡', 'À CA 8 000 €/mois le ratio devient très intéressant. Objectif à viser en mois 6.', 'green_background'),
    ]),
    p(),
    tod('Expert-comptable choisi et contacté'),
    tod('Compte pro SASU ouvert'),
    tod('RC Pro souscrite'),
    tod('Numéro SIRET obtenu'),
    tod('Modèle de contrat prestation rédigé (avec EC ou avocat)'),
    tod('Première facture émise'),
    p(),
    div(),
  );

  // ── Phase 3 ────────────────────────────────────────────────────────────────
  add(
    h1('🚀 Phase 3 — 90 jours après lancement'),
    p(),
  );

  add(
    h2('Mois 1 — Poser les fondations'),
    p(),
    num('Signer 2 à 3 clients (dont au moins 1 CORE)'),
    num('Mettre en place le process d\'onboarding (template Notion ou PDF)'),
    num('Créer le template de devis + contrat type'),
    num('Formaliser la méthode en 4 phases (document interne)'),
    num('Documenter chaque projet (temps réel, frictions, livrables)'),
    p(),
    cal('🎯', 'Objectif mois 1 : CA ≥ 3 000 € HT + 1 client en récurrence Maintenance.', 'green_background'),
    p(),
  );

  add(
    h2('Mois 2 — Structurer et capitaliser'),
    p(),
    num('Ajouter l\'offre Maintenance (300 €/mois) dès la fin de chaque projet'),
    num('Transformer le premier client en cas d\'étude anonymisé'),
    num('Publier le cas d\'étude sur schoolsWP.com + LinkedIn'),
    num('Optimiser le pricing si le taux de closing est > 50% (sous-facturation)'),
    num('Tester la proposition PREMIUM sur 2 prospects qualifiés'),
    p(),
    cal('🎯', 'Objectif mois 2 : MRR Maintenance ≥ 600 €/mois + 1 projet PREMIUM signé ou en cours.', 'green_background'),
    p(),
  );

  add(
    h2('Mois 3 — Accélérer et automatiser'),
    p(),
    num('Stabiliser le pipeline : ≥ 3 prospects qualifiés en permanence'),
    num('Automatiser la qualification (formulaire Notion + séquence email)'),
    num('Augmenter le panier moyen (upsell SEO Mensuel ou PREMIUM sur clients actifs)'),
    num('Premier bilan comptable partiel avec l\'EC (ajuster le salaire si CA stable)'),
    num('Décision : recruter un partenaire technique ou rester solo ?'),
    p(),
    cal('🎯', 'Objectif mois 3 : CA ≥ 8 000 €/mois HT · MRR ≥ 900 € · pipeline autonome amorcé.', 'green_background'),
    p(),
    div(),
  );

  // ── KPI ───────────────────────────────────────────────────────────────────
  add(
    h1('📊 KPI de transition'),
    p(),
  );

  const kpis = [
    ['1er client signé avant lancement', 'Oui (signal GO obligatoire)'],
    ['3 clients dans les 90 premiers jours', 'Minimum non négociable'],
    ['Taux de closing sur devis envoyés', '> 25%'],
    ['Panier moyen projet', '≥ 4 000 € HT'],
    ['MRR Maintenance à M3', '≥ 600 €/mois'],
    ['Trésorerie SASU à M3', '≥ 2 mois de charges'],
    ['Stress financier perçu', 'Minimal (trésorerie perso OK)'],
    ['Articles formateurs publiés', '≥ 10 en 90 jours'],
    ['Leads entrants via schoolsWP', '≥ 3 par mois à M3'],
  ];

  kpis.forEach(([kpi, cible]) => {
    add(bul(`${kpi}  →  ${cible}`));
  });

  add(p(), div());

  // ── Stratégie intelligente ─────────────────────────────────────────────────
  add(
    h1('🔥 Stratégie intelligente'),
    p(),
    h2('Ce qu\'on évite absolument'),
    p(),
    bul('❌  Quitter sans pipeline (au moins 3 prospects chauds avant J0)'),
    bul('❌  Lancer sans offre testée (vendre avant d\'immatriculer)'),
    bul('❌  Multiplier les services (1 offre, 2 niveaux maximum)'),
    bul('❌  Sous-facturer pour "ne pas effrayer" (c\'est l\'inverse qui qualifie)'),
    bul('❌  Gérer la comptabilité seul les 6 premiers mois (expert-comptable dès M1)'),
    bul('❌  Compter sur 1 seul gros client (concentration = risque mortel)'),
    p(),
    h2('Ce qu\'on vise'),
    p(),
    bul('✔  Offre claire — 1 offre signature, 2 niveaux max'),
    bul('✔  Système clair — pipeline documenté, onboarding formalisé'),
    bul('✔  Positionnement clair — formateurs WordPress, pas "tous les sites"'),
    bul('✔  Pipeline amorcé — leads entrants avant la sortie'),
    bul('✔  Récurrence active — Maintenance dès le premier client'),
    bul('✔  schoolsWP en levier — contenu qui travaille pendant les missions'),
    p(),
    cal('💡', 'schoolsWP + SASU = double moteur. Le contenu génère des leads pendant que tu livres les projets.', 'green_background'),
    p(),
    div(),
  );

  // ── Dashboard de suivi ─────────────────────────────────────────────────────
  add(
    h1('✅ Dashboard de suivi — Master Checklist'),
    p('Cocher au fur et à mesure. 100% = GO pour la transition.'),
    p(),
    h2('Phase 1 — Fondations (avant la sortie)'),
    p(),
    h3('Modèle et offre'),
    tod('Offre principale définie (WordPress Learning System™)'),
    tod('Positionnement formateurs documenté'),
    tod('Page offre publiée sur schoolsWP.com'),
    tod('Tunnel minimal actif (CTA → formulaire → appel)'),
    p(),
    h3('Trésorerie et sécurité'),
    tod('Charges perso mensuelles calculées'),
    tod('Objectif trésorerie 6 mois défini'),
    tod('Trésorerie cible atteinte'),
    tod('Budget outils SASU provisionné'),
    p(),
    h3('Validation marché'),
    tod('3 entretiens de découverte réalisés'),
    tod('1 devis envoyé à prix cible (pas bradé)'),
    tod('1 mission signée et livrée'),
    tod('Temps réel mesuré sur 1 projet complet'),
    tod('Pricing validé par 2 clients payants'),
    p(),
    h3('Pipeline schoolsWP'),
    tod('CTA Audit sur 10 articles stratégiques'),
    tod('Page "Diagnostic WordPress Business" créée'),
    tod('Formulaire qualifiant installé (3 questions)'),
    tod('5 articles cluster formateurs publiés'),
    tod('Séquence email "formateurs" démarrée'),
    tod('LinkedIn : 2 posts/semaine sur formateurs WordPress'),
    p(),
    h2('Phase 2 — Structuration SASU'),
    p(),
    tod('Expert-comptable choisi et briefé'),
    tod('Compte pro SASU ouvert'),
    tod('RC Pro souscrite'),
    tod('SASU immatriculée (SIRET obtenu)'),
    tod('Contrat prestation type validé'),
    tod('Template devis opérationnel'),
    tod('Logiciel facturation configuré'),
    p(),
    h2('Phase 3 — 90 jours post-lancement'),
    p(),
    tod('1er client SASU signé (J1 → J30)'),
    tod('2e client signé (J1 → J30)'),
    tod('Template onboarding client créé'),
    tod('Méthode 4 phases documentée'),
    tod('1er cas d\'étude anonymisé publié'),
    tod('Offre Maintenance proposée systématiquement'),
    tod('MRR Maintenance ≥ 300 €/mois à M2'),
    tod('MRR Maintenance ≥ 600 €/mois à M3'),
    tod('CA M3 ≥ 8 000 € HT'),
    tod('Pipeline : 3 prospects qualifiés en continu'),
    tod('Bilan M3 avec EC — salaire ajusté'),
    p(),
    div(),
  );

  // ── Message final ─────────────────────────────────────────────────────────
  add(
    cal('🧭', 'La bonne question n\'est pas "quand je quitte ?" mais "qu\'est-ce qui doit être vrai pour que ce soit la décision rationnelle ?"', 'blue_background'),
    p(),
    qot('Quitter intelligemment, c\'est quitter quand le système est prêt — pas quand les émotions débordent.'),
    p(),
  );

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Plan de transition Salarié → SASU\n');

  const template = buildTemplate();
  const batches  = [];
  for (let i = 0; i < template.length; i += CHUNK) {
    batches.push(template.slice(i, i + CHUNK));
  }

  console.log(`  📄  Création page (${template.length} blocs en ${batches.length} batches)...\n`);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '🚀' },
    properties: {
      title: { title: [{ text: { content: '🚀 Transition Salarié → SASU — Plan Stratégique' } }] },
    },
    children: batches[0],
  });

  console.log(`        ✅  Batch 1 créé (${batches[0].length} blocs)`);

  for (let i = 1; i < batches.length; i++) {
    await sleep(600);
    await notion('PATCH', `blocks/${page.id}/children`, { children: batches[i] });
    console.log(`        ✅  Batch ${i + 1} ajouté (${batches[i].length} blocs)`);
  }

  // ── Résumé ────────────────────────────────────────────────────────────────
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Plan de transition activé !\n');
  console.log('  🚀  Page : "🚀 Transition Salarié → SASU — Plan Stratégique"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Structure de la page :');
  console.log('    🟢  5 signaux de déclenchement GO (avec checkboxes)');
  console.log('    🧱  Phase 1 — Avant la sortie : 4 blocs actionnables');
  console.log('    🏗   Phase 2 — Structuration SASU : structure + rémunération');
  console.log('    🚀  Phase 3 — 90 jours : objectifs par mois');
  console.log('    📊  KPI de transition (9 indicateurs)');
  console.log('    🔥  Stratégie intelligente (éviter vs viser)');
  console.log('    ✅  Dashboard master checklist (35 actions cochables)');
  console.log('');
  console.log('  Signaux GO (tous doivent être verts) :');
  console.log('    1.  Offre vendue au moins 2 fois');
  console.log('    2.  Trésorerie perso ≥ 6 mois de charges');
  console.log('    3.  Pipeline : ≥ 3 prospects qualifiés');
  console.log('    4.  MRR schoolsWP ≥ 300 €/mois');
  console.log('    5.  Positionnement + page offre publiés');
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  💡  Première action :');
  console.log('      Ouvrir le Dashboard master checklist et cocher ce qui est déjà fait.');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
