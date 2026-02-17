import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

type Props = {
  title: string;
  desc: string;
  index: number;
};

export const SolutionBlock: React.FC<Props> = ({ title, desc, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const delay = index * 120; // 4s stagger
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

  const translateX = interpolate(entrance, [0, 1], [60, 0]);

  return (
    <div
      style={{
        opacity,
        transform: `translateX(${translateX}px)`,
        display: "flex",
        alignItems: "stretch",
        gap: 20,
        width: 720,
      }}
    >
      {/* Green accent bar */}
      <div
        style={{
          width: 5,
          borderRadius: 3,
          backgroundColor: THEME.primary,
          flexShrink: 0,
        }}
      />
      <div style={{ padding: "12px 0" }}>
        <div
          style={{
            fontFamily: THEME.headingFont,
            fontSize: THEME.fontSizeH3,
            fontWeight: 700,
            color: THEME.textPrimary,
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
            color: THEME.textSecondary,
            lineHeight: THEME.lineHeight,
          }}
        >
          {desc}
        </div>
      </div>
    </div>
  );
};
