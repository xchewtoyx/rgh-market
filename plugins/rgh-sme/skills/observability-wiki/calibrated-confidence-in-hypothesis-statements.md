---
type: concept
title: Calibrated Confidence in Hypothesis Statements
description: Stating a debugging hypothesis with an explicit confidence level ("I'm 70% sure this is a DNS issue") rather than a flat assertion communicates real uncertainty to collaborators and is measurably trainable — most people are overconfident by default until they practice checking their stated confidence against actual outcomes.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything (Douglas W. Hubbard), ch. 5"
---

A hypothesis stated as a flat claim ("it's the database") loses information a hypothesis stated with an explicit confidence level keeps ("I'm about 70% sure it's the database, 20% it's the cache layer, 10% something we haven't considered"). The second form is more useful mid-investigation for the same reason a range beats a single point estimate: it tells collaborators how much to trust the claim and how much investigative effort is still justified, and it makes [testing the hypothesis against real data](hypothesis-testing-with-real-data.md) a genuine update rather than a binary right/wrong verdict.

**Calibration** is whether stated confidence matches actual hit rate: of everything someone claims "70% confident" about, roughly 70% should turn out true. The dominant failure mode, measured repeatedly across professions, is overconfidence — most people's "90% confident" claims are right well under 90% of the time. Calibration is not innate and does not automatically improve with experience; it is a trainable skill, and people who practice it (with feedback against real outcomes) measurably close the gap, without necessarily getting more answers *right* — the improvement is in knowing how confident to actually be, which is a distinct skill from raw domain knowledge.

Two techniques transfer directly to debugging and incident response:

- **The equivalent-bet check**: for a stated confidence level, ask whether you'd genuinely rather stake something real on being right at that odds, versus a fair random device set to the same probability. If you'd rather take the random device, your stated confidence is higher than your real confidence — you're overconfident and should say a lower number.
- **The absurdity test for bounding a guess**: rather than anchoring on a single point estimate and padding it, start from an implausibly wide range and narrow it by rejecting values you're confident are impossible, until you reach genuine uncertainty at both edges. Applied to debugging: instead of guessing "the leak started around 2pm," bound it — "definitely after the last deploy at noon, definitely before the alert fired at 4pm" — then narrow from there using whatever telemetry actually distinguishes the sub-range.

The practical payoff during an incident is the same one [resulting](resulting-bias-in-postmortem-evaluation.md) argues for after the fact: a well-calibrated 70%-confidence call that turns out wrong was still a good call, and treating it as such (rather than either false certainty or reflexive "I don't know") is what lets a team actually reason about which of several competing hypotheses to chase first under time pressure.
