---
type: concept
title: Incremental Infrastructure Change
description: Delivering a large infrastructure redesign as a sequence of small, independently pushed changes, rather than as one big-bang cutover, using incremental, iterative, walking-skeleton, and refactoring techniques.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

Large infrastructure changes — splitting a [monolithic stack](monolithic-stack-antipattern.md) into several, swapping a cluster technology — are safer and more debuggable delivered as a series of small changes than as one big cutover, for the same reason Agile and Lean generally favor small batch sizes: a small change is easier to plan, implement, test, and debug than a large one. A single engineer following this discipline effectively can push changes as often as hourly, each one integrated and tested for production-readiness through the full [pipeline](infrastructure-delivery-pipeline.md).

A few related terms describe the shape of this incremental work: an **incremental** change adds one complete piece of a larger plan (build the networking stack, then the cluster stack, then the application stack); an **iterative** change makes a basic version of everything and progressively deepens it; a **walking skeleton** is a bare-bones implementation of a new system's main parts, built to validate its overall shape before investing in production-grade choices for every piece; **refactoring** changes a component's internal design without changing its external behavior, often specifically to make a later behavioral change easier and safer — for example, extracting a container cluster into its own stack purely to establish clean integration points, before actually changing what runs inside it.

Because infrastructure serves live traffic, delivering a change incrementally often means the system has to keep working correctly *during* a multi-step migration, not just before and after it — see [pushing incomplete changes to production](feature-toggles-for-infrastructure.md) and [zero downtime infrastructure changes](blue-green-infrastructure-change.md) for the specific techniques that make that possible.
