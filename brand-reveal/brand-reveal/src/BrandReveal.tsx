import React from "react";
import { AbsoluteFill, interpolate, Sequence, useCurrentFrame } from "remotion";
import { THEME } from "./theme";
import { Scene1Background } from "./scenes/Scene1Background";
import { Scene2LogoReveal } from "./scenes/Scene2LogoReveal";
import { Scene3Message } from "./scenes/Scene3Message";

export const BrandReveal: React.FC = () => {
  const frame = useCurrentFrame();

  // Global fade-out (last 2 seconds → fade to background color)
  const globalOpacity = interpolate(
    frame,
    [THEME.fadeStart, THEME.totalFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill style={{ backgroundColor: THEME.background }}>
      {/* Content layer — fades out at the end */}
      <AbsoluteFill style={{ opacity: globalOpacity }}>
        {/* Layer 1: Background (grid + gradient) — full duration */}
        <Scene1Background />

        {/* Layer 2: 3D Logo — always mounted for useMemo cache, opacity controlled internally */}
        <Scene2LogoReveal />

        {/* Layer 3: Message text — appears at msgIn */}
        <Sequence from={THEME.msgIn}>
          <Scene3Message />
        </Sequence>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
