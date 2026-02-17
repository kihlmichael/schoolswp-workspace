import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

type Props = {
  icon: string;
  title: string;
  desc: string;
  index: number;
};

export const ProblemCard: React.FC<Props> = ({ icon, title, desc, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const delay = index * 120; // 4s stagger between cards
  const delayedFrame = Math.max(0, frame - delay);

  const entrance = spring({
    fps,
    frame: delayedFrame,
    config: THEME.springSmooth,
  });

  const opacity = interpolate(delayedFrame, [0, 25], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const translateX = interpolate(entrance, [0, 1], [-60, 0]);

  return (
    <div
      style={{
        opacity,
        transform: `translateX(${translateX}px)`,
        display: "flex",
        alignItems: "center",
        gap: 24,
        padding: "20px 32px",
        borderRadius: 16,
        backgroundColor: "rgba(255, 255, 255, 0.06)",
        borderLeft: `4px solid ${THEME.red}`,
        width: 720,
      }}
    >
      <span style={{ fontSize: 40, flexShrink: 0 }}>{icon}</span>
      <div>
        <div
          style={{
            fontFamily: THEME.headingFont,
            fontSize: THEME.fontSizeH3,
            fontWeight: 700,
            color: THEME.textWhite,
            marginBottom: 4,
          }}
        >
          {title}
        </div>
        <div
          style={{
            fontFamily: THEME.bodyFont,
            fontSize: THEME.fontSizeCaption,
            fontWeight: 400,
            color: THEME.textLight,
            lineHeight: THEME.lineHeight,
          }}
        >
          {desc}
        </div>
      </div>
    </div>
  );
};
