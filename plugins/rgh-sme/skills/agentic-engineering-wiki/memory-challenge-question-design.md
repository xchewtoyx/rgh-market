---
type: concept
title: Memory Challenge Question Design
description: >
  Build long-memory eval questions that require the old conversation log — never
  answerable from persona summaries alone — so retrieval, not priors, is tested.
sources:
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §6 Appendix"
---

When synthesizing [deep memory retrieval](deep-memory-retrieval.md) probes
(self-instruct over multi-session chats), constrain the generator so each
question:

1. Is asked from user A to user B about something B would know only by having
   **participated in a prior conversation**.
2. Is **not** answerable from persona cards alone (“cheating”) — the gold must
   live in the chat log, not in static “I like surfing”-style facts.
3. Has a narrow, checkable answer (place, item, commitment) suitable for
   ROUGE/LLM-judge scoring.

Worked contrast: after a Pacifica surfing chat that mentions Taco Bell lunch,
ask where they ate (requires the log); do not ask whether they like surfing
(persona-only). Pair with judge instructions that are **topic-generous** but
**hard on wrong items / “I don’t remember”**, and force a single final token
(`CORRECT`/`WRONG`) after a one-sentence rationale so grading scripts stay
parseable under [offline prompt evaluation](offline-prompt-evaluation.md).
