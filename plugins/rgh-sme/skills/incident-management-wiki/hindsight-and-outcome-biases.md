---
type: concept
title: Hindsight and Outcome Biases
description: Cognitive biases that distort failure analysis by overestimating predictability and judging decision quality by the severity of the outcome.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 2"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 6"
  - title: "Thinking in Bets"
    resource: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts (Annie Duke), ch. 1, 6"
---

Failure analysis is routinely distorted by two powerful retrospective biases:
* **Hindsight Bias**: The tendency for observers with knowledge of an outcome to overestimate how predictable and preventability the event was in real time. Hindsight collapses a complex, branching timeline into a linear sequence where the "correct" choice appears obvious.
* **Outcome Bias**: The tendency to evaluate the quality of a decision based on its result rather than the information available to the decision-maker at the time.

Retrospective bias fosters the **illusion of cause-consequence equivalence**—the false belief that severe outcomes must be caused by equally severe failures in process. In reality, normal work processes are full of minor fluctuations that usually succeed but occasionally lead to bad outcomes. 

To overcome these biases, investigators must apply the [local rationality principle](local-rationality-principle.md) during [learning reviews](learning-reviews.md) to reconstruct the situation as it unfolded from the inside out, rather than analyzing decisions in the misleading light of hindsight.

### A "bias" explanation can be unfalsifiable

A specific trap for a postmortem to avoid: labeling a bad outcome as
evidence of a named cognitive bias in the responders, when the label can
explain literally any outcome after the fact. The official investigation
into the USS Vincennes shooting down a civilian airliner attributed the
crew's fatal misreading of the aircraft's altitude to "expectancy bias" —
seeing what they expected rather than what was there. Gary Klein's
counterargument: in the month before the incident, ships in the area had
challenged 150 aircraft, and 83% turned out to be hostile military versus
1.3% commercial — so acting on that expectancy was, empirically, the
better bet. Had the crew *not* fired and been hit by an actual attacker,
the same reviewers would have called it a failure to use available base
rates. "If you act on expectancies and you are wrong, you are guilty of
expectancy bias. If you ignore expectancies and are wrong, you are guilty
of ignoring base rates... no one can win" — a bias framing this
unfalsifiable explains nothing, and a review that reaches for it should be
treated as a sign the investigation stopped one step too early.

In the same case, the actual explanation turned out to be findable and far
more useful than a bias label: the display showed altitude only as a raw
number with no trend indicator, forcing a slow manual read under noisy,
high-tempo conditions, and — separately — a recycled tracking-number
briefly pointed different crew members at data for two different aircraft
without that reassignment being clearly broadcast. Both are concrete,
fixable [contributing factors](root-cause-fallacy.md) — an interface
redesign and a data-handling gap — that a "the crew was biased" conclusion
would never have surfaced, and neither required attributing the outcome to
a flaw in the people involved.

### "Resulting": judging the decision by the outcome

Poker players have a name for outcome bias applied to a single event:
**resulting** — grading a decision's quality by whether it happened to work
out, rather than by the quality of reasoning available at the time. A
well-known NFL example: a coach's play call was branded "the worst call in
Super Bowl history" purely because it was intercepted, even though the
same play thrown under the same conditions succeeds the overwhelming
majority of the time — the call would have drawn no criticism at all had
the pass simply been caught. The same pattern shows up reviewing an
incident response decision made under real uncertainty: a mitigation that
happened to make things worse gets remembered as "the wrong call," while
an equally uncertain call that happened to work gets treated as obviously
correct, even when both were reasoned the same way from the same
information.

The useful image for why this distortion happens: think of time as a tree,
with one trunk (the fixed past) and many branches (the futures that were
genuinely possible from any given decision point). Once an outcome
happens, it's tempting to see it as the only branch that was ever really
there — the other branches quietly vanish from view, and the branch that
did occur looks like it was inevitable all along. A postmortem's job is to
deliberately look back at the tree *before* it got cut down: to reconstruct
which outcomes looked plausible at decision time, not just which one
happened. A U.S. federal appeals judge overturning a jury verdict against
a contractor made exactly this point explicit: "the verdict appears to be
a consequence of hindsight bias — the human tendency to believe that
whatever happened was bound to happen, and that everyone must have known
it... hindsight bias is not enough to support a verdict."
