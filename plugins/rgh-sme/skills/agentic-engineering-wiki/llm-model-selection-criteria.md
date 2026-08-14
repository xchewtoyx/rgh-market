---
type: concept
title: LLM Model Selection Criteria
description: >
  Rank candidate models by intelligence, speed, cost, ease of use,
  functionality, and special constraints — and keep the choice swappable in code.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

Model pick drives agent and workflow success, but named model rankings go
stale fast — encode *criteria*, not a hard-coded winner. Prefer a
[model gateway](model-gateway.md) or unified client so swapping providers is
revision, not rewrite. Cost and latency are their own bucket under
[application evaluation criteria](application-evaluation-criteria.md): a
high-quality but slow or expensive model is not useful for the product even
if it wins every capability benchmark.

Order of importance for most harnesses:

1. **Intelligence** — closeness to an expert human answer; dominant when the
   agent needs hard reasoning or high accuracy.
2. **Speed** — user-visible wait; dominant for interactive agents.
3. **Cost** — per-call inference or GPU; dominant for high-frequency loops
   (many tool turns, [self-consistency decoding](self-consistency-decoding.md)).
4. **Ease of use** — how much provisioning, routing, and recovery the platform
   absorbs.
5. **Functionality** — instruct/chat/tool-use, logprobs, multimodal, and other
   harness features the [ACI](agent-computer-interface.md) assumes
   ([logprob completion quality signal](logprob-completion-quality-signal.md)).
6. **Special requirements** — open weights, data residency, update cadence,
   logging/on-prem — these can veto otherwise strong options.

**Pareto / hard-filter selection.** Be explicit about which objectives are
non-negotiable. Filter candidates against hard latency and cost thresholds
first, then pick the best quality among survivors — do not average a
deal-breaking p90 latency into a soft "overall score." Write each criterion
as *metric + benchmark + hard requirement + ideal* (e.g. cost per output
token hard `< $30/1M`, ideal `< $15/1M`; time-to-first-token p90 hard
`< 200ms`; factual-consistency internal score hard `> 0.8`). Distinguish
must-have vs nice-to-have latency: everyone says they want lower latency if
asked, but for many products high latency is an annoyance rather than a
ship-blocker. Latency depends on the model, the prompt, and sampling;
autoregressive generation means more output tokens raise wait time —
mitigate with concise prompting and stopping conditions, not only by
buying a faster model.

**API vs self-hosted cost shape.** Hosted APIs typically charge per token
(input + output), so reducing tokens reduces cost linearly. Self-hosting is
mostly compute: teams often pick the largest model that fits available GPU
memory (common sizes cluster popular open models around ~7B or ~65B
parameters). API $/token stays roughly flat with traffic; self-hosted
$/token can fall once a cluster is provisioned (a fleet sized for 1B
tokens/day costs the same at 1M or 1B) — re-evaluate build-vs-buy at
different scale points rather than once.

Trade-offs: high-volume simple steps tolerate a cheap small model; low-volume
hard work can afford a premium tier; wanting both cheapest *and* smartest at
high volume is usually impossible. Within a provider lineup, pick the
**smallest model that reliably clears the task**. For
[chain-of-thought prompting](chain-of-thought-prompting.md), that threshold is
often higher than “can emit step-by-step text” —
[scale-dependent chain of thought](scale-dependent-chain-of-thought.md) means
CoT can hurt undersized models. Prototype slightly above the budget you expect
at ship time — flagship releases push older prices down, and prompts already
tuned for the stronger model keep paying off. Route easy vs hard steps with a
[model router](model-router.md) under the
[generality–strength tradeoff](generality-strength-tradeoff.md) rather than one
global model for every turn.
