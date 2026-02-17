import React from "react";
import { Composition } from "remotion";
import { VideoMarketing } from "./VideoMarketing";
import { THEME } from "./theme";

export const Root: React.FC = () => {
  return (
    <Composition
      id="VideoMarketing"
      component={VideoMarketing}
      durationInFrames={THEME.totalFrames}
      width={1920}
      height={1080}
      fps={THEME.fps}
    />
  );
};
