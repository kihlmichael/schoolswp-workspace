#!/usr/bin/env node
/**
 * setup-notion-agency.js — Mode Agency SASU WordPress schoolsWP
 *
 * Phase 1 — Crée la base "🏢 Prospects" (CRM pipeline agency) avec :
 *   17 propriétés  : identité · canal · qualification · statut · valeur
 *   2  formules    : Label Fit · Priorité pipeline
 *
 * Phase 2 — Ajoute à la base Articles (optionnel) :
 *   CTA Agency (checkbox)  — cet article pointe vers le tunnel agency
 *   Type CTA   (select)    — Audit / Diagnostic / Appel
 *
 * Phase 3 — Crée la page "🏢 Mode Agency — Architecture SASU WordPress" :
 *   Positionnement · Offre Signature · Tunnel · KPI · Stratégie contenu
 *   Différenciation · Timeline lancement SASU
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   NOTION_ARTICLES_DB_ID=xxx \     # optionnel — Phase 2
 *   node scripts/setup-notion-agency.js
 *
 * Pré-requis : Node 18+
 */

const API_KEY   = process.env.NOTION_API_KEY;
const PAGE_ID   = process.env.NOTION_PARENT_PAGE_ID;
const ART_DB_ID = process.env.NOTION_ARTICLES_DB_ID;  // optionnel

if (!API_KEY || !PAGE_ID) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY + NOTION_PARENT_PAGE_ID');
  process.exit(1);
}

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
const sel   = (...opts) => ({ select: { options: opts.map(([n, c]) => ({ name: n, color: c })) } });
const fml   = (expr) => ({ formula: { expression: expr } });

// ─── Formules Prospects ───────────────────────────────────────────────────────

// Label Fit — niveau d'adéquation client
const FORMULA_LABEL_FIT =
  'if(prop("Score fit") >= 5, "🔥 Parfait", ' +
    'if(prop("Score fit") >= 4, "🟢 Top Fit", ' +
      'if(prop("Score fit") >= 3, "🟡 Bon Fit", ' +
        'if(prop("Score fit") >= 2, "🟠 Moyen", ' +
          '"⚫ Faible"))))';

// Priorité pipeline — action requise selon statut + fit
const FORMULA_PRIORITE =
  'if(prop("Statut") == "Call planifié", "🎯 Préparer le call", ' +
    'if(prop("Statut") == "Proposition", "📄 Suivi proposition", ' +
      'if(prop("Statut") == "Client", "✅ Client actif", ' +
        'if(prop("Statut") == "Lead" and prop("Score fit") >= 4, "⚡ Contacter urgent", ' +
          'if(prop("Statut") == "Contacté", "📞 Relancer", ' +
            'if(prop("Statut") == "Perdu", "📁 Archivé", "—"))))))';

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

// ─── Page Agency template ────────────────────────────────────────────────────

