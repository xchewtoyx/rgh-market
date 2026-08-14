---
type: concept
title: Self-Similar Traffic and Buffer Sizing
description: Network and request traffic that is bursty at every time scale (long-range-dependent) violates the independent-arrivals assumption behind conventional queueing-based buffer sizing, and can drive unbounded queue growth at surprisingly low average utilization.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 10"
---

Conventional buffer/queue sizing (e.g. via [the M/M/1 queue model](mm1-queue-model.md)) assumes arrivals are statistically independent (a Poisson process) — under that assumption, expected queue length is a clean function of utilization alone, $Q = \rho/(1-\rho)$, blowing up only as utilization approaches 100%.

Real network and request traffic frequently isn't independent in this way — it is **self-similar / long-range-dependent (LRD)**: traffic looks equally bursty whether you look at it over 100 seconds, 1 second, or 0.1 seconds, rather than smoothing out into a steady average at any zoomed-in scale the way independent arrivals would. This bursty, clustered structure produces long "trains" of back-to-back arrivals that a Poisson-based buffer estimate doesn't anticipate.

## Why This Breaks Conventional Sizing

The severity of LRD is characterized by the **Hurst parameter H**. At H=0.5, traffic behaves like the conventional independent-arrivals case and standard queueing formulas apply unchanged. As H increases toward 1 (stronger long-range correlation), a generalized queue-length model shows buffer occupancy can grow **unbounded at intermediate — not just near-100% — average utilization**. This is the counterintuitive core finding: a link or buffer sized using conventional utilization-based rules of thumb, and running at a comfortable-looking average utilization, can still overflow because of correlation structure the sizing model never accounted for, not because average load was too high.

## A Later Complication: Where the Correlation Actually Comes From

Follow-up measurement work found something that reframes the practical risk: in at least one detailed study, packet *arrivals into* a server were confirmed genuinely Poisson (uncorrelated), while the LRD/self-similar signature only appeared in *outbound* packetization — generated internally by the OS/network-stack packetization process itself, not by the arrival pattern of client requests. This suggests LRD effects are often more localized (specific to how a given stack fragments and emits traffic) than a backbone-wide phenomenon, and that observed real-world buffer overflows are more commonly explained by conventional causes (e.g., a denial-of-service flood saturating a listen queue — see [socket backlog queues](socket-backlog-queues.md)) than by fractal traffic correlation.

## Practical Takeaway

Don't treat a comfortable average-utilization number as sufficient evidence that a buffer or queue is safely sized if the traffic feeding it is known to be bursty/correlated rather than independent — burstiness at every observed time scale is itself a risk signal independent of the average. At the same time, don't over-invest in exotic LRD-aware sizing formulas by default: measure the actual traffic's burstiness first, and treat conventional listen-queue exhaustion and thundering-herd-style causes (see [synchronized retry storm](synchronized-retry-storm.md)) as the more common real-world explanation before reaching for a fractal traffic model.
