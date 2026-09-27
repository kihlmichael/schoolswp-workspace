import { normalizeTranscript } from "./timeline.mjs";

function token(text) {
  return text.toLocaleLowerCase("fr-FR").replace(/[^\p{L}\p{N}]+/gu, "");
}

export function findCutCandidates(input) {
  const transcript = normalizeTranscript(input);
  const words = transcript.words;
  const candidates = [];
  const seen = new Set();

  for (let i = 0; i < words.length - 1; i++) {
    if (token(words[i].text) && token(words[i].text) === token(words[i + 1].text)) {
      const key = "stutter:" + i;
      seen.add(key);
      candidates.push({
        id: key,
        type: "stutter",
        confidence: 0.82,
        cut: { start: words[i].start, end: words[i + 1].start },
        removes: words[i].text,
        keeps: words[i + 1].text,
        context: words.slice(Math.max(0, i - 4), Math.min(words.length, i + 6)).map((w) => w.text).join(" "),
        recommendation: "REVIEW"
      });
    }
  }

  for (let n = 2; n <= 5; n++) {
    for (let i = 0; i + n * 2 <= words.length; i++) {
      const a = words.slice(i, i + n).map((w) => token(w.text)).join(" ");
      const b = words.slice(i + n, i + n * 2).map((w) => token(w.text)).join(" ");
      if (!a || a !== b) continue;
      const gap = words[i + n].start - words[i + n - 1].end;
      if (gap > 1.5) continue;
      const key = "phrase-repeat:" + i + ":" + n;
      if (seen.has(key)) continue;
      candidates.push({
        id: key,
        type: "retake",
        confidence: 0.72,
        cut: { start: words[i].start, end: words[i + n].start },
        removes: words.slice(i, i + n).map((w) => w.text).join(" "),
        keeps: words.slice(i + n, i + n * 2).map((w) => w.text).join(" "),
        context: words.slice(Math.max(0, i - 4), Math.min(words.length, i + n * 2 + 4)).map((w) => w.text).join(" "),
        recommendation: "REVIEW"
      });
    }
  }

  return candidates.sort((a, b) => a.cut.start - b.cut.start);
}
