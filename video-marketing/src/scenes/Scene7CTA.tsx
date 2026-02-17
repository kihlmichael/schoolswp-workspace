import React from "react";
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { CTAButton } from "../components/CTAButton";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene7CTA: React.FC = () => {
  const frame = useCurrentFrame();

  // Scene fade-in
  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Final fade-out to black
  const fadeOut = interpolate(frame, [390, 450], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ opacity: fadeIn * fadeOut }}>
      {/* Green background */}
      <AbsoluteFill style={{ backgroundColor: THEME.primary }} />

      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          gap: 40,
        }}
      >
        {/* Headline */}
        <AnimatedText
          text={TEXTS.cta.headline}
          fontSize={THEME.fontSizeHero}
          color={THEME.textWhite}
          delay={0}
          heading
          style={{ maxWidth: 1200 }}
        />

        {/* CTA Button */}
        <CTAButton text={TEXTS.cta.button} delay={60} />

        {/* URL */}
        <AnimatedText
          text={TEXTS.cta.url}
          fontSize={THEME.fontSizeCaption}
          color="rgba(255, 255, 255, 0.7)"
          delay={90}
          style={{ letterSpacing: 2 }}
        />

        {/* Bottom: logo + tagline */}
        <div
          style={{
            position: "absolute",
            bottom: 60,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          <Img
            src={staticFile("logo-schoolswp.svg")}
            style={{ width: 60, height: 60, opacity: 0.8 }}
          />
          <AnimatedText
            text={TEXTS.cta.tagline}
            fontSize={THEME.fontSizeSmall}
            color="rgba(255, 255, 255, 0.6)"
            delay={120}
            style={{ letterSpacing: 3, textTransform: "uppercase" }}
          />
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
