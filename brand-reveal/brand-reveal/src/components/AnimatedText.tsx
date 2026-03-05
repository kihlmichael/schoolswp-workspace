import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

type Props = {
  text: string;
  accentPhrase?: string;
  fontSize?: number;
  color?: string;
  delay?: number;
  style?: React.CSSProperties;
};

export const AnimatedText: React.FC<Props> = ({
  text,
  accentPhrase,
  fontSize = THEME.fontSizeHero,
  color = THEME.textPrimary,
  delay = 0,
  style,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const delayedFrame = Math.max(0, frame - delay);

  const slideUp = spring({
    fps,
    frame: delayedFrame,
    config: THEME.springPunch,
  });

  const translateY = interpolate(slideUp, [0, 1], [40, 0]);
  const opacity = interpolate(delayedFrame, [0, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const renderText = () => {
    if (!accentPhrase || !text.includes(accentPhrase)) {
      return text;
    }

    const idx = text.indexOf(accentPhrase);
    const before = text.slice(0, idx);
    const after = text.slice(idx + accentPhrase.length);

    return (
      <>
        {before}
        <span style={{ color: THEME.accent }}>{accentPhrase}</span>
        {after}
      </>
    );
  };

  return (
    <div
      style={{
        opacity,
        transform: `translateY(${translateY}px)`,
        fontFamily: THEME.fontFamily,
        fontSize,
        fontWeight: 700,
        color,
        letterSpacing: THEME.letterSpacing,
        lineHeight: THEME.lineHeight,
        textAlign: "center",
        ...style,
      }}
    >
      {renderText()}
    </div>
  );
};
