#!/usr/bin/env node
/**
 * setup-notion-pricing.js — Pricing Premium SASU WordPress schoolsWP
 *
 * Phase 1 — Enrichit la base Prospects (si fournie) :
 *   Offre cible · Prix proposé · Prix signé · Récurrence mensuelle · Montant récurrence
 *
 * Phase 2 — Crée la base "💼 Catalogue Offres" et seed les 3 offres + 3 maintenances :
 *   Audit & Blueprint (1 200-2 000€) · System Setup (4 000-7 000€)
 *   Business System Premium (8 000-15 000€) · Maintenances Starter/Expert/Premium
 *
 * Phase 3 — Crée la page "💰 Pricing Premium — SASU WordPress" :
 *   Principes · 3 offres détaillées · Montée en gamme · Récurrence
 *   Processus de vente · KPI · Règles d'or
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   NOTION_PROSPECTS_DB_ID=xxx \     # optionnel — Phase 1
 *   node scripts/setup-notion-pricing.js
 *
 * Pré-requis : Node 18+
 */

const API_KEY      = process.env.NOTION_API_KEY;
const PAGE_ID      = process.env.NOTION_PARENT_PAGE_ID;
const PROSP_DB_ID  = process.env.NOTION_PROSPECTS_DB_ID;   // optionnel

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

// ─── Données seed — les 3 offres ──────────────────────────────────────────────

