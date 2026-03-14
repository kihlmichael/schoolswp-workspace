// ---------------------------------------------------------------------------
// CONTENU TEXTUEL — Vidéo marketing schoolsWP
// Source : docs/video-presentation-schoolswp.md
// ---------------------------------------------------------------------------

export const TEXTS = {
  // --- SCÈNE 1 : Hook ---
  hook: {
    lines: [
      "Ton site web est souvent le premier contact",
      "entre un futur élève et ton établissement.",
      "Combien de sites d'écoles sont lents,",
      "obsolètes ou impossibles à mettre à jour ?",
    ],
    punchline: "Et si ton site travaillait vraiment pour toi ?",
  },

  // --- SCÈNE 2 : Présentation ---
  presentation: {
    tagline: "WordPress. Clair. Structuré. Utile.",
    headline: "Sites WordPress pour le secteur éducatif",
    keywords: ["Création", "Refonte", "Optimisation"],
    subtitle:
      "Un site professionnel, rapide, sécurisé et facile à gérer.",
  },

  // --- SCÈNE 3 : Problèmes ---
  problems: [
    { icon: "⏱️", title: "Site lent", desc: "Les visiteurs partent avant de voir tes programmes." },
    { icon: "🎨", title: "Design obsolète", desc: "Il ne reflète pas la qualité de ton établissement." },
    { icon: "🔧", title: "Mises à jour complexes", desc: "Tu dépends d'un prestataire pour chaque modification." },
    { icon: "📉", title: "Conversions en berne", desc: "Le formulaire est enterré, le parcours d'inscription est flou." },
    { icon: "🔍", title: "Invisible sur Google", desc: "Ton école n'apparaît pas quand on cherche une formation." },
  ],

  // --- SCÈNE 4 : Solutions ---
  solutions: [
    { title: "Performance", desc: "Des sites qui chargent en moins de 2 secondes." },
    { title: "Design professionnel", desc: "Moderne, clair, adapté au mobile." },
    { title: "Autonomie", desc: "Ton équipe met à jour les contenus sans compétence technique." },
    { title: "Conversion", desc: "Des parcours pensés pour générer des inscriptions." },
    { title: "Visibilité SEO", desc: "Une structure optimisée pour les moteurs de recherche." },
  ],

  // --- SCÈNE 5 : Bénéfices ---
  benefits: {
    before: {
      title: "Avant",
      items: [
        "Temps perdu sur la technique",
        "Site qui n'inspire pas confiance",
        "Aucune demande entrante",
        "Dépendance prestataire",
      ],
    },
    after: {
      title: "Après schoolsWP",
      items: [
        "Plus de temps pour tes programmes",
        "Crédibilité dès la première visite",
        "Demandes d'info naturelles",
        "Un partenaire unique",
      ],
    },
    punchline: "Un site qui travaille pour toi, pas l'inverse.",
  },

  // --- SCÈNE 6 : Crédibilité ---
  credibility: {
    founder: "Michaël KIHL",
    founderTitle: "Fondateur & expert WordPress éducation",
    badges: [
      { value: "2021", label: "Depuis" },
      { value: "100+", label: "Contenus publiés" },
      { value: "5", label: "Étapes — la méthode schoolsWP" },
    ],
    ecosystemItems: ["Blog", "Newsletter", "YouTube", "Academy"],
  },

  // --- SCÈNE 7 : CTA ---
  cta: {
    headline: "Transforme ton site en levier d'inscriptions.",
    button: "Contacte-nous →",
    url: "schoolswp.com/contact",
    tagline: "WordPress. Clair. Structuré. Utile.",
  },
} as const;
