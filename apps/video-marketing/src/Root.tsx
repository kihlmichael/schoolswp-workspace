import { Composition } from "remotion";
import { BrandIntro } from "./compositions/BrandIntro";
import { BrandOutroA } from "./compositions/BrandOutroA";
import { BrandOutroB } from "./compositions/BrandOutroB";
import { BrandOutroC } from "./compositions/BrandOutroC";
import { BrandOutroCPro } from "./compositions/BrandOutroCPro";
import { THEME } from "./theme";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="BrandIntro"
        component={BrandIntro}
        durationInFrames={THEME.fps * 5}
        fps={THEME.fps}
        width={1920}
        height={1080}
      />
      <Composition
        id="BrandOutroA"
        component={BrandOutroA}
        durationInFrames={THEME.fps * 5}
        fps={THEME.fps}
        width={1920}
        height={1080}
      />
      <Composition
        id="BrandOutroB"
        component={BrandOutroB}
        durationInFrames={THEME.fps * 6}
        fps={THEME.fps}
        width={1920}
        height={1080}
      />
      <Composition
        id="BrandOutroC"
        component={BrandOutroC}
        durationInFrames={THEME.fps * 5}
        fps={THEME.fps}
        width={1920}
        height={1080}
      />
      <Composition
        id="BrandOutroCPro"
        component={BrandOutroCPro}
        durationInFrames={THEME.fps * 5}
        fps={THEME.fps}
        width={1920}
        height={1080}
      />
    </>
  );
};
