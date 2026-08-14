---
type: concept
title: Incorporation-by-Reference Hazard
description: >
  Citing an entire external standard as a requirement silently binds the
  product to everything in that document, not just the specific part the
  author actually meant.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 17"
---

A [mandated constraint](mandated-constraint.md) or non-functional
requirement that references an external standard broadly — "the product
must conform to ISO 601" — does not actually narrow the requirement to
whatever specific clause the author had in mind. It incorporates the
*entire* referenced document by reference, obligating the product to every
requirement in that standard, including ones the author never considered
and that may not even be relevant to the product.

The fix is to always cite the specific section or clause actually
intended, not the standard as a whole: "conforms to ISO 601 §4.2" instead
of "conforms to ISO 601." This is the same discipline [fit
criteria](fit-criterion.md) apply to vague adjectives, aimed at a
different failure mode — here the requirement isn't ambiguous in wording,
it's accidentally far broader in scope than anyone intended, and the gap
between the two only surfaces later when someone actually reads the full
referenced document.
