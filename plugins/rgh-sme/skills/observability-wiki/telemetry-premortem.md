---
type: concept
title: Telemetry Premortem
description: Before shipping a system (or as a standing exercise on an existing one), imagine a specific plausible failure has already happened and ask whether current telemetry would let you diagnose it quickly — a thought-experiment way of finding instrumentation gaps without waiting for a real incident or running a live chaos experiment.
sources:
  - title: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts"
    resource: "Thinking in Bets (Annie Duke), ch. 6"
---

A **premortem** imagines a plan has already failed and works backward to find why, as the deliberate negative counterpart to imagining success. Applied to observability specifically: pick a plausible failure mode for a system (a dependency times out, a queue backs up, a specific downstream service returns malformed data) and walk through, concretely, whether the telemetry that exists *today* would let an on-call engineer localize and diagnose it quickly — not whether the system would survive the failure, just whether it would be legible if it happened.

This sits between two other techniques already in the toolkit, cheaper than one and more predictive than the other:

- Compared to [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md), a premortem doesn't require a real incident to have already happened — it finds gaps before they cost anyone an outage, at the price of being speculative rather than evidence-based.
- Compared to [chaos engineering as an observability stress test](chaos-engineering-as-observability-stress-test.md), a premortem is a thought experiment rather than an actual production fault injection — much cheaper to run, but it only surfaces gaps the participants think to imagine, whereas a real injected fault can surface a gap nobody anticipated.

Practical framing that makes the exercise concrete rather than a vague brainstorm: for the chosen failure mode, ask specifically "what would the first dashboard we'd open show," "what would we grep the logs for," and "would that actually distinguish this failure from the two or three other things that look similar from the outside" — the same move as [asking what would have predicted an incident earlier](closing-telemetry-gaps-from-past-incidents.md), run in advance of the failure instead of after it.
