---
type: concept
title: "Coupling: The Probability a Change Propagates"
description: >
  Coupling is the probability that a modification to one module requires a
  modification to another, which arises whenever the two modules'
  responsibilities overlap — the formal, quantitative face of dependency
  and change amplification.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 8 (concept traces to 1960s structured-design theory)"
---

Formally: coupling between two modules is the probability that a
modification to one requires a modification to the other, to keep the
overall system correct. It arises whenever two modules' responsibilities
overlap — the more one module's implementation choices leak into what
another module has to know or assume, the higher that probability climbs.
This is the same phenomenon [dependencies as a cause of
complexity](dependencies-as-a-cause-of-complexity.md) describes from the
angle of a single codebase's cognitive load: a dependency is exactly a case
where one piece of code can't be understood or changed in isolation, and
coupling is the probabilistic measure of how often that inability actually
bites.

High coupling is modifiability's enemy — it's the mechanism behind [change
amplification](change-amplification.md): a design decision that should
have touched one module instead ripples into others because they were
never truly independent. [Shotgun Surgery](shotgun-surgery.md) is high
coupling's most visible symptom: one conceptual change forces edits
scattered across many modules.

**Reducing coupling** generally means inserting an intermediary between two
otherwise tightly-coupled modules — the same move as
[encapsulation](information-hiding.md) and [dependency
inversion](dependency-inversion-principle.md): depend on a stable interface
rather than directly on another module's concrete implementation, so the
implementation can change without forcing a corresponding change on the
dependent side. Restricting *which* modules may depend on which — a
layer using only the next layer down, a wrapped class reachable only
through its wrapper — is a structural way to keep coupling low by
construction rather than relying on discipline alone.

See [cohesion](cohesion.md) for coupling's complementary measure — how
tightly a single module's own responsibilities belong together — and
[Divergent Change](divergent-change.md) for what happens when cohesion,
rather than coupling, is the underlying problem. Coupling inferred purely
from reading code can also miss real coupling that only shows up in how
files actually change together over time — see [evolutionary
coupling](evolutionary-coupling.md).
