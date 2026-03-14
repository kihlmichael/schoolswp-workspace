#!/usr/bin/env node
/**
 * setup-notion-template.js — Crée la page template Article schoolsWP dans Notion
 *
 * Usage :
 *   # Créer dans la base Articles (recommandé — puis "Save as template" dans Notion)
 *   NOTION_API_KEY=secret_xxx NOTION_ARTICLES_DB_ID=xxx node scripts/setup-notion-template.js
 *
 *   # Créer comme page standalone (si base Articles pas encore créée)
 *   NOTION_API_KEY=secret_xxx NOTION_PARENT_PAGE_ID=xxx node scripts/setup-notion-template.js
 *
 * Note : l'API Notion limite à 100 blocs par requête.
 *        Ce script découpe automatiquement en 2 appels si nécessaire.
 */

const API_KEY = process.env.NOTION_API_KEY;
const DB_ID   = process.env.NOTION_ARTICLES_DB_ID;
const PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;

if (!API_KEY || (!DB_ID && !PAGE_ID)) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY + NOTION_ARTICLES_DB_ID (ou NOTION_PARENT_PAGE_ID)');
  process.exit(1);
}

// ─── API helper ───────────────────────────────────────────────────────────────

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

// ─── Block helpers ────────────────────────────────────────────────────────────

const rt  = (t) => [{ type: 'text', text: { content: t } }];
const h1  = (t) => ({ type: 'heading_1',          heading_1:          { rich_text: rt(t) } });
const h2  = (t) => ({ type: 'heading_2',          heading_2:          { rich_text: rt(t) } });
const h3  = (t) => ({ type: 'heading_3',          heading_3:          { rich_text: rt(t) } });
const p   = (t='') => ({ type: 'paragraph',       paragraph:          { rich_text: t ? rt(t) : [] } });
const bul = (t) => ({ type: 'bulleted_list_item', bulleted_list_item: { rich_text: rt(t) } });
const num = (t) => ({ type: 'numbered_list_item', numbered_list_item: { rich_text: rt(t) } });
const tod = (t) => ({ type: 'to_do',              to_do:              { rich_text: rt(t), checked: false } });
const div = () =>  ({ type: 'divider',            divider:            {} });
const qot = (t) => ({ type: 'quote',              quote:              { rich_text: rt(t) } });
const cal = (text, emoji = '💡', color = 'gray_background') => ({
  type: 'callout',
  callout: { rich_text: rt(text), icon: { type: 'emoji', emoji }, color }
});

// ─── Template blocks ──────────────────────────────────────────────────────────

