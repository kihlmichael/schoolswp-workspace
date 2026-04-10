/**
 * CLAUDE.md content generator.
 * Builds the markdown output based on user selections.
 */

function generateClaudeMd(data) {
  const sections = [];

  sections.push('# CLAUDE.md');
  sections.push('');
  sections.push('> Fichier genere par [CLAUDE.md Generator](https://schoolswp.com) — guide Claude Code pour intervenir sur ce projet WordPress.');
  sections.push('');

  // 1. Project overview
  sections.push('## 1. Vue d\'ensemble du projet');
  sections.push('');
  if (data.projectDescription) {
    sections.push(data.projectDescription);
  } else {
    sections.push('Projet WordPress.');
  }
  sections.push('');

  // 2. Detected stack
  sections.push('## 2. Stack detectee');
  sections.push('');
  sections.push('| Element | Valeur | Confiance |');
  sections.push('| --- | --- | --- |');

  // WordPress
  if (data.wpVersion && data.wpVersion !== 'unknown') {
    sections.push(`| WordPress | ${data.wpVersion} | Confirme |`);
  } else {
    sections.push('| WordPress | Version non specifiee | Inconnu |');
  }

  // PHP
  if (data.phpVersion && data.phpVersion !== 'unknown') {
    sections.push(`| PHP | ${data.phpVersion} | Confirme |`);
  } else {
    sections.push('| PHP | Version non specifiee | Inconnu |');
  }

  // Theme
  const themeName = getThemeName(data);
  if (themeName) {
    sections.push(`| Theme | ${themeName} | Confirme |`);
  }

  // Child theme
  if (data.hasChildTheme === true) {
    sections.push('| Theme enfant | Oui | Confirme |');
  } else if (data.hasChildTheme === false) {
    sections.push('| Theme enfant | Non | Confirme |');
  } else {
    sections.push('| Theme enfant | Non specifie | Inconnu |');
  }

  // Hosting
  if (data.hosting && data.hosting !== '' && data.hosting !== 'unknown') {
    const hostName = HOSTING_TEMPLATES[data.hosting]?.name || data.hosting;
    sections.push(`| Hebergeur | ${hostName} | Confirme |`);
  } else {
    sections.push('| Hebergeur | Non specifie | Non detectable |');
  }

  // Page builder
  if (data.selectedPageBuilder && data.selectedPageBuilder !== 'Aucun') {
    sections.push(`| Page Builder | ${data.selectedPageBuilder} | Confirme |`);
  }

  // Composer
  if (data.hasComposer === true) {
    sections.push('| Composer | Oui | Confirme |');
  }

  // Build tools
  if (data.selectedBuildTools.length > 0) {
    sections.push(`| Build tools | ${data.selectedBuildTools.join(', ')} | Confirme |`);
  }

  // Git
  if (data.usesGit === true) {
    sections.push('| Git | Oui | Confirme |');
  }

  // CI/CD
  if (data.hasCICD === true && data.cicdTool) {
    sections.push(`| CI/CD | ${data.cicdTool} | Confirme |`);
  }

  // WP-CLI
  if (data.usesWPCLI === true) {
    sections.push('| WP-CLI | Oui | Confirme |');
  }

  sections.push('');

  // 3. Theme, plugins et briques cles
  sections.push('## 3. Theme, plugins et briques cles');
  sections.push('');

  // Theme details
  sections.push('### Theme');
  sections.push('');
  const themeTemplate = getThemeTemplate(data);
  if (themeTemplate) {
    sections.push(`**${themeTemplate.name}**`);
    sections.push('');
    if (themeTemplate.structure) {
      sections.push(themeTemplate.structure);
      sections.push('');
    }
  }

  if (data.hasChildTheme === true) {
    sections.push('Un theme enfant est utilise — toutes les modifications doivent aller dans le theme enfant.');
  } else if (data.hasChildTheme === false && data.selectedTheme !== 'custom') {
    sections.push('**Attention** : pas de theme enfant detecte. Toute modification de template doit passer par un theme enfant pour survivre aux mises a jour.');
  }
  sections.push('');

  // Plugins
  if (data.selectedPlugins.length > 0) {
    sections.push('### Plugins actifs');
    sections.push('');
    sections.push('| Plugin | Role |');
    sections.push('| --- | --- |');
    data.selectedPlugins.forEach(pluginId => {
      const plugin = PLUGIN_TEMPLATES[pluginId];
      if (plugin) {
        sections.push(`| ${plugin.name} | ${plugin.category} |`);
      }
    });
    sections.push('');
  }

  // Page builder
  if (data.selectedPageBuilder && data.selectedPageBuilder !== 'Aucun') {
    sections.push('### Page Builder');
    sections.push('');
    sections.push(PAGE_BUILDER_RULES[data.selectedPageBuilder] || `${data.selectedPageBuilder} est utilise comme page builder.`);
    sections.push('');
  }

  // 4. Structure importante
  sections.push('## 4. Structure importante');
  sections.push('');
  sections.push('```text');
  sections.push('wp-content/');
  sections.push('├── themes/');
  if (data.hasChildTheme === true) {
    sections.push(`│   ├── ${getThemeSlug(data)}/          # Theme parent — NE PAS MODIFIER`);
    sections.push(`│   └── ${getThemeSlug(data)}-child/    # Theme enfant — modifications ici`);
  } else {
    sections.push(`│   └── ${getThemeSlug(data)}/`);
  }
  sections.push('├── plugins/');
  data.selectedPlugins.forEach(pluginId => {
    const plugin = PLUGIN_TEMPLATES[pluginId];
    if (plugin) {
      sections.push(`│   ├── ${pluginId}/`);
    }
  });
  sections.push('├── uploads/');
  sections.push('└── mu-plugins/             # Si present');
  sections.push('```');
  sections.push('');

  // CPT / Taxonomies
  if (data.hasCPT === true && data.cptList) {
    sections.push('### Custom Post Types');
    sections.push('');
    const cpts = data.cptList.split(',').map(s => s.trim()).filter(Boolean);
    cpts.forEach(cpt => {
      sections.push(`- \`${cpt}\``);
    });
    sections.push('');
  }

  if (data.hasTaxonomies === true && data.taxonomyList) {
    sections.push('### Taxonomies custom');
    sections.push('');
    const taxos = data.taxonomyList.split(',').map(s => s.trim()).filter(Boolean);
    taxos.forEach(taxo => {
      sections.push(`- \`${taxo}\``);
    });
    sections.push('');
  }

  // 5. Regles de travail
  sections.push('## 5. Regles de travail pour Claude Code');
  sections.push('');

  // Theme-specific rules
  if (themeTemplate && themeTemplate.rules) {
    sections.push('### Regles liees au theme');
    sections.push('');
    themeTemplate.rules.forEach(rule => {
      sections.push(`- ${rule}`);
    });
    sections.push('');
  }

  // Plugin-specific rules
  const pluginRules = [];
  data.selectedPlugins.forEach(pluginId => {
    const plugin = PLUGIN_TEMPLATES[pluginId];
    if (plugin && plugin.rules) {
      pluginRules.push({ name: plugin.name, rules: plugin.rules });
    }
  });

  if (pluginRules.length > 0) {
    sections.push('### Regles liees aux plugins');
    sections.push('');
    pluginRules.forEach(({ name, rules }) => {
      sections.push(`**${name}** :`);
      rules.forEach(rule => {
        sections.push(`- ${rule}`);
      });
      sections.push('');
    });
  }

  // General rules
  sections.push('### Regles generales');
  sections.push('');
  sections.push('- Ne jamais modifier les fichiers core de WordPress (`wp-admin/`, `wp-includes/`).');
  sections.push('- Ne jamais modifier directement les fichiers des plugins installes via `wp-content/plugins/`.');

  if (data.hasChildTheme !== true && data.selectedTheme !== 'custom') {
    sections.push('- Creer un theme enfant avant toute modification de template.');
  }

  if (data.usesGit === true) {
    sections.push('- Committer chaque changement logique separement avec un message clair.');
  }

  if (data.hasComposer === true) {
    sections.push('- Gerer les dependances PHP via Composer — ne pas copier les librairies manuellement dans le projet.');
  }

  if (data.selectedBuildTools.length > 0) {
    sections.push(`- Lancer le build (${data.selectedBuildTools.join('/')}) apres toute modification des assets source.`);
  }

  sections.push('- Toujours tester les modifications sur un environnement de staging avant la production.');
  sections.push('- Verifier la compatibilite mobile apres chaque modification front-end.');
  sections.push('');

  // 6. Precautions
  sections.push('## 6. Precautions avant modification');
  sections.push('');
  sections.push('Avant toute intervention :');
  sections.push('');
  sections.push('1. **Backup** — S\'assurer qu\'un backup recent existe.');
  sections.push('2. **Identifier la source** — Verifier si le comportement vient du theme, d\'un plugin, ou du core.');
  sections.push('3. **Lire avant d\'ecrire** — Comprendre le code existant avant de le modifier.');
  sections.push('4. **Verifier les hooks** — Chercher si un hook existant permet d\'intervenir sans modifier le fichier source.');
  sections.push('5. **Tester isolement** — Desactiver temporairement les plugins de cache pour voir les changements.');
  sections.push('');

  // 7. Zones sensibles
  sections.push('## 7. Zones sensibles');
  sections.push('');

  // Theme warnings
  if (themeTemplate && themeTemplate.warnings) {
    themeTemplate.warnings.forEach(warning => {
      sections.push(`- ${warning}`);
    });
  }

  // Plugin warnings
  data.selectedPlugins.forEach(pluginId => {
    const plugin = PLUGIN_TEMPLATES[pluginId];
    if (plugin && plugin.warnings) {
      plugin.warnings.forEach(warning => {
        sections.push(`- ${warning}`);
      });
    }
  });

  sections.push('- `wp-config.php` — fichier sensible, ne modifier qu\'en connaissance de cause.');
  sections.push('- `.htaccess` — regen par WordPress et certains plugins, modifications manuelles peuvent etre ecrasees.');
  sections.push('- `wp-content/uploads/` — ne jamais supprimer de fichiers sans verifier les references en base.');
  sections.push('');

  // 8. Workflow
  sections.push('## 8. Workflow recommande');
  sections.push('');
  sections.push('1. **Comprendre** — Lire le code et la documentation avant d\'intervenir.');
  sections.push('2. **Planifier** — Decrire le changement prevu en 2-3 lignes avant de coder.');
  sections.push('3. **Intervenir** — Modifier le minimum necessaire.');
  sections.push('4. **Verifier** — Tester front-end et back-end.');
  sections.push('5. **Documenter** — Commenter les parties non evidentes.');

  if (data.usesGit === true) {
    sections.push('6. **Committer** — Un commit par changement logique, message clair.');
  }

  if (data.deployMethod) {
    sections.push(`7. **Deployer** — Via ${data.deployMethod}.`);
  }

  sections.push('');

  // Hosting notes
  if (data.hosting && HOSTING_TEMPLATES[data.hosting]) {
    sections.push('### Notes hebergeur');
    sections.push('');
    HOSTING_TEMPLATES[data.hosting].notes.forEach(note => {
      sections.push(`- ${note}`);
    });
    sections.push('');
  }

  // WP-CLI commands
  if (data.usesWPCLI === true) {
    sections.push('### Commandes WP-CLI utiles');
    sections.push('');
    sections.push('```bash');
    sections.push('wp cache flush                    # Vider le cache objet');
    sections.push('wp rewrite flush                  # Regenerer les permaliens');
    sections.push('wp plugin list --status=active     # Lister les plugins actifs');
    sections.push('wp theme list                      # Lister les themes');
    sections.push('wp db export backup.sql            # Exporter la base');
    sections.push('wp search-replace "old" "new"      # Rechercher/remplacer en base');
    sections.push('```');
    sections.push('');
  }

  // 9. Hypotheses
  sections.push('## 9. Hypotheses et limites');
  sections.push('');
  sections.push('Ce fichier a ete genere a partir de declarations utilisateur, pas d\'une analyse directe du projet.');
  sections.push('');
  sections.push('**Confirme** : les elements renseignes par l\'utilisateur.');
  sections.push('**Non verifiable** : la coherence entre les plugins declares et leur configuration reelle.');
  sections.push('**Non detectable** : les hooks custom, les mu-plugins, les modifications directes en base, les configurations serveur specifiques.');
  sections.push('');

  // Unknowns
  const unknowns = [];
  if (!data.wpVersion || data.wpVersion === 'unknown') unknowns.push('Version WordPress');
  if (!data.phpVersion || data.phpVersion === 'unknown') unknowns.push('Version PHP');
  if (data.hasChildTheme === null) unknowns.push('Presence d\'un theme enfant');
  if (!data.hosting || data.hosting === 'unknown') unknowns.push('Hebergeur');
  if (data.hasCPT === null) unknowns.push('Custom Post Types');
  if (data.hasTaxonomies === null) unknowns.push('Taxonomies custom');
  if (data.hasCustomBlocks === null) unknowns.push('Blocks Gutenberg custom');
  if (data.hasComposer === null) unknowns.push('Utilisation de Composer');
  if (data.hasCICD === null) unknowns.push('CI/CD');
  if (data.usesWPCLI === null) unknowns.push('WP-CLI');

  if (unknowns.length > 0) {
    sections.push('**Elements non renseignes** (a verifier manuellement) :');
    sections.push('');
    unknowns.forEach(u => {
      sections.push(`- ${u}`);
    });
    sections.push('');
  }

  sections.push('---');
  sections.push('');
  sections.push('*Genere par [CLAUDE.md Generator](https://schoolswp.com) — un outil schoolsWP.*');

  return sections.join('\n');
}

// Helper functions

function getThemeName(data) {
  if (data.selectedTheme === 'custom') {
    return data.customThemeName || 'Theme custom';
  }
  const template = THEME_TEMPLATES[data.selectedTheme];
  return template ? template.name : null;
}

function getThemeSlug(data) {
  if (data.selectedTheme === 'custom') {
    return (data.customThemeName || 'mon-theme').toLowerCase().replace(/\s+/g, '-');
  }
  return data.selectedTheme || 'theme';
}

function getThemeTemplate(data) {
  return THEME_TEMPLATES[data.selectedTheme] || null;
}
