---
type: concept
title: Chronic Unease
description: The organizational state of maintaining constant vigilance, welcoming doubt, and actively looking for signs of systemic drift in operations.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 5"
  - title: "Drift into Failure"
    resource: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems (Sidney Dekker), ch. 1-2"
---

**Chronic Unease** is a core organizational trait of High-Reliability Organizations (HROs). It is the psychological state of resisting complacency and refusing to accept past success as a guarantee of future safety. 

Key attributes of chronic unease:
* **Distrusting Success**: Interpreting a long period without incidents not as a sign of safety, but as a period of accumulating latent risks.
* **Reluctance to Simplify**: Resisting simple explanations for anomalies and seeking the messy operational details instead.
* **Sensitivity to Operations**: Maintaining active leadership presence at the sharp end to hear "bad news" and operational constraints directly from practitioners.
* **Welcoming Doubt**: Encouraging minority viewpoints and formalizing roles with the authority to challenge safety assumptions.

Chronic unease helps organizations detect [practical drift](practical-drift.md) before safety margins are fully eroded. It requires looking beyond reported safety metrics to avoid [survivorship bias in safety](survivorship-bias-in-safety.md).

### Why incident trends alone can't be trusted to reveal drift

A specific reason "distrusting success" matters: drift changes what counts
as an incident in the first place. As a risky practice gets normalized in
small steps, the same underlying deviance stops generating incident reports
at all — a check interval that would have been flagged as a lapse years
earlier becomes, after enough incremental extensions, the approved standard
practice, so nothing gets reported even though the underlying risk never
went away. This is the empirical basis for treating incident/near-miss
counts as a weak, lagging signal: in mature complex systems, accidents tend
to emerge from the accumulation of ordinary, successful, unremarkable
work — not from a legible trail of near-misses that a reporting system would
have caught. Practically, this means chronic unease requires periodically
studying *normal*, successful operations directly (not just triaging
reported incidents) to see whether the boundary of accepted practice has
quietly moved.
