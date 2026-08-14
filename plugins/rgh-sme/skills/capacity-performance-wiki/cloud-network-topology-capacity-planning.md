---
type: concept
title: Cloud Network Topology and Egress Cost Planning
description: Bandwidth, latency, and cost between two cloud resources depend heavily on whether they sit in the same availability zone, the same region, or different regions, so placement is a capacity and cost lever independent of instance sizing.
sources:
  - title: "Fundamentals of Data Engineering"
    resource: "Fundamentals of Data Engineering (Joe Reis, Matt Housley), appendix B"
---

Public clouds expose a resource hierarchy — availability zones grouped into regions — that has direct capacity and cost consequences, separate from how large or numerous the compute/storage resources themselves are. Traffic within a single availability zone gets the highest bandwidth and lowest latency; traffic crossing zones within a region is still fast but strictly worse and typically carries a small egress charge; traffic crossing regions is slower again and usually carries a larger egress charge. A high-throughput workload — a large ephemeral processing cluster, a tightly-coupled distributed job — should be placed to run within a single zone whenever possible, for both the performance and the cost reasons at once, since crossing zone or region boundaries pays the same [bandwidth-delay product](bandwidth-delay-product.md) cost as any other network hop, on top of the metered egress fee.

## Egress Fees as a Structural Cost, Not Just a Line Item

Cloud providers generally charge for outbound data leaving a zone, region, or the provider's network entirely, while inbound traffic is free — an asymmetric pricing structure that functions as a retention mechanism (data is cheap to bring in, costly to move out or use elsewhere) as much as a genuine cost-recovery mechanism. This makes egress a capacity-planning variable that has to be modeled explicitly for any architecture that moves meaningful data volume across zone, region, or provider boundaries — a workload that looks cheap based on compute and storage pricing alone can have its total cost dominated by egress once cross-boundary data movement is accounted for. A direct network connection between an organization's own network and a cloud region (rather than routing over the public internet) can cut egress pricing by a large multiple, making it worth evaluating for any workload with sustained cross-boundary transfer volume.

## Mitigations

*   **Co-locate resources that talk to each other frequently or in bulk**, keeping same-zone traffic wherever the workload's fault-tolerance requirements allow it — this is the same [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) trade-off in a different guise: spreading a workload across zones/regions buys availability, at a direct bandwidth-cost and latency-cost price that must be weighed against the availability gained.
*   **Use a CDN for data served repeatedly to many geographically distributed consumers** rather than serving it directly from one region — this trades a per-region caching cost for eliminating repeated cross-region egress on the same data, the same [cache hit ratio economics](cache-hit-ratio-economics.md) calculation applied to network egress specifically rather than compute.
*   **Treat cross-boundary data movement as a first-class quantity in capacity forecasts**, not an incidental side effect of compute sizing — a design that fans data out across multiple regions for redundancy or locality needs its egress volume modeled with the same rigor as its compute and storage footprint, since it scales with data movement patterns that don't necessarily track compute or storage growth at all.

Because egress pricing is set by the provider rather than by physical necessity, it is also one of the more volatile inputs to a long-range capacity or cost model — a pricing change from a provider can shift the economics of a multi-region or multi-cloud architecture significantly without any change to the workload itself, which is a reason to revisit cross-boundary architecture decisions periodically rather than treating them as settled once made.
