# CAPABILITY-EXCHANGE-001 — terminal report

Lane closed. Verdict: **PASS_CAPABILITY_TRANSFER_AND_SETTLEMENT_001**.
Paid spend: $0.00 of $3.00 (fully offline, zero paid calls). One committed
transaction, no interruption, no threshold movement, no rescue.

Both sides operated by Terrynce on one host. Separate Ed25519 keys, separate
credential directories, separate signing subprocesses. This demonstrates the
authority boundary; it does not establish independent outside adoption.

## Stage 0 — archaeology / execution gate: PASS

Read-only inspection of openline-wallet, openline-airlock,
openline-receipt-gate found composable machinery for every required property:
Ed25519 identity + ReferenceGate principal pinning + DISTINCT_PARTIES_REQUIRED;
coordinator-001's receiver-owned evaluation ("never accepts a worker's
verdict"); Wallet scoped mandates + revoke(); ReferenceGate challenges and
per-action evaluate; coordinator-001 state machine + settle() + idempotent
SIM_USD bank; hash-chained sqlite event log; MANDATE_REVOKED gate stops;
settle idempotency + bank stable-key dedup; agreement digest + accept() payload
binding {job, candidate, evaluation}. No missing primitive; no new protocol
built. Adaptations A1–A4 (64-hex package hash submit; artifact-bound buyer
evaluation; verified invocation receipts; invocation-gated settlement) are
documented in apparatus/cx_coordinator.py.

## Capability

symptom_summarizer, version baseline — the frozen repair-process component
from SECOND-ORDER-APPARATUS-001. sha256
80d6bb6ea5198cbbc4ec4fa300704fd1b1a7254062da461cd59b49ea43bfb44b.
Real function, zero imports, bounded interface
summarize(probe_results, absent_files) -> dict, deterministic, 12 frozen
fixtures with expected labels predating this exchange. Not invented for it.

## The run (main)

agree (both parties, distinct principals) -> seller packages artifact +
signed manifest (package_hash 6ef470c4fbcd0cf6...) -> submit 64-hex hash ->
buyer-owned acceptance battery ELIGIBLE (10/12; schema, determinism,
accuracy, no-regression vs frozen 10/12 baseline, fixture integrity) ->
buyer accepts the exact evaluated package -> import into buyer lineage
(artifact hash re-verified) -> 4 fresh-work invocations by the buyer agent in
a separate process, each output recomputed by the receiver from the
hash-bound lineage artifact -> settlement: one payment of 250 SIM_USD,
buyer 10000 -> 9750, seller 0 -> 250, transfers = 1. Hash chain intact over
12 events. No payment existed before acceptance (pre-settle balances logged).

## Terminal conditions (14/14)

1. legitimate reusable capability packaged by A — yes
2. exact artifact/version/hash frozen — yes (FREEZE.md)
3. B independently accepts under B-owned criteria — yes, 10/12 ELIGIBLE
4. negative candidate rejected — yes (schema-violating candidate REJECTED)
5. accepted capability transfers intact — yes (import hash verified)
6. provenance bound — yes (lineage.json -> seller principal + package hash)
7. invocation on fresh work proven — yes (4/4, receiver-recomputed)
8. fresh work satisfies receiver condition — yes (labels matched)
9. settlement exactly once — yes (1 transfer)
10. rejection prevents settlement — yes (REJECTED -> settle blocked)
11. substitution/mutation prevents settlement — yes (IMPORT_BINDING_MISMATCH;
    wrong-version ARTIFACT_BINDING_MISMATCH; settle blocked)
12. replay cannot double-pay — yes (double settle + direct bank receipt replay
    -> same receipt, still 1 transfer)
13. buyer authority external to seller/capability — yes (PARTY_MISMATCH shown;
    buyer-owned receiver/coordinator)
14. tamper boundary holds — yes (fixture-write detected via T5 and rejected;
    altered battery -> BATTERY_INTEGRITY abort; altered agreement ->
    AGREEMENT_MISMATCH)

## Revocation control (existing machinery)

After settlement: buyer revoked the buyer-agent invoke mandate; a subsequent
invocation attempt through the receiver was denied (AUTHORITY_STOPPED:
MANDATE_REVOKED); the historical settlement receipt is byte-identical and the
state remains SETTLED. History preserved; future use denied.

## Claim (frozen ceiling, verbatim)

"One independently controlled agent transferred a reusable capability to
another; the buyer independently accepted the exact capability under its own
rules, invoked it on fresh work, and settled one simulated payment after
acceptance."

Seller and buyer were operated within this experiment. Separate
keys/processes demonstrate an authority boundary, not independent external
adoption. No claim is made about marketplaces, demand, economics, production
readiness, interoperability, adoption, recursive improvement, equilibrium,
receipt market value, or BUY-beats-BUILD.

## Disclosures

- Pre-contact build correction: this lane's battery initially transcribed the
  T4 baseline as 12/12; the frozen record is 10/12. Corrected before the live
  run; no frozen source altered.
- Pre-contact apparatus fixes during dry runs (documented in run log):
  candidate hash width 64-hex, float-free evidence canonicalization,
  PosixPath serialization in event log, subject_id role binding. All before
  scientific contact; none after.

## Unresolved

BUILD-vs-IMPORT is not authorized and was not started. The capability was
genuine but small and deterministic; transfer of stateful, networked, or
nondeterministic capabilities is untested. Revocation used mandate revocation;
long-horizon standing/expiry behavior untested. All earlier lanes untouched.
