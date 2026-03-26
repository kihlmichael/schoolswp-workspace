#!/usr/bin/env node
/**
 * setup-notion-roadmap.js — Roadmap Content trimestrielle schoolsWP
 *
 * Ce script fait deux choses en séquence :
 *
 *   Phase 1 — Enrichit la base Clusters avec 4 propriétés par trimestre :
 *     Priorité Q[N] · Impact business estimé · Difficulté SEO · ROI potentiel
 *
 *   Phase 2 — Crée la page "🗓 Roadmap Content Q[N] [YEAR]" avec :
 *     Bloc 1 — Vue Stratégique (thème + KPI cibles)
 *     Bloc 2 — Priorités Clusters (instructions vues filtrées)
 *     Bloc 3 — Backlog Stratégique (filtre Articles intent décisionnelle)
 *     Bloc 4 — Plan 90 jours (Mois 1 Fondations / Mois 2 Expansion / Mois 3 Optimisation)
 *     + Weekly Check · Vision Long Terme
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   NOTION_CLUSTERS_DB_ID=xxx \
 *   node scripts/setup-notion-roadmap.js [--quarter Q2] [--year 2026]
 *
 * Options :
 *   --quarter   Q1|Q2|Q3|Q4      (défaut : Q1)
 *   --year      YYYY              (défaut : 2026)
 *   --skip-clusters               Ne pas modifier la base Clusters
 *
 * Pré-requis : Node 18+ (fetch natif), pas de dépendances npm
 */

const API_KEY  = process.env.NOTION_API_KEY;
const PAGE_ID  = process.env.NOTION_PARENT_PAGE_ID;
const CLUST_ID = process.env.NOTION_CLUSTERS_DB_ID;

if (!API_KEY || !PAGE_ID) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY           — obligatoire');
  console.error('    NOTION_PARENT_PAGE_ID    — obligatoire (page parente dans Notion)');
  console.error('    NOTION_CLUSTERS_DB_ID    — optionnel  (pour enrichir la base Clusters)');
  process.exit(1);
}

// ─── CLI args ─────────────────────────────────────────────────────────────────

const args        = process.argv.slice(2);
const getArg      = (flag, def) => { const i = args.indexOf(flag); return i !== -1 && args[i + 1] ? args[i + 1] : def; };
const QUARTER     = getArg('--quarter', 'Q1').toUpperCase();
const YEAR        = getArg('--year', '2026');
const SKIP_CLUST  = args.includes('--skip-clusters');
const Q_NUM       = parseInt(QUARTER.replace('Q', ''), 10) || 1;

// Thèmes stratégiques par défaut — adapter en début de trimestre
const THEMES = {
  Q1: { theme: 'Fondations SEO + Clusters CRM & LMS',   focus: 'Trafic organique + Autorité thématique' },
  Q2: { theme: 'Domination cluster LMS + autorité SEO', focus: 'Position SERP + Maillage cluster'       },
  Q3: { theme: 'Accélération revenus affiliés Fluent',  focus: 'Revenus affiliés + Leads'               },
  Q4: { theme: 'Consolidation + Visibilité LLM',        focus: 'Score Global moyen + Citations LLM'     }
};
const T = THEMES[QUARTER] || THEMES.Q1;

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
const h1  = (t) => ({ type: 'heading_1',          heading_1:          { rich_text: rt(t) } });
const h2  = (t) => ({ type: 'heading_2',          heading_2:          { rich_text: rt(t) } });
const p   = (t = '') => ({ type: 'paragraph',     paragraph:          { rich_text: t ? rt(t) : [] } });
const bul = (t) => ({ type: 'bulleted_list_item', bulleted_list_item: { rich_text: rt(t) } });
const tod = (t) => ({ type: 'to_do',              to_do:              { rich_text: rt(t), checked: false } });
const div = () => ({ type: 'divider',             divider:            {} });
const qot = (t) => ({ type: 'quote',              quote:              { rich_text: rt(t) } });
const cal = (text, emoji = '💡', color = 'gray_background') => ({
  type: 'callout',
  callout: { rich_text: rt(text), icon: { type: 'emoji', emoji }, color }
});

