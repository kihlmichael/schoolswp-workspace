import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { TimelineBadge } from "../components/TimelineBadge";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene6Credibility: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const fadeOut = interpolate(frame, [540, 600], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Founder name entrance
  const founderSpring = spring({ fps, frame, config: THEME.springSmooth });
  const founderOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const founderScale = interpolate(founderSpring, [0, 1], [0.95, 1]);

  // Ecosystem items entrance
  const ecoDelay = 240;

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
          gap: 32,
        }}
      >
        {/* Founder avatar placeholder + name */}
        <div
          style={{
            opacity: founderOpacity,
            transform: `scale(${founderScale})`,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          {/* Avatar placeholder */}
          <div
            style={{
              width: 100,
              height: 100,
              borderRadius: "50%",
              backgroundColor: THEME.primary,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <span
              style={{
                fontFamily: THEME.headingFont,
                fontSize: 40,
                fontWeight: 700,
                color: THEME.textWhite,
              }}
            >
              MK
            </span>
          </div>
          <div
            style={{
              fontFamily: THEME.headingFont,
              fontSize: THEME.fontSizeH3,
              fontWeight: 700,
              color: THEME.textPrimary,
              textAlign: "center",
            }}
          >
            {TEXTS.credibility.founder}
          </div>
          <div
            style={{
              fontFamily: THEME.bodyFont,
              fontSize: THEME.fontSizeCaption,
              fontWeight: 400,
              color: THEME.textSecondary,
            }}
          >
            {TEXTS.credibility.founderTitle}
          </div>
        </div>

        {/* Timeline badges */}
        <div style={{ display: "flex", gap: 24, marginTop: 16 }}>
          {TEXTS.credibility.badges.map((badge, i) => (
            <TimelineBadge
              key={i}
              value={badge.value}
              label={badge.label}
              index={i}
            />
          ))}
        </div>

        {/* Ecosystem row */}
        <div style={{ display: "flex", gap: 16, marginTop: 8 }}>
          {TEXTS.credibility.ecosystemItems.map((item, i) => (
            <AnimatedText
              key={i}
              text={item}
              fontSize={THEME.fontSizeSmall}
              color={THEME.textSecondary}
              delay={ecoDelay + i * 20}
              style={{
                padding: "8px 20px",
                borderRadius: 20,
                border: `1px solid ${THEME.textLight}`,
              }}
            />
          ))}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
