import { loadFont } from "@remotion/google-fonts/Inter";

const { fontFamily } = loadFont();

// ---------------------------------------------------------------------------
// REGLAGES RAPIDES — Modifier ici pour ajuster l'animation
// ---------------------------------------------------------------------------

export const THEME = {
  // --- COULEURS ---
  background: "#F7F7F5",
  backgroundGradient: "#EEEEE9",
  textPrimary: "#1F1F1F",
  textSecondary: "#6B6B6B",
  accent: "#00D400",
  accentDark: "#1CA61C",
  gridColor: "rgba(0, 0, 0, 0.035)",
  separatorColor: "#E0E0E0",

  // --- TYPOGRAPHIE ---
  fontFamily,
  fontSizeHero: 72,
  fontSizePreTitle: 34,
  fontSizeSubtitle: 30,
  fontSizeCTA: 26,
  letterSpacing: 1.5,
  lineHeight: 1.45,

  // --- TIMELINE (frames @ 30fps) ---
  fps: 30,
  totalFrames: 540, // 18s

  logoIn: 60, //  2s — logo starts appearing
  logoStable: 150, //  5s — logo fully stable
  msgIn: 210, //  7s — message text appears
  cobrandIn: 300, // 10s — WordPress co-branding
  ctaIn: 420, // 14s — CTA text
  fadeStart: 480, // 16s — start global fade-out

  // --- SPRING CONFIGS ---
  springSmooth: { damping: 200, mass: 1, stiffness: 80 },
  springPunch: { damping: 120, mass: 0.8, stiffness: 150 },

  // --- THREE.JS ---
  cameraFov: 50,
  cameraZ: 12,
  extrudeDepth: 4,
  bevelThickness: 0.3,
  bevelSize: 0.2,
  logoScaleTarget: 10, // Three.js units width

  // --- LOGO PATHS ---
  logoSchoolsWP: "logo-schoolswp.svg",
  logoWordPress: "logo-wordpress.png",
} as const;

// ---------------------------------------------------------------------------
// TEXTES
// ---------------------------------------------------------------------------

export const TEXT = {
  preTitle: "Votre site WordPress",
  headline: "Plus rapide. Plus rentable.",
  accentPhrase: "Plus rentable.",
  subtitle: "SEO \u00B7 Performance \u00B7 Automatisation",
  cta: "Retrouvez le guide complet",
};
