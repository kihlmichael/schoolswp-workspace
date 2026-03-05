import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { BeforeAfter } from "../components/BeforeAfter";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene5Benefits: React.FC = () => {
  const frame = useCurrentFrame();

  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const fadeOut = interpolate(frame, [540, 600], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        opacity: fadeIn * fadeOut,
        backgroundColor: THEME.bgSubtle,
      }}
    >
      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          gap: 40,
        }}
      >
        <BeforeAfter
          beforeTitle={TEXTS.benefits.before.title}
          afterTitle={TEXTS.benefits.after.title}
          beforeItems={TEXTS.benefits.before.items}
          afterItems={TEXTS.benefits.after.items}
        />

        {/* Punchline */}
        <AnimatedText
          text={TEXTS.benefits.punchline}
          fontSize={THEME.fontSizeH2}
          color={THEME.primary}
          delay={200}
          heading
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
