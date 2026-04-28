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

// ============================================================
// NEON PARTICLES — exploding outward from center
// ============================================================
const NEON_COLORS = [
  THEME.primary, // green
  THEME.accent, // pink
  "#00E5FF", // cyan
  "#FFEA00", // yellow neon
  "#FF3D00", // orange neon
  "#B388FF", // lavender neon
];

const PARTICLE_COUNT = 80;
const PARTICLES = Array.from({ length: PARTICLE_COUNT }, (_, i) => {
  const angle = random(`angle-${i}`) * Math.PI * 2;
  const speed = 4 + random(`speed-${i}`) * 12;
  const size = 2 + random(`size-${i}`) * 5;
  const colorIndex = Math.floor(random(`color-${i}`) * NEON_COLORS.length);
  const delay = random(`delay-${i}`) * 10; // stagger frames
  const lifetime = 30 + random(`life-${i}`) * 40;
  const rotationSpeed = (random(`rot-${i}`) - 0.5) * 20;

  return {
    angle,
    speed,
    size,
    color: NEON_COLORS[colorIndex],
    delay,
    lifetime,
    rotationSpeed,
    // Shape variant: 0 = circle, 1 = square, 2 = diamond
    shape: Math.floor(random(`shape-${i}`) * 3),
  };
});

// Second wave of particles (delayed explosion)
const PARTICLES_WAVE2 = Array.from({ length: 40 }, (_, i) => {
  const angle = random(`w2angle-${i}`) * Math.PI * 2;
  const speed = 3 + random(`w2speed-${i}`) * 8;
  const size = 1.5 + random(`w2size-${i}`) * 3;
  const colorIndex = Math.floor(random(`w2color-${i}`) * NEON_COLORS.length);
  const delay = 15 + random(`w2delay-${i}`) * 8;
  const lifetime = 25 + random(`w2life-${i}`) * 35;

  return {
    angle,
    speed,
    size,
    color: NEON_COLORS[colorIndex],
    delay,
    lifetime,
    shape: Math.floor(random(`w2shape-${i}`) * 3),
    rotationSpeed: (random(`w2rot-${i}`) - 0.5) * 15,
  };
});

// ============================================================
// GLITCH HELPERS
// ============================================================

/** Pseudo-random glitch offset — deterministic per frame */
function glitchOffset(frame: number, seed: string, amplitude: number): number {
  const r = random(`${seed}-${Math.floor(frame / 2)}`);
  return (r - 0.5) * 2 * amplitude;
}

/** Whether a glitch "event" is active at this frame */
function isGlitchActive(frame: number, seed: string): boolean {
  return random(`glitch-active-${seed}-${Math.floor(frame / 3)}`) > 0.6;
}

