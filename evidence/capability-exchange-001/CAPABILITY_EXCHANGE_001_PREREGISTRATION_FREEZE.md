# CAPABILITY-EXCHANGE-001 — pre-contact freeze

Frozen before any scientific contact. After contact: no threshold tuning,
no replacing failed tasks, no changing the capability, buyer acceptance,
settlement conditions, or success criteria. No rescue rerun under this label.

## Stage 0 outcome

Repository archaeology (read-only) of openline-wallet, openline-airlock,
openline-receipt-gate found composable machinery for every required property:

| required property | existing primitive | composition |
|---|---|---|
| agent identity / authority boundary | openline_wallet.crypto (Ed25519), ReferenceGate.pin_principal, coordinator DISTINCT_PARTIES_REQUIRED | separate keys/processes for A and B |
| Airlock acceptance | coordinator-001 evaluate(): receiver-owned local evaluation, never accepts worker verdict; airlock.sieve protected-files principle | buyer-owned deterministic battery on exact artifact |
| Wallet authority | openline_wallet.wallet grant/revoke scoped mandates, bundles | per-action scoped mandates; invoke-mandate revocation |
| Receipt Gate | openline_wallet.receiver.ReferenceGate | challenges, presentations, per-action evaluate |
| coordinator / settlement | coordinator-001 Coordinator + settle() + bank() | state machine subclass; SIM_USD; stable-key idempotent dedup |
| lineage / provenance | coordinator sqlite hash-chained event log | manifest + import record bound to seller principal |
| standing / revocation | Wallet.grant expires_at + revoke(); gate returns MANDATE_REVOKED; coordinator preserves observed revocation | invoke-mandate revocation control |
| replay protection | settle() idempotent on SETTLED; bank stable-key dedup | double-settle / receipt replay -> single payment |
| exact artifact/version binding | agreement digest; accept() payload binding {job,candidate,evaluation} | 64-hex sha256 package hash bound at submit/accept/import/invocation |
| effect closure | n/a — pure-computation capability | stated not applicable |

No missing primitive. Gate PASSES. No new protocol primitive is built;
adaptations A1–A4 are documented in apparatus/cx_coordinator.py.

## Chosen capability

`symptom_summarizer`, version `baseline` — the frozen repair-process component
from SECOND-ORDER-APPARATUS-001 (read-only source; bytes copied, hash-verified).

- sha256: 80d6bb6ea5198cbbc4ec4fa300704fd1b1a7254062da461cd59b49ea43bfb44b
- real function: summarizes probe results into the symptom summary a repair
  proposer reads (tally non-ok tasks by component; documented tie/edge rules)
- bounded interface: summarize(probe_results, absent_files) -> dict
- dependencies: none (zero imports; stdlib language only)
- independently testable: deterministic; 12 frozen fixtures with expected labels
- acceptance does not depend on hidden seller knowledge: expected labels are
  frozen records predating this exchange, derived from the documented rule
- not invented for this exchange; not staged to pass

## Parties

- Seller Agent A: principal openline:principal:a84f9961655979d8a6dbf4e7b869fd187a956f92d53d89b1e7977b6ae252deaa
- Buyer Agent B: principal openline:principal:2c722570a8281049c0e113ffca1880286e86218f11baa07fdc1d9002d3235f8a
- Buyer-controlled receiver: buyer's ReferenceGate + coordinator sqlite
- Both sides are operated by Terrynce on one host. Separate keys, credential
  dirs, and signing subprocesses demonstrate the authority boundary.
  They do NOT establish independent outside adoption.

## Package

package_hash = sha256(artifact_bytes || 0x00 || canonical_json(manifest minus signatures))
Manifest binds: name, version, artifact filename, declared scope, dependencies,
runtime requirements, seller principal, asking price, provenance (source record),
signatures (seller Ed25519 over canonical manifest).

## Buyer acceptance criteria (buyer-owned, frozen)

Battery: apparatus/acceptance_battery.py, sha256 pinned in terms.
12 fixtures (byte-copies of frozen records). Bar, all required:
- T1 schema PASS, T2 determinism PASS, T3 accuracy >= 10/12,
  T4 no-regression (accuracy == frozen baseline 10/12),
  T5 fixture integrity (no test-time modification).
Negative candidate required to be rejected (see controls).

## Fresh work (frozen)

apparatus/fresh/w01..w04.json — 4 new fixtures, task_ids disjoint from the 12
acceptance fixtures, expected labels frozen pre-contact. Not in seller
construction, not in buyer acceptance, ordinary use, independently checkable.

## Price and settlement

- Asking price: 250 SIM_USD (integer, simulated only)
- Settlement condition (all required, frozen): buyer acceptance receipt exists;
  imported artifact hash == accepted package hash; verified invocation evidence
  recorded for the accepted artifact; amount/currency/parties match terms;
  receiver settle decision.
- Settlement occurs only after all conditions; exactly one payment.

## Negative controls (frozen)

1. rejected capability (schema-violating candidate) -> REJECTED, no settlement
2. accepted artifact mutated before import/use -> binding mismatch, denied, no settlement
3. settlement replay (second settle call; direct bank receipt replay) -> no double payment
4. wrong buyer (seller signs buyer accept) -> PARTY_MISMATCH
5. wrong version (delivered bytes != submitted hash) -> ARTIFACT_BINDING_MISMATCH
6. tamper: capability attempts fixture modification at import -> detected (T5), rejected
7. tamper: altered acceptance battery file -> BATTERY_INTEGRITY abort
8. tamper: altered agreement amount -> AGREEMENT_MISMATCH / exclusive init

## Revocation control (existing machinery, no new mechanism)

After settlement: buyer revokes the buyer-agent invoke mandate; a subsequent
invocation attempt through the receiver must be denied (MANDATE_REVOKED);
the historical settlement receipt must remain unchanged.

## Success criteria

PASS_CAPABILITY_TRANSFER_AND_SETTLEMENT_001 iff all 14 terminal conditions
hold (work order verbatim). Otherwise the narrow terminal result is frozen.

## Build correction (pre-contact, disclosed)

During apparatus dry-run (before any scientific contact), the battery's T4
baseline was transcribed as 12/12; the frozen record
(second-order-apparatus-001/hidden_files/acceptance/holdout_tests.py,
BASELINE_ACCURACY = 10/12) is 10/12. Corrected to 10/12 before the live run.
No frozen source record was altered; the error was in this lane's new battery
file only. Battery sha256 is pinned in the agreement terms at run time.

## Budget

Paid exposure bound: $0.00 (fully offline, zero paid calls). Cap: $3.00.
Balance freeze recorded in hidden_files/balance_freeze.json.

## Claim ceiling (verbatim)

If PASS: "One independently controlled agent transferred a reusable capability
to another; the buyer independently accepted the exact capability under its own
rules, invoked it on fresh work, and settled one simulated payment after
acceptance." Plus: seller and buyer were operated within this experiment.
Separate keys/processes demonstrate an authority boundary, not independent
external adoption. None of the excluded claims (marketplace, demand, economics,
production readiness, interoperability, adoption, recursive improvement,
equilibrium, receipt market value, BUY-beats-BUILD).
