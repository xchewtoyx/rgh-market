---
type: concept
title: Coupling and Cohesion in Infrastructure Components
description: The two properties — how often a change to one component forces a change to another, and how closely related a component's own elements are — that determine whether modularizing infrastructure actually makes it easier to change.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 15"
---

Designing infrastructure components well means deciding which elements to group together and which to keep apart, and the goal throughout is low coupling and high cohesion — the same properties software design has used for decades, applied to infrastructure.

**Coupling** describes how often a change to one component forces a change to another. Zero coupling between two things that are genuinely part of the same system usually isn't realistic or desirable; the aim is *low* coupling, where a change to one component rarely ripples into another. **Cohesion** describes how closely related the elements *within* one component are; a stack with low cohesion (say, networking for two unrelated other stacks bundled together) forces unrelated changes through the same [blast radius](blast-radius.md), while high cohesion keeps a component small, focused, and easier to reason about.

Where two or more components are so tightly coupled that their versions genuinely can't vary independently, [tuple-versioned deployment](tuple-versioned-deployment.md) tests and ships them as one approved combination rather than pretending they're independently releasable.

A specific coupling risk to watch for is a **circular dependency** — a provider component that (directly or indirectly) consumes resources from one of its own consumers. Circular dependencies are always a sign to redraw the boundary; the usual fix is moving the offending, consumer-specific elements out of the shared provider and into the consumer that actually needs them, which improves cohesion on both sides at once.

The commitment to [continuously testing infrastructure](progressive-testing-for-infrastructure.md) makes low coupling and high cohesion a forcing function rather than a nice-to-have: it's difficult to write and run fast, isolated tests against a spaghetti codebase with tangled dependencies, or against components too large to provision quickly, so automated testing effectively drives better design as a side effect. This chapter's ideas — [avoiding duplication](infrastructure-domain-specific-languages.md), [drawing boundaries between components](drawing-boundaries-between-infrastructure-components.md), and choosing between [stack modules and stacks as components](infrastructure-domain-entity-pattern.md) — are all applications of coupling and cohesion to specific infrastructure design decisions.
