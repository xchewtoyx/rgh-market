---
type: concept
title: Decrementalism in Constraint Drift
description: >
  A documented limit erodes not through one deliberate revision but
  through a sequence of small, individually-justified steps, each too
  small relative to the last accepted value to trigger the review that a
  single large change would have provoked.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems (Sidney Dekker), ch. 1-2"
---

A documented [mandated constraint](mandated-constraint.md) or requirement
rarely goes stale by one dramatic decision to abandon it. It erodes through
**decrementalism**: a sequence of individually small, locally-justified
adjustments, each one judged only against the *immediately preceding*
value rather than against the original constraint's actual rationale.
A worked real-world case: an aircraft part's inspection interval was
extended repeatedly over three decades — 300 hours, then 700, then 1,000,
then 1,200, then 1,600, then 2,550 — with each single step small enough
that nobody involved treated it as a significant change worth escalating,
even though the cumulative result was nearly a tenfold loosening of the
original requirement.

This matters for documentation specifically because it explains a failure
mode that [requirement revisit triggers](requirement-revisit-triggers.md)
don't catch by default: a trigger built to fire on "a significant change"
never fires, because no single step in a decremental sequence is
significant relative to the step before it — only the sequence, compared
against the *original* documented value, is significant. Each step also
meets with apparent empirical success (nothing failed under the loosened
constraint), which is taken as validation rather than as what it actually
is: an untested assumption that hasn't yet been disproven. Past success
under a loosened constraint is not evidence the loosening was safe, only
evidence that the failure mode the original constraint guarded against
hasn't occurred yet.

The documentation countermeasure is to anchor a revisit trigger to
**cumulative drift from the original documented value and its recorded
rationale**, not to the size of the most recent change — and to record
each revision as a delta against that original baseline, not only against
the immediately prior one, so that a reviewer looking at the current value
in isolation can still see how far it has moved from where the
[requirement rationale](requirement-rationale.md) was actually established
and re-ask whether that rationale still holds.
