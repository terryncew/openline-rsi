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

`CX001_EVENT_LOG.json` holds the coordinator's 12 hash-chained events:

1. agree — both parties, distinct principals
2. submit — 64-hex package hash
3. accept — buyer ELIGIBLE verdict, accuracy 10/12
4–7. invoke — 4 fresh-work invocations, each output recomputed by the
   receiver from the hash-bound lineage artifact
8. settle — one payment of 250 SIM_USD, transfers = 1
9–12. control events and post-settlement revocation records

Each event embeds its decision authority and epoch certificate; the chain
is append-only — the frozen report notes "hash chain intact over 12 events".

## 4. Check the settlement bank state

`CX001_SETTLEMENT_BANK.json` shows final balances (buyer 9750, seller 250)
and a single transfer record — one payment, no double payment. The negative
controls (rejected candidate, mutated artifact, double settle, receipt
replay, wrong buyer, wrong version, tamper attempts) are narrated in the
terminal report's "Terminal conditions" section; their frozen status is
the report itself, not an attached second database.

## 5. Confirm the revocation boundary

After settlement the buyer revoked the buyer-agent invoke mandate; the next
invocation attempt through the receiver was denied (MANDATE_REVOKED) while
the historical settlement receipt is byte-identical and the state remains
SETTLED. The exact wording: "Future use through this receiver blocked" —
the revocation denies gated future use; it does not claim exported code was
erased or all use prevented.

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
