---
type: concept
title: Telemetry Quality Failure Modes
description: Degraded telemetry is worse than absent telemetry in a specific way — lossy, laggy, unpredictable, or wrong signals create false confidence and teach the wrong lessons, whereas telemetry that's simply missing at least makes the blind spot obvious.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 24"
---

Telemetry can fail in more ways than simply "not existing," and the partial failure modes are often more dangerous than an honest gap, because they create false confidence rather than an obvious blind spot:

- **Lossy** — you see only part of what actually happened (e.g. a sample rate that drops the events that mattered most).
- **Laggy** — the signal arrives, but too late to act on before the consequences have already played out.
- **Unpredictable** — sometimes present, sometimes not, for reasons that aren't clear; this specifically erodes trust, since engineers stop being able to rely on the signal being there when they need it.
- **Wrong** — false positives or false negatives; the telemetry actively misleads rather than merely under-informing.
- **Missing entirely** — an open loop, nobody is even looking at this dimension.

All five are self-reinforcing once they take hold: bad feedback teaches the wrong lessons about what's actually going on, erodes trust in the ability to safely investigate or change the system, and tends to produce compensating rituals (excess caution, manual double-checking, distrust of dashboards) that don't actually fix the underlying signal problem. When diagnosing why an observability setup "isn't working," it's worth explicitly asking which of these five failure modes is actually present — "we have no telemetry for X" and "we have telemetry for X but it's laggy" call for different fixes, and conflating them leads to fixing the wrong thing. See [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md) for a related but distinct question — this note is about diagnosing *why* existing telemetry is untrustworthy, that one is about identifying what telemetry doesn't exist yet at all.

The mature response to a "wrong" or "unpredictable" signal is not to discard it wholesale — see [calibrated trust in known instrument lies](calibrated-trust-in-known-instrument-lies.md) for scoping distrust to the specific, named condition under which a signal misbehaves, so it stays useful everywhere else. When diagnosing a "wrong" signal specifically, [distinguishing systemic from random error](systemic-vs-random-error-in-telemetry.md) determines whether the fix is more data or a pipeline bug hunt — the two error types need opposite remedies.
