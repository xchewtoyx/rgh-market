---
type: concept
title: "Binding Time: When a Change Gets Fixed in Place"
description: >
  The point in a system's life cycle at which a design decision becomes
  fixed — source edit, compile, build, deployment configuration, or
  runtime — and why deferring it later is cheaper only if the architecture
  was prepared for that deferral in advance.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 8"
---

Every design decision gets bound — fixed in place — at some point in a
system's life cycle: at implementation (a source-code edit), at compile
time (a compile-time switch or flag), at build time (choosing which
library or component to link in), at deployment/configuration time (a
setting an installer or administrator provides), or at runtime (a
parameter or plug-in chosen while the system is running). Different agents
naturally act at different binding times too — a developer binds at
implementation or compile time; an administrator binds at configuration
time; an end user, or a self-adapting system, can bind at runtime.

**Later binding is cheaper, all else equal** — human-mediated changes
(editing and redeploying source) are slower and more error-prone than a
computer applying an already-built flexibility mechanism. But "all else
equal" is doing real work in that sentence: later binding is only cheaper
if the architecture was actually prepared in advance to allow it. An
unprepared architecture makes a late-binding attempt costly regardless of
how conceptually late the binding point is — the cost of preparing for
deferral has to be paid somewhere, and it doesn't disappear just because
the binding itself happens late.

[Configuration parameters](configuration-parameters-as-incomplete-solutions.md)
are the archetypal deferred-binding mechanism: a parameter generalizes a
hardcoded value the way `f(a, b)` generalizes `f(a)` fixed at `b = 0`,
moving the moment that value gets fixed later in the life cycle. Whether
that deferral is worth its cost is exactly the trade-off in [every piece of
design infrastructure must pay for
itself](design-cost-benefit-of-infrastructure.md), sharpened by [the
cost-benefit inequality for building a change
mechanism](cost-benefit-of-a-change-mechanism.md): binding is worth
deferring only when enough future changes will actually exercise the
deferral to amortize the cost of building it.

Separating "who builds the mechanism" from "who exercises it" — a
developer builds a flexible mechanism once, an administrator or installer
uses it later, possibly much later, without ever touching code — is called
**externalizing the change**, and is often the whole point of choosing a
later binding time in the first place.
