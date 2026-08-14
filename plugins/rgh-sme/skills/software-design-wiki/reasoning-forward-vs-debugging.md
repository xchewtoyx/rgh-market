---
type: concept
title: Reasoning Forward vs. Debugging
description: >
  Debugging reasons backward from an observed bad result to its cause;
  finding good test placement before a change requires the opposite skill —
  reasoning forward from a change to everywhere it could possibly show up.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 11"
---

Two related but distinct reasoning tasks are easy to conflate because both
involve tracing cause and effect through code. **Debugging** reasons
backward: given an observed bad result, trace back to find what produced it.
**Placing tests before a change** requires reasoning forward instead: "if we
make a particular change, how could it possibly affect the rest of the
results of the program?" The forward direction is the actual skill needed to
find good test points, and it's largely tacit, "just part of being a
programmer" knowledge that's rarely taught explicitly — see
[effect sketches](effect-sketches.md) for the technique that makes it
explicit and repeatable.
