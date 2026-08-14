---
type: concept
title: Prompt-Level Attack Defenses
description: >
  Explicit refuse rules, reinforced system instructions, and known-attack
  preemption inside the prompt — useful layers that never guarantee obedience.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Prompt-level defenses for [defensive prompt engineering](defensive-prompt-engineering.md)
include:

- Explicit prohibitions (do not return emails, phones, addresses; return only
  allowed fields).
- **Repeat the system prompt** before and after untrusted content to reinforce
  the task — at token and latency cost, aiding
  [lost in the middle](lost-in-the-middle.md) placement.
- Preempt known attack modes (roleplay jailbreaks, DAN-style overrides) by
  naming them and instructing the model to continue the original task.
- Inspect third-party default templates for missing safety constraints —
  permissive defaults have shown near-total injection success until restricted.

There is no guarantee the model follows these instructions. Pair them with
[instruction hierarchy](instruction-hierarchy.md) and system-level isolation /
[human approval gates](human-approval-gates.md).
