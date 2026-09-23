# CX001 replay note — frozen demonstration vs. new experiment

CAPABILITY-EXCHANGE-001 is a closed scientific lane. Its frozen records —
the terminal report, the pre-contact freeze, the frozen identifiers, the
12-event run log, and the settlement bank state — are not edited in this
package and are not to be re-run under this label. The lane terminalized on
2026-09-23 with verdict PASS_CAPABILITY_TRANSFER_AND_SETTLEMENT_001.

A repeat of a frozen demonstration is not a new scientific experiment.
Neither is needed for this release. What follows distinguishes the two:

- The experiment: the live lane run on 2026-09-23, one committed
  transaction, $0.00 of $3.00 spent, fully offline. It earned the frozen
  claim quoted in CAPABILITY_EXCHANGE_001_TERMINAL_REPORT.md and nothing
  beyond the frozen ceiling.
- The demonstration: `cx001-demo.mp4`, a 38-second rendered replay built
  from the recorded results, labeled on screen throughout as
  "Replay of recorded results". It re-shows the recorded steps in order —
  acceptance, fresh-work invocation, single simulated payment, substitution
  refused, replay paying once, revocation blocking the next gated use.
  It introduces no new output, no new acceptance score, no new timestamp,
  and no new payment event. It is a telling of the record, not new evidence.

The video's on-screen plain language is a summary for a sound-off viewer.
Exact identifiers, hashes, and the full receipt live in this directory —
they were deliberately kept out of the video.

## Disclosures carried into the video

- Local prototype; simulated payment (250 SIM_USD; no real money).
- Both agents operated by Terrynce on one host — separate Ed25519 keys,
  separate credential directories, separate signing subprocesses. The
  authority boundary is demonstrated; independent outside adoption is not
  established and is not claimed.

No new experiment was run to produce this package. No paid API calls were
made. The frozen evidence is byte-for-byte the lane's record, verified by
`python3 tools/verify_evidence.py` from the repository root.
