# openline-rsi replay data model — `openline.rsi.replay.v1`

The replay is rendered from structured data, not hand-coded UI states.
`site/data/replay.json` is the first investigation's data; `site/app.js`
renders it. `tools/validate_replay.py` enforces this contract and fails the
build on violation.

## Top-level shape

```json
{
  "schema": "openline.rsi.replay.v1",
  "investigation": {
    "id": "RSI-003",
    "title": "…",
    "question": "…",
    "arc": ["RSI-003", "RSI-004", "RSI-005"],
    "lineage": { "predecessor": null, "successor": "RSI-004" },
    "status": "completed"
  },
  "stages": [ … ],
  "earned": [ … ],
  "not_earned": [ … ],
  "standing": { "as_of": "…", "note": "…", "entries": [ … ] },
  "future_slots": [ … ]
}
```

## Stage

```json
{
  "key": "observed_result",
  "status": "frozen",
  "marker": "Observed",
  "marker_status": "observed",
  "plain": { "headline": "…", "body": "…" },
  "record": {
    "evidence_key": "rsi003_receipt",
    "record_type": "result receipt",
    "plain": "…what this record establishes, in ordinary words…",
    "limitations": ["…optional, encoded weaknesses…"]
  },
  "also": { "evidence_key": "…", "record_type": "…", "plain": "…" },
  "verdict": "FAIL_RSI_003_QUESTIONED_ANCESTRY_NOT_PROPAGATED",
  "claim_boundary": ["…optional, quoted from the record…"],
  "why_permitted": "…one line: why this transition was allowed…"
}
```

Rules:

- `status` is `"frozen"` or `"unresolved"`. Nothing else exists.
- A `"frozen"` stage **must** bind `record.evidence_key` to an entry in
  `site/data/manifest.json` (a verified copy with a SHA-256, or an external
  reference with a stated limitation). A frozen stage with no evidence
  binding is invalid and fails validation.
- An `"unresolved"` stage must carry an explicit label, must not carry a
  `verdict`, and renders as an empty slot. There is no schema state that
  looks complete while no result exists.
- Stage-level `"standing"` keys are forbidden. Historical verdict and
  current standing are separate: the verdict lives on the stage, standing
  lives only in the top-level `standing` object, dated via `as_of`.
- `earned` / `not_earned` are quoted from the records' own claim
  boundaries. The replay never invents them.
- `plain.headline` / `plain.body` translate the machinery into ordinary
  language first. Internal terms appear underneath, only where needed.

## Evidence manifest — `openline.rsi.evidence-manifest.v1`

```json
{
  "schema": "openline.rsi.evidence-manifest.v1",
  "copies": [
    {
      "key": "rsi003_receipt",
      "copy_path": "evidence/rsi-003/RSI_003_RECEIPT.json",
      "source_repo": "terryncew/openline-airlock",
      "source_path": "proofs/rsi-003/RSI_003_RECEIPT.json",
      "frozen_ref": "main commit c82f0242…",
      "record_type": "result receipt",
      "sha256": "81fae997…",
      "verification": "verified-copy"
    }
  ],
  "external_references": [
    {
      "key": "ril_001r_raw_result",
      "kind": "raw execution result",
      "ref": "https://…",
      "sha256": "26ceb940…",
      "limitation": "…why the bytes are not local…"
    }
  ]
}
```

`tools/verify_evidence.py` hashes every copy and fails on any mismatch.
External references must state their limitation; their absence is encoded,
never silently reconstructed.

## Contrast lanes — `openline.rsi.contrast.v1`

`site/data/contrast.json` holds subordinate lanes (e.g. the RIL
productivity history) under the same evidence-binding contract. Future
records plug in as new lanes or new entries — never as replacements.

## Future slots

Each slot: `{ "key", "label", "plain", "plug_in", "status": "unresolved" }`.
`plug_in` names the exact location a future record will occupy:

- `productivity_result` → the RIL contrast lane grows (`contrast.json`).
- `replication` → `site/data/replication-*.json`, same replay schema,
  linked from the replicated stage.
- `correction_demonstration` → a new event in the top-level `standing`
  object. The historical verdict stays frozen; the correction attaches
  after it.