// ============================================================
// COMPONENT
// ============================================================
export const OutroFinalV3New: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const totalFrames = fps * 5; // 5 seconds = 150 frames

  // ===== TIMELINE =====
  // Phase 1 (0-30): Neon particles explode from center
  // Phase 2 (20-60): Logo appears with heavy glitch
  // Phase 3 (60-100): Glitch stabilizes, logo holds
  // Phase 4 (80-120): URL and line appear
  // Phase 5 (120-150): Hold + fade out

  // ===== GLITCH INTENSITY (peaks early, calms down, micro-bursts later) =====
  const glitchIntensity = interpolate(
    frame,
    [20, 35, 55, 70, 100, 110, 115, 130],
    [0, 1, 0.8, 0.15, 0.05, 0.4, 0.1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  // ===== LOGO =====
  const logoEntrySpring = spring({
    frame: frame - 20,
    fps,
    config: { damping: 80, stiffness: 120, mass: 1 },
    durationInFrames: 40,
  });
  const logoOpacity = interpolate(logoEntrySpring, [0, 0.5], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logoScale = interpolate(logoEntrySpring, [0, 1], [1.15, 1]);

  // Glitch transforms on the logo
  const glitchX =
    glitchIntensity > 0.05
      ? glitchOffset(frame, "gx", 30 * glitchIntensity)
      : 0;
  const glitchY =
    glitchIntensity > 0.05
      ? glitchOffset(frame, "gy", 12 * glitchIntensity)
      : 0;
  const glitchSkew =
    glitchIntensity > 0.1
      ? glitchOffset(frame, "gskew", 8 * glitchIntensity)
      : 0;
  const glitchScaleX =
    glitchIntensity > 0.1
      ? 1 + glitchOffset(frame, "gscalex", 0.08 * glitchIntensity)
      : 1;

  // RGB split (chromatic aberration) — 3 layers
  const rgbSplitAmount = glitchIntensity * 12;

  // Glitch "slice" bars — horizontal bars that appear during glitch
  const showSlices = glitchIntensity > 0.3;
  const GLITCH_SLICES = Array.from({ length: 6 }, (_, i) => ({
    y: random(`slice-y-${i}-${Math.floor(frame / 2)}`) * 1080,
    height:
      2 +
      random(`slice-h-${i}-${Math.floor(frame / 2)}`) * 20 * glitchIntensity,
    offsetX: glitchOffset(frame, `slice-ox-${i}`, 60 * glitchIntensity),
    color:
      NEON_COLORS[
        Math.floor(
          random(`slice-c-${i}-${Math.floor(frame / 3)}`) * NEON_COLORS.length,
        )
      ],
    opacity: 0.15 + random(`slice-o-${i}-${Math.floor(frame / 2)}`) * 0.3,
  }));

  // ===== NEON GLOW BEHIND LOGO =====
  const glowOpacity = interpolate(
    frame,
    [20, 40, 100, 140, 150],
    [0, 0.15, 0.1, 0.12, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  const glowScale = 1 + Math.sin(frame * 0.08) * 0.05;

  // ===== GREEN ACCENT LINE =====
  const lineProgress = interpolate(frame, [80, 110], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const lineWidth = lineProgress * 200;
  const lineOpacity = interpolate(frame, [80, 92], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== URL TEXT =====
  const urlText = "schoolsWP.com";
  const urlStartFrame = 95;
  const staggerPerChar = 2;

  // ===== PARTICLE EXPLOSION OPACITY =====
  const particleGlobalOpacity = interpolate(
    frame,
    [0, 5, 60, 90],
    [0, 1, 0.6, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  // ===== BACKGROUND FLICKER =====
  const bgFlicker =
    glitchIntensity > 0.4 && isGlitchActive(frame, "bgflick") ? 0.06 : 0;

  // ===== SCANLINES =====
  const scanlinesOpacity = interpolate(
    frame,
    [0, 20, 130, 150],
    [0, 0.04, 0.04, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  // ===== GLOBAL FADE OUT =====
  const globalOpacity = interpolate(frame, [140, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  // ===== SCREEN SHAKE =====
  const shakeX =
    glitchIntensity > 0.3
      ? glitchOffset(frame, "shakex", 6 * glitchIntensity)
      : 0;
  const shakeY =
    glitchIntensity > 0.3
      ? glitchOffset(frame, "shakey", 4 * glitchIntensity)
      : 0;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: THEME.bgDark,
        justifyContent: "center",
        alignItems: "center",
        opacity: globalOpacity,
        overflow: "hidden",
        transform: `translate(${shakeX}px, ${shakeY}px)`,
      }}
    >
      {/* ===== BACKGROUND FLICKER ===== */}
      {bgFlicker > 0 && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            backgroundColor: THEME.primary,
            opacity: bgFlicker,
          }}
        />
      )}

      {/* ===== SCANLINES OVERLAY ===== */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          opacity: scanlinesOpacity,
          backgroundImage:
            "repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.3) 2px, rgba(0,0,0,0.3) 4px)",
          pointerEvents: "none",
        }}
      />

      {/* ===== NEON PARTICLE EXPLOSION (wave 1) ===== */}
      {PARTICLES.map((p, i) => {
        const t = Math.max(0, frame - p.delay);
        if (t <= 0 || t > p.lifetime) return null;

        const progress = t / p.lifetime;
        const deceleration = 1 - progress * 0.6;
        const dist = p.speed * t * deceleration;
        const px = 960 + Math.cos(p.angle) * dist;
        const py = 540 + Math.sin(p.angle) * dist;
        const pOpacity = interpolate(
          progress,
          [0, 0.1, 0.7, 1],
          [0, 1, 0.6, 0],
          {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          },
        );
        const rotation = t * p.rotationSpeed;

        const shapeStyle: React.CSSProperties = {
          position: "absolute",
          left: px - p.size / 2,
          top: py - p.size / 2,
          width: p.size,
          height: p.size,
          backgroundColor: p.color,
          opacity: pOpacity * particleGlobalOpacity,
          boxShadow: `0 0 ${p.size * 2}px ${p.color}, 0 0 ${p.size * 4}px ${p.color}50`,
          transform: `rotate(${rotation}deg)`,
          borderRadius: p.shape === 0 ? "50%" : p.shape === 2 ? "0" : "1px",
          ...(p.shape === 2
            ? { transform: `rotate(${rotation + 45}deg)` }
            : {}),
        };

        return <div key={`p1-${i}`} style={shapeStyle} />;
      })}

      {/* ===== NEON PARTICLE EXPLOSION (wave 2) ===== */}
      {PARTICLES_WAVE2.map((p, i) => {
        const t = Math.max(0, frame - p.delay);
        if (t <= 0 || t > p.lifetime) return null;

        const progress = t / p.lifetime;
        const deceleration = 1 - progress * 0.5;
        const dist = p.speed * t * deceleration;
        const px = 960 + Math.cos(p.angle) * dist;
        const py = 540 + Math.sin(p.angle) * dist;
        const pOpacity = interpolate(
          progress,
          [0, 0.15, 0.6, 1],
          [0, 0.8, 0.4, 0],
          {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          },
        );

        return (
          <div
            key={`p2-${i}`}
            style={{
              position: "absolute",
              left: px - p.size / 2,
              top: py - p.size / 2,
              width: p.size,
              height: p.size,
              borderRadius: p.shape === 0 ? "50%" : "1px",
              backgroundColor: p.color,
              opacity: pOpacity * particleGlobalOpacity,
              boxShadow: `0 0 ${p.size * 3}px ${p.color}`,
              transform: `rotate(${(frame - p.delay) * p.rotationSpeed}deg)`,
            }}
          />
        );
      })}

      {/* ===== NEON GLOW (breathing) ===== */}
      <div
        style={{
          position: "absolute",
          width: 600,
          height: 600,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, ${THEME.accent}30 40%, transparent 70%)`,
          opacity: glowOpacity,
          filter: "blur(100px)",
          transform: `scale(${glowScale})`,
        }}
      />

      {/* ===== GLITCH SLICES (horizontal disruption bars) ===== */}
      {showSlices &&
        GLITCH_SLICES.map((slice, i) => (
          <div
            key={`slice-${i}`}
            style={{
              position: "absolute",
              left: slice.offsetX,
              top: slice.y,
              width: "100%",
              height: slice.height,
              backgroundColor: slice.color,
              opacity: slice.opacity * glitchIntensity,
              mixBlendMode: "screen",
            }}
          />
        ))}

      {/* ===== LOGO — RGB SPLIT (red channel offset) ===== */}
      {rgbSplitAmount > 1 && (
        <Img
          src={staticFile("logos/nom-white.svg")}
          style={{
            position: "absolute",
            width: 440,
            opacity: logoOpacity * 0.5,
            transform: `scale(${logoScale * glitchScaleX}) translate(${glitchX - rgbSplitAmount}px, ${glitchY}px) skewX(${glitchSkew}deg)`,
            filter: "brightness(2) hue-rotate(-60deg)",
            mixBlendMode: "screen",
          }}
        />
      )}

      {/* ===== LOGO — RGB SPLIT (blue channel offset) ===== */}
      {rgbSplitAmount > 1 && (
        <Img
          src={staticFile("logos/nom-white.svg")}
          style={{
            position: "absolute",
            width: 440,
            opacity: logoOpacity * 0.5,
            transform: `scale(${logoScale * glitchScaleX}) translate(${glitchX + rgbSplitAmount}px, ${glitchY}px) skewX(${glitchSkew}deg)`,
            filter: "brightness(2) hue-rotate(180deg)",
            mixBlendMode: "screen",
          }}
        />
      )}

      {/* ===== LOGO — MAIN (green/white) ===== */}
      <Img
        src={staticFile("logos/nom-white.svg")}
        style={{
          width: 440,
          opacity: logoOpacity,
          transform: `scale(${logoScale * glitchScaleX}) translate(${glitchX}px, ${glitchY}px) skewX(${glitchSkew}deg)`,
          zIndex: 10,
        }}
      />

      {/* ===== GREEN ACCENT LINE (eased) ===== */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 52,
          width: lineWidth,
          height: 2,
          backgroundColor: THEME.primary,
          opacity: lineOpacity,
          boxShadow: `0 0 10px ${THEME.primary}80, 0 0 20px ${THEME.primary}30`,
          zIndex: 10,
        }}
      />

      {/* ===== STAGGERED URL REVEAL ===== */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 74,
          display: "flex",
          fontFamily: THEME.headingFont,
          fontSize: 18,
          letterSpacing: 3,
          zIndex: 10,
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
          const charY = interpolate(charSpring, [0, 1], [14, 0]);

          // Occasional neon glow on individual characters
          const charGlow =
            frame > charFrame + 10 &&
            random(`charglow-${i}-${Math.floor(frame / 8)}`) > 0.85
              ? `0 0 8px ${NEON_COLORS[i % NEON_COLORS.length]}`
              : "none";

          return (
            <span
              key={i}
              style={{
                opacity: charOpacity,
                transform: `translateY(${charY}px)`,
                color: THEME.textWhite,
                display: "inline-block",
                textShadow: charGlow,
              }}
            >
              {char}
            </span>
          );
        })}
      </div>

      {/* ===== NOISE / STATIC OVERLAY ===== */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          opacity: interpolate(
            glitchIntensity,
            [0, 0.2, 1],
            [0.01, 0.03, 0.08],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
          ),
          backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' seed='${Math.floor(frame * 3)}' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.6'/%3E%3C/svg%3E")`,
          backgroundSize: "256px 256px",
          mixBlendMode: "overlay",
          pointerEvents: "none",
        }}
      />

      {/* ===== VIGNETTE ===== */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.5) 100%)",
          pointerEvents: "none",
        }}
      />
    </AbsoluteFill>
  );
};
