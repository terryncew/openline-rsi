# OpenLine RSI

**Recursive self-improvement. Open to inspection.**

What happens when an AI improves the way it improves itself?

One version can learn something and pass that lesson to the next version. But what if the original lesson turns out to be wrong?

Does the mistake keep spreading?

That’s what this project tested.

The first version failed. It kept trusting an inherited conclusion after the evidence behind it had been questioned.

A later version fixed that specific problem: the doubt traveled forward, and the next inheritance was blocked.

Then the research hit its stop rule.

We did **not** prove that the AI became more productive at improving itself.

Everything is here so you can see what happened for yourself.

- [Replay the experiment](https://terryncew.github.io/openline-rsi/) — step through what happened, stage by stage
- [Open the evidence](https://github.com/terryncew/openline-rsi/tree/main/evidence) — the frozen records behind every claim
- [See how to build a test like this](#build-your-own-investigation) — the method, so you can copy the structure

## What happened?

Version 1 learns something
↓
Version 2 inherits it
↓
The original evidence gets questioned
↓
Version 2 still trusts it

**That failed.**

Then:

New mechanism
↓
The doubt travels forward
↓
Later versions lose permission to inherit the bad foundation

**That passed its test.**

## Where did it stop?

We wanted to test whether this actually made the AI better at improving its own research process.

That experiment never started.

The rules written beforehand said to stop if preparing the test became too complicated.

It did.

So we stopped.

`Recursive productivity advantage was not established.`

The exact stop record lives below in the technical section. The short version is: the experiment never started because its own rules said to stop.

## Replay the experiment

Open the replay in your browser — no server, no credentials:

[https://terryncew.github.io/openline-rsi/](https://terryncew.github.io/openline-rsi/)

It walks through each investigation stage by stage: the question, what was predicted, what actually happened, and what was earned. Each stage links directly to the frozen record it came from.

`site/investigations.html` holds the subordinate lanes and the explicitly empty future slots — the places where the record says "nothing here."

## Inspect the evidence

The records are copies, made once and never edited. You can check them yourself:

```bash
python3 tools/verify_evidence.py   # confirm every copied record still matches its fingerprint
python3 tools/validate_replay.py   # confirm every stage in the replay points to real evidence
```

`site/data/manifest.json` lists every record with its source and fingerprint. The Methods page (`site/methods.html`) describes the record types, the verification steps, and the known limitations.

Claims about self-improving AI are usually stories told after the fact. This one you can check.

## Want the technical version?

This is where the precise language lives. The story above is accurate; what follows is the machinery.

`openline-rsi` is a statement repository: evidence-backed claims plus a legible method you can copy. It replays what was predicted, what actually happened, what evidence survives, and what claim was earned — for each investigation, including the ones that failed, crashed, or stopped before contact.

It is not the Airlock runtime, a teaching starter, a generic agent framework, a product SDK, or a graveyard of experiment reports. Airlock remains the thing you can adopt operationally; this repo is where the claims about the method are kept checkable.

### The investigations, precisely

The system under study keeps an installed policy for each generation of its own research method. The question that started everything: when the evidence behind the first generation's policy was reopened and that generation's standing changed to "questioned," would the doubt travel down to the second generation — which had inherited the first generation's policy — or would the system keep building on a questioned foundation?

**RSI-003** ran that question as a preregistered experiment. The prediction, written down before execution, was blunt: the system would fail. The component that assigns standing to each generation was known to look at one generation at a time — it took no lineage input — so the second generation would keep its inherited standing even after the first was questioned. The run confirmed the prediction exactly: formal verdict `FAIL_RSI_003_QUESTIONED_ANCESTRY_NOT_PROPAGATED`. A forged reopening message was rejected along the way; installed references were byte-identical at every checkpoint.

The failure was then locked, not fixed. RSI-003 is permanently closed under that ID — no rerun, no repair, no tuning. The recorded finding: recursive inheritance exists, but questioned standing does not propagate through inherited ancestry.

The lesson — doubt has to travel down the lineage, not stop at the generation where it started — was not applied as a patch. It was frozen as a new experiment with its own ID, its own preregistration, and its own verdicts. **RSI-004** tested a component redesigned to walk the lineage — a *lineage-aware projector*, in the records' term. Its run crashed in under a second: the runner expected a `state/` directory that was never created, so writing the phase token raised `FileNotFoundError`. Zero of twelve phases ran. No verdict of any kind — a failed run, not a failed hypothesis. RSI-004 is permanently closed as a harness failure.

**RSI-005** tested the redesigned component under its own ID and its own preregistration. After the reopening, all three generations became questioned — the doubt propagated down the lineage. An admission probe for a never-executed fourth generation was denied. Receipts and installed references were unchanged. Formal verdict: `PASS_RSI_005_LINEAGE_AWARE_INHERITANCE`. RSI-003 and RSI-004 stayed exactly as frozen; the PASS does not re-litigate either one.

What the arc earned: questioned standing must propagate along the lineage — and a redesigned component that passed its own preregistered tests. What it did not earn: the productivity claim — whether any of this makes later research cheaper per verified result.

### The productivity question, precisely

That productivity question was asked once on live infrastructure as RIL-001R. The verdict was `INCONCLUSIVE_RIL_001R_LIVE_EXECUTION`: negative evidence, preserved rather than hidden. It appears here as a contrast lane.

RSI-006 was the next attempt at that question, not the first. The planned productivity test was not authorized under its frozen protocol. Q6's mechanism repair held, but qualification required more new architecture than the preregistered bound allowed, so the experiment stopped before scientific contact.

The full terminal branch — preregistration, mechanism result, and the Gate-2A freeze record (`NO_GO_Q6_QUALIFICATION_BINDING_COMPLEXITY`) — is preserved as its own contrast lane, not hidden. The productivity question itself remains unanswered, and no further attempt is currently authorized.

### What's unresolved

- **Productivity result.** The planned RSI-006 productivity test was not authorized under its frozen protocol. The question itself remains unanswered.
- **Independent replication.** No result in this replay has been independently replicated.
- **Integrated correction.** Not yet demonstrated.

These render in the replay as explicitly empty slots.

## Build your own investigation

The pattern this repo demonstrates, in seven steps:

1. Pick a consequential claim you want to test.
2. Write down beforehand what would count, what would falsify it, and what must stay frozen — a preregistration, not a plan you edit after seeing results.
3. Separate the thing being tested from the machinery that decides whether the evidence counts. A receiver you don't control defines "better"; you never grade your own homework.
4. Run the test through receiver-owned checks, and preserve the receipts.
5. Keep positive, negative, failed, and stopped runs as frozen records. Never rewrite them; never hide the unfavorable branch.
6. Publish a replayable statement whose evidence anyone can verify independently. `SCHEMA.md` defines the data model this repo uses (`openline.rsi.replay.v1`); `site/methods.html` states the honesty rules the validator enforces.
7. If a result earns something useful, that mechanism can then become part of a product, workflow, service, or other system. That operational step lives outside this repo — in Airlock's case, Airlock itself is the thing people adopt.

That is what a reader should be able to take away: "I understand how this was done, I can verify it, and I could structure one of my own claims this way."

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
    contrast.json     subordinate lanes: the RIL productivity history, the terminal RSI-006 branch
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
