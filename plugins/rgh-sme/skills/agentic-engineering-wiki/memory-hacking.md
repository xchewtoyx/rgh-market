---
type: concept
title: Memory Hacking
description: >
  Adversarial conversation that implants false past events into an agent’s
  durable memory — a retrieval/reflection risk beyond ordinary prompt injection.
sources:
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

Long-lived agents that store comprehensive experience in a
[memory stream](memory-stream.md) can be attacked by **memory hacking**: craft
dialogue that convinces the agent a nonexistent past event occurred, then let
retrieval and [reflection trees](reflection-tree.md) amplify the lie into
plans and speech. This is distinct from one-shot
[jailbreaking and prompt injection](jailbreaking-and-prompt-injection.md) —
the payload persists across sessions via the memory architecture itself.

Mitigations for [generative agent architecture](generative-agent-architecture.md)
and [OS-inspired agent memory](os-inspired-agent-memory.md): provenance tags on
observations, distrust unverified user claims before archival write, audit
logs of inputs and generated outputs, and disclose computational nature to
limit parasocial misuse. Treat embellished or world-knowledge-bleed memories
as expected failure modes in
[offline prompt evaluation](offline-prompt-evaluation.md) interviews, not as
rare bugs.
