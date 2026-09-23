# CX001 offline verification instructions

Everything below runs locally. No network, no paid calls, no live
experiment. Requires only Python 3 (stdlib).

## 1. Confirm these copies are byte-exact

From the repository root:

```
python3 tools/verify_evidence.py
```

It re-hashes every copied object against the digest declared in
`site/data/manifest.json` and fails nonzero on any mismatch. The CX001
copies are registered under keys `cx001_*`.

A digest match proves only that these copies are byte-exact — that the
evidence you are reading is the evidence that was frozen. It does not
prove the experiment was correct, the controls were sufficient, or the
claims are true. Those are questions for the frozen record and its stated
limits, below.

## 2. Check the frozen identifiers against the terminal report

`CX001_TERMINAL_EVIDENCE.json` carries the lane's frozen digests:

- `artifact_sha256` — the traded capability (`symptom_summarizer`, baseline)
- `package_hash` — the signed seller package
- `battery_sha256` — the buyer-owned acceptance battery
- `settlement` — one transfer of 250 SIM_USD (buyer 9750, seller 250)

The same values appear, quoted verbatim, in
CAPABILITY_EXCHANGE_001_TERMINAL_REPORT.md ("Terminal conditions", "The run
(main)") and were pinned in the pre-contact freeze
(CAPABILITY_EXCHANGE_001_PREREGISTRATION_FREEZE.md) before any scientific
contact.

## 3. Walk the run log

`CX001_EVENT_LOG.json` holds the coordinator's 12 hash-chained events of
the main run. The exact sequence, read from the log itself:

1. agree — buyer agrees (distinct buyer principal)
2. agree — seller agrees (distinct seller principal)
3. submit — seller submits the 64-hex package hash
4. evaluation — buyer-owned battery verdict (ELIGIBLE, accuracy 10/12)
5. accept — buyer accepts the exact evaluated package
6. import — artifact hash re-verified at import into the buyer lineage
7. invocation — fresh-work invocation 1 (receiver gate: ALLOWED)
8. invocation — fresh-work invocation 2 (ALLOWED)
9. invocation — fresh-work invocation 3 (ALLOWED)
10. invocation — fresh-work invocation 4 (ALLOWED)
11. payment_intent — settlement precondition recorded
12. settlement — one payment of 250 SIM_USD, transfers = 1

Each gate-checked event carries a gate receipt: `decision_authority` is the
buyer's receiver (RECEIVER_GATE), and the ALLOWED decisions are signed by
the gate. Events 4–6 and 11–12 are coordinator records without gate
receipts; their content is what the frozen terminal report quotes.

Independently checkable from this file: the sequence of kinds, the two
distinct principals, the ALLOWED gate decisions, and the single settlement
with one transfer. The event bodies also embed the parties' mandate
histories (mandate issue/revoke records with public keys and signatures —
no private keys); these are per-action mandate lifecycle records, not a
record of any single control.

## 4. Check the control runs (separate from the main log)

`CX001_CONTROL_EVENT_LOGS.json` exports the preserved coordinator event
logs of the seven frozen control runs, exported with no reconstruction:

- rejected: halted after event 4 (evaluation) — schema-violating candidate
- mutated: halted after event 5 (accept) — accepted artifact mutated
- wrong_buyer: halted after event 4 (evaluation) — seller-signed buyer accept
- wrong_version: halted after event 3 (submit) — delivered bytes != hash
- tamper_battery: halted after event 3 (submit) — altered battery
- tamper_fixture: halted after event 4 (evaluation) — fixture write attempt
- tamper_terms: halted after event 2 (agree) — altered agreement amount

What these logs show: each control run stopped at the frozen boundary,
with no event beyond the blocking step and no settlement in any of them.
What they do not show: the denial payloads themselves (e.g. the REJECTED
verdict text, the IMPORT_BINDING_MISMATCH / ARTIFACT_BINDING_MISMATCH /
PARTY_MISMATCH / BATTERY_INTEGRITY / AGREEMENT_MISMATCH reason strings)
were not preserved as standalone checkable records in this package. Those
outcomes are claims of the frozen terminal report (section "Terminal
conditions", items 10–14), not outcomes you can re-derive from the
published artifacts. They are report-only here, stated as such.

The post-settlement revocation control is likewise report-only in this
package: the terminal report describes the buyer revoking the buyer-agent
invoke mandate and the next receiver-gated invocation being denied
(MANDATE_REVOKED) with the settlement receipt unchanged. No standalone
denial receipt for that invocation is preserved in the published
artifacts; the MANDATE_REVOKED records embedded in the mandate histories
are lifecycle events, not the control's denial record. The wording stands
as the report gives it: "Future use through this receiver blocked."

## 5. Check the settlement bank state

`CX001_SETTLEMENT_BANK.json` shows final balances (buyer 9750, seller 250)
and a single transfer record — one payment, no double payment. Checkable
from this file: exactly one transfer exists. The replay control (double
settle + direct bank receipt replay producing the same receipt, still one
transfer) is report-only, per section 4 above.

## What these records do not let you claim

The frozen claim ceiling (verbatim) is:

"One independently controlled agent transferred a reusable capability to
another; the buyer independently accepted the exact capability under its
own rules, invoked it on fresh work, and settled one simulated payment
after acceptance."

Both sides were operated by Terrynce — separate keys and processes
demonstrate the authority boundary, not independent outside adoption.
No claim is made about marketplaces, demand, economics, production
readiness, interoperability, adoption, recursive improvement, equilibrium,
receipt market value, or BUY-beats-BUILD. The capability was genuine but
small and deterministic; stateful, networked, or nondeterministic
capabilities are untested.
