---
type: concept
title: Engineering Work vs. Toil vs. Overhead
description: >
  Operational work splits into three categories with different value —
  engineering work builds enduring, sublinearly-scaling improvements, toil
  is manual work that scales linearly and leaves nothing behind, and
  overhead is administrative work that isn't either.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 5"
---

# Engineering Work vs. Toil vs. Overhead

Time spent operating a production system isn't a single undifferentiated
pool — it's worth splitting into three categories, because only one of them
compounds in your favor:

- **Engineering work**: designing, building, and refactoring software,
  architecture, or automation systems. It produces enduring value — the
  system is measurably better afterward — and the effort required scales
  sublinearly with the system's growth.
- **Toil**: see [toil](toil.md) — manual, repetitive, automatable, reactive
  work with no enduring value, scaling linearly with the system.
- **Overhead**: administrative work that isn't operational at all — hiring,
  team meetings, performance reviews, travel. It's neither toil nor
  engineering work, and doesn't get counted against either budget.

The distinction matters because only engineering work — building the
automation, tooling, or platform that removes a class of toil permanently —
changes the shape of the curve. Doing the toil faster or more carefully
doesn't; it's still linear. This is the basis for [the case for eliminating
toil](case-for-eliminating-toil.md): the goal isn't to do toil more
efficiently, it's to convert time spent on toil into time spent on
engineering work that removes it.
