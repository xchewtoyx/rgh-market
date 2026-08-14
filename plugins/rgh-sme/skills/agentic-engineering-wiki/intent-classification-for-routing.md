---
type: concept
title: Intent Classification for Routing
description: >
  Classify what the user is trying to do so the agent selects the right tools
  and can decline out-of-scope queries before wasting a plan.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

Intent classification identifies what the user is trying to accomplish before
or during planning. It can be a prompt or a dedicated classifier. Correct
intent steers [tool inventory](tool-inventory.md) selection — billing queries
need payment tools; password resets need docs retrieval — and supports breaking
complex requests into simpler subtasks.

The classifier should be able to label a query **IRRELEVANT** (out of scope) so
the agent declines politely instead of inventing an impossible plan. That early
exit prevents wasted compute and reduces
[planning failure modes](agent-planning-failure-modes.md) driven by goal
mismatch.
