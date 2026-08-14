---
type: concept
title: Exhaustive Archival Search Instruction
description: >
  Tell document agents the answer is always in archival memory and to keep
  searching — including nested key lookups — until verification, not early exit.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §6 Appendix"
---

For [OS-inspired agent memory](os-inspired-agent-memory.md) document and
key–value tasks, the system prompt’s job is not only “you may search” but
**when to stop**. Effective MemGPT-style instructions:

- State that the answer **is always** in archival memory — keep calling search
  if not found.
- Require citing the archival hit used (`ANSWER: …, DOCUMENT: …`) so graders can
  check grounding, not only fluency.
- For nested K/V chains: do not stop until verifying a value is **not** itself
  a further key; baselines need the same nested-lookup rule when all context
  is dumped upfront.

Without the keep-searching / nested-until-done contract,
[self-directed memory management](self-directed-memory-management.md) often
answers from shallow top-\(K\) or invents from weights. Document-analysis
judges should reject missing `DOCUMENT` fields and
`INSUFFICIENT INFORMATION` when gold exists — score **answer + evidence**, not
answer alone ([offline prompt evaluation](offline-prompt-evaluation.md)).
Baselines that receive a fixed retrieved list still need
`INSUFFICIENT INFORMATION` when none support the answer, so ungrounded
completions do not count as success.
