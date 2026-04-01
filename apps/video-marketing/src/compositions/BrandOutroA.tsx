import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";
import { THEME } from "../theme";

export const BrandOutroA: React.FC = () => {
  const frame = useCurrentFrame();

  // === Background transition: light → dark (3.0s-4.0s / frames 90-120) ===
  const bgProgress = interpolate(frame, [90, 120], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 1: Green line traces path (0.0s-2.0s / frames 0-60) ===
  // Line enters from left, curves to center
  const lineProgress = interpolate(frame, [5, 60], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const lineOpacity = interpolate(frame, [5, 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 2: Logo fade in (2.0s-3.0s / frames 60-90) ===
  const logoOpacity = interpolate(frame, [60, 90], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logoScale = interpolate(frame, [60, 90], [0.93, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 3: Slogan fade in (3.0s-4.0s / frames 90-120) ===
  const sloganOpacity = interpolate(frame, [100, 125], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const sloganY = interpolate(frame, [100, 125], [12, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // === PHASE 4: Hold + fade out (4.0s-5.0s / frames 120-150) ===
  const linePulse = interpolate(frame, [120, 135, 150], [0.8, 1, 0.8], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const globalOpacity = interpolate(frame, [140, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Determine which logo to show based on background
  const useWhiteLogo = bgProgress > 0.5;

  // SVG path for the flowing line
  const pathLength = 800;
  const dashOffset = interpolate(frame, [5, 60], [pathLength, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: interpolateColor(bgProgress),
        justifyContent: "center",
        alignItems: "center",
        opacity: globalOpacity,
      }}
    >
      {/* Animated green line path */}
      <svg
        width="1920"
        height="1080"
        viewBox="0 0 1920 1080"
        style={{
          position: "absolute",
          opacity: lineOpacity * linePulse,
        }}
      >
        <path
          d="M -100,540 Q 400,300 600,540 Q 800,780 960,540"
          fill="none"
          stroke={THEME.primary}
          strokeWidth="2.5"
          strokeDasharray={pathLength}
          strokeDashoffset={dashOffset}
          strokeLinecap="round"
        />
      </svg>

      {/* Underline beneath logo (converged line) */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 48,
          width: interpolate(frame, [50, 75], [0, 160], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          }),
          height: 2,
          backgroundColor: THEME.primary,
          opacity: lineOpacity * linePulse,
        }}
      />

      {/* Logo — switches from black to white during bg transition */}
      <Img
        src={staticFile(
          useWhiteLogo ? "logos/nom-white.svg" : "logos/nom-black.svg",
        )}
        style={{
          width: 420,
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
        }}
      />

      {/* Slogan */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          marginTop: 75,
          opacity: sloganOpacity,
          transform: `translateY(${sloganY}px)`,
          fontFamily: THEME.bodyFont,
          fontSize: 20,
          fontStyle: "italic",
          color: useWhiteLogo ? THEME.textWhite : THEME.textPrimary,
          letterSpacing: 1,
        }}
      >
        WordPress peut travailler pour toi.
      </div>
    </AbsoluteFill>
  );
};

// Helper: interpolate between light and dark background
function interpolateColor(progress: number): string {
  const r = Math.round(250 - progress * (250 - 18));
  const g = Math.round(251 - progress * (251 - 17));
  const b = Math.round(253 - progress * (253 - 31));
  return `rgb(${r},${g},${b})`;
}
