---
type: concept
title: Explicit vs. Implicit Feedback Signals as Telemetry
description: Production feedback for an LLM/AI application comes as either explicit signals (thumbs-up/down) — intuitive but low-volume and biased toward strongly opinionated users — or implicit behavioral signals, which are higher-volume but need to be chosen for genuine correlation with the outcome that matters, not just for being easy to measure.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

Once an AI application ships, telemetry ("measure everything") becomes the primary evaluation signal — this is the online half of evaluation, feeding the same loop as [the eval/monitoring feedback loop](eval-monitoring-feedback-loop.md). Two kinds of feedback telemetry exist, with different failure modes:

- **Explicit feedback** (e.g. a thumbs-up/down control per response) is intuitive to interpret but biased: only strongly-opinionated users — often specifically angry ones — tend to vote at all, and interaction volume on the control itself stays proportionally low unless overall traffic is very high. A low volume of explicit votes is not evidence of a quiet, well-behaved system; it may just be evidence that the control is rarely used.
- **Implicit indicators** are derived from what users actually do rather than what they explicitly report — for example, GitHub Copilot measures code-completion acceptance rate and whether users subsequently modify what they accepted. These give far more volume, but need careful interpretation: for a scheduling assistant, a user interacting briefly and then leaving could mean efficient task completion (good) or frustrated abandonment (bad) — session length alone is ambiguous and cannot distinguish the two.

The guidance for picking an implicit signal is to measure something that demonstrably correlates with the outcome that actually matters, not whatever is easiest to instrument — Copilot chose acceptance rate specifically because, among the implicit signals available, it correlated most highly with independently measured user productivity gains. For a scheduling assistant, a concrete outcome like successfully created calendar events (plus how often users later edit those event details) is preferable to an ambiguous proxy like session length. This is the same discipline as [actionable metrics vs. vanity metrics](actionable-vs-vanity-metrics.md) — a metric earns a prominent role only if it actually predicts the thing you care about, not because it was convenient to log.
