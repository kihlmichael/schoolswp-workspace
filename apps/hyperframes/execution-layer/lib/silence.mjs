import { normalizeTranscript } from "./timeline.mjs";

export function planSilenceCuts(input, profile) {
  const transcript = normalizeTranscript(input);
  const words = transcript.words;
  if (!words.length) return [];

  const p = {
    gapThreshold: 0.55,
    headPad: 0.22,
    tailPad: 0.34,
    normalBreath: 0.14,
    sentenceBreath: 0.20,
    longPauseBreath: 0.24,
    longPauseThreshold: 2.0,
    ...profile
  };

  const cuts = [];
  const headEnd = words[0].start - p.headPad;
  if (headEnd > 0.01) cuts.push({ start: 0, end: headEnd, type: "silence", reason: "head dead air", approved: true });

  for (let i = 1; i < words.length; i++) {
    const prev = words[i - 1];
    const next = words[i];
    const gap = next.start - prev.end;
    if (gap < p.gapThreshold) continue;

    const sentenceEnd = /[.!?…]["')\]]?$/.test(prev.text);
    const breath = gap >= p.longPauseThreshold
      ? p.longPauseBreath
      : sentenceEnd
        ? p.sentenceBreath
        : p.normalBreath;

    const keepAfter = breath * 0.6;
    const keepBefore = breath * 0.4;
    const start = prev.end + keepAfter;
    const end = next.start - keepBefore;
    if (end > start + 0.01) {
      cuts.push({
        start,
        end,
        type: "silence",
        reason: "pause " + gap.toFixed(3) + "s",
        approved: true
      });
    }
  }

  const tailStart = words.at(-1).end + p.tailPad;
  if (tailStart < transcript.duration - 0.01) {
    cuts.push({ start: tailStart, end: transcript.duration, type: "silence", reason: "tail dead air", approved: true });
  }

  return cuts;
}
