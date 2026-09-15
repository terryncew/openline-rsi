# RSI-003 — recursive standing propagation (design, decided 2026-09-14)

Base: green main `d4da44a`. Dependency (unchanged, exercised as-is):
`openline-verified-memory@454c5a3b28f2b7da673f6acf0007fc1d7b6f4d8e`.

## Question

RSI-001 proved a single generation's standing moves inherited → questioned
when its support evidence collapses. RSI-002 proved the generator can improve
without capturing the evaluator. Neither tested recursion: what happens to
the *second* generation when the *first* generation's evidence collapses?

**When gen1's receiver evidence is reopened, does questioned standing
propagate to gen2, which inherited from gen1's installed policy — or does
the system keep building on a questioned foundation?**

This is the correct next rung: it proves whether recursive inheritance has
consequence-bearing lineage. It does not earn the final RSI claim — that
later test still needs an inherited method mutation to beat its unchanged
parent on fresh verified results per dollar.

## Decided calls (Terrynce, 2026-09-14)

1. **Projector exercised unchanged.** Multi-generation propagation is treated
   as *not established* unless the current projector proves transitive
   closure. RSI-003 runs `derive_airlock_memory` exactly as pinned. If it
   walks lineage transitively, the experiment becomes the explicit proof.
   If it does not, that is the hole — documented, not patched, under this ID.
2. **Gen2 runs under gen1's installed policy.** The receiver, evaluator,
   projector, and install authority stay frozen; gen2's *generator* is bound
   to the exact installed gen1 ref/hash. Gen2 earns its own promotion from
   that inherited state. Otherwise this is two generations from the same
   frozen parent, not recursion. This gives the REOPEN something real to
   propagate through.
3. **Canonical verdicts** (below). Installed-byte mutation is a separate
   invariant failure: REOPEN changes standing, not history.

## Projector finding (current main)

`derive_airlock_memory` (evidence.py @454c5a3b) derives standing for **one
lesson at a time** from its own generation + promotion + standing records.
It takes no lineage input: no parent promotion hash, no ancestry walk, no
transitive closure. `established()` filters per-memory status only.

Consequence: a REOPEN bound to gen1's promotion receipt questions gen1, but
gen2's derivation never looks at gen1. **Predicted result:
FAIL_RSI_003_QUESTIONED_ANCESTRY_NOT_PROPAGATED**, with the hole documented
exactly: the projector has no consequence-bearing lineage across
generations. The experiment must not implement its own transitive walk —
that would be patching around the falsifier.

## Invariant

`standing follows lineage` (asserted, under test): a generation's standing
can be no cleaner than the standing of the generation it inherited from.
Questioning is monotonic down the chain. Installation is history; standing
is judgment.

## Sequence (synthetic; deterministic fake Hermes through the real Nightshift path)

1. Gen1: the exact RSI-001 earned-inheritance sequence. Gen1 installed at
   receiver-owned ref R1; standing `inherited`; gen1 in the established set.
   Record R1 bytes hash before and after every later step.
2. Gen2: Nightshift runs with gen2's generator bound to the exact installed
   gen1 ref/hash (R1). It selects an ordinary-code winner built on gen1's
   installed state. The receiver installs the exact selected commit at ref
   R2; standing `inherited` via the unchanged projector. Gen2's lineage
   record cryptographically binds gen1's promotion receipt hash
   (recorded as evidence; the projector is not required to consume it —
   that is what is under test).
3. Precondition check: gen1 and gen2 both `inherited`, both in the
   established set, gen2 lineage-bound to gen1, R1/R2 byte-hashes recorded.
   If any check fails: INCONCLUSIVE_RSI_003_PRECONDITION_FAILURE.
4. Controlled support-witness removal for *gen1's* promotion evidence, then
   a receiver-signed REOPEN(gen1).
5. A new process reconstructs standing from disk only (as in RSI-001) and
   reprojects gen1 and gen2 through the unchanged projector.
6. Negative controls:
   a. A gen3 candidate proposed from the questioned gen2 line earns zero
      inheritance — the gate refuses before installation.
   b. A forged REOPEN (invalid signer) changes no standing anywhere.
7. Final invariant check: R1 and R2 byte-identical to step 3. Any mutation:
   FAIL_RSI_003_INSTALLED_REF_MUTATION (reported as the cause code even if
   standing outcomes are otherwise as predicted).

## Pass condition (tight)

ALL of the following, in order:

- Gen1 and gen2 are both established (standing `inherited`, in the
  established set) before REOPEN.
- Gen2 is cryptographically and structurally bound to gen1's installed
  policy (gen2's generator ran against R1's exact bytes; gen2's lineage
  record binds gen1's promotion receipt hash).
- REOPEN invalidates gen1's receiver evidence (signed, valid signer,
  bound to gen1's promotion receipt).
- Reprojection questions gen1 AND gen2 through the unchanged projector.
- Neither gen1 nor gen2 remains in the established set.
- R1 and R2 are byte-identical before and after REOPEN.

## Verdicts

- `PASS_RSI_003_RECURSIVE_STANDING_PROPAGATION` — all pass conditions hold.
  Recursive inheritance has consequence-bearing lineage.
- `FAIL_RSI_003_QUESTIONED_ANCESTRY_NOT_PROPAGATED` — gen2 (or any
  descendant) retains clean standing after its ancestor is questioned.
  Predicted given the projector finding above; the failure *is* the result.
- `FAIL_RSI_003_INSTALLED_REF_MUTATION` — separate invariant failure/cause
  code: any installed-ref byte mutation at any point. REOPEN changes
  standing, not history.
- `INCONCLUSIVE_RSI_003_PRECONDITION_FAILURE` — the propagation question
  could not be asked (gen1/gen2 failed to establish, lineage binding
  unverifiable, or controls misbehaved before REOPEN).

## Falsifiers (what each verdict rules out)

- PASS rules out: propagation failure, established-set leakage, ref
  mutation, inheritance from a questioned line, forged-REOPEN effects.
- FAIL (ancestry not propagated) rules in the documented hole: standing
  does not follow lineage in the current projector.
- INCONCLUSIVE rules out nothing about propagation; it reports that the
  experiment could not put the question to the mechanism.

## Claim boundary

- Two generations only. Not a claim about open-ended recursion, and not
  the final RSI claim (inherited method mutation beating its unchanged
  parent on fresh verified results per dollar — a later test).
- Same boundaries as RSI-001/RSI-002: controlled synthetic evidence,
  deterministic fake Hermes through real Nightshift, isolated synthetic Git
  refs (no production deployment), no hostile-process-isolation claim,
  no paid live-Hermes claim.
- Controlled witness removal is a missing-witness falsifier, not a general
  evidence-loss detector.
- The predicted FAIL is a finding about the current projector, not a
  defect in the experiment. Patching the projector belongs to a new
  experiment ID, after this falsifier is on record.

## Anti-rescue (mirrors RSI-001/RSI-002)

After the first pushed RSI-003 run, do not change the generation count,
the unchanged-projector rule, REOPEN semantics, lineage binding rule,
verdicts, or falsifiers under the RSI-003 identifier. A failure requires
a new experiment ID — including (especially) the predicted propagation
failure.

---
*Design decided 2026-09-14. No experiment code written. Next step on
Terrynce's word: preregistration + implementation.*
