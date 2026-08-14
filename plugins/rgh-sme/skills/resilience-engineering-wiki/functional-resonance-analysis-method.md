---
type: concept
title: Functional Resonance Analysis Method (FRAM)
description: >
  Model a system as coupled functions rather than coupled components, so
  that catastrophic outcomes can be traced to the normal, everyday
  performance variability of several functions combining — not to any single
  function breaking.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 13"
---

FRAM (Hollnagel) analyses a system by its **functions** — what it actually
does — rather than by its institutional or mechanical components, which
takes current organisational structure as a given rather than as one
possible implementation of the functions underneath it. This functional
perspective is what lets the same method describe a chemical plant, an
airline, or a banking system: the components differ completely, but the
functional relationships can share the same shape.

**Each function has six aspects**, conventionally drawn as a hexagon:

- **Input (I)** — what the function receives or transforms.
- **Output (O)** — what the function produces or changes.
- **Preconditions (P)** — what must already be true before the function can
  execute.
- **Resources (R)** — what the function consumes or needs while executing.
- **Time (T)** — the deadlines, duration, or timing constraints it operates
  under.
- **Control (C)** — the monitoring, regulatory, or policy mechanisms that
  govern how it executes.

**Functions couple** when one function's output serves as another's input,
precondition, resource, or control. Mapping these couplings across a whole
system produces a network of functional dependencies that cuts across
institutional boundaries — a dependency invisible to anyone analysing a
single institution's internal processes in isolation, because the coupling
lives *between* organisations, not inside any one of them.

**Functional resonance is the payoff concept.** In physics, stochastic
resonance is random background noise pushing a weak signal over a detection
threshold. FRAM borrows the shape but changes the mechanism: the "noise" is
the normal, individually-undetectable performance variability of each
coupled function — the same [everyday performance variability that
Safety-II treats as the ordinary source of both success and
failure](safety-i-and-safety-ii.md), not a malfunction in any single
function. When several functions' normal variability combines through their
couplings, the result is systematic and can be disproportionate: an
unexpected, catastrophic outcome that no single function's own performance
would predict, because no single function actually failed.

**Case: the collapse of Northern Rock (2007).** A UK mortgage lender's
*Transfer Economic Resources* function depended on a continuous output from
the global credit market's own transfer function, which in turn had its own
preconditions — positive credit ratings, favourable investor risk
assessment. When a separate part of the system (US sub-prime defaults)
eroded those preconditions, credit markets seized, and Northern Rock's
function failed not because of any defect in its own mortgage underwriting,
but because a precondition supplied by a functionally-coupled but
institutionally unrelated part of the system silently stopped holding. A
regulator monitoring only Northern Rock's internal data, using traditional
[risk metrics grounded in historical outcomes](heinrich-triangle-myth.md),
had no visibility into this coupling at all.

**System boundaries are drawn relative to who is asking**, not fixed by the
system itself — see [system boundaries are perspective-dependent](system-boundaries-are-perspective-dependent.md)
for what this means for who can even see a given functional coupling in the
first place. And because the couplings that produce resonance are the
system's *normal* operating variability rather than a fault condition,
monitoring for it is a proactive-monitoring problem, not an incident-response
one: see [safety-control upward and downward
forces](safety-control-upward-and-downward-forces.md) for how a monitoring
architecture can be built specifically to detect a system drifting toward
resonance before it happens.
