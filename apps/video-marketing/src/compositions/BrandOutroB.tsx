import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  random,
} from "remotion";
import { THEME } from "../theme";

// Generate stable particle positions
const PARTICLES = Array.from({ length: 30 }, (_, i) => ({
  x: random(`x-${i}`) * 1920,
  y: random(`y-${i}`) * 1080,
  size: 2 + random(`s-${i}`) * 4,
  speed: 0.5 + random(`sp-${i}`) * 1.5,
  delay: random(`d-${i}`) * 30,
}));

export const BrandOutroB: React.FC = () => {
  const frame = useCurrentFrame();

  // === PHASE 1: Particles drift toward center (0.0s-2.5s / frames 0-75) ===
  const particleConverge = interpolate(frame, [0, 75], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const particleGlobalOpacity = interpolate(
    frame,
    [0, 15, 65, 80],
    [0, 0.6, 0.6, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  // === PHASE 2: Condensation flash (1.5s-2.5s / frames 45-75) ===
  const flashOpacity = interpolate(frame, [70, 75, 80], [0, 0.2, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 3: Logo scale-in (2.5s-3.5s / frames 75-105) ===
  const logoOpacity = interpolate(frame, [75, 105], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logoScale = interpolate(frame, [75, 105], [0.95, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 4: Slogan (3.5s-4.5s / frames 105-135) ===
  const sloganOpacity = interpolate(frame, [105, 130], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const sloganY = interpolate(frame, [105, 130], [10, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 5: URL + line (4.0s-5.0s / frames 120-150) ===
  const urlOpacity = interpolate(frame, [120, 140], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const lineWidth = interpolate(frame, [115, 140], [0, 160], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === Global fade out ===
  const globalOpacity = interpolate(frame, [170, 180], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Glow behind logo
  const glowOpacity = interpolate(
    frame,
    [75, 105, 150, 165, 180],
    [0, 0.1, 0.1, 0.14, 0.1],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  const centerX = 960;
  const centerY = 500;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: THEME.bgDark,
        justifyContent: "center",
        alignItems: "center",
        opacity: globalOpacity,
      }}
    >
      {/* Particles converging */}
      {PARTICLES.map((p, i) => {
        const progress = interpolate(frame, [p.delay, 75], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        const px = p.x + (centerX - p.x) * progress;
        const py = p.y + (centerY - p.y) * progress;
        const pOpacity = particleGlobalOpacity * (1 - progress * 0.5);

        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: px,
              top: py,
              width: p.size,
              height: p.size,
              borderRadius: "50%",
              backgroundColor: THEME.primary,
              opacity: pOpacity,
              filter: "blur(1px)",
            }}
          />
        );
      })}

      {/* Flash at condensation */}
      <div
        style={{
          position: "absolute",
          width: 300,
          height: 300,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 70%)`,
          opacity: flashOpacity,
          filter: "blur(40px)",
        }}
      />

      {/* Glow behind logo */}
      <div
        style={{
          position: "absolute",
          width: 500,
          height: 500,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 70%)`,
          opacity: glowOpacity,
          filter: "blur(90px)",
        }}
      />

      {/* Logo white */}
      <Img
        src={staticFile("logos/nom-white.svg")}
        style={{
          width: 420,
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
        }}
      />

      {/* Green accent line */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 50,
          width: lineWidth,
          height: 2,
          backgroundColor: THEME.primary,
        }}
      />

      {/* Slogan */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 65,
          opacity: sloganOpacity,
          transform: `translateY(${sloganY}px)`,
          fontFamily: THEME.bodyFont,
          fontSize: 19,
          fontStyle: "italic",
          color: THEME.textWhite,
          letterSpacing: 1,
        }}
      >
        La clarté bat toujours la complexité.
      </div>

      {/* URL */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 100,
          opacity: urlOpacity,
          fontFamily: THEME.headingFont,
          fontSize: 16,
          color: THEME.textWhite,
          letterSpacing: 4,
          textTransform: "lowercase",
        }}
      >
        schoolsWP.com
      </div>
    </AbsoluteFill>
  );
};
