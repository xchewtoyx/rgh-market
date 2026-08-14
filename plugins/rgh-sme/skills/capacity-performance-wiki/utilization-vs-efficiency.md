---
type: concept
title: Utilization vs. Efficiency
description: Utilization measures how much of paid-for capacity is busy; efficiency measures how much value that busy capacity produces per unit of cost — a system can raise one while leaving the other flat or worse, so tracking only utilization misses whether the resource is being used well, not just used.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 7"
---

**Utilization** is the portion of paid-for compute resources actually in use — the converse of wastefulness. **Efficiency** is a different ratio entirely: value produced divided by cost. The two are easy to conflate but measure different things — a workload can run at high utilization (every core busy) while producing very little value per unit of that busy time, if the work itself is poorly targeted or wastefully structured. Raising utilization alone doesn't guarantee raising efficiency; a system needs both measured separately to know whether "using more of what's paid for" is actually the same as "getting more value per dollar."

## Two Ways to Measure the Cost Side

*   **Money-indexed cost** (dollars spent): the measure that ultimately matters for the business, but it moves for reasons that have nothing to do with the system itself — a cloud provider raising GPU prices changes money-indexed efficiency without any change to how the system runs, which makes it a noisy signal for deciding *what to fix*.
*   **Resource-indexed cost** (a constant unit like CPU-seconds or GPU-seconds, using whichever resource is most expensive or most constrained): immediately reflects an actual system-level efficiency change, isolated from external pricing swings. This is the better signal for identifying and validating improvement work; money-indexed cost is the better signal for reporting business impact once a project is done.

## Two Granularities for the Value Side

*   **Per-unit-of-work value** (e.g., examples processed per GPU-second): a proxy metric that avoids needing to know or agree on what the work is actually worth, making it cheap to compute and compare across changes to the same workload.
*   **Overall program value**: value across an entire effort — staff time, experimentation, and production operation combined — measured over a longer horizon (months, not requests) and ideally tied to an organizational outcome the business actually cares about. This is harder to compute and slower to move, but it's the number that answers whether the whole effort is worth its cost, not just whether one component got cheaper per unit.

## Why This Distinction Matters for Capacity Decisions

An organization that tracks only utilization can convince itself a system is well-run because nothing sits idle, while actually wasting resource-indexed cost on low-value work that happens to keep every core busy. Conversely, a system with headroom (deliberately under-utilized, e.g. for [capacity headroom safety margin](capacity-headroom-safety-margin.md) or fast recovery) is not automatically inefficient — it may be spending that idle capacity on exactly the insurance it was provisioned for. Treating utilization as a proxy for efficiency skips the actual question — value per unit of cost — in favor of an easier number that happens to correlate with it only some of the time. Without *some* efficiency measure, however imperfect, an organization has no basis for prioritizing engineering time between [efficiency investment and just buying more resource cost](efficiency-investment-vs-resource-cost.md) — an imperfect, improvable efficiency metric beats optimizing on utilization alone.
