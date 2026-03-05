import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME, TEXT } from "../theme";

export const Scene5Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Inside <Sequence from={ctaIn}>, so frame 0 = global ctaIn.

  const ctaSpring = spring({
    fps,
    frame: Math.max(0, frame - 15),
    config: THEME.springSmooth,
  });
  const ctaOpacity = interpolate(frame, [10, 35], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const ctaY = interpolate(ctaSpring, [0, 1], [20, 0]);

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "flex-end",
        paddingBottom: 56,
      }}
    >
      <div
        style={{
          opacity: ctaOpacity,
          transform: `translateY(${ctaY}px)`,
          fontFamily: THEME.fontFamily,
          fontSize: THEME.fontSizeCTA,
          fontWeight: 500,
          color: THEME.accent,
          letterSpacing: 2,
          textAlign: "center",
        }}
      >
        {TEXT.cta}
      </div>
    </AbsoluteFill>
  );
};
