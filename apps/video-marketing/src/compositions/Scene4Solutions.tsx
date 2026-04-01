import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { SolutionBlock } from "../components/SolutionBlock";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene4Solutions: React.FC = () => {
  const frame = useCurrentFrame();

  // Scene fade-in
  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Scene fade-out
  const fadeOut = interpolate(frame, [990, 1050], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        opacity: fadeIn * fadeOut,
        backgroundColor: THEME.bgLight,
      }}
    >
      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          gap: 20,
          padding: "0 200px",
        }}
      >
        {/* Section title */}
        <div style={{ marginBottom: 24 }}>
          <AnimatedText
            text="schoolsWP résout ça, étape par étape."
            fontSize={THEME.fontSizeH2}
            color={THEME.textPrimary}
            delay={0}
            heading
            accentPhrase="étape par étape"
          />
        </div>

        {/* Solution blocks — staggered */}
        {TEXTS.solutions.map((solution, i) => (
          <SolutionBlock
            key={i}
            title={solution.title}
            desc={solution.desc}
            index={i}
          />
        ))}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
