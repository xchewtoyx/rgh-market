---
type: concept
title: Next-Turn Salience Promotion
description: >
  A middleware warning appended after tool output routinely gets ignored on
  the very next model turn — promote it into a top-of-context reminder before
  that turn instead of trailing it after the observation.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. C.1.4, C.2.4"
---

A middleware hook that detects a risky pattern (see
[proxy-validation failure pattern](proxy-validation-failure-pattern.md) for a
concrete catalog) and appends a warning to that step's tool output can still
fail to change the agent's behavior — not because the detection was wrong, but
because the warning arrives in the wrong place in context. Tool output trails
the step that produced it; the model's *next* decision (publish, clean up,
submit) is often made from attention weighted toward the most recent and most
prominent parts of context, and a warning buried in the tail of a tool
observation loses to whatever the model was already planning to do.

**Next-turn salience promotion** fixes the placement, not the detection: carry
any execution-risk note emitted on one step forward and re-inject it as a
prominent, top-of-context reminder immediately before the *next* model turn —
visible at the point where the model is actually reasoning about what to do
next, rather than sitting downstream of a tool result the model has already
mentally moved past. The same detection logic that worked before can start
actually changing outcomes purely by moving where its output lands in the
prompt.

This is a specific instance of a general
[context engineering](context-engineering.md) principle: what gets attended
to depends on placement and salience, not only on whether the information is
present somewhere in context at all. Where possible, pair salience promotion
with an execution-time enforcement mechanism for anything safety-critical
(see [publish-state protection guard](publish-state-protection-guard.md)) —
a promoted reminder makes the right action more likely, but only a tool-level
intercept makes the wrong action impossible; use promotion for guidance the
harness can't cheaply hard-block, and hard blocks for guidance it can.
