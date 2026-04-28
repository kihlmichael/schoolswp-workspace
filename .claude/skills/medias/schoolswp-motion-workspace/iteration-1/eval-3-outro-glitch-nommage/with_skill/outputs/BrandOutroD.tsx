import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  random,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { THEME } from "../theme";

// ---------------------------------------------------------------------------
// BrandOutroD — "Pulse Impact"
// Particules convergentes → flash → logo spring punch → pulse rings → URL
// Variante energetique tout en restant premium / schoolsWP
// ---------------------------------------------------------------------------

// Converging particles (40 — more than B/CPro for density)
const PARTICLES = Array.from({ length: 40 }, (_, i) => ({
  x: random(`od-px-${i}`) * 1920,
  y: random(`od-py-${i}`) * 1080,
  size: 1.5 + random(`od-ps-${i}`) * 3,
  delay: random(`od-pd-${i}`) * 20,
}));

export const BrandOutroD: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const centerX = 960;
  const centerY = 500;

  // ===== PHASE 1: Particles converge toward center (0-1.5s / frames 0-45) =====
  const particleConverge = interpolate(frame, [0, 45], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.in(Easing.quad),
  });
  const particleGlobalOpacity = interpolate(
    frame,
    [0, 10, 35, 48],
    [0, 0.7, 0.7, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  // ===== PHASE 2: Condensation flash (1.3s-1.8s / frames 40-55) =====
  const flashOpacity = interpolate(frame, [40, 45, 55], [0, 0.25, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== PHASE 2b: Logo spring punch entrance (1.5s-2.5s / frames 45-75) =====
  const logoSpring = spring({
    frame: frame - 45,
    fps,
    config: THEME.springPunch,
    durationInFrames: 30,
  });
  const logoScale = interpolate(logoSpring, [0, 1], [0.85, 1]);
  const logoOpacity = logoSpring;

  // ===== PHASE 3: Pulse rings from logo (1.8s-3.2s / frames 54-96) =====
  const ring1Spring = spring({
    frame: frame - 50,
    fps,
    config: { damping: 25, stiffness: 35, mass: 1.5 },
    durationInFrames: 45,
  });
  const ring1Scale = interpolate(ring1Spring, [0, 1], [0, 12]);
  const ring1Opacity = interpolate(ring1Spring, [0, 0.2, 1], [0, 0.3, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const ring2Spring = spring({
    frame: frame - 58,
    fps,
    config: { damping: 22, stiffness: 30, mass: 1.8 },
    durationInFrames: 50,
  });
  const ring2Scale = interpolate(ring2Spring, [0, 1], [0, 9]);
  const ring2Opacity = interpolate(ring2Spring, [0, 0.2, 1], [0, 0.2, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const ring3Spring = spring({
    frame: frame - 65,
    fps,
    config: { damping: 18, stiffness: 25, mass: 2 },
    durationInFrames: 55,
  });
  const ring3Scale = interpolate(ring3Spring, [0, 1], [0, 6]);
  const ring3Opacity = interpolate(ring3Spring, [0, 0.15, 1], [0, 0.12, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== PHASE 4: Green accent line (3.0s-3.8s / frames 90-114) =====
  const lineProgress = interpolate(frame, [90, 114], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const lineWidth = lineProgress * 200;
  const lineOpacity = interpolate(frame, [90, 100], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== PHASE 4b: URL stagger reveal (3.2s-4.2s / frames 96-126) =====
  const urlText = "schoolsWP.com";
  const urlStartFrame = 96;
  const staggerPerChar = 2;

  // ===== GLOW: breathing behind logo =====
  const glowBase = interpolate(frame, [45, 75], [0, 0.1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const glowBreath = Math.sin(frame * 0.07) * 0.03;
  const glowOpacity = Math.max(0, glowBase + glowBreath);

  // ===== PHASE 5: Global fade out (last 10 frames) =====
  const globalOpacity = interpolate(frame, [140, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: THEME.bgDark,
        justifyContent: "center",
        alignItems: "center",
        opacity: globalOpacity,
        overflow: "hidden",
      }}
    >
      {/* ===== CONVERGING PARTICLES ===== */}
      {PARTICLES.map((p, i) => {
        const progress = interpolate(frame, [p.delay, 45], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
          easing: Easing.in(Easing.quad),
        });
        const px = p.x + (centerX - p.x) * progress;
        const py = p.y + (centerY - p.y) * progress;
        const pOpacity =
          particleGlobalOpacity * (0.4 + random(`od-po-${i}`) * 0.6);

        return (
          <div
            key={`p-${i}`}
            style={{
              position: "absolute",
              left: px,
              top: py,
              width: p.size,
              height: p.size,
              borderRadius: "50%",
              backgroundColor: THEME.primary,
              opacity: pOpacity,
              filter: "blur(0.5px)",
            }}
          />
        );
      })}

      {/* ===== CONDENSATION FLASH ===== */}
      <div
        style={{
          position: "absolute",
          width: 400,
          height: 400,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 65%)`,
          opacity: flashOpacity,
          filter: "blur(50px)",
        }}
      />

      {/* ===== PULSE RINGS (spring-driven, radiating outward) ===== */}
      <div
        style={{
          position: "absolute",
          width: 60,
          height: 60,
          borderRadius: "50%",
          border: `2px solid ${THEME.primary}`,
          opacity: ring1Opacity,
          transform: `scale(${ring1Scale})`,
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 60,
          height: 60,
          borderRadius: "50%",
          border: `1.5px solid ${THEME.primary}`,
          opacity: ring2Opacity,
          transform: `scale(${ring2Scale})`,
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 60,
          height: 60,
          borderRadius: "50%",
          border: `1px solid ${THEME.primary}`,
          opacity: ring3Opacity,
          transform: `scale(${ring3Scale})`,
        }}
      />

      {/* ===== GLOW (breathing) ===== */}
      <div
        style={{
          position: "absolute",
          width: 550,
          height: 550,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 60%)`,
          opacity: glowOpacity,
          filter: "blur(100px)",
        }}
      />

      {/* ===== LOGO schoolsWP (spring punch entrance) ===== */}
      <Img
        src={staticFile("logos/nom-white.svg")}
        style={{
          width: 440,
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
        }}
      />

      {/* ===== GREEN ACCENT LINE ===== */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 50,
          width: lineWidth,
          height: 2,
          backgroundColor: THEME.primary,
          opacity: lineOpacity,
          boxShadow: `0 0 10px ${THEME.primary}50`,
        }}
      />

      {/* ===== STAGGERED URL REVEAL: schoolsWP.com ===== */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 72,
          display: "flex",
          fontFamily: THEME.headingFont,
          fontSize: THEME.fontSizeSmall,
          letterSpacing: 3,
        }}
      >
        {urlText.split("").map((char, i) => {
          const charFrame = urlStartFrame + i * staggerPerChar;
          const charSpring = spring({
            frame: frame - charFrame,
            fps,
            config: { damping: 200, stiffness: 120 },
            durationInFrames: 20,
          });
          const charOpacity = charSpring;
          const charY = interpolate(charSpring, [0, 1], [12, 0]);

          return (
            <span
              key={i}
              style={{
                opacity: charOpacity,
                transform: `translateY(${charY}px)`,
                color: THEME.textWhite,
                display: "inline-block",
              }}
            >
              {char}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
