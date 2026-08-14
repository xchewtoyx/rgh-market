---
type: concept
title: Noticing Non-Events
description: >
  Human perception is tuned to detect change, not the absence of expected
  change, so a monitoring display that only reacts when something moves will
  systematically fail to flag a value that should have changed and didn't.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 4"
---

Preattentive perception evolved to notice sudden change — motion, flicker,
contrast — not the absence of change (see
[preattentive processing](preattentive-processing.md)). This creates a
specific blind spot for monitoring displays: a value that was expected to
change but silently didn't (an uncommanded altitude drift that stops
correcting, a vessel that stays off its intended course, a process reading
that should be trending and instead flatlines) gives the viewer nothing to
preattentively latch onto. Nothing is flickering, nothing is moving, so
nothing draws the eye — even though the absence of expected movement is
itself the important signal.

The design implication: a monitoring or operational display cannot rely
solely on [dynamic highlighting](static-vs-dynamic-highlighting.md) triggered
by a value crossing a threshold, because that only works when the value
*does* change. Where "should be changing but isn't" is itself an alertable
condition, the display needs an explicit, separate check for staleness or
stagnation — e.g., flagging a value that hasn't updated or moved within its
expected cadence — rather than assuming a lack of alarm means a lack of
problem.
