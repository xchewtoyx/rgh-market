---
type: concept
title: Change Approval Board Pathology
description: >
  External change approval boards (CABs) correlate negatively with delivery
  tempo and show no measurable improvement to stability, making them a net
  cost rather than a risk-reduction mechanism.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 1"
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 7"
---

# Change Approval Board Pathology

DORA research found that the presence of a formal external change approval
board (CAB) — a body separate from the team, reviewing changes before they
reach production — does not predict higher stability or lower risk. In fact:

| Change approval method | Correlation with tempo | Correlation with stability |
| :--- | :--- | :--- |
| External CAB / manager approval | Strong negative (slows lead time and deploys) | Zero (no effect on change fail rate or MTTR) |
| High-risk-only approval | None | None |
| Peer review | Strong positive | Strong positive |
| No approval process | Positive | Neutral |

External CABs fail because they inspect changes without the intimate
contextual knowledge of system internals that the authoring team has. They
function as **risk management theater**: a compliance checkbox that exists
to shift blame after a failure, while adding to
[lead time for changes](lead-time-for-changes.md) and handoff delays that a
purely local, contextual review does not incur — without moving
[change failure rate](change-failure-rate.md) at all.

This is one of the strongest quantified findings behind the case for
replacing CABs with [peer review as change control](peer-review-as-change-control.md).
