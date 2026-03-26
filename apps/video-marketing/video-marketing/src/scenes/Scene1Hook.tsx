import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene1Hook: React.FC = () => {
  const frame = useCurrentFrame();

  // Background fade-in
  const bgOpacity = interpolate(frame, [0, 40], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Subtle grid (same pattern as brand-reveal)
  const gridOffsetY = interpolate(frame, [0, 600], [0, -20]);
  const gridOpacity = interpolate(frame, [20, 60], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Scene fade-out
  const fadeOut = interpolate(frame, [540, 600], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      {/* Light background with grid */}
      <AbsoluteFill
        style={{
          opacity: bgOpacity,
          background: `linear-gradient(180deg, ${THEME.bgLight} 0%, ${THEME.bgSubtle} 100%)`,
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
            <pattern id="gridHook" width="80" height="80" patternUnits="userSpaceOnUse">
              <path
                d="M 80 0 L 0 0 0 80"
                fill="none"
                stroke={THEME.gridColorLight}
                strokeWidth="1"
              />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#gridHook)" />
        </svg>
      </AbsoluteFill>

      {/* Text content */}
      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          padding: "0 200px",
          gap: 8,
        }}
      >
        {TEXTS.hook.lines.map((line, i) => (
          <AnimatedText
            key={i}
            text={line}
            fontSize={THEME.fontSizeH2}
            color={THEME.textPrimary}
            delay={i * 60}
            heading
            style={{ fontWeight: 400 }}
          />
        ))}

        {/* Punchline — appears last, in accent green */}
        <div style={{ marginTop: 40 }}>
          <AnimatedText
            text={TEXTS.hook.punchline}
            fontSize={THEME.fontSizeH2}
            color={THEME.primary}
            delay={300}
            heading
          />
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
