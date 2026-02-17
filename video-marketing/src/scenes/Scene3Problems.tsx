import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { ProblemCard } from "../components/ProblemCard";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene3Problems: React.FC = () => {
  const frame = useCurrentFrame();

  // Scene fade-in (from light to dark)
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
        backgroundColor: THEME.bgDark,
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
            text="Tu reconnais ces problèmes ?"
            fontSize={THEME.fontSizeH2}
            color={THEME.textWhite}
            delay={0}
            heading
          />
        </div>

        {/* Problem cards — staggered */}
        {TEXTS.problems.map((problem, i) => (
          <ProblemCard
            key={i}
            icon={problem.icon}
            title={problem.title}
            desc={problem.desc}
            index={i}
          />
        ))}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
