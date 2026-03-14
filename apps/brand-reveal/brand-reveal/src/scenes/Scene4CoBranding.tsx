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

export const Scene4CoBranding: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // This component is inside <Sequence from={cobrandIn}>,
  // so frame 0 = global frame cobrandIn.

  // WordPress logo entrance
  const wpSpring = spring({
    fps,
    frame,
    config: THEME.springSmooth,
  });
  const wpScale = interpolate(wpSpring, [0, 1], [0.9, 1]);
  const wpOpacity = interpolate(frame, [0, 25], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Separator line slide-in
  const lineSpring = spring({
    fps,
    frame: Math.max(0, frame - 10),
    config: THEME.springSmooth,
  });
  const lineWidth = interpolate(lineSpring, [0, 1], [0, 120]);

  // Snap alignment micro-translate
  const snapX = spring({
    fps,
    frame: Math.max(0, frame - 20),
    config: { damping: 300, mass: 0.5, stiffness: 200 },
  });
  const nudge = interpolate(snapX, [0, 1], [3, 0]);

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "flex-end",
        paddingBottom: 120,
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 16,
          opacity: wpOpacity,
          transform: `translateX(${nudge}px)`,
        }}
      >
        {/* Separator line */}
        <div
          style={{
            width: lineWidth,
            height: 1,
            backgroundColor: THEME.separatorColor,
          }}
        />

        {/* WordPress badge */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 12,
            transform: `scale(${wpScale})`,
          }}
        >
          <Img
            src={staticFile(THEME.logoWordPress)}
            style={{ width: 32, height: 32 }}
          />
          <span
            style={{
              fontFamily: THEME.fontFamily,
              fontSize: 18,
              fontWeight: 500,
              color: THEME.textSecondary,
              letterSpacing: 1,
            }}
          >
            Propuls\u00E9 par WordPress
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
};
