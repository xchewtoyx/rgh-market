---
type: concept
title: Checklist Forcing Function Types
description: The two complementary purposes a checklist item can serve — forcing a predictable step to happen, or forcing team members to exchange information — and why complex operations need both.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 4"
---

Checklist items serve one of two distinct purposes. Confusing the two, or building a checklist that only serves one, leaves a documented procedure unable to handle the situations it will actually meet in production.

## The Two Types

- **Procedural forcing functions**: Ensure a basic, predictable, but easily-forgotten step is never skipped (e.g. "confirm the correct target before an irreversible action"). These items guard against lapses in routine, well-understood work.
- **Communication forcing functions**: Establish a mandatory touchpoint where operators exchange information, surface risks that weren't anticipated in advance, and adapt the plan to the actual situation (e.g. a team briefing before a non-routine event). These items guard against the unknown-unknowns that no fixed procedural step could anticipate, because the plan itself can't enumerate them ahead of time.

## Why Both Are Needed

A checklist built entirely from procedural items is brittle: it executes flawlessly for the failure modes its authors thought of, and offers nothing when reality departs from the plan. A checklist built entirely from communication items is unreliable: it relies on operators to reason correctly in the moment about routine steps that are better handled by rote verification.

Effective operational checklists mix both types deliberately: procedural items to eliminate lapses in the routine parts of the job, and communication items placed at the points where non-routine risk is most likely to surface (before a change, before a handoff between operators, at a natural pause point).

This distinction is one input into deciding what earns a place on a length-constrained checklist — see [Checklist Item Selection Trade-offs](checklist-item-selection-tradeoffs.md). For how communication-type items should actually be run once included, see [Checklist Execution as Team Communication](checklist-execution-as-team-communication.md).

For work that spans multiple specialists or system components, the communication-forcing type is often best implemented as a standalone document rather than items embedded in a process checklist — see [Cross-Specialist Communication Schedule](cross-specialist-communication-schedule.md).
