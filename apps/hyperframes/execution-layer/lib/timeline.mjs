const EPS = 1e-6;

export function normalizeTranscript(input) {
  const rawWords = Array.isArray(input?.words) ? input.words : [];
  const words = rawWords
    .filter((w) => w && w.type !== "spacing" && typeof w.text === "string" && w.text.trim())
    .map((w) => ({
      text: w.text.trim(),
      start: Number(w.start),
      end: Number(w.end),
      ...(Number.isFinite(w.sourceStart) ? { sourceStart: Number(w.sourceStart) } : {}),
      ...(Number.isFinite(w.sourceEnd) ? { sourceEnd: Number(w.sourceEnd) } : {}),
      ...(Number.isFinite(w.confidence) ? { confidence: Number(w.confidence) } : {}),
      ...(w.type ? { type: w.type } : {})
    }));

  const duration = Number(
    input?.duration ??
    input?.audio_duration_secs ??
    input?.audioDuration ??
    words.at(-1)?.end ??
    0
  );

  const normalized = {
    schema_version: "1.1",
    duration,
    text: typeof input?.text === "string" ? input.text : words.map((w) => w.text).join(" "),
    words
  };

  const result = validateTranscript(normalized);
  if (!result.ok) throw new Error("Invalid transcript: " + result.errors.join("; "));
  return normalized;
}

export function validateTranscript(transcript) {
  const errors = [];
  if (!Number.isFinite(transcript?.duration) || transcript.duration < 0) errors.push("Invalid duration");
  if (!Array.isArray(transcript?.words)) errors.push("Missing words");
  let previousEnd = 0;
  for (let i = 0; i < (transcript?.words || []).length; i++) {
    const w = transcript.words[i];
    if (typeof w.text !== "string" || !w.text.trim()) errors.push("Word " + i + " has no text");
    if (!Number.isFinite(w.start) || !Number.isFinite(w.end) || w.start < 0 || w.end <= w.start) {
      errors.push("Word " + i + " has invalid timing");
      continue;
    }
    if (w.start + EPS < previousEnd) errors.push("Word " + i + " overlaps previous word");
    if (w.end > transcript.duration + 0.01) errors.push("Word " + i + " exceeds transcript duration");
    if (Number.isFinite(w.sourceStart) !== Number.isFinite(w.sourceEnd)) errors.push("Word " + i + " has partial source mapping");
    previousEnd = w.end;
  }
  return { ok: errors.length === 0, errors };
}

export function normalizeCuts(cuts, duration) {
  const sorted = (cuts || [])
    .map((c) => ({
      ...c,
      start: Math.max(0, Number(c.start)),
      end: Math.min(duration, Number(c.end))
    }))
    .filter((c) => Number.isFinite(c.start) && Number.isFinite(c.end) && c.end > c.start + EPS)
    .sort((a, b) => a.start - b.start);

  const merged = [];
  for (const cut of sorted) {
    const last = merged.at(-1);
    if (last && cut.start <= last.end + EPS && (cut.type || "edit") === (last.type || "edit")) {
      last.end = Math.max(last.end, cut.end);
      last.reasons = [...new Set([...(last.reasons || []), ...(cut.reasons || []), cut.reason].filter(Boolean))];
    } else {
      merged.push({
        ...cut,
        reasons: [...new Set([...(cut.reasons || []), cut.reason].filter(Boolean))]
      });
    }
  }
  return merged;
}

export function buildKeeps(duration, cuts) {
  const normalized = normalizeCuts(cuts, duration);
  const keeps = [];
  let cursor = 0;
  let editedCursor = 0;
  for (const cut of normalized) {
    if (cut.start > cursor + EPS) {
      const len = cut.start - cursor;
      keeps.push({ sourceStart: cursor, sourceEnd: cut.start, start: editedCursor, end: editedCursor + len });
      editedCursor += len;
    }
    cursor = Math.max(cursor, cut.end);
  }
  if (cursor < duration - EPS) {
    const len = duration - cursor;
    keeps.push({ sourceStart: cursor, sourceEnd: duration, start: editedCursor, end: editedCursor + len });
    editedCursor += len;
  }
  return { keeps, editedDuration: editedCursor, cuts: normalized };
}

export function buildInitialEdl({ projectId, source = {}, cuts = [], revision = 1 }) {
  const duration = Number(source.duration);
  if (!Number.isFinite(duration) || duration < 0) throw new Error("source.duration is required");
  const built = buildKeeps(duration, cuts);
  return {
    schema_version: "1.1",
    project_id: projectId || "UNASSIGNED",
    source: { ...source, duration },
    edited_duration: built.editedDuration,
    keeps: built.keeps,
    cuts: built.cuts.map((c) => ({
      sourceStart: c.start,
      sourceEnd: c.end,
      type: c.type || "edit",
      reason: c.reason || c.reasons?.join("; ") || "unspecified",
      approved: c.approved !== false
    })),
    revision
  };
}

