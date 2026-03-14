import React from "react";
import { Composition } from "remotion";
import { BrandReveal } from "./BrandReveal";
import { THEME } from "./theme";

export const Root: React.FC = () => {
  return (
    <Composition
      id="BrandReveal"
      component={BrandReveal}
      durationInFrames={THEME.totalFrames}
      width={1920}
      height={1080}
      fps={THEME.fps}
    />
  );
};
