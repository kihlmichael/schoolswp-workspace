import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { THEME } from "../theme";

export const Scene1Background: React.FC = () => {
  const frame = useCurrentFrame();

  // Background fade-in over first 60 frames (2s)
  const bgOpacity = interpolate(frame, [0, 60], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Subtle parallax on the grid (very slow vertical drift)
  const gridOffsetY = interpolate(frame, [0, THEME.totalFrames], [0, -30]);

  // Grid line opacity fades in slightly later
  const gridOpacity = interpolate(frame, [20, 80], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill>
      {/* Gradient background */}
      <AbsoluteFill
        style={{
          opacity: bgOpacity,
          background: `linear-gradient(180deg, ${THEME.background} 0%, ${THEME.backgroundGradient} 100%)`,
        }}
      />

      {/* Subtle grid */}
      <AbsoluteFill
        style={{
          opacity: gridOpacity * bgOpacity,
          transform: `translateY(${gridOffsetY}px)`,
        }}
      >
        <svg width="100%" height="120%" style={{ position: "absolute", top: -40 }}>
          <defs>
            <pattern id="grid" width="80" height="80" patternUnits="userSpaceOnUse">
              <path
                d="M 80 0 L 0 0 0 80"
                fill="none"
                stroke={THEME.gridColor}
                strokeWidth="1"
              />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#grid)" />
        </svg>
      </AbsoluteFill>

      {/* Center dot accent (repere graphique minimal) */}
      <AbsoluteFill
        style={{
          opacity: interpolate(frame, [30, 70], [0, 0.15], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          }),
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div
          style={{
            width: 6,
            height: 6,
            borderRadius: "50%",
            backgroundColor: THEME.accent,
          }}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
