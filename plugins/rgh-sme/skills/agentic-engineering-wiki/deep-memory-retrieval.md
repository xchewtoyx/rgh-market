---
type: concept
title: Deep Memory Retrieval
description: >
  Probe long-conversation consistency with questions answerable only from prior
  sessions — favoring full recall plus paginated search over lossy summary
  baselines.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §3.1"
---

Deep memory retrieval (DMR) evaluates whether a conversational agent stays
**consistent** when the user asks something that explicitly refers to an
earlier session and has a narrow expected answer. Build QA pairs so the gold
depends only on past-session knowledge; score with ROUGE-L recall (replies are
often more verbose than gold) and/or an LLM judge for consistency.

The harness comparison that matters for
[OS-inspired agent memory](os-inspired-agent-memory.md): fixed-context agents
that see only a **lossy summarization** of prior sessions versus agents that
keep the **full history** in recall storage and must
[self-direct](self-directed-memory-management.md) paginated search into
[main-context sections](main-context-sections.md). Empirically, MemGPT-style
paging lifts accuracy and ROUGE sharply across GPT-3.5/4/4-Turbo bases —
removing the memory layer collapses performance even when the base model is
strong.

Use DMR-style probes in
[offline prompt evaluation](offline-prompt-evaluation.md) whenever an
“infinite context” companion claims weeks-to-years continuity: consistency
(facts align with prior statements) is distinct from **engagement** (drawing
on long-range user knowledge to personalize). Engaging openers that beat
hand-written baselines rely on actively storing persona facts in **working
context**, not only hoping the FIFO transcript still contains them. Construct
synthetic probes with
[memory challenge question design](memory-challenge-question-design.md) so
persona cards cannot short-circuit retrieval.
