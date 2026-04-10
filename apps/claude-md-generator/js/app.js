/**
 * Alpine.js application for the CLAUDE.md Generator.
 */

function claudeGenerator() {
  return {
    // Navigation
    step: 1,
    stepLabels: ['Stack', 'Structure', 'Conventions', 'Resultat'],
    copied: false,

    // Step 1: Stack
    themes: [
      { id: 'astra', name: 'Astra' },
      { id: 'generatepress', name: 'GeneratePress' },
      { id: 'divi', name: 'Divi' },
      { id: 'kadence', name: 'Kadence' },
      { id: 'oceanwp', name: 'OceanWP' },
      { id: 'custom', name: 'Theme custom' },
    ],
    selectedTheme: '',
    customThemeName: '',
    hasChildTheme: null,

    plugins: [
      { id: 'woocommerce', name: 'WooCommerce', category: 'E-commerce' },
      { id: 'acf', name: 'ACF', category: 'Custom Fields' },
      { id: 'yoast', name: 'Yoast SEO', category: 'SEO' },
      { id: 'elementor', name: 'Elementor', category: 'Page Builder' },
      { id: 'cf7', name: 'Contact Form 7', category: 'Formulaires' },
    ],
    selectedPlugins: [],

    hosting: '',
    phpVersion: '',
    wpVersion: '',

    // Step 2: Structure
    hasCPT: null,
    cptList: '',
    hasTaxonomies: null,
    taxonomyList: '',
    hasCustomBlocks: null,
    selectedPageBuilder: '',
    pageBuilders: [
      'Gutenberg (natif)',
      'Elementor',
      'Divi Builder',
      'Beaver Builder',
      'Bricks',
      'Oxygen',
      'Aucun',
    ],
    selectedBuildTools: [],
    buildTools: ['Vite', 'Webpack', 'Gulp', 'npm scripts', 'Aucun'],
    hasComposer: null,

    // Step 3: Conventions
    usesGit: null,
    deployMethod: '',
    deployMethods: ['FTP/SFTP', 'Git push', 'CI/CD pipeline', 'SSH + WP-CLI', 'Panel hebergeur', 'Je ne sais pas'],
    selectedEnvironments: [],
    environments: ['Local', 'Staging', 'Production'],
    hasCICD: null,
    cicdTool: '',
    usesWPCLI: null,
    projectDescription: '',

    // Methods
    toggleSelection(field, value) {
      this[field] = this[field] === value ? '' : value;
    },

    toggleArraySelection(field, value) {
      const index = this[field].indexOf(value);
      if (index === -1) {
        this[field].push(value);
      } else {
        this[field].splice(index, 1);
      }
    },

    nextStep() {
      if (this.step < 4) {
        this.step++;
      }
    },

    prevStep() {
      if (this.step > 1) {
        this.step--;
      }
    },

    goToStep(s) {
      this.step = s;
    },

    generatePreview() {
      return generateClaudeMd(this.getData());
    },

    getData() {
      return {
        selectedTheme: this.selectedTheme,
        customThemeName: this.customThemeName,
        hasChildTheme: this.hasChildTheme,
        selectedPlugins: this.selectedPlugins,
        hosting: this.hosting,
        phpVersion: this.phpVersion,
        wpVersion: this.wpVersion,
        hasCPT: this.hasCPT,
        cptList: this.cptList,
        hasTaxonomies: this.hasTaxonomies,
        taxonomyList: this.taxonomyList,
        hasCustomBlocks: this.hasCustomBlocks,
        selectedPageBuilder: this.selectedPageBuilder,
        selectedBuildTools: this.selectedBuildTools,
        hasComposer: this.hasComposer,
        usesGit: this.usesGit,
        deployMethod: this.deployMethod,
        selectedEnvironments: this.selectedEnvironments,
        hasCICD: this.hasCICD,
        cicdTool: this.cicdTool,
        usesWPCLI: this.usesWPCLI,
        projectDescription: this.projectDescription,
      };
    },

    async copyToClipboard() {
      const content = generateClaudeMd(this.getData());
      try {
        await navigator.clipboard.writeText(content);
        this.copied = true;
        setTimeout(() => { this.copied = false; }, 2000);
      } catch {
        // Fallback
        const textarea = document.createElement('textarea');
        textarea.value = content;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        this.copied = true;
        setTimeout(() => { this.copied = false; }, 2000);
      }
    },

    downloadFile() {
      const content = generateClaudeMd(this.getData());
      const blob = new Blob([content], { type: 'text/markdown' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'CLAUDE.md';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    },
  };
}
