---
type: concept
title: Normalization of Deviance
description: A practice that once departed from the accepted norm becomes the new accepted norm through a long chain of small, individually-defensible steps, each one invisible as a departure because the gap from the immediately preceding step is too small to notice or report.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Sidney Dekker), ch. 1-2"
---
# Normalization of Deviance

A safety margin, a maintenance interval, a review threshold, or any other operating constraint rarely gets abandoned in one visible, debatable step. Instead it erodes through **decrementalism**: a long sequence of small extensions, each one justified locally by recent operational success and each one only a marginal change from the immediately preceding, already-accepted practice. Because the gap between yesterday's norm and today's is too small to seem worth flagging, the cumulative drift is invisible to the people living through it in real time, even though the total distance traveled from the original standard can be enormous.

## Worked Example: A Decade of Interval Creep
A regulated maintenance interval for a critical aircraft part moved from every 300-350 flight hours to every 2,550 flight hours — nearly an order of magnitude — over roughly three decades, entirely through a sequence of separately-approved, individually-modest extensions, never one large jump. Each extension was justified by the empirical fact that the prior interval had produced no failures — but past success at a shorter interval says nothing about safety at a substantially longer one, because the mechanism was never actually tested at the new interval before being adopted. The part that eventually failed catastrophically had gone without lubrication for longer than even the (already heavily stretched) interval called for, and no single person in the chain of approvals had made a decision that, viewed against the immediately preceding standard, looked unreasonable.

## Why "Past Success Proves Safety" Is the Wrong Inference
The central inferential error normalization of deviance depends on: repeated safe operation under a loosened practice is treated as validation that the loosening was fine, when it may simply mean the danger hadn't yet been triggered by the right combination of circumstances. "Nothing bad happened" is compatible both with "the practice is safe" and with "the practice is unsafe but we got lucky every time so far" — a track record of successful outcomes cannot distinguish between these two explanations, especially when the underlying failure mode is rare or has a long latency.

## Why This Escapes Ordinary Incident Reporting
A monitoring or incident-reporting system built to flag departures from the norm cannot catch this kind of drift, because the norm itself is a moving target that gets redefined at each step. A missed check that would have been a reportable incident under an earlier, shorter interval is not an incident at all once the interval has been officially extended to cover that same gap — the deviant practice has been absorbed into the new definition of normal, so there is no longer any rule being violated to report against.

## A Leading Indicator: Renaming That Quietly Lowers Perceived Risk
Watch specifically for terminology shifts that recategorize a hazard as something more benign without any accompanying change in the underlying facts — a recurring physical "debris strike" relabeled a "foam loss," or a flight-safety issue recategorized as a routine "maintenance" or "turnaround" issue. The specific consequences of any one such renaming are rarely foreseeable in advance, but the renaming itself is a detectable, checkable signal independent of whether a bad outcome can be predicted from it: language that downgrades a category of event, especially when the downgrade also removes a formal reporting or review requirement that used to apply to it, is worth flagging on its own terms.

A financial-fraud executive's own first-person account of exactly this dynamic, describing repeatedly re-classifying a dead deal as merely dormant to avoid a required write-off: "You did it once, it smelled bad. You did it again, it didn't smell as bad" — a direct, self-aware description of how repetition itself erodes the felt wrongness of a departure from the honest baseline, independent of whether anything about the underlying facts changed between repetitions.

## Verification Action
When evaluating a claim that a current practice, threshold, or tolerance is safe or acceptable because "it's always been done this way" or "we've never had a problem," ask specifically how the current standard was arrived at: was it validated directly, or reached through a sequence of incremental extensions from an earlier, more conservative standard, each justified only by the absence of failure under the prior (shorter) step? If the latter, treat the current standard as unvalidated at its current level regardless of how long it has been in place, and check whether anyone has ever tested — rather than merely not yet been burned by — the cumulative distance traveled from the original, validated baseline.

## See Also
- [Root Cause Fallacy](root-cause-fallacy.md)
- [Hindsight Bias in Review](hindsight-bias-in-review.md)
- [Precision vs. Accuracy in Measurement](precision-vs-accuracy-in-measurement.md)
