# graphify-brain

Guardrail wrapper turning `graphify` into the schoolsWP second brain. graphify maps; schoolsWP decides what is indexed, what egresses to Gemini, and logs every refresh. The memory stays in your existing markdown (index-in-place, zero migration).

## Env vars

- `SCHOOLSWP_REPO_PATH` - repo root.
- `OBSIDIAN_BRIDGE_PATH` - obsidian-bridge folder, read-only source. Default: `<repo>/obsidian-bridge`.
- `GRAPHIFY_OUTPUT_PATH` - graphify output dir (gitignored). Default: `<repo>/schoolswp-brain/.graphify`.
- `GEMINI_API_KEY` - required only for `refresh --gemini`.

## Commands (run from repo root)

```
python schoolswp-brain/tools/graphify-brain/brain.py refresh --local
python schoolswp-brain/tools/graphify-brain/brain.py refresh --changed --dry-run
python schoolswp-brain/tools/graphify-brain/brain.py refresh --gemini --yes
python schoolswp-brain/tools/graphify-brain/brain.py query "what connects X to Y?"
python schoolswp-brain/tools/graphify-brain/brain.py explain "SomeNode"
python schoolswp-brain/tools/graphify-brain/brain.py path "A" "B"
```

- `refresh --local`: offline code AST (graphify) + local markdown structural index. Zero egress, no confirmation.
- `refresh --changed --dry-run`: lists new/modified files, what stays local vs what would go to Gemini, with a token/cost estimate. Sends nothing.
- `refresh --gemini`: replays the dry-run, runs a pre-send secret scan over the FULL Gemini corpus (all markdown under gemini roots, not just changed files), requires `--yes`, then re-processes that corpus with `gemini-2.5-flash`.

What is indexed is defined solely by `allowlist.yml`. Code is always extracted offline regardless of a root's `backend` tag; only markdown under a `gemini` root can ever egress, and only after an explicit `--yes`.
