import { loadFont as loadNunitoSans } from "@remotion/google-fonts/NunitoSans";
import { loadFont as loadRoboto } from "@remotion/google-fonts/Roboto";

const { fontFamily: headingFont } = loadNunitoSans();
const { fontFamily: bodyFont } = loadRoboto();

export const THEME = {
  // --- COULEURS (brand kit schoolsWP) ---
  primary: "#00D400",
  primaryDark: "#00A100",
  accent: "#E668D4",
  bgLight: "#FAFBFD",
  bgSubtle: "#F4F6FB",
  bgDark: "#12111F",
  bgDarkAlt: "#212121",
  textPrimary: "#212121",
  textSecondary: "#57556D",
  textLight: "#8F8DA5",
  textWhite: "#FAFBFD",
  gridColor: "rgba(255, 255, 255, 0.04)",
  gridColorLight: "rgba(0, 0, 0, 0.035)",
  red: "#B82105",
  redSubtle: "rgba(184, 33, 5, 0.12)",
  greenSubtle: "rgba(0, 212, 0, 0.12)",

  // --- TYPOGRAPHIE ---
  headingFont,
  bodyFont,
  fontSizeHero: 64,
  fontSizeH2: 48,
  fontSizeH3: 36,
  fontSizeBody: 28,
  fontSizeCaption: 22,
  fontSizeSmall: 18,
  lineHeight: 1.4,

  // --- TIMELINE (frames @ 30fps) ---
  fps: 30,
  totalFrames: 5100, // 2:50

  scene1: { start: 0, duration: 600 }, // Hook (20s)
  scene2: { start: 600, duration: 750 }, // Presentation (25s)
  scene3: { start: 1350, duration: 1050 }, // Problemes (35s)
  scene4: { start: 2400, duration: 1050 }, // Solutions (35s)
  scene5: { start: 3450, duration: 600 }, // Benefices (20s)
  scene6: { start: 4050, duration: 600 }, // Credibilite (20s)
  scene7: { start: 4650, duration: 450 }, // CTA (15s)

  // --- SPRING CONFIGS ---
  springSmooth: { damping: 200, mass: 1, stiffness: 80 },
  springPunch: { damping: 120, mass: 0.8, stiffness: 150 },
  springGentle: { damping: 200, mass: 1.2, stiffness: 60 },

  // --- ANIMATION ---
  fadeInDuration: 20, // frames for standard fade-in
  staggerDelay: 15, // frames between staggered items
  transitionFrames: 30, // frames for scene transitions
} as const;
