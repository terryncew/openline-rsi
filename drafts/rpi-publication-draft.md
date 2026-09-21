DRAFT FOR REVIEW — not published.

# RPI-001: a genuine operating improvement that did not pay for itself

One sentence: the learning worked; the economics didn't.

RPI-001 ran a frozen recursive-productivity experiment: a proposer tried to
improve a task-solving method, a receiver gate accepted or rejected each
candidate on its own evidence, and the accepted method then ran 36 fresh
paired downstream tasks against the frozen baseline. Arm A used the baseline
method (M0). Arm B used the learned improvement (M1). Arm C ran the same M1
while bearing the extra recursive-search cost. All 192 scientific calls
settled; 36/36 paired tasks per arm completed; zero dropped; zero unresolved
exposure.

The improvement was real. M1 compresses the method to three steps — inspect,
fix, verify. Paired against M0 across 36 tasks, M1's operating work per
dollar ran about 3.8% higher: geomean ratio 1.038, 95% CI [1.0042, 1.073],
zero regressions. The interval excludes 1.0. An independent receiver
verified every task's usefulness, so this is not a self-graded gain.

It did not repay its cost. All-in work per dollar — operating spend plus the
preregistered share of the $0.745 improvement acquisition cost — was 73.23
for A, 42.58 for B, 30.07 for C. Neither B nor C cleared the preregistered
all-in bar (≥1.05× the comparator, no regressions). C-vs-B on the identical
method returned a ratio of about 1, as a calibrated comparison should.

The earned claim, verbatim from the frozen terminal record:

"B and C did not produce more independently verified useful work per
dollar than A and B respectively, within the frozen horizon and split."

The mechanism is worth stating plainly. The operating comparison can detect
small sustained advantages; the all-in comparison inside 36 downstream tasks
needs very large ones to move. That is a property of the horizon, not the
method. The second-round proposal — pushing the compression further — was
rejected by the receiver on cost (cost ratio 1.0302), which is the system
working: further compression cost more, not less.

Limits, with no generalization: frozen 100-task corpus (eval sha256
933cfadd…17bc06a3), one model (gpt-5.6-sol), a 36-task horizon, the frozen
accounting split. Total spend $2.5369 ($2.5343 scientific of the $10.00
budget; $0.00264 apparatus, reported separately). No rerun, no rescue, no
threshold movement after contact. The record is terminal.

What survives this negative: an independently verified method improvement
exists and compounds nowhere yet — it earned a real edge and still did not
produce more useful work per dollar within the frozen horizon. That is the
distinction the experiment was built to draw, and it drew it.
