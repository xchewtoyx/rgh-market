---
type: concept
title: Outcome-Completion Rate as a UX Proxy
description: Rather than guessing at user happiness from a technical metric, instrument the paired start/end events of an intended user action and track what fraction of attempts actually complete — this ties directly to two correlatable events plus rich client-only context, and surfaces bugs invisible to any backend-only signal.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 19"
---

Detecting a technical anomaly first and then guessing at its user impact gets the order of operations backwards. A more reliable approach: **detect user impact first, then investigate the technical cause.** The concrete technique is to instrument a user's *intention* and its *outcome* as a paired pair of events (e.g. `start_checkout` / `end_checkout`) and track **intention → outcome completion rate** (completed checkouts / checkout attempts) as a direct proxy for user happiness, rather than relying on a vague "happiness score" or on a technical metric like latency that may not actually track user experience.

This pairing is powerful because the client can attach rich contextual metadata that only it observes — session ID, app version, previous screen, payment type — which is invisible to backend-only telemetry. A real-world investigation using this technique (a food-delivery app's checkout-completion drop) surfaced multiple categories of bug that never showed up in aggregate technical metrics: an unlogged UI rendering bug, a discount-code format bug that silently disabled the submit button, and several small independent glitches whose *cumulative* effect degraded conversion even though none individually moved any top-line metric.

This is especially important on mobile/frontend because [percentile aggregates can be misleading when the underlying population is heterogeneous](percentile-aggregates-misleading-with-heterogeneous-population.md) — a completion-rate proxy tied to a specific user action doesn't have that weakness, since it's directly measuring the thing that matters rather than a technical proxy for it.
