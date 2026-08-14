---
type: concept
title: Precommitted Evaluation Criteria
description: Defining exactly what result will count as confirming or disconfirming a claim before gathering the evidence, so ambiguous results can't be rationalized after the fact.
sources:
  - title: "Continuous Discovery Habits"
    resource: "Continuous Discovery Habits (Teresa Torres), ch. 10, 11"
  - title: "Good Strategy/Bad Strategy"
    resource: "Good Strategy/Bad Strategy (Richard P. Rumelt), ch. 17"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 12"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Gary Klein), ch. 2"
---
# Precommitted Evaluation Criteria

Before running a test, survey, or other evidence-gathering exercise meant to confirm or disconfirm a claim, write down the exact result that will count as confirmation and the exact result that will count as disconfirmation. A vague threshold ("some people should do X," "engagement should improve") produces after-the-fact disagreement about what the result actually means — different reviewers can read the same ambiguous outcome as success or failure depending on what they wanted to find, which defeats the purpose of gathering the evidence at all.

## Why This Guards Against Confirmation Bias
Once results are in hand, [confirmation bias in verification](confirmation-bias-in-verification.md) makes it easy to selectively interpret an ambiguous number as supporting whatever was already believed. Committing to a specific numerator and denominator (e.g., "at least 3 of 10 participants must do X," not "some people" or an unanchored percentage) before seeing the data removes that after-the-fact wiggle room. This is the interpretation-side counterpart to [cherry-picking](cherry-picking.md)'s p-hacking pattern: p-hacking manipulates *which analysis* gets reported after seeing the data, while unprecommitted criteria let a reviewer manipulate *how a fixed result gets read* after seeing it — both are defeated by locking in the rule before the data arrives.

## Calibrate Rigor to Stakes, Not to a Fixed Standard
Precommitted criteria do not need to be scientifically rigorous to be useful — the appropriate strictness depends on how much is riding on the claim and how reversible the decision built on it is. A low-stakes, easily-reversible claim can be adequately tested with a fast, small-sample check against a loosely precommitted threshold; a high-stakes or hard-to-reverse claim warrants a stricter threshold, a larger sample, and [evidence triangulation](evidence-triangulation.md) across multiple independent test types rather than a single measurement. The goal in either case is calibrated confidence proportional to the evidence gathered, not proof — see [claim verification triage](claim-verification-triage.md) for prioritizing verification effort by stakes more generally.

## Precommitment as a Calibration Tool, Not Just a Test Design
The same discipline applies to individual judgment, not just formal tests: privately writing down a specific prediction (what will happen, what position someone will take, what the right call is) before an event and comparing it against the actual outcome afterward is what makes it possible to detect whether a person's judgment is actually improving over time. Without a recorded prediction made in advance, [hindsight bias in review](hindsight-bias-in-review.md) makes outcomes look like they "could have been predicted" whether or not they actually were — the written precommitment is the only artifact that can distinguish genuine foresight from a retrospective story.

## Held-Out Validation: Testing a Model Against Data It Never Saw
A specific, especially strong form of precommitment applies to any model or formula built from historical or expert-judgment data: withhold a subset of known cases from the data used to build the model, then check the model's predictions against that held-out subset's real outcomes. A worked case: a life-sciences company that had built a revenue-forecasting formula from 50+ historical product scenarios (via a [regression-based lens model](statistical-model-track-record-vs-expert-judgment.md) fit to expert judgment) validated it by holding back 16 real products with known outcomes, excluded entirely from the model-building step, and comparing the model's predictions for those 16 against both the real results and the original experts' own contemporaneous forecasts — finding a 76% reduction in forecasting error versus the experts, and confirming the improvement wasn't an artifact of the model having implicitly "seen" the answer already. A claimed model or formula whose accuracy is only ever demonstrated on the same data used to build it has not actually been validated — it may simply be fit to that data's noise.

## A Presented Comparison Can Be a Post-Hoc Justification, Not a Real Evaluation
A documented multi-criteria comparison ("we evaluated options A and B against these dimensions and chose A") can look like rigorous precommitted evaluation while actually being a rationalization constructed after a gut choice was already made. A classic study of MIT students trained in formal rational-choice methodology (identify options, weight dimensions, score each, pick the winner) found their eventual job choice was predictable with 87% accuracy up to three weeks *before* they announced a "decision," simply from noting their early gut favorite — students then went through the trained ritual of picking one comparison candidate and showing (sometimes admittedly "fudging a little") that their favorite scored as well or better on each dimension, before announcing the choice they'd already made. They were not making a decision; they were constructing a justification for one already made.

## Verification Action
- Before evidence is gathered, ask "what specific result would make us say this claim is false?" — if no one can answer precisely, the test as designed cannot actually falsify anything.
- When reviewing a completed test or study, check whether success/failure criteria were defined before or after the result was known; a threshold introduced only in retrospect should be treated with the same suspicion as a p-hacked analysis.
- When a document presents a multi-criteria comparison that conveniently favors the option ultimately chosen, check whether the comparison was actually conducted before the choice was made (or could have been), and be alert to individual dimension scores that look adjusted to reach the predetermined winner.
- Where the underlying evidence is thin (a small sample, an early-stage signal), don't over-claim certainty — treat the result as one data point toward [evidence triangulation](evidence-triangulation.md) rather than as a final determination, and note explicitly what larger or independent check would be needed to raise confidence further.

## See Also
- [Confirmation Bias in Verification](confirmation-bias-in-verification.md)
- [Cherry-Picking](cherry-picking.md)
- [Claim Verification Triage](claim-verification-triage.md)
- [Evidence Triangulation](evidence-triangulation.md)
