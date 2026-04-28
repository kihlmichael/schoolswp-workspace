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
import { THEME } from "../theme";
import { TEXTS } from "../texts";

/**
 * Scene 6 — Credibilite
 * Duree : 20s (600 frames @ 30fps)
 * Position : apres Scene 4 (Solutions) dans la timeline globale
 *
 * Structure :
 *   Phase 1 (0-2s)   : Fond sombre + portrait fondateur + nom/titre
 *   Phase 2 (2-6s)   : 3 badges apparaissent en stagger (depuis 2021, 100+ contenus, 5 etapes)
 *   Phase 3 (6-12s)  : Ecosysteme schoolsWP — 4 piliers (Blog, Newsletter, YouTube, Academy)
 *   Phase 4 (12-18s) : Hold / respiration
 *   Phase 5 (18-20s) : Fade-out
 */

export const Scene6Credibility: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { credibility } = TEXTS;

  // ===== SCENE FADE-IN / FADE-OUT =====
  const fadeIn = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(frame, [540, 600], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== PHASE 1: Founder portrait + name =====
  const founderSpring = spring({
    frame,
    fps,
    config: THEME.springSmooth,
    durationInFrames: 40,
  });
  const founderScale = interpolate(founderSpring, [0, 1], [0.9, 1]);
  const founderOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Founder name/title
  const nameOpacity = interpolate(frame, [20, 50], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const nameY = interpolate(frame, [20, 50], [15, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== PHASE 2: Badges stagger (start frame 60 = 2s) =====
  const badgeBaseDelay = 60;
  const badgeStagger = 25;

  // ===== PHASE 3: Ecosystem (start frame 180 = 6s) =====
  const ecoTitleOpacity = interpolate(frame, [180, 210], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const ecoTitleY = interpolate(frame, [180, 210], [20, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const ecoBaseDelay = 220;
  const ecoStagger = 30;

  // ===== Green accent line under section title =====
  const lineWidth = interpolate(frame, [190, 230], [0, 120], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // ===== Subtle glow behind founder avatar =====
  const glowOpacity = interpolate(
    frame,
    [0, 30, 360, 540, 600],
    [0, 0.1, 0.1, 0.06, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

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
          gap: 0,
        }}
      >
        {/* ===== TOP SECTION: Founder ===== */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            marginBottom: 40,
          }}
        >
          {/* Glow behind avatar */}
          <div
            style={{
              position: "absolute",
              top: 120,
              width: 300,
              height: 300,
              borderRadius: "50%",
              background: `radial-gradient(circle, ${THEME.primary} 0%, transparent 70%)`,
              opacity: glowOpacity,
              filter: "blur(60px)",
            }}
          />

          {/* Avatar placeholder — green circle with initials */}
          <div
            style={{
              width: 120,
              height: 120,
              borderRadius: "50%",
              backgroundColor: THEME.primary,
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              opacity: founderOpacity,
              transform: `scale(${founderScale})`,
              border: `3px solid ${THEME.primaryDark}`,
              boxShadow: `0 0 30px ${THEME.primary}30`,
            }}
          >
            <span
              style={{
                fontFamily: THEME.headingFont,
                fontSize: 42,
                fontWeight: 700,
                color: THEME.bgDark,
              }}
            >
              MK
            </span>
          </div>

          {/* Founder name */}
          <div
            style={{
              marginTop: 20,
              opacity: nameOpacity,
              transform: `translateY(${nameY}px)`,
              fontFamily: THEME.headingFont,
              fontSize: THEME.fontSizeH3,
              fontWeight: 700,
              color: THEME.textWhite,
              textAlign: "center",
            }}
          >
            {credibility.founder}
          </div>

          {/* Founder title */}
          <div
            style={{
              marginTop: 8,
              opacity: nameOpacity,
              transform: `translateY(${nameY}px)`,
              fontFamily: THEME.bodyFont,
              fontSize: THEME.fontSizeCaption,
              color: THEME.textLight,
              textAlign: "center",
            }}
          >
            {credibility.founderTitle}
          </div>
        </div>

        {/* ===== BADGES ROW ===== */}
        <div
          style={{
            display: "flex",
            gap: 40,
            marginBottom: 50,
          }}
        >
          {credibility.badges.map((badge, i) => {
            const delay = badgeBaseDelay + i * badgeStagger;
            const badgeSpring = spring({
              frame: frame - delay,
              fps,
              config: THEME.springPunch,
              durationInFrames: 30,
            });
            const badgeScale = interpolate(badgeSpring, [0, 1], [0.8, 1]);
            const badgeOpacity = badgeSpring;

            return (
              <div
                key={i}
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  gap: 8,
                  opacity: badgeOpacity,
                  transform: `scale(${badgeScale})`,
                }}
              >
                {/* Badge value */}
                <div
                  style={{
                    fontFamily: THEME.headingFont,
                    fontSize: THEME.fontSizeH2,
                    fontWeight: 700,
                    color: THEME.primary,
                    lineHeight: 1,
                  }}
                >
                  {badge.value}
                </div>
                {/* Badge label */}
                <div
                  style={{
                    fontFamily: THEME.bodyFont,
                    fontSize: THEME.fontSizeSmall,
                    color: THEME.textLight,
                    textAlign: "center",
                    maxWidth: 160,
                  }}
                >
                  {badge.label}
                </div>
              </div>
            );
          })}
        </div>

        {/* ===== GREEN ACCENT LINE ===== */}
        <div
          style={{
            width: lineWidth,
            height: 2,
            backgroundColor: THEME.primary,
            marginBottom: 30,
            boxShadow: `0 0 8px ${THEME.primary}40`,
          }}
        />

        {/* ===== ECOSYSTEM SECTION ===== */}
        <div
          style={{
            opacity: ecoTitleOpacity,
            transform: `translateY(${ecoTitleY}px)`,
            fontFamily: THEME.headingFont,
            fontSize: THEME.fontSizeBody,
            fontWeight: 700,
            color: THEME.textWhite,
            letterSpacing: 2,
            textTransform: "uppercase",
            marginBottom: 30,
          }}
        >
          L'ecosysteme schoolsWP
        </div>

        {/* Ecosystem items row */}
        <div
          style={{
            display: "flex",
            gap: 50,
          }}
        >
          {credibility.ecosystemItems.map((item, i) => {
            const delay = ecoBaseDelay + i * ecoStagger;
            const itemSpring = spring({
              frame: frame - delay,
              fps,
              config: THEME.springSmooth,
              durationInFrames: 30,
            });
            const itemOpacity = itemSpring;
            const itemY = interpolate(itemSpring, [0, 1], [20, 0]);

            // Icon mapping
            const icon = getEcosystemIcon(item);

            return (
              <div
                key={i}
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  gap: 12,
                  opacity: itemOpacity,
                  transform: `translateY(${itemY}px)`,
                }}
              >
                {/* Icon circle */}
                <div
                  style={{
                    width: 64,
                    height: 64,
                    borderRadius: 16,
                    backgroundColor: THEME.greenSubtle,
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                  }}
                >
                  <span style={{ fontSize: 28 }}>{icon}</span>
                </div>
                {/* Label */}
                <div
                  style={{
                    fontFamily: THEME.bodyFont,
                    fontSize: THEME.fontSizeCaption,
                    color: THEME.textWhite,
                    fontWeight: 500,
                  }}
                >
                  {item}
                </div>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Map ecosystem item names to emoji icons */
function getEcosystemIcon(item: string): string {
  switch (item.toLowerCase()) {
    case "blog":
      return "\u{1F4DD}"; // memo
    case "newsletter":
      return "\u{2709}\u{FE0F}"; // envelope
    case "youtube":
      return "\u{1F3AC}"; // clapper board
    case "academy":
      return "\u{1F393}"; // graduation cap
    default:
      return "\u{2B50}"; // star
  }
}
