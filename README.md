# openline-rsi

This repository replays a real investigation into recursive self-improvement — a system that revises its own research method, one generation at a time — from frozen records: predictions written down before each run, results recorded after. You can step through what the system tried to learn, what it expected, what actually happened, and why each change to the method was allowed to survive. Every step links to the evidence behind it.

Claims about self-improving AI are usually stories told after the fact. This one you can check.

## The investigation

The system under study keeps an installed policy for each generation of its own research method. The question that started everything: when the evidence behind the first generation's policy was reopened and that generation's standing changed to "questioned," would the doubt travel down to the second generation — which had inherited the first generation's policy — or would the system keep building on a questioned foundation?

**RSI-003** ran that question as a preregistered experiment. The prediction, written down before execution, was blunt: the system would fail. The component that assigns standing to each generation was known to look at one generation at a time — it took no lineage input — so the second generation would keep its inherited standing even after the first was questioned. The run confirmed the prediction exactly: formal verdict `FAIL_RSI_003_QUESTIONED_ANCESTRY_NOT_PROPAGATED`. A forged reopening message was rejected along the way; installed references were byte-identical at every checkpoint.

The failure was then locked, not fixed. RSI-003 is permanently closed under that ID — no rerun, no repair, no tuning. The recorded finding: recursive inheritance exists, but questioned standing does not propagate through inherited ancestry.

The lesson — doubt has to travel down the lineage, not stop at the generation where it started — was not applied as a patch. It was frozen as a new experiment with its own ID, its own preregistration, and its own verdicts. **RSI-004** tested a component redesigned to walk the lineage — a *lineage-aware projector*, in the records' term. Its run crashed in under a second: the runner expected a `state/` directory that was never created, so writing the phase token raised `FileNotFoundError`. Zero of twelve phases ran. No verdict of any kind — a failed run, not a failed hypothesis. RSI-004 is permanently closed as a harness failure.

**RSI-005** tested the redesigned component under its own ID and its own preregistration. After the reopening, all three generations became questioned — the doubt propagated down the lineage. An admission probe for a never-executed fourth generation was denied. Receipts and installed references were unchanged. Formal verdict: `PASS_RSI_005_LINEAGE_AWARE_INHERITANCE`. RSI-003 and RSI-004 stayed exactly as frozen; the PASS does not re-litigate either one.

What the arc earned: questioned standing must propagate along the lineage — and a redesigned component that passed its own preregistered tests. What it did not earn: the productivity claim — whether any of this makes later research cheaper per verified result. That question belonged to a later test.

That later test was RSI-006. It never ran.

## What you can see here

**The replay.** Open `site/index.html` in a browser — no server, no credentials. It walks the investigation stage by stage: question, prediction, run, verdict, lock, and the two successor experiments. Each stage links directly to the frozen record it came from.

**The evidence.** `evidence/` holds the frozen records the replay is built from: design drafts, preregistrations, result receipts, and freeze notes for RSI-003, RSI-004, and RSI-005, the earlier productivity attempt, and the terminal RSI-006 branch (the Q6 preregistration and the Gate-2A NO-GO freeze record). The records are hash-pinned and never edited; `site/data/manifest.json` lists every record with its source and digest.

**How the records were produced and checked.** The Methods & provenance page (`site/methods.html`) describes the record types, the verification steps, and the known limitations — including the one external reference that exists only as a GitHub artifact.

## The productivity question, and where it stands

Before this arc, the productivity question — does governed recursive improvement actually produce more verified progress per dollar? — was asked once on live infrastructure as RIL-001R. The verdict was `INCONCLUSIVE_RIL_001R_LIVE_EXECUTION`: negative evidence, preserved rather than hidden. It appears here as a contrast lane.

RSI-006 was the next attempt at that question, not the first. It never ran.

