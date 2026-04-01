import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";
import { THEME } from "../theme";

export const BrandOutroC: React.FC = () => {
  const frame = useCurrentFrame();
  const fps = THEME.fps; // 30

  // === PHASE 1: Signal pulse (0.5s-1.5s / frames 15-45) ===
  const pulseScale = interpolate(frame, [15, 45], [0, 8], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const pulseOpacity = interpolate(frame, [15, 45], [0.25, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Second pulse ring (delayed)
  const pulse2Scale = interpolate(frame, [22, 52], [0, 6], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const pulse2Opacity = interpolate(frame, [22, 52], [0.15, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 2: Logo fade in (1.2s-2.2s / frames 36-66) ===
  const logoOpacity = interpolate(frame, [36, 66], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logoScale = interpolate(frame, [36, 66], [0.92, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 3: Green accent line (2.2s-3.2s / frames 66-96) ===
  const lineWidth = interpolate(frame, [66, 96], [0, 180], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const lineOpacity = interpolate(frame, [66, 80], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 4: URL fade in (3.0s-4.0s / frames 90-120) ===
  const urlOpacity = interpolate(frame, [90, 120], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const urlY = interpolate(frame, [90, 120], [10, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 5: Hold + micro glow (4.0s-5.0s / frames 120-150) ===
  const glowOpacity = interpolate(
    frame,
    [36, 66, 120, 135, 150],
    [0, 0.08, 0.08, 0.12, 0.08],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  // === Global fade out (last 10 frames) ===
  const globalOpacity = interpolate(frame, [140, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: THEME.bgDark,
        justifyContent: "center",
        alignItems: "center",
        opacity: globalOpacity,
      }}
    >
      {/* Pulse ring 1 */}
      <div
        style={{
          position: "absolute",
          width: 100,
          height: 100,
          borderRadius: "50%",
          border: `2px solid ${THEME.primary}`,
          opacity: pulseOpacity,
          transform: `scale(${pulseScale})`,
        }}
      />

      {/* Pulse ring 2 (delayed) */}
      <div
        style={{
          position: "absolute",
          width: 100,
          height: 100,
          borderRadius: "50%",
          border: `1px solid ${THEME.primary}`,
          opacity: pulse2Opacity,
          transform: `scale(${pulse2Scale})`,
        }}
      />

      {/* Micro glow behind logo */}
      <div
        style={{
          position: "absolute",
          width: 400,
          height: 400,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 70%)`,
          opacity: glowOpacity,
          filter: "blur(80px)",
        }}
      />

      {/* Logo schoolsWP white */}
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
          opacity: lineOpacity,
        }}
      />

      {/* URL */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 72,
          opacity: urlOpacity,
          transform: `translateY(${urlY}px)`,
          fontFamily: THEME.headingFont,
          fontSize: 18,
          color: THEME.textWhite,
          letterSpacing: 4,
          textTransform: "none",
        }}
      >
        schoolsWP.com
      </div>
    </AbsoluteFill>
  );
};
