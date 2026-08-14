---
type: concept
title: Embedding Decision Support to Reduce Sharp-End Cognitive Load
description: >
  Pairing a generic, high-level sensemaking framework with a real-time
  decision-support tool built into the automation itself lowers how much
  adaptive competence a sharp-end operator must supply unaided during a
  genuine surprise.
sources:
  - title: Resilience Engineering in Practice
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

# Embedding Decision Support to Reduce Sharp-End Cognitive Load

A resilient system architecture combines two complementary properties
rather than relying on either alone:

- **Generic anticipation schemes** — high-level, abstract frameworks for
  sensemaking that wrap around unpredictable variation, instead of rigid,
  hyper-specific action recipes that only fire when the situation matches
  them exactly.
- **Real-time implementation skill** — the sharp end's ability to adapt
  those generic schemes to the actual, constrained conditions in front of
  it, under time pressure.

The second property is expensive to keep sharp in a human alone — it's
exactly the capacity the [irony of resilience](irony-of-resilience.md)
erodes and [unbriefed surprise
exposure](unbriefed-surprise-builds-uncertainty-competence.md) has to work
to rebuild. Engineering decision-support tools directly into the automated
system reduces how much of that burden falls on the human's real-time
adaptation alone: a worked example is building an all-engine-out
glide-distance management module directly into a Flight Management System,
so that during an actual dual-engine-failure event the crew's cognitive
load goes toward flying the specific situation rather than also computing
glide range by hand under time pressure.

This is a design-time investment, not a runbook: it belongs alongside other
[safeguards against runaway automation](safeguards-against-runaway-automation.md)
as part of what an automated system owes the human who has to work with it
during an off-normal event, and it's the same underlying move as
[self-healing overload response](self-healing-overload-response.md) —
handling as much of a known-shape problem automatically as is safe to do,
so that sharp-end attention is spent on the part of the problem that
actually needs human judgment.
