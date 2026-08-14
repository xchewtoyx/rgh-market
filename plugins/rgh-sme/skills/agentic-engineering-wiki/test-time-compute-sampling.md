---
type: concept
title: Test-Time Compute Sampling
description: >
  Generate several candidate completions instead of one and select the best,
  trading roughly linear extra cost for higher output quality.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 2"
---

Instead of generating a single response per query, generate several and pick
the best one. Cost scales roughly linearly with the number of samples (two
outputs cost roughly twice one, modulo optimizations like reusing shared
prompt processing across the outputs) — the name "test-time compute" borrows
ML-research terminology where "test time" means inference, even though the
technique applies to ordinary production inference, not just research
evaluation. **Best-of-N** generates the N outputs independently; **beam
search** is the more strategic variant, keeping a fixed number of
most-promising candidates (the beam) alive at each generation step rather
than generating full independent completions and comparing only at the end —
the same lookahead idea covered in [temperature and
sampling](temperature-and-sampling.md).

Increasing *diversity* among the candidates — for example, varying sampling
parameters across the separate generations rather than reusing identical
settings — tends to improve the odds that at least one candidate is good.

**Selecting the best of N** needs its own method, and the right one is
task-dependent:

- **Show all candidates to the user** and let them choose directly.
- **Highest average logprob.** A sequence's probability is the product of its
  tokens' conditional probabilities; summing logprobs instead of multiplying
  probabilities avoids numeric underflow. Longer sequences accumulate more
  negative logprob simply by having more tokens, so *average* logprob (sum
  divided by length) is used instead of raw total, to avoid systematically
  favoring shorter outputs.
- **Reward model or verifier score** — a separately trained scorer ranks
  candidates. Reported to be a particularly strong lever in practice: one
  study found the accuracy boost from adding a verifier to a small model
  roughly matched a 30x increase in model size on its own.
- **Application-specific heuristics** — e.g. prefer the shortest valid
  candidate, or keep generating until output actually parses as valid SQL for
  a text-to-SQL task.
- **First-completed-and-valid** — for latency-sensitive cases with long
  generation times (e.g. chain-of-thought queries), generate several
  candidates in parallel and surface whichever finishes first *and* passes
  validation, rather than waiting for every candidate to complete.
- **Most-frequent-answer (self-consistency)** — good for tasks with one exact
  correct answer (math, multiple choice): sample many independent
  completions and take a majority vote over the final answers, discarding the
  reasoning paths that led there.

A model is **robust** when small input variations don't dramatically change
its output; the less robust a model is, the more this technique helps, though
sampling more outputs is a workaround for a brittle model, not a fix for one
— swapping to a more robust model is the more durable option when that's
feasible. There are diminishing, and eventually *negative*, returns to
sampling more candidates: one experiment found performance improving up to
roughly 400 samples and then decreasing, hypothesized to be because more
samples increases the odds of finding an adversarial output that happens to
fool the verifier being used for selection — though a separate study found
solve rate still increasing log-linearly out to 10,000 samples on a different
task, so the shape of this tradeoff is task-dependent, and in practice
production systems rarely sample anywhere near that many candidates per
request given the linear cost.
