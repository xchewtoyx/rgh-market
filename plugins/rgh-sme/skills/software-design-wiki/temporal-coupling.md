---
type: concept
title: Temporal Coupling
description: >
  Temporal coupling bundles two pieces of behavior together only because
  they must happen at the same time, not because they're conceptually
  related — such ties are prone to fusing together and becoming hard to
  separate later without a seam.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 6"
---

Inlining a new piece of behavior directly into an existing method purely
because it needs to run alongside the method's existing call sites creates
temporal coupling: the two behaviors are now bundled in one place for no
reason other than timing, not because they belong together conceptually.
Once fused this way, separating them later requires finding or creating a
[seam](seam.md) between them, work that wouldn't have been necessary if they
had been kept structurally separate — see
[wrap method](wrap-method.md) and [wrap class](wrap-class.md) for the
techniques that add new behavior alongside old without creating this
coupling in the first place.
