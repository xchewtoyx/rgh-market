---
type: concept
title: Fresh-Context State Summary
description: >
  Rebuild each agent turn from a written environment summary so the only memory
  of prior steps is what the harness deliberately records.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §2"
---

Some browsing and tool agents reset the model prompt every step: the LM sees a
**fresh context** containing the question, current page (or tool state) at the
cursor, and a harness-written summary of prior actions — not the raw full
trajectory. Prior steps persist only if the summary records them.

This is deliberate [context engineering](context-engineering.md) and
[agent memory tiers](agent-memory-tiers.md): the summary is the durable working
memory; observations stay local to the turn (pair with
[collapsed observations](collapsed-observations.md) when you keep a longer
transcript instead). Design the summary schema carefully — missing fields are
permanent amnesia. Combine with a small discrete
[browser tool action inventory](browser-tool-action-inventory.md) so each turn
still emits one valid command under
[action format enforcement](action-format-enforcement.md).
