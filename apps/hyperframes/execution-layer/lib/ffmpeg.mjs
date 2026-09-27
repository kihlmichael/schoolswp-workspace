import { spawn } from "node:child_process";

function run(command, args) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: ["ignore", "ignore", "pipe"] });
    let stderr = "";
    child.stderr.on("data", (d) => { stderr += d.toString(); });
    child.on("error", reject);
    child.on("close", (code) => {
      if (code === 0) resolve();
      else reject(new Error(command + " exited " + code + ": " + stderr.slice(-1200)));
    });
  });
}

export async function renderKeeps(inputPath, outputPath, keeps) {
  if (!keeps?.length) throw new Error("No keep ranges to render");

  const parts = [];
  const labels = [];
  keeps.forEach((k, i) => {
    parts.push(
      "[0:v]trim=start=" + k.sourceStart + ":end=" + k.sourceEnd + ",setpts=PTS-STARTPTS[v" + i + "]",
      "[0:a]atrim=start=" + k.sourceStart + ":end=" + k.sourceEnd + ",asetpts=PTS-STARTPTS[a" + i + "]"
    );
    labels.push("[v" + i + "][a" + i + "]");
  });
  parts.push(labels.join("") + "concat=n=" + keeps.length + ":v=1:a=1[vout][aout]");

  await run("ffmpeg", [
    "-y",
    "-i", inputPath,
    "-filter_complex", parts.join(";"),
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "20",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-movflags", "+faststart",
    outputPath
  ]);
}

export async function ffprobeDuration(inputPath) {
  return await new Promise((resolve, reject) => {
    const child = spawn("ffprobe", [
      "-v", "error",
      "-show_entries", "format=duration",
      "-of", "default=noprint_wrappers=1:nokey=1",
      inputPath
    ]);
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (d) => { stdout += d.toString(); });
    child.stderr.on("data", (d) => { stderr += d.toString(); });
    child.on("error", reject);
    child.on("close", (code) => {
      if (code !== 0) reject(new Error("ffprobe failed: " + stderr));
      else resolve(Number(stdout.trim()));
    });
  });
}
