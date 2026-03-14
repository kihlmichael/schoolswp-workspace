#!/usr/bin/env node
/**
 * setup-notion-offer-signature.js — Offre Signature WordPress Business System
 *
 * Crée dans Notion :
 *   Phase 1 — Ajoute 2 offres dans la base Catalogue Offres (CORE + PREMIUM)
 *   Phase 2 — Crée la page "🎯 Offre Signature — WordPress Business System"
 *              avec positionnement, 4 phases CORE, option Premium, exclusions,
 *              message commercial et KPI.
 *
 * Variables d'environnement :
 *   NOTION_API_KEY          — obligatoire
 *   NOTION_PARENT_PAGE_ID   — page Notion parente (obligatoire pour Phase 2)
 *   NOTION_OFFERS_DB_ID     — base Catalogue Offres (optionnel — Phase 1 ignorée si absent)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   NOTION_OFFERS_DB_ID=xxx \
 *   node scripts/setup-notion-offer-signature.js
 *
 * Pré-requis : Node 18+
 */

const API_KEY       = process.env.NOTION_API_KEY;
const PARENT_ID     = process.env.NOTION_PARENT_PAGE_ID;
const OFFERS_DB_ID  = process.env.NOTION_OFFERS_DB_ID;

if (!API_KEY || !PARENT_ID) {
  console.error('❌  Variables manquantes : NOTION_API_KEY + NOTION_PARENT_PAGE_ID');
  process.exit(1);
}

// ─── API helper ───────────────────────────────────────────────────────────────

