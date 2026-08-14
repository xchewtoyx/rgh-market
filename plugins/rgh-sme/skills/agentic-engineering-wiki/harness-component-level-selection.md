---
type: concept
title: Harness Component-Level Selection
description: >
  Match a harness fix to the component level whose enforcement strength and
  scope fits the failure — and if a level doesn't stick after repeated
  attempts, pivot to a different level rather than iterating harder there.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. B.2"
---

Given a [component-observable](component-observability.md) harness, the same
failure pattern can usually be fixed at more than one component level, and the
levels are not interchangeable — they differ in scope and enforcement
strength:

| Component | Scope | Enforcement |
|---|---|---|
| System prompt | Applies to every task | Advisory only — the model can ignore it under pressure |
| Tool description | Read when that specific tool is called | Advisory, but scoped to the moment of use |
| Tool implementation | Controls the tool's actual behavior | Enforced — the tool can refuse, hint, or block |
| Middleware | Hooks into the agent loop pipeline | Enforced, and reacts to **cross-step** history a single prompt or tool call cannot see |
| Skill | Loaded on demand when relevant | Advisory, but only surfaces when needed |
| Sub-agent | Delegated, isolated execution | Enforced by the delegation boundary itself |
| Long-term memory | Persists across sessions | Advisory, but survives context resets |

A prompt rule can be forgotten under pressure; a tool-level guard cannot be
bypassed by forgetting, only by an explicit override — see the
[publish-state protection guard](publish-state-protection-guard.md) for a
concrete case where a prompt rule alone left a gap that only a tool-level
intercept closed. Consider all levels before picking one, including creating a
new component if none of the existing ones fit.

**The pivot rule:** if the same failure class persists across two or more
iterations despite fixes at one component level, that level is probably the
wrong choice for this failure — roll the ineffective change back (see
[evidence-driven change manifest](evidence-driven-change-manifest.md)) and
re-approach the same failure pattern from a different level, rather than
stacking a third fix on a level that has already failed twice. A recurring
symptom that a prompt rule cannot cure is a strong signal to move enforcement
down to a tool or middleware level, where the harness can act rather than only
advise.
