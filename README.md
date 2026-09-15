# openline-rsi

**Watch an AI improve how it researches — and inspect why each improvement was allowed to survive.**

A recorded-replay product for recursive self-improvement research. v0 renders one completed investigation — the RSI-003 → RSI-004 → RSI-005 lineage arc — from frozen evidence, plus the earlier RIL productivity work as a contrast lane with its negative results preserved.

## What this is

A **presentation layer**. It renders frozen scientific records so a stranger can watch an investigation unfold and inspect the evidence behind every transition. It answers, in ordinary English: what was it trying to learn, what did it expect, what actually happened, what changed because of that, and why that change was allowed to survive.

## What this is not

- Not a dependency of Airlock or of RSI-006.
- Not an experiment runner.
- Not an alternate receipt authority.
- Not a place that modifies or repairs historical evidence.
- Not a new scientific mechanism.

The source repositories and their frozen records remain authoritative. `openline-rsi` renders them.

## Repository layout

```
site/                  the static experience (open site/index.html, or serve the dir)
  templates/           hand-editable page templates (data injected at build)
  data/
    replay.json        the first investigation, in the replay data model
    contrast.json      subordinate lanes (RIL productivity history)
    manifest.json      evidence manifest: source paths, digests, verification
  app.js               renders the pages from the inlined data (no backend)
evidence/              frozen record copies, hash-pinned (never edited)
tools/
  build.py             injects data into templates -> site/*.html (deterministic)
  verify_evidence.py   hashes every copied record; fails on any mismatch
  validate_replay.py   enforces the data contract; fails on violation
SCHEMA.md              the replay data model
```

## Working with it

```bash
python3 tools/build.py             # rebuild the pages from site/data/*.json
python3 tools/verify_evidence.py   # confirm every copied record still matches its digest
python3 tools/validate_replay.py   # confirm every earned stage binds to evidence
# then open site/index.html in a browser (no server, no credentials needed)
```

Edit the data in `site/data/*.json` or the templates in `site/templates/`,
then rebuild. Never edit `site/index.html` / `site/investigations.html`
directly — they are build outputs.

## Provenance

v0 evidence: 16 frozen records copied from `terryncew/openline-airlock`
(main `c82f0242e6556bbc8d920291f444090b526adeee`) and 2 design drafts from
the local workspace, plus 1 external reference (RIL-001R raw result bytes,
GitHub artifact only — limitation stated in the manifest). See
`site/data/manifest.json` and the Methods & provenance page.

## Product boundary

This repository must not grow into a dashboard, a governance console, an
experiment framework, or a receipt authority. One investigation dominates;
evidence is one click down; unresolved future slots render as explicitly
empty. See `SCHEMA.md` for the data contract that keeps it honest.