async function notion(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1/${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${API_KEY}`,
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

// ─── Block builders ───────────────────────────────────────────────────────────

const rt  = (txt, opts = {}) => ({
  type: 'text',
  text: { content: txt },
  annotations: opts,
});

const h1 = (txt) => ({
  object: 'block', type: 'heading_1',
  heading_1: { rich_text: [rt(txt)] },
});

const h2 = (txt) => ({
  object: 'block', type: 'heading_2',
  heading_2: { rich_text: [rt(txt)] },
});

const h3 = (txt) => ({
  object: 'block', type: 'heading_3',
  heading_3: { rich_text: [rt(txt)] },
});

const p = (txt) => ({
  object: 'block', type: 'paragraph',
  paragraph: { rich_text: txt ? [rt(txt)] : [] },
});

const bul = (txt, bold = false) => ({
  object: 'block', type: 'bulleted_list_item',
  bulleted_list_item: { rich_text: [rt(txt, bold ? { bold: true } : {})] },
});

const div = () => ({
  object: 'block', type: 'divider',
  divider: {},
});

const cal = (emoji, txt, color = 'gray_background') => ({
  object: 'block', type: 'callout',
  callout: {
    icon: { type: 'emoji', emoji },
    rich_text: [rt(txt)],
    color,
  },
});

const qot = (txt) => ({
  object: 'block', type: 'quote',
  quote: { rich_text: [rt(txt)] },
});

const tog = (title, children = []) => ({
  object: 'block', type: 'toggle',
  toggle: {
    rich_text: [rt(title, { bold: true })],
    children,
  },
});

// ─── Offres à seeder ──────────────────────────────────────────────────────────

const NOUVELLES_OFFRES = [
  {
    nom:      '🥇 WordPress Business System — CORE',
    niveau:   'CORE',
    prix_mini: 3000,
    prix_maxi: 6000,
    duree:    '3-5 semaines',
    pour_qui: 'Freelances, formateurs, solopreneurs avec un site existant à structurer',
    livrables:'Audit stratégique · Restructuration stack · CRM configuré · Tunnel intégré · Automatisations · Formation autonomie',
    recurrence: false,
    prix_rec_mini: 0,
    prix_rec_maxi: 0,
  },
  {
    nom:      '🥈 WordPress Business System — PREMIUM',
    niveau:   'PREMIUM',
    prix_mini: 6000,
    prix_maxi: 10000,
    duree:    '6-10 semaines',
    pour_qui: 'Entrepreneurs ambitieux : SEO cluster + LMS ou booking + suivi 3 mois inclus',
    livrables:'CORE complet + SEO avancé · Stratégie contenu cluster · LMS ou booking · Suivi mensuel 3 mois',
    recurrence: true,
    prix_rec_mini: 300,
    prix_rec_maxi: 600,
  },
];

// ─── Template page ─────────────────────────────────────────────────────────────

function buildTemplate() {
  return [

    // ── En-tête ────────────────────────────────────────────────────────────────
    cal('🎯', 'Je ne crée pas des sites. Je structure des systèmes WordPress rentables et automatisés.', 'green_background'),
    p(''),

    h2('🎯 Positionnement'),
    p('Un site WordPress mal structuré coûte de l\'argent chaque mois — en temps perdu, en leads manqués, en bricolage permanent.'),
    p('Le WordPress Business System transforme ton site en système clair, automatisé et rentable.'),
    p('Pas une refonte graphique. Pas un template. Un système fonctionnel aligné sur ton business.'),
    p(''),

    h2('👤 Cible prioritaire'),
    bul('Freelances, formateurs, solopreneurs avec un site existant'),
    bul('Déjà actifs — pas en phase de démarrage'),
    bul('Veulent plus de clarté, d\'automatisation et de rentabilité'),
    bul('En ont assez du bricolage permanent et du support Elementor à 3h du matin'),
    p(''),
    cal('⚠️', 'Ce n\'est PAS pour les porteurs de projet sans site, ni pour les entreprises cherchant une refonte graphique.', 'yellow_background'),
    p(''),

    div(),

    // ── CORE ──────────────────────────────────────────────────────────────────
    h1('🥇 CORE — WordPress Business System'),
    cal('💶', '3 000 € – 6 000 €   ·   3 à 5 semaines   ·   selon complexité', 'blue_background'),
    p(''),

    h3('Phase 1 — Audit stratégique'),
    bul('Analyse architecture WordPress'),
    bul('Analyse tunnel / conversion'),
    bul('Analyse SEO structure'),
    bul('Analyse stack plugins (identifier le superflu)'),
    bul('Analyse automatisation (ce qui manque)'),
    p(''),
    cal('📦', 'Livrable : Rapport stratégique clair · Roadmap priorisée · Gains rapides identifiés', 'gray_background'),
    p(''),

    h3('Phase 2 — Structuration'),
    bul('Simplification stack plugins (supprimer ce qui alourdit)'),
    bul('Architecture pages claire et orientée conversion'),
    bul('CRM configuré (FluentCRM ou équivalent)'),
    bul('Tunnel simple intégré et fonctionnel'),
    bul('Automatisations clés en place'),
    p(''),

    h3('Phase 3 — Optimisation'),
    bul('CTA stratégiques positionnés'),
    bul('Performance technique (Core Web Vitals)'),
    bul('SEO structure (maillage interne, balises)'),
    bul('Email automation minimale viable'),
    p(''),

    h3('Phase 4 — Transmission'),
    bul('Formation enregistrée (vidéo ou Loom)'),
    bul('Documentation simplifiée (PDF ou Notion)'),
    bul('Autonomie client garantie'),
    p(''),

    div(),

    // ── PREMIUM ───────────────────────────────────────────────────────────────
    h1('🥈 PREMIUM — Option avancée'),
    cal('💶', '6 000 € – 10 000 €   ·   6 à 10 semaines   ·   CORE + modules additionnels', 'purple_background'),
    p(''),
    p('Le PREMIUM inclut tout le CORE plus :'),
    p(''),
    bul('Optimisation SEO avancée (audit technique complet, Core Web Vitals)'),
    bul('Stratégie contenu cluster (architecture thématique + piliers)'),
    bul('Intégration booking ou LMS (Tutor LMS, Calendly, ThriveCart…)'),
    bul('3 mois de suivi mensuel (audit mensuel + ajustements)'),
    p(''),
    qot('Le PREMIUM, c\'est pour les entrepreneurs qui veulent l\'accélérateur, pas juste les fondations.'),
    p(''),

    div(),

    // ── Exclusions ────────────────────────────────────────────────────────────
    h2('❌ Ce qu\'on exclut volontairement'),
    cal('🚫', 'Ces demandes ne correspondent pas au positionnement — les refuser clairement protège la valeur de l\'offre.', 'red_background'),
    p(''),
    bul('Création de site vitrine simple (pas de transformation système)'),
    bul('Micro-modifications Elementor (support, pas du conseil)'),
    bul('Dépannage ponctuel (erreur 404, mise à jour plugin)'),
    bul('Refonte graphique seule (changement de couleurs, logo, template)'),
    bul('Projets sans site existant (pas le bon moment pour ce système)'),
    p(''),
    p('On reste sur : Structure + Automatisation + Rentabilité.'),
    p(''),

    div(),

    // ── Message commercial ────────────────────────────────────────────────────
    h2('💬 Message commercial'),
    qot('Votre WordPress doit être un système, pas un empilement de plugins.'),
    p(''),
    p('Axes de conviction :'),
    bul('Tu ne paies pas mon temps. Tu paies la transformation de ton système.'),
    bul('Un système bien structuré travaille quand tu dors. Un empilement de plugins te rappelle à 3h du matin.'),
    bul('L\'audit seul, c\'est la clarté. Le CORE, c\'est la transformation. Le PREMIUM, c\'est l\'accélération.'),
    p(''),

    div(),

    // ── Grille tarifaire ──────────────────────────────────────────────────────
    h2('💰 Grille tarifaire simplifiée'),
    tog('CORE — 3 000 € à 6 000 €', [
      p('Fourchette basse (3 000 €) : site existant, stack simple, peu d\'automatisation'),
      p('Fourchette haute (6 000 €) : CRM + tunnel + automatisations + formation complète'),
      p('Modificateur urgence : +15 à +20%'),
      p('Modificateur complexité technique : +10 à +35%'),
      p('Récurrence optionnelle : Maintenance Starter 300 €/mois'),
    ]),
    p(''),
    tog('PREMIUM — 6 000 € à 10 000 €', [
      p('Fourchette basse (6 000 €) : CORE standard + SEO avancé sans LMS'),
      p('Fourchette haute (10 000 €) : CORE + SEO cluster + LMS + booking + 3 mois suivi'),
      p('Récurrence incluse : Maintenance Expert 600 €/mois conseillé'),
    ]),
    p(''),

    div(),

    // ── Upsell naturel ────────────────────────────────────────────────────────
    h2('📈 Progression naturelle'),
    bul('Audit seul (1 200 €) → démontre l\'expertise → ouverture naturelle CORE'),
    bul('CORE → 3 mois post-livraison → proposition PREMIUM ou Maintenance'),
    bul('Maintenance → suivi SEO → proposition SEO Mensuel'),
    p(''),
    cal('💡', 'Ne jamais vendre directement le PREMIUM à froid — commencer par l\'Audit ou le CORE si le prospect est indécis.', 'blue_background'),
    p(''),

    div(),

    // ── KPI ───────────────────────────────────────────────────────────────────
    h2('📊 Ce que ça crée'),
    bul('Panier moyen élevé (vs missions à 500 €)'),
    bul('Clients plus matures (moins de "c\'est combien juste pour changer la couleur")'),
    bul('Moins de support inutile (le client est formé + documenté)'),
    bul('Positionnement expert clair ("système WordPress" pas "développeur WordPress")'),
    bul('Cohérence totale avec schoolsWP (même vocabulaire, même cible, même angle)'),
    p(''),

    div(),

    // ── Qualification ─────────────────────────────────────────────────────────
    h2('🔍 7 questions de qualification rapide'),
    p('Poser AVANT de proposer une offre :'),
    p(''),
    bul('1. Tu as déjà un site WordPress actif ?'),
    bul('2. Quel est ton problème principal aujourd\'hui (trafic, conversion, automatisation) ?'),
    bul('3. Tu utilises déjà un CRM ou une liste email ?'),
    bul('4. Tu as un produit ou service déjà vendu (ou en cours) ?'),
    bul('5. Quel est ton objectif à 6 mois ? (revenus, clients, visibilité)'),
    bul('6. Tu as un budget estimé pour ce projet ?'),
    bul('7. Tu cherches quelqu\'un pour faire à ta place ou pour te former ?'),
    p(''),
    cal('✅', 'Si 5/7 réponses positives → Score fit ≥ 4 → CORE ou PREMIUM selon périmètre.', 'green_background'),
    p(''),

  ];
}

// ─── Main ──────────────────────────────────────────────────────────────────────

const CHUNK = 90;

async function main() {
  console.log('🚀  schoolsWP — Offre Signature WordPress Business System\n');

  // ── Phase 1 : Ajouter les offres au Catalogue ──────────────────────────────
  if (OFFERS_DB_ID) {
    console.log('  📦  Phase 1 — Ajout offres dans Catalogue Offres...\n');

    for (const offre of NOUVELLES_OFFRES) {
      await notion('POST', 'pages', {
        parent: { database_id: OFFERS_DB_ID },
        properties: {
          'Nom offre':   { title: [{ text: { content: offre.nom } }] },
          'Niveau':      { select: { name: offre.niveau } },
          'Prix mini':   { number: offre.prix_mini },
          'Prix maxi':   { number: offre.prix_maxi },
          'Durée':       { rich_text: [{ text: { content: offre.duree } }] },
          'Pour qui':    { rich_text: [{ text: { content: offre.pour_qui } }] },
          'Livrables':   { rich_text: [{ text: { content: offre.livrables } }] },
          'Récurrence':  { checkbox: offre.recurrence },
          ...(offre.recurrence ? {
            'Prix récurrence mini': { number: offre.prix_rec_mini },
            'Prix récurrence maxi': { number: offre.prix_rec_maxi },
          } : {}),
        },
      });
      console.log(`        ✅  ${offre.nom}  (${offre.prix_mini.toLocaleString('fr-FR')} – ${offre.prix_maxi.toLocaleString('fr-FR')} €)`);
      await sleep(400);
    }

    console.log('');
  } else {
    console.log('  ℹ️   Phase 1 ignorée (NOTION_OFFERS_DB_ID non fourni)\n');
  }

  // ── Phase 2 : Créer la page Offre Signature ────────────────────────────────
  console.log('  📄  Phase 2 — Création page "Offre Signature"...\n');

  const template = buildTemplate();
  const batch1   = template.slice(0, CHUNK);
  const batch2   = template.slice(CHUNK);

  const page = await notion('POST', 'pages', {
    parent: { page_id: PARENT_ID },
    icon:   { type: 'emoji', emoji: '🎯' },
    properties: {
      title: { title: [{ text: { content: '🎯 Offre Signature — WordPress Business System' } }] },
    },
    children: batch1,
  });

  console.log(`        ✅  Page créée (${batch1.length} blocs)`);

  if (batch2.length > 0) {
    await sleep(600);
    await notion('PATCH', `blocks/${page.id}/children`, { children: batch2 });
    console.log(`        ✅  Blocs additionnels ajoutés (${batch2.length} blocs)`);
  }

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Offre Signature activée !\n');
  console.log('  🎯  Page créée : "🎯 Offre Signature — WordPress Business System"');
  if (page.url) console.log(`  🔗  ${page.url}`);
  console.log('');
  console.log('  Structure :');
  console.log('    🥇  CORE       3 000 € – 6 000 €    4 phases · 3-5 semaines');
  console.log('    🥈  PREMIUM    6 000 € – 10 000 €   CORE + SEO avancé + LMS + suivi 3 mois');
  console.log('');
  console.log('  Exclusions documentées :');
  console.log('    ❌  Création site vitrine simple');
  console.log('    ❌  Micro-modifs Elementor');
  console.log('    ❌  Dépannage ponctuel');
  console.log('    ❌  Refonte graphique seule');
  console.log('');
  console.log('  Message commercial :');
  console.log('    "Votre WordPress doit être un système, pas un empilement de plugins."');
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  💡  Prochaine étape :');
  console.log('      node scripts/pricing-simulator.js   Pour calculer le prix exact d\'un prospect');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch((e) => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
