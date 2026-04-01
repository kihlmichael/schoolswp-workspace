import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  random,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { THEME } from "../theme";

// Grid dots pattern
const GRID_COLS = 24;
const GRID_ROWS = 14;
const GRID_DOTS = Array.from({ length: GRID_COLS * GRID_ROWS }, (_, i) => ({
  col: i % GRID_COLS,
  row: Math.floor(i / GRID_COLS),
  delay: random(`grid-${i}`) * 20,
}));

// Floating particles
const PARTICLES = Array.from({ length: 20 }, (_, i) => ({
  x: random(`px-${i}`) * 1920,
  y: random(`py-${i}`) * 1080,
  size: 1.5 + random(`ps-${i}`) * 2.5,
  speedX: (random(`psx-${i}`) - 0.5) * 0.8,
  speedY: (random(`psy-${i}`) - 0.5) * 0.6,
  delay: random(`pd-${i}`) * 40,
}));

export const BrandOutroCPro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // ===== GRID BACKGROUND: dots fade in with stagger =====
  const gridGlobalOpacity = interpolate(
    frame,
    [0, 30, 130, 150],
    [0, 0.06, 0.06, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  // ===== NOISE TEXTURE OVERLAY =====
  const noiseOpacity = interpolate(frame, [0, 20], [0, 0.03], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== SIGNAL PULSE (spring-driven) =====
  const pulseSpring = spring({
    frame: frame - 15,
    fps,
    config: { damping: 30, stiffness: 40, mass: 1.5 },
    durationInFrames: 40,
  });
  const pulseScale = interpolate(pulseSpring, [0, 1], [0, 10]);
  const pulseOpacity = interpolate(pulseSpring, [0, 0.3, 1], [0, 0.3, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Second pulse (delayed, lighter)
  const pulse2Spring = spring({
    frame: frame - 22,
    fps,
    config: { damping: 25, stiffness: 35, mass: 1.8 },
    durationInFrames: 45,
  });
  const pulse2Scale = interpolate(pulse2Spring, [0, 1], [0, 7]);
  const pulse2Opacity = interpolate(pulse2Spring, [0, 0.3, 1], [0, 0.18, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Third micro pulse
  const pulse3Spring = spring({
    frame: frame - 28,
    fps,
    config: { damping: 20, stiffness: 30, mass: 2 },
    durationInFrames: 50,
  });
  const pulse3Scale = interpolate(pulse3Spring, [0, 1], [0, 5]);
  const pulse3Opacity = interpolate(pulse3Spring, [0, 0.2, 1], [0, 0.1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== LOGO: spring entrance =====
  const logoSpring = spring({
    frame: frame - 36,
    fps,
    config: { damping: 200, stiffness: 100 },
    durationInFrames: 35,
  });
  const logoScale = interpolate(logoSpring, [0, 1], [0.88, 1]);
  const logoOpacity = logoSpring;

  // ===== GREEN ACCENT LINE: eased expansion =====
  const lineProgress = interpolate(frame, [66, 100], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const lineWidth = lineProgress * 200;
  const lineOpacity = interpolate(frame, [66, 78], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== STAGGERED TEXT REVEAL: "schoolsWP.com" letter by letter =====
  const urlText = "schoolsWP.com";
  const urlStartFrame = 88;
  const staggerPerChar = 2;

  // ===== GLOW: breathing effect =====
  const glowBase = interpolate(frame, [36, 66], [0, 0.08], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const glowBreath = Math.sin(frame * 0.06) * 0.03;
  const glowOpacity = Math.max(0, glowBase + glowBreath);

  // ===== GLOBAL FADE OUT =====
  const globalOpacity = interpolate(frame, [140, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  // ===== FLOATING PARTICLES =====
  const particleGlobalOpacity = interpolate(
    frame,
    [10, 30, 130, 150],
    [0, 0.4, 0.4, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

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
      {/* ===== GRID DOTS BACKGROUND ===== */}
      <div
        style={{ position: "absolute", inset: 0, opacity: gridGlobalOpacity }}
      >
        {GRID_DOTS.map((dot, i) => {
          const dotOpacity = interpolate(
            frame,
            [dot.delay, dot.delay + 15],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
          );
          const cx = (dot.col + 0.5) * (1920 / GRID_COLS);
          const cy = (dot.row + 0.5) * (1080 / GRID_ROWS);
          // Distance from center for radial reveal
          const dist = Math.sqrt((cx - 960) ** 2 + (cy - 540) ** 2);
          const maxDist = 800;
          const radialDelay = (dist / maxDist) * 25;
          const radialOpacity = interpolate(
            frame,
            [15 + radialDelay, 30 + radialDelay],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
          );

          return (
            <div
              key={i}
              style={{
                position: "absolute",
                left: cx,
                top: cy,
                width: 2,
                height: 2,
                borderRadius: "50%",
                backgroundColor: THEME.primary,
                opacity: dotOpacity * radialOpacity,
              }}
            />
          );
        })}
      </div>

      {/* ===== NOISE TEXTURE ===== */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          opacity: noiseOpacity,
          backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/%3E%3C/svg%3E")`,
          backgroundSize: "256px 256px",
          mixBlendMode: "overlay",
        }}
      />

      {/* ===== FLOATING PARTICLES ===== */}
      {PARTICLES.map((p, i) => {
        const px = p.x + p.speedX * frame;
        const py = p.y + p.speedY * frame;
        const pOpacity = interpolate(
          frame,
          [p.delay, p.delay + 20],
          [0, 0.5 + random(`po-${i}`) * 0.5],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
        );

        return (
          <div
            key={`p-${i}`}
            style={{
              position: "absolute",
              left: ((px % 1920) + 1920) % 1920,
              top: ((py % 1080) + 1080) % 1080,
              width: p.size,
              height: p.size,
              borderRadius: "50%",
              backgroundColor: THEME.primary,
              opacity: pOpacity * particleGlobalOpacity,
              filter: "blur(0.5px)",
            }}
          />
        );
      })}

      {/* ===== PULSE RINGS (spring-driven) ===== */}
      <div
        style={{
          position: "absolute",
          width: 80,
          height: 80,
          borderRadius: "50%",
          border: `2px solid ${THEME.primary}`,
          opacity: pulseOpacity,
          transform: `scale(${pulseScale})`,
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 80,
          height: 80,
          borderRadius: "50%",
          border: `1.5px solid ${THEME.primary}`,
          opacity: pulse2Opacity,
          transform: `scale(${pulse2Scale})`,
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 80,
          height: 80,
          borderRadius: "50%",
          border: `1px solid ${THEME.primary}`,
          opacity: pulse3Opacity,
          transform: `scale(${pulse3Scale})`,
        }}
      />

      {/* ===== GLOW (breathing) ===== */}
      <div
        style={{
          position: "absolute",
          width: 500,
          height: 500,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 65%)`,
          opacity: glowOpacity,
          filter: "blur(90px)",
        }}
      />

      {/* ===== LOGO (spring entrance) ===== */}
      <Img
        src={staticFile("logos/nom-white.svg")}
        style={{
          width: 440,
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
        }}
      />

      {/* ===== GREEN ACCENT LINE (eased) ===== */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 50,
          width: lineWidth,
          height: 2,
          backgroundColor: THEME.primary,
          opacity: lineOpacity,
          boxShadow: `0 0 8px ${THEME.primary}40`,
        }}
      />

      {/* ===== STAGGERED URL REVEAL ===== */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 72,
          display: "flex",
          fontFamily: THEME.headingFont,
          fontSize: 18,
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
