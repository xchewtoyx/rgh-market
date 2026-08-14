---
type: concept
title: Binary Search Isolation
description: Isolate a faulty component by repeatedly bisecting the space of suspects — system components, a dependency graph, or a revision history — rather than inspecting candidates one at a time.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 12"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

When a fault could originate anywhere in a large space of candidates — services in a call graph, commits in a revision history, subsystems in a codebase — isolate it by bisection: split the candidate set in half, determine which half still exhibits the problem, and repeat. This converges in logarithmic time rather than linear time.

The same idea applies at the code level: reproduce the bug, then disable components or comment out subroutines until the smallest subset of code that still manifests the problem is found. For example, isolating variation in per-thread stack sizes was narrowed from "kernel, glibc, threading library, and all code that starts threads" down to a single culprit library by ruling out each layer with a targeted test.

Bisection presupposes you can reliably reproduce the symptom on each candidate half — if the failure only manifests at production scale or under a specific rare condition, you may not be able to isolate this way and instead need to lean on production telemetry and [the core analysis loop](core-analysis-loop.md) to narrow the search by dimension rather than by component.
