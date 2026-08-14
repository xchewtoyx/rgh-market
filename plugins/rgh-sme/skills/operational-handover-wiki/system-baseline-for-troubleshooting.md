---
type: concept
title: System Baseline for Troubleshooting
description: A new operator must know what a system's normal behavior looks like before they can recognize what's abnormal, and must calibrate how rare a cause is likely to be given the system's scale and age.
sources:
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 15"
---

Debugging and troubleshooting a system you didn't build requires two kinds of calibration that an operator new to a system usually lacks and that a handover should deliberately transfer.

## Know what's normal

Unfamiliar operators often start debugging behavior that is actually expected — a routine `abort` call at the end of shutdown, a client's known background probes, a steady rate of harmless errors that has always been present. Mistaking routine behavior for a symptom wastes investigation time and can send a new operator down the wrong path during a live incident.

The fix is to establish (and hand over) a baseline of what the system's metrics, logs, and error rates look like when nothing is wrong, so a deviation is recognizable as a deviation. When a baseline wasn't captured in advance, historical logs from before a problem began can often reconstruct one after the fact.

A related trap is **normalized deviance**: a bug or degraded state that has been present so long everyone stopped noticing it and started treating it as the expected baseline (e.g., accepting a large fixed memory-fragmentation loss as "just how the system runs"). Rotating people through on-call, and asking newcomers what looks strange to them before they're told what's "normal," surfaces deviance that veteran operators have stopped seeing — the same mechanism as [The Author's Blind Spot for Complexity](authors-blind-spot-for-complexity.md), applied to system behavior rather than documentation.

## Calibrate rarity to system maturity ("horses vs. zebras")

When you hear hoofbeats, think horses, not zebras — most causes are common ones. But this heuristic is scale- and age-dependent: as a system's operators eliminate the common bugs over time, and as a system runs at greater scale, rare ("zebra") causes become proportionally more frequent among the problems that remain. A single-machine bit-flip is astronomically unlikely on any one server, but becomes a near-daily occurrence across a fleet of hundreds of thousands of memory chips.

The operational implication for handover: tell incoming operators where the system currently sits on this spectrum. A new, small, or recently-changed system should make an operator suspect ordinary causes first. An old, large, heavily-hardened system has usually already had its "horses" found and fixed, so operators should expect to be dealing disproportionately with rare interactions — and should not assume a strange symptom is user error just because it seems too unusual to be real.

Once a deviation from baseline is confirmed, [decision tables and trees](decision-tables-for-branching-diagnostics.md) help an operator navigate the space of possible causes without missing a combination the diagnostic should have accounted for.
