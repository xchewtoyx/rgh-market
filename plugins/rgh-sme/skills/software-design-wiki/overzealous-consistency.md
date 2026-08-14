---
type: concept
title: Overzealous Consistency
description: >
  Consistency also requires dissimilar things to look dissimilar — forcing
  genuinely different things into a shared name, pattern, or template just
  for uniformity's sake breaks the trust guarantee that makes consistency
  useful in the first place.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 17"
---

The reciprocal failure mode to inconsistency: applying a shared name, coding
pattern, or design-pattern template to things that aren't actually alike,
purely for the sake of looking uniform. [Consistency's](consistency-as-a-design-tool.md)
benefit depends entirely on a trust guarantee — "if it looks like an x, it
really is an x" — and conformity for its own sake breaks that guarantee just
as thoroughly as never establishing the convention at all, which makes the
whole mechanism backfire instead of helping.
