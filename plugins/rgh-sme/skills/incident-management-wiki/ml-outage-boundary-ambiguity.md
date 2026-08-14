---
type: concept
title: ML Outage Boundary Ambiguity
description: ML outages are less sharply defined than conventional ones along both time (unclear start/end) and impact (unclear broken-vs-not-yet-good), which complicates declaring and closing them.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

ML outages resist the clean boundaries that non-ML incidents usually have,
along two separate dimensions:

- **Time**: even when a triggering event can be traced, establishing a
  definitive causal chain from that event to user-facing impact is often
  impractical, so a precise start and end are hard to pin down. This makes
  timing measures like [outage tracking metrics](outage-tracking-metrics.md)
  (time to detect, mitigate, resolve) inherently fuzzier for ML incidents
  than for a service that either returns 500s or doesn't.
- **Impact**: it's often unclear whether a condition is a genuine outage or
  simply a model that isn't yet as sophisticated as hoped. Every model
  starts basic and, ideally, improves over time — there is frequently no
  sharp transition between "bad" and "good," only "better" and "not quite
  as good yet." The line between "broken" (worth declaring an incident over)
  and "could be better" (ordinary iterative improvement work) isn't always
  clear-cut, which makes [incident severity
  classification](incident-severity-classification.md) harder to apply
  mechanically for quality-based ML incidents than for availability-based
  ones.

Because both dimensions are ambiguous, ML incident processes benefit from
explicit, pre-agreed thresholds for "this is a regression, not just
room-to-improve" — deciding that criterion mid-incident, under the same
ambiguity the criterion is meant to resolve, reproduces the delay that
[early incident declaration](early-incident-declaration.md) warns against
in general.

The impact dimension can resolve in a genuinely unexpected direction: in a
documented case, a recommendation system started showing visibly "weird,"
sparse recommendations, and the investigation found a real, traceable
cause (a supplier had stopped shipping the exact products customers now
wanted, so few in-stock items cleared the system's minimum
expected-value bar). The team concluded there was nothing to fix in the
ML system at all — the model was behaving about as well as it could given
real supply constraints outside its control — and the incident was judged
effectively over once leadership chose to address the supply problem
instead of the model. Not every "the system looks broken" investigation
ends in "and here's the bug"; sometimes the correct resolution is
recognizing the boundary of what the model can be expected to fix at all.

See also [ML outage visibility gap](ml-outage-visibility-gap.md) and [ML
incident organizational breadth](ml-incident-organizational-breadth.md).
