---
type: concept
title: Component Observability
description: >
  Expose every editable harness piece as its own file at a fixed mount point so
  each failure pattern localizes to one component and every edit is a
  reviewable, revertible diff.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3.1"
---

A harness — system prompt, tool descriptions, tool implementations, middleware,
skills, sub-agent configs, long-term memory — is only safely editable, by hand
or by an automated evolve loop, if each of those pieces is an explicit,
independently addressable artifact rather than prose scattered across one
giant prompt. **Component observability** names that property: expose every
editable harness component as its own file at a fixed mount point in a single
workspace, with component types kept **loosely coupled** — adding a middleware
should not require touching the system prompt; adding a skill should not touch
any tool.

This decoupling is what makes root-causing tractable: a given failure pattern
maps to a single component class ("this is a tool-description problem," "this
needs a middleware hook") instead of forcing a diagnosis to hunt through
hundreds of lines of unstructured prompt text for the one clause responsible.
Each logical edit then becomes one commit in the workspace's version-control
history, giving file-level diffs and rollback granularity for free — the
mechanical prerequisite for the attribution step in an
[evidence-driven change manifest](evidence-driven-change-manifest.md) to
actually roll back a single ineffective edit without touching anything else.

Treat this as a sharper, implementation-level version of the
[configurable ACI harness](configurable-aci-harness.md) pattern: where a
configurable harness separates the agent loop from a declarative interface
definition in general, component observability additionally insists each
*type* of component (prompt vs. tool vs. middleware vs. memory) lives at its
own mount point so edits at different levels never collide or require touching
each other. When deciding *which* component level a given failure should be
fixed at, see
[harness component-level selection](harness-component-level-selection.md).
