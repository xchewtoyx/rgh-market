---
type: concept
title: Operability as a Design Property
description: Treating how easy a system is for an operator to run day-to-day as a deliberate design goal alongside correctness and performance, not an afterthought left to documentation.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 1"
---

A system's maintainability rests on more than whether its documentation is good — it also depends on whether the system itself was built to be operable: whether routine operational tasks are actually easy to do, independent of how well anyone wrote them up afterward. Operability is a property of the system's design, not a property of its documentation, and the two need separate investment.

## What Operable Systems Provide

- **Visibility into runtime behavior**: good monitoring and telemetry so an operator can see what the system is actually doing, not just what it's supposed to do.
- **Support for automation**: standard interfaces that let routine work be scripted rather than performed by hand every time.
- **Avoiding dependency on individual machines**: routine maintenance (patching, upgrades) doesn't require any specific node to stay alive or in a particular state.
- **Good, overridable defaults**: the system behaves sensibly out of the box, but an operator can still override behavior explicitly when the default doesn't fit.
- **Self-healing where appropriate, with manual override**: the system recovers from routine faults automatically, but an operator can always step in and take manual control when automatic recovery isn't the right call.
- **Predictable behavior**: minimizing surprises, so an operator's mental model of the system stays accurate over time.

## Relationship to Documentation-Driven Approaches

This is the operational-readiness counterpart to [Reducing Documentation Need Through System Design](reducing-documentation-need-through-system-design.md): both treat a system property (how much explanation it needs, how easy it is to run) as a design target to optimize directly, rather than relying entirely on downstream artifacts — runbooks in one case, prose documentation in the other — to compensate for a system that wasn't built with operators in mind. A system with strong visibility, automation support, and predictable behavior needs a thinner [runbook](runbook-checklist-design.md) to operate safely, because much of what a runbook would otherwise have to spell out is instead directly observable or automatically handled by the system itself.
