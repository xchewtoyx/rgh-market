---
type: concept
title: Interception Point
description: >
  A point in a program where the effects of a particular change can be
  detected — found by tracing effects forward from the change, then chosen
  to be as close to the change point as possible.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 12"
---

An **interception point** is "a point in your program where you can detect
the effects of a particular change." Found by tracing effects forward from a
change point using [effect sketches](effect-sketches.md); not every
interception point found this way is equally good — choosing among them is
a judgment call.

**Prefer interception points close to the change point**, for two reasons:
(1) **safety** — every hop between the change point and the chosen
interception point is a link in a logical argument ("this affects this,
which affects this other thing..."); more hops means more ways to be wrong,
and the only real fallback for verifying a distant chain holds is to
deliberately break the change point and confirm the interception point's
test actually fails. (2) **practicality** — distant interception points are
typically harder to set up tests against, and require more mental "playing
computer" to convince yourself a test genuinely covers the change.

Worked illustration: extracting shipping-cost logic out of `Invoice.getValue()`
into a new collaborator. The new field itself is a poor interception
point — private, and narrow enough that it could confirm the new
collaborator computes correctly but couldn't catch other regressions
elsewhere in `getValue()`. A distant caller further up the call chain would
technically work but is unnecessarily far away. `Invoice.getValue()` itself
is the closest usable interception point, so that's where the test belongs.
When several related change points cluster together and no single close
interception point covers all of them, look for a
[pinch point](pinch-point.md) instead.
