---
type: concept
title: Cyclic Workflow Repair Loops
description: >
  Route a failed work item back to an earlier task for another attempt, at the
  cost of context reattachment, universal failure handling, and loop limits.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

A cyclic [workflow topology](workflow-topology.md) — output from a task
circling back to an upstream task — is useful for quality control: if a
generated result is high quality, send it onward; otherwise route failure
information back to an earlier step to try again. LLM-based workflows
sometimes need this to repair a work item after an LLM mistake, but cycles add
considerable complexity compared to a DAG:

- Failure information looping back to an earlier task must be reunited with
  whatever original context that task needed (e.g. the source website
  content) — context a DAG's one-directional flow would never need to retain
  past the task that first consumed it.
- Every task in the loop must now anticipate that a work item may arrive
  carrying failure info attached, and handle that case in its own
  implementation — not just the task that detects failure.
- A stopping mechanism is required (an attempt counter plus a give-up
  threshold) so a work item cannot cycle indefinitely.

Recommendation: where possible, hide recursion *inside* a single task rather
than hoisting the cyclic complexity up to the workflow level, where every
other task in the loop would otherwise need to handle carrying failure state.
This pairs naturally with [Reflexion](reflexion.md) at the task level
(evaluate output, self-reflect, retry inside the task) as an alternative to a
workflow-level retry loop that routes a failed item all the way back to an
earlier task.
