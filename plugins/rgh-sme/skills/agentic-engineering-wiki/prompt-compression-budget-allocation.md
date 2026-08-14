---
type: concept
title: Prompt Compression Budget Allocation
description: >
  Give a prompt's instruction and question a light compression ratio and its
  demonstrations a heavier one, selecting which demonstrations survive by
  perplexity rather than compressing every segment uniformly.
sources:
  - title: "LLMLingua: Compressing Prompts for Large Language Models"
    resource: "LLMLingua (Jiang et al.), §4.1"
---

When a prompt must be compressed to fit a token budget, compressing every
segment by the same ratio wastes the budget: not all prompt segments carry
equal risk if trimmed. The **budget controller** pattern allocates a
*different* compression ratio per segment role instead of one uniform ratio,
before [perplexity-based token pruning](perplexity-based-prompt-compression.md)
is applied within each role's allotted budget:

- **Instructions and the question get a light compression ratio** — they
  directly determine what the model is supposed to produce, so they need to
  retain essentially all their original content.
- **Demonstrations get a heavier compression ratio** — when several
  demonstrations are present, they are often mutually redundant, so more of
  the token budget can be reclaimed from them without losing information the
  instruction/question pair doesn't already convey.

Within the demonstration budget, selection is **at the demonstration level,
not the token level**, and **ranked by perplexity**: compute each candidate
demonstration's perplexity under a small reference model, sort demonstrations
in *descending* perplexity order, and keep adding whole demonstrations to the
kept set until the running token total would exceed the demonstration budget.
Higher-perplexity demonstrations — content the small model finds more
surprising, hence more informative — are kept preferentially over
low-perplexity ones the model would have predicted anyway. Any budget left
over from demonstration selection stopping short of its allocated ratio (a
demonstration boundary rarely lands exactly on the budget line) rolls forward
into a slightly relaxed compression ratio for the instruction and question.

Whole-demonstration selection at this stage exists specifically to avoid a
failure mode of pure token-level dropout at high compression ratios: dropping
individual tokens indiscriminately across a demonstration can leave a
trivialized, barely-coherent fragment behind, while dropping an entire
low-value demonstration and keeping a high-value one intact preserves
linguistic integrity where it matters. Finer-grained token-level compression
is then applied only *within* whatever text survives this coarser,
role-differentiated allocation — not as a substitute for it. That
finer-grained pass should itself account for what's already been dropped
elsewhere in the prompt rather than scoring every token in isolation; see
[iterative token-level compression](iterative-token-level-compression.md).

This complements [elastic snippets](elastic-snippets.md)'s approach to
budget-constrained prompt assembly: elastic snippets choose *which whole size*
of one retrieved item fits the remaining space, while budget allocation here
decides *how much compression each prompt role* (instruction, question,
demonstrations) is allowed to receive before any individual item's size is
even considered — the two operate at different levels of the same
budget-fitting problem and can be combined.