// ─── Template ─────────────────────────────────────────────────────────────────

function buildTemplate(quarter, year, theme) {
  const nextQ = (n) => `Q${(((Q_NUM - 1 + n) % 4) + 1)}`;

  return [

    // ── HEADER ──────────────────────────────────────────────────────────────────
    cal(
      `TRIMESTRE : ${quarter} ${year}\n` +
      `THÈME     : ${theme.theme}\n` +
      `KPI FOCUS : ${theme.focus}\n` +
      `STATUT    : En préparation`,
      '🗓', 'blue_background'
    ),
    div(),

    // ── BLOC 1 — VUE STRATÉGIQUE ──────────────────────────────────────────────
    h1(`🎯 1 — VUE STRATÉGIQUE ${quarter} ${year}`),

    h2('Ambition & Thème'),
    cal(
      `Thème stratégique  : ${theme.theme}\n` +
      `KPI principal      : ${theme.focus}\n` +
      `Objectif chiffré   : à compléter en début de trimestre`,
      '🎯', 'yellow_background'
    ),
    p('Contexte : pourquoi ce thème ce trimestre ? (compléter ici)'),
    p(''),

    h2('📊 KPI Cibles du Trimestre'),
    cal(
      'Trafic organique    →  +25 %  (ou ___ sessions / mois)\n' +
      'Leads opt-in        →  +40 %\n' +
      'Revenus affiliés    →  +30 %  (ou ___€ / mois)\n' +
      'Articles publiés    →  12\n' +
      'Articles optimisés  →  8\n' +
      'Score moyen Global  →  > 85',
      '📊', 'gray_background'
    ),
    p('→ Adapter ces cibles à la situation réelle (GSC + Notion) en début de trimestre.'),
    div(),

    // ── BLOC 2 — PRIORITÉS CLUSTERS ───────────────────────────────────────────
    h1(`🧠 2 — PRIORITÉS CLUSTERS ${quarter}`),
    cal(
      `Vue à créer dans Notion :\n` +
      `  Base : Clusters (linked database view)\n` +
      `  Nom  : "🎯 Clusters prioritaires ${quarter}"\n` +
      `  Filtre    : Priorité ${quarter} = Haute\n` +
      `  Tri       : ROI potentiel DESC  ·  Score ROI Cluster DESC\n` +
      `  Colonnes  : Nom cluster · Priorité ${quarter} · ROI potentiel · Impact business estimé\n` +
      `              Score ROI Cluster · Nombre d'articles · Statut`,
      '🧠', 'purple_background'
    ),

    h2(`Clusters sélectionnés ${quarter}`),
    bul('Cluster 1 : ____________  (à compléter)'),
    bul('Cluster 2 : ____________'),
    bul('Cluster 3 : ____________'),
    p(''),

    h2('Critères de sélection'),
    bul('ROI potentiel élevé → impact business direct sur revenus ou leads'),
    bul('Cluster incomplet (% Complétude = "À renforcer 🔧") → levier de croissance'),
    bul('Mot-clé pilier en position 10-20 → quick win SEO accessible ce trimestre'),
    div(),

    // ── BLOC 3 — BACKLOG STRATÉGIQUE ─────────────────────────────────────────
    h1('📋 3 — BACKLOG STRATÉGIQUE'),
    cal(
      'Vue à créer dans Notion :\n' +
      '  Base      : Articles (linked database view)\n' +
      '  Nom       : "📋 Backlog stratégique"\n' +
      '  Filtres   : Statut = Idée\n' +
      '              ET Intent = Décisionnelle  OU  Comparative\n' +
      '  Tri       : Revenus estimés DESC  ·  Score Opportunité DESC\n' +
      '  Colonnes  : Titre · Cluster · Intent · Score Opportunité · Volume · Revenus estimés',
      '📋', 'orange_background'
    ),

    h2('Articles à produire ce trimestre'),
    tod('Article 1 — pilier ou comparatif décisionnel (cluster __)'),
    tod('Article 2 — satellite Intent Comparative'),
    tod('Article 3 — satellite Intent Décisionnelle'),
    tod('Article 4 — ____________'),
    tod('Article 5 — ____________'),
    p(''),

    h2('Règle de sélection'),
    bul('Intent Décisionnelle / Comparative en priorité → impact direct sur conversions'),
    bul('Score Opportunité élevé → mot-clé accessible à fort volume ce trimestre'),
    bul('Cluster déjà actif → renforcement maillage, pas dispersion thématique'),
    div(),

    // ── BLOC 4 — PLAN 90 JOURS ───────────────────────────────────────────────
    h1('🗓 4 — PLAN D\'EXÉCUTION 90 JOURS'),

    // Mois 1
    h2('🧱 Mois 1 — Fondations'),
    cal(
      'Focus : poser les bases solides du trimestre.\n' +
      '→ 1 pilier renforcé · 3 satellites produits · maillage installé · CTA en place.',
      '🧱', 'gray_background'
    ),
    tod('Confirmer le cluster prioritaire et son article pilier'),
    tod('Créer ou renforcer l\'article pilier du cluster choisi'),
    tod('Produire 3 satellites : 1 Informationnelle + 1 Comparative + 1 Décisionnelle'),
    tod('Optimiser 3 anciens articles avec Score Global < 80'),
    tod('Ajouter CTA structurés sur les 5 articles les plus visités'),
    tod('Vérifier maillage interne : ≥ 2 liens entrants par article du cluster'),
    p(''),

    // Mois 2
    h2('🚀 Mois 2 — Expansion'),
    cal(
      'Focus : scaler le contenu décisionnel et renforcer la visibilité LLM.\n' +
      '→ Comparatifs + articles business + blocs AIO + maillage renforcé.',
      '🚀', 'blue_background'
    ),
    tod('Publier 2 comparatifs décisionnels (format Plugin A vs Plugin B)'),
    tod('Produire 3 articles business (intent Décisionnelle + CTA affilié)'),
    tod('Renforcer maillage interne : chaque pilier ≥ 5 liens entrants'),
    tod('LLM-SEO : ajouter blocs "Réponse rapide" + "Points clés" sur top 5 articles'),
    tod('FAQ AIO/GEO : 1 page pilier avec FAQ structurée + JSON-LD FAQPage'),
    tod('Vérifier sync GSC → Notion opérationnel (chaque lundi)'),
    p(''),

    // Mois 3
    h2('💰 Mois 3 — Optimisation & Revenus'),
    cal(
      'Focus : convertir le trafic acquis, corriger les articles en dessous du seuil.\n' +
      '→ Audit Score < 85 · CTA testés · internal links · bilan ROI cluster.',
      '💰', 'green_background'
    ),
    tod('Audit complet : lister articles Score Global < 85 → plan de correction'),
    tod('Optimisation Conversion : réviser CTA sur 5 articles à fort trafic / faible CTR'),
    tod('Internal linking boost : ≥ 3 liens entrants pour chaque article satellite'),
    tod('Test CTA : itérer texte + placement sur 3 articles clés'),
    tod('Bilan trimestre : mettre à jour Score ROI Cluster dans Notion'),
    tod('Préparer le backlog et les priorités du trimestre suivant'),
    div(),

    // ── WEEKLY CHECK ─────────────────────────────────────────────────────────
    h1('📈 KPI Suivi Hebdo — Weekly Check'),
    cal(
      'Tracker à remplir chaque lundi matin (15 min · source : GSC + Notion).\n' +
      'Si 2 indicateurs sont en rouge 2 semaines de suite → session stratégique d\'urgence (1h).',
      '📈', 'yellow_background'
    ),
    cal(
      'Vue à créer dans Notion :\n' +
      '  Base      : Articles (linked database view)\n' +
      '  Nom       : "📈 Weekly Check"\n' +
      '  Filtres   : Dernière MAJ = Cette semaine (7 jours)  OU  Score Global < 80\n' +
      '  Tri       : Score Global ASC (les plus urgents en premier)\n' +
      '  Colonnes  : Titre · Score Global · Position moyenne · Clics · CTR · Dernière MAJ',
      '📊', 'gray_background'
    ),
    p('Semaine du ___ au ___ :'),
    tod('Nouveaux clics organiques (GSC — 7 derniers jours)             →  ___'),
    tod('Position moyenne du site (GSC — 7 derniers jours)              →  ___'),
    tod('Nombre d\'articles avec Score Global < 80                       →  ___'),
    tod('Articles présents en AI Overview Google cette semaine          →  ___'),
    tod('Revenus affiliés de la semaine (tableau de bord)               →  ___€'),
    p(''),
    qot('Règle : si 2 indicateurs sont en rouge la même semaine → action immédiate.'),
    div(),

    // ── VISION LONG TERME ─────────────────────────────────────────────────────
    h1('🎯 Vision Long Terme schoolsWP'),
    cal(
      'Objectif Annuel — le système cible\n\n' +
      '→ 5 clusters dominants         Score ROI > 80 chacun\n' +
      '→ 50 articles premium          Score Global > 90\n' +
      '→ Score moyen portefeuille     > 90\n' +
      '→ Citations LLM régulières     Perplexity · ChatGPT · Gemini · Claude\n' +
      '→ Système automatisé           génération → scoring → sync GSC → Notion → Discord',
      '🎯', 'green_background'
    ),

    h2('Le système complet'),
    bul('Le SEO sert le business      → chaque article est un actif mesuré'),
    bul('Les clusters servent l\'autorité → maillage + cohérence thématique'),
    bul('Les CTA servent la conversion   → chaque article pointe vers un objectif précis'),
    bul('Les LLM servent la visibilité   → blocs AIO + FAQs structurées + citations IA'),
    bul('Le scoring sert la décision     → écrire ce qui rapporte, optimiser ce qui stagne'),
    p(''),

    h2('Jalons annuels'),
    tod(`${quarter} ${year} : ${theme.theme}`),
    tod(`${nextQ(1)} ${year} : à définir`),
    tod(`${nextQ(2)} ${year} : à définir`),
    tod(`${nextQ(3)} ${year} : à définir`),
    p(''),

    // Footer
    cal(
      `Roadmap ${quarter} ${year} — schoolsWP Content Engine\nWordPress. Clair. Structuré. Utile.`,
      '🧠', 'purple_background'
    )
  ];
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log(`🚀  schoolsWP — Roadmap Content ${QUARTER} ${YEAR}\n`);
  console.log(`  Thème : ${T.theme}`);
  console.log(`  Focus : ${T.focus}\n`);

  // ── Phase 1 : Enrichissement base Clusters ────────────────────────────────
  if (!SKIP_CLUST && CLUST_ID) {
    console.log(`  📊  Phase 1 — Propriétés Clusters pour ${QUARTER}...\n`);

    await notion('PATCH', `databases/${CLUST_ID}`, {
      properties: {
        [`Priorité ${QUARTER}`]: {
          select: {
            options: [
              { name: 'Haute',   color: 'red'    },
              { name: 'Moyenne', color: 'yellow' },
              { name: 'Basse',   color: 'gray'   }
            ]
          }
        },
        'Impact business estimé': {
          select: {
            options: [
              { name: '🔥 Très élevé', color: 'red'    },
              { name: '🟢 Élevé',      color: 'green'  },
              { name: '🟡 Moyen',      color: 'yellow' },
              { name: '⚫ Faible',     color: 'gray'   }
            ]
          }
        },
        'Difficulté SEO': {
          number: { format: 'number' }
        },
        'ROI potentiel': {
          select: {
            options: [
              { name: '🔥 Très élevé', color: 'red'    },
              { name: '🟢 Élevé',      color: 'green'  },
              { name: '🟡 Moyen',      color: 'yellow' },
              { name: '⚫ Faible',     color: 'gray'   }
            ]
          }
        }
      }
    });

    console.log(`        ✅  Priorité ${QUARTER}           (select : Haute / Moyenne / Basse)`);
    console.log('        ✅  Impact business estimé   (select : 4 niveaux)');
    console.log('        ✅  Difficulté SEO           (number : KD 0-100)');
    console.log('        ✅  ROI potentiel            (select : 4 niveaux)');
    await sleep(600);

  } else if (!SKIP_CLUST && !CLUST_ID) {
    console.log('  ⚠️   NOTION_CLUSTERS_DB_ID non fourni — skip enrichissement Clusters');
    console.log('       Relancer avec NOTION_CLUSTERS_DB_ID=xxx pour ajouter les propriétés.\n');
  } else {
    console.log('  ⏭   Phase 1 — enrichissement Clusters ignoré (--skip-clusters).\n');
  }

  // ── Phase 2 : Création page Roadmap ───────────────────────────────────────
  console.log(`\n  📄  Phase 2 — Création page Roadmap ${QUARTER} ${YEAR}...`);

  const template = buildTemplate(QUARTER, YEAR, T);
  const CHUNK    = 95;
  const batch1   = template.slice(0, CHUNK);
  const batch2   = template.slice(CHUNK);

  console.log(`        Blocs : ${template.length} (batch 1: ${batch1.length}${batch2.length > 0 ? ` + batch 2: ${batch2.length}` : ''})`);

  const page = await notion('POST', 'pages', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: '🗓' },
    properties: {
      title: [{ type: 'text', text: { content: `🗓 Roadmap Content ${QUARTER} ${YEAR}` } }]
    },
    children: batch1
  });
  console.log(`        ✅  Page créée : ${page.id}`);

  if (batch2.length > 0) {
    await sleep(500);
    await notion('PATCH', `blocks/${page.id}/children`, { children: batch2 });
    console.log(`        ✅  Batch 2 ajouté (${batch2.length} blocs)`);
  }

  const pageUrl = page.url || `https://www.notion.so/${page.id.replace(/-/g, '')}`;

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log(`✅  Roadmap Content ${QUARTER} ${YEAR} créée !\n`);
  console.log(`  🔗  ${pageUrl}\n`);

  console.log('  📋  3 vues à créer manuellement dans Notion :\n');

  console.log(`  1️⃣  Vue "🎯 Clusters prioritaires ${QUARTER}"`);
  console.log('      Base     : Clusters (linked database view)');
  console.log(`      Filtre   : Priorité ${QUARTER} = Haute`);
  console.log('      Tri      : ROI potentiel DESC  ·  Score ROI Cluster DESC');
  console.log(`      Colonnes : Nom cluster · Priorité ${QUARTER} · ROI potentiel`);
  console.log("               · Impact business estimé · Score ROI Cluster · Nombre d'articles\n");

  console.log('  2️⃣  Vue "📋 Backlog stratégique"');
  console.log('      Base     : Articles (linked database view)');
  console.log('      Filtres  : Statut = Idée  ET  Intent = Décisionnelle OU Comparative');
  console.log('      Tri      : Revenus estimés DESC  ·  Score Opportunité DESC');
  console.log('      Colonnes : Titre · Cluster · Intent · Score Opportunité · Volume · Revenus estimés\n');

  console.log('  3️⃣  Vue "📈 Weekly Check"');
  console.log('      Base     : Articles (linked database view)');
  console.log('      Filtres  : Dernière MAJ = Cette semaine  OU  Score Global < 80');
  console.log('      Tri      : Score Global ASC (urgents en premier)');
  console.log("      Colonnes : Titre · Score Global · Position moyenne · Clics · CTR · Dernière MAJ\n");

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  ✅  Checklist de lancement :\n');
  console.log(`  □  Ouvrir la page Roadmap ${QUARTER} ${YEAR} dans Notion`);
  console.log('  □  Personnaliser thème + objectif chiffré (bloc jaune)');
  if (CLUST_ID) {
    console.log(`  □  Renseigner Priorité ${QUARTER} sur chaque cluster (base Clusters)`);
    console.log('  □  Qualifier Impact business estimé + ROI potentiel par cluster');
  }
  console.log('  □  Créer les 3 vues linked database (voir instructions ci-dessus)');
  console.log('  □  Identifier 5 articles pour le Backlog stratégique');
  console.log('  □  Bloquer 15 min chaque lundi pour le Weekly Check');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