I tried to get to a preregistered test of whether an AI improvement process could improve itself. I stopped before the productivity experiment because the final execution substrate violated a complexity limit written down in advance. The mechanism repair worked. The qualification architecture exceeded the bound. Here is the record.

Concretely: RSI-006's Q6 line first repaired the coordinator-death recovery mechanism — Gate 1 stands as `Q6_MECHANISM_HOLDS`. But the frozen Q6 preregistration required the final environment-qualification binding to be a thin wrapper of at most 150 lines, with an explicit stop written in advance: if binding the new execution surface to the qualification machinery required a large new qualification framework, STOP and return NO-GO. The construction that implemented the desired qualification semantics needed roughly 960 lines across the new qualification layer — `q6_receipt.py` grew to 463 lines and a new `q6_stage1.py` added 497 — while passing all 77 of its correctness fixtures. Correctness passed; boundedness failed. Gate 2A therefore terminated pre-contact as `NO_GO_Q6_QUALIFICATION_BINDING_COMPLEXITY`. That is not a NOT_QUALIFIED substrate verdict: no Stage 1 ran, no environment receipt was frozen, no scientific contact occurred. RSI-006 productivity execution is permanently unauthorized under this preregistration. There is no Q7.

The credibility point is that the stop rule actually stopped us. The productivity question itself — whether inherited improvement beats the unchanged process per dollar on fresh work — remains unanswered, and no further attempt is currently authorized. The terminal branch is preserved as its own contrast lane, not hidden.

## What's unresolved

- **Productivity result.** The planned RSI-006 productivity test was not authorized under its frozen protocol — the Q6 substrate line ended pre-contact at `NO_GO_Q6_QUALIFICATION_BINDING_COMPLEXITY`. The question itself remains unanswered.
- **Independent replication.** No result in this replay has been independently replicated.
- **Integrated correction.** Not yet demonstrated.

The first slot above is not simply "open": RSI-006, the planned vehicle, is terminally closed and will not fill it. These render in the replay as explicitly empty slots.

## Running it

```bash
python3 tools/build.py             # rebuild the pages from site/data/*.json
python3 tools/verify_evidence.py   # confirm every copied record still matches its digest
python3 tools/validate_replay.py   # confirm every earned stage binds to evidence
# then open site/index.html in a browser
```

Edit the data in `site/data/*.json` or the templates in `site/templates/` and rebuild. `site/index.html` and `site/investigations.html` are build outputs — don't edit them directly.

## Where things live

```
site/
  index.html, investigations.html, methods.html   built pages (open index.html to start)
  templates/          page templates; data is injected at build time
  data/
    replay.json       the RSI-003 → RSI-004 → RSI-005 investigation
    contrast.json     the RIL productivity history and the terminal RSI-006 branch
    manifest.json     every evidence record: source path, digest, verification
  app.js              renders the pages from the inlined data (no backend)
evidence/             frozen record copies, hash-pinned (never edited)
tools/
  build.py            injects data into templates -> site/*.html (deterministic)
  verify_evidence.py  hashes every copied record; fails on any mismatch
  validate_replay.py  enforces the data contract; fails on violation
SCHEMA.md             the replay data model (openline.rsi.replay.v1)
CONTRIBUTING.md       contributor guidance and repository scope
```

## Provenance

v0 evidence: 16 frozen records copied from `terryncew/openline-airlock` (main `c82f0242e6556bbc8d920291f444090b526adeee`), 2 design drafts from the local workspace, and 1 external reference (RIL-001R raw result bytes, GitHub artifact only — the limitation is stated in the manifest). The RSI-006 terminal branch added 2 more frozen records from `terryncew/openline-airlock` at main `d3b29da9a83c8ee65ee095fae1b052460e08ece3` (the Q6 preregistration, frozen at its PR #166 merge `b947b3d3151432975e2c722f8647e593cd3ab257`, and the Gate-2A NO-GO freeze record from PR #169). The source repositories and their frozen records remain authoritative.
