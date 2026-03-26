import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

type Props = {
  value: string;
  label: string;
  index: number;
};

export const TimelineBadge: React.FC<Props> = ({ value, label, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const delay = index * 40;
  const delayedFrame = Math.max(0, frame - delay);

  const scale = spring({
    fps,
    frame: delayedFrame,
    config: THEME.springPunch,
  });

  const opacity = interpolate(delayedFrame, [0, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        opacity,
        transform: `scale(${interpolate(scale, [0, 1], [0.8, 1])})`,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 8,
        padding: "24px 32px",
        borderRadius: 16,
        backgroundColor: THEME.greenSubtle,
        minWidth: 160,
      }}
    >
      <div
        style={{
          fontFamily: THEME.headingFont,
          fontSize: THEME.fontSizeH2,
          fontWeight: 700,
          color: THEME.primary,
        }}
      >
        {value}
      </div>
      <div
        style={{
          fontFamily: THEME.bodyFont,
          fontSize: THEME.fontSizeSmall,
          fontWeight: 400,
          color: THEME.textSecondary,
          textAlign: "center",
        }}
      >
        {label}
      </div>
    </div>
  );
};
