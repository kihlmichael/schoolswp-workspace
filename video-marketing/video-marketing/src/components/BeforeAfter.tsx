import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

type Props = {
  beforeTitle: string;
  afterTitle: string;
  beforeItems: readonly string[];
  afterItems: readonly string[];
};

export const BeforeAfter: React.FC<Props> = ({
  beforeTitle,
  afterTitle,
  beforeItems,
  afterItems,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Left column slides in from left
  const leftSpring = spring({ fps, frame, config: THEME.springSmooth });
  const leftX = interpolate(leftSpring, [0, 1], [-80, 0]);
  const leftOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Right column slides in from right with delay
  const rightSpring = spring({
    fps,
    frame: Math.max(0, frame - 20),
    config: THEME.springSmooth,
  });
  const rightX = interpolate(rightSpring, [0, 1], [80, 0]);
  const rightOpacity = interpolate(frame, [20, 50], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const columnStyle: React.CSSProperties = {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    gap: 16,
    padding: "32px 40px",
    borderRadius: 20,
  };

  const itemStyle = (color: string): React.CSSProperties => ({
    fontFamily: THEME.bodyFont,
    fontSize: THEME.fontSizeCaption,
    fontWeight: 400,
    color,
    lineHeight: 1.6,
    display: "flex",
    alignItems: "center",
    gap: 12,
  });

  return (
    <div
      style={{
        display: "flex",
        gap: 40,
        width: 1400,
        alignItems: "stretch",
      }}
    >
      {/* BEFORE column */}
      <div
        style={{
          ...columnStyle,
          opacity: leftOpacity,
          transform: `translateX(${leftX}px)`,
          backgroundColor: THEME.redSubtle,
        }}
      >
        <div
          style={{
            fontFamily: THEME.headingFont,
            fontSize: THEME.fontSizeH3,
            fontWeight: 700,
            color: THEME.red,
            marginBottom: 8,
          }}
        >
          {beforeTitle}
        </div>
        {beforeItems.map((item, i) => (
          <div key={i} style={itemStyle(THEME.textPrimary)}>
            <span style={{ color: THEME.red, fontSize: 20 }}>✕</span>
            {item}
          </div>
        ))}
      </div>

      {/* AFTER column */}
      <div
        style={{
          ...columnStyle,
          opacity: rightOpacity,
          transform: `translateX(${rightX}px)`,
          backgroundColor: THEME.greenSubtle,
        }}
      >
        <div
          style={{
            fontFamily: THEME.headingFont,
            fontSize: THEME.fontSizeH3,
            fontWeight: 700,
            color: THEME.primaryDark,
            marginBottom: 8,
          }}
        >
          {afterTitle}
        </div>
        {afterItems.map((item, i) => (
          <div key={i} style={itemStyle(THEME.textPrimary)}>
            <span style={{ color: THEME.primary, fontSize: 20 }}>✓</span>
            {item}
          </div>
        ))}
      </div>
    </div>
  );
};
