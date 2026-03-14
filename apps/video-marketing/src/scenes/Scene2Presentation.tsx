import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene2Presentation: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Scene fade-in
  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Scene fade-out
  const fadeOut = interpolate(frame, [690, 750], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Logo entrance
  const logoSpring = spring({ fps, frame, config: THEME.springSmooth });
  const logoScale = interpolate(logoSpring, [0, 1], [0.85, 1]);
  const logoOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Keywords staggered entrance
  const keywordBaseDelay = 180;

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
          gap: 24,
        }}
      >
        {/* Logo */}
        <div
          style={{
            opacity: logoOpacity,
            transform: `scale(${logoScale})`,
            marginBottom: 16,
          }}
        >
          <Img
            src={staticFile("logo-schoolswp.svg")}
            style={{ width: 200, height: 200 }}
          />
        </div>

        {/* Tagline */}
        <AnimatedText
          text={TEXTS.presentation.tagline}
          fontSize={THEME.fontSizeCaption}
          color={THEME.textSecondary}
          delay={40}
          style={{ letterSpacing: 3, textTransform: "uppercase" }}
        />

        {/* Headline */}
        <AnimatedText
          text={TEXTS.presentation.headline}
          fontSize={THEME.fontSizeHero}
          color={THEME.textPrimary}
          delay={80}
          heading
        />

        {/* Keywords row */}
        <div
          style={{
            display: "flex",
            gap: 40,
            marginTop: 24,
          }}
        >
          {TEXTS.presentation.keywords.map((kw, i) => (
            <AnimatedText
              key={i}
              text={kw}
              fontSize={THEME.fontSizeH3}
              color={THEME.primary}
              delay={keywordBaseDelay + i * 30}
              heading
              style={{
                padding: "12px 32px",
                borderRadius: 12,
                backgroundColor: THEME.greenSubtle,
              }}
            />
          ))}
        </div>

        {/* Subtitle */}
        <AnimatedText
          text={TEXTS.presentation.subtitle}
          fontSize={THEME.fontSizeBody}
          color={THEME.textSecondary}
          delay={300}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
