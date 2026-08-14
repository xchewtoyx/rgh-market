---
type: concept
title: Variation-Point Documentation
description: >
  A variation point documents where an architecture deliberately permits
  alternatives — what the options are, when they get bound, what
  constrains the choice, and what each option costs.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 6"
---

A variation point records a place in the architecture where more than one
option is deliberately allowed, rather than a single fixed design. Document
what the actual options are, when the choice between them gets bound
(compile time, deployment time, runtime configuration), what constrains
which options are valid in a given context, and what the consequences of
each option are.

This is distinct from an [architectural decision
record](architectural-decision-capture.md): a decision record explains why
one option was chosen and closes the question; a variation point explains
that the question is deliberately still open, and bounds how it can be
answered. Confusing the two is a common documentation failure — either
treating a genuinely closed decision as if alternatives were still live
(inviting someone to "fix" it), or treating a genuine variation point as
if it were arbitrary, undocumented flexibility with no real constraints
on it.

Whether a variation point is worth building at all, rather than just
hand-editing the system whenever the anticipated change arrives, is
itself a decision worth recording — see [change-mechanism investment
justification](change-mechanism-investment-justification.md).
