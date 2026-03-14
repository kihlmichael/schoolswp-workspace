import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { ThreeCanvas } from "@remotion/three";
import { Logo3D } from "../components/Logo3D";
import { THEME } from "../theme";

export const Scene2LogoReveal: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height, fps } = useVideoConfig();

  // Logo entrance timing (relative to global frame)
  const entranceFrame = Math.max(0, frame - THEME.logoIn);

  // Move-up timing (when message appears)
  const moveUpFrame = Math.max(0, frame - THEME.msgIn);

  // Container opacity: invisible before logoIn, fade in over 30 frames
  const containerOpacity = interpolate(
    frame,
    [THEME.logoIn, THEME.logoIn + 30],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  // Soft shadow under the canvas (2D overlay, more controllable than 3D shadow)
  const shadowOpacity = interpolate(
    frame,
    [THEME.logoIn + 30, THEME.logoIn + 60],
    [0, 0.08],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill style={{ opacity: containerOpacity }}>
      <ThreeCanvas
        width={width}
        height={height}
        camera={{ position: [0, 0, THEME.cameraZ], fov: THEME.cameraFov }}
        gl={{ preserveDrawingBuffer: true, alpha: true }}
        style={{ background: "transparent" }}
      >
        {/* Lighting: soft and clean */}
        <ambientLight intensity={0.6} color="#ffffff" />
        <directionalLight
          intensity={0.8}
          position={[5, 5, 5]}
          castShadow={false}
        />
        <directionalLight
          intensity={0.3}
          position={[-3, 2, 4]}
        />

        <Logo3D
          frame={entranceFrame}
          fps={fps}
          moveUpProgress={moveUpFrame}
        />
      </ThreeCanvas>

      {/* 2D drop shadow overlay for premium feel */}
      <div
        style={{
          position: "absolute",
          top: "55%",
          left: "50%",
          transform: "translate(-50%, 0)",
          width: 600,
          height: 20,
          borderRadius: "50%",
          background: `radial-gradient(ellipse, rgba(0,0,0,${shadowOpacity}) 0%, transparent 70%)`,
        }}
      />
    </AbsoluteFill>
  );
};