const TEMPLATE = [

  // ── HEADER ──────────────────────────────────────────────────────────────────
  cal(
    'MOT-CLÉ :       ____\nINTENT :        informationnelle / comparative / décisionnelle\nCLUSTER :       ____\nTYPE :          Pilier / Satellite / Comparatif / Tutoriel',
    '🏷', 'blue_background'
  ),
  div(),

  // ── SECTION 1 — STRATÉGIE ───────────────────────────────────────────────────
  h1('✍️ 1 — STRATÉGIE'),
  p('🎯 Objectif de l\'article'),
  p('Problème principal :'),
  p('Niveau lecteur :   Débutant / Intermédiaire / Avancé'),
  p('Angle différenciant :'),
  p('Décision que le lecteur doit pouvoir prendre après lecture :'),
  div(),

  // ── SECTION 2 — STRUCTURE SEO ───────────────────────────────────────────────
  h1('🧱 2 — STRUCTURE SEO'),

  h2('H1 — Titre optimisé'),
  p('✏️ Rédiger le titre ici (inclure le mot-clé principal)'),

  h2('H2 — Réponse rapide'),
  cal(
    '📍 Bloc LLM extractible — 3 à 6 lignes claires, sans jargon.\nRépond directement à l\'intention de recherche. Format court.\nIdéal pour AI Overview Google et citations LLM.',
    '📍', 'yellow_background'
  ),
  p('Réponse rapide ici...'),

  h2('H2 — Points clés'),
  bul('Point clé 1 :'),
  bul('Point clé 2 :'),
  bul('Point clé 3 :'),

  h2('H2 — Comprendre le sujet'),
  cal('💡 Explication stratégique — commence par POURQUOI, ensuite seulement COMMENT', '💡', 'gray_background'),
  p('Explication ici...'),

  h2('H2 — Les différentes approches'),
  h3('Option 1 —'),
  p('Description, avantages, cas d\'usage...'),
  h3('Option 2 —'),
  p('Description, avantages, cas d\'usage...'),
  h3('Option 3 —'),
  p('Description, avantages, cas d\'usage...'),

  h2('H2 — Comparaison claire'),
  bul('✅ Avantages :'),
  bul('❌ Limites :'),
  bul('🎯 Quand choisir quoi :'),

  h2('H2 — Recommandation schoolsWP'),
  cal('🎓 Ma recommandation — basée sur ton profil. Pas de réponse générique.', '🎓', 'green_background'),
  p('Profil A (débutant / petit budget) →'),
  p('Profil B (intermédiaire / croissance) →'),
  p('Profil C (avancé / business établi) →'),

  h2('H2 — Erreurs fréquentes'),
  bul('❌ Erreur 1 :'),
  bul('❌ Erreur 2 :'),
  bul('❌ Erreur 3 :'),

  h2('H2 — FAQ SEO'),
  h3('❓ Question 1'),
  p('→ Réponse directe (2-3 phrases max)'),
  h3('❓ Question 2'),
  p('→ Réponse directe (2-3 phrases max)'),
  h3('❓ Question 3'),
  p('→ Réponse directe (2-3 phrases max)'),

  h2('H2 — En résumé'),
  cal('✅ 5 points actionnables — ce que tu dois retenir de cet article', '✅', 'green_background'),
  num('Point 1 :'),
  num('Point 2 :'),
  num('Point 3 :'),
  num('Point 4 :'),
  num('Point 5 :'),
  div(),

  // ── SECTION 3 — CONVERSION LAYER ────────────────────────────────────────────
  h1('💰 3 — CONVERSION LAYER'),
  cal(
    '🎯 CTA Principal\nType : Lead / Affiliation / Autorité / Formation\nTexte CTA :\nURL / Lien :',
    '🎯', 'orange_background'
  ),
  p('🔌 Lien affilié (si applicable) :'),
  qot('⚠️ Mention transparence : Cet article contient des liens affiliés. Je touche une commission si tu passes par mes liens, sans frais supplémentaires pour toi.'),
  div(),

  // ── SECTION 4 — MAILLAGE INTERNE ────────────────────────────────────────────
  h1('🧱 4 — MAILLAGE INTERNE'),
  p('🔁 Liens à intégrer dans le corps de l\'article :'),
  bul('Vers pilier :        [URL + ancre]'),
  bul('Vers satellite 1 :  [URL + ancre]'),
  bul('Vers satellite 2 :  [URL + ancre]'),
  bul('Vers tutoriel lié :  [URL + ancre]'),
  div(),

  // ── SECTION 5 — AUTO-AUDIT ───────────────────────────────────────────────────
  h1('🧠 5 — AUTO-AUDIT'),
  cal(
    'Remplir manuellement ou lancer : node scripts/auto-scorer.js --file article.md\n' +
    'Résultat JSON → copier les scores ci-dessous.',
    '⚙️', 'gray_background'
  ),
  tod('Score SEO :        __ /100'),
  tod('Score LLM :        __ /100'),
  tod('Score Conversion : __ /100'),
  tod('Score Autorité :   __ /100'),
  tod('Score Global :     __ /100  →  ✅ Actif Premium / 🟢 Performant / 🟡 Optimiser / 🔴 Révision'),

  h2('Améliorations avant publication'),
  tod('Amélioration 1 :'),
  tod('Amélioration 2 :'),
  tod('Amélioration 3 :'),

  h2('Checklist publication'),
  tod('Title tag optimisé (mot-clé + valeur)'),
  tod('Meta description < 160 caractères, avec CTA'),
  tod('Image principale avec alt-text descriptif'),
  tod('URL slug court et lisible'),
  tod('Maillage interne vérifié (≥ 2 liens entrants dans le cluster)'),
  tod('CTA visible sans scroll sur mobile'),
  tod('Mention affilié présente si liens commerciaux'),
  div(),

  // ── SECTION 6 — ÉVOLUTION FUTURE ────────────────────────────────────────────
  h1('🚀 6 — ÉVOLUTION FUTURE'),
  p('Peut devenir pilier ? Oui / Non / Éventuellement'),
  p('Articles satellites à créer :'),
  num('Satellite 1 :'),
  num('Satellite 2 :'),
  num('Satellite 3 :'),
  p(''),
  cal(
    'Généré avec schoolsWP Content Engine · WordPress. Clair. Structuré. Utile.',
    '🧠', 'purple_background'
  )

];

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Création page template Article\n');
  console.log(`  Blocs à créer : ${TEMPLATE.length}`);

  // L'API Notion accepte max 100 blocs dans children à la création
  const CHUNK = 95;
  const firstBatch  = TEMPLATE.slice(0, CHUNK);
  const secondBatch = TEMPLATE.slice(CHUNK);

  const parent = DB_ID
    ? { database_id: DB_ID }
    : { type: 'page_id', page_id: PAGE_ID };

  const titleProp = DB_ID
    ? { 'Titre': { title: [{ text: { content: '📄 [TEMPLATE] Article schoolsWP' } }] }, 'Statut': { select: { name: 'Idée' } } }
    : { title: [{ type: 'text', text: { content: '📄 [TEMPLATE] Article schoolsWP' } }] };

  const pageBody = {
    parent: parent,
    icon: { type: 'emoji', emoji: '📄' },
    properties: titleProp,
    children: firstBatch
  };

  console.log(`\n  📄  Création de la page (batch 1 / ${firstBatch.length} blocs)...`);
  const page = await notion('POST', 'pages', pageBody);
  console.log(`        ✅  ${page.id}`);

  if (secondBatch.length > 0) {
    console.log(`  📝  Ajout des blocs restants (batch 2 / ${secondBatch.length} blocs)...`);
    await notion('PATCH', `blocks/${page.id}/children`, { children: secondBatch });
    console.log('        ✅  Blocs ajoutés');
  }

  const pageUrl = page.url || `https://www.notion.so/${page.id.replace(/-/g, '')}`;

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Page template créée avec succès !\n');
  console.log(`  🔗  ${pageUrl}\n`);

  if (DB_ID) {
    console.log('  📋  Pour en faire un vrai template Notion :');
    console.log('      1. Ouvrir la page ci-dessus dans Notion');
    console.log('      2. Menu "..." (3 points) en haut à droite');
    console.log('      3. "Turn into template" ou "Enregistrer comme modèle"');
    console.log('      4. Renommer : "📄 Article schoolsWP"');
    console.log('      5. Ce template sera disponible dans Articles → bouton "New" ▾');
  } else {
    console.log('  📋  Étapes suivantes :');
    console.log('      1. Ouvrir la page dans Notion');
    console.log('      2. Vérifier le contenu');
    console.log('      3. Dans la base Articles : cliquer sur "New" ▾ → "New template"');
    console.log('      4. Copier/coller le contenu depuis cette page');
  }
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
