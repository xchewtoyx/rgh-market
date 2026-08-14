---
type: concept
title: Reference Data Anchored to Prior System Output
description: >
  Why building a "corrected" reference dataset by editing a system's own
  prior output, instead of deriving it independently, silently biases the
  reference toward that system's existing errors.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

A reference or "ground truth" dataset is supposed to be an independent
standard a system's output gets checked against. That independence quietly
breaks when the reference itself is built by starting from the system's own
prior output and having a reviewer edit it — a common shortcut, since
editing an already-mostly-right output is cheaper than producing a
from-scratch reference. The reviewer's edits inherit whatever structure the
original output already had wherever the reviewer didn't happen to change
it, so the resulting "ground truth" ends up correlated with the very
system's behavior it's meant to independently evaluate.

**This produces a specific, hard-to-detect failure**: a newer version of the
system gets penalized on the reference set not for being wrong, but for
disagreeing with the old version's own (reviewer-endorsed) style or
tendencies — mistaken for a regression when it's actually the reference set
carrying forward a bias nobody deliberately introduced. It's especially
hard to catch because every individual reference entry looks legitimate
(a human reviewed it), and the bias only shows up as a systematic pattern
across the disagreeing entries, not as any one obviously wrong value.

**The mitigation is a [lineage](data-lineage.md) question, not a modeling
one**: know and record whether a given reference dataset's creation process
started from a prior system's output or was produced independently, since
that provenance fact determines whether the dataset can be trusted as an
unbiased check on that same system's descendants. Where retention rules or
storage limits mean the reference set itself won't be
[reproducible or reconstructible](data-retention-and-lifecycle-management.md)
later, capturing this provenance fact at creation time is the only way a
future investigation can even suspect this failure mode, let alone confirm
it.
