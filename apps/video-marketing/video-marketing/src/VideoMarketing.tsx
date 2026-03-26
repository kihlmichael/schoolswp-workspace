import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { THEME } from "./theme";
import { Scene1Hook } from "./scenes/Scene1Hook";
import { Scene2Presentation } from "./scenes/Scene2Presentation";
import { Scene3Problems } from "./scenes/Scene3Problems";
import { Scene4Solutions } from "./scenes/Scene4Solutions";
import { Scene5Benefits } from "./scenes/Scene5Benefits";
import { Scene6Credibility } from "./scenes/Scene6Credibility";
import { Scene7CTA } from "./scenes/Scene7CTA";

export const VideoMarketing: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: THEME.bgDark }}>
      <Sequence from={THEME.scene1.start} durationInFrames={THEME.scene1.duration}>
        <Scene1Hook />
      </Sequence>

      <Sequence from={THEME.scene2.start} durationInFrames={THEME.scene2.duration}>
        <Scene2Presentation />
      </Sequence>

      <Sequence from={THEME.scene3.start} durationInFrames={THEME.scene3.duration}>
        <Scene3Problems />
      </Sequence>

      <Sequence from={THEME.scene4.start} durationInFrames={THEME.scene4.duration}>
        <Scene4Solutions />
      </Sequence>

      <Sequence from={THEME.scene5.start} durationInFrames={THEME.scene5.duration}>
        <Scene5Benefits />
      </Sequence>

      <Sequence from={THEME.scene6.start} durationInFrames={THEME.scene6.duration}>
        <Scene6Credibility />
      </Sequence>

      <Sequence from={THEME.scene7.start} durationInFrames={THEME.scene7.duration}>
        <Scene7CTA />
      </Sequence>
    </AbsoluteFill>
  );
};
