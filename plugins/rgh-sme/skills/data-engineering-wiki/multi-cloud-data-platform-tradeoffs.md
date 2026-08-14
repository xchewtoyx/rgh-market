---
type: concept
title: Multi-Cloud Data Platform Trade-Offs
description: >
  Why running pipelines and storage across more than one cloud provider is
  usually driven by data sovereignty rather than cost or resilience, and the
  concrete pipeline costs that decision carries.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 16"
---

Running data infrastructure across more than one cloud provider, rather than
standardizing on one, is a real architectural choice with a narrower
legitimate justification than it's often given credit for. The strongest
concrete driver is **data sovereignty**: when a region requires data to be
stored and processed within its borders and the organization's primary
cloud provider has no datacenter there, routing that region's pipelines and
storage through a second provider that does is a genuine, compliance-driven
reason to run multi-cloud rather than a matter of preference.

**The costs a data engineer actually pays for multi-cloud are concrete, not
abstract:**

- Clouds aren't built to interoperate. Moving data or running compute across
  a provider boundary is slower and more brittle than doing the same within
  one provider's network, and products from different providers frequently
  don't integrate cleanly even when both claim to support "standard"
  interfaces.
- **Egress fees** apply specifically to data leaving one cloud for another —
  a cost that doesn't exist for equivalent movement within a single
  provider's network, and one that scales with exactly the kind of
  cross-region [data movement](data-federation-and-virtualization.md) a
  multi-region pipeline needs to do routinely.
- Portable, cross-cloud infrastructure generally has to be built on IaaS
  rather than PaaS to stay provider-agnostic, giving up the operational
  benefits [PaaS buys for a single-cloud deployment](oss-vs-managed-platform-choice.md)
  — this is a real opportunity cost, not a one-time migration tax.
- Every additional provider duplicates network backbone investment,
  security policy administration, monitoring, and billing — real recurring
  operational overhead per provider, not a one-time setup cost.

**Two commonly cited benefits don't hold up as reasons on their own:**
pricing leverage between competing providers is largely a myth, since
volume-based and reserved-capacity discounts scale with commitment to a
*single* provider, so splitting spend across two providers usually costs
more overall than consolidating it; and outage protection is better achieved
by failing over to a different region within the same provider than by
standing up a second provider, since a provider's own regions are already
designed to fail independently of each other.

**The practical takeaway for pipeline design**: default to one cloud
provider, and bring in a second only for the specific regions or workloads
where a concrete, named constraint — data sovereignty being the clearest
one — actually requires it, rather than adopting multi-cloud as a
platform-wide default. Where it is required, scope it narrowly (the
specific region's ingestion and storage) instead of trying to make every
component of the platform portable across both providers.