const OFFRES = [
  {
    nom: '🟢 Audit & Blueprint',
    niveau: 'Audit',
    prix_mini: 1200,
    prix_maxi: 2000,
    duree: '2-5 jours',
    pour_qui: 'Entrepreneurs déjà équipés mais mal structurés — solopreneurs, formateurs, coachs.',
    livrables:
      'Audit technique WordPress · Audit SEO (structure, maillage, vitesse) · ' +
      'Audit automatisation (CRM, séquences, intégrations) · Diagnostic business ' +
      '(conversions, tunnel, CTA) · Roadmap 90 jours priorisée · ' +
      'Recommandations outils et plugins',
    positionnement: 'Diagnostic premium — le client sait exactement où il perd de l\'argent.',
    recurrence: false,
    prix_rec_mini: 0,
    prix_rec_maxi: 0,
    note: 'Porte d\'entrée idéale — 70% des clients Audit passent ensuite au Setup.',
    statut: 'Active'
  },
  {
    nom: '🔵 System Setup',
    niveau: 'Setup',
    prix_mini: 4000,
    prix_maxi: 7000,
    duree: '3-6 semaines',
    pour_qui: 'Freelances, formateurs, coachs voulant structurer leur système WordPress de A à Z.',
    livrables:
      'Architecture WordPress optimisée (thème · structure · performance) · ' +
      'CRM FluentCRM (listes, tags, automatisations de base) · ' +
      'Tunnel simple (capture lead → séquence email → CTA) · ' +
      'Optimisation performances (cache, images, vitesse) · ' +
      'Tracking GA4 + events clés · Formation client 2h (reprise en main)',
    positionnement: 'Transformation système — le client passe d\'un site vitrail à une machine à leads.',
    recurrence: true,
    prix_rec_mini: 300,
    prix_rec_maxi: 600,
    note: 'Cœur de l\'offre SASU — meilleure marge, client idéal, études de cas concrètes.',
    statut: 'Active'
  },
  {
    nom: '🔴 Business System Premium',
    niveau: 'Premium',
    prix_mini: 8000,
    prix_maxi: 15000,
    duree: '6-12 semaines + accompagnement 3 mois',
    pour_qui: 'Clients sérieux — formations en ligne structurées, e-commerce, consultants établis.',
    livrables:
      'Architecture WordPress complète · CRM avancé (FluentCRM + segmentation avancée) · ' +
      'LMS complet (Tutor LMS) OU WooCommerce optimisé · ' +
      'Automatisation multi-niveaux (n8n + FluentCRM + webhooks) · ' +
      'SEO technique complet · Tunnel avancé (upsell, sequences, lead scoring) · ' +
      'Dashboard KPI (GSC + Notion + rapport mensuel) · ' +
      'Accompagnement stratégique 3 mois (appels bi-mensuels + Slack)',
    positionnement: 'Infrastructure business — le client paie pour un système qui tourne sans lui.',
    recurrence: true,
    prix_rec_mini: 600,
    prix_rec_maxi: 900,
    note: 'Offre flagship — 1 client/trimestre suffit. Génère les meilleures études de cas.',
    statut: 'Active'
  },
  {
    nom: '🔧 Maintenance Starter',
    niveau: 'Maintenance',
    prix_mini: 300,
    prix_maxi: 300,
    duree: 'Mensuel',
    pour_qui: 'Clients Setup ou Premium voulant déléguer la maintenance de base.',
    livrables:
      'Mises à jour WordPress, thème et plugins · Surveillance sécurité · ' +
      'Backup mensuel vérifié · 1h support technique/mois',
    positionnement: 'Tranquillité d\'esprit — le client ne touche plus à la technique.',
    recurrence: true,
    prix_rec_mini: 300,
    prix_rec_maxi: 300,
    note: 'Récurrence pure — 10 clients = 3000€/mois de base fixe.',
    statut: 'Active'
  },
  {
    nom: '🔧 Maintenance Expert',
    niveau: 'Maintenance',
    prix_mini: 600,
    prix_maxi: 600,
    duree: 'Mensuel',
    pour_qui: 'Clients voulant optimisation continue en plus de la maintenance.',
    livrables:
      'Tout Starter + Optimisation performance mensuelle · ' +
      'Rapport mensuel (trafic, conversions, leads) · ' +
      '2h support + consulting/mois · Veille technique et sécurité',
    positionnement: 'Partenaire mensuel — le client a un expert WordPress à disposition.',
    recurrence: true,
    prix_rec_mini: 600,
    prix_rec_maxi: 600,
    note: 'Cible : clients Premium qui ont goûté à la qualité.',
    statut: 'Active'
  },
  {
    nom: '📈 SEO Mensuel',
    niveau: 'SEO',
    prix_mini: 500,
    prix_maxi: 900,
    duree: 'Mensuel',
    pour_qui: 'Clients voulant croître en trafic organique mois après mois.',
    livrables:
      '2-4 articles SEO optimisés (méthode schoolsWP) · ' +
      'Optimisation technique SEO · Rapport position + trafic · ' +
      'Stratégie cluster et maillage interne · Score ROI contenu',
    positionnement: 'Machine à leads organique — chaque mois, plus de trafic qualifié.',
    recurrence: true,
    prix_rec_mini: 500,
    prix_rec_maxi: 900,
    note: 'Levier différenciant — très peu d\'agences WordPress proposent du SEO contenu.',
    statut: 'Active'
  }
];

// ─── Block helpers ────────────────────────────────────────────────────────────

const rt  = (t) => [{ type: 'text', text: { content: t } }];
const h1  = (t) => ({ type: 'heading_1', heading_1: { rich_text: rt(t) } });
const h2  = (t) => ({ type: 'heading_2', heading_2: { rich_text: rt(t) } });
const p   = (t = '') => ({ type: 'paragraph', paragraph: { rich_text: t ? rt(t) : [] } });
const bul = (t) => ({ type: 'bulleted_list_item', bulleted_list_item: { rich_text: rt(t) } });
const tod = (t) => ({ type: 'to_do', to_do: { rich_text: rt(t), checked: false } });
const div = () => ({ type: 'divider', divider: {} });
const qot = (t) => ({ type: 'quote', quote: { rich_text: rt(t) } });
const cal = (text, emoji = '💡', color = 'gray_background') => ({
  type: 'callout',
  callout: { rich_text: rt(text), icon: { type: 'emoji', emoji }, color }
});

// ─── Template page Pricing ────────────────────────────────────────────────────

