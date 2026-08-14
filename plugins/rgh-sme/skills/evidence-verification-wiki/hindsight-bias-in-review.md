---
type: concept
title: Hindsight Bias in Review
description: Knowing an outcome distorts a reviewer's judgment of how predictable and preventable it was, and of the quality of the decisions that led to it — a specific bias to guard against when evaluating past decisions or incidents.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 2-3"
  - title: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts"
    resource: "Thinking in Bets (Annie Duke), ch. 1, 6"
---
# Hindsight Bias in Review

**Hindsight bias** is the tendency for knowledge of an outcome to make that outcome seem, in retrospect, far more predictable and preventable than it actually was to the people involved at the time, without the reviewer being aware their judgment has been distorted this way. A closely related **outcome bias** leads reviewers to judge the *quality of a decision* by how it turned out rather than by the information actually available when it was made. Together these produce an **illusion of cause-consequence equivalence**: the mistaken assumption that a severe outcome must reflect an equally severe flaw in the process that led to it — when in fact a sound process can produce a bad outcome in a complex, uncertain situation, and a flawed or improvised process frequently produces a fine one.

## Why This Matters for Reviewing Claims About Past Decisions
Any review that reconstructs why a past decision was made — an incident postmortem, an audit of a prior judgment call, a retrospective evaluation of a recommendation — is vulnerable to hindsight bias distorting the reviewer's own assessment, not just the account being reviewed. A reviewer who already knows how things turned out will tend to find the failure "obvious" in retrospect and treat everyone involved as having had access to information or clarity they didn't actually have at the time. This connects to [confirmation bias in verification](confirmation-bias-in-verification.md) and [confabulation in testimony](confabulation-in-testimony.md): a source's own after-the-fact account of "why" they acted is itself vulnerable to the same outcome-knowledge distortion, since they too now know how it turned out.

## Named Pattern: "Resulting"
Poker players call this specific error **resulting**: judging the quality of a past decision by the quality of the outcome it happened to produce, rather than by the information and reasoning actually available when it was made. A famously criticized football play call (a pass thrown from the 1-yard line late in a championship game, intercepted for a loss) was universally declared "the worst call in history" once it failed — but a statistical review found that pass plays from that exact situation were intercepted only about 2% of the time historically, meaning the call was a reasonable, positive-expected-value decision that happened to hit the unlucky tail. The habit of "resulting" is strongest precisely when a bad outcome arrives to punish a good decision, or a good outcome arrives to reward a bad one — both cases invert the actual relationship between decision quality and result quality, and only a review that deliberately sets the outcome aside can catch either error.

## The Counterfactual Trap
A specific symptom of hindsight bias is **counterfactual reasoning** substituting for explanation: statements like "they should have noticed X" or "if only they had done Y" describe a hypothetical, better-informed version of events, not what the person actually knew or perceived at the time. A counterfactual is not an explanation — it describes a world that didn't exist for the person being reviewed, and citing one does not establish that the actual decision was unreasonable given what was actually known or observable in the moment. Distinguish between information that was technically **available** (present in a system, logged, or recorded somewhere) and information that was actually **observable** (perceivable given workload, interface design, and where attention was actually focused) — a claim that someone "should have seen" something available is not the same claim as it being observable to them at the time, and verifying which one is actually true is a distinct, necessary step.

## The Tree Metaphor
Picture time as a tree: a single trunk (the fixed, already-happened past) with many branches emerging from the present, each a possible future. As events resolve, an observer's view acts like a chainsaw that severs every branch that didn't happen, leaving only the one that did — which then appears, in retrospect, to have been the tree's only real branch all along, expanding to fill the observer's entire view of what was "always" going to happen. A reviewer assessing a past decision is looking at the trunk and one surviving branch, and must deliberately reconstruct the other branches that were genuinely live possibilities at decision time before judging whether the choice was reasonable.

A federal appeals court applied exactly this reasoning to overturn a large jury verdict against a contractor after a workplace explosion, with the presiding judge writing that the verdict was "a consequence of hindsight bias—the human tendency to believe that whatever happened was bound to happen, and that everyone must have known it," and stating plainly that "hindsight bias is not enough to support a verdict." The same logic applies to any retrospective judgment of a decision, not only legal liability: a bad outcome resulting from a chain of independently unlikely events is not proof the decision that preceded it was flawed, and a claim's post-hoc "obviousness" is not evidence it was actually predictable at the time.

## Verification Action
- When reviewing an account of a past decision or incident, deliberately reconstruct what was known, observable, and salient to the actor *at the time*, before evaluating whether their action was reasonable — resist evaluating the decision against information only available in hindsight.
- Treat any purely counterfactual claim ("they should have...") as a placeholder for a missing explanation, not an explanation itself — ask what would need to be true about the actor's knowledge, attention, or constraints at the time for the counterfactual action to have actually been available to them.
- When a claim asserts information "was available," separately verify whether it was also observable under the actual conditions (workload, interface, timing) — these are different claims requiring different evidence.

## See Also
- [Confirmation Bias in Verification](confirmation-bias-in-verification.md)
- [Confabulation in Testimony](confabulation-in-testimony.md)
- [Incident Postmortem Verification](incident-postmortem-verification.md)
- [Root Cause Fallacy](root-cause-fallacy.md)
