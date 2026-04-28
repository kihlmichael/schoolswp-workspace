import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";
import { THEME } from "../theme";

export const BrandIntro: React.FC = () => {
  const frame = useCurrentFrame();

  // Logo fade in + scale (frames 20-70)
  const logoOpacity = interpolate(frame, [20, 70], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logoScale = interpolate(frame, [20, 70], [0.9, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Tagline fade in (frames 60-100)
  const textOpacity = interpolate(frame, [60, 100], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const textY = interpolate(frame, [60, 100], [15, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Subtle green glow pulse
  const glowOpacity = interpolate(
    frame,
    [40, 80, 110, 150],
    [0, 0.12, 0.08, 0.12],
    { extrapolateRight: "extend" },
  );

  // Accent line expand (frames 80-120)
  const lineWidth = interpolate(frame, [80, 120], [0, 220], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#1a1a2e",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      {/* Subtle radial glow behind logo */}
      <div
        style={{
          position: "absolute",
          width: 600,
          height: 600,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 70%)`,
          opacity: glowOpacity,
          filter: "blur(100px)",
        }}
      />

      {/* Logo + Nom White (V1.1) */}
      <Img
        src={staticFile("logos/nom-white.svg")}
        style={{
          width: 500,
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
        }}
      />

      {/* Tagline */}
      <div
        style={{
          position: "absolute",
          bottom: 240,
          opacity: textOpacity,
          transform: `translateY(${textY}px)`,
          fontFamily: THEME.headingFont,
          fontSize: 24,
          color: "#6CB4EE",
          letterSpacing: 4,
          textTransform: "uppercase",
        }}
      >
        WordPress · SEO · Automatisation
      </div>

      {/* Accent line */}
      <div
        style={{
          position: "absolute",
          bottom: 220,
          width: lineWidth,
          height: 2,
          backgroundColor: THEME.primary,
        }}
      />
    </AbsoluteFill>
  );
};