function buildPricingPage() {
  const blocks = [];

  // HEADER
  blocks.push(cal(
    'PRICING PREMIUM — SASU WordPress schoolsWP\n\n' +
    'Principe : "Ne jamais vendre du temps. Toujours vendre une transformation mesurable."\n\n' +
    '3 offres packagées · Positionnement résultat business · Récurrence systématique',
    '💰', 'purple_background'
  ));
  blocks.push(div());

  // ── SECTION 1 — PRINCIPES ────────────────────────────────────────────────────
  blocks.push(h1('💡 1 — PRINCIPES PRICING'));
  blocks.push(cal(
    '❌  À éviter absolument :\n' +
    '    Tarif journalier ("je suis à 600€/jour") · "Site vitrine 1500€"\n' +
    '    Devis sur mesure flou · Empilement de prestations sans cap\n' +
    '    Négociation sur le prix sans négociation sur le scope',
    '❌', 'red_background'
  ));
  blocks.push(cal(
    '✅  À viser systématiquement :\n' +
    '    Offre packagée avec livrables précis · Positionnement transformation\n' +
    '    Résultat business promis · 3 niveaux maximum · Récurrence systématique',
    '✅', 'green_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Logique de prix'));
  blocks.push(cal(
    'Ton prix reflète :\n' +
    '  · Impact business client (combien ce système peut lui rapporter)\n' +
    '  · Complexité système (nombre de composants + intégrations)\n' +
    '  · Expertise rare (WordPress + SEO + CRM + Automatisation = profil unique)\n' +
    '  · Gain long terme (un système qui tourne 3 ans sans refaire)',
    '🧠', 'blue_background'
  ));
  blocks.push(p(''));
  blocks.push(qot(
    '"Si ton offre est claire, le prix paraît logique. Si ton offre est floue, le prix paraît cher." ' +
    '— Règle d\'or schoolsWP Agency'
  ));
  blocks.push(div());

  // ── SECTION 2 — LES 3 OFFRES ─────────────────────────────────────────────────
  blocks.push(h1('🏗 2 — LES 3 OFFRES'));

  // Offre 1
  blocks.push(h2('🟢 OFFRE 1 — Audit & Blueprint   |   1 200 – 2 000 €'));
  blocks.push(cal(
    'Pour qui : Entrepreneurs déjà équipés mais mal structurés.\n' +
    '           Ils ont un site, un CRM peut-être, mais ça ne convertit pas.\n\n' +
    'Ce qu\'ils achètent : La clarté — comprendre exactement ce qui bloque et le plan pour corriger.\n\n' +
    'Livrables :\n' +
    '  □ Audit technique WordPress (thème, plugins, performance, sécurité)\n' +
    '  □ Audit SEO (structure, maillage, vitesse, opportunités)\n' +
    '  □ Audit automatisation (CRM, séquences, intégrations)\n' +
    '  □ Diagnostic business (tunnel, CTA, taux de conversion)\n' +
    '  □ Roadmap 90 jours priorisée (ce qui rapporte le plus vite)\n' +
    '  □ Recommandations plugins + stack optimale\n\n' +
    'Prix : 1 200€ (simple) → 2 000€ (système complexe ou urgence)\n' +
    'Durée livraison : 2-5 jours\n\n' +
    'Positionnement : Diagnostic premium — ce n\'est pas un audit technique banal.\n' +
    '                 C\'est un plan stratégique pour transformer le site en machine business.',
    '🟢', 'green_background'
  ));
  blocks.push(bul('Porte d\'entrée naturelle : faible friction, valeur immédiate'));
  blocks.push(bul('70% des clients Audit deviennent clients Setup → Valeur pipeline'));
  blocks.push(bul('Peut être revendu à distance (appel 1h + livrable PDF/Notion) → très haute marge'));
  blocks.push(p(''));

  // Offre 2
  blocks.push(h2('🔵 OFFRE 2 — System Setup   |   4 000 – 7 000 €'));
  blocks.push(cal(
    'Pour qui : Freelances, formateurs, coachs voulant structurer leur système de A à Z.\n' +
    '           Ils ont une activité qui tourne mais perdent des leads et du temps chaque semaine.\n\n' +
    'Ce qu\'ils achètent : Un système qui capte, nurture et convertit sans intervention manuelle.\n\n' +
    'Livrables :\n' +
    '  □ Architecture WordPress optimisée (thème léger, structure SEO, performance)\n' +
    '  □ CRM FluentCRM (listes, tags, séquences automatisées)\n' +
    '  □ Tunnel simple (landing → capture → séquence email → CTA)\n' +
    '  □ Optimisation performances (cache, images, Core Web Vitals)\n' +
    '  □ Tracking GA4 + événements conversions\n' +
    '  □ Formation client 2h (le client reprend le système en main)\n\n' +
    'Prix : 4 000€ (périmètre standard) → 7 000€ (CRM avancé ou e-commerce)\n' +
    'Durée : 3-6 semaines\n\n' +
    'Positionnement : Transformation système — le client passe d\'un site vitrine à une machine à leads.',
    '🔵', 'blue_background'
  ));
  blocks.push(bul('Cœur de l\'offre SASU — meilleure marge, client idéal, études de cas concrètes'));
  blocks.push(bul('Option maintenance Starter (300€/mois) à proposer systématiquement à la signature'));
  blocks.push(bul('Simulateur de prix : node scripts/pricing-simulator.js'));
  blocks.push(p(''));

  // Offre 3
  blocks.push(h2('🔴 OFFRE 3 — Business System Premium   |   8 000 – 15 000 €+'));
  blocks.push(cal(
    'Pour qui : Clients sérieux — formations en ligne établies, e-commerce actif, consultants.\n' +
    '           Ils ont des revenus existants et veulent structurer pour scaler.\n\n' +
    'Ce qu\'ils achètent : Une infrastructure business qui tourne sans eux.\n\n' +
    'Livrables :\n' +
    '  □ Architecture WordPress complète (thème sur mesure ou avancé, structure claire)\n' +
    '  □ CRM avancé (FluentCRM — segmentation, lead scoring, automations complexes)\n' +
    '  □ LMS complet (Tutor LMS) OU WooCommerce optimisé selon l\'activité\n' +
    '  □ Automatisation multi-niveaux (n8n + FluentCRM + webhooks)\n' +
    '  □ SEO technique complet (schema, maillage, performances, audits)\n' +
    '  □ Tunnel avancé (upsell, downsell, séquences, lead scoring)\n' +
    '  □ Dashboard KPI (GSC + Notion + rapport mensuel)\n' +
    '  □ Accompagnement stratégique 3 mois (appels bi-mensuels + support Slack)\n\n' +
    'Prix : 8 000€ (périmètre défini) → 15 000€+ (infrastructure complète)\n' +
    'Durée : 6-12 semaines + 3 mois accompagnement\n\n' +
    'Positionnement : Infrastructure business — le client achète 3 ans de fonctionnement fluide.',
    '🔴', 'red_background'
  ));
  blocks.push(bul('Offre flagship — 1 client/trimestre suffit à couvrir le CA cible'));
  blocks.push(bul('Génère les meilleures études de cas → alimente schoolsWP et la réputation'));
  blocks.push(bul('Option maintenance Expert (600€/mois) + SEO mensuel (500-900€/mois) → très forte LTV'));
  blocks.push(div());

  // ── SECTION 3 — MONTÉE EN GAMME ──────────────────────────────────────────────
  blocks.push(h1('📈 3 — LOGIQUE DE MONTÉE EN GAMME'));
  blocks.push(cal(
    'L\'Audit (1200-2000€)       alimente le Setup\n' +
    '   → 70% de conversion Audit → Setup (la roadmap existe déjà)\n\n' +
    'Le Setup (4000-7000€)      alimente le Premium\n' +
    '   → Le client a vu la qualité, il revient pour aller plus loin\n\n' +
    'Le Premium (8000-15000€)   génère les études de cas\n' +
    '   → Qui alimentent schoolsWP et crédibilisent toutes les offres\n\n' +
    'La Maintenance (300-900€)  stabilise le CA\n' +
    '   → 10 clients maintenance = 3000-9000€/mois de base fixe',
    '📈', 'yellow_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Pitch de montée automatique'));
  blocks.push(bul('Après Audit : "La roadmap est prête. La prochaine étape logique est le Setup. Voilà ce que ça donne."'));
  blocks.push(bul('Après Setup : "Le système est en place. On peut maintenant optimiser en continu — voilà l\'option maintenance."'));
  blocks.push(bul('Après 6 mois maintenance : "Votre site génère des leads. C\'est le bon moment pour un SEO mensuel."'));
  blocks.push(div());

  // ── SECTION 4 — RÉCURRENCE ───────────────────────────────────────────────────
  blocks.push(h1('🔁 4 — OPTIONS RÉCURRENCE (indispensable pour stabilité SASU)'));
  blocks.push(cal(
    'Maintenance Starter   300€/mois   Mises à jour + sécurité + backup + 1h support\n' +
    'Maintenance Expert    600€/mois   Starter + optimisation + rapport mensuel + 2h consulting\n' +
    'SEO Mensuel       500-900€/mois   2-4 articles SEO + optimisations + rapport positions\n\n' +
    'Objectif CA récurrent : 3 000-5 000€/mois (10-15 clients en maintenance)\n' +
    'Ce CA couvre les charges SASU et libère l\'énergie pour les projets setup/premium.',
    '🔁', 'gray_background'
  ));
  blocks.push(p(''));
  blocks.push(tod('Proposer systématiquement la récurrence à chaque signature (Setup + Premium)'));
  blocks.push(tod('Définir clairement le scope maintenance (ce qui est inclus vs hors forfait)'));
  blocks.push(tod('Viser 10 clients maintenance avant de lancer les offres Premium'));
  blocks.push(tod('Tracker le CA récurrent dans Notion (objectif : > 3000€/mois avant lancement SASU)'));
  blocks.push(div());

  // ── SECTION 5 — PROCESSUS VENTE ──────────────────────────────────────────────
  blocks.push(h1('🤝 5 — PROCESSUS DE VENTE (ne jamais improviser)'));
  blocks.push(cal(
    'Étape 1 — Appel découverte (30 min)\n' +
    '  Objectif : comprendre le problème, qualifier le budget, évaluer le fit\n' +
    '  Question clé : "Qu\'est-ce que ce système vous coûte de ne pas avoir aujourd\'hui ?"\n\n' +
    'Étape 2 — Proposition sous 48h\n' +
    '  Format : PDF ou Notion partagé · 3 pages max\n' +
    '  Structure : Problème → Solution → Livrables → Prix → Prochaine étape\n\n' +
    'Étape 3 — Appel proposition (20 min)\n' +
    '  Pas de négociation sur le prix — négocier sur le scope si nécessaire\n' +
    '  "Si le budget est serré, on commence par l\'Audit. C\'est la porte d\'entrée."\n\n' +
    'Étape 4 — Signature + acompte 50%\n' +
    '  Jamais démarrer sans acompte · DocuSign ou Yousign pour les contrats',
    '🤝', 'blue_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Objections fréquentes + réponses'));
  blocks.push(bul('"C\'est cher." → "Par rapport à quoi ? Un système qui génère 3 leads qualifiés par mois se rembourse en 2 clients."'));
  blocks.push(bul('"Je dois réfléchir." → "Bien sûr. Qu\'est-ce qui vous retient concrètement ?" (identifier le vrai blocage)'));
  blocks.push(bul('"Je veux juste un site." → "Je ne crée pas des sites, je structure des systèmes. Ce n\'est pas le même métier."'));
  blocks.push(bul('"J\'ai un devis moins cher ailleurs." → "C\'est possible. Ce que je propose inclut X et Y — est-ce dans leur devis ?"'));
  blocks.push(div());

  // ── SECTION 6 — KPI ──────────────────────────────────────────────────────────
  blocks.push(h1('📊 6 — KPI PRICING À VISER'));
  blocks.push(cal(
    'Panier moyen               >  5 000€  (mix Setup + Premium)\n' +
    'Clients actifs / mois      2-4 max    (ne pas diluer la qualité)\n' +
    'Taux closing (call → sig)  > 25%      (qualifier avant le call)\n' +
    'CA récurrent mensuel       > 3 000€   (10+ clients maintenance)\n' +
    'Marge nette                > 60%      (solopreneur, pas d\'équipe)',
    '📊', 'gray_background'
  ));
  blocks.push(p(''));
  blocks.push(h2('Simulateur de prix'));
  blocks.push(bul('Pour calculer le prix exact d\'un prospect : node scripts/pricing-simulator.js'));
  blocks.push(bul('Intègre le scope, la complexité, l\'urgence et les options récurrence'));
  blocks.push(div());

  // FOOTER
  blocks.push(qot(
    '"Tu ne vends pas un site. Tu vends une architecture WordPress rentable, ' +
    'structurée et automatisée." — schoolsWP Agency'
  ));
  blocks.push(p(''));
  blocks.push(cal(
    'Pricing Premium — schoolsWP / SASU WordPress\nWordPress. Clair. Structuré. Utile.',
    '💰', 'purple_background'
  ));

  return blocks;
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Pricing Premium SASU WordPress\n');

  // ── Phase 1 : Enrichissement Prospects DB ─────────────────────────────────
  if (PROSP_DB_ID) {
    console.log('  📊  Phase 1 — Enrichissement base Prospects...');

    await notion('PATCH', `databases/${PROSP_DB_ID}`, {
      properties: {
        'Offre cible': {
          select: {
            options: [
              { name: '🟢 Audit & Blueprint',       color: 'green'  },
              { name: '🔵 System Setup',             color: 'blue'   },
              { name: '🔴 Business System Premium',  color: 'red'    },
              { name: '🔧 Maintenance',              color: 'gray'   },
              { name: '📈 SEO Mensuel',              color: 'orange' }
            ]
          }
        },
        'Prix proposé':       { number: { format: 'euro' } },
        'Prix signé':         { number: { format: 'euro' } },
        'Récurrence':         { checkbox: {} },
        'Montant récurrence': { number: { format: 'euro' } }
      }
    });

    console.log('        ✅  Offre cible (select 5 niveaux)');
    console.log('        ✅  Prix proposé (€) · Prix signé (€) · Récurrence · Montant récurrence');
    await sleep(500);
  } else {
    console.log('  ⚠️   Phase 1 — NOTION_PROSPECTS_DB_ID non fourni — skip enrichissement Prospects.\n');
  }

  // ── Phase 2 : Catalogue Offres DB ────────────────────────────────────────
  console.log('\n  💼  Phase 2 — Création base "Catalogue Offres"...');

  const catalogueDb = await notion('POST', 'databases', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: '💼' },
    title: [{ type: 'text', text: { content: 'Catalogue Offres — SASU WordPress' } }],
    properties: {
      'Nom offre':      { title: {} },
      'Niveau':         { select: { options: [
        { name: 'Audit',       color: 'green'  },
        { name: 'Setup',       color: 'blue'   },
        { name: 'Premium',     color: 'red'    },
        { name: 'Maintenance', color: 'gray'   },
        { name: 'SEO',         color: 'orange' }
      ]}},
      'Prix mini':      { number: { format: 'euro' } },
      'Prix maxi':      { number: { format: 'euro' } },
      'Durée':          { rich_text: {} },
      'Pour qui':       { rich_text: {} },
      'Livrables':      { rich_text: {} },
      'Positionnement': { rich_text: {} },
      'Récurrence':     { checkbox: {} },
      'Récurrence mini':{ number: { format: 'euro' } },
      'Récurrence maxi':{ number: { format: 'euro' } },
      'Note interne':   { rich_text: {} },
      'Statut':         { select: { options: [
        { name: 'Active',   color: 'green'  },
        { name: 'Test',     color: 'yellow' },
        { name: 'Archive',  color: 'gray'   }
      ]}}
    }
  });

  const CAT_DB_ID = catalogueDb.id;
  console.log(`        ✅  Base "Catalogue Offres" créée : ${CAT_DB_ID}`);
  await sleep(500);

  // Seed
  for (const offre of OFFRES) {
    await notion('POST', 'pages', {
      parent: { type: 'database_id', database_id: CAT_DB_ID },
      icon: { type: 'emoji', emoji: offre.niveau === 'Audit' ? '🟢' : offre.niveau === 'Setup' ? '🔵' : offre.niveau === 'Premium' ? '🔴' : offre.niveau === 'SEO' ? '📈' : '🔧' },
      properties: {
        'Nom offre':       { title: [{ type: 'text', text: { content: offre.nom } }] },
        'Niveau':          { select: { name: offre.niveau } },
        'Prix mini':       { number: offre.prix_mini },
        'Prix maxi':       { number: offre.prix_maxi },
        'Durée':           { rich_text: [{ type: 'text', text: { content: offre.duree } }] },
        'Pour qui':        { rich_text: [{ type: 'text', text: { content: offre.pour_qui } }] },
        'Livrables':       { rich_text: [{ type: 'text', text: { content: offre.livrables } }] },
        'Positionnement':  { rich_text: [{ type: 'text', text: { content: offre.positionnement } }] },
        'Récurrence':      { checkbox: offre.recurrence },
        'Récurrence mini': { number: offre.prix_rec_mini },
        'Récurrence maxi': { number: offre.prix_rec_maxi },
        'Note interne':    { rich_text: [{ type: 'text', text: { content: offre.note } }] },
        'Statut':          { select: { name: offre.statut } }
      }
    });
    const prixStr = offre.prix_mini === offre.prix_maxi
      ? `${offre.prix_mini}€/mois`
      : `${offre.prix_mini}-${offre.prix_maxi}€`;
    console.log(`        ✅  ${offre.nom.padEnd(36)} ${prixStr}`);
    await sleep(400);
  }

  // ── Phase 3 : Page Pricing ────────────────────────────────────────────────
  console.log('\n  📄  Phase 3 — Création page Pricing Strategy...');

  const template = buildPricingPage();
  const CHUNK    = 90;
  const batch1   = template.slice(0, CHUNK);
  const batch2   = template.slice(CHUNK);

  const page = await notion('POST', 'pages', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: '💰' },
    properties: {
      title: [{ type: 'text', text: { content: '💰 Pricing Premium — SASU WordPress' } }]
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
  const catUrl  = catalogueDb.url || `https://www.notion.so/${CAT_DB_ID.replace(/-/g, '')}`;

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Système Pricing activé !\n');
  console.log(`  💼  Catalogue Offres : ${catUrl}`);
  console.log(`  💰  Page Pricing     : ${pageUrl}\n`);

  console.log('  📋  Récapitulatif des 6 offres créées :\n');
  console.log('  Offre                          Prix          Récurrence');
  console.log('  ─────────────────────────────────────────────────────────────');
  console.log('  🟢 Audit & Blueprint           1 200-2 000€  —');
  console.log('  🔵 System Setup                4 000-7 000€  300-600€/mois');
  console.log('  🔴 Business System Premium    8 000-15 000€  600-900€/mois');
  console.log('  🔧 Maintenance Starter               300€/mois');
  console.log('  🔧 Maintenance Expert                600€/mois');
  console.log('  📈 SEO Mensuel                  500-900€/mois');
  console.log('');
  console.log('  💡  Simulateur de prix : node scripts/pricing-simulator.js');
  console.log('      → Pour chaque prospect, calculer le prix exact en 2 minutes.');
  console.log('');
  console.log('  📌  Variable à sauvegarder :');
  console.log(`      NOTION_CATALOGUE_DB_ID=${CAT_DB_ID}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