function subtractInterval(segmentStart, segmentEnd, cuts) {
  let parts = [[segmentStart, segmentEnd]];
  for (const cut of cuts) {
    const next = [];
    for (const [a, b] of parts) {
      if (cut.end <= a + EPS || cut.start >= b - EPS) next.push([a, b]);
      else {
        if (cut.start > a + EPS) next.push([a, Math.min(cut.start, b)]);
        if (cut.end < b - EPS) next.push([Math.max(cut.end, a), b]);
      }
    }
    parts = next;
  }
  return parts;
}

export function applyTimelineCuts(previousEdl, newCuts, meta = {}) {
  const stageDuration = Number(previousEdl.edited_duration);
  const cuts = normalizeCuts(newCuts, stageDuration);
  const keeps = [];
  let editedCursor = 0;

  for (const k of previousEdl.keeps) {
    const localParts = subtractInterval(k.start, k.end, cuts);
    for (const [a, b] of localParts) {
      const sourceStart = k.sourceStart + (a - k.start);
      const sourceEnd = k.sourceStart + (b - k.start);
      const len = b - a;
      keeps.push({ sourceStart, sourceEnd, start: editedCursor, end: editedCursor + len });
      editedCursor += len;
    }
  }

  const mappedCuts = [];
  for (const cut of cuts) {
    for (const k of previousEdl.keeps) {
      const a = Math.max(cut.start, k.start);
      const b = Math.min(cut.end, k.end);
      if (b <= a + EPS) continue;
      mappedCuts.push({
        sourceStart: k.sourceStart + (a - k.start),
        sourceEnd: k.sourceStart + (b - k.start),
        type: cut.type || meta.type || "edit",
        reason: cut.reason || meta.reason || "reviewed edit",
        approved: cut.approved !== false
      });
    }
  }

  return {
    schema_version: "1.1",
    project_id: previousEdl.project_id,
    source: previousEdl.source,
    edited_duration: editedCursor,
    keeps,
    cuts: [...(previousEdl.cuts || []), ...mappedCuts],
    revision: Number(previousEdl.revision || 1) + 1
  };
}

export function retimeTranscript(transcriptInput, edl) {
  const transcript = normalizeTranscript(transcriptInput);
  const words = [];

  for (const word of transcript.words) {
    const sourceStart = Number.isFinite(word.sourceStart) ? word.sourceStart : word.start;
    const sourceEnd = Number.isFinite(word.sourceEnd) ? word.sourceEnd : word.end;
    const keep = edl.keeps.find((k) => sourceStart >= k.sourceStart - 0.002 && sourceEnd <= k.sourceEnd + 0.002);
    if (!keep) continue;
    words.push({
      ...word,
      sourceStart,
      sourceEnd,
      start: keep.start + (sourceStart - keep.sourceStart),
      end: keep.start + (sourceEnd - keep.sourceStart)
    });
  }

  return {
    schema_version: "1.1",
    duration: edl.edited_duration,
    text: words.map((w) => w.text).join(" "),
    words
  };
}

export function validateEdl(edl) {
  const errors = [];
  if (edl?.schema_version !== "1.1") errors.push("Unsupported schema_version");
  const duration = Number(edl?.source?.duration);
  if (!Number.isFinite(duration) || duration < 0) errors.push("Invalid source duration");
  if (!Array.isArray(edl?.keeps)) errors.push("Missing keeps");
  let sourceCursor = -Infinity;
  let editCursor = 0;
  for (const [i, k] of (edl?.keeps || []).entries()) {
    if (![k.sourceStart, k.sourceEnd, k.start, k.end].every(Number.isFinite)) {
      errors.push("Keep " + i + " has invalid numbers");
      continue;
    }
    if (k.sourceEnd <= k.sourceStart || k.end <= k.start) errors.push("Keep " + i + " has no duration");
    if (k.sourceStart < sourceCursor - EPS) errors.push("Keep " + i + " source order invalid");
    if (Math.abs(k.start - editCursor) > 0.003) errors.push("Keep " + i + " edited timeline is not contiguous");
    const sourceLen = k.sourceEnd - k.sourceStart;
    const editLen = k.end - k.start;
    if (Math.abs(sourceLen - editLen) > 0.003) errors.push("Keep " + i + " changes playback speed");
    sourceCursor = k.sourceEnd;
    editCursor = k.end;
  }
  if (Number.isFinite(edl?.edited_duration) && Math.abs(editCursor - edl.edited_duration) > 0.003) {
    errors.push("edited_duration differs from keeps");
  }
  return { ok: errors.length === 0, errors };
}
