import React, { useMemo } from "react";
import { interpolate, spring } from "remotion";
import * as THREE from "three";
import { SVGLoader } from "three/examples/jsm/loaders/SVGLoader.js";
import { THEME } from "../theme";
import { LOGO_SVG_RAW, preprocessSvgForThreeJs } from "../assets/logo-svg-data";

type Props = {
  frame: number;
  fps: number;
  moveUpProgress: number;
};

export const Logo3D: React.FC<Props> = ({ frame, fps, moveUpProgress }) => {
  const svgGroup = useMemo(() => {
    const processed = preprocessSvgForThreeJs(LOGO_SVG_RAW);
    const loader = new SVGLoader();
    const data = loader.parse(processed);
    const group = new THREE.Group();

    data.paths.forEach((path) => {
      const fillColor = path.userData?.style?.fill;
      if (!fillColor || fillColor === "none") return;

      const shapes = SVGLoader.createShapes(path);

      shapes.forEach((shape) => {
        const geometry = new THREE.ExtrudeGeometry(shape, {
          depth: THEME.extrudeDepth,
          bevelEnabled: true,
          bevelThickness: THEME.bevelThickness,
          bevelSize: THEME.bevelSize,
          bevelSegments: 2,
          curveSegments: 8,
        });

        const material = new THREE.MeshStandardMaterial({
          color: new THREE.Color(fillColor),
          roughness: 0.7,
          metalness: 0.05,
        });

        const mesh = new THREE.Mesh(geometry, material);
        group.add(mesh);
      });
    });

    // Center the geometry
    const box = new THREE.Box3().setFromObject(group);
    const center = box.getCenter(new THREE.Vector3());
    const size = box.getSize(new THREE.Vector3());

    group.children.forEach((child) => {
      if (child instanceof THREE.Mesh) {
        child.position.x -= center.x;
        child.position.y -= center.y;
        child.position.z -= center.z;
      }
    });

    // Scale to fit target width in Three.js units + flip Y (SVG coords)
    const scaleFactor = THEME.logoScaleTarget / size.x;
    group.scale.set(scaleFactor, -scaleFactor, scaleFactor);

    return group;
  }, []);

  // --- Entrance animation (frame 0 → 90) ---
  const entranceSpring = spring({
    fps,
    frame,
    config: THEME.springSmooth,
  });

  const rotY = interpolate(entranceSpring, [0, 1], [-0.26, 0]);
  const scale = interpolate(entranceSpring, [0, 1], [0.85, 1]);

  // --- Move up when message appears ---
  const moveUpSpring = spring({
    fps,
    frame: Math.max(0, moveUpProgress),
    config: THEME.springSmooth,
  });
  const posY = interpolate(moveUpSpring, [0, 1], [0, 1.8]);

  return (
    <group rotation={[0, rotY, 0]} scale={[scale, scale, scale]} position={[0, posY, 0]}>
      <primitive object={svgGroup} />
    </group>
  );
};
