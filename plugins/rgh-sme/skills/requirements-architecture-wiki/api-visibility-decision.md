---
type: concept
title: API Visibility Decision
description: >
  Choosing where an API may be reached from — public Internet, a
  restricted community network, or solution-internal only — is an
  architectural decision whose forces span organization, security,
  workload, and lifecycle funding.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

API visibility answers: from where may clients call this API — the open
Web, an access-controlled extranet/intranet, or only the data center or
logical layer hosting the solution? Deployment topology and network
connections constrain the technical options, but the choice is primarily
organizational: which end-user population the API serves, who funds
ongoing operations, and how predictable the workload is. Those forces
directly shape [non-functional requirements](non-functional-requirement.md)
— performance, scalability, and security — that belong in the
[architectural decision record](architectural-decision-capture.md).

Three recurring visibility patterns give a shared vocabulary for the
decision and its trade-offs (see [pattern-language documentation
format](pattern-language-documentation-format.md)):

- **Public API** — unlimited or unknown clients, globally distributed;
  highest peak-load and security demands; often needs explicit funding for
  operations beyond initial build (subscriptions, per-call pricing, or
  cross-funding).
- **Community API** — a closed group spanning multiple legal entities;
  deployed in a restricted network; stakeholder concerns are more diverse
  than for a public API because the provider cannot unilaterally set
  standards; lifecycle commitments (e.g., keeping a version in operation
  for paying customers) are often contractual.
- **Solution-internal API** — access limited to components of one
  application; budget and lifecycle usually sit with a single project or
  product; workloads tend to be more predictable unless traffic is
  forwarded from a public-facing API.

A solution-internal API that graduates to community or public visibility
should be a conscious [architecturally significant
decision](architecturally-significant-decision.md), not scope creep —
security, funding, and workload assumptions all change. Message and data
structure visibility is part of the same decision: client and provider
need a shared understanding of exchanged structures (in domain-driven
design terms, part of the published language), which aids developer
experience but introduces coupling that [interface
documentation](interface-documentation.md) must make explicit.
