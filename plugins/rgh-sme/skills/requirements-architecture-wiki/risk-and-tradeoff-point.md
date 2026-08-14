---
type: concept
title: Risk, Non-Risk, Sensitivity Point, and Tradeoff Point
description: >
  Four terms for classifying what an architecture evaluation finds when it
  checks a decision against quality-attribute scenarios — distinguishing a
  problem from a deliberate, analyzed tradeoff instead of lumping every
  finding together as "an issue."
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 21"
---

When an [architecture evaluation](architecture-tradeoff-analysis-method.md)
walks a design decision against the [quality attribute
scenarios](quality-attribute-scenario.md) it's meant to satisfy, four
distinct outcomes are worth recording under four different names, because
they call for different follow-up:

- A **risk** is a decision that may cause an undesirable consequence given
  a stated quality-attribute requirement — something that needs either a
  fix or an explicit, owned decision to accept it as-is.
- A **non-risk** is a decision that was analyzed and judged safe. Recording
  non-risks matters as much as recording risks: it's the evidence that a
  concern was actually checked, not simply overlooked, and it keeps a
  later reviewer from re-litigating a question that already has an
  answer.
- A **sensitivity point** is a decision that has a marked effect on some
  quality attribute's response — a parameter worth watching closely,
  because a small change to it moves that response a lot.
- A **tradeoff point** is a decision where two or more quality-attribute
  responses are *both* sensitive to it, and move in opposite directions —
  a worked example: heartbeat frequency is a sensitivity point for
  availability (faster heartbeats mean faster fault detection) and also
  for performance (faster heartbeats cost more processing and bandwidth);
  because the two responses pull against each other at the same decision
  point, it's a tradeoff point, not just two separate sensitivity points.

Individual risks that share a common underlying cause are worth grouping
into a **risk theme** — for example, several unrelated-looking risks that
all trace back to inadequate documentation, or to insufficient attention
to availability. A risk theme is what turns a list of technical findings
into a systemic diagnosis, and mapping each theme back to the specific
business goal it threatens is what makes a technical risk legible to a
manager who isn't going to read the individual findings — see
[business-goal-driven requirements](business-goal-driven-requirements.md)
for where those goals come from in the first place.

This vocabulary is worth using in any [trade-off
write-up](documenting-trade-offs.md), not just a formal ATAM exercise: it
forces a reviewer to say specifically which of these four things a
finding is, rather than flattening every observation into an undifferentiated
"issue," which is what makes the eventual remediation or acceptance
decision traceable back to a specific, named concern.