function buildAgencyPage(prospectsDbId) {
  const blocks = [];

  // HEADER
  blocks.push(cal(
    'MODE AGENCY ACTIVÉ — SASU WordPress\n\n' +
    'Positionnement : "Systèmes WordPress rentables et automatisés"\n' +
    'Cible          : Formateurs · Coachs · Consultants · Solopreneurs\n' +
    'schoolsWP      : Autorité + Acquisition indirecte\n' +
    'SASU           : Monétisation premium + Transformation système',
    '🏢', 'purple_background'
  ));
  blocks.push(div());

  // ── SECTION 1 — POSITIONNEMENT ───────────────────────────────────────────────
  blocks.push(h1('🎯 1 — POSITIONNEMENT SASU'));
  blocks.push(cal(
    'Pas ça   : "Je crée des sites WordPress"\n\n' +
    'Mais ça  : "Je structure un système WordPress qui génère des clients et s\'automatise"\n\n' +
    'Preuve   : schoolsWP — autorité SEO + clusters thématiques + articles décisionnels\n' +
    'Méthode  : Audit → Architecture → Livraison → Formation client\n' +
    'Résultat : Plus de leads, CRM actif, automatisation, clarté business',
    '🎯', 'yellow_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Offre Signature — WordPress Business System'));
  blocks.push(cal(
    'Ce que tu livres (intitulé à affiner) :\n\n' +
    '□  Audit stratégique WordPress (structure, contenu, conversions, technique)\n' +
    '□  Refonte architecture WordPress (thème · structure · performance)\n' +
    '□  CRM + Automatisation (FluentCRM + n8n + séquences email)\n' +
    '□  Tunnel simple (capture lead → séquence → appel ou vente)\n' +
    '□  Optimisation SEO technique (vitesse · maillage · schema)\n' +
    '□  Formation client (le client reprend la main sur son système)',
    '🧠', 'blue_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Tarification (à définir avant lancement)'));
  blocks.push(tod('Définir le panier moyen cible (recommandation : 3 000-6 000€ système complet)'));
  blocks.push(tod('Créer 3 paliers : Audit seul (500€) · Système partiel (2000€) · Système complet (5000€)'));
  blocks.push(tod('Décider : forfait fixe vs retainer mensuel pour la maintenance'));
  blocks.push(tod('Préparer une page de vente "Audit WordPress Business" sur schoolsWP'));
  blocks.push(div());

  // ── SECTION 2 — TUNNEL AGENCY ────────────────────────────────────────────────
  blocks.push(h1('🔄 2 — TUNNEL AGENCY MINIMAL'));
  blocks.push(cal(
    'Étape 1  →  Article SEO décisionnel (schoolsWP)\n' +
    'Étape 2  →  CTA "Audit WordPress Business gratuit"\n' +
    'Étape 3  →  Formulaire de qualification (7 questions)\n' +
    'Étape 4  →  Appel stratégique 30 min (Calendly / Cal.com)\n' +
    'Étape 5  →  Proposition personnalisée → Signature',
    '🔄', 'green_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Articles à CTA fort (Étape 1)'));
  blocks.push(p('Filtrer la vue "💰 Money Focus" dans Notion (Potentiel Conversion ≥ 8) — ces articles reçoivent le CTA en priorité.'));
  blocks.push(tod('Identifier les 5 articles avec le plus fort Potentiel Conversion'));
  blocks.push(tod('Ajouter CTA "Audit WordPress" en fin de chaque article (cocher CTA Agency dans Notion)'));
  blocks.push(tod('Créer la page de destination de l\'audit sur schoolsWP'));
  blocks.push(tod('Configurer Calendly ou Cal.com (durée : 30 min · questions pré-call)'));
  blocks.push(tod('Rédiger le formulaire de qualification (7 questions structurées)'));
  blocks.push(p(''));
  blocks.push(h2('7 Questions de qualification (formulaire)'));
  blocks.push(bul('1. Quel est votre activité principale et comment vous générez des revenus aujourd\'hui ?'));
  blocks.push(bul('2. Quel est votre objectif principal avec votre site WordPress dans les 6 prochains mois ?'));
  blocks.push(bul('3. Quelle est votre frustration principale avec votre système WordPress actuel ?'));
  blocks.push(bul('4. Utilisez-vous un CRM ? Si oui, lequel ? Êtes-vous satisfait ?'));
  blocks.push(bul('5. Combien de leads ou clients entrants générez-vous par mois actuellement ?'));
  blocks.push(bul('6. Quelle est votre budget pour un accompagnement complet (restructuration système) ?'));
  blocks.push(bul('7. Pourquoi schoolsWP plutôt qu\'une agence généraliste ?'));
  blocks.push(div());

  // ── SECTION 3 — RÔLE SCHOOLSWP ───────────────────────────────────────────────
  blocks.push(h1('🧠 3 — RÔLE DE schoolsWP DANS L\'ÉCOSYSTÈME'));
  blocks.push(cal(
    'schoolsWP est :    Vitrine d\'expertise + Machine SEO + Générateur de leads qualifiés\n\n' +
    'Chaque article →   Amène vers l\'audit OU vers le lead magnet\n' +
    'Chaque cluster →   Démontre l\'autorité sur un domaine précis\n' +
    'Chaque score →     Prouve la méthode (scoring, audit, système)\n\n' +
    'La question à poser avant chaque article :\n' +
    '"Ce contenu peut-il amener quelqu\'un à vouloir travailler avec moi ?"',
    '🧠', 'gray_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Contenu orienté acquisition (30-40% du plan)'));
  blocks.push(tod('Article décisionnel : "Comment choisir son CRM WordPress en 2026 (guide honnête)"'));
  blocks.push(tod('Article architecture : "Système WordPress complet pour formateurs : la stack que j\'utilise"'));
  blocks.push(tod('Article audit : "Audit système WordPress : les 10 points qui coûtent des leads"'));
  blocks.push(tod('Article comparatif : "Agence WordPress vs freelance expert : ce que tu dois vraiment savoir"'));
  blocks.push(tod('Article preuve : "Étude de cas : refonte système WordPress pour un coach en ligne"'));
  blocks.push(div());

  // ── SECTION 4 — BASE PROSPECTS ───────────────────────────────────────────────
  blocks.push(h1('🗂 4 — BASE PROSPECTS (CRM PIPELINE)'));
  if (prospectsDbId) {
    blocks.push(cal(
      `Base Prospects créée et configurée ✅\n` +
      `ID : ${prospectsDbId}\n\n` +
      `Vues à créer (voir instructions en bas de page) :\n` +
      `  📊 Pipeline complet (Board par Statut)\n` +
      `  🔥 Top Fit actifs (Score fit ≥ 4 · Statut ≠ Perdu)\n` +
      `  📋 À relancer (Statut = Contacté · sans RDV planifié)`,
      '🗂', 'green_background'
    ));
  } else {
    blocks.push(cal(
      'Base Prospects non créée automatiquement.\n' +
      'Exécuter le script avec NOTION_PARENT_PAGE_ID pour créer la base.',
      '⚠️', 'orange_background'
    ));
  }
  blocks.push(p(''));
  blocks.push(h2('Score Fit — grille de qualification (1-5)'));
  blocks.push(bul('5 — Budget confirmé · Problème clair · Urgence · Secteur cœur schoolsWP'));
  blocks.push(bul('4 — Bon budget · Problème identifié · Prêt à avancer'));
  blocks.push(bul('3 — Budget flou · Intéressé mais pas pressé'));
  blocks.push(bul('2 — Budget insuffisant OU secteur peu aligné'));
  blocks.push(bul('1 — Pas le profil cible · Ne pas poursuivre'));
  blocks.push(div());

  // ── SECTION 5 — KPI AGENCY ───────────────────────────────────────────────────
  blocks.push(h1('📊 5 — KPI AGENCY'));
  blocks.push(cal(
    'Leads qualifiés / mois   →  objectif 5-15\n' +
    'Taux closing              →  objectif > 25%\n' +
    'Panier moyen              →  objectif 3 000-6 000€\n' +
    'Temps projet moyen        →  objectif 3-6 semaines\n' +
    'Marge nette               →  objectif > 60% (solopreneur sans équipe)',
    '📊', 'gray_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Tracker mensuel'));
  blocks.push(tod('Leads reçus ce mois           →  ___'));
  blocks.push(tod('Calls effectués               →  ___'));
  blocks.push(tod('Propositions envoyées         →  ___'));
  blocks.push(tod('Clients signés                →  ___'));
  blocks.push(tod('CA signé (€)                  →  ___'));
  blocks.push(tod('Taux closing (signés/proposes) →  ___%'));
  blocks.push(div());

  // ── SECTION 6 — TIMELINE LANCEMENT ───────────────────────────────────────────
  blocks.push(h1('🗓 6 — TIMELINE LANCEMENT SASU'));

  blocks.push(h2('Phase 1 — 3 mois avant lancement'));
  blocks.push(cal(
    'Focus : poser les fondations business avant d\'annoncer.\n' +
    'Ne pas lancer sans offre claire, page audit et 3 articles décisionnels publiés.',
    '🧱', 'gray_background'
  ));
  blocks.push(tod('Clarifier l\'offre : intitulé exact + livrables précis + délai'));
  blocks.push(tod('Définir le pricing (3 paliers : Audit · Système · Retainer)'));
  blocks.push(tod('Créer la page "Audit WordPress Business" sur schoolsWP'));
  blocks.push(tod('Rédiger et publier 5 articles décisionnels avec CTA'));
  blocks.push(tod('Configurer Calendly + formulaire de qualification'));
  blocks.push(tod('Préparer les démarches SASU (statuts · KBIS · compte pro)'));
  blocks.push(p(''));

  blocks.push(h2('Phase 2 — Lancement'));
  blocks.push(cal(
    'Focus : rendre visible l\'offre et activer le réseau existant.\n' +
    'Objectif : 3 premiers calls dans le premier mois.',
    '🚀', 'blue_background'
  ));
  blocks.push(tod('Annoncer officiellement sur LinkedIn (post + article)'));
  blocks.push(tod('Ajouter le CTA Agency sur 10 articles clés de schoolsWP'));
  blocks.push(tod('Activer le réseau : DM LinkedIn personnalisés × 20 contacts'));
  blocks.push(tod('Lancer le premier appel découverte (Calendly ouvert)'));
  blocks.push(tod('Mettre à jour la bio schoolsWP + page À propos'));
  blocks.push(p(''));

  blocks.push(h2('Phase 3 — Stabilisation (3-6 mois après lancement)'));
  blocks.push(cal(
    'Focus : preuve sociale + optimisation du pipeline + upsell.\n' +
    'Objectif : 2 clients récurrents (maintenance / optimisation).',
    '💰', 'green_background'
  ));
  blocks.push(tod('Rédiger 2 études de cas clients (format article schoolsWP)'));
  blocks.push(tod('Collecter 3 témoignages structurés (avant/après chiffré)'));
  blocks.push(tod('Lancer une offre upsell : maintenance + optimisation mensuelle'));
  blocks.push(tod('Analyser pipeline : taux closing · panier moyen · satisfaction'));
  blocks.push(tod('Mettre à jour les tarifs si la demande dépasse la capacité'));
  blocks.push(div());

  // ── SECTION 7 — DIFFÉRENCIATION ───────────────────────────────────────────────
  blocks.push(h1('💡 7 — DIFFÉRENCIATION FORTE'));
  blocks.push(cal(
    'Tu ne vends pas : "Je crée des sites WordPress"\n\n' +
    'Tu vends        : "Je structure un système WordPress rentable et automatisé\n' +
    '                   qui génère des leads et tourne avec moins de friction"\n\n' +
    'Preuve          : schoolsWP — 100+ articles · autorité SEO · méthode documentée\n' +
    'Méthode         : Audit → Architecture → Livraison → Formation client\n' +
    'Résultat garanti: Un système que le client comprend et peut faire évoluer seul',
    '💡', 'green_background'
  ));
  blocks.push(p(''));
  blocks.push(qot(
    'schoolsWP = Autorité  ·  SASU = Monétisation premium  ·  ' +
    'Contenu = Acquisition  ·  Automatisation = Scalabilité'
  ));
  blocks.push(p(''));

  // FOOTER
  blocks.push(cal(
    'Mode Agency — schoolsWP / SASU WordPress\nWordPress. Clair. Structuré. Utile.',
    '🏢', 'purple_background'
  ));

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Mode Agency SASU WordPress\n');

  // ── Phase 1 : Base Prospects ──────────────────────────────────────────────
  console.log('  🗂   Phase 1 — Création base Prospects (CRM pipeline)...\n');

  const prospectsDb = await notion('POST', 'databases', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: '🏢' },
    title: [{ type: 'text', text: { content: 'Prospects — Pipeline Agency' } }],
    properties: {

      // ── Identité ─────────────────────────────────────────────────────────
      'Nom':              { title: {} },
      'Entreprise':       { rich_text: {} },
      'Email':            { email: {} },
      'Téléphone':        { phone_number: {} },
      'Site actuel':      { url: {} },

      // ── Source & canal ───────────────────────────────────────────────────
      'Source article':   { rich_text: {} },
      'Canal':            sel(['Organique SEO','green'],['LinkedIn','blue'],['Réseau','purple'],['Recommandation','yellow'],['Autre','gray']),
      'Secteur':          sel(['Formation','blue'],['Coaching','green'],['Consulting','orange'],['Freelance','yellow'],['PME','purple'],['E-commerce','red'],['Autre','gray']),

      // ── Qualification ────────────────────────────────────────────────────
      'Niveau maturité':  sel(['Découverte','gray'],['Évaluation','yellow'],['Prêt à acheter','green']),
      'Problème principal': sel(
        ['Pas de CRM','red'],['Site obsolète','orange'],['Manque d\'automatisation','yellow'],
        ['Performance','blue'],['Tunnel absent','purple'],['Positionnement flou','pink'],['Autre','gray']
      ),
      'Budget estimé':    sel(['<500€','gray'],['500-2k€','yellow'],['2-5k€','orange'],['5-10k€','green'],['10k€+','red']),
      'Score fit':        { number: { format: 'number' } },

      // ── Pipeline ─────────────────────────────────────────────────────────
      'Statut':           sel(['Lead','gray'],['Contacté','blue'],['Call planifié','orange'],['Proposition','yellow'],['Client','green'],['Perdu','red']),
      'Date contact':     { date: {} },
      'Date RDV':         { date: {} },
      'Valeur contrat':   { number: { format: 'euro' } },
      'Lien Calendly':    { url: {} },
      'Notes':            { rich_text: {} }
    }
  });

  const PROSPECTS_ID = prospectsDb.id;
  console.log(`        ✅  Base "Prospects" créée : ${PROSPECTS_ID}`);
  console.log('        ✅  17 propriétés configurées');
  await sleep(600);

  // Formules en Phase 1b
  await notion('PATCH', `databases/${PROSPECTS_ID}`, {
    properties: {
      'Label Fit':       fml(FORMULA_LABEL_FIT),
      'Priorité':        fml(FORMULA_PRIORITE)
    }
  });
  console.log('        ✅  Label Fit (🔥/🟢/🟡/🟠/⚫)');
  console.log('        ✅  Priorité pipeline (action contextuelle automatique)');
  await sleep(500);

  // ── Phase 2 : Ajout CTA tracking dans Articles (optionnel) ───────────────
  if (ART_DB_ID) {
    console.log('\n  📝  Phase 2 — Propriétés CTA Agency dans Articles...');

    await notion('PATCH', `databases/${ART_DB_ID}`, {
      properties: {
        'CTA Agency': { checkbox: {} },
        'Type CTA':   sel(['Audit','green'],['Diagnostic','blue'],['Appel stratégique','orange'],['Lead magnet','yellow'])
      }
    });

    console.log('        ✅  CTA Agency (checkbox — cet article pointe vers le tunnel)');
    console.log('        ✅  Type CTA (Audit / Diagnostic / Appel stratégique / Lead magnet)');
    await sleep(500);
  } else {
    console.log('\n  ⚠️   Phase 2 — NOTION_ARTICLES_DB_ID non fourni — skip CTA tracking.');
    console.log('        Relancer avec NOTION_ARTICLES_DB_ID=xxx pour ajouter les propriétés CTA.\n');
  }

  // ── Phase 3 : Page Agency ─────────────────────────────────────────────────
  console.log('\n  📄  Phase 3 — Création page Agency Strategy...');

  const template = buildAgencyPage(PROSPECTS_ID);
  const CHUNK    = 90;
  const batch1   = template.slice(0, CHUNK);
  const batch2   = template.slice(CHUNK);

  console.log(`        Blocs : ${template.length} (batch 1: ${batch1.length}${batch2.length > 0 ? ` + batch 2: ${batch2.length}` : ''})`);

  const page = await notion('POST', 'pages', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: '🏢' },
    properties: {
      title: [{ type: 'text', text: { content: '🏢 Mode Agency — Architecture SASU WordPress' } }]
    },
    children: batch1
  });
  console.log(`        ✅  Page créée : ${page.id}`);

  if (batch2.length > 0) {
    await sleep(600);
    await notion('PATCH', `blocks/${page.id}/children`, { children: batch2 });
    console.log(`        ✅  Batch 2 ajouté (${batch2.length} blocs)`);
  }

  const pageUrl  = page.url  || `https://www.notion.so/${page.id.replace(/-/g, '')}`;
  const prospectsUrl = prospectsDb.url || `https://www.notion.so/${PROSPECTS_ID.replace(/-/g, '')}`;

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Mode Agency activé !\n');
  console.log(`  🏢  Base Prospects  : ${prospectsUrl}`);
  console.log(`  📄  Page Agency     : ${pageUrl}\n`);

  console.log('  📋  3 vues à créer dans la base Prospects :\n');

  console.log('  1️⃣  Vue "📊 Pipeline" (vue principale)');
  console.log('      Type    : Board groupé par Statut');
  console.log('      Tri     : Score fit DESC');
  console.log('      Colonnes: Nom · Entreprise · Label Fit · Budget estimé · Priorité · Date RDV\n');

  console.log('  2️⃣  Vue "🔥 Top Fit actifs"');
  console.log('      Type    : Table');
  console.log('      Filtres : Score fit >= 4  ET  Statut ≠ Perdu  ET  Statut ≠ Client');
  console.log('      Tri     : Score fit DESC · Date contact ASC (les plus anciens d\'abord)\n');

  console.log('  3️⃣  Vue "📞 À relancer"');
  console.log('      Type    : Table');
  console.log('      Filtres : Statut = Contacté  ET  Date RDV = vide');
  console.log('      Tri     : Date contact ASC');
  console.log('      → Prospects contactés sans RDV planifié = à relancer\n');

  if (ART_DB_ID) {
    console.log('  📝  Vue Articles à créer (base Articles) :\n');
    console.log('  4️⃣  Vue "🎯 CTA Agency actifs"');
    console.log('      Type    : Table');
    console.log('      Filtres : CTA Agency = ✓');
    console.log('      Tri     : Potentiel Conversion DESC');
    console.log('      → Suivi des articles du tunnel acquisition\n');
  }

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  🚀  Prochaines étapes :\n');
  console.log('  □  Ouvrir la page Agency et valider le positionnement (Section 1)');
  console.log('  □  Compléter l\'Offre Signature (livrables + délai + prix)');
  console.log('  □  Identifier les 5 articles à CTA Agency (vue Money Focus → Potentiel Conversion ≥ 8)');
  if (ART_DB_ID) {
    console.log('  □  Cocher "CTA Agency" sur ces 5 articles + renseigner "Type CTA"');
  }
  console.log('  □  Créer la page Audit WordPress sur schoolsWP');
  console.log('  □  Configurer Calendly (lien → copier dans Notion SASU section)');
  console.log('  □  Premier prospect testé manuellement dans la base Prospects');
  console.log('');
  console.log('  📌  Variables à sauvegarder :');
  console.log(`      NOTION_PROSPECTS_DB_ID=${PROSPECTS_ID}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
