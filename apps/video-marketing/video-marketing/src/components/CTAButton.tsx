import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

type Props = {
  text: string;
  delay?: number;
};

export const CTAButton: React.FC<Props> = ({ text, delay = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const delayedFrame = Math.max(0, frame - delay);

  const entrance = spring({
    fps,
    frame: delayedFrame,
    config: THEME.springPunch,
  });

  const opacity = interpolate(delayedFrame, [0, 25], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const scale = interpolate(entrance, [0, 1], [0.9, 1]);

  // Subtle pulse after entrance
  const pulseFrame = Math.max(0, delayedFrame - 40);
  const pulse = pulseFrame > 0
    ? Math.sin(pulseFrame * 0.06) * 0.02
    : 0;

  return (
    <div
      style={{
        opacity,
        transform: `scale(${scale + pulse})`,
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "24px 64px",
        borderRadius: 60,
        backgroundColor: THEME.textWhite,
        boxShadow: "0 8px 32px rgba(0, 0, 0, 0.15)",
      }}
    >
      <span
        style={{
          fontFamily: THEME.headingFont,
          fontSize: THEME.fontSizeH3,
          fontWeight: 700,
          color: THEME.primary,
          letterSpacing: 1,
        }}
      >
        {text}
      </span>
    </div>
  );
};
