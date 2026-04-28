// ---------------------------------------------------------------------------
// CONTENU TEXTUEL — Video marketing schoolsWP
// Source : docs/video-presentation-schoolswp.md
// ---------------------------------------------------------------------------

export const TEXTS = {
  // --- SCENE 1 : Hook ---
  hook: {
    lines: [
      "Ton site web est souvent le premier contact",
      "entre un futur eleve et ton etablissement.",
      "Combien de sites d'ecoles sont lents,",
      "obsoletes ou impossibles a mettre a jour ?",
    ],
    punchline: "Et si ton site travaillait vraiment pour toi ?",
  },

  // --- SCENE 2 : Presentation ---
  presentation: {
    tagline: "WordPress. Clair. Structure. Utile.",
    headline: "Sites WordPress pour le secteur educatif",
    keywords: ["Creation", "Refonte", "Optimisation"],
    subtitle: "Un site professionnel, rapide, securise et facile a gerer.",
  },

  // --- SCENE 3 : Problemes ---
  problems: [
    {
      icon: "\u23F1\uFE0F",
      title: "Site lent",
      desc: "Les visiteurs partent avant de voir tes programmes.",
    },
    {
      icon: "\uD83C\uDFA8",
      title: "Design obsolete",
      desc: "Il ne reflete pas la qualite de ton etablissement.",
    },
    {
      icon: "\uD83D\uDD27",
      title: "Mises a jour complexes",
      desc: "Tu depends d'un prestataire pour chaque modification.",
    },
    {
      icon: "\uD83D\uDCC9",
      title: "Conversions en berne",
      desc: "Le formulaire est enterre, le parcours d'inscription est flou.",
    },
    {
      icon: "\uD83D\uDD0D",
      title: "Invisible sur Google",
      desc: "Ton ecole n'apparait pas quand on cherche une formation.",
    },
  ],

  // --- SCENE 4 : Solutions ---
  solutions: [
    {
      title: "Performance",
      desc: "Des sites qui chargent en moins de 2 secondes.",
    },
    {
      title: "Design professionnel",
      desc: "Moderne, clair, adapte au mobile.",
    },
    {
      title: "Autonomie",
      desc: "Ton equipe met a jour les contenus sans competence technique.",
    },
    {
      title: "Conversion",
      desc: "Des parcours penses pour generer des inscriptions.",
    },
    {
      title: "Visibilite SEO",
      desc: "Une structure optimisee pour les moteurs de recherche.",
    },
  ],

  // --- SCENE 5 : Benefices ---
  benefits: {
    before: {
      title: "Avant",
      items: [
        "Temps perdu sur la technique",
        "Site qui n'inspire pas confiance",
        "Aucune demande entrante",
        "Dependance prestataire",
      ],
    },
    after: {
      title: "Apres schoolsWP",
      items: [
        "Plus de temps pour tes programmes",
        "Credibilite des la premiere visite",
        "Demandes d'info naturelles",
        "Un partenaire unique",
      ],
    },
    punchline: "Un site qui travaille pour toi, pas l'inverse.",
  },

  // --- SCENE 6 : Credibilite ---
  credibility: {
    founder: "Michael KIHL",
    founderTitle: "Fondateur & expert WordPress education",
    badges: [
      { value: "2021", label: "Depuis" },
      { value: "100+", label: "Contenus publies" },
      { value: "5", label: "Etapes \u2014 la methode schoolsWP" },
    ],
    ecosystemTitle: "L'ecosysteme schoolsWP",
    ecosystemItems: ["Blog", "Newsletter", "YouTube", "Academy"],
  },

  // --- SCENE 7 : CTA ---
  cta: {
    headline: "Transforme ton site en levier d'inscriptions.",
    button: "Contacte-nous \u2192",
    url: "schoolswp.com/contact",
    tagline: "WordPress. Clair. Structure. Utile.",
  },
} as const;
