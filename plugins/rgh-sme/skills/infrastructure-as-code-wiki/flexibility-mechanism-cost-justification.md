---
type: concept
title: Flexibility Mechanism Cost Justification
description: A cost inequality for deciding whether a change mechanism (a parameter, a factored-out module, a config option) is worth building versus hand-editing code each time a similar change recurs.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 8"
---

Every mechanism that lets someone change infrastructure without editing code — a [stack instance parameter](stack-parameter-design-principles.md), a factored-out module, a config-file setting — costs something to build, and usually costs less to exercise afterward than a bare code edit would. Whether building it is worth it depends on how many times you expect to use it: given N anticipated instances of a similar change, building the mechanism pays off when

**N × (cost of a plain code edit) ≥ (cost of building the mechanism) + N × (cost of exercising the mechanism)**

This gives the "don't add a parameter until you need it" heuristic a concrete reason rather than treating it as a bare rule of thumb: a parameter added for a single anticipated caller rarely clears this bar, since the mechanism's build cost is paid once but its savings only accrue per use. A few caveats keep the inequality honest rather than falsely precise: N is itself a guess, and building an expensive mechanism for a change that turns out rarer than expected leaves you worse off than if you'd just hand-edited each time; money and time spent building the mechanism isn't spent on anything else, so it's a real opportunity cost, not a free investment; and a cheaper mechanism that isn't ready when the change is actually needed doesn't help — availability timing matters as much as total cost.

The same reasoning applies one level up when deciding whether a repeated infrastructure change pattern is worth [extracting into a reusable module](reusable-stack-pattern.md) or an [abstraction-layer component](abstraction-layer-for-infrastructure.md): the module's authoring and testing cost only pays for itself across enough consuming call sites, which is why premature abstraction — building a general mechanism for a change that never recurs — is exactly the failure mode this inequality predicts.
