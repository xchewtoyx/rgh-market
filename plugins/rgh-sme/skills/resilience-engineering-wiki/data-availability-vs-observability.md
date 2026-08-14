---
type: concept
title: Data Availability vs Data Observability
description: >
  Information being physically present in the system is not the same as
  information being perceivable by the operator given displays, workload,
  lighting, and attentional focus.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 3"
---

- **Availability**: the information was physically present somewhere in the
  system — a parameter was recorded, an indication existed on some page of
  some display.
- **Observability**: the information was actually perceivable by this
  operator at this moment, given display design, active workload, lighting,
  and where attention was legitimately directed.

Investigations routinely establish availability and then reason as if they
had established observability: "the data was right there in front of them".
That inference is invalid — availability is a property of the system,
observability a property of the situated human-system ensemble. The gap
between the two is often precisely the finding: the system made critical
data available in a form or place where it could not compete for attention
(a design fact for which the [blunt end](sharp-end-and-blunt-end.md) is
responsible).

Uses:

- When reconstructing the [inside-the-tunnel
  view](local-rationality-principle.md), overlay process parameters with the
  operator's goal states, active tasks, and what each display actually
  annunciated — not with what the flight recorder knew.
- "They should have seen it" claims are
  [counterfactuals](counterfactual-reasoning.md) built on availability;
  demand the observability analysis instead.
- The distinction operationalises part of what pseudo-labels like ["loss of
  situation awareness"](complacency-and-loss-of-situation-awareness.md)
  paper over: attention was somewhere, for reasons, and the un-perceived
  data had specific perceptual and workload obstacles.
