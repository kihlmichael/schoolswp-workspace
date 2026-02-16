import React from "react";
import { AbsoluteFill } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { THEME, TEXT } from "../theme";

export const Scene3Message: React.FC = () => {
  // Inside <Sequence from={msgIn}>, so useCurrentFrame() starts at 0.

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        paddingTop: 120,
      }}
    >
      {/* Pre-title */}
      <AnimatedText
        text={TEXT.preTitle}
        fontSize={THEME.fontSizePreTitle}
        color={THEME.textSecondary}
        delay={0}
        style={{ fontWeight: 400, marginBottom: 12 }}
      />

      {/* Headline */}
      <AnimatedText
        text={TEXT.headline}
        accentPhrase={TEXT.accentPhrase}
        fontSize={THEME.fontSizeHero}
        color={THEME.textPrimary}
        delay={10}
      />

      {/* Subtitle */}
      <AnimatedText
        text={TEXT.subtitle}
        fontSize={THEME.fontSizeSubtitle}
        color={THEME.textSecondary}
        delay={25}
        style={{ fontWeight: 400, marginTop: 24, letterSpacing: 4 }}
      />
    </AbsoluteFill>
  );
};
