---
type: concept
title: Efficiency Investment vs. Resource Cost
description: Deciding whether to pay for more capacity or pay engineering time to make the existing capacity more efficient is a cost trade-off that should be made explicitly, using per-stage cost visibility even when the SLO is end-to-end.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 13"
---

Meeting growing demand has two competing levers: buy more capacity (more machines, more storage, more bandwidth) or invest engineering effort to make the existing capacity handle more load per unit (algorithmic improvements, reduced redundant work, better resource utilization). Neither lever is free, and the right choice depends on weighing the ongoing resource cost of *not* investing against the one-time (or ongoing) engineering cost of an efficiency project. Over-provisioning to avoid this trade-off entirely just for peak load defers the cost rather than avoiding it — capacity provisioned for a peak sits unused, and paid for, the rest of the time.

## Making the Trade-Off Visible

This trade-off can't be made well without knowing where the cost actually comes from:

*   **Forecast growth first.** The size of the trade-off scales with expected future demand — an efficiency investment that doesn't pay back before demand outgrows it again isn't worth making yet; one that will keep paying back for years is worth prioritizing sooner.
*   **Measure cost per stage, even when the SLO is end-to-end.** An end-to-end latency or freshness SLO can be met while one internal stage is silently getting far more expensive per unit of work — without per-stage cost visibility, a sudden jump in a specific component's resource usage has no obvious owner to trace it back to or justify fixing.

This trade-off is about [efficiency](utilization-vs-efficiency.md) — value produced per unit of cost — not [utilization](utilization-law.md) on its own; a system can already be running at high utilization and still be a good candidate for efficiency investment if the busy capacity is producing comparatively little value per unit of cost.

## Relationship to Utilization Targets

This is the cost-accounting counterpart to the [utilization vs. latency trade-off](mm1-queue-model.md): running closer to full utilization is cheaper per unit of work but risks latency blowup under variance, while running with more [headroom](capacity-headroom-safety-margin.md) costs more per unit of work but buys latency safety margin. Efficiency investment shifts that curve — it lets the system do more useful work at the same utilization and the same latency risk, rather than trading one for the other — which is why it's often the better lever once headroom has already been tuned to its target and demand keeps growing.

## Practical Levers

Two concrete places to apply this trade-off: choosing among [compute purchasing models](compute-purchasing-model-spectrum.md) that trade idle-capacity cost against engineering effort and operational flexibility, and working through a [squeeze-optimize-migrate](fleet-rightsizing-squeeze-optimize-migrate.md) sequence that exhausts cheap configuration-level savings before spending effort on code or architecture changes. None of this addresses waste that isn't a sizing decision at all — capacity left running after it stopped being needed — which is a separate problem best solved by [automated waste elimination](automated-cloud-cost-waste-elimination.md) rather than by re-tuning a sizing trade-off.
