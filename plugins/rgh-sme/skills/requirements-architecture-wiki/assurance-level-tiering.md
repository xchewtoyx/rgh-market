---
type: concept
title: Assurance-Level Tiering
description: >
  Ranking each function by the severity of what happens if it fails, then
  spending verification and documentation rigor in proportion to that
  ranking rather than uniformly across the whole system.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 10"
---

Standards like avionics' DO-178C (Design Assurance Levels, A–E from
Catastrophic down to No Effect) and IEC 61508's Safety Integrity Levels
(SIL 1–4) rank each function by the severity of the consequence if it
fails, then require verification effort in proportion to that rank rather
than treating every function as equally deserving of scrutiny. A function
whose failure could kill someone gets exhaustive analysis and testing; a
function whose failure is a cosmetic annoyance gets much less — spending
the same rigor on both wastes budget on the low-severity one and is the
only way to afford the rigor the high-severity one actually needs.

This is a distinct axis from [requirements
prioritization](requirements-prioritization.md): prioritization decides
what to build first based on value, cost, and risk; assurance tiering
decides, for something already committed to being built, how rigorously
its correctness has to be established and documented before it ships. A
requirement's [fit criterion](fit-criterion.md) states what "correct"
means; its assurance level states how convincingly that has to be
demonstrated. The two are set independently — a low-priority feature can
still carry a high assurance requirement if its failure mode is severe
enough, and a high-priority feature can be low-assurance if getting it
wrong is merely annoying.

The tiering is worth recording explicitly against each safety- or
mission-critical [functional requirement](functional-requirement.md),
because it is what later justifies (or challenges) a specific verification
budget: an entertainment-system feature and a flight-control function
compete for the same finite testing budget, and only a documented
assurance level makes it defensible that one gets far more of it than the
other.
