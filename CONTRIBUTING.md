# Contributing to openline-rsi

## Scope

This repository renders frozen scientific records. It must not grow into a
dashboard, a governance console, an experiment framework, or a receipt
authority.

Concretely, it is not:

- a dependency of Airlock or of RSI-006,
- an experiment runner,
- an alternate receipt authority,
- a place that modifies or repairs historical evidence,
- a new scientific mechanism.

The source repositories and their frozen records remain authoritative.
`openline-rsi` renders them.

## Working rules

- One investigation dominates the replay. Subordinate lanes stay subordinate.
- Every rendered claim binds to evidence one click down.
- Unresolved future slots render as explicitly empty — never as implied
  progress.
- `site/index.html` and `site/investigations.html` are build outputs. Edit
  `site/data/*.json` or `site/templates/` and rebuild with
  `python3 tools/build.py`.
- `evidence/` is never edited. To correct a copy, re-copy from the source
  and update the manifest.
- `tools/validate_replay.py` enforces the data contract in `SCHEMA.md`;
  the build fails on violation.
