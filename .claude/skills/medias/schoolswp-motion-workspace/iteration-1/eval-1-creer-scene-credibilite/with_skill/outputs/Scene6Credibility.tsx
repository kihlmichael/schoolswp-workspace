import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { AnimatedText } from "../components/AnimatedText";
import { TimelineBadge } from "../components/TimelineBadge";
import { THEME } from "../theme";
import { TEXTS } from "../texts";

export const Scene6Credibility: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // --- Scene fade-in / fade-out ---
  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(frame, [540, 600], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // --- Accent line (horizontal expansion from center) ---
  const lineSpring = spring({
    fps,
    frame,
    config: THEME.springSmooth,
  });
  const lineWidth = interpolate(lineSpring, [0, 1], [0, 120]);

  // --- Ecosystem items stagger ---
  const ecosystemBaseDelay = 300; // 10s into scene

  // --- Ecosystem label pulse (subtle breathing) ---
  const pulseOpacity = interpolate(
    Math.sin((frame - ecosystemBaseDelay) * 0.08),
    [-1, 1],
    [0.6, 1],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

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
          padding: "0 160px",
        }}
      >
        {/* --- TOP SECTION: Founder --- */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 8,
            marginBottom: 16,
          }}
        >
          <AnimatedText
            text={TEXTS.credibility.founder}
            fontSize={THEME.fontSizeH2}
            color={THEME.textPrimary}
            delay={0}
            heading
          />
          <AnimatedText
            text={TEXTS.credibility.founderTitle}
            fontSize={THEME.fontSizeBody}
            color={THEME.textSecondary}
            delay={20}
          />
        </div>

        {/* --- Accent line --- */}
        <div
          style={{
            width: lineWidth,
            height: 3,
            backgroundColor: THEME.primary,
            borderRadius: 2,
            marginTop: 16,
            marginBottom: 32,
          }}
        />

        {/* --- MIDDLE SECTION: Badges row --- */}
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: 40,
            marginBottom: 48,
          }}
        >
          {TEXTS.credibility.badges.map((badge, i) => (
            <TimelineBadge
              key={i}
              value={badge.value}
              label={badge.label}
              index={i}
            />
          ))}
        </div>

        {/* --- BOTTOM SECTION: Ecosystem --- */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 20,
          }}
        >
          {/* Ecosystem label */}
          <AnimatedText
            text={TEXTS.credibility.ecosystemTitle}
            fontSize={THEME.fontSizeH3}
            color={THEME.textPrimary}
            delay={ecosystemBaseDelay - 30}
            heading
            accentPhrase="schoolsWP"
          />

          {/* Ecosystem items row */}
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              gap: 32,
              opacity: frame > ecosystemBaseDelay ? pulseOpacity : 0,
            }}
          >
            {TEXTS.credibility.ecosystemItems.map((item, i) => {
              const itemDelay = ecosystemBaseDelay + i * THEME.staggerDelay;
              const itemDelayedFrame = Math.max(0, frame - itemDelay);

              const itemSpring = spring({
                fps,
                frame: itemDelayedFrame,
                config: THEME.springGentle,
              });

              const itemOpacity = interpolate(
                itemDelayedFrame,
                [0, THEME.fadeInDuration],
                [0, 1],
                {
                  extrapolateLeft: "clamp",
                  extrapolateRight: "clamp",
                },
              );

              const itemTranslateY = interpolate(itemSpring, [0, 1], [30, 0]);

              return (
                <div
                  key={i}
                  style={{
                    opacity: itemOpacity,
                    transform: `translateY(${itemTranslateY}px)`,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    padding: "16px 36px",
                    borderRadius: 12,
                    backgroundColor: THEME.bgSubtle,
                    border: `1px solid ${THEME.gridColorLight}`,
                  }}
                >
                  <span
                    style={{
                      fontFamily: THEME.headingFont,
                      fontSize: THEME.fontSizeBody,
                      fontWeight: 600,
                      color: THEME.textPrimary,
                    }}
                  >
                    {item}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
