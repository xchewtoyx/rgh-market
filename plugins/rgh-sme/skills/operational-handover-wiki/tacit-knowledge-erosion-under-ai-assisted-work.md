---
type: concept
title: Tacit Knowledge Erosion Under AI-Assisted Work
description: AI coding and operations agents accelerate the loss of institutional knowledge that used to accumulate as a side effect of engineers personally authoring, debugging, and reviewing their own systems.
sources:
  - title: "Observability Engineering"
    resource: "Observability Engineering, 2nd ed. (Majors, Fong-Jones, Miranda), ch. 10"
---

Senior engineers historically accumulated a large body of institutional knowledge — service topology, naming aliases, which dependencies are flaky, recent incident history, which endpoints actually matter to the business — "for free," as a side effect of personally writing, debugging, and reviewing code over years. That knowledge then implicitly seeded the informal context every new team member eventually absorbed.

## Why AI-Assisted Work Breaks This

As coding and operations agents write more code with less line-by-line human review, and deployment pipelines automate further, fewer humans are personally living through the debugging cycles and postmortems that used to generate this context as a byproduct. The informal knowledge layer is eroding faster than most organizations are building an explicit, machine-readable replacement for it — and an AI agent has no access to tacit knowledge that was never written down; unlike a new human hire, it cannot pick it up by osmosis from sitting near experienced colleagues.

This makes the underlying problem this whole domain exists to address — can someone (or something) who wasn't involved operate the system safely — sharper, not milder, as more of the "who" doing daily operational work becomes an agent with zero tacit context by default.

## The Response

Treat the context layer itself — service topology, naming conventions, deploy state, known issues, recent incident history, business criticality of specific components — as a first-class engineering responsibility to keep explicit and current, not an informal byproduct to hope accumulates. Organizations that do this get materially more value from agent integration than organizations that expect an agent to "figure it out" the way a curious new hire eventually would. This is the same discipline [Self-Documenting Declarative Systems](self-documenting-declarative-systems.md) and [Reuse Existing Authoritative Sources](reuse-existing-authoritative-sources.md) already argue for on independent grounds — AI-assisted work simply removes the slack that used to let organizations get away with skipping it.
