---
type: concept
title: Dynamic Context Source Discovery
description: >
  Find what runtime context to gather by mind-mapping the question and ranking
  sources by application proximity and stability.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

[Dynamic context gathering](dynamic-context-gathering.md) needs a systematic
way to invent candidate facts before wiring retrieval. Two complementary
moves:

**Mind-map the target question.** Put the ask in the center and vary words
or aspects ("What book shall I read *next*?" → drop "next", vary "I") until
follow-up questions appear ("What did I read last?", "Did I like it?"). This
surfaces context you would want *if you had it*; obtaining some items may be
infeasible or deferred to a later version.

**Inventory what you can actually gather**, then assess relevance. Sort
candidates on either axis (pick one; both are optional):

- **Proximity to the application** (nearer ≈ easier): on-screen / system
  state → already-saved profiles → activity the app could start recording →
  public APIs → permissioned systems or direct user questions. Farther
  sources must earn more usefulness to justify cost.
- **Stability** (more stable ≈ easier to prepare): always-same user facts →
  slow-changing histories → ephemeral live state. Unstable sources resist
  preparability and amplify latency pressure.

Recommended loop: mind-map desired knowledge, list obtainable sources,
ship the obvious near ones first, then extend to exotic sources as
[context engineering](context-engineering.md) matures.
