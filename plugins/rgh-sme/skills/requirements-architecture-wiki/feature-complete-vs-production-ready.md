---
type: concept
title: Feature-Complete vs. Production-Ready
description: >
  Conventional requirements practice specifies what a system should do
  and neglects what it must never do, leaving operational failure modes
  undiscovered until they happen in production against real conditions.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 1"
---

Conventional requirements practice focuses almost entirely on
[functional requirements](functional-requirement.md) — what a system
*should* do — verified by feature checklists and input validation against
a QA suite. It systematically neglects the implicit operational
requirements: what a system must *not* do. It must not crash, hang, leak
memory, violate privacy, or lose money, and none of that shows up on a
feature checklist because it was never elicited as a requirement in the
first place.

Nygard calls the resulting gap the **QA Lab Fallacy**: systems get built
and tested to pass an artificial, pristine test suite that doesn't
represent hostile production conditions — unstructured and adversarial
inputs, degrading hardware, real traffic spikes — so the operational
qualities that would have caught these failures are discovered for the
first time as an outage, not as a requirement that was checked off during
design.

The fix this argues for is treating operational qualities as first-class
requirements to elicit and specify — see [non-functional
requirement](non-functional-requirement.md) and, for the stronger claim
that the "non-functional" label itself contributes to the neglect,
[operational requirements as first-class
requirements](operational-requirements-as-first-class.md) — rather than as
engineering afterthoughts owned informally by whoever happens to be on
call when they matter. "Feature-complete" and "production-ready" measure different
things, and a specification that only captures the first has not actually
finished specifying the system.
