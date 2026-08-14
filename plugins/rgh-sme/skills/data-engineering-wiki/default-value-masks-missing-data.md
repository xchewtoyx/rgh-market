---
type: concept
title: Default Value Masks Missing Data
description: >
  Why defaulting a field to a valid-looking value while awaiting a
  confirming update conflates "not yet known" with "confirmed negative,"
  and silently corrupts downstream output if the confirmation never arrives.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

A common pipeline pattern: write a row with a field defaulted to some
plausible value (a boolean set `false`, a status set to a baseline state),
expecting a later feed to update it once the real outcome is confirmed. This
is dangerous specifically because the default value is **structurally
indistinguishable from a genuine, confirmed negative** — a downstream
consumer, or a [quality screen](quality-screens.md), sees a well-formed,
correctly-typed value either way, so nothing about the row itself signals
"this hasn't been confirmed yet."

**The failure mode this enables**: if the confirming feed stops working
entirely — an upstream outage, a broken pipeline stage — every row in the
affected window keeps its default value forever, and every downstream
consumer reads it as legitimate data rather than as an artifact of an
outage. A real incident of this shape: an ad-click training pipeline
defaulted each impression's `was_clicked` flag to false, updated later by a
separate verified-click feed; when that feed's infrastructure broke for
several days, every impression shown during the outage kept `was_clicked =
false`, and a model trained on that window learned "click probability is
near zero" — a conclusion that was internally consistent with the data the
model saw, and wrong about reality. No single row was malformed enough for
[binary validation](data-quality-validation-tests.md) to catch it; the
data's *distribution* was the only place the failure was visible, and even
distributional drift can look like a real trend until someone traces it
back to a specific outage window.

**The fix is representational, not just a better test**: track "pending
confirmation" as a state genuinely distinct from every real outcome the
field can hold — a separate `confirmed`/`confirmed_at` field, or a
tri-state (unknown/true/false) rather than a boolean defaulted to one of
its two real values. This makes a stalled upstream feed visible as a growing
count of never-confirmed rows, which is a concrete, checkable signal a
[quality screen](quality-screens.md) can alert on, instead of an ambiguity
baked silently into the data itself.

**A validation gate guarding an automated promotion decision (deploying a
newly trained model, publishing a newly computed metric) should include a
distributional sanity check on exactly the field a silent outage would
distort** — e.g., flagging when a label's positive-rate in a held-out
sample falls outside a normal historical range — as a concrete instance of
the [statistical validation](data-quality-validation-tests.md) a binary
check alone can't provide, and specifically because promotion decisions
compound an undetected data problem into production impact rather than just
sitting quietly in a table.
