---
type: concept
title: Timing of Architectural Decisions
description: >
  Architecture decisions are usually made at the point of least real
  knowledge about a system's operational behavior, and become
  organizationally hard to reverse regardless of whether they were
  technically sound — which is why capturing their rationale matters.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 1"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 13"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 4"
---

System boundaries and subsystem decompositions chosen early in a project
tend to crystallize into team structures, budgets, and management
hierarchies (Conway's Law) — and they are typically chosen at the point
when the team has the least real knowledge of how the system will actually
behave in production, sometimes called "peak ignorance." The decision then
becomes organizationally difficult to reverse, independent of whether it
was the technically right call.

This has two consequences for how a decision should be documented. First,
the constraints and assumptions in force *at decision time* need to be
recorded explicitly — a design that looks "prescient" or "shortsighted" in
hindsight usually just served the goals and scale of its own era, and
there is no single architecture that works at 1x, 10x, and 100x scale, so
judging a past decision by later requirements it was never meant to meet
is a documentation failure, not a design failure. Second, deferring a
decision's real cost (security, reliability, maintainability work skipped
to preserve short-term velocity) is not free just because it isn't paid
immediately: these properties are usually emergent rather than localized
to one module, so retrofitting them later is comparable in cost to
changing a foundational architectural choice, and doing that retrofit
under incident pressure risks introducing further flaws.

Nygard's related distinction is between **Ivory Tower Architecture**
(dogmatic standards detached from physical and operational constraints)
and **Pragmatic Architecture** (grounded in acknowledged real-world
constraints: networks drop packets, disks fill, third-party APIs fail).
The rationale a decision record needs to capture is exactly the pragmatic
constraints in force when the decision was made — see [architectural
decision capture](architectural-decision-capture.md).

Capturing rationale after the fact is only half the discipline; the
forward-looking half is tracking how much [architectural
runway](architectural-runway.md) the current design still has before its
next decision point becomes forced by circumstance rather than chosen
deliberately. One lever for reducing how much rides on getting a
peak-ignorance decision right the first time is sorting decisions by how
expensive they are to undo — see [reversible architectural
decisions](reversible-architectural-decisions.md) — and deliberately
designing more of them as cheaply reversible.
