#!/usr/bin/env node
/**
 * n8n Maintenance Script
 * Automatise la maintenance des workflows n8n :
 * - Détection des nœuds obsolètes
 * - Nettoyage des workflows archivés
 * - Génération de rapports
 *
 * Usage: node n8n-maintenance.js [command]
 * Commands: audit | clean | report | update-check
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Configuration - Charger depuis .env ou .mcp.json
const CONFIG = {
  N8N_API_URL: process.env.N8N_API_URL || 'https://schoolswp-n8n.wp1.host',
  N8N_API_KEY: process.env.N8N_API_KEY || '',
  REPORT_DIR: process.env.REPORT_DIR || './reports',
  DRY_RUN: process.env.DRY_RUN !== 'false', // Par défaut en mode simulation
};

// Charger la config depuis .mcp.json si pas de clé API
if (!CONFIG.N8N_API_KEY) {
  try {
    const mcpConfig = JSON.parse(fs.readFileSync(path.join(__dirname, '../.mcp.json'), 'utf8'));
    if (mcpConfig.mcpServers?.['n8n-mcp']?.env) {
      CONFIG.N8N_API_URL = mcpConfig.mcpServers['n8n-mcp'].env.N8N_API_URL || CONFIG.N8N_API_URL;
      CONFIG.N8N_API_KEY = mcpConfig.mcpServers['n8n-mcp'].env.N8N_API_KEY || '';
    }
  } catch (e) {
    // Ignorer si .mcp.json n'existe pas
  }
}

// Versions connues des nœuds (à mettre à jour régulièrement)
const LATEST_NODE_VERSIONS = {
  'n8n-nodes-base.manualTrigger': 1,
  'n8n-nodes-base.httpRequest': 4.2,
  'n8n-nodes-base.set': 3.4,
  'n8n-nodes-base.if': 2.2,
  'n8n-nodes-base.code': 2,
  'n8n-nodes-base.webhook': 2.1,
  'n8n-nodes-base.googleSheets': 4.7,
  'n8n-nodes-base.googleDrive': 3,
  'n8n-nodes-base.gmail': 2.2,
  'n8n-nodes-base.gmailTrigger': 1.3,
  'n8n-nodes-base.slack': 2.3,
  'n8n-nodes-base.discord': 2.2,
  'n8n-nodes-base.telegram': 1.2,
  'n8n-nodes-base.notion': 2.3,
  'n8n-nodes-base.airtable': 2.2,
  '@n8n/n8n-nodes-langchain.agent': 3.1,
  '@n8n/n8n-nodes-langchain.lmChatOpenAi': 1.2,
  '@n8n/n8n-nodes-langchain.lmChatOpenRouter': 1,
  '@n8n/n8n-nodes-langchain.vectorStorePinecone': 1.3,
  '@n8n/n8n-nodes-langchain.embeddingsOpenAi': 1.2,
};

// Couleurs pour la console
const colors = {
  reset: '\x1b[0m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  gray: '\x1b[90m',
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

// API Helper
async function apiRequest(endpoint, method = 'GET', body = null) {
  return new Promise((resolve, reject) => {
    const url = new URL(endpoint, CONFIG.N8N_API_URL);

    const options = {
      hostname: url.hostname,
      port: url.port || 443,
      path: url.pathname + url.search,
      method,
      headers: {
        'X-N8N-API-KEY': CONFIG.N8N_API_KEY,
        'Content-Type': 'application/json',
      },
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          resolve(data);
        }
      });
    });

    req.on('error', reject);

    if (body) {
      req.write(JSON.stringify(body));
    }

    req.end();
  });
}

// Récupérer tous les workflows
async function getAllWorkflows() {
  const workflows = [];
  let cursor = null;

  do {
    const url = cursor
      ? `/api/v1/workflows?limit=100&cursor=${cursor}`
      : '/api/v1/workflows?limit=100';

    const response = await apiRequest(url);
    workflows.push(...response.data);
    cursor = response.nextCursor;
  } while (cursor);

  return workflows;
}

// Analyser les nœuds obsolètes
function analyzeOutdatedNodes(workflows) {
  const outdated = [];

  for (const workflow of workflows) {
    if (!workflow.nodes) continue;

    for (const node of workflow.nodes) {
      const latestVersion = LATEST_NODE_VERSIONS[node.type];

      if (latestVersion && node.typeVersion < latestVersion) {
        outdated.push({
          workflowId: workflow.id,
          workflowName: workflow.name,
          nodeId: node.id,
          nodeName: node.name,
          nodeType: node.type,
          currentVersion: node.typeVersion,
          latestVersion,
          isActive: workflow.active,
        });
      }
    }
  }

  return outdated;
}

// Identifier les workflows à nettoyer
function identifyCleanupCandidates(workflows) {
  const now = new Date();
  const sixMonthsAgo = new Date(now.setMonth(now.getMonth() - 6));

  return {
    archived: workflows.filter(w => w.isArchived),
    inactive: workflows.filter(w => !w.active && !w.isArchived),
    stale: workflows.filter(w => {
      const updated = new Date(w.updatedAt);
      return !w.active && !w.isArchived && updated < sixMonthsAgo;
    }),
    unnamed: workflows.filter(w =>
      w.name.startsWith('My workflow') ||
      w.name === 'Untitled' ||
      w.name.match(/^workflow\s*\d*$/i)
    ),
  };
}

// Supprimer un workflow
async function deleteWorkflow(workflowId) {
  if (CONFIG.DRY_RUN) {
    log(`  [DRY RUN] Suppression simulée: ${workflowId}`, 'yellow');
    return { success: true, dryRun: true };
  }

  try {
    await apiRequest(`/api/v1/workflows/${workflowId}`, 'DELETE');
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

// Générer le rapport Markdown
function generateReport(data) {
  const { workflows, outdatedNodes, cleanup, stats } = data;
  const now = new Date().toISOString().split('T')[0];

  let report = `# Rapport de Maintenance n8n
> Généré le ${now}

## Résumé

| Métrique | Valeur |
|----------|--------|
| Total workflows | ${stats.total} |
| Actifs | ${stats.active} |
| Inactifs | ${stats.inactive} |
| Archivés | ${stats.archived} |
| Nœuds obsolètes | ${outdatedNodes.length} |

## Workflows Actifs

| Nom | ID | Nœuds |
|-----|-------|-------|
${workflows.filter(w => w.active).map(w =>
  `| ${w.name} | \`${w.id}\` | ${w.nodes?.length || 0} |`
).join('\n')}

## Nœuds Obsolètes

${outdatedNodes.length === 0 ? '✅ Aucun nœud obsolète détecté !' : `
| Workflow | Nœud | Type | Version | Dernière |
|----------|------|------|---------|----------|
${outdatedNodes.map(n =>
  `| ${n.workflowName} | ${n.nodeName} | \`${n.nodeType}\` | ${n.currentVersion} | ${n.latestVersion} |`
).join('\n')}
`}

## Candidats au Nettoyage

### Archivés (${cleanup.archived.length})
${cleanup.archived.length === 0 ? 'Aucun' : cleanup.archived.map(w => `- \`${w.id}\` - ${w.name}`).join('\n')}

### Non nommés (${cleanup.unnamed.length})
${cleanup.unnamed.length === 0 ? 'Aucun' : cleanup.unnamed.map(w => `- \`${w.id}\` - ${w.name}`).join('\n')}

### Inactifs depuis 6+ mois (${cleanup.stale.length})
${cleanup.stale.length === 0 ? 'Aucun' : cleanup.stale.map(w => `- \`${w.id}\` - ${w.name} (modifié: ${w.updatedAt?.split('T')[0]})`).join('\n')}

## Recommandations

1. ${outdatedNodes.length > 0 ? `⚠️ Mettre à jour ${outdatedNodes.length} nœud(s) obsolète(s)` : '✅ Tous les nœuds sont à jour'}
2. ${cleanup.archived.length > 0 ? `🗑️ Supprimer ${cleanup.archived.length} workflow(s) archivé(s)` : '✅ Aucun workflow archivé'}
3. ${cleanup.unnamed.length > 0 ? `📝 Renommer ${cleanup.unnamed.length} workflow(s) sans nom explicite` : '✅ Tous les workflows sont nommés'}
4. ${cleanup.stale.length > 0 ? `🔍 Réviser ${cleanup.stale.length} workflow(s) inactif(s) depuis 6+ mois` : '✅ Aucun workflow obsolète'}

---
*Rapport généré par n8n-maintenance.js*
`;

  return report;
}

// === COMMANDES ===

async function cmdAudit() {
  log('\n🔍 Audit des workflows n8n...', 'cyan');

  const workflows = await getAllWorkflows();
  const outdatedNodes = analyzeOutdatedNodes(workflows);
  const cleanup = identifyCleanupCandidates(workflows);

  log(`\n📊 Résumé:`, 'blue');
  log(`   Total workflows: ${workflows.length}`);
  log(`   Actifs: ${workflows.filter(w => w.active).length}`, 'green');
  log(`   Inactifs: ${workflows.filter(w => !w.active && !w.isArchived).length}`, 'yellow');
  log(`   Archivés: ${cleanup.archived.length}`, 'gray');

  log(`\n⚠️  Nœuds obsolètes: ${outdatedNodes.length}`, outdatedNodes.length > 0 ? 'red' : 'green');

  if (outdatedNodes.length > 0) {
    for (const node of outdatedNodes.slice(0, 10)) {
      log(`   - ${node.workflowName} → ${node.nodeName} (v${node.currentVersion} → v${node.latestVersion})`, 'yellow');
    }
    if (outdatedNodes.length > 10) {
      log(`   ... et ${outdatedNodes.length - 10} autres`, 'gray');
    }
  }

  log(`\n🗑️  Candidats au nettoyage:`, 'blue');
  log(`   Archivés: ${cleanup.archived.length}`);
  log(`   Non nommés: ${cleanup.unnamed.length}`);
  log(`   Inactifs 6+ mois: ${cleanup.stale.length}`);

  return { workflows, outdatedNodes, cleanup };
}

async function cmdClean(options = {}) {
  log('\n🧹 Nettoyage des workflows...', 'cyan');

  if (CONFIG.DRY_RUN) {
    log('   Mode simulation (DRY_RUN=true)', 'yellow');
  }

  const workflows = await getAllWorkflows();
  const cleanup = identifyCleanupCandidates(workflows);

  const targets = options.all
    ? [...cleanup.archived, ...cleanup.unnamed]
    : cleanup.archived;

  log(`\n   ${targets.length} workflow(s) à nettoyer`, 'blue');

  let deleted = 0;
  let failed = 0;

  for (const workflow of targets) {
    const result = await deleteWorkflow(workflow.id);
    if (result.success) {
      deleted++;
      log(`   ✓ ${workflow.name}`, 'green');
    } else {
      failed++;
      log(`   ✗ ${workflow.name}: ${result.error}`, 'red');
    }
  }

  log(`\n📊 Résultat: ${deleted} supprimé(s), ${failed} échec(s)`, deleted > 0 ? 'green' : 'yellow');

  return { deleted, failed, total: targets.length };
}

async function cmdReport() {
  log('\n📝 Génération du rapport...', 'cyan');

  const workflows = await getAllWorkflows();
  const outdatedNodes = analyzeOutdatedNodes(workflows);
  const cleanup = identifyCleanupCandidates(workflows);

  const stats = {
    total: workflows.length,
    active: workflows.filter(w => w.active).length,
    inactive: workflows.filter(w => !w.active && !w.isArchived).length,
    archived: cleanup.archived.length,
  };

  const report = generateReport({ workflows, outdatedNodes, cleanup, stats });

  // Créer le dossier reports si nécessaire
  const reportDir = path.resolve(__dirname, '..', 'reports');
  if (!fs.existsSync(reportDir)) {
    fs.mkdirSync(reportDir, { recursive: true });
  }

  const reportPath = path.join(reportDir, `n8n-maintenance-${new Date().toISOString().split('T')[0]}.md`);
  fs.writeFileSync(reportPath, report);

  log(`   ✓ Rapport sauvegardé: ${reportPath}`, 'green');

  return { reportPath, stats };
}

async function cmdUpdateCheck() {
  log('\n🔄 Vérification des mises à jour de nœuds...', 'cyan');

  const workflows = await getAllWorkflows();
  const outdatedNodes = analyzeOutdatedNodes(workflows);

  if (outdatedNodes.length === 0) {
    log('\n   ✅ Tous les nœuds sont à jour !', 'green');
    return { outdated: [] };
  }

  // Grouper par type de nœud
  const byType = {};
  for (const node of outdatedNodes) {
    if (!byType[node.nodeType]) {
      byType[node.nodeType] = [];
    }
    byType[node.nodeType].push(node);
  }

  log(`\n   ⚠️ ${outdatedNodes.length} nœud(s) obsolète(s) dans ${Object.keys(byType).length} type(s):\n`, 'yellow');

  for (const [type, nodes] of Object.entries(byType)) {
    const latest = LATEST_NODE_VERSIONS[type];
    log(`   ${type}`, 'blue');
    log(`      Version actuelle → dernière: v${nodes[0].currentVersion} → v${latest}`);
    log(`      Workflows affectés: ${nodes.length}`);
    for (const n of nodes.slice(0, 3)) {
      log(`         - ${n.workflowName}`, 'gray');
    }
    if (nodes.length > 3) {
      log(`         ... et ${nodes.length - 3} autres`, 'gray');
    }
    log('');
  }

  return { outdated: outdatedNodes, byType };
}

// === MAIN ===

async function main() {
  const command = process.argv[2] || 'audit';

  log('═══════════════════════════════════════════', 'cyan');
  log('        n8n Maintenance Script', 'cyan');
  log('═══════════════════════════════════════════', 'cyan');
  log(`   Instance: ${CONFIG.N8N_API_URL}`, 'gray');
  log(`   Commande: ${command}`, 'gray');

  if (!CONFIG.N8N_API_KEY) {
    log('\n❌ Erreur: N8N_API_KEY non configurée', 'red');
    log('   Définir via variable d\'environnement ou .mcp.json', 'gray');
    process.exit(1);
  }

  try {
    switch (command) {
      case 'audit':
        await cmdAudit();
        break;
      case 'clean':
        await cmdClean({ all: process.argv.includes('--all') });
        break;
      case 'report':
        await cmdReport();
        break;
      case 'update-check':
        await cmdUpdateCheck();
        break;
      default:
        log(`\n❌ Commande inconnue: ${command}`, 'red');
        log('\nCommandes disponibles:', 'blue');
        log('   audit        - Analyser tous les workflows');
        log('   clean        - Supprimer les workflows archivés (--all pour inclure non nommés)');
        log('   report       - Générer un rapport Markdown');
        log('   update-check - Vérifier les nœuds obsolètes');
        process.exit(1);
    }

    log('\n✅ Terminé !', 'green');
  } catch (error) {
    log(`\n❌ Erreur: ${error.message}`, 'red');
    process.exit(1);
  }
}

main();
