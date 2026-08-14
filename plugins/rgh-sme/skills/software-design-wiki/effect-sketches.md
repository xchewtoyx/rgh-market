---
type: concept
title: Effect Sketches
description: >
  An informal diagram tracing what a variable or method's value can change
  and everything downstream whose runtime value changes as a result, used
  to find exactly which methods need characterization tests before a change.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 11"
---

Testing every changed method directly is only sufficient for simple,
well-understood code. In tangled legacy code, "a change in one place can
affect behavior someplace else; unless we have a test in place, we might
never know about it." Every functional change has an associated chain of
effects propagating outward — but most of a codebase is typically
*unaffected* by any given change, because it doesn't call the changed code
directly or indirectly. The skill this chapter names and makes explicit:
reasoning **forward** from a change to everywhere it could possibly show up,
as opposed to [debugging's backward reasoning](reasoning-forward-vs-debugging.md)
from an observed bad result to its cause.

An **effect sketch** makes this reasoning concrete: a bubble per
variable/method whose value can change, with arrows to everything whose
runtime value can change as a result — no fixed syntax, the point is just
laying out the causal graph by hand. Individual small sketches for each
method can be merged into one combined sketch for a class.

**Reasoning forward, step by step**, to find where to place
[characterization tests](characterization-tests.md) before a change: (1) identify the change points; (2) for each, ask
what internal state it modifies; (3) ask what reads that modified state,
and what reads *that* in turn, recursing outward; (4) follow the chain
through any further layers, including objects the changed code constructs
or mutates. The result narrows the test surface sharply — often only a
handful of externally-observable methods actually need coverage for a given
change, not every method touched along the way. See
[effect propagation mechanisms](effect-propagation-mechanisms.md) for the
concrete channels this tracing has to follow, and
[know your language for effect analysis](know-your-language-for-effect-analysis.md)
for where the tracing can safely stop.

An explicit caution folded into the method: make sure you've found *all* the
clients of the class under examination — a superclass or subclasses may have
other clients you haven't considered, and non-private fields or methods
create sensing paths outside the obvious call graph.

**Design payoff beyond testing**: "one measure of goodness in software is
that rather complicated effects on the outside world are the sum of a much
simpler set of effects in the code." An effect sketch with multiple
independent methods reading the same underlying state directly ("fan-out")
means testing one doesn't exercise the other's logic. Removing the
duplication — having one method call the other internally instead of
re-reading the shared state itself — collapses the sketch's endpoints, so
testing one now automatically exercises the other too. This ties effect-
sketch simplification directly back to ordinary
[duplication removal](code-duplication-red-flag.md) as a design activity,
not just a testing convenience: "when we remove tiny pieces of duplication,
we often end up getting effect sketches with a smaller set of endpoints.
This often translates into easier testing decisions."

Practicing effect analysis opportunistically, not just when forced to, pays
off over time: as familiarity with a codebase grows, a sense that certain
kinds of effect don't need checking at all — when that instinct is
justified — indicates "basic goodness" in the code, meaning implicit or
explicit rules the codebase actually honors consistently (e.g., "callers
never retain and mutate a list they hand to a constructor"). Codebases where
that instinct is reliably correct are far easier to work in than ones where
such rules are riddled with exceptions.
